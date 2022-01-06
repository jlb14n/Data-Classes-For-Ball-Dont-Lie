#------------------------------------------------------------------------------------------------------------------------------------------
#Imports
from dataclasses import dataclass, field
from datetime import date,datetime,time
#------------------------------------------------------------------------------------------------------------------------------------------
#Part 1: Class Definitions
@dataclass
class Player():

    PlayerID: int
    first_name: str
    last_name: str
    height_ft: int
    height_in: int
    position: str
    teamID: int
    weight_pounds: int  

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
    season: date #(year)

@dataclass
class Stats():

    StatID: int
    GameID: int
    PlayerID: int
    TeamID: int
    min: time
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
    season: date #(year)
    min: time  
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
#------------------------------------------------------------------------------------------------------------------------------------------
#Part 2: API Consumption