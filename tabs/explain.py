import dash_core_components as dcc

layout = [dcc.Markdown("""
### Methodology

#### Introduction

NFL fantasy football is a game in which football fans take on the role of the coach or general manager
of a pro football team.  Partipants draft their initial teams, select players to play each week and trade players
in order to compete weekly during a season against other teams.  The winning teams are determined by the
real-life statistics of the pro athletes.

#### Goal of the Trade Analyzer

The goal of the trade analyzer is to determine if a proposed trade of one or more players is a "good"
or "bad" trade during any week of the 2019 football season.  A good trade is defined as trading a player
on your team for a player with higher expected fantasy football points.  The goal, therefore, is to determine
the expected fantasy football points of each pro football player for each week of the 2019 season.  The expected
points can then be compared between players.

#### The Points System

The trade analyzer uses the ESPN Standard League rules for determining fantasy football points.
A team consists of 9 starters in 7 position.  The 7 postions are quarterback(QB), running back(RB),
wide receiver(WR), tight end(TE), kicker(K) and team defense(DF).  A team's defensive squad is
considered one "player" in fantasy football.

| QB/RB/WR/TE                          | Kickers                         | Defense and Special Teams |
| -------------------------------------|---------------------------------|---------------------------|
|6 pts rush or receive TD              |5 pts 50+ yard FG made           |6 pts def/special teams TD |
|6 pts returning kick/punt for TD      |4 pts 40-49 yard FG made         |2 pts interception         |
|6 pts player ret/rec fumble for TD    |3 pts FG made 39 yards or less   |2 pts fumble recovery      |
|4 pts passing TD                      |2 pts rush/pass/rec 2 pt. conv   |2 pts blocked punt/PAT/FG  |
|2 pts rush/receive 2 pt. conv         |1 pt extra point made            |2 pts safety               |
|2 pts passing 2 pt. conversion        |-1 pt missed FG                  |4 pts 1-6 points allowed   |
|1 pts 10 yards rush or receive        |                                 |3 pts 7-13 points allowed  |
|1 pt 25 yards passing                 |                                 |1 pts 14-17 points allowed |
|2 pts rush or receive TD of 40+ yds   |                                 |0 pts 18-27 points allowed |
|2 pts passing TD of 40+ yds           |                                 |-1 pts 28-34 points allowed|
|-2 pts interception                   |                                 |-3 pts 35-45 points allowed|
|-2 pts fumble lost                    |                                 |-5 pts 46+ points allowed  |
|                                      |                                 |1 pt per sack              |

#### Data

The data used for modeling came from *ArmchairAnalysis.com*.  The data consists of over 700+ data points
over 28 different excel tables providing 20 years of detailed stats for every player in the NFL since the
year 2000.

The raw data was initially manipulated in Excel in order to link and extract the relevant data for all
2019 NFL players.  The manipulated data formed the basis for the initial modeling data.

""")]
