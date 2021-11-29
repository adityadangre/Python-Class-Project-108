import random 
import plotly.express as px
import plotly.figure_factory as ff


sum = []
count = []

for i in range(100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sum.append(dice1+dice2)
    count.append(i)

fig = ff.create_distplot([sum], ["Count"])
fig.show()
