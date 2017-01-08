#!/usr/bin/env python3

## Ben Kite
## 2017-01-06

import pandas, os, argparse
import dataScrape

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--year", help="Year of games to be collected. Eventually I'll allow multiple years (e.g., 2010-2012 or 2010 2012 2013, etc.)")
parser.add_argument("--team", help="Name of team you want data for. I'll also work to allow multiple teams. Defaults to pull for all teams.", default = "ALL")
parser.add_argument("--datdir", help="Name of directory where the data should be stored.  If the directory does not exist it will be created. Defaults to data/", default = "data/")

args = parser.parse_args()

year  = str(args.year)
team = str(args.team)
directory = str(args.datdir)

if not os.path.exists(directory):
    os.makedirs(directory)

if team == "ALL":
    teams = ['ATL', 'ARI', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL',
             'DET', 'KCR', 'HOU', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY',
             'OAK', 'PHI', 'PIT', 'SDP', 'SEA', 'SFG', 'STL', 'TBR', 'TEX', 'TOR',
             'WSN'] 
    checkold = True   
    oldteams = ['ANA', 'BRO', 'CAL', 'FLA', 'KCA', 'MLN', 'MON', 'NYG', 'SLB', 'TBD', 'WSA']
    
else:
    teams = [team]
    checkold = False

## Eventually years will have a range    
years = [year]
 
for year in years:      
    for t in teams:
        try:
            Batting = dataScrape.playerdata(t, year, "team_batting")
            Batting.to_csv(directory + "/" + t + "_" + str(year) + "_batting.csv", index = False, encoding = "utf-8")
        except IndexError:
            pass
    
        try:
            Pitching = dataScrape.playerdata(t, year, "team_pitching")
            Pitching.to_csv(directory + "/" + t + "_" + str(year) + "_pitching.csv", index = False, encoding = "utf-8")
        except IndexError:
            pass
    
        try:        
            Fielding = dataScrape.playerdata(t, year, "standard_fielding")
            Fielding.to_csv(directory + "/" + t + "_" + str(year) + "_fielding.csv", index = False, encoding = "utf-8")
        except IndexError:
            pass
        
        try:        
            ValueBatting = dataScrape.playerdata(t, year, "players_value_batting")
            ValueBatting.to_csv(directory + "/" + t + "_" + str(year) + "_Valuebatting.csv", index = False, encoding = "utf-8")
        except IndexError:
            pass
    
        try:
            ValuePitching = dataScrape.playerdata(t, year, "players_value_pitching")
            ValuePitching.to_csv(directory + "/" + t + "_" + str(year) + "_Valuepitching.csv", index = False, encoding = "utf-8")
        except IndexError:
            pass

if checkold:
    for year in years:      
        for t in oldteams:
            try:
                Batting = dataScrape.playerdata(t, year, "team_batting")
                Batting.to_csv(directory + "/" + t + "_" + str(year) + "_batting.csv", index = False, encoding = "utf-8")
            except IndexError:
                pass
                
            try:
                Pitching = dataScrape.playerdata(t, year, "team_pitching")
                Pitching.to_csv(directory + "/" + t + "_" + str(year) + "_pitching.csv", index = False, encoding = "utf-8")
            except IndexError:
                pass
                
            try:        
                Fielding = dataScrape.playerdata(t, year, "standard_fielding")
                Fielding.to_csv(directory + "/" + t + "_" + str(year) + "_fielding.csv", index = False, encoding = "utf-8")
            except IndexError:
                pass
                
            try:        
                ValueBatting = dataScrape.playerdata(t, year, "players_value_batting")
                ValueBatting.to_csv(directory + "/" + t + "_" + str(year) + "_Valuebatting.csv", index = False, encoding = "utf-8")
            except IndexError:
                pass
                
            try:
                ValuePitching = dataScrape.playerdata(t, year, "players_value_pitching")
                ValuePitching.to_csv(directory + "/" + t + "_" + str(year) + "_Valuepitching.csv", index = False, encoding = "utf-8")
            except IndexError:
                pass
