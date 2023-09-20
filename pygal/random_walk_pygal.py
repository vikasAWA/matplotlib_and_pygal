from random import choice 
import pygal
from pygal.style import Style

x_values = [0]
y_values = [0]

for _ in range(1000):
    x_values.append(x_values[-1] + choice([-1, 1])*choice([0,1, 2, 3, 4]))
    y_values.append(y_values[-1] + choice([-1, 1])*choice([0, 1, 2, 3, 4]))

point_numbers = list(range(1001))
    
custom_style = Style(
    colors=['#008000', '#FFFF00', '#FFA500', '#FF0000', '#800080'])

scatter_plot = pygal.XY(style=custom_style)
for x, y, value in zip(x_values, y_values, point_numbers):
    scatter_plot.add('Data', [(x, y)], stroke=False, fill=True, color=point_numbers)

scatter_plot.title = 'Scatter Plot Example'
scatter_plot.x_title = 'X-Axis Label'
scatter_plot.y_title = 'Y-Axis Label'
scatter_plot.render_to_file('rw_pygal.svg')