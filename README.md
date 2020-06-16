# NFL-Live
### NFL Fantasy Football Trading Project

You can find the app at [https://nfl-trade.herokuapp.com][1]

### Contents

### data-science

The data science directory containing the following Colab notebooks and data:

#### *actuals* - The Colab notebooks calculating the actual fantasy football points for each 2019 NFL player

- Actuals_Defense.ipynb - calculate actuals for each team defense
- Actuals_Kicker.ipynb - calculate actuals for each kicker
- Actuals_Offense.ipynb - calculate actuals for each offensive player (QB, RB, TE, WR)
- Actuals_Rookie_2019_Kickers.ipynb - calculate actuals for each 2019 rookie kicker
- Actuals_Rookie_2019_Offense.ipynb - calculate actuals for each 2019 rookie offensive player
- Actuals_Rookie_Kickers.ipynb - calculate actuals for non-rookie kickers in their rookie year
- Actuals_Roookie_Offense.ipynb - calculate actuals for non-rookie offensive players in their rookie year

#### *data* - The raw and calculated data used in the models

##### actuals - The actual points for each 2019 player for each game from 2000-2019

- actuals_defense.csv - the actual points for each team defense
- actuals_kickers.csv - the actual points for each kicker
- actuals_offense.csv - the actual points for each offensive player
- actuals_rookie2019_kickers.csv - the actual points for each 2019 rookie kicker
- actuals_rookie2019_offense.csv - the actual points for each 2019 rookie offensive player
- actuals_rookie_kicker.csv - the actual points for each non-rookie kicker in their rookie year
- actuals_rookie_offense.csv - the actual points for each non-rookie offensive player in their rookie year

##### arima_combined - The final combined ARIMA model predicted points for each week of the 2019 season

- predictions-week(1-17).csv - the weekly (weeks 1-17) ARIMA model predictions for all players in 2019

##### arima - The ARIMA model predicted points for defenses and non-rookie players, XGBoost predicted points for rookies

- week(1-17)-pred-defense.csv - the ARIMA model predicted points for defenses for weeks 1-17
- week(1-17)-pred-offense-norookies.csv - the ARIMA model predicted points for non-rookie offensive players for weeks 1-17
- week(1-17)-pred-offense-rookies.csv - the XGBoost model predicted points for rookies for weeks 1-17

##### metrics

- ab_metrics.csv - the stats comparing the correct predictions for the Average model vs the ARIMA model
- arima_metrics.csv - the stats comparing the MAE for the Average model vs the ARIMA model
- ban_metrics.csv - the combined percent correct stats for Average, ARIMA and RNN models
- metrics.csv - the combined MAE stats for Average, ARIMA and RNN models
- nb_metrics.csv - the stats comparing the correct predictions for the Average model vs the RNN model
- nn_metrics.csv - the stats comparing the MAE for the Average model vs the RNN model

##### raw - The starting data from manipulated excel raw data from [ArmchairAnalysis.com][2].
The original excel data was reduced to 2019 excel data for players and teams.  Other manipulations were done in excel including linking and aggregating the data.

- bye.csv - raw data for bye weeks fo each team in 2019
- conv.csv - raw data on touchdown conversions by player
- defense.csv - raw data on defensive fantasy points by team for each game, does not include points-allowed fantasy points
- game.csv - raw data on each game each season, use to determine home and away teams
- injury.csv - raw data for injuries for 2019 players (IR and Out classifications only)
- kicking.csv - raw data on kicking points by kickers
- missedfg.csv - raw data on missed field goals by kickers
- offense.csv - raw data on ofensive points by player
- players.csv - raw data on 2019 players
- players_full.csv - initial full list of all 2019 players
- players_full1.csv - final enhanced list of 2019 players
- rookies.csv - raw data on 2019 rookies 
- rookies_non.csv - raw data on all non-rookie 2019 players
- rookies_non_kicker.csv - raw data on all non-rookie 2019 kickers
- rookies_non_offense.csv - raw data on all non-rookie 2019 offensive players
- td.csv - raw data ob touchdowns by player (both QB and receiver/rusher)

##### rnn-combined - The final combined RNN model predicted points for each week of the 2019 season

- predictions-week(1-17).csv - the weekly (weeks 1-17) RNN model predictions for all players in 2019

##### rnn - The RNN model predicted points for defenses and non-rookie players
The RNN model is resource instensive and for time purposes were run by position with the data output by position.  Rookie points were calculated using an XGBoost model (see arima data directory for rookie results).

- **df** - directory containing week(1-17)-pred-defense.csv, the defensive predicted points for weeks 1-17
- **ki** - directory containing week(1-17)-pred-offense-norookies-k.csv, the non-rookie kicker predicted points for weeks 1-17
- **qb** - directory containing week(1-17)-pred-offense-norookies-qb.csv, the non-rookie QB predicted points for weeks 1-17
- **rb** - directory containing week(1-17)-pred-offense-norookies-rb.csv, the non-rookie RB predicted points for weeks 1-17
- **te** - directory containing week(1-17)-pred-offense-norookies-te.csv, the non-rookie TE predicted points for weeks 1-17
- **wr** - directory containing week(1-17)-pred-offense-norookies-wr.csv, the non-rookie WR predicted points for weeks 1-17

#### *metrics* - The Colab notebooks used to create the performance metrics and graphs

- Graphs.ipynb - create the two performance graphs using plotly express
- MetricsARIMA_MAE.ipynb - calculate the MAE for the ARIMA model for weeks 1-17
- MetricsARIMA_PvA.ipynb - calculate the percentage correct for predictions vs. actuals for the ARIMA model for weeks 1-17
- MetricsNN_MAE.ipynb - calculate the MAE for the RNN model for weeks 1-17
- MetricsNN_PvA.ipynb - calculate the percentage correct for predictions vs. actuals for the RNN model for weeks 1-17

#### *model-arima* - The Colab notebooks calculating the ARIMA model predicted fantasy football points for each 2019 NFL player

- Predictions_Combined.ipynb - code to combine the defense, offense and rookie ARIMA predictions for all 2019 weeks
- Predictions_Defense.ipynb - code to create the team defense ARIMA predictions for all 2019 weeks
- Predictions_Offense.ipynb - code to create the offensive player ARIMA predictions for all 2019 weeks
- Predictions_Rookies_1.ipynb - code to create the rookie player XGBoost predictions for week 1 of 2019
- Predictions_Rookies_2_to_17.ipynb - code to create the rookie player Average predictions for weeks 2-17 for 2019

#### *model-rnn* - The Colab notebooks calculating the RNN model predicted fantasy football points for each 2019 NFL player

- Predictions_Combined.ipynb - code to combine the defense, offense and rookie RNN predictions for all 2019 weeks
- Predictions_Defense.ipynb - code to create the team defense RNN predictions for all 2019 weeks
- Predictions_Offense.ipynb - code to create the offensive player RNN predictions for all 2019 weeks

#### *players* - The Colab notebook creating the detailed 2019 NFL player list

- Players_Full.ipynb - code to create an enhanced list (includes bye week and injury week) of all 2019 NFL players

### data

The data directory containing the final production data for the Dash app

- players_full1.csv - the final enhanced player list including bye week and injury week
- predictions-week(1-17).csv - the final RNN predictions

### metrics

The metrics directory containing the final metrics data for the Dash app

- ban_metrics.csv - the final percent correct stats for Average, ARIMA and RNN models
- metrics.csv - the final combined MAE stats for Average, ARIMA and RNN models

### tabs

The tabs directory containing the code for the Dash tabs

- evaluate.py - the code for the Evaluate tab
- explain.py - the code for the Methodology tab
- predict.py - the code for the Trade tab

### main app

- Procfile - the Procfile for Heroku
- app.py - initiates the Dash app
- index.py - the main Dash code with the layout and callback
- requirements.txt - the environment file for Heroku


[1]: <https://nfl-trade.herokuapp.com>
[2]: <https://www.armchairanalysis.com>
