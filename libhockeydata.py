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

    $FileInfo: libhockeydata.py - Last Update: 2/5/2018 Ver. 0.0.2 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals;
import sqlite3, sys, os, re, time;
import xml.etree.ElementTree as ET;

if(sys.version[0]=="2"):
 from cgi import escape as xml_escape;
if(sys.version[0]>="3"):
 from html import escape as xml_escape;

__program_name__ = "PyHockeyStats";
__project__ = __program_name__;
__project_url__ = "https://github.com/GameMaker2k/Neo-Hockey-Test";
__version_info__ = (0, 0, 2, "RC 1", 1);
__version_date_info__ = (2018, 2, 5, "RC 1", 1);
__version_date__ = str(__version_date_info__[0])+"."+str(__version_date_info__[1]).zfill(2)+"."+str(__version_date_info__[2]).zfill(2);
if(__version_info__[4] is not None):
 __version_date_plusrc__ = __version_date__+"-"+str(__version_date_info__[4]);
if(__version_info__[4] is None):
 __version_date_plusrc__ = __version_date__;
if(__version_info__[3] is not None):
 __version__ = str(__version_info__[0])+"."+str(__version_info__[1])+"."+str(__version_info__[2])+" "+str(__version_info__[3]);
if(__version_info__[3] is None):
 __version__ = str(__version_info__[0])+"."+str(__version_info__[1])+"."+str(__version_info__[2]);

def MakeHockeyDatabase(sdbfile, synchronous="FULL", journal_mode="DELETE"):
 sqlcon = sqlite3.connect(sdbfile, isolation_level=None);
 sqlcur = sqlcon.cursor();
 sqldatacon = (sqlcur, sqlcon);
 sqlcur.execute("PRAGMA encoding = \"UTF-8\";");
 sqlcur.execute("PRAGMA auto_vacuum = 1;");
 sqlcur.execute("PRAGMA foreign_keys = 0;");
 sqlcur.execute("PRAGMA synchronous = "+str(synchronous)+";");
 sqlcur.execute("PRAGMA journal_mode = "+str(journal_mode)+";");
 return sqldatacon;

def OpenHockeyDatabase(sdbfile):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 sqlcon = sqlite3.connect(sdbfile, isolation_level=None);
 sqlcur = sqlcon.cursor();
 sqldatacon = (sqlcur, sqlcon);
 sqlcur.execute("PRAGMA encoding = \"UTF-8\";");
 sqlcur.execute("PRAGMA auto_vacuum = 1;");
 sqlcur.execute("PRAGMA foreign_keys = 0;");
 return sqldatacon;

def GetLastGames(sqldatacon, leaguename, teamname, gamelimit=10):
 wins = 0;
 losses = 0;
 otlosses = 0;
 getlastninegames = sqldatacon[0].execute("SELECT NumberPeriods, TeamWin, TeamLost FROM "+leaguename+"Games WHERE (HomeTeam=\""+str(teamname)+"\" OR AwayTeam=\""+str(teamname)+"\") ORDER BY id DESC LIMIT "+str(gamelimit)).fetchall();
 nmax = len(getlastninegames);
 nmin = 0;
 while(nmin<nmax):
  if(teamname==str(getlastninegames[nmin][1])):
   wins = wins + 1;
  if(teamname==str(getlastninegames[nmin][2])):
   if(int(getlastninegames[nmin][0])==3):
    losses = losses + 1;
   if(int(getlastninegames[nmin][0])>3):
    otlosses = otlosses + 1;
  nmin = nmin + 1;
 return str(wins)+":"+str(losses)+":"+str(otlosses);

def GetLastTenGames(sqldatacon, leaguename, teamname):
 return GetLastGames(sqldatacon, leaguename, teamname, 10);

def GetLastGamesWithShootout(sqldatacon, leaguename, teamname, gamelimit=10):
 wins = 0;
 losses = 0;
 otlosses = 0;
 solosses = 0;
 getlastninegames = sqldatacon[0].execute("SELECT NumberPeriods, TeamWin, TeamLost FROM "+leaguename+"Games WHERE (HomeTeam=\""+str(teamname)+"\" OR AwayTeam=\""+str(teamname)+"\") ORDER BY id DESC LIMIT "+str(gamelimit)).fetchall();
 nmax = len(getlastninegames);
 nmin = 0;
 while(nmin<nmax):
  if(teamname==str(getlastninegames[nmin][1])):
   wins = wins + 1;
  if(teamname==str(getlastninegames[nmin][2])):
   if(int(getlastninegames[nmin][0])==3):
    losses = losses + 1;
   if(int(getlastninegames[nmin][0])==4):
    otlosses = otlosses + 1;
   if(int(getlastninegames[nmin][0])>4):
    solosses = solosses + 1;
  nmin = nmin + 1;
 return str(wins)+":"+str(losses)+":"+str(otlosses)+":"+str(solosses);

def GetLastTenGamesWithShootout(sqldatacon, leaguename, teamname):
 return GetLastGamesWithShootout(sqldatacon, leaguename, teamname, 10);

def UpdateHockeyData(sqldatacon, leaguename, tablename, wherename, wheredata, wheretype, dataname, addtodata, addtype):
 wheretype = wheretype.lower();
 if(wheretype!="int" and wheretype!="str"):
  wheretype = "int";
 if(addtype!="=" and addtype!="+" and addtype!="-"):
  addtype = "=";
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+" and wheretype=="int"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+tablename+" WHERE "+wherename+"="+str(wheredata)).fetchone()[0]) + addtodata;
 if(addtype=="-" and wheretype=="int"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+tablename+" WHERE "+wherename+"="+str(wheredata)).fetchone()[0]) - addtodata;
 if(addtype=="+" and wheretype=="str"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+tablename+" WHERE "+wherename+"=\""+str(wheredata)+"\"").fetchone()[0]) + addtodata;
 if(addtype=="-" and wheretype=="str"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+tablename+" WHERE "+wherename+"=\""+str(wheredata)+"\"").fetchone()[0]) - addtodata;
 if(wheretype=="int"):
  sqldatacon[0].execute("UPDATE "+leaguename+tablename+" SET "+dataname+"="+str(TMPData)+" WHERE "+wherename+"="+str(wheredata));
 if(wheretype=="str"):
  sqldatacon[0].execute("UPDATE "+leaguename+tablename+" SET "+dataname+"="+str(TMPData)+" WHERE "+wherename+"=\""+str(wheredata)+"\"");
 return int(TMPData);

def UpdateHockeyDataString(sqldatacon, leaguename, tablename, wherename, wheredata, wheretype, dataname, newdata):
 if(wheretype=="int"):
  sqldatacon[0].execute("UPDATE "+leaguename+tablename+" SET "+dataname+"=\""+str(newdata)+"\" WHERE "+wherename+"="+str(wheredata));
 if(wheretype=="str"):
  sqldatacon[0].execute("UPDATE "+leaguename+tablename+" SET "+dataname+"=\""+str(newdata)+"\" WHERE "+wherename+"=\""+str(wheredata)+"\"");
 return True;

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

def MakeHockeyLeagueTable(sqldatacon):
 sqldatacon[0].execute("DROP TABLE IF EXISTS HockeyLeagues");
 sqldatacon[0].execute("CREATE TABLE HockeyLeagues (id INTEGER PRIMARY KEY, LeagueName TEXT, LeagueFullName TEXT, CountryName TEXT, FullCountryName TEXT, NumberOfTeams INTEGER, NumberOfConferences INTEGER, NumberOfDivisions INTEGER)");
 return True;

def MakeHockeyLeagues(sqldatacon, leaguename, leaguefullname, countryname, fullcountryname):
 sqldatacon[0].execute("INSERT INTO HockeyLeagues (LeagueName, LeagueFullName, CountryName, FullCountryName, NumberOfTeams, NumberOfConferences, NumberOfDivisions) VALUES(\""+str(leaguename)+"\", \""+str(leaguefullname)+"\", \""+str(countryname)+"\", \""+str(fullcountryname)+"\", 0, 0, 0)");
 return True;

def MakeHockeyConferenceTable(sqldatacon, leaguename):
 sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Conferences");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Conferences (id INTEGER PRIMARY KEY, Conference TEXT, LeagueName TEXT, LeagueFullName TEXT, NumberOfTeams INTEGER, NumberOfDivisions INTEGER)");
 return True;

def MakeHockeyConferences(sqldatacon, leaguename, conference, hasconferences=True):
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Conferences (Conference, LeagueName, LeagueFullName, NumberOfTeams, NumberOfDivisions) VALUES(\""+str(conference)+"\", \""+leaguename+"\", \""+GetLeagueName(sqldatacon, leaguename)+"\", 0, 0)");
 if(hasconferences is True):
  UpdateLeagueData(sqldatacon, leaguename, "NumberOfConferences", 1, "+");
 return True;

def MakeHockeyDivisionTable(sqldatacon, leaguename):
 sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Divisions");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Divisions (id INTEGER PRIMARY KEY, Division TEXT, Conference TEXT, LeagueName TEXT, LeagueFullName TEXT, NumberOfTeams INTEGER)");
 return True;

