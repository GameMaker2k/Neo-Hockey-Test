#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2015-2020 Game Maker 2k - https://github.com/GameMaker2k
    Copyright 2015-2020 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: hockeydatabase.py - Last Update: 2/9/2020 Ver. 0.2.0 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals;
import sqlite3, sys, os, re;
import logging as log;

try:
 from xml.sax.saxutils import xml_escape;
except ImportError:
 if(sys.version[0]=="2"):
  from cgi import escape as html_escape;
 if(sys.version[0]>="3"):
  from html import escape as html_escape;

def EscapeXMLString(inxml, quote=True):
 if(quote is True):
  xml_escape_dict = { "\"": "&quot;", "'": "&apos;" };
 else:
  xml_escape_dict = {};
 outxml = False;
 try:
  outxml = xml_escape(inxml, xml_escape_dict);
 except NameError:
  outxml = html_escape(inxml, quote);
 return outxml;

def VerbosePrintOut(dbgtxt, outtype="log", dbgenable=True):
 if(outtype=="print" and dbgenable):
  print(dbgtxt);
  return True;
 if(outtype=="log" and dbgenable):
  log.info(dbgtxt);
  return True;
 if(not dbgenable):
  return True;
 return False;

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

def CreateHockeyArray(databasename="./hockeydatabase.sdb"):
 hockeyarray = { 'database': databasename, 'leaguelist': [] };
 return hockeyarray;

def CreateHockeyDatabase(sdbfile):
 if(os.path.exists(sdbfile) or os.path.isfile(sdbfile)):
  return False;
 sqlcon = sqlite3.connect(sdbfile, isolation_level=None);
 sqlcur = sqlcon.cursor();
 sqlcur.execute("PRAGMA encoding = \"UTF-8\";");
 sqlcur.execute("PRAGMA auto_vacuum = 1;");
 sqlcur.execute("PRAGMA foreign_keys = 0;");
 sqlcur.close();
 sqlcon.close();
 return True;

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
 getlastninegames = sqldatacon[0].execute("SELECT NumberPeriods, TeamWin, TeamLost, TieGame FROM "+leaguename+"Games WHERE (HomeTeam=\""+str(teamname)+"\" OR AwayTeam=\""+str(teamname)+"\") ORDER BY id DESC LIMIT "+str(gamelimit)).fetchall();
 nmax = len(getlastninegames);
 nmin = 0;
 while(nmin<nmax):
  if(teamname==str(getlastninegames[nmin][1]) and int(getlastninegames[nmin][3])==0):
   wins = wins + 1;
  if(teamname==str(getlastninegames[nmin][2]) or int(getlastninegames[nmin][3])==1):
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
 getlastninegames = sqldatacon[0].execute("SELECT NumberPeriods, TeamWin, TeamLost, TieGame, IsPlayOffGame FROM "+leaguename+"Games WHERE (HomeTeam=\""+str(teamname)+"\" OR AwayTeam=\""+str(teamname)+"\") ORDER BY id DESC LIMIT "+str(gamelimit)).fetchall();
 nmax = len(getlastninegames);
 nmin = 0;
 while(nmin<nmax):
  if(teamname==str(getlastninegames[nmin][1]) and int(getlastninegames[nmin][3])==0):
   wins = wins + 1;
  if(teamname==str(getlastninegames[nmin][2]) or int(getlastninegames[nmin][3])==1):
   if(int(getlastninegames[nmin][0])==3):
    losses = losses + 1;
   if(int(getlastninegames[nmin][0])==4 and int(getlastninegames[nmin][4])==0):
    otlosses = otlosses + 1;
   if(int(getlastninegames[nmin][0])>4 and int(getlastninegames[nmin][4])==0):
    solosses = solosses + 1;
   if(int(getlastninegames[nmin][0])>3 and (int(getlastninegames[nmin][4])==1 or int(getlastninegames[nmin][4])==2)):
    otlosses = otlosses + 1;
  nmin = nmin + 1;
 return str(wins)+":"+str(losses)+":"+str(otlosses)+":"+str(solosses);

def GetLastTenGamesWithShootout(sqldatacon, leaguename, teamname):
 return GetLastGamesWithShootout(sqldatacon, leaguename, teamname, 10);

def GetLastGamesWithoutShootout(sqldatacon, leaguename, teamname, gamelimit=10):
 wins = 0;
 losses = 0;
 otlosses = 0;
 getlastninegames = sqldatacon[0].execute("SELECT NumberPeriods, TeamWin, TeamLost, TieGame FROM "+leaguename+"Games WHERE (HomeTeam=\""+str(teamname)+"\" OR AwayTeam=\""+str(teamname)+"\") ORDER BY id DESC LIMIT "+str(gamelimit)).fetchall();
 nmax = len(getlastninegames);
 nmin = 0;
 while(nmin<nmax):
  if(teamname==str(getlastninegames[nmin][1]) and int(getlastninegames[nmin][3])==0):
   wins = wins + 1;
  if(teamname==str(getlastninegames[nmin][2]) or int(getlastninegames[nmin][3])==1):
   if(int(getlastninegames[nmin][0])==3):
    losses = losses + 1;
   if(int(getlastninegames[nmin][0])>3):
    otlosses = otlosses + 1;
  nmin = nmin + 1;
 return str(wins)+":"+str(losses)+":"+str(otlosses)+":0";

def GetLastTenGamesWithoutShootout(sqldatacon, leaguename, teamname):
 return GetLastGamesWithoutShootout(sqldatacon, leaguename, teamname, 10);

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

def GetFullTeamName(teamname, teamnameprefix="", teamnamesuffix=""):
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
 return fullteamname;

def GetNum2Arena(sqldatacon, leaguename, ArenaNum, ReturnVar):
 return str(sqldatacon[0].execute("SELECT "+ReturnVar+" FROM "+leaguename+"Arenas WHERE id="+str(ArenaNum)).fetchone()[0]);

def GetArena2Num(sqldatacon, leaguename, ArenaName):
 return int(sqldatacon[0].execute("SELECT id FROM "+leaguename+"Arenas WHERE FullArenaName=\""+str(ArenaName)+"\"").fetchone()[0]);

def GetFullArenaName(arenaname, cityname):
 return str(arenaname)+", "+str(cityname);

