import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv("WHO-COVID-19-global-data.csv")

print(data)
data.info()

data["DateReported"] = pd.to_datetime(data["DateReported"])

data.info()

x = data.groupby("DateReported").sum()
print(x)

graf = go.Figure()
graf.add_trace(go.Scatter(x = x.index,y = x["New_deaths"]) )
graf.write_html("Graf.HTML",auto_open = True)