def MakeHockeyDivisions(sqldatacon, leaguename, division, conference, hasconferences=True, hasdivisions=True):
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Divisions (Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES(\""+str(division)+"\", \""+str(conference)+"\", \""+leaguename+"\", \""+GetLeagueName(sqldatacon, leaguename)+"\", 0)");
 if(hasconferences is True):
  UpdateConferenceData(sqldatacon, leaguename, conference, "NumberOfDivisions", 1, "+");
 if(hasdivisions is True):
  UpdateLeagueData(sqldatacon, leaguename, "NumberOfDivisions", 1, "+");
 return True;

def MakeHockeyTeamTable(sqldatacon, leaguename):
 sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Arenas");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Arenas (id INTEGER PRIMARY KEY, TeamID INTEGER, TeamName TEXT, TeamFullName TEXT, CityName TEXT, AreaName TEXT, CountryName TEXT, FullCountryName TEXT, FullCityName TEXT, FullAreaName TEXT, FullCityNameAlt TEXT, ArenaName TEXT, FullArenaName TEXT, GamesPlayed INTEGER, FOREIGN KEY(TeamID) REFERENCES "+leaguename+"Teams(id))");
 sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Teams");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Teams (id INTEGER PRIMARY KEY, Date INTEGER, FullName TEXT, CityName TEXT, TeamPrefix TEXT, TeamSuffix TEXT, AreaName TEXT, CountryName TEXT, FullCountryName TEXT, FullCityName TEXT, FullAreaName TEXT, FullCityNameAlt TEXT, TeamName TEXT, Conference TEXT, Division TEXT, LeagueName TEXT, LeagueFullName TEXT, ArenaName TEXT, FullArenaName TEXT, GamesPlayed INTEGER, GamesPlayedHome INTEGER, GamesPlayedAway INTEGER, Ties INTEGER, Wins INTEGER, OTWins INTEGER, SOWins INTEGER, OTSOWins INTEGER, TWins INTEGER, Losses INTEGER, OTLosses INTEGER, SOLosses INTEGER, OTSOLosses INTEGER, TLosses INTEGER, ROW INTEGER, ROT INTEGER, ShutoutWins INTEGER, ShutoutLosses INTEGER, HomeRecord TEXT, AwayRecord TEXT, Shootouts TEXT, GoalsFor INTEGER, GoalsAgainst INTEGER, GoalsDifference INTEGER, SOGFor INTEGER, SOGAgainst INTEGER, SOGDifference INTEGER, ShotsBlockedFor INTEGER, ShotsBlockedAgainst INTEGER, ShotsBlockedDifference INTEGER, PPGFor INTEGER, PPGAgainst INTEGER, PPGDifference INTEGER, SHGFor INTEGER, SHGAgainst INTEGER, SHGDifference INTEGER, PenaltiesFor INTEGER, PenaltiesAgainst INTEGER, PenaltiesDifference INTEGER, PIMFor INTEGER, PIMAgainst INTEGER, PIMDifference INTEGER, HITSFor INTEGER, HITSAgainst INTEGER, HITSDifference INTEGER, TakeAways INTEGER, GiveAways INTEGER, TAGADifference INTEGER, FaceoffWins INTEGER, FaceoffLosses INTEGER, FaceoffDifference INTEGER, Points INTEGER, PCT REAL, LastTen TEXT, Streak TEXT)");
 sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Stats");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Stats (id INTEGER PRIMARY KEY, TeamID INTEGER, Date INTEGER, FullName TEXT, CityName TEXT, TeamPrefix TEXT, TeamSuffix TEXT, AreaName TEXT, CountryName TEXT, FullCountryName TEXT, FullCityName TEXT, FullAreaName TEXT, FullCityNameAlt TEXT, TeamName TEXT, Conference TEXT, Division TEXT, LeagueName TEXT, LeagueFullName TEXT, ArenaName TEXT, FullArenaName TEXT, GamesPlayed INTEGER, GamesPlayedHome INTEGER, GamesPlayedAway INTEGER, Ties INTEGER, Wins INTEGER, OTWins INTEGER, SOWins INTEGER, OTSOWins INTEGER, TWins INTEGER, Losses INTEGER, OTLosses INTEGER, SOLosses INTEGER, OTSOLosses INTEGER, TLosses INTEGER, ROW INTEGER, ROT INTEGER, ShutoutWins INTEGER, ShutoutLosses INTEGER, HomeRecord TEXT, AwayRecord TEXT, Shootouts TEXT, GoalsFor INTEGER, GoalsAgainst INTEGER, GoalsDifference INTEGER, SOGFor INTEGER, SOGAgainst INTEGER, SOGDifference INTEGER, ShotsBlockedFor INTEGER, ShotsBlockedAgainst INTEGER, ShotsBlockedDifference INTEGER, PPGFor INTEGER, PPGAgainst INTEGER, PPGDifference INTEGER, SHGFor INTEGER, SHGAgainst INTEGER, SHGDifference INTEGER, PenaltiesFor INTEGER, PenaltiesAgainst INTEGER, PenaltiesDifference INTEGER, PIMFor INTEGER, PIMAgainst INTEGER, PIMDifference INTEGER, HITSFor INTEGER, HITSAgainst INTEGER, HITSDifference INTEGER, TakeAways INTEGER, GiveAways INTEGER, TAGADifference INTEGER, FaceoffWins INTEGER, FaceoffLosses INTEGER, FaceoffDifference INTEGER, Points INTEGER, PCT REAL, LastTen TEXT, Streak TEXT, FOREIGN KEY(TeamID) REFERENCES "+leaguename+"Teams(id))");
 sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"GameStats");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"GameStats (id INTEGER PRIMARY KEY, GameID INTEGER, Date INTEGER, TeamID INTEGER, FullName TEXT, CityName TEXT, TeamPrefix TEXT, TeamSuffix TEXT, AreaName TEXT, CountryName TEXT, FullCountryName TEXT, FullCityName TEXT, FullAreaName TEXT, FullCityNameAlt TEXT, TeamName TEXT, Conference TEXT, Division TEXT, LeagueName TEXT, LeagueFullName TEXT, ArenaName TEXT, FullArenaName TEXT, GoalsFor INTEGER, GoalsAgainst INTEGER, GoalsDifference INTEGER, SOGFor INTEGER, SOGAgainst INTEGER, SOGDifference INTEGER, ShotsBlockedFor INTEGER, ShotsBlockedAgainst INTEGER, ShotsBlockedDifference INTEGER, PPGFor INTEGER, PPGAgainst INTEGER, PPGDifference INTEGER, SHGFor INTEGER, SHGAgainst INTEGER, SHGDifference INTEGER, PenaltiesFor INTEGER, PenaltiesAgainst INTEGER, PenaltiesDifference INTEGER, PIMFor INTEGER, PIMAgainst INTEGER, PIMDifference INTEGER, HITSFor INTEGER, HITSAgainst INTEGER, HITSDifference INTEGER, TakeAways INTEGER, GiveAways INTEGER, TAGADifference INTEGER, FaceoffWins INTEGER, FaceoffLosses INTEGER, FaceoffDifference INTEGER, FOREIGN KEY(GameID) REFERENCES "+leaguename+"Games(id), FOREIGN KEY(TeamID) REFERENCES "+leaguename+"Teams(id))");
 return True;

def MakeHockeyTeams(sqldatacon, leaguename, date, cityname, areaname, countryname, fullcountryname, fullareaname, teamname, conference, division, arenaname, teamnameprefix="", teamnamesuffix="", hasconferences=True, hasdivisions=True):
 if(teamnameprefix.strip()=="" and teamnamesuffix.strip()==""):
  fullteamname = str(teamname);
  teamnameprefix = teamnameprefix.strip();
  teamnamesuffix = teamnamesuffix.strip();
 if(teamnameprefix.strip()!="" and teamnamesuffix.strip()==""):
  fullteamname = str(teamnameprefix+" "+teamname);
  teamnamesuffix = teamnamesuffix.strip();
 if(teamnameprefix.strip()=="" and teamnamesuffix.strip()!=""):
  fullteamname = str(teamname+" "+teamnamesuffix);
  teamnameprefix = teamnameprefix.strip();
 if(teamnameprefix.strip()!="" and teamnamesuffix.strip()!=""):
  fullteamname = str(teamnameprefix+" "+teamname+" "+teamnamesuffix);
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Teams (Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES(\""+str(date)+"\", \""+fullteamname+"\", \""+str(cityname)+"\", \""+str(teamnameprefix)+"\", \""+str(teamnamesuffix)+"\", \""+str(areaname)+"\", \""+str(countryname)+"\", \""+str(fullcountryname)+"\", \""+str(cityname+", "+areaname)+"\", \""+str(fullareaname)+"\", \""+str(cityname+", "+fullareaname)+"\", \""+str(teamname)+"\", \""+str(conference)+"\", \""+str(division)+"\", \""+leaguename+"\", \""+GetLeagueName(sqldatacon, leaguename)+"\", \""+str(arenaname)+"\", \""+str(arenaname+", "+cityname)+"\", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \"0:0:0:0\", \"0:0:0:0\", \"0:0\", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \"0:0:0:0\", \"None\")");
 TeamID = int(sqldatacon[0].lastrowid);
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Stats (TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) SELECT id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE FullName=\""+fullteamname+"\";");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Arenas (TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES("+str(TeamID)+", \""+str(teamname)+"\", \""+fullteamname+"\", \""+str(cityname)+"\", \""+str(areaname)+"\", \""+str(countryname)+"\", \""+str(fullcountryname)+"\", \""+str(cityname+", "+areaname)+"\", \""+str(fullareaname)+"\", \""+str(cityname+", "+fullareaname)+"\", \""+str(arenaname)+"\", \""+str(arenaname+", "+cityname)+"\", 0)");
 if(hasconferences is True):
  UpdateConferenceData(sqldatacon, leaguename, conference, "NumberOfTeams", 1, "+");
 if(hasdivisions is True):
  UpdateDivisionData(sqldatacon, leaguename, division, "NumberOfTeams", 1, "+");
 UpdateLeagueData(sqldatacon, leaguename, "NumberOfTeams", 1, "+");
 return True;

def MakeHockeyPlayoffTeamTable(sqldatacon, leaguename):
 sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"PlayoffTeams");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"PlayoffTeams (id INTEGER PRIMARY KEY, TeamID INTEGER, Date INTEGER, FullName TEXT, CityName TEXT, TeamPrefix TEXT, TeamSuffix TEXT, AreaName TEXT, CountryName TEXT, FullCountryName TEXT, FullCityName TEXT, FullAreaName TEXT, FullCityNameAlt TEXT, TeamName TEXT, Conference TEXT, Division TEXT, LeagueName TEXT, LeagueFullName TEXT, ArenaName TEXT, FullArenaName TEXT, GamesPlayed INTEGER, GamesPlayedHome INTEGER, GamesPlayedAway INTEGER, Ties, Wins INTEGER, OTWins INTEGER, SOWins INTEGER, OTSOWins INTEGER, TWins INTEGER, Losses INTEGER, OTLosses INTEGER, SOLosses INTEGER, OTSOLosses INTEGER, TLosses INTEGER, ROW INTEGER, ROT INTEGER, ShutoutWins INTEGER, ShutoutLosses INTEGER, HomeRecord TEXT, AwayRecord TEXT, Shootouts TEXT, GoalsFor INTEGER, GoalsAgainst INTEGER, GoalsDifference INTEGER, SOGFor INTEGER, SOGAgainst INTEGER, SOGDifference INTEGER, ShotsBlockedFor INTEGER, ShotsBlockedAgainst INTEGER, ShotsBlockedDifference INTEGER, PPGFor INTEGER, PPGAgainst INTEGER, PPGDifference INTEGER, SHGFor INTEGER, SHGAgainst INTEGER, SHGDifference INTEGER, PenaltiesFor INTEGER, PenaltiesAgainst INTEGER, PenaltiesDifference INTEGER, PIMFor INTEGER, PIMAgainst INTEGER, PIMDifference INTEGER, HITSFor INTEGER, HITSAgainst INTEGER, HITSDifference INTEGER, TakeAways INTEGER, GiveAways INTEGER, TAGADifference INTEGER, FaceoffWins INTEGER, FaceoffLosses INTEGER, FaceoffDifference INTEGER, Points INTEGER, PCT REAL, LastTen TEXT, Streak TEXT, FOREIGN KEY(TeamID) REFERENCES "+leaguename+"Teams(id))");
 return True;

def MakeHockeyPlayoffTeams(sqldatacon, leaguename, playofffmt="Division=3,Conference=2"):
 playoffspl = playofffmt.split(',');
 playoffcnt = 0;
 while(playoffcnt<len(playoffspl)):
  subplayoffspl = playoffspl[playoffcnt].split('=');
  subsubplayoffspl = subplayoffspl[0].split(":")
  if(subsubplayoffspl[0]=="League"):
   sqldatacon[0].execute("INSERT INTO "+leaguename+"PlayoffTeams (TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) SELECT id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE NOT EXISTS(SELECT TeamID FROM "+leaguename+"PlayoffTeams WHERE "+leaguename+"PlayoffTeams.TeamID = "+leaguename+"Teams.id) ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC LIMIT "+subplayoffspl[1]+";");
  if(subsubplayoffspl[0]=="Conference"):
   conferencecur = sqldatacon[1].cursor();
   if(len(subsubplayoffspl)==1):
    getconference = conferencecur.execute("SELECT Conference FROM "+leaguename+"Conferences WHERE LeagueName=\""+leaguename+"\"");
   if(len(subsubplayoffspl)>1):
    getconference = conferencecur.execute("SELECT Conference FROM "+leaguename+"Conferences WHERE LeagueName=\""+leaguename+"\" AND Conference=\""+subsubplayoffspl[1]+"\"");
   for conferenceinfo in getconference:
    sqldatacon[0].execute("INSERT INTO "+leaguename+"PlayoffTeams (TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) SELECT id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE Conference=\""+conferenceinfo[0]+"\" AND NOT EXISTS(SELECT TeamID FROM "+leaguename+"PlayoffTeams WHERE "+leaguename+"PlayoffTeams.TeamID = "+leaguename+"Teams.id) ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC LIMIT "+subplayoffspl[1]+";");
   conferencecur.close();
  if(subsubplayoffspl[0]=="Division"):
   divisioncur = sqldatacon[1].cursor();
   if(len(subsubplayoffspl)==1):
    getdivision = divisioncur.execute("SELECT Division FROM "+leaguename+"Divisions WHERE LeagueName=\""+leaguename+"\"");
   if(len(subsubplayoffspl)>1):
    getdivision = divisioncur.execute("SELECT Division FROM "+leaguename+"Divisions WHERE LeagueName=\""+leaguename+"\" AND Division=\""+subsubplayoffspl[1]+"\"");
   for divisioninfo in getdivision:
    sqldatacon[0].execute("INSERT INTO "+leaguename+"PlayoffTeams (TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) SELECT id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE Division=\""+divisioninfo[0]+"\" AND NOT EXISTS(SELECT TeamID FROM "+leaguename+"PlayoffTeams WHERE "+leaguename+"PlayoffTeams.TeamID = "+leaguename+"Teams.id) ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC LIMIT "+subplayoffspl[1]+";");
   divisioncur.close();
  playoffcnt = playoffcnt + 1;
 return True;

