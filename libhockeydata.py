#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2018 Cool Dude 2k - http://idb.berlios.de/
    Copyright 2018 Game Maker 2k - http://intdb.sourceforge.net/
    Copyright 2018 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: libhockeydata.py - Last Update: 1/29/2018 Ver. 0.0.1 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals;
import sqlite3, sys, os, re;
import xml.etree.ElementTree as ET;

__program_name__ = "PyHockeyStats";
__project__ = __program_name__;
__project_url__ = "https://github.com/GameMaker2k/Neo-Hockey-Test";
__version_info__ = (0, 0, 1, "RC 1", 1);
__version_date_info__ = (2018, 1, 28, "RC 1", 1);
__version_date__ = str(__version_date_info__[0])+"."+str(__version_date_info__[1]).zfill(2)+"."+str(__version_date_info__[2]).zfill(2);
if(__version_info__[4] is not None):
 __version_date_plusrc__ = __version_date__+"-"+str(__version_date_info__[4]);
if(__version_info__[4] is None):
 __version_date_plusrc__ = __version_date__;
if(__version_info__[3] is not None):
 __version__ = str(__version_info__[0])+"."+str(__version_info__[1])+"."+str(__version_info__[2])+" "+str(__version_info__[3]);
if(__version_info__[3] is None):
 __version__ = str(__version_info__[0])+"."+str(__version_info__[1])+"."+str(__version_info__[2]);

def MakeHockeyDatabase(filename, synchronous="FULL", journal_mode="DELETE"):
 print("Creating Hockey Database.");
 sqlcon = sqlite3.connect(filename, isolation_level=None);
 sqlcur = sqlcon.cursor();
 sqldatacon = (sqlcur, sqlcon);
 sqlcur.execute("PRAGMA encoding = \"UTF-8\";");
 sqlcur.execute("PRAGMA auto_vacuum = 1;");
 sqlcur.execute("PRAGMA foreign_keys = 0;");
 sqlcur.execute("PRAGMA synchronous = "+str(synchronous)+";");
 sqlcur.execute("PRAGMA journal_mode = "+str(journal_mode)+";");
 return sqldatacon;

def GetLastTenGames(sqldatacon, leaguename, teamname):
 wins = 0;
 losses = 0;
 otlosses = 0;
 getlastninegames = sqldatacon[0].execute("SELECT NumberPeriods, TeamWin FROM "+leaguename+"Games WHERE (HomeTeam=\""+str(teamname)+"\" OR AwayTeam=\""+str(teamname)+"\") ORDER BY id DESC LIMIT 10").fetchall();
 nmax = len(getlastninegames);
 nmin = 0;
 while(nmin<nmax):
  if(teamname==str(getlastninegames[nmin][1])):
   wins = wins + 1;
  if(teamname!=str(getlastninegames[nmin][1])):
   if(int(getlastninegames[nmin][0])==3):
    losses = losses + 1;
   if(int(getlastninegames[nmin][0])>3):
    otlosses = otlosses + 1;
  nmin = nmin + 1;
 return str(wins)+":"+str(losses)+":"+str(otlosses);

def UpdateTeamData(sqldatacon, leaguename, teamid, dataname, addtodata, addtype):
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0]) + addtodata;
 if(addtype=="-"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0]) - addtodata;
 sqldatacon[0].execute("UPDATE "+leaguename+"Teams SET "+dataname+"="+str(TMPData)+" WHERE id="+str(teamid));
 return int(TMPData);

def UpdateTeamDataString(sqldatacon, leaguename, teamid, dataname, newdata):
 sqldatacon[0].execute("UPDATE "+leaguename+"Teams SET "+dataname+"=\""+str(newdata)+"\" WHERE id="+str(teamid));
 return True;

def GetTeamData(sqldatacon, leaguename, teamid, dataname, datatype):
 if(datatype=="float"):
  TMPData = float(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0]);
 if(datatype=="int"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0]);
 if(datatype=="str"):
  TMPData = str(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0]);
 return TMPData;

def UpdateGameData(sqldatacon, leaguename, gameid, dataname, addtodata, addtype):
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Games WHERE id="+str(gameid)).fetchone()[0]) + addtodata;
 if(addtype=="-"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Games WHERE id="+str(gameid)).fetchone()[0]) - addtodata;
 sqldatacon[0].execute("UPDATE "+leaguename+"Games SET "+dataname+"="+str(TMPData)+" WHERE id="+str(gameid));
 return int(TMPData);

def UpdateGameDataString(sqldatacon, leaguename, gameid, dataname, newdata):
 sqldatacon[0].execute("UPDATE "+leaguename+"Games SET "+dataname+"=\""+str(newdata)+"\" WHERE id="+str(gameid));
 return True;

def GetGameData(sqldatacon, leaguename, gameid, dataname, datatype):
 if(datatype=="float"):
  TMPData = float(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Games WHERE id="+str(gameid)).fetchone()[0]);
 if(datatype=="int"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Games WHERE id="+str(gameid)).fetchone()[0]);
 if(datatype=="str"):
  TMPData = str(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Games WHERE id="+str(gameid)).fetchone()[0]);
 return TMPData;

def UpdateArenaData(sqldatacon, leaguename, arenaid, dataname, addtodata, addtype):
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0]) + addtodata;
 if(addtype=="-"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0]) - addtodata;
 sqldatacon[0].execute("UPDATE "+leaguename+"Arenas SET "+dataname+"="+str(TMPData)+" WHERE id="+str(arenaid));
 return int(TMPData);

def UpdateArenaDataString(sqldatacon, leaguename, arenaid, dataname, newdata):
 sqldatacon[0].execute("UPDATE "+leaguename+"Arenas SET "+dataname+"=\""+str(newdata)+"\" WHERE id="+str(arenaid));
 return True;

def GetArenaData(sqldatacon, leaguename, arenaid, dataname, datatype):
 if(datatype=="float"):
  TMPData = float(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0]);
 if(datatype=="int"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0]);
 if(datatype=="str"):
  TMPData = str(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0]);
 return TMPData;

def UpdateConferenceData(sqldatacon, leaguename, conference, dataname, addtodata, addtype):
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Conferences WHERE Conference=\""+str(conference)+"\"").fetchone()[0]) + addtodata;
 if(addtype=="-"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Conferences WHERE Conference=\""+str(conference)+"\"").fetchone()[0]) - addtodata;
 sqldatacon[0].execute("UPDATE "+leaguename+"Conferences SET "+dataname+"="+str(TMPData)+" WHERE Conference=\""+str(conference)+"\"");
 return int(TMPData);

def UpdateDivisionData(sqldatacon, leaguename, division, dataname, addtodata, addtype):
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Divisions WHERE Division=\""+str(division)+"\"").fetchone()[0]) + addtodata;
 if(addtype=="-"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Divisions WHERE Division=\""+str(division)+"\"").fetchone()[0]) - addtodata;
 sqldatacon[0].execute("UPDATE "+leaguename+"Divisions SET "+dataname+"="+str(TMPData)+" WHERE Division=\""+str(division)+"\"");
 return int(TMPData);

