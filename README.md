# MLOps - Neoland

This repo contains materials and code of the Neoland workshop **MLOps or how not to die to put models in production**.

Slides can be found in this repository with the following name [Neoland-MLops.pdf](Neoland-MLops.pdf).

## Contents

1. [Installation](#installation)
1. [Run MLFlow server](#run-mlflow-server)
1. [MLFlow Tracking demo](#mlflow-tracking-demo)
1. [MLFlow Projects demo](#mlflow-projects-demo)
1. [MLFlow Models demo](#mlflow-models-demo)

## Environment preparation

Configure your local machine to execute all the examples in your laptop.

1. First of all, please do install Anaconda in your machine

    * Windows version [here](https://repo.anaconda.com/archive/Anaconda3-2018.12-Windows-x86_64.exe).
    * Linux version [here](https://repo.anaconda.com/archive/Anaconda3-2018.12-Linux-x86_64.sh).
    * MacOS X version [here](https://repo.anaconda.com/archive/Anaconda3-2018.12-MacOSX-x86_64.pkg).

Anaconda is a free and open-source distribution of the Python and R languages. It makes easy the management of packages and their use. In addition, Anaconda comes with more than 1,500 packages as well as the *conda* package and virtual environment manager. 
> Note that Anaconda is suggested as package and virtual environment manager, but you can use other managers such as [venv](https://docs.python.org/3/library/venv.html) and [pip](https://pip.pypa.io/en/stable/). 

2. Once you have installed anaconda, now it is time to create a virtual environment with all the package necessaries:

```bash
> conda env create -n YOUR_ENV_NAME
```

3. Once the creation of the environment ends, the environment must be activated. The name of the environment is the one given by you, in case you want to activate it manually any other time. 

```bash
> conda activate YOUR_ENV_NAME
```

4. Install python inside the environment.

```bash
> conda install python=3.8
```

5. Install all the dependencies from the `requirements.txt` file.

```bash
> pip install -r src/requirements.txt
```
>Note that if you have problems try to install first the package libmysqlclient-dev by using the following command: `sudo apt-get install libmysqlclient-dev`

6. Once activated the virtual environment, you only have to run the Jupyter Notebook server.

```bash
> jupyter notebook
```
> Note that the server will be initiated but you need an IDE or a modern web browser to access the notebook server.

Finally, if you want to *install any other library* you could **activate the environment** in another command prompt and uses **conda** or **pip** to install the package you needed.

If you want to use an IDE tool, I recommend the use of [Visual Studio Code](https://code.visualstudio.com/) (VSCode) to develop and execute the different demos in this workshop.

1. Install **VSCode** from [here](https://code.visualstudio.com/)
2. Install the extensions [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
3. Connect to the local jupyter notebook server, using the URL given when opening the server. 
    1. Press in VSCode `Ctrl+Shift+P`
    2. Search for *"Python: Specify local or remote Jupyter server for connections"* and press enter.
    3. Paste the URL of the local server and you can execute your notebooks from VSCode.
    > Note that you can only connect with your local Jupyter server since the login is done by token and not user authentication.

> In order to create a blank notebook just hit `Ctrl+Shift+P` and search for *"Python: Create New blank Jupyter notebook"*.

## Run MLFlow server

In order to run the MLFlow server you should follow the next steps:

1. First of all, please install Docker in your machine

    * Windows version [here](https://docs.docker.com/docker-for-windows/install/).
    * Linux version [here](https://docs.docker.com/install/).
    * MacOS X version [here](https://docs.docker.com/docker-for-mac/).

2. Then the following command in order to start the server. Remember to configure first the `infra.yml` file before executing the 

```bash
> docker-compose -f './server/infra.yml' up --build -d
```
> Note that in case you want to shut down the server you should run the following command
    
```bash
> docker-compose -f './server/infra.yml' down
```

Finally, export the tracking uri server, `export MLFLOW_TRACKING_URI=http://localhost:5000`

## MLFlow Tracking demo
Run ``jupyter notebook`` and execute the notebook ``tracking.ipynb``.

## MLFlow Projects demo
The first example uses a public project located in the official MLFlow repository (https://github.com/mlflow/)

``mlflow run https://github.com/mlflow/mlflow-example.git -P alpha=5.0``

The second example uses our own project (./src/roject_example)

```bash
cd src/project_example
mlflow run . -P n_estimators=500
```

## MLFlow Models demo
Execute the notebook ``models.ipynb``.

The second part of the demo consist on deploying a trained model from the ``mlruns`` folder that MLFlow creates after tracking experiments.

So, it is necessary to navigate through the corresponding folder and execute the ``mlflow serve`` command.

```bash
cd mlruns/<selected experiment_id>/<selected run_id>/artifacts/model/
mlflow models serve -m . -p 1234
```

After some time, a gunicorn + Flask microservice is deployed on port 1234. It is possible to send http post request by means of programs like Postman. The endpoint is:

``localhost:1234/invocations``

And this is an example of valid body for the request:

```json
{
	"data": [[ 0.52444161,  0.97309661,  0.43247518,  0.38717859, -1.03377319,
       -0.73048166, -0.70972218, -0.41044243, -1.00047971, -0.82507126,
       -0.08818832, -0.04623819, -0.18209319, -0.0038316 , -1.04758402,
       -0.93257644, -0.65865037, -0.69601737, -0.71241416, -0.25530814,
        0.58767599,  1.36061943,  0.48167379,  0.44795641, -0.62887522,
       -0.64418546, -0.62375274, -0.23693879,  0.08147618,  0.05512114]]
}
```