import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5_000)

    rw.fill_walk()

    plt.style.use('classic')
    fix, ax = plt.subplots(figsize=(16,9))

    point_numbers = range(rw.num_points)

    ax.plot(rw.x_values,rw.y_values,linewidth = 2)

    ax.set_aspect('equal')

    ax.plot(0, 0,c = 'green')
    ax.plot(rw.x_values[-1], rw.y_values[-1])
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    break
'''
    keep_visual = input("Make anoher visualization? (y/n): ")
    if keep_visual == 'n':
        print("closing ...")
        break
'''