def MakeHockeyArena(sqldatacon, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, arenaname):
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Arenas (TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES(0, \"None\", \"None\", \""+str(cityname)+"\", \""+str(areaname)+"\", \""+str(countryname)+"\", \""+str(fullcountryname)+"\", \""+str(cityname+", "+areaname)+"\", \""+str(fullareaname)+"\", \""+str(cityname+", "+fullareaname)+"\", \""+str(arenaname)+"\", \""+str(arenaname+", "+cityname)+"\", 0)");
 return True;

def MakeHockeyGameTable(sqldatacon, leaguename):
 sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Games");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Games (id INTEGER PRIMARY KEY, Date INTEGER, HomeTeam TEXT, AwayTeam TEXT, AtArena TEXT, TeamScorePeriods TEXT, TeamFullScore TEXT, ShotsOnGoal TEXT, FullShotsOnGoal TEXT, ShotsBlocked TEXT, FullShotsBlocked TEXT, PowerPlays TEXT, FullPowerPlays TEXT, ShortHanded TEXT, FullShortHanded TEXT, Penalties TEXT, FullPenalties TEXT, PenaltyMinutes TEXT, FullPenaltyMinutes TEXT, HitsPerPeriod TEXT, FullHitsPerPeriod TEXT, TakeAways TEXT, FullTakeAways TEXT, GiveAways TEXT, FullGiveAways TEXT, FaceoffWins TEXT, FullFaceoffWins TEXT, NumberPeriods INTEGER, TeamWin TEXT, TeamLost TEXT, TieGame INTEGER, IsPlayOffGame INTEGER)");
 return True;

def MakeHockeyGame(sqldatacon, leaguename, date, hometeam, awayteam, periodsscore, shotsongoal, ppgoals, shgoals, periodpens, periodpims, periodhits, takeaways, faceoffwins, atarena, isplayoffgame):
 if(isplayoffgame.isdigit()):
  isplayoffgame = int(isplayoffgame);
 if(isplayoffgame==0 or isplayoffgame=="0"):
  isplayoffgame = False;
 if(isplayoffgame==1 or isplayoffgame=="1"):
  isplayoffgame = True;
 if(isplayoffgame==2 or isplayoffgame=="2"):
  isplayoffgame = None;
 isplayoffgsql = "0";
 if(isplayoffgame is True):
  isplayoffgsql = "1";
 if(isplayoffgame is False):
  isplayoffsql = "0";
 if(isplayoffgame is None):
  isplayoffsql = "2";
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
  if(isplayoffgame is True and periodcounting > 3):
   homescore = homescore + int(periodscoresplit[0]);
   awayscore = awayscore + int(periodscoresplit[1]);
  if(isplayoffgame is False and periodcounting > 3):
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
 shgoalssplits = shgoals.split(",");
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
 homeshg = 0;
 awayshg = 0;
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
  periodshgsplit = shgoalssplits[periodsogcounting].split(":");
  periodpimsplit = periodpimssplits[periodsogcounting].split(":");
  periodpensplit = periodpenssplits[periodsogcounting].split(":");
  periodhitsplit = periodhitssplits[periodsogcounting].split(":");
  periodtawsplit = takeawayssplits[periodsogcounting].split(":");
  periodfowsplit = faceoffwinssplits[periodsogcounting].split(":");
  homesog = homesog + int(periodsogsplit[0]);
  homesb = int(periodsogsplit[0]) - int(periodscoresplit[0]);
  hometsb = homesb + hometsb;
  homeppg = homeppg + int(periodppgsplit[0]);
  homeshg = homeshg + int(periodshgsplit[0]);
  homepims = homepims + int(periodpimsplit[0]);
  homepens = homepens + int(periodpensplit[0]);
  homehits = homehits + int(periodhitsplit[0]);
  hometaws = hometaws + int(periodtawsplit[0]);
  homefows = homefows + int(periodfowsplit[0]);
  awaysog = awaysog + int(periodsogsplit[1]);
  awaysb = int(periodsogsplit[1]) - int(periodscoresplit[1]);
  awaytsb = awaysb + awaytsb;
  awayppg = awayppg + int(periodppgsplit[1]);
  awayshg = awayshg + int(periodshgsplit[1]);
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
 totalshg = str(homeshg)+":"+str(awayshg);
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
 if(teamscores[0] > teamscores[1]):
  losingteam = awayteam;
  winningteam = hometeam;
  winningteamname = hometeamname;
  losingteamname = awayteamname;
 if(teamscores[0] < teamscores[1]):
  losingteam = hometeam;
  winningteam = awayteam;
  winningteamname = awayteamname;
  losingteamname = hometeamname;
 tiegame = 0;
 if(teamscores[0] == teamscores[1]):
  losingteam = 0;
  winningteam = 0;
  tiegame = 1;
  winningteamname = "";
  losingteamname = "";
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Games (Date, HomeTeam, AwayTeam, AtArena, TeamScorePeriods, TeamFullScore, ShotsOnGoal, FullShotsOnGoal, ShotsBlocked, FullShotsBlocked, PowerPlays, FullPowerPlays, ShortHanded, FullShortHanded, Penalties, FullPenalties, PenaltyMinutes, FullPenaltyMinutes, HitsPerPeriod, FullHitsPerPeriod, TakeAways, FullTakeAways, GiveAways, FullGiveAways, FaceoffWins, FullFaceoffWins, NumberPeriods, TeamWin, TeamLost, TieGame, IsPlayOffGame) VALUES("+str(date)+", \""+str(hometeamname)+"\", \""+str(awayteamname)+"\", \""+str(atarenaname)+"\", \""+str(periodsscore)+"\", \""+str(totalscore)+"\", \""+str(shotsongoal)+"\", \""+str(totalsog)+"\", \""+str(sbstr)+"\", \""+str(tsbstr)+"\", \""+str(ppgoals)+"\", \""+str(totalppg)+"\", \""+str(shgoals)+"\", \""+str(totalshg)+"\", \""+str(periodpens)+"\", \""+str(totalpens)+"\", \""+str(periodpims)+"\", \""+str(totalpims)+"\", \""+str(periodhits)+"\", \""+str(totalhits)+"\", \""+str(takeaways)+"\", \""+str(totaltaws)+"\", \""+str(gaws_str)+"\", \""+str(totalgaws)+"\", \""+str(faceoffwins)+"\", \""+str(totalfows)+"\", "+str(numberofperiods)+", \""+str(winningteamname)+"\", \""+str(losingteamname)+"\", \""+str(tiegame)+"\", "+str(isplayoffgsql)+")");
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
 UpdateTeamData(sqldatacon, leaguename, hometeam, "SHGFor", int(homeshg), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "SHGAgainst", int(awayshg), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "SHGDifference", int(int(homeshg) - int(awayshg)), "+");
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
 UpdateTeamData(sqldatacon, leaguename, awayteam, "PPGFor", int(awayppg), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "PPGAgainst", int(homeppg), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "PPGDifference", int(int(awayppg) - int(homeppg)), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "SHGFor", int(awayshg), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "SHGAgainst", int(homeshg), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "SHGDifference", int(int(awayshg) - int(homeshg)), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "PenaltiesFor", int(homepens), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "PenaltiesAgainst", int(awaypens), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "PenaltiesDifference", int(int(homepens) - int(awaypens)), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "PIMFor", int(awaypims), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "PIMAgainst", int(homepims), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "PIMDifference", int(int(awaypims) - int(homepims)), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "HITSFor", int(awayhits), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "HITSAgainst", int(homehits), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "HITSDifference", int(int(awayhits) - int(homehits)), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "TakeAways", int(awaytaws), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "GiveAways", int(hometaws), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "TAGADifference", int(int(awaytaws) - int(hometaws)), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "FaceoffWins", int(awayfows), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "FaceoffLosses", int(homefows), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "FaceoffDifference", int(int(awayfows) - int(homefows)), "+");
 if(tiegame==1):
  UpdateTeamData(sqldatacon, leaguename, hometeam, "Ties", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, awayteam, "Ties", 1, "+");
 if(winningteam==hometeam and int(teamscores[1])==0):
  UpdateTeamData(sqldatacon, leaguename, hometeam, "ShutoutWins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, awayteam, "ShutoutLosses", 1, "+");
 if(winningteam==awayteam and int(teamscores[0])==0):
  UpdateTeamData(sqldatacon, leaguename, awayteam, "ShutoutWins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, hometeam, "ShutoutLosses", 1, "+");
 UpdateTeamDataString(sqldatacon, leaguename, hometeam, "LastTen", GetLastGamesWithShootout(sqldatacon, leaguename, winningteamname));
 UpdateTeamDataString(sqldatacon, leaguename, awayteam, "LastTen", GetLastGamesWithShootout(sqldatacon, leaguename, losingteamname));
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
 if((isplayoffgame is False and numberofperiods<5 and (winningteam==hometeam or winningteam==awayteam)) or (isplayoffgame is True and (winningteam==hometeam or winningteam==awayteam))):
  UpdateTeamData(sqldatacon, leaguename, winningteam, "ROW", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "ROT", 1, "+");
 if(numberofperiods==3 and (winningteam==hometeam or winningteam==awayteam)):
  UpdateTeamData(sqldatacon, leaguename, winningteam, "Wins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, winningteam, "TWins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, winningteam, "Points", 2, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "Losses", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "TLosses", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "Points", 0, "+");
  if(winningteam==hometeam):
   HomeTeamRecord = GetTeamData(sqldatacon, leaguename, winningteam, "HomeRecord", "str");
   HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
   NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2])+":"+str(HTRSpit[3]);
   UpdateTeamDataString(sqldatacon, leaguename, winningteam, "HomeRecord", NewHTR);
   AwayTeamRecord = GetTeamData(sqldatacon, leaguename, losingteam, "AwayRecord", "str");
   ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
   NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1] + 1)+":"+str(ATRSpit[2])+":"+str(ATRSpit[3]);
   UpdateTeamDataString(sqldatacon, leaguename, losingteam, "AwayRecord", NewATR);
  if(losingteam==hometeam):
   HomeTeamRecord = GetTeamData(sqldatacon, leaguename, winningteam, "AwayRecord", "str");
   HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
   NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2])+":"+str(HTRSpit[3]);
   UpdateTeamDataString(sqldatacon, leaguename, winningteam, "AwayRecord", NewHTR);
   AwayTeamRecord = GetTeamData(sqldatacon, leaguename, losingteam, "HomeRecord", "str");
   ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
   NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1] + 1)+":"+str(ATRSpit[2])+":"+str(ATRSpit[3]);
   UpdateTeamDataString(sqldatacon, leaguename, losingteam, "HomeRecord", NewATR);
 if(numberofperiods>3 and (winningteam==hometeam or winningteam==awayteam)):
  if((numberofperiods==4 and isplayoffgame is False) or (numberofperiods>4 and isplayoffgame is True)):
   UpdateTeamData(sqldatacon, leaguename, winningteam, "OTWins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, winningteam, "OTSOWins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, winningteam, "TWins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, winningteam, "Points", 2, "+");
  if((numberofperiods==4 and isplayoffgame is False) or (numberofperiods>4 and isplayoffgame is True)):
   UpdateTeamData(sqldatacon, leaguename, losingteam, "OTLosses", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "OTSOLosses", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "TLosses", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "Points", 1, "+");
  if(isplayoffgame is True):
   if(winningteam==hometeam):
    HomeTeamRecord = GetTeamData(sqldatacon, leaguename, winningteam, "HomeRecord", "str");
    HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
    NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2])+":"+str(HTRSpit[3]);
    UpdateTeamDataString(sqldatacon, leaguename, winningteam, "HomeRecord", NewHTR);
    AwayTeamRecord = GetTeamData(sqldatacon, leaguename, losingteam, "AwayRecord", "str");
    ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
    NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1])+":"+str(ATRSpit[2] + 1)+":"+str(ATRSpit[3]);
    UpdateTeamDataString(sqldatacon, leaguename, losingteam, "AwayRecord", NewATR);
   if(losingteam==hometeam):
    HomeTeamRecord = GetTeamData(sqldatacon, leaguename, winningteam, "AwayRecord", "str");
    HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
    NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2])+":"+str(HTRSpit[3]);
    UpdateTeamDataString(sqldatacon, leaguename, winningteam, "AwayRecord", NewHTR);
    AwayTeamRecord = GetTeamData(sqldatacon, leaguename, losingteam, "HomeRecord", "str");
    ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
    NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1])+":"+str(ATRSpit[2] + 1)+":"+str(ATRSpit[3]);
    UpdateTeamDataString(sqldatacon, leaguename, losingteam, "HomeRecord", NewATR);
  if(isplayoffgame is False and numberofperiods==4):
   if(winningteam==hometeam):
    HomeTeamRecord = GetTeamData(sqldatacon, leaguename, winningteam, "HomeRecord", "str");
    HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
    NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2])+":"+str(HTRSpit[3]);
    UpdateTeamDataString(sqldatacon, leaguename, winningteam, "HomeRecord", NewHTR);
    AwayTeamRecord = GetTeamData(sqldatacon, leaguename, losingteam, "AwayRecord", "str");
    ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
    NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1])+":"+str(ATRSpit[2] + 1)+":"+str(ATRSpit[3]);
    UpdateTeamDataString(sqldatacon, leaguename, losingteam, "AwayRecord", NewATR);
   if(losingteam==hometeam):
    HomeTeamRecord = GetTeamData(sqldatacon, leaguename, winningteam, "AwayRecord", "str");
    HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
    NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2])+":"+str(HTRSpit[3]);
    UpdateTeamDataString(sqldatacon, leaguename, winningteam, "AwayRecord", NewHTR);
    AwayTeamRecord = GetTeamData(sqldatacon, leaguename, losingteam, "HomeRecord", "str");
    ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
    NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1])+":"+str(ATRSpit[2] + 1)+":"+str(ATRSpit[3]);
    UpdateTeamDataString(sqldatacon, leaguename, losingteam, "HomeRecord", NewATR);
  if(isplayoffgame is False and numberofperiods>4):
   if(winningteam==hometeam):
    HomeTeamRecord = GetTeamData(sqldatacon, leaguename, winningteam, "HomeRecord", "str");
    HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
    NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2])+":"+str(HTRSpit[3]);
    UpdateTeamDataString(sqldatacon, leaguename, winningteam, "HomeRecord", NewHTR);
    AwayTeamRecord = GetTeamData(sqldatacon, leaguename, losingteam, "AwayRecord", "str");
    ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
    NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1])+":"+str(ATRSpit[2])+":"+str(ATRSpit[3] + 1);
    UpdateTeamDataString(sqldatacon, leaguename, losingteam, "AwayRecord", NewATR);
   if(losingteam==hometeam):
    HomeTeamRecord = GetTeamData(sqldatacon, leaguename, winningteam, "AwayRecord", "str");
    HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
    NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2])+":"+str(HTRSpit[3]);
    UpdateTeamDataString(sqldatacon, leaguename, winningteam, "AwayRecord", NewHTR);
    AwayTeamRecord = GetTeamData(sqldatacon, leaguename, losingteam, "HomeRecord", "str");
    ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
    NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1])+":"+str(ATRSpit[2])+":"+str(ATRSpit[3] + 1);
    UpdateTeamDataString(sqldatacon, leaguename, losingteam, "HomeRecord", NewATR);
 if(isplayoffgame is False and numberofperiods>4 and (winningteam==hometeam or winningteam==awayteam)):
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
 HomeWinsPCTAlt = float("%.3f" % float(float(GetTeamData(sqldatacon, leaguename, hometeam, "TWins", "float") + HomeOTLossesPCT) / float(GetTeamData(sqldatacon, leaguename, hometeam, "GamesPlayed", "float"))));
 HomeWinsPCT = float("%.3f" % float(GetTeamData(sqldatacon, leaguename, hometeam, "Points", "float") / float(GetTeamData(sqldatacon, leaguename, hometeam, "GamesPlayed", "float") * 2)));
 AwayOTLossesPCT = float("%.2f" % float(float(0.5) * float(GetTeamData(sqldatacon, leaguename, awayteam, "OTSOLosses", "float"))));
 AwayWinsPCTAlt = float("%.3f" % float(float(GetTeamData(sqldatacon, leaguename, awayteam, "TWins", "float") + AwayOTLossesPCT) / float(GetTeamData(sqldatacon, leaguename, awayteam, "GamesPlayed", "float"))));
 AwayWinsPCT = float("%.3f" % float(GetTeamData(sqldatacon, leaguename, awayteam, "Points", "float") / float(GetTeamData(sqldatacon, leaguename, awayteam, "GamesPlayed", "float") * 2)));
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PCT", HomeWinsPCT, "=");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "PCT", AwayWinsPCT, "=");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"GameStats (GameID, Date, TeamID, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference) VALUES("+str(GameID)+", "+str(date)+", "+str(hometeam)+", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "CityName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "TeamPrefix")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "TeamSuffix")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "AreaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "CountryName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullCountryName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullCityName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullAreaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullCityNameAlt")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "TeamName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "Conference")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "Division")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "LeagueName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "LeagueFullName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "ArenaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullArenaName")+"\", "+str(teamscores[0])+", "+str(teamscores[1])+", "+str(int(teamscores[0]) - int(teamscores[1]))+", "+str(teamssog[0])+", "+str(teamssog[1])+", "+str(int(teamssog[0]) - int(teamssog[1]))+", "+str(hometsb)+", "+str(awaytsb)+", "+str(int(hometsb) - int(awaytsb))+", "+str(homeppg)+", "+str(awayppg)+", "+str(int(homeppg) - int(awayppg))+", "+str(homeshg)+", "+str(awayshg)+", "+str(int(homeshg) - int(awayshg))+", "+str(homepens)+", "+str(awaypens)+", "+str(int(homepens) - int(awaypens))+", "+str(homepims)+", "+str(awaypims)+", "+str(int(homepims) - int(awaypims))+", "+str(homehits)+", "+str(awayhits)+", "+str(int(homehits) - int(awayhits))+", "+str(hometaws)+", "+str(awaytaws)+", "+str(int(hometaws) - int(awaytaws))+", "+str(homefows)+", "+str(awayfows)+", "+str(int(homefows) - int(awayfows))+")");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"GameStats (GameID, Date, TeamID, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference) VALUES("+str(GameID)+", "+str(date)+", "+str(awayteam)+", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "CityName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "TeamPrefix")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "TeamSuffix")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "AreaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "CountryName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullCountryName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullCityName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullAreaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullCityNameAlt")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "TeamName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "Conference")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "Division")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "LeagueName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "LeagueFullName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "ArenaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullArenaName")+"\", "+str(teamscores[1])+", "+str(teamscores[0])+", "+str(int(teamscores[1]) - int(teamscores[0]))+", "+str(teamssog[1])+", "+str(teamssog[0])+", "+str(int(teamssog[1]) - int(teamssog[0]))+", "+str(awaytsb)+", "+str(hometsb)+", "+str(int(awaytsb) - int(hometsb))+", "+str(awayppg)+", "+str(homeppg)+", "+str(int(awayppg) - int(homeppg))+", "+str(awayshg)+", "+str(homeshg)+", "+str(int(awayshg) - int(homeshg))+", "+str(awaypens)+", "+str(homepens)+", "+str(int(awaypens) - int(homepens))+", "+str(awaypims)+", "+str(homepims)+", "+str(int(awaypims) - int(homepims))+", "+str(awayhits)+", "+str(homehits)+", "+str(int(awayhits) - int(homehits))+", "+str(awaytaws)+", "+str(hometaws)+", "+str(int(awaytaws) - int(hometaws))+", "+str(awayfows)+", "+str(homefows)+", "+str(int(awayfows) - int(homefows))+")");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Stats (TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) SELECT id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE FullName=\""+hometeamname+"\";");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Stats (TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) SELECT id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE FullName=\""+awayteamname+"\";");
 return True;

