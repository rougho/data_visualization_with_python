import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()

rw.fill_walk()

plt.style.use('classic')
fix, ax = plt.subplots()

ax.scatter(rw.x_values,rw.y_values, s=10)
ax.set_aspect('equal')

plt.show()
