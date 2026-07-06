import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv("WHO-COVID-19-global-data.csv")

data["DateReported"] = pd.to_datetime(data["DateReported"])


x = data.groupby("DateReported").sum(numeric_only=True)

graf = go.Figure()

graf.add_trace(go.Scatter(
    x=x.index,
    y=x["Cumulative_cases"],
    mode="lines",
    name="Cumulative Cases"
))

graf1 = go.Figure()

graf1.add_trace(go.Scatter(
    x=x.index,
    y=x["New_cases"],
    mode="lines",
    name="New Cases"
))
graf1.write_html("Graf1.html",auto_open=True)
graf.write_html("Graf.html", auto_open=True)