def CloseHockeyDatabase(sqldatacon):
 db_integrity_check = sqldatacon[0].execute("PRAGMA integrity_check(100);").fetchone()[0];
 sqldatacon[0].execute("PRAGMA optimize;");
 sqldatacon[0].close();
 sqldatacon[1].close();
 return True;

def MakeHockeyDatabaseFromXML(xmlfile, sdbfile=None, returnxml=False):
 if(os.path.exists(xmlfile) and os.path.isfile(xmlfile)):
  hockeyfile = ET.parse(xmlfile);
 else:
  return False;
 gethockey = hockeyfile.getroot();
 print("<?xml version=\"1.0\" encoding=\"UTF-8\"?>");
 xmlstring = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
 if(gethockey.tag == "hockey"):
  if(sdbfile is None):
   sqldatacon = MakeHockeyDatabase(gethockey.attrib['database']);
  if(sdbfile is not None):
   sqldatacon = MakeHockeyDatabase(sdbfile);
  print("<hockey database=\""+xml_escape(gethockey.attrib['database'], quote=True)+"\" year=\""+xml_escape(gethockey.attrib['year'], quote=True)+"\" month=\""+xml_escape(gethockey.attrib['month'], quote=True)+"\" day=\""+xml_escape(gethockey.attrib['day'], quote=True)+"\">");
  xmlstring = xmlstring+"<hockey database=\""+xml_escape(gethockey.attrib['database'], quote=True)+"\" year=\""+xml_escape(gethockey.attrib['year'], quote=True)+"\" month=\""+xml_escape(gethockey.attrib['month'], quote=True)+"\" day=\""+xml_escape(gethockey.attrib['day'], quote=True)+"\">\n";
 leaguecount = 0;
 for getleague in gethockey:
  if(leaguecount==0 and getleague.tag=="league"):
   MakeHockeyLeagueTable(sqldatacon);
  if(getleague.tag=="league"):
   MakeHockeyTeamTable(sqldatacon, getleague.attrib['name']);
   MakeHockeyConferenceTable(sqldatacon, getleague.attrib['name']);
   MakeHockeyGameTable(sqldatacon, getleague.attrib['name']);
   MakeHockeyDivisionTable(sqldatacon, getleague.attrib['name']);
   HockeyLeagueHasDivisions = True;
   if(getleague.attrib['conferences'].lower()=="no"):
    HockeyLeagueHasDivisions = False;
   HockeyLeagueHasConferences = True;
   if(getleague.attrib['divisions'].lower()=="no"):
    HockeyLeagueHasConferences = False;
   MakeHockeyLeagues(sqldatacon, getleague.attrib['name'], getleague.attrib['fullname'], getleague.attrib['country'], getleague.attrib['fullcountry']);
   print(" <league name=\""+xml_escape(getleague.attrib['name'], quote=True)+"\" fullname=\""+xml_escape(getleague.attrib['fullname'], quote=True)+"\" country=\""+xml_escape(getleague.attrib['country'], quote=True)+"\" fullcountry=\""+xml_escape(getleague.attrib['fullcountry'], quote=True)+"\" conferences=\""+xml_escape(getleague.attrib['conferences'], quote=True)+"\" divisions=\""+xml_escape(getleague.attrib['divisions'], quote=True)+"\">");
   xmlstring = " <league name=\""+xml_escape(getleague.attrib['name'], quote=True)+"\" fullname=\""+xml_escape(getleague.attrib['fullname'], quote=True)+"\" country=\""+xml_escape(getleague.attrib['country'], quote=True)+"\" fullcountry=\""+xml_escape(getleague.attrib['fullcountry'], quote=True)+"\" conferences=\""+xml_escape(getleague.attrib['conferences'], quote=True)+"\" divisions=\""+xml_escape(getleague.attrib['divisions'], quote=True)+"\">\n";
  leaguecount = leaguecount + 1;
  if(getleague.tag == "league"):
   conferencecount = 0;
   for getconference in getleague:
    if(getconference.tag == "conference"):
     MakeHockeyConferences(sqldatacon, getleague.attrib['name'], getconference.attrib['name'], HockeyLeagueHasConferences);
     print("  <conference name=\""+xml_escape(getconference.attrib['name'], quote=True)+"\">");
     xmlstring = "  <conference name=\""+xml_escape(getconference.attrib['name'], quote=True)+"\">\n";
     conferencecount = conferencecount + 1;
    if(getconference.tag == "arenas"):
     arenascount = 0;
     print("  <arenas>");
     xmlstring = "  <arenas>\n";
     for getarenas in getconference:
      MakeHockeyArena(sqldatacon, getleague.attrib['name'], getarenas.attrib['city'], getarenas.attrib['area'], getarenas.attrib['country'], getarenas.attrib['fullcountry'], getarenas.attrib['fullarea'], getarenas.attrib['name']);
      print("   <arena city=\""+xml_escape(getarenas.attrib['city'], quote=True)+"\" area=\""+xml_escape(getarenas.attrib['area'], quote=True)+"\" fullarea=\""+xml_escape(getarenas.attrib['fullarea'], quote=True)+"\" country=\""+xml_escape(getarenas.attrib['country'], quote=True)+"\" fullcountry=\""+xml_escape(getarenas.attrib['fullcountry'], quote=True)+"\" name=\""+xml_escape(getarenas.attrib['name'], quote=True)+"\" />");
      xmlstring = "   <arena city=\""+xml_escape(getarenas.attrib['city'], quote=True)+"\" area=\""+xml_escape(getarenas.attrib['area'], quote=True)+"\" fullarea=\""+xml_escape(getarenas.attrib['fullarea'], quote=True)+"\" country=\""+xml_escape(getarenas.attrib['country'], quote=True)+"\" fullcountry=\""+xml_escape(getarenas.attrib['fullcountry'], quote=True)+"\" name=\""+xml_escape(getarenas.attrib['name'], quote=True)+"\" />\n";
      arenascount = arenascount + 1;
     print("  </arenas>");
     xmlstring = "  </arenas>\n";
    if(getconference.tag == "games"):
     gamecount = 0;
     print("  <games>");
     xmlstring = "  <games>\n";
     for getgame in getconference:
      MakeHockeyGame(sqldatacon, getleague.attrib['name'], getgame.attrib['date'], getgame.attrib['hometeam'], getgame.attrib['awayteam'], getgame.attrib['goals'], getgame.attrib['sogs'], getgame.attrib['ppgs'], getgame.attrib['shgs'], getgame.attrib['penalties'], getgame.attrib['pims'], getgame.attrib['hits'], getgame.attrib['takeaways'], getgame.attrib['faceoffwins'], getgame.attrib['atarena'], getgame.attrib['isplayoffgame']);
      print("   <game date=\""+xml_escape(getgame.attrib['date'], quote=True)+"\" hometeam=\""+xml_escape(getgame.attrib['hometeam'], quote=True)+"\" awayteam=\""+xml_escape(getgame.attrib['awayteam'], quote=True)+"\" goals=\""+xml_escape(getgame.attrib['goals'], quote=True)+"\" sogs=\""+xml_escape(getgame.attrib['sogs'], quote=True)+"\" ppgs=\""+xml_escape(getgame.attrib['ppgs'], quote=True)+"\" shgs=\""+xml_escape(getgame.attrib['shgs'], quote=True)+"\" penalties=\""+xml_escape(getgame.attrib['penalties'], quote=True)+"\" pims=\""+xml_escape(getgame.attrib['pims'], quote=True)+"\" hits=\""+xml_escape(getgame.attrib['hits'], quote=True)+"\" takeaways=\""+xml_escape(getgame.attrib['takeaways'], quote=True)+"\" faceoffwins=\""+xml_escape(getgame.attrib['faceoffwins'], quote=True)+"\" atarena=\""+xml_escape(getgame.attrib['atarena'], quote=True)+"\" isplayoffgame=\""+xml_escape(getgame.attrib['isplayoffgame'], quote=True)+"\" />");
      xmlstring = "   <game date=\""+xml_escape(getgame.attrib['date'], quote=True)+"\" hometeam=\""+xml_escape(getgame.attrib['hometeam'], quote=True)+"\" awayteam=\""+xml_escape(getgame.attrib['awayteam'], quote=True)+"\" goals=\""+xml_escape(getgame.attrib['goals'], quote=True)+"\" sogs=\""+xml_escape(getgame.attrib['sogs'], quote=True)+"\" ppgs=\""+xml_escape(getgame.attrib['ppgs'], quote=True)+"\" shgs=\""+xml_escape(getgame.attrib['shgs'], quote=True)+"\" penalties=\""+xml_escape(getgame.attrib['penalties'], quote=True)+"\" pims=\""+xml_escape(getgame.attrib['pims'], quote=True)+"\" hits=\""+xml_escape(getgame.attrib['hits'], quote=True)+"\" takeaways=\""+xml_escape(getgame.attrib['takeaways'], quote=True)+"\" faceoffwins=\""+xml_escape(getgame.attrib['faceoffwins'], quote=True)+"\" atarena=\""+xml_escape(getgame.attrib['atarena'], quote=True)+"\" isplayoffgame=\""+xml_escape(getgame.attrib['isplayoffgame'], quote=True)+"\" />\n";
      gamecount = gamecount + 1;
     print("  </games>");
     xmlstring = "  </games>\n";
    if(getconference.tag == "conference"):
     divisioncount = 0;
     for getdivision in getconference:
      MakeHockeyDivisions(sqldatacon, getleague.attrib['name'], getdivision.attrib['name'], getconference.attrib['name'], HockeyLeagueHasConferences, HockeyLeagueHasDivisions);
      print("   <division name=\""+xml_escape(getdivision.attrib['name'], quote=True)+"\">");
      xmlstring = "   <division name=\""+xml_escape(getdivision.attrib['name'], quote=True)+"\">\n";
      divisioncount = divisioncount + 1;
      if(getdivision.tag == "division"):
       teamcount = 0;
       for getteam in getdivision:
        if(getteam.tag == "team"):
         MakeHockeyTeams(sqldatacon, getleague.attrib['name'], str(gethockey.attrib['year']+gethockey.attrib['month']+gethockey.attrib['day']), getteam.attrib['city'], getteam.attrib['area'], getteam.attrib['country'], getteam.attrib['fullcountry'], getteam.attrib['fullarea'], getteam.attrib['name'], getconference.attrib['name'], getdivision.attrib['name'], getteam.attrib['arena'], getteam.attrib['prefix'], getteam.attrib['suffix'], HockeyLeagueHasConferences, HockeyLeagueHasDivisions);
         print("    <team city=\""+xml_escape(getteam.attrib['city'], quote=True)+"\" area=\""+xml_escape(getteam.attrib['area'], quote=True)+"\" fullarea=\""+xml_escape(getteam.attrib['fullarea'], quote=True)+"\" country=\""+xml_escape(getteam.attrib['country'], quote=True)+"\" fullcountry=\""+xml_escape(getteam.attrib['fullcountry'], quote=True)+"\" name=\""+xml_escape(getleague.attrib['name'], quote=True)+"\" arena=\""+xml_escape(getteam.attrib['arena'], quote=True)+"\" prefix=\""+xml_escape(getteam.attrib['prefix'], quote=True)+"\" suffix=\""+xml_escape(getteam.attrib['suffix'], quote=True)+"\" />");
         xmlstring = "    <team city=\""+xml_escape(getteam.attrib['city'], quote=True)+"\" area=\""+xml_escape(getteam.attrib['area'], quote=True)+"\" fullarea=\""+xml_escape(getteam.attrib['fullarea'], quote=True)+"\" country=\""+xml_escape(getteam.attrib['country'], quote=True)+"\" fullcountry=\""+xml_escape(getteam.attrib['fullcountry'], quote=True)+"\" name=\""+xml_escape(getleague.attrib['name'], quote=True)+"\" arena=\""+xml_escape(getteam.attrib['arena'], quote=True)+"\" prefix=\""+xml_escape(getteam.attrib['prefix'], quote=True)+"\" suffix=\""+xml_escape(getteam.attrib['suffix'], quote=True)+"\" />\n";
        teamcount = teamcount + 1;
       print("   </division>");
       xmlstring = "   </division>\n";
     print("  </conference>");
     xmlstring = "  </conference>\n";
   print(" </league>");
   xmlstring = " </league>\n";
 print("</hockey>");
 xmlstring = "</hockey>\n";
 CloseHockeyDatabase(sqldatacon);
 if(returnxml is True):
  return xmlstring;
 if(returnxml is False):
  return True;
 return True;

