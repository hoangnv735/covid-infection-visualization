import json
import pandas as pd

# import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# provinces = json.load(open("vietnam.geojson", "r"))
provinces = json.load(open("vietnam.simplified.geojson", "r"))
df = pd.read_csv("data.csv", header=0)
df["Total"] = df["Total"].apply(lambda x: int(str(x).replace(".", "")))
df["Death"] = df["Death"].apply(lambda x: int(str(x).replace(".", "")))
rows, cols = 2, 1
fig = make_subplots(
    rows=rows,
    cols=cols,
    specs=[[{"type": "choropleth"}], [{"type": "choropleth"}]],
    # specs=[[{"type": "choropleth"}, {"type": "choropleth"}]],
    subplot_titles=("Infection cases", "Death cases"),
)

fig.add_trace(
    go.Choropleth(
        geojson=provinces,
        featureidkey="properties.ten_tinh",
        locations=df["Province"],
        z=df["Total"],
        colorscale="Viridis",
        # color_continuous_scale="YlOrRd",
        zmin=0,
        zmax=df["Total"].max(),
        # colorbar=dict(title="Total Infections", x=0.45, len=0.5),
        colorbar=dict(title="Total Infections", y=0.8, len=0.5),
        name="Infections",
    ),
    row=1,
    col=1,
)

fig.add_trace(
    go.Choropleth(
        geojson=provinces,
        featureidkey="properties.ten_tinh",
        locations=df["Province"],
        z=df["Death"],
        colorscale="YlOrRd",
        # color_continuous_scale="YlOrRd",
        zmin=0,
        zmax=df["Death"].max(),
        # colorbar=dict(title="Total Death", x=1, len=0.5),
        colorbar=dict(title="Total Death", y=0.25, len=0.5),
        name="Death",
    ),
    row=2,
    col=1,
)

fig.update_geos(fitbounds="locations", showcountries=False, visible=False)
fig.update_layout(
    autosize=True,
    height=1000,
    title_text="COVID-19 Total Cases by Province in Vietnam",
    # margin={"r": 0, "t": 0, "l": 0, "b": 0},
)
fig.show()