def GetAreaInfoFromUSCA(areaname):
 areaname = areaname.replace(".", "");
 areaname = areaname.upper();
 areacodes = { 'AL': { 'AreaName': "AL", 'FullAreaName': "Alabama", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'AK': { 'AreaName': "AK", 'FullAreaName': "Alaska", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'AZ': { 'AreaName': "AZ", 'FullAreaName': "Arizona", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'AR': { 'AreaName': "AR", 'FullAreaName': "Arkansas", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'CA': { 'AreaName': "CA", 'FullAreaName': "California", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'CO': { 'AreaName': "CO", 'FullAreaName': "Colorado", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'CT': { 'AreaName': "CT", 'FullAreaName': "Connecticut", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'DC': { 'AreaName': "DC", 'FullAreaName': "District of Columbia", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'DE': { 'AreaName': "DE", 'FullAreaName': "Delaware", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'FL': { 'AreaName': "FL", 'FullAreaName': "Florida", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'GA': { 'AreaName': "GA", 'FullAreaName': "Georgia", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'HI': { 'AreaName': "HI", 'FullAreaName': "Hawaii", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'ID': { 'AreaName': "ID", 'FullAreaName': "Idaho", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'IL': { 'AreaName': "IL", 'FullAreaName': "Illinois", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'IN': { 'AreaName': "IN", 'FullAreaName': "Indiana", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'IA': { 'AreaName': "IA", 'FullAreaName': "Iowa", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'KS': { 'AreaName': "KS", 'FullAreaName': "Kansas", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'KY': { 'AreaName': "KY", 'FullAreaName': "Kentucky", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'LA': { 'AreaName': "LA", 'FullAreaName': "Louisiana", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'ME': { 'AreaName': "ME", 'FullAreaName': "Maine", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'MD': { 'AreaName': "MD", 'FullAreaName': "Maryland", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'MA': { 'AreaName': "MA", 'FullAreaName': "Massachusetts", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'MI': { 'AreaName': "MI", 'FullAreaName': "Michigan", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'MN': { 'AreaName': "MN", 'FullAreaName': "Minnesota", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'MS': { 'AreaName': "MS", 'FullAreaName': "Mississippi", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'MO': { 'AreaName': "MO", 'FullAreaName': "Missouri", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'MT': { 'AreaName': "MT", 'FullAreaName': "Montana", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'NE': { 'AreaName': "NE", 'FullAreaName': "Nebraska", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'NV': { 'AreaName': "NV", 'FullAreaName': "Nevada", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'NH': { 'AreaName': "NH", 'FullAreaName': "New Hampshire", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'NJ': { 'AreaName': "NJ", 'FullAreaName': "New Jersey", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'NM': { 'AreaName': "NM", 'FullAreaName': "New Mexico", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'NY': { 'AreaName': "NY", 'FullAreaName': "New York", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'NC': { 'AreaName': "NC", 'FullAreaName': "North Carolina", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'ND': { 'AreaName': "ND", 'FullAreaName': "North Dakota", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'OH': { 'AreaName': "OH", 'FullAreaName': "Ohio", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'OK': { 'AreaName': "OK", 'FullAreaName': "Oklahoma", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'OR': { 'AreaName': "OR", 'FullAreaName': "Oregon", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'PA': { 'AreaName': "PA", 'FullAreaName': "Pennsylvania", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'RI': { 'AreaName': "RI", 'FullAreaName': "Rhode Island", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'SC': { 'AreaName': "SC", 'FullAreaName': "South Carolina", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'SD': { 'AreaName': "SD", 'FullAreaName': "South Dakota", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'TN': { 'AreaName': "TN", 'FullAreaName': "Tennessee", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'TX': { 'AreaName': "TX", 'FullAreaName': "Texas", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'UT': { 'AreaName': "UT", 'FullAreaName': "Utah", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'VT': { 'AreaName': "VT", 'FullAreaName': "Vermont", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'VA': { 'AreaName': "VA", 'FullAreaName': "Virginia", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'WA': { 'AreaName': "WA", 'FullAreaName': "Washington", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'WV': { 'AreaName': "WV", 'FullAreaName': "West Virginia", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'WI': { 'AreaName': "WI", 'FullAreaName': "Wisconsin", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'WY': { 'AreaName': "WY", 'FullAreaName': "Wyoming", 'CountryName': "USA", 'FullCountryName': "United States" }, 
               'AB': { 'AreaName': "AB", 'FullAreaName': "Alberta", 'CountryName': "CAN", 'FullCountryName': "Canada" }, 
               'BC': { 'AreaName': "BC", 'FullAreaName': "British Columbia", 'CountryName': "CAN", 'FullCountryName': "Canada" }, 
               'MB': { 'AreaName': "MB", 'FullAreaName': "Manitoba", 'CountryName': "CAN", 'FullCountryName': "Canada" }, 
               'NB': { 'AreaName': "NB", 'FullAreaName': "New Brunswick", 'CountryName': "CAN", 'FullCountryName': "Canada" }, 
               'NL': { 'AreaName': "NL", 'FullAreaName': "Newfoundland and Labrador", 'CountryName': "CAN", 'FullCountryName': "Canada" }, 
               'NS': { 'AreaName': "NS", 'FullAreaName': "Nova Scotia", 'CountryName': "CAN", 'FullCountryName': "Canada" }, 
               'NT': { 'AreaName': "NT", 'FullAreaName': "Northwest Territories", 'CountryName': "CAN", 'FullCountryName': "Canada" }, 
               'NU': { 'AreaName': "NU", 'FullAreaName': "Nunavut", 'CountryName': "CAN", 'FullCountryName': "Canada" }, 
               'ON': { 'AreaName': "ON", 'FullAreaName': "Ontario", 'CountryName': "CAN", 'FullCountryName': "Canada" }, 
               'PE': { 'AreaName': "PE", 'FullAreaName': "Prince Edward Island", 'CountryName': "CAN", 'FullCountryName': "Canada" }, 
               'QC': { 'AreaName': "QC", 'FullAreaName': "Quebec", 'CountryName': "CAN", 'FullCountryName': "Canada" }, 
               'SK': { 'AreaName': "SK", 'FullAreaName': "Saskatchewan", 'CountryName': "CAN", 'FullCountryName': "Canada" }, 
               'YT': { 'AreaName': "YT", 'FullAreaName': "Yukon", 'CountryName': "CAN", 'FullCountryName': "Canada" } };
 return areacodes.get(areaname, { areaname: { 'AreaName': areaname, 'FullAreaName': "Unknown", 'CountryName': "Unknown", 'FullCountryName': "Unknown" } });

def GetHockeyLeaguesInfo(leaguename):
 leaguename = leaguename.upper();
 leagueinfo = { 'NHL': { 'LeagueName': "NHL", 'FullLeagueName': "National Hockey League", 'CountryName': "USA", 'FullCountryName': "United States", 'StartDate': 20151007, 'PlayOffFMT': "Division=3,Conference=2", 'OrderType': "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC" }, 
                'AHL': { 'LeagueName': "AHL", 'FullLeagueName': "American Hockey League", 'CountryName': "USA", 'FullCountryName': "United States", 'StartDate': 20151009, 'PlayOffFMT': "Division=4", 'OrderType': "ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC" }, 
                'ECHL': { 'LeagueName': "ECHL", 'FullLeagueName': "ECHL", 'CountryName': "USA", 'FullCountryName': "United States", 'StartDate': 20151007, 'PlayOffFMT': "Division=1,Conference=5", 'OrderType': "ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC" }, 
                'FHL': { 'LeagueName': "FHL", 'FullLeagueName': "Federal Hockey League", 'CountryName': "USA", 'FullCountryName': "United States", 'StartDate': 20151106, 'PlayOffFMT': "League=4", 'OrderType': "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC" }, 
                'SPHL': { 'LeagueName': "SPHL", 'FullLeagueName': "Southern Professional Hockey League", 'CountryName': "USA", 'FullCountryName': "United States", 'StartDate': 20151023, 'PlayOffFMT': "League=8", 'OrderType': "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC" } };
 return leagueinfo.get(leaguename, { leaguename: { 'LeagueName': leaguename, 'FullLeagueName': "Unknown", 'CountryName': "Unknown", 'FullCountryName': "Unknown", 'StartDate': 0, 'PlayOffFMT': "Unknown", 'OrderType': "Unknown" } });

def AddHockeyLeagueToArray(hockeyarray, leaguename, leaguefullname, countryname, fullcountryname, date, playofffmt, ordertype, hasconferences="yes", hasdivisions="yes"):
 if "leaguelist" not in hockeyarray.keys():
  hockeyarray.update( { 'leaguelist': [] } );
 if "database" not in hockeyarray.keys():
  hockeyarray.update( { 'database': "./hockeydatabase.sdb" } );
 if leaguename not in hockeyarray.keys():
  hockeyarray.update( { leaguename: { 'leagueinfo': { 'name': str(leaguename), 'fullname': str(leaguefullname), 'country': str(countryname), 'fullcountry': str(fullcountryname), 'date': str(date), 'playofffmt': str(playofffmt), 'ordertype': str(ordertype), 'conferences': str(hasconferences), 'divisions': str(hasdivisions), 'conferencelist': [] }, 'quickinfo': {'conferenceinfo': {}, 'divisioninfo': {}, 'teaminfo': {} }, 'arenas': [ {} ], 'games': [ {} ] } } );
  hockeyarray['leaguelist'].append(str(leaguename));
 return hockeyarray;

def RemoveHockeyLeagueFromArray(hockeyarray, leaguename):
 if "leaguelist" not in hockeyarray.keys():
  hockeyarray.update( { 'leaguelist': [] } );
 if "database" not in hockeyarray.keys():
  hockeyarray.update( { 'database': "./hockeydatabase.sdb" } );
 if leaguename in hockeyarray.keys():
  hockeyarray.pop(leaguename, None);
  hockeyarray['leaguelist'].remove(leaguename);
 return hockeyarray;

def ReplaceHockeyLeagueFromArray(hockeyarray, oldleaguename, newleaguename, leaguefullname=None, countryname=None, fullcountryname=None, date=None, playofffmt=None, ordertype=None, hasconferences=None, hasdivisions=None):
 if "leaguelist" not in hockeyarray.keys():
  hockeyarray.update( { 'leaguelist': [] } );
 if "database" not in hockeyarray.keys():
  hockeyarray.update( { 'database': "./hockeydatabase.sdb" } );
 if oldleaguename in hockeyarray.keys() and newleaguename not in hockeyarray.keys():
  hockeyarray[newleaguename] = hockeyarray.pop(str(oldleaguename));
  hockeyarray[newleaguename]['leagueinfo']['name'] = str(newleaguename);
  if(leaguefullname is not None):
   hockeyarray[newleaguename]['leagueinfo']['fullname'] =  str(leaguefullname);
  if(countryname is not None):
   hockeyarray[newleaguename]['leagueinfo']['country'] = str(countryname);
  if(fullcountryname is not None):
   hockeyarray[newleaguename]['leagueinfo']['fullcountry'] = str(fullcountryname);
  if(date is not None):
   hockeyarray[newleaguename]['leagueinfo']['date'] = str(date);
  if(playofffmt is not None):
   hockeyarray[newleaguename]['leagueinfo']['playofffmt'] = str(playofffmt);
  if(ordertype is not None):
   hockeyarray[newleaguename]['leagueinfo']['ordertype'] = str(ordertype);
  if(hasconferences is not None):
   hockeyarray[newleaguename]['leagueinfo']['conferences'] = str(hasconferences);
  if(hasdivisions is not None):
   hockeyarray[newleaguename]['leagueinfo']['divisions'] = str(hasdivisions);
  if "conferencelist" not in hockeyarray[newleaguename].keys():
   hockeyarray[newleaguename].update( { 'conferencelist': [] } );
  hlin = hockeyarray['leaguelist'].index(oldleaguename);
  hockeyarray['leaguelist'][hlin] = newleaguename;
  for hlkey in hockeyarray['leaguelist']:
   for hckey in hockeyarray[hlkey]['conferencelist']:
    hockeyarray[newleaguename][hckey]['conferenceinfo']['league'] = str(newleaguename);
    for hdkey in hockeyarray[hlkey][hckey]['divisionlist']:
     hockeyarray[newleaguename][hckey][hdkey]['divisioninfo']['league'] = str(newleaguename);
     for htkey in hockeyarray[hlkey][hckey][hdkey]['teamlist']:
      hockeyarray[newleaguename][hckey][hdkey][htkey]['teaminfo']['league'] = str(newleaguename);
 return hockeyarray;

def MakeHockeyLeagueTable(sqldatacon, droptable=True):
 if(droptable is True):
  sqldatacon[0].execute("DROP TABLE IF EXISTS HockeyLeagues");
 sqldatacon[0].execute("CREATE TABLE HockeyLeagues (\n" + \
 "  id INTEGER PRIMARY KEY AUTOINCREMENT,\n" + \
 "  LeagueName TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueFullName TEXT NOT NULL DEFAULT '',\n" + \
 "  CountryName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullCountryName TEXT NOT NULL DEFAULT '',\n" + \
 "  Date INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PlayOffFMT TEXT NOT NULL DEFAULT '',\n" + \
 "  OrderType TEXT NOT NULL DEFAULT '',\n" + \
 "  NumberOfTeams INTEGER NOT NULL DEFAULT 0,\n" + \
 "  NumberOfConferences INTEGER NOT NULL DEFAULT 0,\n" + \
 "  NumberOfDivisions INTEGER NOT NULL DEFAULT ''\n" + \
 ");");
 return True;

def MakeHockeyLeague(sqldatacon, leaguename, leaguefullname, countryname, fullcountryname, date, playofffmt, ordertype):
 sqldatacon[0].execute("INSERT INTO HockeyLeagues (LeagueName, LeagueFullName, CountryName, FullCountryName, Date, PlayOffFMT, OrderType, NumberOfTeams, NumberOfConferences, NumberOfDivisions) VALUES \n" + \
 "(\""+str(leaguename)+"\", \""+str(leaguefullname)+"\", \""+str(countryname)+"\", \""+str(fullcountryname)+"\", \""+str(date)+"\", \""+str(playofffmt)+"\", \""+str(ordertype)+"\", 0, 0, 0)");
 return True;

def AddHockeyConferenceToArray(hockeyarray, leaguename, conference):
 if leaguename in hockeyarray.keys() and "conferencelist" not in hockeyarray[leaguename].keys():
  hockeyarray[leaguename].update( { 'conferencelist': [] } );
 if "database" not in hockeyarray.keys():
  hockeyarray.update( { 'database': "./hockeydatabase.sdb" } );
 if leaguename in hockeyarray.keys():
  if conference not in hockeyarray[leaguename].keys():
   hockeyarray[leaguename].update( { str(conference): { 'conferenceinfo': { 'name': str(conference), 'league': str(leaguename), 'divisionlist': [] } } } );
   hockeyarray[leaguename]['quickinfo']['conferenceinfo'].update( { str(conference): { 'name': str(conference), 'league': str(leaguename) } } );
   hockeyarray[leaguename]['conferencelist'].append(str(conference));
 return hockeyarray;

def RemoveHockeyConferenceFromArray(hockeyarray, leaguename, conference):
 if leaguename in hockeyarray.keys() and "conferencelist" not in hockeyarray[leaguename].keys():
  hockeyarray[leaguename].update( { 'conferencelist': [] } );
 if "database" not in hockeyarray.keys():
  hockeyarray.update( { 'database': "./hockeydatabase.sdb" } );
 if leaguename in hockeyarray.keys():
  if conference in hockeyarray[leaguename].keys():
   for hdkey in hockeyarray[leaguename][conference]['divisionlist']:
    hockeyarray[leaguename]['quickinfo']['divisioninfo'].pop(hdkey, None);
    for htkey in hockeyarray[leaguename][conference][hdkey]['teamlist']:
     fullteamname = GetFullTeamName(hockeyarray[leaguename][conference][hdkey][htkey]['teaminfo']['name'], hockeyarray[leaguename][conference][hdkey][htkey]['teaminfo']['prefix'], hockeyarray[leaguename][conference][hdkey][htkey]['teaminfo']['suffix']);
     newgamelist = [];
     for hgkey in hockeyarray[leaguename]['games']:
      if(hgkey['hometeam']!=fullteamname and hgkey['awayteam']!=fullteamname):
       newgamelist.append(hgkey);
     hockeyarray[leaguename]['games'] = newgamelist;
     hockeyarray[leaguename]['quickinfo']['teaminfo'].pop(htkey, None);
   hockeyarray[leaguename].pop(conference, None);
   hockeyarray[leaguename]['quickinfo']['conferenceinfo'].pop(conference, None);
   hockeyarray[leaguename]['conferencelist'].remove(conference);
 return hockeyarray;

def ReplaceHockeyConferencFromArray(hockeyarray, leaguename, oldconference, newconference):
 if leaguename in hockeyarray.keys() and "conferencelist" not in hockeyarray[leaguename].keys():
  hockeyarray[leaguename].update( { 'conferencelist': [] } );
 if "database" not in hockeyarray.keys():
  hockeyarray.update( { 'database': "./hockeydatabase.sdb" } );
 if oldconference in hockeyarray[leaguename].keys() and newconference not in hockeyarray[leaguename].keys():
  hockeyarray[leaguename][newconference] = hockeyarray[leaguename].pop(str(oldconference));
  hockeyarray[leaguename]['quickinfo']['conferenceinfo'][newconference] = hockeyarray[leaguename]['quickinfo']['conferenceinfo'].pop(str(oldconference));
  hockeyarray[leaguename][newconference]['conferenceinfo']['name'] = str(newconference);
  if "divisionlist" not in hockeyarray[leaguename][newconference].keys():
   hockeyarray[leaguename][newconference].update( { 'divisionlist': [] } );
  hcin = hockeyarray[leaguename]['conferencelist'].index(oldconference);
  hockeyarray[leaguename]['conferencelist'][hcin] = newconference;
  for hlkey in hockeyarray['leaguelist']:
   for hckey in hockeyarray[hlkey]['conferencelist']:
    for hdkey in hockeyarray[hlkey][hckey]['divisionlist']:
     hockeyarray[leaguename][newconference][hdkey]['divisioninfo']['conference'] = str(newconference);
     for htkey in hockeyarray[hlkey][hckey][hdkey]['teamlist']:
      hockeyarray[leaguename][newconference][hdkey][htkey]['teaminfo']['conference'] = str(newconference);
 return hockeyarray;

def MakeHockeyConferenceTable(sqldatacon, leaguename, droptable=True):
 if(droptable is True):
  sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Conferences");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Conferences (\n" + \
 "  id INTEGER PRIMARY KEY AUTOINCREMENT,\n" + \
 "  Conference TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueName TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueFullName TEXT NOT NULL DEFAULT '',\n" + \
 "  NumberOfTeams INTEGER NOT NULL DEFAULT 0,\n" + \
 "  NumberOfDivisions INTEGER NOT NULL DEFAULT ''\n" + \
 ");");
 return True;

def MakeHockeyConference(sqldatacon, leaguename, conference, hasconferences=True):
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Conferences (Conference, LeagueName, LeagueFullName, NumberOfTeams, NumberOfDivisions) VALUES \n" + \
 "(\""+str(conference)+"\", \""+leaguename+"\", \""+GetLeagueName(sqldatacon, leaguename)+"\", 0, 0)");
 if(hasconferences is True):
  UpdateLeagueData(sqldatacon, leaguename, "NumberOfConferences", 1, "+");
 return True;

def AddHockeyDivisionToArray(hockeyarray, leaguename, division, conference):
 if leaguename in hockeyarray.keys() and conference in hockeyarray[leaguename].keys() and "divisionlist" not in hockeyarray[leaguename][conference].keys():
  hockeyarray[leaguename][conference].update( { 'divisionlist': [] } );
 if "database" not in hockeyarray.keys():
  hockeyarray.update( { 'database': "./hockeydatabase.sdb" } );
 if leaguename in hockeyarray.keys():
  if conference in hockeyarray[leaguename].keys():
   if division not in hockeyarray[leaguename][conference].keys():
    hockeyarray[leaguename][conference].update( { str(division): { 'divisioninfo': { 'name': str(division), 'league': str(leaguename), 'conference': str(conference), 'teamlist': [] } } } );
    hockeyarray[leaguename]['quickinfo']['divisioninfo'].update( { str(division): { 'name': str(division), 'league': str(leaguename), 'conference': str(conference) } } );
    hockeyarray[leaguename][conference]['divisionlist'].append(str(division));
 return hockeyarray;

def RemoveHockeyDivisionFromArray(hockeyarray, leaguename, division, conference):
 if leaguename in hockeyarray.keys() and conference in hockeyarray[leaguename].keys() and "divisionlist" not in hockeyarray[leaguename][conference].keys():
  hockeyarray[leaguename][conference].update( { 'divisionlist': [] } );
 if "database" not in hockeyarray.keys():
  hockeyarray.update( { 'database': "./hockeydatabase.sdb" } );
 if leaguename in hockeyarray.keys():
  if conference in hockeyarray[leaguename].keys():
   if division in hockeyarray[leaguename][conference].keys():
    for htkey in hockeyarray[leaguename][conference][division]['teamlist']:
     fullteamname = GetFullTeamName(hockeyarray[leaguename][conference][division][htkey]['teaminfo']['name'], hockeyarray[leaguename][conference][division][htkey]['teaminfo']['prefix'], hockeyarray[leaguename][conference][division][htkey]['teaminfo']['suffix']);
     newgamelist = [];
     for hgkey in hockeyarray[leaguename]['games']:
      if(hgkey['hometeam']!=fullteamname and hgkey['awayteam']!=fullteamname):
       newgamelist.append(hgkey);
     hockeyarray[leaguename]['games'] = newgamelist;
     hockeyarray[leaguename]['quickinfo']['teaminfo'].pop(htkey, None);
    hockeyarray[leaguename][conference].pop(division, None);
    hockeyarray[leaguename]['quickinfo']['divisioninfo'].pop(division, None);
    hockeyarray[leaguename][conference]['divisionlist'].remove(division);
 return hockeyarray;

def ReplaceHockeyDivisionFromArray(hockeyarray, leaguename, olddivision, newdivision, conference):
 if leaguename in hockeyarray.keys() and conference in hockeyarray[leaguename].keys() and "divisionlist" not in hockeyarray[leaguename][conference].keys():
  hockeyarray[leaguename][conference].update( { 'divisionlist': [] } );
 if "database" not in hockeyarray.keys():
  hockeyarray.update( { 'database': "./hockeydatabase.sdb" } );
 if olddivision in hockeyarray[leaguename][conference].keys() and newdivision not in hockeyarray[leaguename][conference].keys():
  hockeyarray[leaguename][conference][newdivision] = hockeyarray[leaguename][conference].pop(str(olddivision));
  hockeyarray[leaguename]['quickinfo']['divisioninfo'][newdivision] = hockeyarray[leaguename]['quickinfo']['divisioninfo'].pop(str(olddivision));
  hockeyarray[leaguename][conference][newdivision]['divisioninfo']['name'] = str(newdivision);
  if "teamlist" not in hockeyarray[leaguename][conference][newdivision].keys():
   hockeyarray[leaguename][conference][newdivision].update( { 'teamlist': [] } );
  hdin = hockeyarray[leaguename][conference]['divisionlist'].index(olddivision);
  hockeyarray[leaguename][conference]['divisionlist'][hdin] = newdivision;
  for hdkey in hockeyarray[leaguename][conference][newdivision].keys():
   if(hdkey!="divisioninfo"):
    hockeyarray[leaguename][conference][newdivision][hdkey]['teaminfo']['division'] = str(newdivision);
 return hockeyarray;

def MakeHockeyDivisionTable(sqldatacon, leaguename, droptable=True):
 if(droptable is True):
  sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Divisions");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Divisions (\n" + \
 "  id INTEGER PRIMARY KEY AUTOINCREMENT,\n" + \
 "  Division TEXT NOT NULL DEFAULT '',\n" + \
 "  Conference TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueName TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueFullName TEXT NOT NULL DEFAULT '',\n" + \
 "  NumberOfTeams INTEGER NOT NULL DEFAULT ''\n" + \
 ");");
 return True;

def MakeHockeyDivision(sqldatacon, leaguename, division, conference, hasconferences=True, hasdivisions=True):
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Divisions (Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES \n" + \
 "(\""+str(division)+"\", \""+str(conference)+"\", \""+leaguename+"\", \""+GetLeagueName(sqldatacon, leaguename)+"\", 0)");
 if(hasconferences is True):
  UpdateConferenceData(sqldatacon, leaguename, conference, "NumberOfDivisions", 1, "+");
 if(hasdivisions is True):
  UpdateLeagueData(sqldatacon, leaguename, "NumberOfDivisions", 1, "+");
 return True;

def AddHockeyTeamToArray(hockeyarray, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, teamname, conference, division, arenaname, teamnameprefix="", teamnamesuffix=""):
 if leaguename in hockeyarray.keys() and conference in hockeyarray[leaguename].keys() and division in hockeyarray[leaguename][conference].keys() and "teamlist" not in hockeyarray[leaguename][conference][division].keys():
  hockeyarray[leaguename][conference][division].update( { 'teamlist': [] } );
 if "database" not in hockeyarray.keys():
  hockeyarray.update( { 'database': "./hockeydatabase.sdb" } );
 if leaguename in hockeyarray.keys():
  if conference in hockeyarray[leaguename].keys():
   if division in hockeyarray[leaguename][conference].keys():
    if teamname not in hockeyarray[leaguename][conference][division].keys():
     fullteamname = GetFullTeamName(str(teamname), str(teamnameprefix), str(teamnamesuffix));
     hockeyarray[leaguename][conference][division].update( { str(teamname): { 'teaminfo': { 'city': str(cityname), 'area': str(areaname), 'fullarea': str(fullareaname), 'country': str(countryname), 'fullcountry': str(fullcountryname), 'name': str(teamname), 'fullname': fullteamname, 'arena': str(arenaname), 'prefix': str(teamnameprefix), 'suffix': str(teamnamesuffix), 'league': str(leaguename), 'conference': str(conference), 'division': str(division) } } } );
     hockeyarray[leaguename]['quickinfo']['teaminfo'].update( { str(teamname): { 'name': str(teamname), 'fullname': fullteamname, 'league': str(leaguename), 'conference': str(conference), 'division': str(division) } } );
     hockeyarray[leaguename][conference][division]['teamlist'].append(str(teamname));
 return hockeyarray;

def RemoveHockeyTeamFromArray(hockeyarray, leaguename, teamname, conference, division):
 if leaguename in hockeyarray.keys() and conference in hockeyarray[leaguename].keys() and division in hockeyarray[leaguename][conference].keys() and "teamlist" not in hockeyarray[leaguename][conference][division].keys():
  hockeyarray[leaguename][conference][division].update( { 'teamlist': [] } );
 if "database" not in hockeyarray.keys():
  hockeyarray.update( { 'database': "./hockeydatabase.sdb" } );
 if leaguename in hockeyarray.keys():
  if conference in hockeyarray[leaguename].keys():
   if division in hockeyarray[leaguename][conference].keys():
    if teamname in hockeyarray[leaguename][conference][division].keys():
     fullteamname = GetFullTeamName(hockeyarray[leaguename][conference][division][teamname]['teaminfo']['name'], hockeyarray[leaguename][conference][division][teamname]['teaminfo']['prefix'], hockeyarray[leaguename][conference][division][teamname]['teaminfo']['suffix']);
     newgamelist = [];
     for hgkey in hockeyarray[leaguename]['games']:
      if(hgkey['hometeam']!=fullteamname and hgkey['awayteam']!=fullteamname):
       newgamelist.append(hgkey);
     hockeyarray[leaguename]['games'] = newgamelist;
     hockeyarray[leaguename][conference][division].pop(teamname, None);
     hockeyarray[leaguename]['quickinfo']['teaminfo'].pop(teamname, None);
     hockeyarray[leaguename][conference][division]['teamlist'].remove(teamname);
 return hockeyarray;

def ReplaceHockeyTeamFromArray(hockeyarray, leaguename, oldteamname, newteamname, conference, division, cityname=None, areaname=None, countryname=None, fullcountryname=None, fullareaname=None, arenaname=None, teamnameprefix=None, teamnamesuffix=None):
 if leaguename in hockeyarray.keys() and conference in hockeyarray[leaguename].keys() and division in hockeyarray[leaguename][conference].keys() and "teamlist" not in hockeyarray[leaguename][conference][division].keys():
  hockeyarray[leaguename][conference][division].update( { 'teamlist': [] } );
 if "database" not in hockeyarray.keys():
  hockeyarray.update( { 'database': "./hockeydatabase.sdb" } );
 if oldteamname in hockeyarray[leaguename][conference][division].keys() and newteamname not in hockeyarray[leaguename][conference][division].keys():
  oldfullteamname = GetFullTeamName(hockeyarray[leaguename][conference][division][oldteamname]['teaminfo']['name'], hockeyarray[leaguename][conference][division][oldteamname]['teaminfo']['prefix'], hockeyarray[leaguename][conference][division][oldteamname]['teaminfo']['suffix']);
  hockeyarray[leaguename][conference][division][newteamname] = hockeyarray[leaguename][conference][division].pop(str(oldteamname));
  hockeyarray[leaguename]['quickinfo']['teaminfo'][newteamname] = hockeyarray[leaguename]['quickinfo']['teaminfo'].pop(str(oldteamname));
  hockeyarray[leaguename][conference][division][newteamname]['teaminfo']['name'] = str(newteamname);
  if(cityname is not None):
   hockeyarray[leaguename][conference][division][newteamname]['teaminfo']['city'] = str(cityname);
  if(areaname is not None):
   hockeyarray[leaguename][conference][division][newteamname]['teaminfo']['area'] = str(areaname);
  if(countryname is not None):
   hockeyarray[leaguename][conference][division][newteamname]['teaminfo']['country'] = str(countryname);
  if(fullcountryname is not None):
   hockeyarray[leaguename][conference][division][newteamname]['teaminfo']['fullcountry'] = str(fullcountryname);
  if(fullareaname is not None):
   hockeyarray[leaguename][conference][division][newteamname]['teaminfo']['fullarea'] = str(fullareaname);
  if(arenaname is not None):
   hockeyarray[leaguename][conference][division][newteamname]['teaminfo']['arena'] = str(arenaname);
  if(teamnameprefix is not None):
   hockeyarray[leaguename][conference][division][newteamname]['teaminfo']['prefix'] = str(teamnameprefix);
  if(teamnamesuffix is not None):
   hockeyarray[leaguename][conference][division][newteamname]['teaminfo']['suffix'] = str(teamnamesuffix);
  htin = hockeyarray[leaguename][conference][division]['teamlist'].index(str(oldteamname));
  hockeyarray[leaguename][conference][division]['teamlist'][htin] = str(newteamname);
  newfullteamname = GetFullTeamName(hockeyarray[leaguename][conference][division][newteamname]['teaminfo']['name'], hockeyarray[leaguename][conference][division][newteamname]['teaminfo']['prefix'], hockeyarray[leaguename][conference][division][newteamname]['teaminfo']['suffix']);
  for hgkey in hockeyarray[leaguename]['games']:
   if(hgkey['hometeam']==oldfullteamname):
    hgkey['hometeam'] = newfullteamname;
   if(hgkey['awayteam']==oldfullteamname):
    hgkey['hometeam'] = newfullteamname;
 return hockeyarray;

def MakeHockeyTeamTable(sqldatacon, leaguename, droptable=True):
 if(droptable is True):
  sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Arenas");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Arenas (\n" + \
 "  id INTEGER PRIMARY KEY AUTOINCREMENT,\n" + \
 "  TeamID INTEGER NOT NULL DEFAULT 0,\n" + \
 "  TeamName TEXT NOT NULL DEFAULT '',\n" + \
 "  TeamFullName TEXT NOT NULL DEFAULT '',\n" + \
 "  CityName TEXT NOT NULL DEFAULT '',\n" + \
 "  AreaName TEXT NOT NULL DEFAULT '',\n" + \
 "  CountryName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullCountryName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullCityName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullAreaName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullCityNameAlt TEXT NOT NULL DEFAULT '',\n" + \
 "  ArenaName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullArenaName TEXT NOT NULL DEFAULT '',\n" + \
 "  GamesPlayed INTEGER NOT NULL DEFAULT ''\n" + \
 ");");
 if(droptable is True):
  sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Teams");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Teams (\n" + \
 "  id INTEGER PRIMARY KEY AUTOINCREMENT,\n" + \
 "  Date INTEGER NOT NULL DEFAULT 0,\n" + \
 "  FullName TEXT NOT NULL DEFAULT '',\n" + \
 "  CityName TEXT NOT NULL DEFAULT '',\n" + \
 "  TeamPrefix TEXT NOT NULL DEFAULT '',\n" + \
 "  TeamSuffix TEXT NOT NULL DEFAULT '',\n" + \
 "  AreaName TEXT NOT NULL DEFAULT '',\n" + \
 "  CountryName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullCountryName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullCityName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullAreaName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullCityNameAlt TEXT NOT NULL DEFAULT '',\n" + \
 "  TeamName TEXT NOT NULL DEFAULT '',\n" + \
 "  Conference TEXT NOT NULL DEFAULT '',\n" + \
 "  Division TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueName TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueFullName TEXT NOT NULL DEFAULT '',\n" + \
 "  ArenaName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullArenaName TEXT NOT NULL DEFAULT '',\n" + \
 "  GamesPlayed INTEGER NOT NULL DEFAULT 0,\n" + \
 "  GamesPlayedHome INTEGER NOT NULL DEFAULT 0,\n" + \
 "  GamesPlayedAway INTEGER NOT NULL DEFAULT 0,\n" + \
 "  Ties INTEGER NOT NULL DEFAULT 0,\n" + \
 "  Wins INTEGER NOT NULL DEFAULT 0,\n" + \
 "  OTWins INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SOWins INTEGER NOT NULL DEFAULT 0,\n" + \
 "  OTSOWins INTEGER NOT NULL DEFAULT 0,\n" + \
 "  TWins INTEGER NOT NULL DEFAULT 0,\n" + \
 "  Losses INTEGER NOT NULL DEFAULT 0,\n" + \
 "  OTLosses INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SOLosses INTEGER NOT NULL DEFAULT 0,\n" + \
 "  OTSOLosses INTEGER NOT NULL DEFAULT 0,\n" + \
 "  TLosses INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ROW INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ROT INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ShutoutWins INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ShutoutLosses INTEGER NOT NULL DEFAULT 0,\n" + \
 "  HomeRecord TEXT NOT NULL DEFAULT '0:0:0:0',\n" + \
 "  AwayRecord TEXT NOT NULL DEFAULT '0:0:0:0',\n" + \
 "  Shootouts TEXT NOT NULL DEFAULT '0:0',\n" + \
 "  GoalsFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  GoalsAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  GoalsDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SOGFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SOGAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SOGDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ShotsBlockedFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ShotsBlockedAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ShotsBlockedDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PPGFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PPGAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PPGDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SHGFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SHGAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SHGDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PenaltiesFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PenaltiesAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PenaltiesDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PIMFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PIMAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PIMDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  HITSFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  HITSAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  HITSDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  TakeAways INTEGER NOT NULL DEFAULT 0,\n" + \
 "  GiveAways INTEGER NOT NULL DEFAULT 0,\n" + \
 "  TAGADifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  FaceoffWins INTEGER NOT NULL DEFAULT 0,\n" + \
 "  FaceoffLosses INTEGER NOT NULL DEFAULT 0,\n" + \
 "  FaceoffDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  Points INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PCT REAL NOT NULL DEFAULT 0,\n" + \
 "  LastTen TEXT NOT NULL DEFAULT '0:0:0:0',\n" + \
 "  Streak TEXT NOT NULL DEFAULT 'None'\n" + \
 ");");
 if(droptable is True):
  sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Stats");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Stats (\n" + \
 "  id INTEGER PRIMARY KEY AUTOINCREMENT,\n" + \
 "  TeamID INTEGER NOT NULL DEFAULT 0,\n" + \
 "  Date INTEGER NOT NULL DEFAULT 0,\n" + \
 "  FullName TEXT NOT NULL DEFAULT '',\n" + \
 "  CityName TEXT NOT NULL DEFAULT '',\n" + \
 "  TeamPrefix TEXT NOT NULL DEFAULT '',\n" + \
 "  TeamSuffix TEXT NOT NULL DEFAULT '',\n" + \
 "  AreaName TEXT NOT NULL DEFAULT '',\n" + \
 "  CountryName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullCountryName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullCityName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullAreaName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullCityNameAlt TEXT NOT NULL DEFAULT '',\n" + \
 "  TeamName TEXT NOT NULL DEFAULT '',\n" + \
 "  Conference TEXT NOT NULL DEFAULT '',\n" + \
 "  Division TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueName TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueFullName TEXT NOT NULL DEFAULT '',\n" + \
 "  ArenaName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullArenaName TEXT NOT NULL DEFAULT '',\n" + \
 "  GamesPlayed INTEGER NOT NULL DEFAULT 0,\n" + \
 "  GamesPlayedHome INTEGER NOT NULL DEFAULT 0,\n" + \
 "  GamesPlayedAway INTEGER NOT NULL DEFAULT 0,\n" + \
 "  Ties INTEGER NOT NULL DEFAULT 0,\n" + \
 "  Wins INTEGER NOT NULL DEFAULT 0,\n" + \
 "  OTWins INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SOWins INTEGER NOT NULL DEFAULT 0,\n" + \
 "  OTSOWins INTEGER NOT NULL DEFAULT 0,\n" + \
 "  TWins INTEGER NOT NULL DEFAULT 0,\n" + \
 "  Losses INTEGER NOT NULL DEFAULT 0,\n" + \
 "  OTLosses INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SOLosses INTEGER NOT NULL DEFAULT 0,\n" + \
 "  OTSOLosses INTEGER NOT NULL DEFAULT 0,\n" + \
 "  TLosses INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ROW INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ROT INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ShutoutWins INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ShutoutLosses INTEGER NOT NULL DEFAULT 0,\n" + \
 "  HomeRecord TEXT NOT NULL DEFAULT '0:0:0:0',\n" + \
 "  AwayRecord TEXT NOT NULL DEFAULT '0:0:0:0',\n" + \
 "  Shootouts TEXT NOT NULL DEFAULT '0:0',\n" + \
 "  GoalsFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  GoalsAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  GoalsDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SOGFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SOGAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SOGDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ShotsBlockedFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ShotsBlockedAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ShotsBlockedDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PPGFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PPGAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PPGDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SHGFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SHGAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SHGDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PenaltiesFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PenaltiesAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PenaltiesDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PIMFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PIMAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PIMDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  HITSFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  HITSAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  HITSDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  TakeAways INTEGER NOT NULL DEFAULT 0,\n" + \
 "  GiveAways INTEGER NOT NULL DEFAULT 0,\n" + \
 "  TAGADifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  FaceoffWins INTEGER NOT NULL DEFAULT 0,\n" + \
 "  FaceoffLosses INTEGER NOT NULL DEFAULT 0,\n" + \
 "  FaceoffDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  Points INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PCT REAL NOT NULL DEFAULT 0,\n" + \
 "  LastTen TEXT NOT NULL DEFAULT '0:0:0:0',\n" + \
 "  Streak TEXT NOT NULL DEFAULT 'None'\n" + \
 ");");
 if(droptable is True):
  sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"GameStats");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"GameStats (\n" + \
 "  id INTEGER PRIMARY KEY AUTOINCREMENT,\n" + \
 "  GameID INTEGER NOT NULL DEFAULT 0,\n" + \
 "  Date INTEGER NOT NULL DEFAULT 0,\n" + \
 "  TeamID INTEGER NOT NULL DEFAULT 0,\n" + \
 "  FullName TEXT NOT NULL DEFAULT '',\n" + \
 "  CityName TEXT NOT NULL DEFAULT '',\n" + \
 "  TeamPrefix TEXT NOT NULL DEFAULT '',\n" + \
 "  TeamSuffix TEXT NOT NULL DEFAULT '',\n" + \
 "  AreaName TEXT NOT NULL DEFAULT '',\n" + \
 "  CountryName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullCountryName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullCityName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullAreaName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullCityNameAlt TEXT NOT NULL DEFAULT '',\n" + \
 "  TeamName TEXT NOT NULL DEFAULT '',\n" + \
 "  Conference TEXT NOT NULL DEFAULT '',\n" + \
 "  Division TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueName TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueFullName TEXT NOT NULL DEFAULT '',\n" + \
 "  ArenaName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullArenaName TEXT NOT NULL DEFAULT '',\n" + \
 "  GoalsFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  GoalsAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  GoalsDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SOGFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SOGAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SOGDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ShotsBlockedFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ShotsBlockedAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ShotsBlockedDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PPGFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PPGAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PPGDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SHGFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SHGAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SHGDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PenaltiesFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PenaltiesAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PenaltiesDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PIMFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PIMAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PIMDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  HITSFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  HITSAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  HITSDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  TakeAways INTEGER NOT NULL DEFAULT 0,\n" + \
 "  GiveAways INTEGER NOT NULL DEFAULT 0,\n" + \
 "  TAGADifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  FaceoffWins INTEGER NOT NULL DEFAULT 0,\n" + \
 "  FaceoffLosses INTEGER NOT NULL DEFAULT 0,\n" + \
 "  FaceoffDifference INTEGER NOT NULL DEFAULT 0\n" + \
 ");");
 return True;

def MakeHockeyTeam(sqldatacon, leaguename, date, cityname, areaname, countryname, fullcountryname, fullareaname, teamname, conference, division, arenaname, teamnameprefix="", teamnamesuffix="", hasconferences=True, hasdivisions=True):
 date = str(date);
 chckyear = date[:4];
 chckmonth = date[4:6];
 chckday = date[6:8];
 fullteamname = GetFullTeamName(teamname, teamnameprefix="", teamnamesuffix="");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Teams (Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES \n" + \
 "(\""+str(chckyear+chckmonth+"00")+"\", \""+fullteamname+"\", \""+str(cityname)+"\", \""+str(teamnameprefix)+"\", \""+str(teamnamesuffix)+"\", \""+str(areaname)+"\", \""+str(countryname)+"\", \""+str(fullcountryname)+"\", \""+str(cityname+", "+areaname)+"\", \""+str(fullareaname)+"\", \""+str(cityname+", "+fullareaname)+"\", \""+str(teamname)+"\", \""+str(conference)+"\", \""+str(division)+"\", \""+leaguename+"\", \""+GetLeagueName(sqldatacon, leaguename)+"\", \""+str(arenaname)+"\", \""+str(arenaname+", "+cityname)+"\", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \"0:0:0:0\", \"0:0:0:0\", \"0:0\", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \"0:0:0:0\", \"None\")");
 TeamID = int(sqldatacon[0].lastrowid);
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Stats (TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak)\n" + \
 "SELECT id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE FullName=\""+fullteamname+"\";");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Arenas (TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES \n" + \
 "("+str(TeamID)+", \""+str(teamname)+"\", \""+fullteamname+"\", \""+str(cityname)+"\", \""+str(areaname)+"\", \""+str(countryname)+"\", \""+str(fullcountryname)+"\", \""+str(cityname+", "+areaname)+"\", \""+str(fullareaname)+"\", \""+str(cityname+", "+fullareaname)+"\", \""+str(arenaname)+"\", \""+str(arenaname+", "+cityname)+"\", 0)");
 if(hasconferences is True):
  UpdateConferenceData(sqldatacon, leaguename, conference, "NumberOfTeams", 1, "+");
 if(hasdivisions is True):
  UpdateDivisionData(sqldatacon, leaguename, division, "NumberOfTeams", 1, "+");
 UpdateLeagueData(sqldatacon, leaguename, "NumberOfTeams", 1, "+");
 return True;

def MakeHockeyPlayoffTeamTable(sqldatacon, leaguename, droptable=True):
 if(droptable is True):
  sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"PlayoffTeams");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"PlayoffTeams (\n" + \
 "  id INTEGER PRIMARY KEY AUTOINCREMENT,\n" + \
 "  TeamID INTEGER NOT NULL DEFAULT 0,\n" + \
 "  Date INTEGER NOT NULL DEFAULT 0,\n" + \
 "  FullName TEXT NOT NULL DEFAULT '',\n" + \
 "  CityName TEXT NOT NULL DEFAULT '',\n" + \
 "  TeamPrefix TEXT NOT NULL DEFAULT '',\n" + \
 "  TeamSuffix TEXT NOT NULL DEFAULT '',\n" + \
 "  AreaName TEXT NOT NULL DEFAULT '',\n" + \
 "  CountryName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullCountryName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullCityName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullAreaName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullCityNameAlt TEXT NOT NULL DEFAULT '',\n" + \
 "  TeamName TEXT NOT NULL DEFAULT '',\n" + \
 "  Conference TEXT NOT NULL DEFAULT '',\n" + \
 "  Division TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueName TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueFullName TEXT NOT NULL DEFAULT '',\n" + \
 "  ArenaName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullArenaName TEXT NOT NULL DEFAULT '',\n" + \
 "  GamesPlayed INTEGER NOT NULL DEFAULT 0,\n" + \
 "  GamesPlayedHome INTEGER NOT NULL DEFAULT 0,\n" + \
 "  GamesPlayedAway INTEGER NOT NULL DEFAULT 0,\n" + \
 "  Ties INTEGER NOT NULL DEFAULT 0,\n" + \
 "  Wins INTEGER NOT NULL DEFAULT 0,\n" + \
 "  OTWins INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SOWins INTEGER NOT NULL DEFAULT 0,\n" + \
 "  OTSOWins INTEGER NOT NULL DEFAULT 0,\n" + \
 "  TWins INTEGER NOT NULL DEFAULT 0,\n" + \
 "  Losses INTEGER NOT NULL DEFAULT 0,\n" + \
 "  OTLosses INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SOLosses INTEGER NOT NULL DEFAULT 0,\n" + \
 "  OTSOLosses INTEGER NOT NULL DEFAULT 0,\n" + \
 "  TLosses INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ROW INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ROT INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ShutoutWins INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ShutoutLosses INTEGER NOT NULL DEFAULT 0,\n" + \
 "  HomeRecord TEXT NOT NULL DEFAULT '0:0:0:0',\n" + \
 "  AwayRecord TEXT NOT NULL DEFAULT '0:0:0:0',\n" + \
 "  Shootouts TEXT NOT NULL DEFAULT '0:0',\n" + \
 "  GoalsFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  GoalsAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  GoalsDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SOGFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SOGAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SOGDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ShotsBlockedFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ShotsBlockedAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  ShotsBlockedDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PPGFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PPGAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PPGDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SHGFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SHGAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  SHGDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PenaltiesFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PenaltiesAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PenaltiesDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PIMFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PIMAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PIMDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  HITSFor INTEGER NOT NULL DEFAULT 0,\n" + \
 "  HITSAgainst INTEGER NOT NULL DEFAULT 0,\n" + \
 "  HITSDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  TakeAways INTEGER NOT NULL DEFAULT 0,\n" + \
 "  GiveAways INTEGER NOT NULL DEFAULT 0,\n" + \
 "  TAGADifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  FaceoffWins INTEGER NOT NULL DEFAULT 0,\n" + \
 "  FaceoffLosses INTEGER NOT NULL DEFAULT 0,\n" + \
 "  FaceoffDifference INTEGER NOT NULL DEFAULT 0,\n" + \
 "  Points INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PCT REAL NOT NULL DEFAULT 0,\n" + \
 "  LastTen TEXT NOT NULL DEFAULT '0:0:0:0',\n" + \
 "  Streak TEXT NOT NULL DEFAULT 'None'\n" + \
 ");");
 return True;

def MakeHockeyPlayoffTeam(sqldatacon, leaguename, playofffmt="Division=3,Conference=2"):
 playoffspl = playofffmt.split(',');
 playoffcnt = 0;
 while(playoffcnt<len(playoffspl)):
  subplayoffspl = playoffspl[playoffcnt].split('=');
  subsubplayoffspl = subplayoffspl[0].split(":")
  if(subsubplayoffspl[0]=="League"):
   sqldatacon[0].execute("INSERT INTO "+leaguename+"PlayoffTeams (TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak)\n" + \
   "SELECT id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE NOT EXISTS(SELECT TeamID FROM "+leaguename+"PlayoffTeams WHERE "+leaguename+"PlayoffTeams.TeamID = "+leaguename+"Teams.id) ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC LIMIT "+subplayoffspl[1]+";");
  if(subsubplayoffspl[0]=="Conference"):
   conferencecur = sqldatacon[1].cursor();
   if(len(subsubplayoffspl)==1):
    getconference = conferencecur.execute("SELECT Conference FROM "+leaguename+"Conferences WHERE LeagueName=\""+leaguename+"\"");
   if(len(subsubplayoffspl)>1):
    getconference = conferencecur.execute("SELECT Conference FROM "+leaguename+"Conferences WHERE LeagueName=\""+leaguename+"\" AND Conference=\""+subsubplayoffspl[1]+"\"");
   for conferenceinfo in getconference:
    sqldatacon[0].execute("INSERT INTO "+leaguename+"PlayoffTeams (TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak)\n" + \
    "SELECT id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE Conference=\""+conferenceinfo[0]+"\" AND NOT EXISTS(SELECT TeamID FROM "+leaguename+"PlayoffTeams WHERE "+leaguename+"PlayoffTeams.TeamID = "+leaguename+"Teams.id) ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC LIMIT "+subplayoffspl[1]+";");
   conferencecur.close();
  if(subsubplayoffspl[0]=="Division"):
   divisioncur = sqldatacon[1].cursor();
   if(len(subsubplayoffspl)==1):
    getdivision = divisioncur.execute("SELECT Division FROM "+leaguename+"Divisions WHERE LeagueName=\""+leaguename+"\"");
   if(len(subsubplayoffspl)>1):
    getdivision = divisioncur.execute("SELECT Division FROM "+leaguename+"Divisions WHERE LeagueName=\""+leaguename+"\" AND Division=\""+subsubplayoffspl[1]+"\"");
   for divisioninfo in getdivision:
    sqldatacon[0].execute("INSERT INTO "+leaguename+"PlayoffTeams (TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak)\n" + \
    "SELECT id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE Division=\""+divisioninfo[0]+"\" AND NOT EXISTS(SELECT TeamID FROM "+leaguename+"PlayoffTeams WHERE "+leaguename+"PlayoffTeams.TeamID = "+leaguename+"Teams.id) ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC LIMIT "+subplayoffspl[1]+";");
   divisioncur.close();
  playoffcnt = playoffcnt + 1;
 return True;

def AddHockeyArenaToArray(hockeyarray, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, arenaname):
 if leaguename in hockeyarray.keys():
  if "arenas" not in hockeyarray[leaguename].keys():
   hockeyarray[leaguename].update( { 'arenas': [ {} ] } );
  hockeyarray[leaguename]['arenas'].append( { 'city': str(cityname), 'area': str(areaname), 'fullarea': str(fullareaname), 'country': str(countryname), 'fullcountry': str(fullcountryname), 'name': str(arenaname) } );
 return hockeyarray;

def MakeHockeyArena(sqldatacon, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, arenaname):
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Arenas (TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES \n" + \
 "(0, \"\", \"\", \""+str(cityname)+"\", \""+str(areaname)+"\", \""+str(countryname)+"\", \""+str(fullcountryname)+"\", \""+str(cityname+", "+areaname)+"\", \""+str(fullareaname)+"\", \""+str(cityname+", "+fullareaname)+"\", \""+str(arenaname)+"\", \""+str(arenaname+", "+cityname)+"\", 0)");
 return True;

def AddHockeyGameToArray(hockeyarray, leaguename, date, hometeam, awayteam, periodsscore, shotsongoal, ppgoals, shgoals, periodpens, periodpims, periodhits, takeaways, faceoffwins, atarena, isplayoffgame):
 if leaguename in hockeyarray.keys():
  if "games" not in hockeyarray[leaguename].keys():
   hockeyarray[leaguename].update( { 'games': [ {} ] } );
 hockeyarray[leaguename]['games'].append( { 'date': str(date), 'hometeam': str(hometeam), 'awayteam': str(awayteam), 'goals': str(periodsscore), 'sogs': str(shotsongoal), 'ppgs': str(ppgoals), 'shgs': str(shgoals), 'penalties': str(periodpens), 'pims': str(periodpims), 'hits': str(periodhits), 'takeaways': str(takeaways), 'faceoffwins': str(faceoffwins), 'atarena': str(atarena), 'isplayoffgame': str(isplayoffgame) } );
 return hockeyarray;

def MakeHockeyGameTable(sqldatacon, leaguename, droptable=True):
 if(droptable is True):
  sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Games");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Games (\n" + \
 "  id INTEGER PRIMARY KEY AUTOINCREMENT,\n" + \
 "  Date INTEGER NOT NULL DEFAULT 0,\n" + \
 "  HomeTeam TEXT NOT NULL DEFAULT '',\n" + \
 "  AwayTeam TEXT NOT NULL DEFAULT '',\n" + \
 "  AtArena TEXT NOT NULL DEFAULT '',\n" + \
 "  TeamScorePeriods TEXT NOT NULL DEFAULT '',\n" + \
 "  TeamFullScore TEXT NOT NULL DEFAULT '',\n" + \
 "  ShotsOnGoal TEXT NOT NULL DEFAULT '',\n" + \
 "  FullShotsOnGoal TEXT NOT NULL DEFAULT '',\n" + \
 "  ShotsBlocked TEXT NOT NULL DEFAULT '',\n" + \
 "  FullShotsBlocked TEXT NOT NULL DEFAULT '',\n" + \
 "  PowerPlays TEXT NOT NULL DEFAULT '',\n" + \
 "  FullPowerPlays TEXT NOT NULL DEFAULT '',\n" + \
 "  ShortHanded TEXT NOT NULL DEFAULT '',\n" + \
 "  FullShortHanded TEXT NOT NULL DEFAULT '',\n" + \
 "  Penalties TEXT NOT NULL DEFAULT '',\n" + \
 "  FullPenalties TEXT NOT NULL DEFAULT '',\n" + \
 "  PenaltyMinutes TEXT NOT NULL DEFAULT '',\n" + \
 "  FullPenaltyMinutes TEXT NOT NULL DEFAULT '',\n" + \
 "  HitsPerPeriod TEXT NOT NULL DEFAULT '',\n" + \
 "  FullHitsPerPeriod TEXT NOT NULL DEFAULT '',\n" + \
 "  TakeAways TEXT NOT NULL DEFAULT '',\n" + \
 "  FullTakeAways TEXT NOT NULL DEFAULT '',\n" + \
 "  GiveAways TEXT NOT NULL DEFAULT '',\n" + \
 "  FullGiveAways TEXT NOT NULL DEFAULT '',\n" + \
 "  FaceoffWins TEXT NOT NULL DEFAULT '',\n" + \
 "  FullFaceoffWins TEXT NOT NULL DEFAULT '',\n" + \
 "  NumberPeriods INTEGER NOT NULL DEFAULT 0,\n" + \
 "  TeamWin TEXT NOT NULL DEFAULT '',\n" + \
 "  TeamLost TEXT NOT NULL DEFAULT '',\n" + \
 "  TieGame INTEGER NOT NULL DEFAULT 0,\n" + \
 "  IsPlayOffGame INTEGER NOT NULL DEFAULT ''\n" + \
 ");");
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
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Games (Date, HomeTeam, AwayTeam, AtArena, TeamScorePeriods, TeamFullScore, ShotsOnGoal, FullShotsOnGoal, ShotsBlocked, FullShotsBlocked, PowerPlays, FullPowerPlays, ShortHanded, FullShortHanded, Penalties, FullPenalties, PenaltyMinutes, FullPenaltyMinutes, HitsPerPeriod, FullHitsPerPeriod, TakeAways, FullTakeAways, GiveAways, FullGiveAways, FaceoffWins, FullFaceoffWins, NumberPeriods, TeamWin, TeamLost, TieGame, IsPlayOffGame) VALUES \n" + \
 "("+str(date)+", \""+str(hometeamname)+"\", \""+str(awayteamname)+"\", \""+str(atarenaname)+"\", \""+str(periodsscore)+"\", \""+str(totalscore)+"\", \""+str(shotsongoal)+"\", \""+str(totalsog)+"\", \""+str(sbstr)+"\", \""+str(tsbstr)+"\", \""+str(ppgoals)+"\", \""+str(totalppg)+"\", \""+str(shgoals)+"\", \""+str(totalshg)+"\", \""+str(periodpens)+"\", \""+str(totalpens)+"\", \""+str(periodpims)+"\", \""+str(totalpims)+"\", \""+str(periodhits)+"\", \""+str(totalhits)+"\", \""+str(takeaways)+"\", \""+str(totaltaws)+"\", \""+str(gaws_str)+"\", \""+str(totalgaws)+"\", \""+str(faceoffwins)+"\", \""+str(totalfows)+"\", "+str(numberofperiods)+", \""+str(winningteamname)+"\", \""+str(losingteamname)+"\", \""+str(tiegame)+"\", "+str(isplayoffgsql)+")");
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
 if(tiegame==0):
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
   if(GetWinningStreakSplit[0][0]=="Tie"):
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
   if(GetLosingStreakSplit[0][0]=="Tie"):
    if(numberofperiods==3):
     GetLosingStreakNext = "Lost 1";
    if(numberofperiods>3):
     GetLosingStreakNext = "OT 1";
  UpdateTeamDataString(sqldatacon, leaguename, losingteam, "Streak", GetLosingStreakNext);
 if(tiegame==1):
  GetWinningStreak = GetTeamData(sqldatacon, leaguename, hometeam, "Streak", "str");
  GetWinningStreakNext = "Tie 1";
  if(GetWinningStreak!="None"):
   GetWinningStreakSplit = re.findall("([a-zA-Z]+) ([0-9]+)", GetWinningStreak);
   if(GetWinningStreakSplit[0][0]=="Won"):
    GetWinningStreakNext = "Tie 1";
   if(GetWinningStreakSplit[0][0]=="Lost"):
    GetWinningStreakNext = "Tie 1";
   if(GetWinningStreakSplit[0][0]=="OT"):
    GetWinningStreakNext = "Tie 1";
   if(GetWinningStreakSplit[0][0]=="Tie"):
    GetWinningStreakNext = "Tie "+str(int(GetWinningStreakSplit[0][1]) + 1);
  UpdateTeamDataString(sqldatacon, leaguename, hometeam, "Streak", GetWinningStreakNext);
  GetLosingStreak = GetTeamData(sqldatacon, leaguename, awayteam, "Streak", "str");
  GetLosingStreakNext = "Tie 1";
  if(GetLosingStreak!="None"):
   GetLosingStreakSplit = re.findall("([a-zA-Z]+) ([0-9]+)", GetLosingStreak);
   if(GetLosingStreakSplit[0][0]=="Won"):
    GetLosingStreakNext = "Tie 1";
   if(GetLosingStreakSplit[0][0]=="Lost"):
    GetLosingStreakNext = "Tie 1";
   if(GetLosingStreakSplit[0][0]=="OS"):
    GetLosingStreakNext = "Tie 1";
   if(GetLosingStreakSplit[0][0]=="Tie"):
    GetLosingStreakNext = "Tie "+str(int(GetLosingStreakSplit[0][1]) + 1);
  UpdateTeamDataString(sqldatacon, leaguename, awayteam, "Streak", GetLosingStreakNext);
 if((isplayoffgame is False and numberofperiods<5 and tiegame==0) or (isplayoffgame is True and tiegame==0)):
  UpdateTeamData(sqldatacon, leaguename, winningteam, "ROW", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "ROT", 1, "+");
 if(numberofperiods==3 and tiegame==0):
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
 if(numberofperiods>3 and tiegame==0):
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
 if(isplayoffgame is False and numberofperiods>4 and tiegame==0):
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
 sqldatacon[0].execute("INSERT INTO "+leaguename+"GameStats (GameID, Date, TeamID, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference) VALUES \n" + \
 "("+str(GameID)+", "+str(date)+", "+str(hometeam)+", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "CityName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "TeamPrefix")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "TeamSuffix")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "AreaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "CountryName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullCountryName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullCityName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullAreaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullCityNameAlt")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "TeamName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "Conference")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "Division")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "LeagueName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "LeagueFullName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "ArenaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullArenaName")+"\", "+str(teamscores[0])+", "+str(teamscores[1])+", "+str(int(teamscores[0]) - int(teamscores[1]))+", "+str(teamssog[0])+", "+str(teamssog[1])+", "+str(int(teamssog[0]) - int(teamssog[1]))+", "+str(hometsb)+", "+str(awaytsb)+", "+str(int(hometsb) - int(awaytsb))+", "+str(homeppg)+", "+str(awayppg)+", "+str(int(homeppg) - int(awayppg))+", "+str(homeshg)+", "+str(awayshg)+", "+str(int(homeshg) - int(awayshg))+", "+str(homepens)+", "+str(awaypens)+", "+str(int(homepens) - int(awaypens))+", "+str(homepims)+", "+str(awaypims)+", "+str(int(homepims) - int(awaypims))+", "+str(homehits)+", "+str(awayhits)+", "+str(int(homehits) - int(awayhits))+", "+str(hometaws)+", "+str(awaytaws)+", "+str(int(hometaws) - int(awaytaws))+", "+str(homefows)+", "+str(awayfows)+", "+str(int(homefows) - int(awayfows))+")");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"GameStats (GameID, Date, TeamID, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference) VALUES \n" + \
 "("+str(GameID)+", "+str(date)+", "+str(awayteam)+", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "CityName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "TeamPrefix")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "TeamSuffix")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "AreaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "CountryName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullCountryName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullCityName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullAreaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullCityNameAlt")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "TeamName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "Conference")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "Division")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "LeagueName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "LeagueFullName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "ArenaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullArenaName")+"\", "+str(teamscores[1])+", "+str(teamscores[0])+", "+str(int(teamscores[1]) - int(teamscores[0]))+", "+str(teamssog[1])+", "+str(teamssog[0])+", "+str(int(teamssog[1]) - int(teamssog[0]))+", "+str(awaytsb)+", "+str(hometsb)+", "+str(int(awaytsb) - int(hometsb))+", "+str(awayppg)+", "+str(homeppg)+", "+str(int(awayppg) - int(homeppg))+", "+str(awayshg)+", "+str(homeshg)+", "+str(int(awayshg) - int(homeshg))+", "+str(awaypens)+", "+str(homepens)+", "+str(int(awaypens) - int(homepens))+", "+str(awaypims)+", "+str(homepims)+", "+str(int(awaypims) - int(homepims))+", "+str(awayhits)+", "+str(homehits)+", "+str(int(awayhits) - int(homehits))+", "+str(awaytaws)+", "+str(hometaws)+", "+str(int(awaytaws) - int(hometaws))+", "+str(awayfows)+", "+str(homefows)+", "+str(int(awayfows) - int(homefows))+")");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Stats (TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak)\n" + \
 "SELECT id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE FullName=\""+hometeamname+"\";");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Stats (TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak)\n" + \
 "SELECT id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE FullName=\""+awayteamname+"\";");
 return True;

def CloseHockeyDatabase(sqldatacon):
 db_integrity_check = sqldatacon[0].execute("PRAGMA integrity_check(100);").fetchone()[0];
 sqldatacon[0].execute("PRAGMA optimize;");
 sqldatacon[0].close();
 sqldatacon[1].close();
 return True;
