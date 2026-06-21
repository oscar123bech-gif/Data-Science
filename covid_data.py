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

graff = px.scatter(top10cases,x="Confirmed",y=top10cases.index,size="Confirmed",size_max=100,color=top10cases.index)

graff.show()

least10cases = csv.groupby("Country_Region")["Recovered"].sum().sort_values(ascending=True).head(10)
print(least10cases)

graff = px.scatter(least10cases,x="Recovered",y=least10cases.index,size="Recovered",size_max=100,color=least10cases.index)

graff.show()

top10active = csv.groupby("Country_Region")["Active"].sum().sort_values(ascending=False).head(10)

graff = px.scatter(top10active,x = "Active",y = top10active.index,size="Active",size_max=100,color=top10active.index)
graff.show()

graff = px.bar(top10active,x = top10active.index,y = "Active",height=500,color="Active",color_continuous_scale=["Green","Red"])
graff.show()

Rowsinus = csv["Country_Region"] == "US"
print(Rowsinus)