# Makes the necessary imports in order to use plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import re

# Reads the CSV file
file = pd.read_csv("results.csv")

# Allocates space on the web page for the graphs
fig = make_subplots(
    rows=7, cols=1,
    shared_xaxes=True,
    vertical_spacing=0.03,
    specs=[[{"type": "table"}], [{"type": "bar"}], [{"type": "bar"}], [{"type": "bar"}], [{"type": "bar"}], [{"type": "bar"}], [{"type": "bar"}]]
)

# Creates the table for COVID-19 stats by US state
fig.add_trace(
    go.Table(
        header=dict(
            values=["USAState", "TotalCases", "NewCases", "TotalDeaths", "NewDeaths", "TotalRecovered", "ActiveCases", "Tot Cases/1M pop", "Deaths/1M pop", "Total Tests", "Tests/1M pop", "Population"],
            font=dict(size=10),
            align="left"
        ),
        cells=dict(
            values=[file[k].tolist() for k in file.columns[1:13]],
            align = "left")
    ),
    row=1, col=1
)

# Creates a bar graph showing the total cases per state
fig.add_trace(
    go.Bar(x=file["USAState"], y=file["TotalCases"],name="Cases"),
    row=2, col=1
)

# Creates a bar graph showing the total deaths per state
fig.add_trace(
    go.Bar(x=file["USAState"], y=file["TotalDeaths"], name="Deaths"),
    row=3, col=1
)

# Creates a bar graph showing the total recovered patients per state (grouped with active cases)
fig.add_trace(
    go.Bar(x=file["USAState"], y=file["TotalRecovered"], name="Recovered"),
    row=4, col=1
)

# Creates a bar graph showing the total active cases per state (grouped with total recovered)
fig.add_trace(
    go.Bar(x=file["USAState"], y=file["ActiveCases"], name="Active Cases"),
    row=4, col=1
)

# Creates a bar graph showing the average cases per 1 million people per state (grouped with deaths/1M pop)
fig.add_trace(
    go.Bar(x=file["USAState"], y=file["Tot Cases/1M pop"], name="Tot Cases/1M pop"),
    row=5, col=1
)

# Creates a bar graph showing the average deaths per 1 million people per state (grouped with tot cases/1M pop)
fig.add_trace(
    go.Bar(x=file["USAState"], y=file["Deaths/1M pop"], name="Deaths/1M pop"),
    row=5, col=1
)

# Creates a bar graph showing new deaths per state
fig.add_trace(
    go.Bar(x=file["USAState"], y=file["NewDeaths"], name="New Deaths"),
    row=6, col=1
)

# Creates a bar graph showing the average tests per 1 million people per state
fig.add_trace(
    go.Bar(x=file["USAState"], y=file["Tests/ 1M pop"], name="Tests/1M pop"),
    row=7, col=1
)

# Groups the graphs within the same rows and adds a title at a specific location
fig.update_layout(barmode = 'group', height=800, showlegend=False, title_text="COVID-19 Statistics in the US by State")

fig.show()
