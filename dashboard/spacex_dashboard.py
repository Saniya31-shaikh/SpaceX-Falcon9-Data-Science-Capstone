import pandas as pd
import plotly.express as px
from pathlib import Path
from dash import Dash, dcc, html, Input, Output


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "spacex_launches_processed.csv"
df = pd.read_csv(DATA_FILE)
required = {"FlightNumber", "LaunchSite", "PayloadMass", "Orbit", "BoosterVersion", "Class"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Dataset is missing required columns: {sorted(missing)}")

app = Dash(__name__)
app.title = "SpaceX Falcon 9 Analytics"
app.layout = html.Div([
    html.H1("SpaceX Falcon 9 Launch Analytics Dashboard", style={"textAlign": "center"}),
    html.P("Historical launch classifications (IBM course labels)", style={"textAlign": "center"}),
    html.P(f"Records: {len(df)} | Class 1: {(df['Class']==1).sum()} | Class 0: {(df['Class']==0).sum()}",
           style={"textAlign": "center"}),
    html.Label("Select Launch Site"),
    dcc.Dropdown(id="site-dropdown", options=[{"label":"All Launch Sites","value":"ALL"}]
                 + [{"label":s,"value":s} for s in sorted(df["LaunchSite"].dropna().unique())],
                 value="ALL", clearable=False),
    dcc.Graph(id="classification-pie-chart"),
    html.Label("Select Payload Range (kg)"),
    dcc.RangeSlider(id="payload-slider", min=0, max=16000, step=1000,
                    value=[0,16000], marks={i:str(i) for i in range(0,16001,4000)}),
    dcc.Graph(id="payload-scatter-chart"),
    html.P("Note: Class 1 follows the course convention; it does not independently verify a successful landing.",
           style={"fontSize":"12px", "color":"#555"})
], style={"maxWidth":"1100px", "margin":"auto", "padding":"20px", "fontFamily":"Arial, sans-serif"})

@app.callback(Output("classification-pie-chart","figure"), Input("site-dropdown","value"))
def update_classification_pie(selected_site):
    subset = df if selected_site == "ALL" else df[df["LaunchSite"] == selected_site]
    counts = subset["Class"].value_counts().reindex([0,1], fill_value=0).reset_index()
    counts.columns = ["Class","Count"]
    counts["Classification"] = counts["Class"].map({0:"Class 0",1:"Class 1"})
    fig = px.pie(counts, values="Count", names="Classification",
                 title=f"Class Distribution — {('All Launch Sites' if selected_site=='ALL' else selected_site)}",
                 color="Classification", color_discrete_map={"Class 0":"red","Class 1":"green"})
    fig.update_traces(textinfo="percent+label", hovertemplate="%{label}: %{value} launches (%{percent})<extra></extra>")
    return fig

@app.callback(Output("payload-scatter-chart","figure"),
              Input("site-dropdown","value"), Input("payload-slider","value"))
def update_payload_scatter(selected_site, payload_range):
    subset = df.copy() if selected_site == "ALL" else df[df["LaunchSite"] == selected_site].copy()
    subset = subset[subset["PayloadMass"].between(payload_range[0],payload_range[1])].copy()
    subset["Classification"] = subset["Class"].map({0:"Class 0",1:"Class 1"})
    fig = px.scatter(subset, x="PayloadMass", y="FlightNumber", color="Classification",
                     color_discrete_map={"Class 0":"red","Class 1":"green"},
                     hover_data=["LaunchSite","Orbit","BoosterVersion"],
                     title="Flight Number vs Payload Mass by Classification",
                     labels={"PayloadMass":"Payload Mass (kg)","FlightNumber":"Flight Number"})
    fig.update_layout(legend_title="Classification")
    return fig

if __name__ == "__main__":
    app.run(debug=False, port=8050)
