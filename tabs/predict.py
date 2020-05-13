from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

from app import app

player_df = pd.read_csv('https://raw.githubusercontent.com/JimKing100/NFL-Live/master/data/players_full1.csv')

weeks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
players = player_df['name'].values.tolist()

style = {'padding': '1.5em'}

layout = html.Div([
    dcc.Markdown("""
        ### Trade
        Select a Week then a Player 1 to trade for Player 2.
    """),

    html.Div([
        dcc.Markdown('#### Week'),
        dcc.Dropdown(
            id='week_no',
            options=[{'label': week, 'value': week} for week in weeks],
            value = "",
            placeholder = "Select Week"
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('#### Player 1'),
        dcc.Dropdown(
            id='player1',
            options=[{'label': player, 'value': player} for player in players],
            value = "",
            placeholder = "Select Player 1"
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('#### Player 2'),
        dcc.Dropdown(
            id='player2',
            options=[{'label': player, 'value': player} for player in players],
            value = "",
            placeholder = "Select Player 2"
        ),
    ], style=style),

    html.Div(id='prediction-content', style={'fontWeight': 'bold'}),

])


@app.callback(
    Output('prediction-content', 'children'),
    [Input('week_no', 'value'),
     Input('player1', 'value'),
     Input('player2', 'value')
     ])


def predict(week_no, player1, player2):

    if (player1 != "") & (player2 != ""):
        filename = 'https://raw.githubusercontent.com/JimKing100/NFL-Live/master/data/predictions-week' + str(week_no) + '.csv'
        pred_df = pd.read_csv(filename)

        col_name = 'week' + str(week_no) + '-pred'

        player1_pred = pred_df[col_name].loc[(pred_df['name'] == player1)].iloc[0]
        player2_pred = pred_df[col_name].loc[(pred_df['name'] == player2)].iloc[0]

        if player1_pred > player2_pred:
            good_bad = 'Bad Trade'
        else:
            good_bad = 'Good Trade'
            
        results = good_bad + ' - ' + player1 + ' Predicted Points = ' + str(player1_pred) + ', ' + player2 + ' Predicted Points = ' + str(player2_pred)
    else:
        results = ""

    return results