def MakeHockeyDatabaseFromXMLWrite(inxmlfile, sdbfile=None, outxmlfile=None, returnxml=False):
 if(not os.path.exists(inxmlfile) or not os.path.isfile(inxmlfile)):
  return False;
 if(outxmlfile is None):
  file_wo_extension, file_extension = os.path.splitext(inxmlfile);
  outxmlfile = file_wo_extension+".xml";
 xmlfp = open(outxmlfile, "w+");
 xmlstring = MakeHockeyDatabaseFromXML(inxmlfile, sdbfile, True);
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml is True):
  return xmlstring;
 if(returnxml is False):
  return True;
 return True;

def MakeHockeyPythonFromXML(xmlfile):
 pyfilename = __name__;
 if(pyfilename=="__main__"):
  pyfilename = os.path.splitext(os.path.basename(__file__))[0];
 if(os.path.exists(xmlfile) and os.path.isfile(xmlfile)):
  hockeyfile = ET.parse(xmlfile);
 else:
  return False;
 gethockey = hockeyfile.getroot();
 print("#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nfrom __future__ import absolute_import, division, print_function, unicode_literals;\nimport "+pyfilename+";\n");
 pystring = "#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nfrom __future__ import absolute_import, division, print_function, unicode_literals;\nimport "+pyfilename+";\n\n";
 if(gethockey.tag == "hockey"):
  print("sqldatacon = "+pyfilename+".MakeHockeyDatabase(\""+gethockey.attrib['database']+"\");");
  pystring = pystring+"sqldatacon = "+pyfilename+".MakeHockeyDatabase(\""+gethockey.attrib['database']+"\");\n";
 leaguecount = 0;
 print(pyfilename+".MakeHockeyLeagueTable(sqldatacon);");
 pystring = pystring+pyfilename+".MakeHockeyLeagueTable(sqldatacon);\n";
 for getleague in gethockey:
  if(getleague.tag=="league"):
   HockeyLeagueHasDivisions = True;
   if(getleague.attrib['conferences'].lower()=="no"):
    HockeyLeagueHasDivisions = False;
   HockeyLeagueHasConferences = True;
   if(getleague.attrib['divisions'].lower()=="no"):
    HockeyLeagueHasConferences = False;
   print(pyfilename+".MakeHockeyTeamTable(sqldatacon, \""+getleague.attrib['name']+"\");\n"+pyfilename+".MakeHockeyConferenceTable(sqldatacon, \""+getleague.attrib['name']+"\");\n"+pyfilename+".MakeHockeyGameTable(sqldatacon, \""+getleague.attrib['name']+"\");\n"+pyfilename+".MakeHockeyDivisionTable(sqldatacon, \""+getleague.attrib['name']+"\");\n"+pyfilename+".MakeHockeyLeagues(sqldatacon, \""+getleague.attrib['name']+"\", \""+getleague.attrib['fullname']+"\", \""+getleague.attrib['country']+"\", \""+getleague.attrib['fullcountry']+"\");");
   pystring = pystring+pyfilename+".MakeHockeyTeamTable(sqldatacon, \""+getleague.attrib['name']+"\");\n"+pyfilename+".MakeHockeyConferenceTable(sqldatacon, \""+getleague.attrib['name']+"\");\n"+pyfilename+".MakeHockeyGameTable(sqldatacon, \""+getleague.attrib['name']+"\");\n"+pyfilename+".MakeHockeyDivisionTable(sqldatacon, \""+getleague.attrib['name']+"\");\n"+pyfilename+".MakeHockeyLeagues(sqldatacon, \""+getleague.attrib['name']+"\", \""+getleague.attrib['fullname']+"\", \""+getleague.attrib['country']+"\", \""+getleague.attrib['fullcountry']+"\");\n";
  leaguecount = leaguecount + 1;
  if(getleague.tag == "league"):
   conferencecount = 0;
   for getconference in getleague:
    if(getconference.tag == "conference"):
     print(pyfilename+".MakeHockeyConferences(sqldatacon, \""+getleague.attrib['name']+"\", \""+getconference.attrib['name']+"\", "+str(HockeyLeagueHasConferences)+");");
     pystring = pystring+pyfilename+".MakeHockeyConferences(sqldatacon, \""+getleague.attrib['name']+"\", \""+getconference.attrib['name']+"\", "+str(HockeyLeagueHasConferences)+");\n";
     conferencecount = conferencecount + 1;
    if(getconference.tag == "arenas"):
     arenascount = 0;
     for getarenas in getconference:
      print(pyfilename+".MakeHockeyArena(sqldatacon, \""+getleague.attrib['name']+"\", \""+getarenas.attrib['city']+"\", \""+getarenas.attrib['area']+"\", \""+getarenas.attrib['country']+"\", \""+getarenas.attrib['fullcountry']+"\", \""+getarenas.attrib['fullarea']+"\", \""+getarenas.attrib['name']+"\");");
      pystring = pystring+pyfilename+".MakeHockeyArena(sqldatacon, \""+getleague.attrib['name']+"\", \""+getarenas.attrib['city']+"\", \""+getarenas.attrib['area']+"\", \""+getarenas.attrib['country']+"\", \""+getarenas.attrib['fullcountry']+"\", \""+getarenas.attrib['fullarea']+"\", \""+getarenas.attrib['name']+"\");\n";
      arenascount = arenascount + 1;
    if(getconference.tag == "games"):
     gamecount = 0;
     for getgame in getconference:
      print(pyfilename+".MakeHockeyGame(sqldatacon, \""+getleague.attrib['name']+"\", "+getgame.attrib['date']+", \""+getgame.attrib['hometeam']+"\", \""+getgame.attrib['awayteam']+"\", \""+getgame.attrib['goals']+"\", \""+getgame.attrib['sogs']+"\", \""+getgame.attrib['ppgs']+"\", \""+getgame.attrib['shgs']+"\", \""+getgame.attrib['penalties']+"\", \""+getgame.attrib['pims']+"\", \""+getgame.attrib['hits']+"\", \""+getgame.attrib['takeaways']+"\", \""+getgame.attrib['faceoffwins']+"\", \""+getgame.attrib['atarena']+"\", \""+getgame.attrib['isplayoffgame']+"\");");
      pystring = pystring+pyfilename+".MakeHockeyGame(sqldatacon, \""+getleague.attrib['name']+"\", "+getgame.attrib['date']+", \""+getgame.attrib['hometeam']+"\", \""+getgame.attrib['awayteam']+"\", \""+getgame.attrib['goals']+"\", \""+getgame.attrib['sogs']+"\", \""+getgame.attrib['ppgs']+"\", \""+getgame.attrib['shgs']+"\", \""+getgame.attrib['penalties']+"\", \""+getgame.attrib['pims']+"\", \""+getgame.attrib['hits']+"\", \""+getgame.attrib['takeaways']+"\", \""+getgame.attrib['faceoffwins']+"\", \""+getgame.attrib['atarena']+"\", \""+getgame.attrib['isplayoffgame']+"\");\n";
      gamecount = gamecount + 1;
    if(getconference.tag == "conference"):
     divisioncount = 0;
     for getdivision in getconference:
      print(pyfilename+".MakeHockeyDivisions(sqldatacon, \""+getleague.attrib['name']+"\", \""+getdivision.attrib['name']+"\", \""+getconference.attrib['name']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");");
      pystring = pystring+pyfilename+".MakeHockeyDivisions(sqldatacon, \""+getleague.attrib['name']+"\", \""+getdivision.attrib['name']+"\", \""+getconference.attrib['name']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");\n";
      divisioncount = divisioncount + 1;
      if(getdivision.tag == "division"):
       teamcount = 0;
       for getteam in getdivision:
        if(getteam.tag == "team"):
         print(pyfilename+".MakeHockeyTeams(sqldatacon, \""+getleague.attrib['name']+"\", "+str(gethockey.attrib['year']+gethockey.attrib['month']+gethockey.attrib['day'])+", \""+getteam.attrib['city']+"\", \""+getteam.attrib['area']+"\", \""+getteam.attrib['country']+"\", \""+getteam.attrib['fullcountry']+"\", \""+getteam.attrib['fullarea']+"\", \""+getteam.attrib['name']+"\", \""+getconference.attrib['name']+"\", \""+getdivision.attrib['name']+"\", \""+getteam.attrib['arena']+"\", \""+getteam.attrib['prefix']+"\", \""+getteam.attrib['suffix']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");");
         pystring = pystring+pyfilename+".MakeHockeyTeams(sqldatacon, \""+getleague.attrib['name']+"\", "+str(gethockey.attrib['year']+gethockey.attrib['month']+gethockey.attrib['day'])+", \""+getteam.attrib['city']+"\", \""+getteam.attrib['area']+"\", \""+getteam.attrib['country']+"\", \""+getteam.attrib['fullcountry']+"\", \""+getteam.attrib['fullarea']+"\", \""+getteam.attrib['name']+"\", \""+getconference.attrib['name']+"\", \""+getdivision.attrib['name']+"\", \""+getteam.attrib['arena']+"\", \""+getteam.attrib['prefix']+"\", \""+getteam.attrib['suffix']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");\n";
        teamcount = teamcount + 1;
  print(" ");
  pystring = pystring+"\n";
 print(pyfilename+".CloseHockeyDatabase(sqldatacon);");
 pystring = pystring+pyfilename+".CloseHockeyDatabase(sqldatacon);\n";
 return pystring;

