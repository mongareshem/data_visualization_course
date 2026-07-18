import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
outputs = [x**3 for x in input_values]

plt.plot(input_values, outputs)
plt.show()