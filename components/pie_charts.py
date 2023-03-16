from dash import Dash, html, dcc
import plotly.express as px
from utill import get_dspell, get_fspell, get_red, get_blue

def render(app):
    df = get_dspell()
    df.index = df.index.str.upper()
    fig = px.pie(df, values = 'd_spell', names = df.index, color_discrete_sequence=['#29CDFF', '#FF6019'], title = 'D Spell Times With Game Result')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart")

def render1(app):
    df = get_fspell()
    df.index = df.index.str.upper()
    fig = px.pie(df, values = 'f_spell', names = df.index, color_discrete_sequence=['#9FC5E8', '#FF5E0E'], title = 'F Spell Times With Game Result')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart1")

def render2(app):
    df = get_red()
    df.index = df.index.str.upper()
    fig = px.pie(df, values = 'result', names = df.index, color_discrete_sequence=['#29CDFF', '#FF6019'], title = 'Red Side With Game Result')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart2")

def render3(app):
    df = get_blue()
    df.index = df.index.str.upper()
    fig = px.pie(df, values = 'result', names = df.index, color_discrete_sequence=['#9FC5E8', '#FF5E0E'], title = 'Blue Side With Game Result')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart3")