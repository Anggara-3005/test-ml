import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassfier
from sklearn.metrics import accuracy_score
import joblib

df = pd.read_csv('winequality-red.csv')

X = df.drop('quality', axis=1)
y = df['quality']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy}")

with open("metrics.txt", "w") as f:
  f.write(f"Accuracy: {accuracy}\n")
  
# Save model
joblib.dump(model, "model.pkl")
