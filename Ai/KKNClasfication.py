import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np


# Training data
x_train = np.array([
    [1, 2],
    [2, 3],
    [3, 3],
    [6, 5],
    [7, 7]
])

y_train = ['A', 'A', 'A', 'B', 'B']

x_test = np.array([[5, 5]])

# Train KNN model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)

#Predict 
prediction = knn.predict(x_test)[0]
print(f"Predicted class for {x_test[0]}: {prediction}")

