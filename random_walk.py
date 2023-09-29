from random import choice
import matplotlib.pyplot as plt

class RandomWalk:
    def __init__(self,num_points = 5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]
    
    def get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_steps = self.get_step()
            y_steps = self.get_step()     

            if x_steps == 0 and y_steps == 0:
                continue

            x = self.x_values[-1] + x_steps
            y = self.y_values[-1] + y_steps

            self.x_values.append(x)
            self.y_values.append(y)     


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