def UpdateLeagueData(sqldatacon, leaguename, dataname, addtodata, addtype):
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM HockeyLeagues WHERE LeagueName=\""+str(leaguename)+"\"").fetchone()[0]) + addtodata;
 if(addtype=="-"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM HockeyLeagues WHERE LeagueName=\""+str(leaguename)+"\"").fetchone()[0]) - addtodata;
 sqldatacon[0].execute("UPDATE HockeyLeagues SET "+dataname+"="+str(TMPData)+" WHERE LeagueName=\""+str(leaguename)+"\"");
 return int(TMPData);

def GetLeagueName(sqldatacon, leaguename):
 TMPData = str(sqldatacon[0].execute("SELECT LeagueFullName FROM HockeyLeagues WHERE LeagueName=\""+str(leaguename)+"\"").fetchone()[0]);
 return TMPData;

def GetNum2Team(sqldatacon, leaguename, TeamNum, ReturnVar):
 return str(sqldatacon[0].execute("SELECT "+ReturnVar+" FROM "+leaguename+"Teams WHERE id="+str(TeamNum)).fetchone()[0]);

def GetTeam2Num(sqldatacon, leaguename, TeamName):
 return int(sqldatacon[0].execute("SELECT id FROM "+leaguename+"Teams WHERE FullName=\""+str(TeamName)+"\"").fetchone()[0]);

def GetNum2Arena(sqldatacon, leaguename, ArenaNum, ReturnVar):
 return str(sqldatacon[0].execute("SELECT "+ReturnVar+" FROM "+leaguename+"Arenas WHERE id="+str(ArenaNum)).fetchone()[0]);

def GetArena2Num(sqldatacon, leaguename, ArenaName):
 return int(sqldatacon[0].execute("SELECT id FROM "+leaguename+"Arenas WHERE FullArenaName=\""+str(ArenaName)+"\"").fetchone()[0]);

def MakeHockeyLeagueTable(sqldatacon, leaguename):
 print("Creating "+leaguename+" League Table.");
 print(" ");
 sqldatacon[0].execute("DROP TABLE IF EXISTS HockeyLeagues");
 sqldatacon[0].execute("CREATE TABLE HockeyLeagues(id INTEGER PRIMARY KEY, LeagueName TEXT, LeagueFullName TEXT, CountryName TEXT, FullCountryName TEXT, NumberOfTeams INTEGER, NumberOfConferences INTEGER, NumberOfDivisions INTEGER)");
 return True;

def MakeHockeyLeagues(sqldatacon, leaguename, leaguefullname, countryname, fullcountryname):
 print("League Name: "+leaguename);
 print(" ");
 sqldatacon[0].execute("INSERT INTO HockeyLeagues(LeagueName, LeagueFullName, CountryName, FullCountryName, NumberOfTeams, NumberOfConferences, NumberOfDivisions) VALUES(\""+str(leaguename)+"\", \""+str(leaguefullname)+"\", \""+str(countryname)+"\", \""+str(fullcountryname)+"\", 0, 0, 0)");
 return True;

def MakeHockeyConferenceTable(sqldatacon, leaguename):
 print("Creating "+leaguename+" Conference Table.");
 print(" ");
 sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Conferences");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Conferences(id INTEGER PRIMARY KEY, Conference TEXT, LeagueName TEXT, LeagueFullName TEXT, NumberOfTeams INTEGER, NumberOfDivisions INTEGER)");
 return True;

def MakeHockeyConferences(sqldatacon, leaguename, conference):
 print("League Name: "+leaguename);
 print("Conference Name: "+conference);
 print(" ");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Conferences(Conference, LeagueName, LeagueFullName, NumberOfTeams, NumberOfDivisions) VALUES(\""+str(conference)+"\", \""+leaguename+"\", \""+GetLeagueName(sqldatacon, leaguename)+"\", 0, 0)");
 UpdateLeagueData(sqldatacon, leaguename, "NumberOfConferences", 1, "+");
 return True;

def MakeHockeyDivisionTable(sqldatacon, leaguename):
 print("Creating "+leaguename+" Division Table.");
 print(" ");
 sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Divisions");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Divisions(id INTEGER PRIMARY KEY, Division TEXT, Conference TEXT, LeagueName TEXT, LeagueFullName TEXT, NumberOfTeams INTEGER)");
 return True;

