import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

# Training data
x = np.array([[1],[2],[3],[4]])
y = np.array([2, 4, 6, 8]) # Linear : y = 2*x

# Train model
model = LinearRegression()
model.fit(x, y)

# Predict for training data
y_train_pred = model.predict(x)

# predict for x = 5
x_new = np.array([[1.5]])
y_new=model.predict(x_new)

# accuracy(R^2 score)
r2 = r2_score(y, y_train_pred)

# Print results
print(f"Predicted value for x = 1.5: {y_new[0]}")
print(f"R^2 Score: {r2}")

# Plot 
x_line = np.linspace(1, 5, 100).reshape(-1,1)
y_line = model.predict(x_line)
plt.scatter(x, y, color='blue', label='Training Data')
plt.plot(x_line, y_line, color='red', label='Regression Line')
plt.scatter(x_new, y_new, color='green', label='Prediction for x=1.5')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression with Accurary and Prediction')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
