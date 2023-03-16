from dash import Dash, html, dcc
from dash.dependencies import Output,Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from utill import get_winrate, get_loserate, get_winrole, get_loserole, get_assists, get_death, get_kda, get_kills, get_level, get_timecc, get_damage_total, get_damage_taken, get_gold_earned, get_total_minions_killed, get_turret_kills, get_vision_score

def render(app):
    df = get_winrate()

    @app.callback(
        Output("bar_volume", component_property='children'),
        Input("win_dropdown",component_property='value')
    )

    def update_bar_chart(dropdown):
        filtered_data = df.query("champion in @dropdown")
        fig = px.bar(
                filtered_data,
                x="champion",
                y="winrate",
                color="winrate",
                title="Win Rate Top 10 Champions")
        return html.Div(dcc.Graph(figure=fig),id="bar_volume")
    return html.Div(id="bar_volume")

def render1(app):
    df = get_loserate()

    @app.callback(
        Output("bar_volume1", component_property='children'),
        Input("lose_dropdown",component_property='value')
    )

    def update_bar_chart(dropdown):
        filtered_data = df.query("champion in @dropdown")
        fig = px.bar(
                filtered_data,
                x="champion",
                y="winrate",
                color="winrate",
                title="Lose Rate Top 10 Champions")
        return html.Div(dcc.Graph(figure=fig),id="bar_volume1")
    return html.Div(id="bar_volume1")

def render2(app):
    df = get_winrole()

    @app.callback(
        Output("bar_volume2", component_property='children'),
        Input("role_dropdown",component_property='value')
    )

    def update_bar_chart(dropdown):
        filtered_data = df.query("role_position in @dropdown")
        fig = px.bar(
                filtered_data,
                x = "role_position",
                y = "win games",
                color= "win games",
                title = "Win Role Count")
        return html.Div(dcc.Graph(figure=fig),id="bar_volume2")
    return html.Div(id="bar_volume2")

def render3(app):
    df = get_loserole()

    @app.callback(
        Output("bar_volume3", component_property='children'),
        Input("role_dropdown",component_property='value')
    )
    
    def update_bar_chart(dropdown):
        filtered_data = df.query("role_position in @dropdown")
        fig = px.bar(
                filtered_data,
                x = "role_position",
                y = "lose games",
                color= "lose games",
                title = "Lose Role Count")
        return html.Div(dcc.Graph(figure=fig),id="bar_volume3")
    return html.Div(id="bar_volume3")

def render4(app):
    df = get_assists()
    fig = px.bar(
        df,
        x = "game_result",
        y = "average_assists",
        color= "average_assists",
        title="Average Assist with Game Result")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume4")

def render5(app):
    df = get_kda()
    fig = px.bar(
        df,
        x = "game_result",
        y = "average_kda",
        color= "average_kda",
        title="Average KDA with Game Result")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume5")

def render6(app):
    df = get_kills()
    fig = px.bar(
        df,
        x = "game_result",
        y = "average_kills",
        color= "average_kills",
        title="Average Kills with Game Result")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume6")

def render7(app):
    df = get_death()
    fig = px.bar(
        df,
        x = "game_result",
        y = "average_death",
        color= "average_death",
        title="Average Death with Game Result")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume7")

def render8(app):
    df = get_level()
    fig = px.bar(
        df,
        x = "game_result",
        y = "average_level",
        color= "average_level",
        title="Average Level with Game Result")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume8")

def render9(app):
    df = get_timecc()
    fig = px.bar(
        df,
        x = "game_result",
        y = "average_time_cc",
        color= "average_time_cc",
        title="Average Timecc with Game Result")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume9")

def render10(app):
    df = get_damage_total()
    fig = px.bar(
        df,
        x = "game_result",
        y = "average_damage_total",
        color= "average_damage_total",
        title="Average Damage Total with Game Result")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume10")

def render11(app):
    df = get_damage_taken()
    fig = px.bar(
        df,
        x = "game_result",
        y = "average_damage_taken",
        color= "average_damage_taken",
        title="Average Damage Taken with Game Result")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume11")

def render12(app):
    df = get_gold_earned()
    fig = px.bar(
        df,
        x = "game_result",
        y = "average_gold_earned",
        color= "average_gold_earned",
        title="Average Gold Earned with Game Result")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume12")

def render13(app):
    df = get_total_minions_killed()
    fig = px.bar(
        df,
        x = "game_result",
        y = "average_total_minions_killed",
        color= "average_total_minions_killed",
        title="Average Total Minions Killed with Game Result")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume13")

def render14(app):
    df = get_turret_kills()
    fig = px.bar(
        df,
        x = "game_result",
        y = "average_turret_kills",
        color= "average_turret_kills",
        title="Average Turret Kills with Game Result")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume14")

def render15(app):
    df = get_vision_score()
    fig = px.bar(
        df,
        x = "game_result",
        y = "average_vision_score",
        color= "average_vision_score",
        title="Average Vision Score with Game Result")
    return html.Div(dcc.Graph(figure=fig),id="bar_volume15")