def MakeHockeyDivisions(sqldatacon, leaguename, division, conference):
 print("League Name: "+leaguename);
 print("Conference Name: "+conference);
 print("Division Name: "+division);
 print(" ");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Divisions(Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES(\""+str(division)+"\", \""+str(conference)+"\", \""+leaguename+"\", \""+GetLeagueName(sqldatacon, leaguename)+"\", 0)");
 UpdateConferenceData(sqldatacon, leaguename, conference, "NumberOfDivisions", 1, "+");
 UpdateLeagueData(sqldatacon, leaguename, "NumberOfDivisions", 1, "+");
 return True;

def MakeHockeyTeamTable(sqldatacon, leaguename):
 print("Creating "+leaguename+" Arena Table.");
 print(" ");
 sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Arenas");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Arenas(id INTEGER PRIMARY KEY, TeamID INTEGER, TeamName TEXT, TeamFullName TEXT, CityName TEXT, AreaName TEXT, CountryName TEXT, FullCountryName TEXT, FullCityName TEXT, FullAreaName TEXT, FullCityNameAlt TEXT, ArenaName TEXT, FullArenaName TEXT, GamesPlayed INTEGER, FOREIGN KEY(TeamID) REFERENCES "+leaguename+"Teams(id))");
 print("Creating "+leaguename+" Team Table.");
 print(" ");
 sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Teams");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Teams(id INTEGER PRIMARY KEY, Date INTEGER, FullName TEXT, CityName TEXT, TeamPrefix TEXT, AreaName TEXT, CountryName TEXT, FullCountryName TEXT, FullCityName TEXT, FullAreaName TEXT, FullCityNameAlt TEXT, TeamName TEXT, Conference TEXT, Division TEXT, LeagueName TEXT, LeagueFullName TEXT, ArenaName TEXT, FullArenaName TEXT, GamesPlayed INTEGER, GamesPlayedHome INTEGER, GamesPlayedAway INTEGER, Wins INTEGER, OTWins INTEGER, SOWins INTEGER, OTSOWins INTEGER, TWins INTEGER, Losses INTEGER, OTLosses INTEGER, SOLosses INTEGER, OTSOLosses INTEGER, TLosses INTEGER, ROW INTEGER, ROT INTEGER, ShutoutWins INTEGER, ShutoutLosses INTEGER, HomeRecord TEXT, AwayRecord TEXT, Shootouts TEXT, GoalsFor INTEGER, GoalsAgainst INTEGER, GoalsDifference INTEGER, SOGFor INTEGER, SOGAgainst INTEGER, SOGDifference INTEGER, ShotsBlockedFor INTEGER, ShotsBlockedAgainst INTEGER, ShotsBlockedDifference INTEGER, PPGFor INTEGER, PPGAgainst INTEGER, PPGDifference INTEGER, PenaltiesFor INTEGER, PenaltiesAgainst INTEGER, PenaltiesDifference INTEGER, PIMFor INTEGER, PIMAgainst INTEGER, PIMDifference INTEGER, HITSFor INTEGER, HITSAgainst INTEGER, HITSDifference INTEGER, TakeAways INTEGER, GiveAways INTEGER, TAGADifference INTEGER, FaceoffWins INTEGER, FaceoffLosses INTEGER, FaceoffDifference INTEGER, Points INTEGER, PCT REAL, LastTen TEXT, Streak TEXT)");
 print("Creating "+leaguename+" Stat Table.");
 print(" ");
 sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Stats");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Stats(id INTEGER PRIMARY KEY, TeamID INTEGER, Date INTEGER, FullName TEXT, CityName TEXT, TeamPrefix TEXT, AreaName TEXT, CountryName TEXT, FullCountryName TEXT, FullCityName TEXT, FullAreaName TEXT, FullCityNameAlt TEXT, TeamName TEXT, Conference TEXT, Division TEXT, LeagueName TEXT, LeagueFullName TEXT, ArenaName TEXT, FullArenaName TEXT, GamesPlayed INTEGER, GamesPlayedHome INTEGER, GamesPlayedAway INTEGER, Wins INTEGER, OTWins INTEGER, SOWins INTEGER, OTSOWins INTEGER, TWins INTEGER, Losses INTEGER, OTLosses INTEGER, SOLosses INTEGER, OTSOLosses INTEGER, TLosses INTEGER, ROW INTEGER, ROT INTEGER, ShutoutWins INTEGER, ShutoutLosses INTEGER, HomeRecord TEXT, AwayRecord TEXT, Shootouts TEXT, GoalsFor INTEGER, GoalsAgainst INTEGER, GoalsDifference INTEGER, SOGFor INTEGER, SOGAgainst INTEGER, SOGDifference INTEGER, ShotsBlockedFor INTEGER, ShotsBlockedAgainst INTEGER, ShotsBlockedDifference INTEGER, PPGFor INTEGER, PPGAgainst INTEGER, PPGDifference INTEGER, PenaltiesFor INTEGER, PenaltiesAgainst INTEGER, PenaltiesDifference INTEGER, PIMFor INTEGER, PIMAgainst INTEGER, PIMDifference INTEGER, HITSFor INTEGER, HITSAgainst INTEGER, HITSDifference INTEGER, TakeAways INTEGER, GiveAways INTEGER, TAGADifference INTEGER, FaceoffWins INTEGER, FaceoffLosses INTEGER, FaceoffDifference INTEGER, Points INTEGER, PCT REAL, LastTen TEXT, Streak TEXT, FOREIGN KEY(TeamID) REFERENCES "+leaguename+"Teams(id))");
 print("Creating "+leaguename+" Game Stat Table.");
 print(" ");
 sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"GameStats");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"GameStats(id INTEGER PRIMARY KEY, GameID INTEGER, Date INTEGER, TeamID INTEGER, FullName TEXT, CityName TEXT, TeamPrefix TEXT, AreaName TEXT, CountryName TEXT, FullCountryName TEXT, FullCityName TEXT, FullAreaName TEXT, FullCityNameAlt TEXT, TeamName TEXT, Conference TEXT, Division TEXT, LeagueName TEXT, LeagueFullName TEXT, ArenaName TEXT, FullArenaName TEXT, GoalsFor INTEGER, GoalsAgainst INTEGER, GoalsDifference INTEGER, SOGFor INTEGER, SOGAgainst INTEGER, SOGDifference INTEGER, ShotsBlockedFor INTEGER, ShotsBlockedAgainst INTEGER, ShotsBlockedDifference INTEGER, PPGFor INTEGER, PPGAgainst INTEGER, PPGDifference INTEGER, PenaltiesFor INTEGER, PenaltiesAgainst INTEGER, PenaltiesDifference INTEGER, PIMFor INTEGER, PIMAgainst INTEGER, PIMDifference INTEGER, HITSFor INTEGER, HITSAgainst INTEGER, HITSDifference INTEGER, TakeAways INTEGER, GiveAways INTEGER, TAGADifference INTEGER, FaceoffWins INTEGER, FaceoffLosses INTEGER, FaceoffDifference INTEGER, FOREIGN KEY(GameID) REFERENCES "+leaguename+"Games(id), FOREIGN KEY(TeamID) REFERENCES "+leaguename+"Teams(id))");
 return True;

