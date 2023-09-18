import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4]
y = [10, 15, 13, 18]


# Hide the axes
plt.axes().get_xaxis().set_visible(False)


# Create a scatter plot
plt.scatter(x, y)

# Display the plot
plt.show()
