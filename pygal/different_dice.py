from die import Die
import pygal

die1 = Die()
die2 = Die(num_sides=10)

result = [die1.roll() + die2.roll() for _ in range(50000)]
frequencies = []
max_result = die1.num_sides + die2.num_sides

for number in range(2, max_result+1):
    frequencies.append(result.count(number))
    
print(frequencies)
print(sum(frequencies))

hist = pygal.Bar()
hist.title = "Result of rolling D6 + D10 50000 times"
hist.x_labels = [f"{x}" for x in range(2, max_result+1)]
hist.x_title = 'Results'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D10', frequencies)
hist.render_to_file("different_dice_visual.svg")