def MakeHockeyTeams(sqldatacon, leaguename, date, cityname, areaname, countryname, fullcountryname, fullareaname, teamname, conference, division, arenaname, teamnameprefix):
 print("Team Name: "+teamname);
 print("Arena Name: "+arenaname);
 print("City Name: "+cityname);
 print("Full City Name: "+cityname+", "+areaname);
 print("Full Name: "+teamnameprefix+" "+teamname);
 print("League: "+leaguename);
 print("Conference: "+conference);
 print("Division: "+division);
 print(" ");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Teams(Date, FullName, CityName, TeamPrefix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES(\""+str(date)+"\", \""+str(teamnameprefix+" "+teamname)+"\", \""+str(cityname)+"\", \""+str(teamnameprefix)+"\", \""+str(areaname)+"\", \""+str(countryname)+"\", \""+str(fullcountryname)+"\", \""+str(cityname+", "+areaname)+"\", \""+str(fullareaname)+"\", \""+str(cityname+", "+fullareaname)+"\", \""+str(teamname)+"\", \""+str(conference)+"\", \""+str(division)+"\", \""+leaguename+"\", \""+GetLeagueName(sqldatacon, leaguename)+"\", \""+str(arenaname)+"\", \""+str(arenaname+", "+cityname)+"\", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \"0:0:0\", \"0:0:0\", \"0:0\", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \"0:0:0\", \"None\")");
 TeamID = int(sqldatacon[0].lastrowid);
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Stats (TeamID, Date, FullName, CityName, TeamPrefix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) SELECT id, Date, FullName, CityName, TeamPrefix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PPGFor, PPGAgainst, PPGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE FullName=\""+teamnameprefix+" "+teamname+"\";");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Arenas(TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES("+str(TeamID)+", \""+str(teamname)+"\", \""+str(teamnameprefix+" "+teamname)+"\", \""+str(cityname)+"\", \""+str(areaname)+"\", \""+str(countryname)+"\", \""+str(fullcountryname)+"\", \""+str(cityname+", "+areaname)+"\", \""+str(fullareaname)+"\", \""+str(cityname+", "+fullareaname)+"\", \""+str(arenaname)+"\", \""+str(arenaname+", "+cityname)+"\", 0)");
 UpdateConferenceData(sqldatacon, leaguename, conference, "NumberOfTeams", 1, "+");
 UpdateDivisionData(sqldatacon, leaguename, division, "NumberOfTeams", 1, "+");
 UpdateLeagueData(sqldatacon, leaguename, "NumberOfTeams", 1, "+");
 return True;

def MakeHockeyArena(sqldatacon, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, arenaname):
 print("Arena Name: "+arenaname);
 print("City Name: "+cityname);
 print("Full City Name: "+cityname+", "+areaname);
 print(" ");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Arenas(TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES(0, \"None\", \"None\", \""+str(cityname)+"\", \""+str(areaname)+"\", \""+str(countryname)+"\", \""+str(fullcountryname)+"\", \""+str(cityname+", "+areaname)+"\", \""+str(fullareaname)+"\", \""+str(cityname+", "+fullareaname)+"\", \""+str(arenaname)+"\", \""+str(arenaname+", "+cityname)+"\", 0)");
 return True;

def MakeHockeyGameTable(sqldatacon, leaguename):
 print("DONE! All Team Data Inserted.");
 print("Creating "+leaguename+" Game Table.");
 print(" ");
 sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Games");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Games(id INTEGER PRIMARY KEY, Date INTEGER, HomeTeam TEXT, AwayTeam TEXT, AtArena TEXT, TeamScorePeriods TEXT, TeamFullScore TEXT, ShotsOnGoal TEXT, FullShotsOnGoal TEXT, ShotsBlocked TEXT, FullShotsBlocked TEXT, PowerPlays TEXT, FullPowerPlays TEXT, Penalties TEXT, FullPenalties TEXT, PenaltyMinutes TEXT, FullPenaltyMinutes TEXT, HitsPerPeriod TEXT, FullHitsPerPeriod TEXT, TakeAways TEXT, FullTakeAways TEXT, GiveAways TEXT, FullGiveAways TEXT, FaceoffWins TEXT, FullFaceoffWins TEXT, NumberPeriods INTEGER, TeamWin TEXT, TeamLost TEXT, IsPlayOffGame INTEGER)");
 return True;

def MakeHockeyGame(sqldatacon, leaguename, date, hometeam, awayteam, periodsscore, shotsongoal, ppgoals, periodpens, periodpims, periodhits, takeaways, faceoffwins, atarena, isplayoffgame):
 isplayoffgsql = "0";
 if(isplayoffgame==True):
  isplayoffgsql = "1";
 if(isplayoffgame==False):
  isplayoffsql = "0";
 periodssplit = periodsscore.split(",");
 periodcounting = 0;
 numberofperiods=int(len(periodssplit));
 homescore = 0;
 awayscore = 0;
 homeperiodscore = "";
 awayperiodscore = "";
 while(periodcounting<numberofperiods):
  periodscoresplit = periodssplit[periodcounting].split(":");
  homeperiodscore = homeperiodscore+" "+str(periodscoresplit[0]);
  awayperiodscore = awayperiodscore+" "+str(periodscoresplit[1]);
  if(periodcounting <= 3):
   homescore = homescore + int(periodscoresplit[0]);
   awayscore = awayscore + int(periodscoresplit[1]);
  if(isplayoffgame==True and periodcounting > 3):
   homescore = homescore + int(periodscoresplit[0]);
   awayscore = awayscore + int(periodscoresplit[1]);
  if(isplayoffgame==False and periodcounting > 3):
   if(periodscoresplit[0] > periodscoresplit[1]):
    homescore = homescore + 1;
   if(periodscoresplit[0] < periodscoresplit[1]):
    awayscore = awayscore + 1;
  periodcounting = periodcounting + 1;
 totalscore = str(homescore)+":"+str(awayscore);
 teamscores=totalscore.split(":");
 shotsongoalsplit = shotsongoal.split(",");
 periodssplits = periodsscore.split(",");
 ppgoalssplits = ppgoals.split(",");
 periodpimssplits = periodpims.split(",");
 periodpenssplits = periodpens.split(",");
 periodhitssplits = periodhits.split(",");
 takeawayssplits = takeaways.split(",");
 faceoffwinssplits = faceoffwins.split(",");
 numberofsogperiods=int(len(shotsongoalsplit));
 periodsogcounting = 0;
 homesog = 0;
 awaysog = 0;
 hometsb = 0;
 awaytsb = 0;
 homeppg = 0;
 awayppg = 0;
 homepims = 0;
 awaypims = 0;
 homepens = 0;
 awaypens = 0;
 homehits = 0;
 awayhits = 0;
 hometaws = 0;
 awaytaws = 0;
 homefows = 0;
 awayfows = 0;
 sbstr = "";
 homeperiodsog = "";
 awayperiodsog = "";
 gaws_str = "";
 while(periodsogcounting<numberofsogperiods):
  periodsogsplit = shotsongoalsplit[periodsogcounting].split(":");
  periodscoresplit = periodssplits[periodsogcounting].split(":");
  periodppgsplit = ppgoalssplits[periodsogcounting].split(":");
  periodpimsplit = periodpimssplits[periodsogcounting].split(":");
  periodpensplit = periodpenssplits[periodsogcounting].split(":");
  periodhitsplit = periodhitssplits[periodsogcounting].split(":");
  periodtawsplit = takeawayssplits[periodsogcounting].split(":");
  periodfowsplit = faceoffwinssplits[periodsogcounting].split(":");
  homesog = homesog + int(periodsogsplit[0]);
  homesb = int(periodsogsplit[0]) - int(periodscoresplit[0]);
  hometsb = homesb + hometsb;
  homeppg = homeppg + int(periodppgsplit[0]);
  homepims = homepims + int(periodpimsplit[0]);
  homepens = homepens + int(periodpensplit[0]);
  homehits = homehits + int(periodhitsplit[0]);
  hometaws = hometaws + int(periodtawsplit[0]);
  homefows = homefows + int(periodfowsplit[0]);
  awaysog = awaysog + int(periodsogsplit[1]);
  awaysb = int(periodsogsplit[1]) - int(periodscoresplit[1]);
  awaytsb = awaysb + awaytsb;
  awayppg = awayppg + int(periodppgsplit[1]);
  awaypims = awaypims + int(periodpimsplit[1]);
  awaypens = awaypens + int(periodpensplit[1]);
  awayhits = awayhits + int(periodhitsplit[1]);
  awaytaws = awaytaws + int(periodtawsplit[1]);
  awayfows = awayfows + int(periodfowsplit[1]);
  sbstr = sbstr+str(homesb)+":"+str(awaysb)+" ";
  gaws_str = gaws_str+str(periodtawsplit[1])+":"+str(periodtawsplit[0])+" ";
  periodsogcounting = periodsogcounting + 1;
 sbstr = sbstr.rstrip();
 sbstr = sbstr.replace(" ", ",");
 gaws_str = gaws_str.rstrip();
 gaws_str = gaws_str.replace(" ", ",");
 tsbstr = str(hometsb)+":"+str(awaytsb);
 totalsog = str(homesog)+":"+str(awaysog);
 totalppg = str(homeppg)+":"+str(awayppg);
 totalpims = str(homepims)+":"+str(awaypims);
 totalpens = str(homepens)+":"+str(awaypens);
 totalhits = str(homehits)+":"+str(awayhits);
 totaltaws = str(hometaws)+":"+str(awaytaws);
 totalgaws = str(awaytaws)+":"+str(hometaws);
 totalfows = str(homefows)+":"+str(awayfows);
 teamssog=totalsog.split(":");
 hometeamname = hometeam;
 hometeam = GetTeam2Num(sqldatacon, leaguename, hometeam);
 awayteamname = awayteam;
 awayteam = GetTeam2Num(sqldatacon, leaguename, awayteam);
 if(atarena.isdigit()):
  atarena = int(atarena);
 if(atarena==0):
  atarena = hometeam;
  atarenaname = GetTeamData(sqldatacon, leaguename, hometeam, "FullArenaName", "str");
 if(atarena==-1):
  atarena = awayteam;
  atarenaname = GetTeamData(sqldatacon, leaguename, awayteam, "FullArenaName", "str");
 if(isinstance(atarena, int) and atarena>0):
  atarenaname = GetNum2Arena(sqldatacon, leaguename, atarena, "FullArenaName");
 if(isinstance(atarena, str)):
  atarenaname = atarena;
  atarena = GetArena2Num(sqldatacon, leaguename, atarenaname);
 print("Home Arena: "+str(atarenaname));
 print("Home Team: "+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullName"));
 print("Home Period Scores:"+homeperiodscore);
 print("Home Score: "+str(teamscores[0]));
 print("Away Team: "+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullName"));
 print("Away Period Scores:"+awayperiodscore);
 print("Away Score: "+str(teamscores[1]));
 print("Number Of Periods: "+str(numberofperiods));
 if(teamscores[0] > teamscores[1]):
  print("Winning Team: "+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullName"));
  print("Losing Team: "+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullName"));
  losingteam = awayteam;
  winningteam = hometeam;
  winningteamname = hometeamname;
  losingteamname = awayteamname;
 if(teamscores[0] < teamscores[1]):
  print("Winning Team: "+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullName"));
  print("Losing Team: "+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullName"));
  losingteam = hometeam;
  winningteam = awayteam;
  winningteamname = awayteamname;
  losingteamname = hometeamname;
 print(" ");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Games(Date, HomeTeam, AwayTeam, AtArena, TeamScorePeriods, TeamFullScore, ShotsOnGoal, FullShotsOnGoal, ShotsBlocked, FullShotsBlocked, PowerPlays, FullPowerPlays, Penalties, FullPenalties, PenaltyMinutes, FullPenaltyMinutes, HitsPerPeriod, FullHitsPerPeriod, TakeAways, FullTakeAways, GiveAways, FullGiveAways, FaceoffWins, FullFaceoffWins, NumberPeriods, TeamWin, TeamLost, IsPlayOffGame) VALUES("+str(date)+", \""+str(hometeamname)+"\", \""+str(awayteamname)+"\", \""+str(atarenaname)+"\", \""+str(periodsscore)+"\", \""+str(totalscore)+"\", \""+str(shotsongoal)+"\", \""+str(totalsog)+"\", \""+str(sbstr)+"\", \""+str(tsbstr)+"\", \""+str(ppgoals)+"\", \""+str(totalppg)+"\", \""+str(periodpens)+"\", \""+str(totalpens)+"\", \""+str(periodpims)+"\", \""+str(totalpims)+"\", \""+str(periodhits)+"\", \""+str(totalhits)+"\", \""+str(takeaways)+"\", \""+str(totaltaws)+"\", \""+str(gaws_str)+"\", \""+str(totalgaws)+"\", \""+str(faceoffwins)+"\", \""+str(totalfows)+"\", "+str(numberofperiods)+", \""+str(winningteamname)+"\", \""+str(losingteamname)+"\", "+str(isplayoffgsql)+")");
 GameID = int(sqldatacon[0].lastrowid);
 UpdateArenaData(sqldatacon, leaguename, atarena, "GamesPlayed", 1, "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "Date", int(date), "=");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "GamesPlayed", 1, "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "GamesPlayedHome", 1, "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "GoalsFor", int(teamscores[0]), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "GoalsAgainst", int(teamscores[1]), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "GoalsDifference", int(int(teamscores[0]) - int(teamscores[1])), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "SOGFor", int(teamssog[0]), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "SOGAgainst", int(teamssog[1]), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "SOGDifference", int(int(teamssog[0]) - int(teamssog[1])), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "ShotsBlockedFor", int(hometsb), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "ShotsBlockedAgainst", int(awaytsb), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "ShotsBlockedDifference", int(int(hometsb) - int(awaytsb)), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PPGFor", int(homeppg), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PPGAgainst", int(awayppg), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PPGDifference", int(int(homeppg) - int(awayppg)), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PenaltiesFor", int(awaypens), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PenaltiesAgainst", int(homepens), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PenaltiesDifference", int(int(awaypens) - int(homepens)), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PIMFor", int(homepims), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PIMAgainst", int(awaypims), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PIMDifference", int(int(homepims) - int(awaypims)), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "HITSFor", int(homehits), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "HITSAgainst", int(awayhits), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "HITSDifference", int(int(homehits) - int(awayhits)), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "TakeAways", int(hometaws), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "GiveAways", int(awaytaws), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "TAGADifference", int(int(hometaws) - int(awaytaws)), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "FaceoffWins", int(homefows), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "FaceoffLosses", int(awayfows), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "FaceoffDifference", int(int(homefows) - int(awayfows)), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "Date", int(date), "=");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "GamesPlayed", 1, "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "GamesPlayedAway", 1, "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "GoalsFor", int(teamscores[1]), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "GoalsAgainst", int(teamscores[0]), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "GoalsDifference", int(int(teamscores[1]) - int(teamscores[0])), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "SOGFor", int(teamssog[1]), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "SOGAgainst", int(teamssog[0]), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "SOGDifference", int(int(teamssog[1]) - int(teamssog[0])), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "ShotsBlockedFor", int(awaytsb), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "ShotsBlockedAgainst", int(hometsb), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "ShotsBlockedDifference", int(int(awaytsb) - int(hometsb)), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PPGFor", int(awayppg), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PPGAgainst", int(homeppg), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PPGDifference", int(int(awayppg) - int(homeppg)), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PenaltiesFor", int(homepens), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PenaltiesAgainst", int(awaypens), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PenaltiesDifference", int(int(homepens) - int(awaypens)), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PIMFor", int(awaypims), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PIMAgainst", int(homepims), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PIMDifference", int(int(awaypims) - int(homepims)), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "HITSFor", int(awayhits), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "HITSAgainst", int(homehits), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "HITSDifference", int(int(awayhits) - int(homehits)), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "TakeAways", int(awaytaws), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "GiveAways", int(hometaws), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "TAGADifference", int(int(awaytaws) - int(hometaws)), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "FaceoffWins", int(awayfows), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "FaceoffLosses", int(homefows), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "FaceoffDifference", int(int(awayfows) - int(homefows)), "+");
 if(winningteam==hometeam and int(teamscores[1])==0):
  UpdateTeamData(sqldatacon, leaguename, hometeam, "ShutoutWins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, awayteam, "ShutoutLosses", 1, "+");
 if(winningteam==awayteam and int(teamscores[0])==0):
  UpdateTeamData(sqldatacon, leaguename, awayteam, "ShutoutWins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, hometeam, "ShutoutLosses", 1, "+");
 UpdateTeamDataString(sqldatacon, leaguename, winningteam, "LastTen", GetLastTenGames(sqldatacon, leaguename, winningteamname));
 UpdateTeamDataString(sqldatacon, leaguename, losingteam, "LastTen", GetLastTenGames(sqldatacon, leaguename, losingteamname));
 GetWinningStreak = GetTeamData(sqldatacon, leaguename, winningteam, "Streak", "str");
 GetWinningStreakNext = "Won 1";
 if(GetWinningStreak!="None"):
  GetWinningStreakSplit = re.findall("([a-zA-Z]+) ([0-9]+)", GetWinningStreak);
  if(GetWinningStreakSplit[0][0]=="Won"):
   GetWinningStreakNext = "Won "+str(int(GetWinningStreakSplit[0][1]) + 1);
  if(GetWinningStreakSplit[0][0]=="Lost"):
   GetWinningStreakNext = "Won 1";
  if(GetWinningStreakSplit[0][0]=="OT"):
   GetWinningStreakNext = "Won 1";
 UpdateTeamDataString(sqldatacon, leaguename, winningteam, "Streak", GetWinningStreakNext);
 GetLosingStreak = GetTeamData(sqldatacon, leaguename, losingteam, "Streak", "str");
 if(numberofperiods==3):
  GetLosingStreakNext = "Lost 1";
 if(numberofperiods>3):
  GetLosingStreakNext = "OT 1";
 if(GetLosingStreak!="None"):
  GetLosingStreakSplit = re.findall("([a-zA-Z]+) ([0-9]+)", GetLosingStreak);
  if(GetLosingStreakSplit[0][0]=="Won"):
   if(numberofperiods==3):
    GetLosingStreakNext = "Lost 1";
   if(numberofperiods>3):
    GetLosingStreakNext = "OT 1";
  if(GetLosingStreakSplit[0][0]=="Lost"):
   if(numberofperiods==3):
    GetLosingStreakNext = "Lost "+str(int(GetLosingStreakSplit[0][1]) + 1);
   if(numberofperiods>3):
    GetLosingStreakNext = "OT 1";
  if(GetLosingStreakSplit[0][0]=="OS"):
   if(numberofperiods==3):
    GetLosingStreakNext = "Lost 1";
   if(numberofperiods>3):
    GetLosingStreakNext = "OT "+str(int(GetLosingStreakSplit[0][1]) + 1);
 UpdateTeamDataString(sqldatacon, leaguename, losingteam, "Streak", GetLosingStreakNext);
 if((isplayoffgame==False and numberofperiods<5) or (isplayoffgame==True)):
  UpdateTeamData(sqldatacon, leaguename, winningteam, "ROW", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "ROT", 1, "+");
 if(numberofperiods==3):
  UpdateTeamData(sqldatacon, leaguename, winningteam, "Wins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, winningteam, "TWins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, winningteam, "Points", 2, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "Losses", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "TLosses", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "Points", 0, "+");
  if(winningteam==hometeam):
   HomeTeamRecord = GetTeamData(sqldatacon, leaguename, winningteam, "HomeRecord", "str");
   HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
   NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2]);
   UpdateTeamDataString(sqldatacon, leaguename, winningteam, "HomeRecord", NewHTR);
   AwayTeamRecord = GetTeamData(sqldatacon, leaguename, losingteam, "AwayRecord", "str");
   ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
   NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1] + 1)+":"+str(ATRSpit[2]);
   UpdateTeamDataString(sqldatacon, leaguename, losingteam, "AwayRecord", NewATR);
  if(losingteam==hometeam):
   HomeTeamRecord = GetTeamData(sqldatacon, leaguename, winningteam, "AwayRecord", "str");
   HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
   NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2]);
   UpdateTeamDataString(sqldatacon, leaguename, winningteam, "AwayRecord", NewHTR);
   AwayTeamRecord = GetTeamData(sqldatacon, leaguename, losingteam, "HomeRecord", "str");
   ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
   NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1] + 1)+":"+str(ATRSpit[2]);
   UpdateTeamDataString(sqldatacon, leaguename, losingteam, "HomeRecord", NewATR);
 if(numberofperiods>3):
  if((numberofperiods==4 and isplayoffgame==False) or (numberofperiods>4 and isplayoffgame==True)):
   UpdateTeamData(sqldatacon, leaguename, winningteam, "OTWins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, winningteam, "OTSOWins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, winningteam, "TWins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, winningteam, "Points", 2, "+");
  if((numberofperiods==4 and isplayoffgame==False) or (numberofperiods>4 and isplayoffgame==True)):
   UpdateTeamData(sqldatacon, leaguename, losingteam, "OTLosses", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "OTSOLosses", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "TLosses", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "Points", 1, "+");
  if(winningteam==hometeam):
   HomeTeamRecord = GetTeamData(sqldatacon, leaguename, winningteam, "HomeRecord", "str");
   HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
   NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2]);
   UpdateTeamDataString(sqldatacon, leaguename, winningteam, "HomeRecord", NewHTR);
   AwayTeamRecord = GetTeamData(sqldatacon, leaguename, losingteam, "AwayRecord", "str");
   ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
   NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1])+":"+str(ATRSpit[2] + 1);
   UpdateTeamDataString(sqldatacon, leaguename, losingteam, "AwayRecord", NewATR);
  if(losingteam==hometeam):
   HomeTeamRecord = GetTeamData(sqldatacon, leaguename, winningteam, "AwayRecord", "str");
   HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
   NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2]);
   UpdateTeamDataString(sqldatacon, leaguename, winningteam, "AwayRecord", NewHTR);
   AwayTeamRecord = GetTeamData(sqldatacon, leaguename, losingteam, "HomeRecord", "str");
   ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
   NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1])+":"+str(ATRSpit[2] + 1);
   UpdateTeamDataString(sqldatacon, leaguename, losingteam, "HomeRecord", NewATR);
 if(isplayoffgame==False and numberofperiods>4):
  UpdateTeamData(sqldatacon, leaguename, winningteam, "SOWins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "SOLosses", 1, "+");
  WinningTeamShootouts = GetTeamData(sqldatacon, leaguename, winningteam, "Shootouts", "str");
  WTSoSplit = [int(n) for n in WinningTeamShootouts.split(":")];
  NewWTSo = str(WTSoSplit[0] + 1)+":"+str(WTSoSplit[1]);
  UpdateTeamDataString(sqldatacon, leaguename, winningteam, "Shootouts", NewWTSo);
  LosingTeamShootouts = GetTeamData(sqldatacon, leaguename, losingteam, "Shootouts", "str");
  LTSoSplit = [int(n) for n in LosingTeamShootouts.split(":")];
  NewLTSo = str(LTSoSplit[0])+":"+str(LTSoSplit[1] + 1);
  UpdateTeamDataString(sqldatacon, leaguename, losingteam, "Shootouts", NewLTSo);
 HomeOTLossesPCT = float("%.2f" % float(float(0.5) * float(GetTeamData(sqldatacon, leaguename, hometeam, "OTSOLosses", "float"))));
 HomeWinsPCT = float("%.3f" % float(float(GetTeamData(sqldatacon, leaguename, hometeam, "TWins", "float") + HomeOTLossesPCT) / float(GetTeamData(sqldatacon, leaguename, hometeam, "GamesPlayed", "float"))));
 AwayOTLossesPCT = float("%.2f" % float(float(0.5) * float(GetTeamData(sqldatacon, leaguename, awayteam, "OTSOLosses", "float"))));
 AwayWinsPCT = float("%.3f" % float(float(GetTeamData(sqldatacon, leaguename, awayteam, "TWins", "float") + AwayOTLossesPCT) / float(GetTeamData(sqldatacon, leaguename, awayteam, "GamesPlayed", "float"))));
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PCT", HomeWinsPCT, "=");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "PCT", AwayWinsPCT, "=");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"GameStats(GameID, Date, TeamID, FullName, CityName, TeamPrefix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference) VALUES("+str(GameID)+", "+str(date)+", "+str(hometeam)+", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "CityName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "TeamPrefix")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "AreaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "CountryName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullCountryName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullCityName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullAreaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullCityNameAlt")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "TeamName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "Conference")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "Division")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "LeagueName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "LeagueFullName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "ArenaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullArenaName")+"\", "+str(teamscores[0])+", "+str(teamscores[1])+", "+str(int(teamscores[0]) - int(teamscores[1]))+", "+str(teamssog[0])+", "+str(teamssog[1])+", "+str(int(teamssog[0]) - int(teamssog[1]))+", "+str(hometsb)+", "+str(awaytsb)+", "+str(int(hometsb) - int(awaytsb))+", "+str(homeppg)+", "+str(awayppg)+", "+str(int(homeppg) - int(awayppg))+", "+str(homepens)+", "+str(awaypens)+", "+str(int(homepens) - int(awaypens))+", "+str(homepims)+", "+str(awaypims)+", "+str(int(homepims) - int(awaypims))+", "+str(homehits)+", "+str(awayhits)+", "+str(int(homehits) - int(awayhits))+", "+str(hometaws)+", "+str(awaytaws)+", "+str(int(hometaws) - int(awaytaws))+", "+str(homefows)+", "+str(awayfows)+", "+str(int(homefows) - int(awayfows))+")");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"GameStats(GameID, Date, TeamID, FullName, CityName, TeamPrefix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference) VALUES("+str(GameID)+", "+str(date)+", "+str(awayteam)+", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "CityName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "TeamPrefix")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "AreaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "CountryName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullCountryName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullCityName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullAreaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullCityNameAlt")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "TeamName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "Conference")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "Division")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "LeagueName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "LeagueFullName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "ArenaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullArenaName")+"\", "+str(teamscores[1])+", "+str(teamscores[0])+", "+str(int(teamscores[1]) - int(teamscores[0]))+", "+str(teamssog[1])+", "+str(teamssog[0])+", "+str(int(teamssog[1]) - int(teamssog[0]))+", "+str(awaytsb)+", "+str(hometsb)+", "+str(int(awaytsb) - int(hometsb))+", "+str(awayppg)+", "+str(homeppg)+", "+str(int(awayppg) - int(homeppg))+", "+str(awaypens)+", "+str(homepens)+", "+str(int(awaypens) - int(homepens))+", "+str(awaypims)+", "+str(homepims)+", "+str(int(awaypims) - int(homepims))+", "+str(awayhits)+", "+str(homehits)+", "+str(int(awayhits) - int(homehits))+", "+str(awaytaws)+", "+str(hometaws)+", "+str(int(awaytaws) - int(hometaws))+", "+str(awayfows)+", "+str(homefows)+", "+str(int(awayfows) - int(homefows))+")");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Stats (TeamID, Date, FullName, CityName, TeamPrefix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) SELECT id, Date, FullName, CityName, TeamPrefix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE FullName=\""+hometeamname+"\";");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Stats (TeamID, Date, FullName, CityName, TeamPrefix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) SELECT id, Date, FullName, CityName, TeamPrefix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE FullName=\""+awayteamname+"\";");
 return True;

