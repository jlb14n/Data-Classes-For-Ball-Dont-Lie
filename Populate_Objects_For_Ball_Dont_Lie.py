from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Player():

    PlayerID: int
    first_name: str
    last_name: str
    position: str
    teamID: int
    height_ft: int = 0
    height_in: int = 0
    weight_pounds: int = 0

@dataclass
class Team():

    TeamID: int
    abbr: str
    city: str
    conference: str
    divison: str
    full_name: str
    name: str

@dataclass
class Game():

    GameID: int
    HomeTeamID: int
    AwayTeamID: int
    home_score: int
    away_score: int
    postseason: bool
    season: int

@dataclass
class Stats():

    StatID: int
    GameID: int
    PlayerID: int
    TeamID: int
    minutes: int
    pts: int
    ast: int
    stl: int
    blk: int
    dreb: int
    oreb: int
    totalreb: int
    pf: int
    turnovers: int
    fg3pct: float
    fg3a: int
    fg3m: int
    fgpct: float
    fga: int
    fgm: int
    ftpct: float
    fta: int
    ftm: int

@dataclass
class SeasonAverages():

    PlayerID: int
    games_played: int
    season: int
    minutes: str
    pts: float
    ast: float
    stl: float
    blk: float
    dreb: float
    oreb: float
    totalreb: float
    pf: float
    turnovers: float
    fg3pct: float
    fg3a: float
    fg3m: float
    fgpct: float
    fga: float
    fgm: float
    ftpct: float
    fta: float
    ftm: float

import json
import requests
import time
from bs4 import BeautifulSoup

data_class_list = ["players", "teams"]
json_dclass = []
for dclass in data_class_list:
    if dclass == "players":
        players_dclass = []
        for page in range(1,39):
            url = f"https://www.balldontlie.io/api/v1/{dclass}?page={page}&per_page=100"
            players_dclass.append(json.loads(requests.get(url).text))
        json_dclass.append({f"{dclass}":players_dclass})
    elif dclass == "teams":
        teams_dclass = []
        url = f"https://www.balldontlie.io/api/v1/{dclass}"
        teams_dclass.append(json.loads(requests.get(url).text))
        json_dclass.append({f"{dclass}":teams_dclass})

print('sleeping part 1')
time.sleep(65)
print("Uh-oh nightmare!")

dclass = "games"
games_dclass = []
for page in range(1,30):
    url = f"https://www.balldontlie.io/api/v1/{dclass}?page={page}&per_page=100"
    games_dclass.append(json.loads(requests.get(url).text))
    
json_dclass.append({f"{dclass}":games_dclass})

print('sleeping part 2')
time.sleep(65)
print("Uh-oh nightmare!")

dclass = "season_averages"
season_averages_dclass = []
for season in range(1979,2020):
    url = f"https://www.balldontlie.io/api/v1/{dclass}?season={season}"
    for I in range(1,5):
        url+=f'&player_ids[]={I}'
    season_averages_dclass.append(json.loads(requests.get(url).text))

json_dclass.append({f"{dclass}":season_averages_dclass})

# Player object
for j in range(0,len(json_dclass[0]["players"])):
    for i in json_dclass[0]["players"][j]['data']:
        if i['first_name'] == 'Stephen' and i['last_name'] == 'Curry':
            try: 
                Stephen_Curry = Player(int(i['id']),i['first_name'],i["last_name"],i["position"],int(i['team']["id"]),int(i["height_feet"]),int(i["height_inches"]),int(i["weight_pounds"]))
            except:
                Stephen_Curry = Player(int(i['id']),i['first_name'],i["last_name"],i["position"],int(i['team']["id"]))

print(f"\nThe players attributes are: {Stephen_Curry.__dict__}")

# Game object
# Grabs the 1st game (0) from the first indexed page (0)
sj2 = json_dclass[2]["games"][0]['data'][0]
# try:
space_jam_2 = Game(sj2['id'],sj2['home_team']['id'],sj2["visitor_team"]["id"],sj2["home_team_score"],sj2['visitor_team_score'],sj2['postseason'],sj2['season'])
# except:
#     space_jam_2 = Player(int(i['id']),i['first_name'],i["last_name"],i["position"],int(i['team']["id"]))
print(f"\nThe game to determine the fate of the universe was: {space_jam_2.__dict__}")

# Team object
i = json_dclass[1]["teams"][0]['data'][22]
Crying_Simmons_Face = Team(i['id'],i['abbreviation'],i["city"],i["conference"],i['division'],i["full_name"],i["name"])
print(f"\nThe team that trusted the process and has lived in misery since: {Crying_Simmons_Face.__dict__}")

# Season_average object
i = json_dclass[3]["season_averages"][-1]['data'][0]
scrub = SeasonAverages(i['player_id'],i["games_played"],i["season"],i["min"],i['pts'],i['ast'],i['stl'],i['blk'],i['dreb'],
                      i['oreb'],i['reb'],i['pf'],i['turnover'],i['fg3_pct'],i['fg3a'],i['fg3m'],i['fg_pct'],i['fga'],i['fgm'],
                      i['ft_pct'],i['fta'],i['ftm'])
print(f"\nThis mans signed a 10 day contract and still got cut: {scrub.__dict__}")