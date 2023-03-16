from dash import Dash, html, dcc
from dash.dependencies import Output,Input
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_winlist, get_loselist, get_rolelist

def render(app):
    list_win = get_winlist()
    top10_win = [{'label':i,'value':i} for i in list_win]
    @app.callback(
    Output(component_id='win_dropdown', component_property='value'),
    Input(component_id='select_all_button', component_property='n_clicks')
    )
    def update_top10_win(n):
        return list_win

    return html.Div(
        children=[
            html.H6("Select Win Rate Top 10 Champions"),
            dcc.Dropdown(
                options=top10_win,
                multi=True,
                id = "win_dropdown",
                value= "Akshan"
            ),
            dbc.Button(
                children=["Select All"],
                color="primary",
                className="me-1",
                id="select_all_button",
                n_clicks=0
            )
        ]
    )

def render1(app):
    list_lose = get_loselist()
    top10_lose = [{'label':i,'value':i} for i in list_lose]
    @app.callback(
    Output(component_id='lose_dropdown', component_property='value'),
    Input(component_id='select_all_button1', component_property='n_clicks')
    )
    def update_top10_lose(n):
        return list_lose

    return html.Div(
        children=[
            html.H6("Select Lose Rate Top 10 Champion"),
            dcc.Dropdown(
                options=top10_lose,
                multi=True,
                id = "lose_dropdown",
                value= "Karma"
            ),
            dbc.Button(
                children=["Select All"],
                color="primary",
                className="me-1",
                id="select_all_button1",
                n_clicks=0
            )
        ]
    )

def render2(app):
    list_role = get_rolelist()
    all_role = [{'label':i,'value':i} for i in list_role]
    @app.callback(
    Output(component_id='role_dropdown', component_property='value'),
    Input(component_id='select_all_button2', component_property='n_clicks')
    )
    def update_all_role(n):
        return list_role

    return html.Div(
        children=[
            html.H6("Select Role Position"),
            dcc.Dropdown(
                options=all_role,
                multi=True,
                id = "role_dropdown",
                value= "jungle"
            ),
            dbc.Button(
                children=["Select All"],
                color="primary",
                className="me-1",
                id="select_all_button2",
                n_clicks=0
            )
        ]
    )