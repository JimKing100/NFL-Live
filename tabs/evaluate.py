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

    """),

    dcc.Graph(figure=fig),

    dcc.Graph(figure=fig1)

    ])
