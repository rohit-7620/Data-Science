import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Load a subset of the Titanic dataset online
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url).dropna(subset=['Age'])

# Simple Feature Selection: Fare and Age
X = df[['Fare', 'Age']]
y = df['Survived']

# Train the model
model = LogisticRegression().fit(X, y)

# Save the model to a file
joblib.dump(model, 'titanic_model.pkl')
print("Model built and saved!")
