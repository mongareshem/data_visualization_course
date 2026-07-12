import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

plt.title("Square Numbers",
          fontdict={'family':'serif', 'fontsize':24, 'fontweight': 'bold'})

plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Values", fontsize=14)
plt.tick_params(axis='both',labelsize=14)
plt.plot(squares)
plt.show()