import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,3,5,7,11]

# GRAHP
plt.plot(x, y)
plt.title("Sample Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# BAR
names = ["Sham", "Ram", "Pam", "Jam"]
scores = [85, 90, 75, 92]

plt.bar(names, scores)
plt.title("Scores Bar Chart")
plt.xlabel("Names")
plt.ylabel("Scores")
plt.show()

