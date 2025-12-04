import pandas as pd

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Gender': ['F', 'M', 'M'],
#     'Age': [25, 30, 35],
#     'Score': [85.5, 90.0, 88.5]
# }

# df = pd.DataFrame(data)
# df.to_csv('import Libraries/output.csv', index=False)
# print(df.head())

# print("########################################")

# data2 = {
#     "Student": ['David', 'Eva', 'Frank', 'Grace', 'Hannah'],
#     "Age": [20, 21, 19, 22, 20],
#     "Marks": [88, 92, 85, 95, 90],
#     "Gender": ['M', 'F', 'M', 'F', 'F'],
#     "City": ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
# }

# df2 = pd.DataFrame(data2)
# df2.to_csv('import Libraries/output2.csv', index=False)
# print(df2.head())

# loading the file 
df = pd.read_csv("import Libraries/output2.csv")
print(df.head()) # display first 5 rows
print("########################################")
print(df.shape) # number of rows and columns
print(df.columns) # column names
print(df.dtypes) # data types of each column
print(df.tail()) # display last 5 rows
print("########################################")
print(df.describe()) # statistical summary
print("########################################")
print(df.isnull().sum()) # check for missing values
print("########################################")

# doing matplotlib with pandas
import matplotlib.pyplot as plt

plt.hist(df["Marks"])
plt.title("marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

df["Gender"].value_counts().plot(kind='bar')
plt.title("Gender Distribution")
plt.show()

# Bivariate Analysis
plt.scatter(df["Age"], df["Marks"])
plt.title("Age vs Marks")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.show()

# average marks of the city
print(df.groupby("City")["Marks"].mean())

