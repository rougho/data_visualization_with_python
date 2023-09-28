import matplotlib.pyplot as plt

squares = [1, 4, 9, 16 ,25]
input_values = [1, 2, 3, 4, 5]

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(input_values,squares, linewidth = 3)

ax.set_title("Squares Numbers", fontsize = 24)
ax.set_ylabel("Square of value")
ax.set_xlabel("Value")
ax.tick_params(labelsize = 14)
print(fig)

plt.show()