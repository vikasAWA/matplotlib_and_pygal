from die import Die
import pygal

die = Die()
result = [die.roll() for _ in range(1000)]

# Analyse the result
frequecies = []
for number in range(1, die.num_sides+1):
    frequecies.append(result.count(number))
    
print(frequecies)

hist = pygal.Bar()
hist.title = "Result of rolling one D6 1000 time"
hist.x_labels = list('123456')
hist.x_title = 'Results'
hist.y_title = "Frequency of Result"

hist.add('D6', frequecies)
hist.render_to_file('die_visual.svg')
    