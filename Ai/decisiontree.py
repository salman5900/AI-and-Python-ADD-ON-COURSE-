from sklearn import tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


x = [
    [0, 1, 1], # <30 Yes,Excellent
    [0, 0, 1], # <30 No, Excellent
    [1, 1, 0], # 30-40 Yes, Fair
    [2, 0, 0], # >40 No, Fair
    [2, 0, 1], # >40 No, Excellent
    [1, 0, 1], # 30-40 No, Excellent
] 

y = ['Buy', 'Dont Buy', 'Buy', 'Buy', 'Dont Buy', 'Dont Buy']



# Train the model
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

# Predict a new Sample
sample = [[0, 1, 0]] # <30 Yes, Fair
prediction = clf.predict(sample)
print(f"Predicted decision for sample {sample} : {prediction}")

# Evaluate on training data
y_pred = clf.predict(x)
accuracy = accuracy_score(y, y_pred)
print(f"Training Accuracy: {accuracy}")

