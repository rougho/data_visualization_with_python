from random import randint
import plotly.express as px


'''Class'''
class Die:
    def __init__(self, sides = 6):
        self.sides = sides
    
    def roll(self):
        return randint(1, self.sides)
    


'''Main'''
#instance of the dice
dice = Die()

#roll the dice
result = []
for roll in range(1000):
    num = dice.roll()
    result.append(num)

#frequency
frequencies = []
poss_results = range(1, dice.sides+1)
for value in poss_results:
    frequency = result.count(value)
    frequencies.append(frequency)

#histogram
print(frequencies)
fig = px.bar(x=poss_results, y=frequencies)
fig.show()