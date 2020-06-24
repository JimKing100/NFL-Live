from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

from app import app

player_df = pd.read_csv('https://raw.githubusercontent.com/JimKing100/NFL-Live/master/data/players_full1.csv')
player_df = player_df.sort_values(by=['last'])

weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
players = player_df['name'].values.tolist()

style = {'padding': '1em'}

layout = html.Div([
    html.Table([
        html.Col(style={'width': '400px'}),
        html.Col(style={'width': '100px'}),
        html.Col(style={'width': '400px'}),
        html.Thead(),
        # Row 1 - Header
        html.Tr(),
        html.Th(
            dcc.Markdown("""
            #### Select a Week
            """),
            colSpan='3'),
        html.Tbody(),
        # Row 2 - Week
        html.Tr(),
        html.Td(),
        html.Td(
            dcc.Dropdown(
                id='week_no',
                options=[{'label': week, 'value': week} for week in weeks],
                value=1,
                clearable=False)
        ),
        html.Td(),
        # Row 3 - Header
        html.Tr(),
        html.Td(
            dcc.Markdown("""
            #### Players to Trade
            """)
        ),
        html.Td(),
        html.Td(
            dcc.Markdown("""
            #### Players to Receive
            """)
        ),
        # Row 4 - Players Line 1
        html.Tr(),
        html.Td(
            dcc.Dropdown(
                id='player1',
                options=[{'label': player, 'value': player} for player in players],
                value="",
                placeholder="Select Player 1")
        ),
        html.Td(),
        html.Td(dcc.Dropdown(
            id='player2',
            options=[{'label': player, 'value': player} for player in players],
            value="",
            placeholder="Select Player 2")
        ),
        # Row 5 - Players Line 2
        html.Tr(),
        html.Td(
            dcc.Dropdown(
                id='player3',
                options=[{'label': player, 'value': player} for player in players],
                value="",
                placeholder="Select Player 3")
        ),
        html.Td(),
        html.Td(dcc.Dropdown(
            id='player4',
            options=[{'label': player, 'value': player} for player in players],
            value="",
            placeholder="Select Player 4")
        ),
        # Row 6 - Analyze Button
        html.Tr(style={'height': '30px'}),
        html.Td(),
        html.Td(
            html.Button('Analyze', id='submit', n_clicks=0)
        ),
        html.Td()
    ], style=style),
    # Results Table
    html.Div([
        html.Table([
            html.Col(style={'width': '350px'}),
            html.Col(style={'width': '100px'}),
            html.Col(style={'width': '350px'}),
            html.Col(style={'width': '100px'}),
            html.Thead(),
            # Row 1 - Header
            html.Tr(),
            html.Th(id='gb', style={'fontWeight': 'bold'}, colSpan='4'),
            html.Tbody(),
            html.Tr(),
            html.Tr(),
            # Row 2 - Players 1 & 2 Results
            html.Tr(),
            html.Td(id='p1'),
            html.Td(id='p1_pred', style={'fontWeight': 'bold'}),
            html.Td(id='p2'),
            html.Td(id='p2_pred', style={'fontWeight': 'bold'}),
            # Row 3 - Players 3 & 4 Results
            html.Tr(),
            html.Td(id='p3'),
            html.Td(id='p3_pred', style={'fontWeight': 'bold'}),
            html.Td(id='p4'),
            html.Td(id='p4_pred', style={'fontWeight': 'bold'}),
            # Row 4 - Line Break
            html.Tr(),
            html.Td(),
            html.Td(id='c1_break'),
            html.Td(),
            html.Td(id='c2_break'),
            # Row 5 - Predicted Totals
            html.Tr(),
            html.Td(id='c_tot', style={'fontWeight': 'bold'}),
            html.Td(id='c1_tot', style={'fontWeight': 'bold'}),
            html.Td(),
            html.Td(id='c2_tot', style={'fontWeight': 'bold'}),
            # Row 6 - Actual Totals
            html.Tr(),
            html.Td(id='a_tot', style={'color': 'blue'}),
            html.Td(id='a1_tot', style={'color': 'blue'}),
            html.Td(id='accuracy', style={'color': 'blue'}),
            html.Td(id='a2_tot', style={'color': 'blue'})
        ], style=style),
    ], style=style),
])


@app.callback(
    [Output('gb', 'children'),
     Output('p1', 'children'),
     Output('p2', 'children'),
     Output('p3', 'children'),
     Output('p4', 'children'),
     Output('p1_pred', 'children'),
     Output('p2_pred', 'children'),
     Output('p3_pred', 'children'),
     Output('p4_pred', 'children'),
     Output('c_tot', 'children'),
     Output('c1_break', 'children'),
     Output('c2_break', 'children'),
     Output('c1_tot', 'children'),
     Output('c2_tot', 'children'),
     Output('a_tot', 'children'),
     Output('a1_tot', 'children'),
     Output('accuracy', 'children'),
     Output('a2_tot', 'children')],
    [Input('submit', 'n_clicks')],
    [State('week_no', 'value'),
     State('player1', 'value'),
     State('player2', 'value'),
     State('player3', 'value'),
     State('player4', 'value')])
