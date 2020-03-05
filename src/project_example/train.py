import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import sys
import warnings
warnings.filterwarnings('ignore')

# Function to validate a model        
def validate_model(model, x_test, y_test):    
    y_pred = model.predict(x_test)
    y_pred = (y_pred > 0.5)
    from sklearn.metrics import confusion_matrix
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    accuracy = (tp + tn) / (tp + fp + tn + fn)
    
    return precision, recall, accuracy
    

def breast_cancer_rf(n_estimators=100, max_depth=2, criterion="gini"):
    from sklearn.ensemble import RandomForestClassifier
    import mlflow.sklearn
    with mlflow.start_run() as run:
        clf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, criterion=criterion)
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_param("criterion", criterion)
        mlflow.set_tag("model type", "sklearn - RandomForest")
        clf.fit(x_train, y_train)
        precision, recall, accuracy = validate_model(clf, x_test, y_test)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.sklearn.log_model(clf, "model")
        print("Model saved in run %s" % mlflow.active_run().info.run_uuid)


if __name__ == "__main__":
	args = sys.argv[1:]
	n_estimators = int(args[0])
	max_depth = int(args[1])
	criterion = args[2]

	cancer = load_breast_cancer()
	X = np.array(cancer.data)
	y = np.array(cancer.target)

	#Feature Scaling
	x_train, x_test, y_train, y_test = train_test_split(X, y, train_size=426, test_size=143, random_state=0)
	sc = StandardScaler()
	x_train = sc.fit_transform(x_train)
	x_test = sc.transform(x_test)

	breast_cancer_rf(n_estimators=n_estimators, max_depth=max_depth, criterion=criterion)