def MakeHockeyPythonFileFromXML(inxmlfile, outpyfile=None, returnpy=False):
 if(not os.path.exists(inxmlfile) or not os.path.isfile(inxmlfile)):
  return False;
 if(outpyfile is None):
  file_wo_extension, file_extension = os.path.splitext(inxmlfile);
  outpyfile = file_wo_extension+".xml";
 pyfp = open(outpyfile, "w+");
 pystring = MakeHockeyPyFromXML(inxmlfile);
 pyfp.write(pystring);
 pyfp.close();
 if(returnpy is True):
  return pystring;
 if(returnpy is False):
  return True;
 return True;

def MakeXMLFromHockeyDatabase(sdbfile, date):
 chckyear = date[:4];
 chckmonth = date[4:6];
 chckday = date[6:8];
 if(os.path.exists(sdbfile) and os.path.isfile(sdbfile)):
  sqlcon = sqlite3.connect(sdbfile, isolation_level=None);
 else:
  return False;
 leaguecur = sqlcon.cursor();
 xmlstring = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
 xmlstring = xmlstring+"<hockey database=\""+xml_escape(sdbfile, quote=True)+"\" year=\""+xml_escape(chckyear, quote=True)+"\" month=\""+xml_escape(chckmonth, quote=True)+"\" day=\""+xml_escape(chckday, quote=True)+"\">\n";
 print("<?xml version=\"1.0\" encoding=\"UTF-8\"?>");
 print("<hockey database=\""+xml_escape(sdbfile, quote=True)+"\" year=\""+xml_escape(chckyear, quote=True)+"\" month=\""+xml_escape(chckmonth, quote=True)+"\" day=\""+xml_escape(chckday, quote=True)+"\">");
 getleague_num = leaguecur.execute("SELECT COUNT(*) FROM HockeyLeagues").fetchone()[0];
 getleague = leaguecur.execute("SELECT LeagueName, LeagueFullName, CountryName, FullCountryName, NumberOfConferences, NumberOfDivisions FROM HockeyLeagues");
 for leagueinfo in getleague:
  HockeyLeagueHasDivisions = "yes";
  if(int(leagueinfo[4])<=0):
   HockeyLeagueHasDivisions = "no";
  HockeyLeagueHasConferences = "yes";
  if(int(leagueinfo[5])<=0):
   HockeyLeagueHasConferences = "no";
  xmlstring = xmlstring+" <league name=\""+xml_escape(leagueinfo[0], quote=True)+"\" fullname=\""+xml_escape(leagueinfo[1], quote=True)+"\" country=\""+xml_escape(leagueinfo[2], quote=True)+"\" fullcountry=\""+xml_escape(leagueinfo[3], quote=True)+"\" conferences=\""+xml_escape(leagueinfo[3], quote=True)+"\" divisions=\""+xml_escape(leagueinfo[3], quote=True)+"\">\n";
  print(" <league name=\""+xml_escape(leagueinfo[0], quote=True)+"\" fullname=\""+xml_escape(leagueinfo[1], quote=True)+"\" country=\""+xml_escape(leagueinfo[2], quote=True)+"\" fullcountry=\""+xml_escape(leagueinfo[3], quote=True)+"\" conferences=\""+xml_escape(leagueinfo[3], quote=True)+"\" divisions=\""+xml_escape(leagueinfo[3], quote=True)+"\">");
  conferencecur = sqlcon.cursor();
  getconference_num = conferencecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Conferences WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\"").fetchone()[0];
  getconference = conferencecur.execute("SELECT Conference FROM "+leagueinfo[0]+"Conferences WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\"");
  for conferenceinfo in getconference:
   xmlstring = xmlstring+"  <conference name=\""+xml_escape(conferenceinfo[0], quote=True)+"\">\n";
   print("  <conference name=\""+xml_escape(conferenceinfo[0], quote=True)+"\">");
   divisioncur = sqlcon.cursor();
   getdivision_num = divisioncur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Divisions WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\"").fetchone()[0];
   getdivision = divisioncur.execute("SELECT Division FROM "+leagueinfo[0]+"Divisions WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\"");
   for divisioninfo in getdivision:
    xmlstring = xmlstring+"   <division name=\""+xml_escape(divisioninfo[0], quote=True)+"\">\n";
    print("   <division name=\""+xml_escape(divisioninfo[0], quote=True)+"\">");
    teamcur = sqlcon.cursor();
    getteam_num = teamcur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Teams WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"").fetchone()[0];
    getteam = teamcur.execute("SELECT CityName, AreaName, FullAreaName, CountryName, FullCountryName, TeamName, ArenaName, TeamPrefix, TeamSuffix FROM "+leagueinfo[0]+"Teams WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"");
    for teaminfo in getteam:
     xmlstring = xmlstring+"    <team city=\""+xml_escape(teaminfo[0], quote=True)+"\" area=\""+xml_escape(teaminfo[1], quote=True)+"\" fullarea=\""+xml_escape(teaminfo[2], quote=True)+"\" country=\""+xml_escape(teaminfo[3], quote=True)+"\" fullcountry=\""+xml_escape(teaminfo[4], quote=True)+"\" name=\""+xml_escape(teaminfo[5], quote=True)+"\" arena=\""+xml_escape(teaminfo[6], quote=True)+"\" prefix=\""+xml_escape(teaminfo[7], quote=True)+"\" suffix=\""+xml_escape(teaminfo[8], quote=True)+"\" />\n";
     print("    <team city=\""+xml_escape(teaminfo[0], quote=True)+"\" area=\""+xml_escape(teaminfo[1], quote=True)+"\" fullarea=\""+xml_escape(teaminfo[2], quote=True)+"\" country=\""+xml_escape(teaminfo[3], quote=True)+"\" fullcountry=\""+xml_escape(teaminfo[4], quote=True)+"\" name=\""+xml_escape(teaminfo[5], quote=True)+"\" arena=\""+xml_escape(teaminfo[6], quote=True)+"\" prefix=\""+xml_escape(teaminfo[7], quote=True)+"\" suffix=\""+xml_escape(teaminfo[8], quote=True)+"\" />");
    teamcur.close();
    xmlstring = xmlstring+"   </division>\n";
    print("   </division>");
   divisioncur.close();
   xmlstring = xmlstring+"  </conference>\n";
   print("  </conference>");
  conferencecur.close();
  arenacur = sqlcon.cursor();
  getteam_num = arenacur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Arenas WHERE TeamID=0").fetchone()[0];
  getarena = arenacur.execute("SELECT CityName, AreaName, FullAreaName, CountryName, FullCountryName, ArenaName FROM "+leagueinfo[0]+"Arenas WHERE TeamID=0");
  if(getteam_num>0):
   xmlstring = xmlstring+"  <arenas>\n";
   print("  <arenas>");
   for arenainfo in getarena:
    xmlstring = xmlstring+"   <arena city=\""+xml_escape(arenainfo[0], quote=True)+"\" area=\""+xml_escape(arenainfo[1], quote=True)+"\" fullarea=\""+xml_escape(arenainfo[2], quote=True)+"\" country=\""+xml_escape(arenainfo[3], quote=True)+"\" fullcountry=\""+xml_escape(arenainfo[4], quote=True)+"\" name=\""+xml_escape(arenainfo[5], quote=True)+"\" />\n";
    print("   <arena city=\""+xml_escape(arenainfo[0], quote=True)+"\" area=\""+xml_escape(arenainfo[1], quote=True)+"\" fullarea=\""+xml_escape(arenainfo[2], quote=True)+"\" country=\""+xml_escape(arenainfo[3], quote=True)+"\" fullcountry=\""+xml_escape(arenainfo[4], quote=True)+"\" name=\""+xml_escape(arenainfo[5], quote=True)+"\" />");
   xmlstring = xmlstring+"  </arenas>\n";
   print("  </arenas>");
  gamecur = sqlcon.cursor();
  getgame_num = gamecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Games").fetchone()[0];
  getgame = gamecur.execute("SELECT Date, HomeTeam, AwayTeam, TeamScorePeriods, ShotsOnGoal, PowerPlays, ShortHanded, Penalties, PenaltyMinutes, HitsPerPeriod, TakeAways, FaceoffWins, AtArena, IsPlayOffGame FROM "+leagueinfo[0]+"Games");
  if(getgame_num>0):
   xmlstring = xmlstring+"  <games>\n";
   print("  <games>");
   for gameinfo in getgame:
    xmlstring = xmlstring+"   <game date=\""+xml_escape(gameinfo[0], quote=True)+"\" hometeam=\""+xml_escape(gameinfo[1], quote=True)+"\" awayteam=\""+xml_escape(gameinfo[2], quote=True)+"\" goals=\""+xml_escape(gameinfo[3], quote=True)+"\" sogs=\""+xml_escape(gameinfo[4], quote=True)+"\" ppgs=\""+xml_escape(gameinfo[5], quote=True)+"\" shgs=\""+xml_escape(gameinfo[6], quote=True)+"\" penalties=\""+xml_escape(gameinfo[7], quote=True)+"\" pims=\""+xml_escape(gameinfo[8], quote=True)+"\" hits=\""+xml_escape(gameinfo[9], quote=True)+"\" takeaways=\""+xml_escape(gameinfo[10], quote=True)+"\" faceoffwins=\""+xml_escape(gameinfo[11], quote=True)+"\" atarena=\""+xml_escape(gameinfo[12], quote=True)+"\" isplayoffgame=\""+xml_escape(gameinfo[13], quote=True)+"\" />\n";
    print("   <game date=\""+xml_escape(gameinfo[0], quote=True)+"\" hometeam=\""+xml_escape(gameinfo[1], quote=True)+"\" awayteam=\""+xml_escape(gameinfo[2], quote=True)+"\" goals=\""+xml_escape(gameinfo[3], quote=True)+"\" sogs=\""+xml_escape(gameinfo[4], quote=True)+"\" ppgs=\""+xml_escape(gameinfo[5], quote=True)+"\" shgs=\""+xml_escape(gameinfo[6], quote=True)+"\" penalties=\""+xml_escape(gameinfo[7], quote=True)+"\" pims=\""+xml_escape(gameinfo[8], quote=True)+"\" hits=\""+xml_escape(gameinfo[9], quote=True)+"\" takeaways=\""+xml_escape(gameinfo[10], quote=True)+"\" faceoffwins=\""+xml_escape(gameinfo[11], quote=True)+"\" atarena=\""+xml_escape(gameinfo[12], quote=True)+"\" isplayoffgame=\""+xml_escape(gameinfo[13], quote=True)+"\" />");
   xmlstring = xmlstring+"  </games>\n";
   print("  </games>");
  xmlstring = xmlstring+" </league>\n";
  print(" </league>");
 xmlstring = xmlstring+"</hockey>\n";
 print("</hockey>");
 leaguecur.close();
 sqlcon.close();
 return xmlstring;

def MakeXMLFileFromHockeyDatabase(sdbfile, date, xmlfile=None, returnxml=False):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(xmlfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  xmlfile = file_wo_extension+".xml";
 xmlfp = open(xmlfile, "w+");
 xmlstring = MakeXMLFromHockeyData(sdbfile, date);
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml is True):
  return xmlstring;
 if(returnxml is False):
  return True;
 return True;

def MakeHockeyPythonFromHockeyDatabase(sdbfile, date):
 pyfilename = __name__;
 if(pyfilename=="__main__"):
  pyfilename = os.path.splitext(os.path.basename(__file__))[0];
 chckyear = date[:4];
 chckmonth = date[4:6];
 chckday = date[6:8];
 if(os.path.exists(sdbfile) and os.path.isfile(sdbfile)):
  sqlcon = sqlite3.connect(sdbfile, isolation_level=None);
 else:
  return False;
 print("#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nfrom __future__ import absolute_import, division, print_function, unicode_literals;\nimport "+pyfilename+";\n");
 pystring = "#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nfrom __future__ import absolute_import, division, print_function, unicode_literals;\nimport "+pyfilename+";\n\n";
 print("sqldatacon = "+pyfilename+".MakeHockeyDatabase(\""+sdbfile+"\");");
 pystring = pystring+"sqldatacon = "+pyfilename+".MakeHockeyDatabase(\""+sdbfile+"\");\n";
 leaguecur = sqlcon.cursor();
 getleague_num = leaguecur.execute("SELECT COUNT(*) FROM HockeyLeagues").fetchone()[0];
 getleague = leaguecur.execute("SELECT LeagueName, LeagueFullName, CountryName, FullCountryName, NumberOfConferences, NumberOfDivisions FROM HockeyLeagues");
 print(pyfilename+".MakeHockeyLeagueTable(sqldatacon);");
 pystring = pystring+pyfilename+".MakeHockeyLeagueTable(sqldatacon);\n";
 for leagueinfo in getleague:
  HockeyLeagueHasDivisions = True;
  if(int(leagueinfo[4])<=0):
   HockeyLeagueHasDivisions = False;
  HockeyLeagueHasConferences = True;
  if(int(leagueinfo[5])<=0):
   HockeyLeagueHasConferences = False;
  print(pyfilename+".MakeHockeyTeamTable(sqldatacon, \""+leagueinfo[0]+"\");\n"+pyfilename+".MakeHockeyConferenceTable(sqldatacon, \""+leagueinfo[0]+"\");\n"+pyfilename+".MakeHockeyGameTable(sqldatacon, \""+leagueinfo[0]+"\");\n"+pyfilename+".MakeHockeyDivisionTable(sqldatacon, \""+leagueinfo[0]+"\");\n"+pyfilename+".MakeHockeyLeagues(sqldatacon, \""+leagueinfo[0]+"\", \""+leagueinfo[1]+"\", \""+leagueinfo[2]+"\", \""+leagueinfo[3]+"\");");
  pystring = pystring+pyfilename+".MakeHockeyTeamTable(sqldatacon, \""+leagueinfo[0]+"\");\n"+pyfilename+".MakeHockeyConferenceTable(sqldatacon, \""+leagueinfo[0]+"\");\n"+pyfilename+".MakeHockeyGameTable(sqldatacon, \""+leagueinfo[0]+"\");\n"+pyfilename+".MakeHockeyDivisionTable(sqldatacon, \""+leagueinfo[0]+"\");\n"+pyfilename+".MakeHockeyLeagues(sqldatacon, \""+leagueinfo[0]+"\", \""+leagueinfo[1]+"\", \""+leagueinfo[2]+"\", \""+leagueinfo[3]+"\");\n";
  conferencecur = sqlcon.cursor();
  getconference_num = conferencecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Conferences WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\"").fetchone()[0];
  getconference = conferencecur.execute("SELECT Conference FROM "+leagueinfo[0]+"Conferences WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\"");
  for conferenceinfo in getconference:
   print(pyfilename+".MakeHockeyConferences(sqldatacon, \""+leagueinfo[0]+"\", \""+conferenceinfo[0]+"\", "+str(HockeyLeagueHasConferences)+");");
   pystring = pystring+pyfilename+".MakeHockeyConferences(sqldatacon, \""+leagueinfo[0]+"\", \""+conferenceinfo[0]+"\", "+str(HockeyLeagueHasConferences)+");\n";
   divisioncur = sqlcon.cursor();
   getdivision_num = divisioncur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Divisions WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\"").fetchone()[0];
   getdivision = divisioncur.execute("SELECT Division FROM "+leagueinfo[0]+"Divisions WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\"");
   for divisioninfo in getdivision:
    print(pyfilename+".MakeHockeyDivisions(sqldatacon, \""+leagueinfo[0]+"\", \""+divisioninfo[0]+"\", \""+conferenceinfo[0]+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");");
    pystring = pystring+pyfilename+".MakeHockeyDivisions(sqldatacon, \""+leagueinfo[0]+"\", \""+divisioninfo[0]+"\", \""+conferenceinfo[0]+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");\n";
    teamcur = sqlcon.cursor();
    getteam_num = teamcur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Teams WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"").fetchone()[0];
    getteam = teamcur.execute("SELECT CityName, AreaName, FullAreaName, CountryName, FullCountryName, TeamName, ArenaName, TeamPrefix, TeamSuffix FROM "+leagueinfo[0]+"Teams WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"");
    for teaminfo in getteam:
     print(pyfilename+".MakeHockeyTeams(sqldatacon, \""+leagueinfo[0]+"\", "+str(chckyear+chckmonth+chckday)+", \""+teaminfo[0]+"\", \""+teaminfo[1]+"\", \""+teaminfo[3]+"\", \""+teaminfo[4]+"\", \""+teaminfo[2]+"\", \""+teaminfo[5]+"\", \""+conferenceinfo[0]+"\", \""+divisioninfo[0]+"\", \""+teaminfo[6]+"\", \""+teaminfo[7]+"\", \""+teaminfo[8]+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");");
     pystring = pystring+pyfilename+".MakeHockeyTeams(sqldatacon, \""+leagueinfo[0]+"\", "+str(chckyear+chckmonth+chckday)+", \""+teaminfo[0]+"\", \""+teaminfo[1]+"\", \""+teaminfo[3]+"\", \""+teaminfo[4]+"\", \""+teaminfo[2]+"\", \""+teaminfo[5]+"\", \""+conferenceinfo[0]+"\", \""+divisioninfo[0]+"\", \""+teaminfo[6]+"\", \""+teaminfo[7]+"\", \""+teaminfo[8]+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");\n";
    teamcur.close();
   divisioncur.close();
  conferencecur.close();
  arenacur = sqlcon.cursor();
  getteam_num = arenacur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Arenas WHERE TeamID=0").fetchone()[0];
  getarena = arenacur.execute("SELECT CityName, AreaName, FullAreaName, CountryName, FullCountryName, ArenaName FROM "+leagueinfo[0]+"Arenas WHERE TeamID=0");
  if(getteam_num>0):
   for arenainfo in getarena:
    print(pyfilename+".MakeHockeyArena(sqldatacon, \""+leagueinfo[0]+"\", \""+arenainfo[0]+"\", \""+arenainfo[1]+"\", \""+arenainfo[3]+"\", \""+arenainfo[4]+"\", \""+arenainfo[2]+"\", \""+arenainfo[5]+"\");");
    pystring = pystring+pyfilename+".MakeHockeyArena(sqldatacon, \""+leagueinfo[0]+"\", \""+arenainfo[0]+"\", \""+arenainfo[1]+"\", \""+arenainfo[3]+"\", \""+arenainfo[4]+"\", \""+arenainfo[2]+"\", \""+arenainfo[5]+"\");\n";
  gamecur = sqlcon.cursor();
  getgame_num = gamecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Games").fetchone()[0];
  getgame = gamecur.execute("SELECT Date, HomeTeam, AwayTeam, TeamScorePeriods, ShotsOnGoal, PowerPlays, ShortHanded, Penalties, PenaltyMinutes, HitsPerPeriod, TakeAways, FaceoffWins, AtArena, IsPlayOffGame FROM "+leagueinfo[0]+"Games");
  if(getgame_num>0):
   for gameinfo in getgame:
    print(pyfilename+".MakeHockeyGame(sqldatacon, \""+leagueinfo[0]+"\", "+gameinfo[0]+", \""+gameinfo[1]+"\", \""+gameinfo[2]+"\", \""+gameinfo[3]+"\", \""+gameinfo[4]+"\", \""+gameinfo[5]+"\", \""+gameinfo[6]+"\", \""+gameinfo[7]+"\", \""+gameinfo[8]+"\", \""+gameinfo[9]+"\", \""+gameinfo[10]+"\", \""+gameinfo[11]+"\", \""+gameinfo[12]+"\", \""+gameinfo[13]+"\");");
    pystring = pystring+pyfilename+".MakeHockeyGame(sqldatacon, \""+leagueinfo[0]+"\", "+gameinfo[0]+", \""+gameinfo[1]+"\", \""+gameinfo[2]+"\", \""+gameinfo[3]+"\", \""+gameinfo[4]+"\", \""+gameinfo[5]+"\", \""+gameinfo[6]+"\", \""+gameinfo[7]+"\", \""+gameinfo[8]+"\", \""+gameinfo[9]+"\", \""+gameinfo[10]+"\", \""+gameinfo[11]+"\", \""+gameinfo[12]+"\", \""+gameinfo[13]+"\");\n";
  print(" ");
  pystring = pystring+"\n";
 leaguecur.close();
 sqlcon.close();
 print(pyfilename+".CloseHockeyDatabase(sqldatacon);");
 pystring = pystring+pyfilename+".CloseHockeyDatabase(sqldatacon);\n";
 return pystring;

def MakeHockeyPythonFileFromHockeyDatabase(sdbfile, date, pyfile=None, returnpy=False):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(pyfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  pyfile = file_wo_extension+".xml";
 pyfp = open(pyfile, "w+");
 pystring = MakeHockeyPyFromHockeyData(sdbfile, date);
 pyfp.write(pystring);
 pyfp.close();
 if(returnpy is True):
  return pystring;
 if(returnpy is False):
  return True;
 return True;

def MakeHockeySQLFromHockeyDatabase(sdbfile):
 if(os.path.exists(sdbfile) and os.path.isfile(sdbfile)):
  sqldatacon = OpenHockeyDatabase(sdbfile);
 else:
  return False;
 sqldump = "-- "+__program_name__+" SQL Dumper\n";
 sqldump = sqldump+"-- "+__version__+"\n";
 sqldump = sqldump+"-- "+__project_url__+"\n";
 sqldump = sqldump+"--\n";
 sqldump = sqldump+"-- Generation Time: "+time.strftime("%B %d, %Y at %I:%M %p", time.localtime())+"\n";
 sqldump = sqldump+"-- SQLite Server version: "+sqlite3.sqlite_version+"\n";
 sqldump = sqldump+"-- PySQLite version: "+sqlite3.version+"\n";
 sqldump = sqldump+"-- Python Version: "+str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2])+"\n\n";
 sqldump = sqldump+"--\n";
 sqldump = sqldump+"-- Database: "+sdbfile+"\n";
 sqldump = sqldump+"--\n\n";
 sqldump = sqldump+"-- --------------------------------------------------------\n\n";
 all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games"];
 table_list = ['HockeyLeagues'];
 getleague_num_tmp = sqldatacon[0].execute("SELECT COUNT(*) FROM HockeyLeagues").fetchone()[0];
 getleague_tmp = sqldatacon[0].execute("SELECT LeagueName FROM HockeyLeagues");
 for leagueinfo_tmp in getleague_tmp:
  for cur_tab in all_table_list:
   table_list.append(leagueinfo_tmp[0]+cur_tab);
 for get_cur_tab in table_list:
  tresult = sqldatacon[0].execute("SELECT * FROM "+get_cur_tab);
  tmbcor = sqldatacon[1].cursor();
  tabresult = tmbcor.execute("SELECT * FROM sqlite_master WHERE type=\"table\" and tbl_name=\""+get_cur_tab+"\";").fetchone()[4];
  tabresultcol = list(map(lambda x: x[0], sqldatacon[0].description));
  tresult_list = [];
  sqldump = sqldump+"--\n";
  sqldump = sqldump+"-- Table structure for table "+str(get_cur_tab)+"\n";
  sqldump = sqldump+"--\n\n";
  sqldump = sqldump+tabresult+"\n\n";
  sqldump = sqldump+"--\n";
  sqldump = sqldump+"-- Dumping data for table "+str(get_cur_tab)+"\n";
  sqldump = sqldump+"--\n\n";
  get_insert_stmt_full = "";
  for tresult_tmp in tresult:
   get_insert_stmt = "INSERT INTO "+str(get_cur_tab)+" (";
   get_insert_stmt_val = "(";
   for result_cal_val in tabresultcol:
    get_insert_stmt += str(result_cal_val)+", ";
   for result_val in tresult_tmp:
    if(isinstance(result_val, str)):
     get_insert_stmt_val += "\""+str(result_val)+"\", ";
    if(isinstance(result_val, int)):
     get_insert_stmt_val += ""+str(result_val)+", ";
   get_insert_stmt = get_insert_stmt[:-3]+") VALUES \n";
   get_insert_stmt_val = get_insert_stmt_val[:-3]+");";
   get_insert_stmt_full += str(get_insert_stmt+get_insert_stmt_val)+"\n";
  sqldump = sqldump+get_insert_stmt_full+"\n-- --------------------------------------------------------\n\n";
 CloseHockeyDatabase(sqldatacon);
 return sqldump;

