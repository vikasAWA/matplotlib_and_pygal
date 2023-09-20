import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(100000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    
    # Set the size of the plotting window
    plt.figure(dpi=128, figsize=(10, 6))

    plt.scatter(rw.x_values, rw.y_values, edgecolors='none', c=point_numbers, cmap=plt.cm.Blues, s=1)
    
    #Emphasize the first and last points 
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    
    # Hide the axes
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
    
    plt.savefig('random_walk.png')
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

