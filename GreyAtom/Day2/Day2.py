:import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#Reading Dataset matches
matches = pd.read_csv("matches.csv")
dfm=matches.copy()
#Reading Dataset matches
deliveries = pd.read_csv("deliveries.csv")
dfd=deliveries.copy()
#looking data contents using head in matches dataset
dfm.head()
dfm.shape
#Total 636 Matches
#looking data contents using head in deliveries dataset
dfd.head()
dfm.groupby('season').season.nunique().sum()
#10 Seasons
dfm.iloc[dfm['win_by_runs'].idxmax()].winner
dfm.iloc[dfm['win_by_wickets'].idxmax()].winner
dfm.iloc[dfm['win_by_runs'].idxmin()].winner
dfm.iloc[dfm['win_by_wickets'].idxmin()].winner
dfm.groupby('season').id.nunique().idxmax()
pd.unique(dfm.team1)
pd.unique(dfm.team2)
#Finding teams having team name %Pune% or %Deccan%
dfm[dfm['team1'].str.contains("Pune|Deccan|Hyderabad ")].team1.value_counts()
#Finding teams having team name %Pune% or %Deccan%
dfm[dfm['team2'].str.contains("Pune|Deccan|Hyderabad")].team2.value_counts()
#Renaming team1 data
dfm.team1=dfm.team1.replace({"Deccan Chargers":"Sunrisers Hyderabad","Pune Warriors":"Rising Pune Supergiant","Rising Pune Supergiants":"Rising Pune Supergiant"})
#Renaming team2 data
dfm.team2=dfm.team2.replace({"Deccan Chargers":"Sunrisers Hyderabad","Pune Warriors":"Rising Pune Supergiant","Rising Pune Supergiants":"Rising Pune Supergiant"})
pd.unique(dfm.team2)
pd.unique(dfm.team1)
matches_played=(dfm.team1.value_counts() + dfm.team2.value_counts()).to_frame()
matches_played.iloc[0].name
len(matches_played)
#matches_played.sort_values(ascending=False)
sucess_rate={}
for i in range(0,len(matches_played)):
    sucess_rate.update({
            matches_played.iloc[i].name:
                (int(matches_played.iloc[i])/dfm[dfm['winner']==
                                     matches_played.iloc[i].name].id.value_counts().sum())}

    
total_runs_per_team={}

for i in pd.unique(dfd.batting_team):
    total_runs_per_team.update({i:dfd[dfd["batting_team"]==i].total_runs.value_counts().sum()})
    
total_runs_per_bowler={}
for i in pd.unique(dfd.bowler):
    total_runs_per_bowler.update({i:(dfd[dfd["bowler"]==i].total_runs.value_counts().sum())/(dfd[dfd["bowler"]==i].over.value_counts().count())})