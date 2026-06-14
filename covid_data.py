import pandas as pd
import plotly.express as px

csv = pd.read_csv("covid_data.csv")
print(csv.info())

top10deaths = csv.groupby("Country_Region")["Deaths"].sum().sort_values(ascending=False).head(10)
print(top10deaths)

graff = px.scatter(top10deaths,x="Deaths",y=top10deaths.index,size="Deaths",size_max=100,color=top10deaths.index)
graff.write_html("top10.html",auto_open=True)

graff.show()

top10cases = csv.groupby("Country_Region")["Confirmed"].sum().sort_values(ascending=False).head(10)
print(top10cases)