def MakeHockeySQLFileFromHockeyDatabase(sdbfile, sqlfile=None, returnsql=False):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(sqlfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  sqlfile = file_wo_extension+".sql";
 sqlfp = open(sqlfile, "w+");
 sqlstring = MakeHockeySQLFromHockeyData(sdbfile);
 sqlfp.write(sqlstring);
 sqlfp.close();
 if(returnsql is True):
  return sqlstring;
 if(returnsql is False):
  return True;
 return True;

def MakeHockeySQLFromXML(xmlfile, returnsql=False):
 if(os.path.exists(xmlfile) and os.path.isfile(xmlfile)):
  hockeyfile = ET.parse(xmlfile);
 else:
  return False;
 gethockey = hockeyfile.getroot();
 if(gethockey.tag == "hockey"):
  sqldatacon = MakeHockeyDatabase(":memory:");
 leaguecount = 0;
 for getleague in gethockey:
  if(leaguecount==0 and getleague.tag=="league"):
   MakeHockeyLeagueTable(sqldatacon);
  if(getleague.tag=="league"):
   MakeHockeyTeamTable(sqldatacon, getleague.attrib['name']);
   MakeHockeyConferenceTable(sqldatacon, getleague.attrib['name']);
   MakeHockeyGameTable(sqldatacon, getleague.attrib['name']);
   MakeHockeyDivisionTable(sqldatacon, getleague.attrib['name']);
   HockeyLeagueHasDivisions = True;
   if(getleague.attrib['conferences'].lower()=="no"):
    HockeyLeagueHasDivisions = False;
   HockeyLeagueHasConferences = True;
   if(getleague.attrib['divisions'].lower()=="no"):
    HockeyLeagueHasConferences = False;
   MakeHockeyLeagues(sqldatacon, getleague.attrib['name'], getleague.attrib['fullname'], getleague.attrib['country'], getleague.attrib['fullcountry']);
  leaguecount = leaguecount + 1;
  if(getleague.tag == "league"):
   conferencecount = 0;
   for getconference in getleague:
    if(getconference.tag == "conference"):
     MakeHockeyConferences(sqldatacon, getleague.attrib['name'], getconference.attrib['name'], HockeyLeagueHasConferences);
     conferencecount = conferencecount + 1;
    if(getconference.tag == "arenas"):
     arenascount = 0;
     for getarenas in getconference:
      MakeHockeyArena(sqldatacon, getleague.attrib['name'], getarenas.attrib['city'], getarenas.attrib['area'], getarenas.attrib['country'], getarenas.attrib['fullcountry'], getarenas.attrib['fullarea'], getarenas.attrib['name']);
      arenascount = arenascount + 1;
    if(getconference.tag == "games"):
     gamecount = 0;
     for getgame in getconference:
      MakeHockeyGame(sqldatacon, getleague.attrib['name'], getgame.attrib['date'], getgame.attrib['hometeam'], getgame.attrib['awayteam'], getgame.attrib['goals'], getgame.attrib['sogs'], getgame.attrib['ppgs'], getgame.attrib['shgs'], getgame.attrib['penalties'], getgame.attrib['pims'], getgame.attrib['hits'], getgame.attrib['takeaways'], getgame.attrib['faceoffwins'], getgame.attrib['atarena'], getgame.attrib['isplayoffgame']);
      gamecount = gamecount + 1;
    if(getconference.tag == "conference"):
     divisioncount = 0;
     for getdivision in getconference:
      MakeHockeyDivisions(sqldatacon, getleague.attrib['name'], getdivision.attrib['name'], getconference.attrib['name'], HockeyLeagueHasConferences, HockeyLeagueHasDivisions);
      divisioncount = divisioncount + 1;
      if(getdivision.tag == "division"):
       teamcount = 0;
       for getteam in getdivision:
        if(getteam.tag == "team"):
         MakeHockeyTeams(sqldatacon, getleague.attrib['name'], str(gethockey.attrib['year']+gethockey.attrib['month']+gethockey.attrib['day']), getteam.attrib['city'], getteam.attrib['area'], getteam.attrib['country'], getteam.attrib['fullcountry'], getteam.attrib['fullarea'], getteam.attrib['name'], getconference.attrib['name'], getdivision.attrib['name'], getteam.attrib['arena'], getteam.attrib['prefix'], getteam.attrib['suffix'], HockeyLeagueHasConferences, HockeyLeagueHasDivisions);
        teamcount = teamcount + 1;
 sqldump = "-- "+__program_name__+" SQL Dumper\n";
 sqldump = sqldump+"-- "+__version__+"\n";
 sqldump = sqldump+"-- "+__project_url__+"\n";
 sqldump = sqldump+"--\n";
 sqldump = sqldump+"-- Generation Time: "+time.strftime("%B %d, %Y at %I:%M %p", time.localtime())+"\n";
 sqldump = sqldump+"-- SQLite Server version: "+sqlite3.sqlite_version+"\n";
 sqldump = sqldump+"-- PySQLite version: "+sqlite3.version+"\n";
 sqldump = sqldump+"-- Python Version: "+str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2])+"\n\n";
 sqldump = sqldump+"--\n";
 sqldump = sqldump+"-- Database: :memory:\n";
 sqldump = sqldump+"--\n\n";
 sqldump = sqldump+"-- --------------------------------------------------------\n\n";
 all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games"];
 table_list = ['HockeyLeagues'];
 getleague_num_tmp = sqldatacon[0].execute("SELECT COUNT(*) FROM HockeyLeagues").fetchone()[0];
 getleague_tmp = sqldatacon[0].execute("SELECT LeagueName FROM HockeyLeagues");
 for leagueinfo_tmp in getleague_tmp:
  for cur_tab in all_table_list:
   table_list.append(leagueinfo_tmp[0]+cur_tab);
 for get_cur_tab in table_list:
  tresult = sqldatacon[0].execute("SELECT * FROM "+get_cur_tab);
  tmbcor = sqldatacon[1].cursor();
  tabresult = tmbcor.execute("SELECT * FROM sqlite_master WHERE type=\"table\" and tbl_name=\""+get_cur_tab+"\";").fetchone()[4];
  tabresultcol = list(map(lambda x: x[0], sqldatacon[0].description));
  tresult_list = [];
  sqldump = sqldump+"--\n";
  sqldump = sqldump+"-- Table structure for table "+str(get_cur_tab)+"\n";
  sqldump = sqldump+"--\n\n";
  sqldump = sqldump+tabresult+"\n\n";
  sqldump = sqldump+"--\n";
  sqldump = sqldump+"-- Dumping data for table "+str(get_cur_tab)+"\n";
  sqldump = sqldump+"--\n\n";
  get_insert_stmt_full = "";
  for tresult_tmp in tresult:
   get_insert_stmt = "INSERT INTO "+str(get_cur_tab)+" (";
   get_insert_stmt_val = "(";
   for result_cal_val in tabresultcol:
    get_insert_stmt += str(result_cal_val)+", ";
   for result_val in tresult_tmp:
    if(isinstance(result_val, str)):
     get_insert_stmt_val += "\""+str(result_val)+"\", ";
    if(isinstance(result_val, int)):
     get_insert_stmt_val += ""+str(result_val)+", ";
   get_insert_stmt = get_insert_stmt[:-3]+") VALUES \n";
   get_insert_stmt_val = get_insert_stmt_val[:-3]+");";
   get_insert_stmt_full += str(get_insert_stmt+get_insert_stmt_val)+"\n";
  sqldump = sqldump+get_insert_stmt_full+"\n-- --------------------------------------------------------\n\n";
 CloseHockeyDatabase(sqldatacon);
 return sqldump;

def MakeHockeySQLFileFromXML(xmlfile, sqlfile=None, returnsql=False):
 if(not os.path.exists(xmlfile) and not os.path.isfile(xmlfile)):
  return False;
 if(sqlfile is None):
  file_wo_extension, file_extension = os.path.splitext(xmlfile);
  sqlfile = file_wo_extension+".sql";
 sqlfp = open(sqlfile, "w+");
 sqlstring = MakeHockeySQLFromXML(xmlfile);
 sqlfp.write(sqlstring);
 sqlfp.close();
 if(returnsql is True):
  return sqlstring;
 if(returnsql is False):
  return True;
 return True;