def predict(n_clicks, week_no, player1, player2, player3, player4):
    if (player1 != "") & (player2 != "") & (player1 is not None) & (player2 is not None):
        filename = 'https://raw.githubusercontent.com/JimKing100/NFL-Live/master/data/predictions-week' + str(week_no) + '.csv'
        pred_df = pd.read_csv(filename)
        # Predicted Points
        col_name = 'week' + str(week_no) + '-pred'
        col1_total = 0
        col2_total = 0
        col_total = 'Total Predicted Points for Remaining Season'
        col1_break = '-----'
        col2_break = '-----'
        # Actual Points
        act_name = 'week' + str(week_no) + '-act'
        act1_total = 0
        act2_total = 0
        act_total = 'Total Actual Points for Remaining Season'
        # Get Predicted Points for Players 1 & 2
        player1_pred = pred_df[col_name].loc[(pred_df['name'] == player1)].iloc[0]
        player2_pred = pred_df[col_name].loc[(pred_df['name'] == player2)].iloc[0]
        player3_pred = 0
        player4_pred = 0
        # Get Actual Points for Players 1 & 2
        player1_act = pred_df[act_name].loc[(pred_df['name'] == player1)].iloc[0]
        player2_act = pred_df[act_name].loc[(pred_df['name'] == player2)].iloc[0]
        player3_act = 0
        player4_act = 0
        # Get Predicted and Actual Points for 3 & 4
        if (player3 != "") & (player3 is not None):
            player3_pred = pred_df[col_name].loc[(pred_df['name'] == player3)].iloc[0]
            player3_act = pred_df[act_name].loc[(pred_df['name'] == player3)].iloc[0]
        if (player4 != "") & (player4 is not None):
            player4_pred = pred_df[col_name].loc[(pred_df['name'] == player4)].iloc[0]
            player4_act = pred_df[act_name].loc[(pred_df['name'] == player4)].iloc[0]
        # Calculate Total Predicted and Actual Points
        col1_total = player1_pred + player3_pred
        col2_total = player2_pred + player4_pred
        act1_total = player1_act + player3_act
        act2_total = player2_act + player4_act
        act1_total = int(act1_total)
        act2_total = int(act2_total)
        # Determine Good or Bad Trade (Predicted)
        if col1_total > col2_total:
            good_bad = 'Bad Trade'
            if act1_total > act2_total:
                accuracy = 'Prediction is Accurate'
            else:
                accuracy = 'Prediction is Inaccurate'
        else:
            good_bad = 'Good Trade'
            if act1_total <= act2_total:
                accuracy = 'Prediction is Accurate'
            else:
                accuracy = 'Prediction is Inaccurate'
        # Get Player Info
        if (player1 != "") & (player1 is not None):
            position = player_df['position1'].loc[(player_df['name'] == player1)].iloc[0]
            team = player_df['cteam'].loc[(player_df['name'] == player1)].iloc[0]
            rank = pred_df['rank-cur'].loc[(pred_df['name'] == player1)].iloc[0]
            rank = int(rank)
            injury_week = player_df['injury_week'].loc[(player_df['name'] == player1)].iloc[0]
            if (injury_week <= week_no):
                injury = ' INJURED'
            else:
                injury = ""
            player1_out = player1 + ', ' + position + ', ' + team + \
                ', Ranking: ' + str(rank) + injury
        else:
            player1_out = None
        if (player2 != "") & (player2 is not None):
            position = player_df['position1'].loc[(player_df['name'] == player2)].iloc[0]
            team = player_df['cteam'].loc[(player_df['name'] == player2)].iloc[0]
            rank = pred_df['rank-cur'].loc[(pred_df['name'] == player2)].iloc[0]
            rank = int(rank)
            injury_week = player_df['injury_week'].loc[(player_df['name'] == player2)].iloc[0]
            if (injury_week <= week_no):
                injury = ' INJURED'
            else:
                injury = ""
            player2_out = player2 + ', ' + position + ', ' + team + \
                ', Ranking: ' + str(rank) + injury
        else:
            player2_out = None
        if (player3 != "") & (player3 is not None):
            position = player_df['position1'].loc[(player_df['name'] == player3)].iloc[0]
            team = player_df['cteam'].loc[(player_df['name'] == player3)].iloc[0]
            rank = pred_df['rank-cur'].loc[(pred_df['name'] == player3)].iloc[0]
            rank = int(rank)
            injury_week = player_df['injury_week'].loc[(player_df['name'] == player3)].iloc[0]
            if (injury_week <= week_no):
                injury = ' INJURED'
            else:
                injury = ""
            player3_out = player3 + ', ' + position + ', ' + team + \
                ', Ranking: ' + str(rank) + injury
        else:
            player3_out = None
        if (player4 != "") & (player4 is not None):
            position = player_df['position1'].loc[(player_df['name'] == player4)].iloc[0]
            team = player_df['cteam'].loc[(player_df['name'] == player4)].iloc[0]
            rank = pred_df['rank-cur'].loc[(pred_df['name'] == player4)].iloc[0]
            rank = int(rank)
            injury_week = player_df['injury_week'].loc[(player_df['name'] == player4)].iloc[0]
            if (injury_week <= week_no):
                injury = ' INJURED'
            else:
                injury = ""
            player4_out = player4 + ', ' + position + ', ' + team + \
                ', Ranking: ' + str(rank) + injury
        else:
            player4_out = None
    # Suppress Data for No Trade
    else:
        good_bad = ""
        accuracy = ""
        player1_out = ""
        player2_out = ""
        player3_out = ""
        player4_out = ""
        player1_pred = None
        player2_pred = None
        player3_pred = None
        player4_pred = None
        col_total = None
        col1_break = None
        col2_break = None
        col1_total = None
        col2_total = None
        act_total = None
        act1_total = None
        act2_total = None
    if (player3 == "") | (player3 is None):
        player3_pred = None
    if (player4 == "") | (player4 is None):
        player4_pred = None

    return good_bad, player1_out, player2_out, player3_out, player4_out, player1_pred, \
        player2_pred, player3_pred, player4_pred, col_total, col1_break, \
        col2_break, col1_total, col2_total, act_total, act1_total, accuracy, act2_total
