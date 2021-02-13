#################################################
# Introduction to API Lab
#################################################

import pandas as pd
import matplotlib.pyplot as plt

def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict  

from nba_api.stats.static import teams

#https://pypi.org/project/nba-api/

nba_teams = teams.get_teams()

dict_nba_team=one_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_team)
print(df_teams.head())

df_warriors=df_teams[df_teams['nickname']=='Warriors']
print(df_warriors)

id_warriors=df_warriors[['id']].values[0][0]
#we now have an integer that can be used   to request the Warriors information 
print(id_warriors)

from nba_api.stats.endpoints import leaguegamefinder

# Since https://stats.nba.com does not allow api calls from Cloud IPs and Skills Network Labs uses a Cloud IP.
# The following code is comment out, you can run it on jupyter labs on your own computer.
# gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)

# Since https://stats.nba.com does not allow api calls from Cloud IPs and Skills Network Labs uses a Cloud IP.
# The following code is comment out, you can run it on jupyter labs on your own computer.
# gamefinder.get_json()

# Since https://stats.nba.com does not allow api calls from Cloud IPs and Skills Network Labs uses a Cloud IP.
# The following code is comment out, you can run it on jupyter labs on your own computer.
# games = gamefinder.get_data_frames()[0]
# print(games.head())

import urllib.request

# Only need to run below 2 lines once to download the file
# url = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl'
# urllib.request.urlretrieve(url, 'Golden_State.pkl')

# ! wget https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl

file_name = "Golden_State.pkl"
games = pd.read_pickle(file_name)
print(games.head())

games_home=games [games ['MATCHUP']=='GSW vs. TOR']
games_away=games [games ['MATCHUP']=='GSW @ TOR']

games_home.mean()['PLUS_MINUS']
games_away.mean()['PLUS_MINUS']

fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
# plt.show() <- Uncomment to plot graph

# Question 1
# Calculate the mean for the column PTS for the dataframes games_home and  games_away:

print("EXERCISE 1")

print(games_home.mean()['PTS'])
print(games_away.mean()['PTS'])