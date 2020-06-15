# NFL-Live
### NFL Fantasy Football Trading Project

You can find the app at [https://nfl-trade.herokuapp.com][1]

### Contents

### data-science

The data science directory containing the following Colab notebooks and data:

#### *actuals* - The Colab notebooks calculating the actual fantasy football points for each 2019 NFL player

- Actuals_Defense.ipynb
- Actuals_Kicker.ipynb
- Actuals_Offense.ipynb
- Actuals_Rookie_2019_Kickers.ipynb
- Actuals_Rookie_2019_Offense.ipynb
- Actuals_Rookie_Kickers.ipynb
- Actuals_Roookie_Offense.ipynb

#### *data* - The raw and calculated data used in the models

##### actuals

- actuals_defense.csv
- actuals_kickers.csv
- actuals_offense.csv
- actuals_rookie2019_kickers.csv
- actuals_rookie2019_offense.csv
- actuals_rookie_kicker.csv
- actuals_rookie_offense.csv

##### arima_combined

- predictions-week(1-17).csv

##### arima

- week(1-17)-pred-defense.csv
- week(1-17)-pred-offense-norookies.csv
- week(1-17)-pred-offense-rookies.csv

##### metrics

- ab_metrics.csv
- arima_metrics.csv
- ban_metrics.csv
- metrics.csv
- nb_metrics.csv
- nn_metrics.csv

##### raw

- bye.csv
- conv.csv
- defense.csv
- game.csv
- injury.csv
- kicking.csv
- missedfg.csv
- offense.csv
- players.csv
- players_full.csv
- players_full1.csv
- rookies.csv
- rookies_non.csv
- rookies_non_kicker.csv
- rookies_non_offense.csv
- td.csv

##### rnn-combined

- predictions-week(1-17).csv

##### rnn

- **df** - directory containing week(1-17)-pred-defense.csv
- **ki** - directory containing week(1-17)-pred-offense-norookies-k.csv
- **qb** - directory containing week(1-17)-pred-offense-norookies-qb.csv
- **rb** - directory containing week(1-17)-pred-offense-norookies-rb.csv
- **te** - directory containing week(1-17)-pred-offense-norookies-te.csv
- **wr** - directory containing week(1-17)-pred-offense-norookies-wr.csv

#### metrics - The Colab notebooks used to create the performance metrics and graphs

- Graphs.ipynb
- MetricsARIMA_MAE.ipynb
- MetricsARIMA_PvA.ipynb
- MetricsNN_MAE.ipynb
- MetricsNN_PvA.ipynb

#### model-arima - The Colab notebooks calculating the ARIMA model predicted fantasy football points for each 2019 NFL player

- Predictions_Combined.ipynb
- Predictions_Defense.ipynb
- Predictions_Offense.ipynb
- Predictions_Rookies_1.ipynb
- Predictions_Rookies_2_to_17.ipynb

#### model-rnn - The Colab notebooks calculating the RNN model predicted fantasy football points for each 2019 NFL player

- Predictions_Combined.ipynb
- Predictions_Defense.ipynb
- Predictions_Offense.ipynb

#### players - The Colab notebook creating the detailed 2019 NFL player list

- Players_Full.ipynb

### data

The data directory containing the final production data for the Dash app

- players_full.csv
- predictions-week(1-17).csv

### metrics

The metrics directory containing the final metrics data for the Dash app

- ban_metrics.csv
- metrics.csv

### tabs

The tabs directory containing the code for the Dash tabs

- evaluate.py
- explain.py
- predict.py

### main app

- Procfile
- app.py
- index.py
- requirements.txt


[1]: <https://nfl-trade.herokuapp.com>