def CloseHockeyDatabase(sqldatacon):
 sqldatacon[0].execute("PRAGMA optimize;");
 print("Database Check Return: "+str(sqldatacon[0].execute("PRAGMA integrity_check(100);").fetchone()[0])+"\n");
 sqldatacon[0].close();
 sqldatacon[1].close();
 print("DONE! All Game Data Inserted.");
 print("DONE! Hockey Database Created.");
 return True;

def MakeHockeyDataFromXML(xmlfile):
 hockeyfile = ET.parse(xmlfile);
 gethockey = hockeyfile.getroot();
 if(gethockey.tag == "hockey"):
  sqldatacon = MakeHockeyDatabase(gethockey.attrib['database']);
 leaguecount = 0;
 for getleague in gethockey:
  if(leaguecount==0 and getleague.tag=="league"):
   MakeHockeyLeagueTable(sqldatacon, getleague.attrib['name']);
  if(getleague.tag=="league"):
   MakeHockeyTeamTable(sqldatacon, getleague.attrib['name']);
   MakeHockeyConferenceTable(sqldatacon, getleague.attrib['name']);
   MakeHockeyGameTable(sqldatacon, getleague.attrib['name']);
   MakeHockeyDivisionTable(sqldatacon, getleague.attrib['name']);
   MakeHockeyLeagues(sqldatacon, getleague.attrib['name'], getleague.attrib['fullname'], getleague.attrib['country'], getleague.attrib['fullcountry']);
  leaguecount = leaguecount + 1;
  if(getleague.tag == "league"):
   conferencecount = 0;
   for getconference in getleague:
    if(getconference.tag == "conference"):
     MakeHockeyConferences(sqldatacon, getleague.attrib['name'], getconference.attrib['name']);
     print("Inserting "+getleague.attrib['name']+" Teams From "+getconference.attrib['name']+" Conference.");
     conferencecount = conferencecount + 1;
    if(getconference.tag == "arenas"):
     arenascount = 0;
     for getarenas in getconference:
      MakeHockeyArena(sqldatacon, getleague.attrib['name'], getarenas.attrib['city'], getarenas.attrib['area'], getarenas.attrib['country'], getarenas.attrib['fullcountry'], getarenas.attrib['fullarea'], getarenas.attrib['name']);
      arenascount = arenascount + 1;
    if(getconference.tag == "games"):
     gamecount = 0;
     for getgame in getconference:
      MakeHockeyGame(sqldatacon, getleague.attrib['name'], getgame.attrib['date'], getgame.attrib['hometeam'], getgame.attrib['awayteam'], getgame.attrib['goals'], getgame.attrib['sogs'], getgame.attrib['ppgs'], getgame.attrib['penalties'], getgame.attrib['pims'], getgame.attrib['hits'], getgame.attrib['takeaways'], getgame.attrib['faceoffwins'], getgame.attrib['atarena'], getgame.attrib['isplayoffgame']);
      gamecount = gamecount + 1;
    if(getconference.tag == "conference"):
     divisioncount = 0;
     for getdivision in getconference:
      MakeHockeyDivisions(sqldatacon, getleague.attrib['name'], getdivision.attrib['name'], getconference.attrib['name']);
      print("Inserting "+getleague.attrib['name']+" Teams From "+getdivision.attrib['name']+" Division.\n");
      divisioncount = divisioncount + 1;
      if(getdivision.tag == "division"):
       teamcount = 0;
       for getteam in getdivision:
        if(getteam.tag == "team"):
         MakeHockeyTeams(sqldatacon, getleague.attrib['name'], str(gethockey.attrib['year']+gethockey.attrib['month']+gethockey.attrib['day']), getteam.attrib['city'], getteam.attrib['area'], getteam.attrib['country'], getteam.attrib['fullcountry'], getteam.attrib['fullarea'], getteam.attrib['name'], getconference.attrib['name'], getdivision.attrib['name'], getteam.attrib['arena'], getteam.attrib['prefix']);
        teamcount = teamcount + 1;
 CloseHockeyDatabase(sqldatacon);
 return True;

