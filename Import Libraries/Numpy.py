import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Type:", type(arr))

a = np.array([1, 2, 3 ,6 ,7 ,8])
b = np.array([4, 5, 6, 9, 10, 11])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Exponentiation:", a ** 2)

# finding mean
print("Mean:",np.mean(a))
print("Medium:",np.median(b))

# using reshape to make 2D array

reshape1 = a.reshape(2, 3)
print("Reshaped Array:\n", reshape1)

reshape2 = b.reshape(3, 2)
print("Reshaped Array:\n", reshape2)


print("#######################################")

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix:\n", matrix)
print("shape:", matrix.shape)
print("Traspose:\n", matrix.T)

