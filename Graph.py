import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]

# Creating the plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label="Sample Line")

# Adding title and labels
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

# Display the plot
plt.show()