from dash import Dash,html
import os   
import dash_bootstrap_components as dbc
from components import dropdown, bar_charts, scatter_charts, pie_charts

image_path = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSI5dMlO9TinyQSz4fy0J_mmRsfoEpTFAJ6Qg&usqp=CAU"
image_path1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1sZ8pgjHNOt0gD27PZm8oFC0pa8rgTdBuOA&usqp=CAU"
win_path = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ25EnWvNSNJENK9P2uSCEByyOrp9ZJqyCPCA&usqp=CAU"
lose_path = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuflTer9x_i95diSZ_nGhCoCd_SxqD9u1VeA&usqp=CAU"
def create_layout(app):
    return dbc.Container(children=[
        dbc.Row([
        html.H1(
                "League Of Lengends NA Analysis", className="header-title", style={'margin-top': '10px', 'text-align': 'center'}
              ),
        html.P(
                "Base on the dataset we can analysis what features could affect game result in the League Of Lengends NA !!!🔥🔥🔥⌨️⌨️⌨️🖥️🖥️🖥️",
                className="header-description", style={'margin-top': '10px', 'text-align': 'center'}
                ),
        html.P(children="✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨", className="header-emoji", style={'margin-top': '10px', 'text-align': 'left'}),
        html.Img(src=image_path, style={"width": "660px", "height": "400px"}),
        html.Img(src=image_path1, style={"width": "660px", "height": "400px"}),
        html.P(children="✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨", className="header-emoji", style={'margin-top': '10px', 'text-align': 'left'}),
        dbc.Col(dropdown.render(app),lg=12, style={'margin-top': '30px', 'text-align': 'left'}),
        dbc.Col(bar_charts.render(app),lg=6,style={'margin-top': '50px'}),
        html.Img(src=win_path, style={'margin-top': '50px', "width": "660px", "height": "450px"}),
        dbc.Col(dropdown.render1(app),lg=12,style={'margin-top': '50px', 'text-align': 'left'}),
        dbc.Col(bar_charts.render1(app),lg=6,style={'margin-top': '50px'}),
        html.Img(src=lose_path, style={'margin-top': '50px', "width": "660px", "height": "450px"})
,       
    ],className="mt-4"),
        dbc.Row([
            dbc.Col(scatter_charts.render(app),lg=6,style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(scatter_charts.render1(app),lg=6,style={'margin-top': '30px', 'text-align': 'center'}),
            dbc.Col(pie_charts.render(app),lg=6,style={'margin-top': '50px', 'text-align': 'center'}),
            dbc.Col(pie_charts.render1(app),lg=6,style={'margin-top': '50px', 'text-align': 'center'}),
            dbc.Col(pie_charts.render2(app),lg=6,style={'margin-top': '50px', 'text-align': 'center'}),
            dbc.Col(pie_charts.render3(app),lg=6,style={'margin-top': '50px', 'text-align': 'center'}),
            dbc.Col(dropdown.render2(app),lg=12,style={'margin-top': '50px', 'text-align': 'left'}),
            dbc.Col(bar_charts.render2(app),lg=6,style={'margin-top': '50px', 'text-align': 'center'}),
            dbc.Col(bar_charts.render3(app),lg=6,style={'margin-top': '50px', 'text-align': 'center'}),
            dbc.Col(bar_charts.render4(app),lg=6,style={'margin-top': '50px', 'text-align': 'center'}),
            dbc.Col(bar_charts.render5(app),lg=6,style={'margin-top': '50px', 'text-align': 'center'}),
            dbc.Col(bar_charts.render6(app),lg=6,style={'margin-top': '50px', 'text-align': 'center'}),
            dbc.Col(bar_charts.render7(app),lg=6,style={'margin-top': '50px', 'text-align': 'center'}),
            dbc.Col(bar_charts.render8(app),lg=6,style={'margin-top': '50px', 'text-align': 'center'}),
            dbc.Col(bar_charts.render9(app),lg=6,style={'margin-top': '50px', 'text-align': 'center'}),
            dbc.Col(bar_charts.render10(app),lg=6,style={'margin-top': '50px', 'text-align': 'center'}),
            dbc.Col(bar_charts.render11(app),lg=6,style={'margin-top': '50px', 'text-align': 'center'}),
            dbc.Col(bar_charts.render12(app),lg=6,style={'margin-top': '50px', 'text-align': 'center'}),
            dbc.Col(bar_charts.render13(app),lg=6,style={'margin-top': '50px', 'text-align': 'center'}),
            dbc.Col(bar_charts.render14(app),lg=6,style={'margin-top': '50px', 'text-align': 'center'}),
            dbc.Col(bar_charts.render15(app),lg=6,style={'margin-top': '50px', 'text-align': 'center'})
        ],className="mt-4"),
    ])