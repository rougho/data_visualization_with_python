import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(10_000_000)

    rw.fill_walk()

    plt.style.use('classic')
    fix, ax = plt.subplots(figsize=(16,9))

    point_numbers = range(rw.num_points)

    ax.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none', s=2)

    ax.set_aspect('equal')

    ax.scatter(0, 0,c = 'green' ,edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1],c='red', edgecolors='none', s=100)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_visual = input("Make anoher visualization? (y/n): ")
    if keep_visual == 'n':
        print("closing ...")
        break



