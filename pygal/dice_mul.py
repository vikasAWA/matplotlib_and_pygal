from die import Die
import pygal

die1 = Die()
die2 = Die()

result = [die1.roll()*die2.roll() for _ in range(1000)]

frequencies = []
for number in range(1, 37):
    frequencies.append(result.count(number))
    
hist = pygal.Bar()
hist.title = "Result of rolling two D6 1000 times"
hist.x_labels = list(range(1,37))
hist.x_title = 'Results'
hist.y_title = 'Frequency of Result'

hist.add('D6 * D6', frequencies)
hist.render_to_file('dice_mul_visual.svg')