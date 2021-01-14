# import packages
from nba_api.stats.endpoints import shotchartdetail
import json 
import requests
import pandas as pd 
import datetime


#Load teams file into a df from our json file

teams = pd.read_json('data/teams.json')

players = pd.read_json('data/players.json')

#get the team id based on team name 

def get_team_id(team):
    return teams['teamId'][teams['teamName'] == team].iloc[0]

#get the player id 
def get_player_id(first, last):
    return players['playerId'][(players['firstName'] == first) & (players['lastName'] == last)].iloc[0]