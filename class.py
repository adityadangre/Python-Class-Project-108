import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv('data.csv')
height = df['Height(Inches)'].tolist()
weight = df['Weight(Pounds)'].tolist()
fig = ff.create_distplot([weight], ['Weight (Pounds)'])
fig.show()