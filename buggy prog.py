import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv(r"D:\Projects\PythonProjects\.venv\college progs\Iris.csv")  

X = data.drop(['Species'],axis=1)  

label_encoder = LabelEncoder() 
y = label_encoder.fit_transform(data['Species'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, train_size=0.6, random_state=42)  

model = XGBClassifier(max_depth=3, learning_rate=0.1, n_estimators=100)

model.fit(X_train, y_train)  

predictions = model.predict(X_test)  

accuracy = accuracy_score(y_test, predictions)  

print("Accuracy:", accuracy)
