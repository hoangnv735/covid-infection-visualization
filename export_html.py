import json
import os
import pandas as pd
import plotly.express as px

# provinces = json.load(open("vietnam.geojson", "r"))
os.makedirs("docs", exist_ok=True)
provinces = json.load(open("vietnam.simplified.geojson", "r"))
df = pd.read_csv("data.csv", header=0)
df["Total"] = df["Total"].apply(lambda x: int(str(x).replace(".", "")))
df["Death"] = df["Death"].apply(lambda x: int(str(x).replace(".", "")))

fig = px.choropleth(
    data_frame=df,
    geojson=provinces,
    featureidkey="properties.ten_tinh",
    locations="Province",
    color="Total",
    color_continuous_scale="Viridis",
    range_color=(0, df["Total"].max()),
    labels={"Total": "Infection Cases"},
    title="COVID-19 Total Infection Cases by Province in Vietnam",
)

fig.update_geos(fitbounds="locations", visible=False)
# fig.show()
fig.write_html("docs/infection.html", include_plotlyjs="cdn")

fig = px.choropleth(
    data_frame=df,
    geojson=provinces,
    featureidkey="properties.ten_tinh",
    locations="Province",
    color="Death",
    color_continuous_scale="YlOrRd",
    range_color=(0, df["Death"].max()),
    labels={"Total": "Death Cases"},
    title="COVID-19 Total Death Cases by Province in Vietnam",
)

fig.update_geos(fitbounds="locations", visible=False)
# fig.show()
fig.write_html("docs/death.html", include_plotlyjs="cdn")
