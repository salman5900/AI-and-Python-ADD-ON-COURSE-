import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Gender': ['F', 'M', 'M'],
    'Age': [25, 30, 35],
    'Score': [85.5, 90.0, 88.5]
}

df = pd.DataFrame(data)
df.to_csv('Ai/import Libraries/output.csv', index=False)
print(df.head())



