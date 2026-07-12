import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, edgecolor='none', s=10) #edgecolors=[]/'none'

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)

# Set the range for each axis
plt.xlim(0, 1100)
plt.ylim(0, 1100000)

# plt.axis('tight')
# plt.autoscale()

plt.show()