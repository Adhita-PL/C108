import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("c108data.csv")
height =  df["Weight(Pounds)"].tolist() 
fig = ff.create_distplot([height], ["Weight"], show_hist=False) 
fig.show() 