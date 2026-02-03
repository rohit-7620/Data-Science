import joblib

# Load the saved model
model = joblib.load('titanic_model.pkl')

# Input: [Ticket Price, Person's Age]
# Let's test: Someone who paid $100 and is 25 years old
passenger = [[100, 25]]
result = model.predict(passenger)

status = "Survived" if result[0] == 1 else "Did not survive"
print(f"Prediction: {status}") 
