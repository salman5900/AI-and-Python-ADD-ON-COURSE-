import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# simple data [Hours Studied]
x = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1 ])  # 0: Fail, 1: Pass

# Train the model
model = LogisticRegression()
model.fit(x, y)

# Predict on training data
y_pred = model.predict(x)
accuracy_score = accuracy_score(y, y_pred)
print(f"Training Accuracy: {accuracy_score}")

# predict a new example
hours = 6.7
predicted = model.predict([[hours]])
probability = model.predict_proba([[hours]])[0][1]
print(f"Predicted outcome for studying {hours} hours: {'Pass' if predicted[0] == 1 else 'Fail'} with probability {probability:.2f}")

# Plotting
x_line = np.linspace(0, 10, 100).reshape(-1, 1)
y_line = model.predict_proba(x_line)[:, 1]
plt.scatter(x, y, color='blue', label='Training Data')
plt.plot(x_line, y_line, color='red', label='Logistic Regression Curve')

# Mark the predicted point 
plt.plot(hours, probability, 'go', label=f'Prediction for {hours} hours')
plt.vlines(hours, 0, probability, colors='green', linestyles='dashed', alpha=0.6)
plt.hlines(probability, 0, hours, colors='green', linestyles='dashed', alpha=0.6)
plt.xlabel('Hours Studied')
plt.ylabel('Probability of Passing')
plt.title('Logistic Regression: Study Hours vs Pass Probability')
plt.legend()
plt.grid(True)
plt.show()