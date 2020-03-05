import os
import mlflow

if __name__ == "__main__":
    mlflow.set_tracking_uri('http://localhost:5000')
    # Log a parameter (key-value pair)
    mlflow.log_param("param1", 5)

    # Log a metric; metrics can be updated throughout the run
    mlflow.log_metric("foo", 1)
    mlflow.log_metric("foo", 2)
    mlflow.log_metric("foo", 3)

    # Log an artifact (output file)
    with open("output.txt", "w") as f:
        f.write("Hello world!")
    mlflow.log_artifact("output.txt")