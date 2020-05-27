import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


# Convert the data to tidy format
def convert_data(df, col_name, col_nn, col_arima, col_avg):
    column_names = ['Week', 'Model', col_name]
    graph_df = pd.DataFrame(columns=column_names)

    for i in range(1, 18):
        week = df['week'].loc[(df['week'] == i)].iloc[0]
        model = 'NN'
        result = df[col_nn].loc[(df['week'] == i)].iloc[0]
        graph_df = graph_df.append({'Week': week,
                                    'Model': model,
                                    col_name: result
                                    }, ignore_index=True)

        model = 'ARIMA'
        result = df[col_arima].loc[(df['week'] == i)].iloc[0]
        graph_df = graph_df.append({'Week': week,
                                    'Model': model,
                                    col_name: result
                                    }, ignore_index=True)

        model = 'Average'
        result = df[col_avg].loc[(df['week'] == i)].iloc[0]
        graph_df = graph_df.append({'Week': week,
                                    'Model': model,
                                    col_name: result
                                    }, ignore_index=True)

        graph_df = graph_df.sort_values(by=['Model', 'Week'])
    return graph_df


# Load the MAE data
mae_df = pd.read_csv('https://raw.githubusercontent.com/Lambda-School-Labs/nfl-fantasy-ds/master/data/metrics/metrics.csv')

# Convert the MAE data to tidy format
mae_graph_df = convert_data(mae_df, 'MAE', 'nn', 'arima', 'average')

# Create the MAE line graph
fig = px.line(mae_graph_df, x='Week', y='MAE', color='Model', render_mode='svg', title='Mean Average Error for Each Model')
fig.update_xaxes(nticks=17)
fig.update_layout(title={'x': 0.5, 'xanchor': 'center'})

# Load the percent correct data
correct_df = pd.read_csv('https://raw.githubusercontent.com/Lambda-School-Labs/nfl-fantasy-ds/master/data/metrics/ban_metrics.csv')

# Convert the percent correct data to tidy format
pct_graph_df = convert_data(correct_df, 'Percent Correct', 'nn-pct', 'arima-pct', 'avg-pct')

# Create the percent correct graph
fig1 = px.line(pct_graph_df, x='Week', y='Percent Correct', color='Model', render_mode='svg', title='Percent of Correct Predictions for Each Model')
fig1.update_xaxes(nticks=17)
fig1.update_layout(title={'x': 0.5, 'xanchor': 'center'})

layout = html.Div([
    dcc.Markdown("""
    ### An Evaluation of the Model Predictions

    The Recurrent Neural Network - LSTM Model(NN) outperforms both the baseline Average and ARIMA models.  While
    both the NN and ARIMA models have lower MAEs they all start to converge about halfway through the season as
    all models incorporate the current season actual points and the number of future predictions are reduced thereby
    increasing accuracy in all the models.

    The real accuracy of the models are shown in the *Percent of Correct Predictions* graph.  For each week, the predicted
    outcome of a "good" or "bad" trade for each player is calculated against every other player and compared with the
    actual outcome.  The NN clearly makes better predictions over the other models with an overall average correct percentage
    of 85.59% for the 2019 season compared with 84.72% for an ARIMA model and 83.17% for the baseline average model.

    """),

    dcc.Graph(figure=fig),

    dcc.Graph(figure=fig1)

    ])
