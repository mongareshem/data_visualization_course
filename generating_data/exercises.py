import matplotlib.pyplot as plt

input_values = list(range(1, 5001))
outputs = [x**3 for x in input_values]

plt.plot(input_values, outputs, linewidth=3, color='turquoise')

plt.title('Cube Numbers',
          fontdict={'family':'Serif', 'fontsize':30, 'fontweight': 'normal', 'fontstyle': 'italic'})
plt.xlabel('Values', fontsize=16)
plt.ylabel('Cube of Values', fontsize=16)
plt.tick_params(axis='both', labelsize=14)

plt.xlim(0, 6000)
plt.ylim(0, 150000000000)

plt.show()