def MakeXMLFromHockeyData(filename, date):
 chckyear = date[:4];
 chckmonth = date[4:6];
 chckday = date[6:8];
 xmlstring = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>";
 xmlstring = xmlstring+"<hockey database=\""+filename+"\" year=\""+chckyear+"\" month=\""+chckmonth+"\" day=\""+chckday+"\">\n";
 sqlcon = sqlite3.connect(filename, isolation_level=None);
 leaguecur = sqlcon.cursor();
 getleague_num = leaguecur.execute("SELECT COUNT(*) FROM HockeyLeagues").fetchone()[0];
 getleague = leaguecur.execute("SELECT LeagueName, LeagueFullName, CountryName, FullCountryName FROM HockeyLeagues");
 for leagueinfo in getleague:
  xmlstring = xmlstring+" <league name=\""+leagueinfo[0]+"\" fullname=\""+leagueinfo[1]+"\" country=\""+leagueinfo[2]+"\" fullcountry=\""+leagueinfo[3]+"\">\n";
  conferencecur = sqlcon.cursor();
  getconference_num = conferencecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Conferences WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\"").fetchone()[0];
  getconference = conferencecur.execute("SELECT Conference FROM "+leagueinfo[0]+"Conferences WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\"");
  for conferenceinfo in getconference:
   xmlstring = xmlstring+"  <conference name=\""+conferenceinfo[0]+"\">\n";
   divisioncur = sqlcon.cursor();
   getdivision_num = divisioncur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Divisions WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\"").fetchone()[0];
   getdivision = divisioncur.execute("SELECT Division FROM "+leagueinfo[0]+"Divisions WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\"");
   for divisioninfo in getdivision:
    xmlstring = xmlstring+"   <division name=\""+divisioninfo[0]+"\">\n";
    teamcur = sqlcon.cursor();
    getteam_num = teamcur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Teams WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"").fetchone()[0];
    getteam = teamcur.execute("SELECT CityName, AreaName, FullAreaName, CountryName, FullCountryName, TeamName, ArenaName, TeamPrefix FROM "+leagueinfo[0]+"Teams WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"");
    for teaminfo in getteam:
     xmlstring = xmlstring+"    <team city=\""+teaminfo[0]+"\" area=\""+teaminfo[1]+"\" fullarea=\""+teaminfo[2]+"\" country=\""+teaminfo[3]+"\" fullcountry=\""+teaminfo[4]+"\" name=\""+teaminfo[5]+"\" arena=\""+teaminfo[6]+"\" prefix=\""+teaminfo[7]+"\" />\n";
    teamcur.close();
    xmlstring = xmlstring+"   </division>\n";
   divisioncur.close();
  xmlstring = xmlstring+"  </conference>\n";
  conferencecur.close();
  arenacur = sqlcon.cursor();
  getteam_num = arenacur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Arenas WHERE TeamID=0").fetchone()[0];
  getarena = arenacur.execute("SELECT CityName, AreaName, FullAreaName, CountryName, FullCountryName, ArenaName FROM "+leagueinfo[0]+"Arenas WHERE TeamID=0");
  if(getteam_num>0):
   xmlstring = xmlstring+"  <arenas>\n";
   for arenainfo in getarena:
    xmlstring = xmlstring+"   <arena city=\""+arenainfo[0]+"\" area=\""+arenainfo[1]+"\" fullarea=\""+arenainfo[2]+"\" country=\""+arenainfo[3]+"\" fullcountry=\""+arenainfo[4]+"\" name=\""+arenainfo[5]+"\" />\n";
   xmlstring = xmlstring+"  </arenas>\n";
  gamecur = sqlcon.cursor();
  getgame_num = gamecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Games").fetchone()[0];
  getgame = gamecur.execute("SELECT Date, HomeTeam, AwayTeam, TeamScorePeriods, ShotsOnGoal, PowerPlays, Penalties, PenaltyMinutes, HitsPerPeriod, TakeAways, FaceoffWins, AtArena, IsPlayOffGame FROM "+leagueinfo[0]+"Games");
  if(getgame_num>0):
   xmlstring = xmlstring+"  <games>\n";
   for gameinfo in getgame:
    xmlstring = xmlstring+"   <game date=\""+gameinfo[0]+"\" hometeam=\""+gameinfo[1]+"\" awayteam=\""+gameinfo[2]+"\" goals=\""+gameinfo[3]+"\" sogs=\""+gameinfo[4]+"\" ppgs=\""+gameinfo[5]+"\" penalties=\""+gameinfo[6]+"\" pims=\""+gameinfo[7]+"\" hits=\""+gameinfo[8]+"\" takeaways=\""+gameinfo[9]+"\" faceoffwins=\""+gameinfo[10]+"\" atarena=\""+gameinfo[11]+"\" isplayoffgame=\""+gameinfo[12]+"\" />\n";
   xmlstring = xmlstring+"  </games>\n";
  xmlstring = xmlstring+" </league>\n";
 xmlstring = xmlstring+"</hockey>\n";
 leaguecur.close();
 sqlcon.close();
 return xmlstring;

def MakeXMLFileFromHockeyData(filename, date, xmlfile=None):
 if(xmlfile is None):
  file_wo_extension, file_extension = os.path.splitext(filename);
  xmlfile = file_wo_extension+".xml";
 xmlfp = open(xmlfile, "w+");
 xmlfp.write(MakeXMLFromHockeyData(filename, date));
 xmlfp.close();
 return True;
