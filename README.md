# NBA Player Similarity

A project for predicting Player Efficiency Rating (PER) for NBA players using supervised learning via an LSTM.

[Data Source](https://www.kaggle.com/drgilermo/nba-players-stats/data)


## Methodology

### Data
The dataset is a collection of statistics for every player averaged over a regular season. Because of this the model is limited to predicting a players statistics per season.

Each players stats is stored as a 2 dimensional matrix with lengths features x number of seasons. When this data is prepared to be put into the model it adds a dimension for players.

### Model
The model chosen for this prediction is an LSTM. LSTMs have been known to perform well for time series predictions. 

| Layer (Type)    |   Output Shape   | Param # |
|-----------------|:----------------:|-------:|
| lstm_1 (LSTM)   | (None, None, 64) |  20480  |
| dense_1 (Dense) | (None, None, 64) |   4160  |
| dense_2 (Dense) | (None, None, 1) |    65   |

Total params: 24,705

Trainable params: 24,705

Non-trainable params: 0


## Results

After training with 30 epochs the model has a loss of 2.884140227940185e-05. But small user checks has shown lackluster, very safe results.

## Glossary

Acrynom | Term |
------- | ---- |
G | Games | N/A
GS | Games Started | N\A
MP |  Minutes Played
PER | Player Efficiency Rating
TS% | True Shooting %
3PAr | 3-Point Attempt Rate
FTr | Free Throw Rate
ORB% | Offensive Rebound Percentage
DRB% | Defensive Rebound Percentage
TRB% | Total Rebound Percentage
AST% | Assist Percentage
STL% | Steal Percentage
BLK% | Block Percentage
TOV% | Turnover Percentage
USG% | Usage Percentage
OWS | Offensive Win Shares
DWS | Defensive Win Shares
WS | Win Shares
WS/48 | Win Shares Per 48 Minutes
OBPM | Offensive Box Plus/Minus
DBPM | Defensive Box Plus/Minus
BPM | Box Plus/Minus
VORP | Value Over Replacement
FG | Field Goals
FGA | Field Goal Attempts
FG% | Field Goal Percentage
3P | 3-Point Field Goals
3PA | 3-Point Field Goal Attempts
3P% | 3-Point Field Goal Percentage
2P | 2-Point Field Goals
2PA | 2-Point Field Goal Attempts
2P% | 2-Point Field Goal Percentage
eFG% | Effective Field Goal Percentage
FT | Free Throws
FTA | Free Throw Attempts
FT% | Free Throw Percentage
ORB | Offensive Rebounds
DRB | Defensive Rebounds
TRB | Total Rebounds
AST | Assists
STL | Steals
BLK | Blocks
TOV | Turnovers
PF | Personal Fouls
PTS | Points
TOT | Total