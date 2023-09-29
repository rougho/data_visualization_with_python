from random import choice

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

    