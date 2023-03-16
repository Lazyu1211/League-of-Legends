from dash import Dash,html,dcc
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from utill import get_win_lose


def render(app):
    df = get_win_lose()
    fig = px.scatter(
            df, 
            x="win_num", 
            y="lose_num",
            title="Win and Lose",
            color="winrate"
            )
    # Add a diagonal line to the plot
    fig.add_trace(
        go.Scatter(
            x=[df["win_num"].min(), df["win_num"].max()], 
            y=[df["lose_num"].min(), df["lose_num"].max()],
            mode="lines",
            name="diagonal line",
            line=dict(color="red", width=1.5, dash="dash"),
            text=["diagonal line"],
            textposition="top left"
        )
    )
    return html.Div(dcc.Graph(figure=fig), id="scatter")

def render1(app):
    df = get_win_lose()
    fig = px.scatter(
            df, 
            x="total_game", 
            y="winrate",
            title="Total Game with Win Rate",
            color="winrate"
            )
    return html.Div(dcc.Graph(figure=fig), id="scatter1")