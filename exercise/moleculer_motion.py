import matplotlib.pyplot as plt
from random import choice

class RandomWalk():
    def __init__(self, num_points=5000):
        self.num_points = num_points
        
        self.x_values = [0]
        self.y_values = [0]
    
        
    def get_step(self):
            direction = choice([-1, 1])
            distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            step = direction*distance
            return step
             
        
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            # getting next points 
            if x_step == 0 and y_step == 0:
                continue
            
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)
 
while True:           
    molecule = RandomWalk(num_points=10000)
    molecule.fill_walk()
    point_numbers = list(range(molecule.num_points))
    plt.figure(dpi=128, figsize=(10,6))
    plt.scatter(molecule.x_values, molecule.y_values, s=5, edgecolors='none', c=point_numbers, cmap=plt.cm.Blues )
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.show()
    
    keep_running = input('Make another Random Walk? (y/n): ')
    if keep_running == 'n':
        break
            
