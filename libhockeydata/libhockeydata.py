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

    $FileInfo: libhockeydata.py - Last Update: 2/4/2020 Ver. 0.1.0 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals;
import sqlite3, sys, os, re, time, json;
import xml.etree.ElementTree as ET;
import logging as log;

try:
 from xml.sax.saxutils import xml_escape;
except ImportError:
 if(sys.version[0]=="2"):
  from cgi import escape as html_escape;
 if(sys.version[0]>="3"):
  from html import escape as html_escape;

__program_name__ = "PyHockeyStats";
__project__ = __program_name__;
__project_url__ = "https://github.com/GameMaker2k/Neo-Hockey-Test";
__version_info__ = (0, 1, 0, "RC 1", 1);
__version_date_info__ = (2020, 2, 4, "RC 1", 1);
__version_date__ = str(__version_date_info__[0])+"."+str(__version_date_info__[1]).zfill(2)+"."+str(__version_date_info__[2]).zfill(2);
__revision__ = __version_info__[3];
__revision_id__ = "$Id: 4ca62d10f283d43fc767538e2c13c1d4ce98db23 $";
if(__version_info__[4] is not None):
 __version_date_plusrc__ = __version_date__+"-"+str(__version_date_info__[4]);
if(__version_info__[4] is None):
 __version_date_plusrc__ = __version_date__;
if(__version_info__[3] is not None):
 __version__ = str(__version_info__[0])+"."+str(__version_info__[1])+"."+str(__version_info__[2])+" "+str(__version_info__[3]);
if(__version_info__[3] is None):
 __version__ = str(__version_info__[0])+"."+str(__version_info__[1])+"."+str(__version_info__[2]);

if __name__ == "__main__":
 import subprocess;
 curscrpath = os.path.dirname(sys.argv[0]);
 if(curscrpath==""):
  curscrpath = ".";
 if(os.sep=="\\"):
  curscrpath = curscrpath.replace(os.sep, "/");
 curscrpath = curscrpath+"/";
 scrfile = curscrpath+"mkhockeydata.py";
 if(os.path.exists(scrfile) and os.path.isfile(scrfile)):
  scrcmd = subprocess.Popen([sys.executable, scrfile] + sys.argv[1:]);
  scrcmd.wait();

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
 hockeyarray = { 'database': databasename, 'quickinfo': {'conferenceinfo': {}, 'divisioninfo': {}, 'teaminfo': {} }, 'leaguelist': [] };
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
 if "quickinfo" not in hockeyarray.keys():
  hockeyarray.update( { 'quickinfo': {'conferenceinfo': {}, 'divisioninfo': {}, 'teaminfo': {} } );
 if "database" not in hockeyarray.keys():
  hockeyarray.update( { 'database': "./hockeydatabase.sdb" } );
 if leaguename not in hockeyarray.keys():
  hockeyarray.update( { leaguename: { 'leagueinfo': { 'name': str(leaguename), 'fullname': str(leaguefullname), 'country': str(countryname), 'fullcountry': str(fullcountryname), 'date': str(date), 'playofffmt': str(playofffmt), 'ordertype': str(ordertype), 'conferences': str(hasconferences), 'divisions': str(hasdivisions), 'conferencelist': [] }, 'arenas': [ {} ], 'games': [ {} ] } } );
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

def MakeHockeyLeagues(sqldatacon, leaguename, leaguefullname, countryname, fullcountryname, date, playofffmt, ordertype):
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
   hockeyarray['quickinfo']['conferenceinfo'].update( { str(conference): { 'league': str(leaguename) } } );
   hockeyarray[leaguename]['conferencelist'].append(str(conference));
 return hockeyarray;

def RemoveHockeyConferenceFromArray(hockeyarray, leaguename, conference):
 if leaguename in hockeyarray.keys() and "conferencelist" not in hockeyarray[leaguename].keys():
  hockeyarray[leaguename].update( { 'conferencelist': [] } );
 if "database" not in hockeyarray.keys():
  hockeyarray.update( { 'database': "./hockeydatabase.sdb" } );
 if leaguename in hockeyarray.keys():
  if conference in hockeyarray[leaguename].keys():
   hockeyarray[leaguename].pop(conference, None);
   hockeyarray['quickinfo']['conferenceinfo'].pop(conference, None);
   hockeyarray[leaguename]['conferencelist'].remove(conference);
 return hockeyarray;

def ReplaceHockeyConferencFromArray(hockeyarray, leaguename, oldconference, newconference):
 if leaguename in hockeyarray.keys() and "conferencelist" not in hockeyarray[leaguename].keys():
  hockeyarray[leaguename].update( { 'conferencelist': [] } );
 if "database" not in hockeyarray.keys():
  hockeyarray.update( { 'database': "./hockeydatabase.sdb" } );
 if oldconference in hockeyarray[leaguename].keys() and newconference not in hockeyarray[leaguename].keys():
  hockeyarray[leaguename][newconference] = hockeyarray[leaguename].pop(str(oldconference));
  hockeyarray['quickinfo']['conferenceinfo'][newconference] = hockeyarray['quickinfo']['conferenceinfo'].pop(str(oldconference));
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

def MakeHockeyConferences(sqldatacon, leaguename, conference, hasconferences=True):
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
    hockeyarray['quickinfo']['divisioninfo'].update( { str(division): { 'league': str(leaguename), 'conference': str(conference) } } );
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
    hockeyarray[leaguename][conference].pop(division, None);
    hockeyarray['quickinfo']['divisioninfo'].pop(division, None);
    hockeyarray[leaguename][conference]['divisionlist'].remove(division);
 return hockeyarray;

def ReplaceHockeyDivisionFromArray(hockeyarray, leaguename, olddivision, newdivision, conference):
 if leaguename in hockeyarray.keys() and conference in hockeyarray[leaguename].keys() and "divisionlist" not in hockeyarray[leaguename][conference].keys():
  hockeyarray[leaguename][conference].update( { 'divisionlist': [] } );
 if "database" not in hockeyarray.keys():
  hockeyarray.update( { 'database': "./hockeydatabase.sdb" } );
 if olddivision in hockeyarray[leaguename][conference].keys() and newdivision not in hockeyarray[leaguename][conference].keys():
  hockeyarray[leaguename][conference][newdivision] = hockeyarray[leaguename][conference].pop(str(olddivision));
  hockeyarray['quickinfo']['divisioninfo'][newdivision] = hockeyarray['quickinfo']['divisioninfo'].pop(str(olddivision));
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

def MakeHockeyDivisions(sqldatacon, leaguename, division, conference, hasconferences=True, hasdivisions=True):
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
     hockeyarray[leaguename][conference][division].update( { str(teamname): { 'teaminfo': { 'city': str(cityname), 'area': str(areaname), 'fullarea': str(fullareaname), 'country': str(countryname), 'fullcountry': str(fullcountryname), 'name': str(teamname), 'arena': str(arenaname), 'prefix': str(teamnameprefix), 'suffix': str(teamnamesuffix), 'league': str(leaguename), 'conference': str(conference), 'division': str(division) } } } );
     hockeyarray['quickinfo']['teaminfo'].update( { str(teamname): { 'league': str(leaguename), 'conference': str(conference), 'division': str(division) } } );
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
     hockeyarray[leaguename][conference][division].pop(teamname, None);
     hockeyarray['quickinfo']['teaminfo'].pop(teamname, None);
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
  hockeyarray['quickinfo']['teaminfo'][newteamname] = hockeyarray['quickinfo']['teaminfo'].pop(str(oldteamname));
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

def MakeHockeyTeams(sqldatacon, leaguename, date, cityname, areaname, countryname, fullcountryname, fullareaname, teamname, conference, division, arenaname, teamnameprefix="", teamnamesuffix="", hasconferences=True, hasdivisions=True):
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

def MakeHockeyPlayoffTeams(sqldatacon, leaguename, playofffmt="Division=3,Conference=2"):
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

def MakeHockeyXMLFromHockeyXML(inxmlfile, xmlisfile=True, verbose=True):
 if(xmlisfile is True and (os.path.exists(inxmlfile) and os.path.isfile(inxmlfile))):
  hockeyfile = ET.parse(inxmlfile);
 elif(xmlisfile is False):
  hockeyfile = ET.ElementTree(ET.fromstring(inxmlfile));
 else:
  return False;
 gethockey = hockeyfile.getroot();
 if(verbose is True):
  VerbosePrintOut("<?xml version=\"1.0\" encoding=\"UTF-8\"?>");
 xmlstring = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
 if(gethockey.tag == "hockey"):
  if(verbose is True):
   VerbosePrintOut("<hockey database=\""+EscapeXMLString(str(gethockey.attrib['database']), quote=True)+"\">");
  xmlstring = xmlstring+"<hockey database=\""+EscapeXMLString(str(gethockey.attrib['database']), quote=True)+"\">\n";
 for getleague in gethockey:
  if(getleague.tag=="league"):
   if(verbose is True):
    VerbosePrintOut(" <league name=\""+EscapeXMLString(str(getleague.attrib['name']), quote=True)+"\" fullname=\""+EscapeXMLString(str(getleague.attrib['fullname']), quote=True)+"\" country=\""+EscapeXMLString(str(getleague.attrib['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(getleague.attrib['fullcountry']), quote=True)+"\" date=\""+EscapeXMLString(str(getleague.attrib['date']), quote=True)+"\" playofffmt=\""+EscapeXMLString(str(getleague.attrib['playofffmt']), quote=True)+"\" ordertype=\""+EscapeXMLString(str(getleague.attrib['ordertype']), quote=True)+"\" conferences=\""+EscapeXMLString(str(getleague.attrib['conferences']), quote=True)+"\" divisions=\""+EscapeXMLString(str(getleague.attrib['divisions']), quote=True)+"\">");
   xmlstring = xmlstring+" <league name=\""+EscapeXMLString(str(getleague.attrib['name']), quote=True)+"\" fullname=\""+EscapeXMLString(str(getleague.attrib['fullname']), quote=True)+"\" country=\""+EscapeXMLString(str(getleague.attrib['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(getleague.attrib['fullcountry']), quote=True)+"\" date=\""+EscapeXMLString(str(getleague.attrib['date']), quote=True)+"\" playofffmt=\""+EscapeXMLString(str(getleague.attrib['playofffmt']), quote=True)+"\" ordertype=\""+EscapeXMLString(str(getleague.attrib['ordertype']), quote=True)+"\" conferences=\""+EscapeXMLString(str(getleague.attrib['conferences']), quote=True)+"\" divisions=\""+EscapeXMLString(str(getleague.attrib['divisions']), quote=True)+"\">\n";
  if(getleague.tag == "league"):
   for getconference in getleague:
    if(getconference.tag == "conference"):
     if(verbose is True):
      VerbosePrintOut("  <conference name=\""+EscapeXMLString(str(getconference.attrib['name']), quote=True)+"\">");
     xmlstring = xmlstring+"  <conference name=\""+EscapeXMLString(str(getconference.attrib['name']), quote=True)+"\">\n";
    if(getconference.tag == "arenas"):
     if(verbose is True):
      VerbosePrintOut("  <arenas>");
     xmlstring = xmlstring+"  <arenas>\n";
     for getarenas in getconference:
      if(verbose is True):
       VerbosePrintOut("   <arena city=\""+EscapeXMLString(str(getarenas.attrib['city']), quote=True)+"\" area=\""+EscapeXMLString(str(getarenas.attrib['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(getarenas.attrib['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(getarenas.attrib['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(getarenas.attrib['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(getarenas.attrib['name']), quote=True)+"\" />");
      xmlstring = xmlstring+"   <arena city=\""+EscapeXMLString(str(getarenas.attrib['city']), quote=True)+"\" area=\""+EscapeXMLString(str(getarenas.attrib['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(getarenas.attrib['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(getarenas.attrib['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(getarenas.attrib['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(getarenas.attrib['name']), quote=True)+"\" />\n";
     if(verbose is True):
      VerbosePrintOut("  </arenas>");
     xmlstring = xmlstring+"  </arenas>\n";
    if(getconference.tag == "games"):
     if(verbose is True):
      VerbosePrintOut("  <games>");
     xmlstring = xmlstring+"  <games>\n";
     for getgame in getconference:
      if(verbose is True):
       VerbosePrintOut("   <game date=\""+EscapeXMLString(str(getgame.attrib['date']), quote=True)+"\" hometeam=\""+EscapeXMLString(str(getgame.attrib['hometeam']), quote=True)+"\" awayteam=\""+EscapeXMLString(str(getgame.attrib['awayteam']), quote=True)+"\" goals=\""+EscapeXMLString(str(getgame.attrib['goals']), quote=True)+"\" sogs=\""+EscapeXMLString(str(getgame.attrib['sogs']), quote=True)+"\" ppgs=\""+EscapeXMLString(str(getgame.attrib['ppgs']), quote=True)+"\" shgs=\""+EscapeXMLString(str(getgame.attrib['shgs']), quote=True)+"\" penalties=\""+EscapeXMLString(str(getgame.attrib['penalties']), quote=True)+"\" pims=\""+EscapeXMLString(str(getgame.attrib['pims']), quote=True)+"\" hits=\""+EscapeXMLString(str(getgame.attrib['hits']), quote=True)+"\" takeaways=\""+EscapeXMLString(str(getgame.attrib['takeaways']), quote=True)+"\" faceoffwins=\""+EscapeXMLString(str(getgame.attrib['faceoffwins']), quote=True)+"\" atarena=\""+EscapeXMLString(str(getgame.attrib['atarena']), quote=True)+"\" isplayoffgame=\""+EscapeXMLString(str(getgame.attrib['isplayoffgame']), quote=True)+"\" />");
      xmlstring = xmlstring+"   <game date=\""+EscapeXMLString(str(getgame.attrib['date']), quote=True)+"\" hometeam=\""+EscapeXMLString(str(getgame.attrib['hometeam']), quote=True)+"\" awayteam=\""+EscapeXMLString(str(getgame.attrib['awayteam']), quote=True)+"\" goals=\""+EscapeXMLString(str(getgame.attrib['goals']), quote=True)+"\" sogs=\""+EscapeXMLString(str(getgame.attrib['sogs']), quote=True)+"\" ppgs=\""+EscapeXMLString(str(getgame.attrib['ppgs']), quote=True)+"\" shgs=\""+EscapeXMLString(str(getgame.attrib['shgs']), quote=True)+"\" penalties=\""+EscapeXMLString(str(getgame.attrib['penalties']), quote=True)+"\" pims=\""+EscapeXMLString(str(getgame.attrib['pims']), quote=True)+"\" hits=\""+EscapeXMLString(str(getgame.attrib['hits']), quote=True)+"\" takeaways=\""+EscapeXMLString(str(getgame.attrib['takeaways']), quote=True)+"\" faceoffwins=\""+EscapeXMLString(str(getgame.attrib['faceoffwins']), quote=True)+"\" atarena=\""+EscapeXMLString(str(getgame.attrib['atarena']), quote=True)+"\" isplayoffgame=\""+EscapeXMLString(str(getgame.attrib['isplayoffgame']), quote=True)+"\" />\n";
     if(verbose is True):
      VerbosePrintOut("  </games>");
     xmlstring = xmlstring+"  </games>\n";
    if(getconference.tag == "conference"):
     for getdivision in getconference:
      if(verbose is True):
       VerbosePrintOut("   <division name=\""+EscapeXMLString(str(getdivision.attrib['name']), quote=True)+"\">");
      xmlstring = xmlstring+"   <division name=\""+EscapeXMLString(str(getdivision.attrib['name']), quote=True)+"\">\n";
      if(getdivision.tag == "division"):
       for getteam in getdivision:
        if(getteam.tag == "team"):
         if(verbose is True):
          VerbosePrintOut("    <team city=\""+EscapeXMLString(str(getteam.attrib['city']), quote=True)+"\" area=\""+EscapeXMLString(str(getteam.attrib['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(getteam.attrib['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(getteam.attrib['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(getteam.attrib['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(getteam.attrib['name']), quote=True)+"\" arena=\""+EscapeXMLString(str(getteam.attrib['arena']), quote=True)+"\" prefix=\""+EscapeXMLString(str(getteam.attrib['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(getteam.attrib['suffix']), quote=True)+"\" />");
         xmlstring = xmlstring+"    <team city=\""+EscapeXMLString(str(getteam.attrib['city']), quote=True)+"\" area=\""+EscapeXMLString(str(getteam.attrib['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(getteam.attrib['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(getteam.attrib['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(getteam.attrib['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(getteam.attrib['name']), quote=True)+"\" arena=\""+EscapeXMLString(str(getteam.attrib['arena']), quote=True)+"\" prefix=\""+EscapeXMLString(str(getteam.attrib['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(getteam.attrib['suffix']), quote=True)+"\" />\n";
       if(verbose is True):
        VerbosePrintOut("   </division>");
       xmlstring = xmlstring+"   </division>\n";
     if(verbose is True):
      VerbosePrintOut("  </conference>");
     xmlstring = xmlstring+"  </conference>\n";
   if(verbose is True):
    VerbosePrintOut(" </league>");
   xmlstring = xmlstring+" </league>\n";
 if(verbose is True):
  VerbosePrintOut("</hockey>");
 xmlstring = xmlstring+"</hockey>\n";
 return xmlstring;

def MakeHockeyXMLFileFromHockeyXML(inxmlfile, outxmlfile=None, xmlisfile=True, returnxml=False, verbose=True):
 if(xmlisfile is True and (not os.path.exists(inxmlfile) or not os.path.isfile(inxmlfile))):
  return False;
 if(outxmlfile is None and xmlisfile is True):
  file_wo_extension, file_extension = os.path.splitext(inxmlfile);
  outxmlfile = file_wo_extension+".xml";
 xmlfp = open(outxmlfile, "w+");
 xmlstring = MakeHockeyXMLFromHockeyXML(inxmlfile, xmlisfile, verbose);
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml is True):
  return xmlstring;
 if(returnxml is False):
  return True;
 return True;

def MakeHockeyXMLFromHockeyArray(inhockeyarray, verbose=True):
 if(verbose is True):
  VerbosePrintOut("<?xml version=\"1.0\" encoding=\"UTF-8\"?>");
 xmlstring = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
 if(verbose is True):
  VerbosePrintOut("<hockey database=\""+EscapeXMLString(str(inhockeyarray['database']), quote=True)+"\">");
 xmlstring = xmlstring+"<hockey database=\""+EscapeXMLString(str(inhockeyarray['database']), quote=True)+"\">\n";
 for hlkey in inhockeyarray['leaguelist']:
  if(verbose is True):
   VerbosePrintOut(" <league name=\""+EscapeXMLString(str(hlkey), quote=True)+"\" fullname=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['fullname']), quote=True)+"\" country=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['fullcountry']), quote=True)+"\" date=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['date']), quote=True)+"\" playofffmt=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['playofffmt']), quote=True)+"\" ordertype=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['ordertype']), quote=True)+"\" conferences=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['conferences']), quote=True)+"\" divisions=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['divisions']), quote=True)+"\">");
  xmlstring = xmlstring+" <league name=\""+EscapeXMLString(str(hlkey), quote=True)+"\" fullname=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['fullname']), quote=True)+"\" country=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['fullcountry']), quote=True)+"\" date=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['date']), quote=True)+"\" playofffmt=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['playofffmt']), quote=True)+"\" ordertype=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['ordertype']), quote=True)+"\" conferences=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['conferences']), quote=True)+"\" divisions=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['divisions']), quote=True)+"\">\n";
  for hckey in inhockeyarray[hlkey]['conferencelist']:
   if(verbose is True):
    VerbosePrintOut("  <conference name=\""+EscapeXMLString(str(hckey), quote=True)+"\">");
   xmlstring = xmlstring+"  <conference name=\""+EscapeXMLString(str(hckey), quote=True)+"\">\n";
   for hdkey in inhockeyarray[hlkey][hckey]['divisionlist']:
    if(verbose is True):
     VerbosePrintOut("   <division name=\""+EscapeXMLString(str(hdkey), quote=True)+"\">");
    xmlstring = xmlstring+"   <division name=\""+EscapeXMLString(str(hdkey), quote=True)+"\">\n";
    for htkey in inhockeyarray[hlkey][hckey][hdkey]['teamlist']:
     if(verbose is True):
      VerbosePrintOut("    <team city=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']), quote=True)+"\" area=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(htkey), quote=True)+"\" arena=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']), quote=True)+"\" prefix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']), quote=True)+"\" />");
     xmlstring = xmlstring+"    <team city=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']), quote=True)+"\" area=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(htkey), quote=True)+"\" arena=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']), quote=True)+"\" prefix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']), quote=True)+"\" />\n";
    if(verbose is True):
     VerbosePrintOut("   </division>");
    xmlstring = xmlstring+"   </division>\n";
   if(verbose is True):
    VerbosePrintOut("  </conference>");
   xmlstring = xmlstring+"  </conference>\n";
   hasarenas = False;
   for hakey in inhockeyarray[hlkey]['arenas']:
    if(hakey is True):
     hasarenas = True;
     if(verbose is True):
      VerbosePrintOut("   <arena city=\""+EscapeXMLString(str(hakey['city']), quote=True)+"\" area=\""+EscapeXMLString(str(hakey['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(hakey['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(hakey['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(hakey['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(hakey['name']), quote=True)+"\" />");
     xmlstring = xmlstring+"   <arena city=\""+EscapeXMLString(str(hakey['city']), quote=True)+"\" area=\""+EscapeXMLString(str(hakey['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(hakey['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(hakey['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(hakey['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(hakey['name']), quote=True)+"\" />\n";
   if(hasarenas is True):
    if(verbose is True):
     VerbosePrintOut("  </arenas>");
    xmlstring = xmlstring+"  </arenas>\n";
   hasgames = False;
   for hgkey in inhockeyarray[hlkey]['games']:
    if(hgkey is True):
     hasgames = True;
     if(verbose is True):
      VerbosePrintOut("   <game date=\""+EscapeXMLString(str(hgkey['date']), quote=True)+"\" hometeam=\""+EscapeXMLString(str(hgkey['hometeam']), quote=True)+"\" awayteam=\""+EscapeXMLString(str(hgkey['awayteam']), quote=True)+"\" goals=\""+EscapeXMLString(str(hgkey['goals']), quote=True)+"\" sogs=\""+EscapeXMLString(str(hgkey['sogs']), quote=True)+"\" ppgs=\""+EscapeXMLString(str(hgkey['ppgs']), quote=True)+"\" shgs=\""+EscapeXMLString(str(hgkey['shgs']), quote=True)+"\" penalties=\""+EscapeXMLString(str(hgkey['penalties']), quote=True)+"\" pims=\""+EscapeXMLString(str(hgkey['pims']), quote=True)+"\" hits=\""+EscapeXMLString(str(hgkey['hits']), quote=True)+"\" takeaways=\""+EscapeXMLString(str(hgkey['takeaways']), quote=True)+"\" faceoffwins=\""+EscapeXMLString(str(hgkey['faceoffwins']), quote=True)+"\" atarena=\""+EscapeXMLString(str(hgkey['atarena']), quote=True)+"\" isplayoffgame=\""+EscapeXMLString(str(hgkey['isplayoffgame']), quote=True)+"\" />");
     xmlstring = xmlstring+"   <game date=\""+EscapeXMLString(str(hgkey['date']), quote=True)+"\" hometeam=\""+EscapeXMLString(str(hgkey['hometeam']), quote=True)+"\" awayteam=\""+EscapeXMLString(str(hgkey['awayteam']), quote=True)+"\" goals=\""+EscapeXMLString(str(hgkey['goals']), quote=True)+"\" sogs=\""+EscapeXMLString(str(hgkey['sogs']), quote=True)+"\" ppgs=\""+EscapeXMLString(str(hgkey['ppgs']), quote=True)+"\" shgs=\""+EscapeXMLString(str(hgkey['shgs']), quote=True)+"\" penalties=\""+EscapeXMLString(str(hgkey['penalties']), quote=True)+"\" pims=\""+EscapeXMLString(str(hgkey['pims']), quote=True)+"\" hits=\""+EscapeXMLString(str(hgkey['hits']), quote=True)+"\" takeaways=\""+EscapeXMLString(str(hgkey['takeaways']), quote=True)+"\" faceoffwins=\""+EscapeXMLString(str(hgkey['faceoffwins']), quote=True)+"\" atarena=\""+EscapeXMLString(str(hgkey['atarena']), quote=True)+"\" isplayoffgame=\""+EscapeXMLString(str(hgkey['isplayoffgame']), quote=True)+"\" />\n";
   if(hasgames is True):
    if(verbose is True):
     VerbosePrintOut("  </games>");
    xmlstring = xmlstring+"  </games>\n";
  if(verbose is True):
   VerbosePrintOut(" </league>");
  xmlstring = xmlstring+" </league>\n";
 if(verbose is True):
  VerbosePrintOut("</hockey>");
 xmlstring = xmlstring+"</hockey>\n";
 return xmlstring;

def MakeHockeyXMLFileFromHockeyArray(inhockeyarray, outxmlfile=None, returnxml=False, verbose=True):
 if(outxmlfile is None):
  return False;
 xmlfp = open(outxmlfile, "w+");
 xmlstring = MakeHockeyXMLFromHockeyArray(inhockeyarray, verbose);
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml is True):
  return xmlstring;
 if(returnxml is False):
  return True;
 return True;

def MakeHockeyJSONFromHockeyArray(inarray, returnjson=False, verbose=True):
 jsonstring = json.dumps(inarray);
 if(verbose is True):
  VerbosePrintOut(jsonstring);
 return jsonstring;

def MakeHockeyArrayFromHockeyXML(inxmlfile, xmlisfile=True, verbose=True):
 if(xmlisfile is True and (os.path.exists(inxmlfile) and os.path.isfile(inxmlfile))):
  hockeyfile = ET.parse(inxmlfile);
 elif(xmlisfile is False):
  hockeyfile = ET.ElementTree(ET.fromstring(inxmlfile));
 else:
  return False;
 gethockey = hockeyfile.getroot();
 if(verbose is True):
  VerbosePrintOut("<?xml version=\"1.0\" encoding=\"UTF-8\"?>");
 if(gethockey.tag == "hockey"):
  if(verbose is True):
   VerbosePrintOut("<hockey database=\""+EscapeXMLString(str(gethockey.attrib['database']), quote=True)+"\">");
 leaguearrayout = { 'database': str(gethockey.attrib['database']), 'quickinfo': {'conferenceinfo': {}, 'divisioninfo': {}, 'teaminfo': {} } };
 leaguelist = [];
 for getleague in gethockey:
  leaguearray = {};
  if(getleague.tag=="league"):
   if(verbose is True):
    VerbosePrintOut(" <league name=\""+EscapeXMLString(str(getleague.attrib['name']), quote=True)+"\" fullname=\""+EscapeXMLString(str(getleague.attrib['fullname']), quote=True)+"\" country=\""+EscapeXMLString(str(getleague.attrib['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(getleague.attrib['fullcountry']), quote=True)+"\" date=\""+EscapeXMLString(str(getleague.attrib['date']), quote=True)+"\" playofffmt=\""+EscapeXMLString(str(getleague.attrib['playofffmt']), quote=True)+"\" ordertype=\""+EscapeXMLString(str(getleague.attrib['ordertype']), quote=True)+"\" conferences=\""+EscapeXMLString(str(getleague.attrib['conferences']), quote=True)+"\" divisions=\""+EscapeXMLString(str(getleague.attrib['divisions']), quote=True)+"\">");
   tempdict = { 'leagueinfo': { 'name': str(getleague.attrib['name']), 'fullname': str(getleague.attrib['fullname']), 'country': str(getleague.attrib['country']), 'fullcountry': str(getleague.attrib['fullcountry']), 'date': str(getleague.attrib['date']), 'playofffmt': str(getleague.attrib['playofffmt']), 'ordertype': str(getleague.attrib['ordertype']), 'conferences': str(getleague.attrib['conferences']), 'divisions': str(getleague.attrib['divisions']) } };
   leaguearray.update( { str(getleague.attrib['name']): tempdict } );
   leaguelist.append(str(getleague.attrib['name']));
  if(getleague.tag == "league"):
   conferencelist = [];
   for getconference in getleague:
    if(getconference.tag == "conference"):
     if(verbose is True):
      VerbosePrintOut("  <conference name=\""+EscapeXMLString(str(getconference.attrib['name']), quote=True)+"\">");
     leaguearray[str(getleague.attrib['name'])].update( { str(getconference.attrib['name']): { 'conferenceinfo': { 'name': str(getconference.attrib['name']), 'league': str(getleague.attrib['name']) } } } );
     leaguearrayout['quickinfo']['conferenceinfo'].update( { str(getconference.attrib['name']): { 'league': str(getleague.attrib['name']) } } );
     conferencelist.append(str(getconference.attrib['name']));
    arenalist = [];
    if(getconference.tag == "arenas"):
     if(verbose is True):
      VerbosePrintOut("  <arenas>");
     for getarenas in getconference:
      if(verbose is True):
       VerbosePrintOut("   <arena city=\""+EscapeXMLString(str(getarenas.attrib['city']), quote=True)+"\" area=\""+EscapeXMLString(str(getarenas.attrib['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(getarenas.attrib['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(getarenas.attrib['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(getarenas.attrib['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(getarenas.attrib['name']), quote=True)+"\" />");
      arenalist.append( { 'city': str(getarenas.attrib['city']), 'area': str(getarenas.attrib['area']), 'fullarea': str(getarenas.attrib['fullarea']), 'country': str(getarenas.attrib['country']), 'fullcountry': str(getarenas.attrib['fullcountry']), 'name': str(getarenas.attrib['name']) } );
     if(verbose is True):
      VerbosePrintOut("  </arenas>");
    leaguearray[str(getleague.attrib['name'])].update( { "arenas": arenalist } );
    gamelist = [];
    if(getconference.tag == "games"):
     if(verbose is True):
      VerbosePrintOut("  <games>");
     for getgame in getconference:
      if(verbose is True):
       VerbosePrintOut("   <game date=\""+EscapeXMLString(str(getgame.attrib['date']), quote=True)+"\" hometeam=\""+EscapeXMLString(str(getgame.attrib['hometeam']), quote=True)+"\" awayteam=\""+EscapeXMLString(str(getgame.attrib['awayteam']), quote=True)+"\" goals=\""+EscapeXMLString(str(getgame.attrib['goals']), quote=True)+"\" sogs=\""+EscapeXMLString(str(getgame.attrib['sogs']), quote=True)+"\" ppgs=\""+EscapeXMLString(str(getgame.attrib['ppgs']), quote=True)+"\" shgs=\""+EscapeXMLString(str(getgame.attrib['shgs']), quote=True)+"\" penalties=\""+EscapeXMLString(str(getgame.attrib['penalties']), quote=True)+"\" pims=\""+EscapeXMLString(str(getgame.attrib['pims']), quote=True)+"\" hits=\""+EscapeXMLString(str(getgame.attrib['hits']), quote=True)+"\" takeaways=\""+EscapeXMLString(str(getgame.attrib['takeaways']), quote=True)+"\" faceoffwins=\""+EscapeXMLString(str(getgame.attrib['faceoffwins']), quote=True)+"\" atarena=\""+EscapeXMLString(str(getgame.attrib['atarena']), quote=True)+"\" isplayoffgame=\""+EscapeXMLString(str(getgame.attrib['isplayoffgame']), quote=True)+"\" />");
      gamelist.append( { 'date': str(getgame.attrib['date']), 'hometeam': str(getgame.attrib['hometeam']), 'awayteam': str(getgame.attrib['awayteam']), 'goals': str(getgame.attrib['goals']), 'sogs': str(getgame.attrib['sogs']), 'ppgs': str(getgame.attrib['ppgs']), 'shgs': str(getgame.attrib['shgs']), 'penalties': str(getgame.attrib['penalties']), 'pims': str(getgame.attrib['pims']), 'hits': str(getgame.attrib['hits']), 'takeaways': str(getgame.attrib['takeaways']), 'faceoffwins': str(getgame.attrib['faceoffwins']), 'atarena': str(getgame.attrib['atarena']), 'isplayoffgame': str(getgame.attrib['isplayoffgame']) } );
     if(verbose is True):
      VerbosePrintOut("  </games>");
    leaguearray[str(getleague.attrib['name'])].update( { "games": gamelist } );
    divisiondict = {};
    divisionlist = [];
    if(getconference.tag == "conference"):
     for getdivision in getconference:
      if(verbose is True):
       VerbosePrintOut("   <division name=\""+str(getdivision.attrib['name'])+"\">");
      leaguearray[str(getleague.attrib['name'])][str(getconference.attrib['name'])].update( { str(getdivision.attrib['name']): { 'divisioninfo': { 'name': str(getdivision.attrib['name']), 'league': str(getleague.attrib['name']), 'conference': str(getconference.attrib['name']) } } } );
      leaguearrayout['quickinfo']['divisioninfo'].update( { str(getdivision.attrib['name']): { 'league': str(getleague.attrib['name']), 'conference': str(getconference.attrib['name']) } } );
      divisionlist.append(str(getdivision.attrib['name']));
      teamdist = {};
      teamlist = [];
      if(getdivision.tag == "division"):
       for getteam in getdivision:
        if(getteam.tag == "team"):
         if(verbose is True):
          VerbosePrintOut("    <team city=\""+EscapeXMLString(str(getteam.attrib['city']), quote=True)+"\" area=\""+EscapeXMLString(str(getteam.attrib['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(getteam.attrib['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(getteam.attrib['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(getteam.attrib['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(getteam.attrib['name']), quote=True)+"\" arena=\""+EscapeXMLString(str(getteam.attrib['arena']), quote=True)+"\" prefix=\""+EscapeXMLString(str(getteam.attrib['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(getteam.attrib['suffix']), quote=True)+"\" />");
         leaguearray[str(getleague.attrib['name'])][str(getconference.attrib['name'])][str(getdivision.attrib['name'])].update( { str(getteam.attrib['name']): { 'teaminfo': { 'city': str(getteam.attrib['city']), 'area': str(getteam.attrib['area']), 'fullarea': str(getteam.attrib['fullarea']), 'country': str(getteam.attrib['country']), 'fullcountry': str(getteam.attrib['fullcountry']), 'name': str(getteam.attrib['name']), 'arena': str(getteam.attrib['arena']), 'prefix': str(getteam.attrib['prefix']), 'suffix': str(getteam.attrib['suffix']), 'league': str(getleague.attrib['name']), 'conference': str(getconference.attrib['name']), 'division': str(getdivision.attrib['name']) } } } );
         leaguearrayout['quickinfo']['teaminfo'].update( { str(getteam.attrib['name']): { 'league': str(getleague.attrib['name']), 'conference': str(getconference.attrib['name']), 'division': str(getdivision.attrib['name']) } } );
         teamlist.append(str(getteam.attrib['name']));
       leaguearray[str(getleague.attrib['name'])][str(getconference.attrib['name'])][str(getdivision.attrib['name'])].update( { 'teamlist': teamlist } );
       if(verbose is True):
        VerbosePrintOut("   </division>");
     leaguearray[str(getleague.attrib['name'])][str(getconference.attrib['name'])].update( { 'divisionlist': divisionlist } );
     if(verbose is True):
      VerbosePrintOut("  </conference>");
   leaguearray[str(getleague.attrib['name'])].update( { 'conferencelist': conferencelist } );
   leaguearrayout.update(leaguearray);
   if(verbose is True):
    VerbosePrintOut(" </league>");
 leaguearrayout.update( { 'leaguelist': leaguelist } );
 if(verbose is True):
  VerbosePrintOut("</hockey>");
 return leaguearrayout;

def MakeHockeyJSONFromHockeyXML(inxmlfile, xmlisfile=True, returnjson=False, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(inxmlfile, xmlisfile, False, False);
 jsonstring = MakeHockeyJSONFromHockeyArray(hockeyarray, returnjson, verbose);
 if(verbose is True):
  VerbosePrintOut(jsonstring);
 return jsonstring;

def MakeHockeyDatabaseFromHockeyArray(inhockeyarray, sdbfile=None, returnxml=False, returndb=False, verbose=True):
 if(verbose is True):
  VerbosePrintOut("<?xml version=\"1.0\" encoding=\"UTF-8\"?>");
 xmlstring = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
 if(sdbfile is None):
  sqldatacon = MakeHockeyDatabase(inhockeyarray['database']);
 if(sdbfile is not None and isinstance(sdbfile, str)):
  sqldatacon = MakeHockeyDatabase(sdbfile);
 if(sdbfile is not None and isinstance(sdbfile, (tuple, list))):
  sqldatacon = tuple(sdbfile);
 if(verbose is True):
  VerbosePrintOut("<hockey database=\""+EscapeXMLString(str(inhockeyarray['database']), quote=True)+"\">");
 xmlstring = xmlstring+"<hockey database=\""+EscapeXMLString(str(inhockeyarray['database']), quote=True)+"\">\n";
 leaguecount = 0;
 for hlkey in inhockeyarray['leaguelist']:
  if(leaguecount==0):
   MakeHockeyLeagueTable(sqldatacon);
  MakeHockeyTeamTable(sqldatacon, hlkey);
  MakeHockeyConferenceTable(sqldatacon, hlkey);
  MakeHockeyGameTable(sqldatacon, hlkey);
  MakeHockeyDivisionTable(sqldatacon, hlkey);
  HockeyLeagueHasDivisions = True;
  if(inhockeyarray[hlkey]['leagueinfo']['conferences'].lower()=="no"):
   HockeyLeagueHasDivisions = False;
  HockeyLeagueHasConferences = True;
  if(inhockeyarray[hlkey]['leagueinfo']['divisions'].lower()=="no"):
   HockeyLeagueHasConferences = False;
  MakeHockeyLeagues(sqldatacon, hlkey, inhockeyarray[hlkey]['leagueinfo']['fullname'], inhockeyarray[hlkey]['leagueinfo']['country'], inhockeyarray[hlkey]['leagueinfo']['fullcountry'], inhockeyarray[hlkey]['leagueinfo']['date'], inhockeyarray[hlkey]['leagueinfo']['playofffmt'], inhockeyarray[hlkey]['leagueinfo']['ordertype']);
  if(verbose is True):
   VerbosePrintOut(" <league name=\""+EscapeXMLString(str(hlkey), quote=True)+"\" fullname=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['fullname']), quote=True)+"\" country=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['fullcountry']), quote=True)+"\" date=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['date']), quote=True)+"\" playofffmt=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['playofffmt']), quote=True)+"\" ordertype=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['ordertype']), quote=True)+"\" conferences=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['conferences']), quote=True)+"\" divisions=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['divisions']), quote=True)+"\">");
  xmlstring = xmlstring+" <league name=\""+EscapeXMLString(str(hlkey), quote=True)+"\" fullname=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['fullname']), quote=True)+"\" country=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['fullcountry']), quote=True)+"\" date=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['date']), quote=True)+"\" playofffmt=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['playofffmt']), quote=True)+"\" ordertype=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['ordertype']), quote=True)+"\" conferences=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['conferences']), quote=True)+"\" divisions=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['divisions']), quote=True)+"\">\n";
  leaguecount = leaguecount + 1;
  for hckey in inhockeyarray[hlkey]['conferencelist']:
   MakeHockeyConferences(sqldatacon, hlkey, hckey, HockeyLeagueHasConferences);
   if(verbose is True):
    VerbosePrintOut("  <conference name=\""+EscapeXMLString(str(hckey), quote=True)+"\">");
   xmlstring = xmlstring+"  <conference name=\""+EscapeXMLString(str(hckey), quote=True)+"\">\n";
   for hdkey in inhockeyarray[hlkey][hckey]['divisionlist']:
    MakeHockeyDivisions(sqldatacon, hlkey, hdkey, hckey, HockeyLeagueHasConferences, HockeyLeagueHasDivisions);
    if(verbose is True):
     VerbosePrintOut("   <division name=\""+EscapeXMLString(str(hdkey), quote=True)+"\">");
    xmlstring = xmlstring+"   <division name=\""+EscapeXMLString(str(hdkey), quote=True)+"\">\n";
    for htkey in inhockeyarray[hlkey][hckey][hdkey]['teamlist']:
     MakeHockeyTeams(sqldatacon, hlkey, str(inhockeyarray[hlkey]['leagueinfo']['date']), inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea'], htkey, hckey, hdkey, inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix'], HockeyLeagueHasConferences, HockeyLeagueHasDivisions);
     if(verbose is True):
      VerbosePrintOut("    <team city=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']), quote=True)+"\" area=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(htkey), quote=True)+"\" arena=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']), quote=True)+"\" prefix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']), quote=True)+"\" />");
     xmlstring = xmlstring+"    <team city=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']), quote=True)+"\" area=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(htkey), quote=True)+"\" arena=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']), quote=True)+"\" prefix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']), quote=True)+"\" />\n";
    if(verbose is True):
     VerbosePrintOut("   </division>");
    xmlstring = xmlstring+"   </division>\n";
   if(verbose is True):
    VerbosePrintOut("  </conference>");
   xmlstring = xmlstring+"  </conference>\n";
   hasarenas = False;
   for hakey in inhockeyarray[hlkey]['arenas']:
    if(hakey is True):
     hasarenas = True;
     MakeHockeyArena(sqldatacon, hlkey, hakey['city'], hakey['area'], hakey['country'], hakey['fullcountry'], hakey['fullarea'], hakey['name']);
     if(verbose is True):
      VerbosePrintOut("   <arena city=\""+EscapeXMLString(str(hakey['city']), quote=True)+"\" area=\""+EscapeXMLString(str(hakey['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(hakey['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(hakey['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(hakey['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(hakey['name']), quote=True)+"\" />");
     xmlstring = xmlstring+"   <arena city=\""+EscapeXMLString(str(hakey['city']), quote=True)+"\" area=\""+EscapeXMLString(str(hakey['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(hakey['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(hakey['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(hakey['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(hakey['name']), quote=True)+"\" />\n";
   if(hasarenas is True):
    if(verbose is True):
     VerbosePrintOut("  </arenas>");
    xmlstring = xmlstring+"  </arenas>\n";
   hasgames = False;
   for hgkey in inhockeyarray[hlkey]['games']:
    if(hgkey is True):
     hasgames = True;
     MakeHockeyGame(sqldatacon, hlkey, hgkey['date'], hgkey['hometeam'], hgkey['awayteam'], hgkey['goals'], hgkey['sogs'], hgkey['ppgs'], hgkey['shgs'], hgkey['penalties'], hgkey['pims'], hgkey['hits'], hgkey['takeaways'], hgkey['faceoffwins'], hgkey['atarena'], hgkey['isplayoffgame']);
     if(verbose is True):
      VerbosePrintOut("   <game date=\""+EscapeXMLString(str(hgkey['date']), quote=True)+"\" hometeam=\""+EscapeXMLString(str(hgkey['hometeam']), quote=True)+"\" awayteam=\""+EscapeXMLString(str(hgkey['awayteam']), quote=True)+"\" goals=\""+EscapeXMLString(str(hgkey['goals']), quote=True)+"\" sogs=\""+EscapeXMLString(str(hgkey['sogs']), quote=True)+"\" ppgs=\""+EscapeXMLString(str(hgkey['ppgs']), quote=True)+"\" shgs=\""+EscapeXMLString(str(hgkey['shgs']), quote=True)+"\" penalties=\""+EscapeXMLString(str(hgkey['penalties']), quote=True)+"\" pims=\""+EscapeXMLString(str(hgkey['pims']), quote=True)+"\" hits=\""+EscapeXMLString(str(hgkey['hits']), quote=True)+"\" takeaways=\""+EscapeXMLString(str(hgkey['takeaways']), quote=True)+"\" faceoffwins=\""+EscapeXMLString(str(hgkey['faceoffwins']), quote=True)+"\" atarena=\""+EscapeXMLString(str(hgkey['atarena']), quote=True)+"\" isplayoffgame=\""+EscapeXMLString(str(hgkey['isplayoffgame']), quote=True)+"\" />");
     xmlstring = xmlstring+"   <game date=\""+EscapeXMLString(str(hgkey['date']), quote=True)+"\" hometeam=\""+EscapeXMLString(str(hgkey['hometeam']), quote=True)+"\" awayteam=\""+EscapeXMLString(str(hgkey['awayteam']), quote=True)+"\" goals=\""+EscapeXMLString(str(hgkey['goals']), quote=True)+"\" sogs=\""+EscapeXMLString(str(hgkey['sogs']), quote=True)+"\" ppgs=\""+EscapeXMLString(str(hgkey['ppgs']), quote=True)+"\" shgs=\""+EscapeXMLString(str(hgkey['shgs']), quote=True)+"\" penalties=\""+EscapeXMLString(str(hgkey['penalties']), quote=True)+"\" pims=\""+EscapeXMLString(str(hgkey['pims']), quote=True)+"\" hits=\""+EscapeXMLString(str(hgkey['hits']), quote=True)+"\" takeaways=\""+EscapeXMLString(str(hgkey['takeaways']), quote=True)+"\" faceoffwins=\""+EscapeXMLString(str(hgkey['faceoffwins']), quote=True)+"\" atarena=\""+EscapeXMLString(str(hgkey['atarena']), quote=True)+"\" isplayoffgame=\""+EscapeXMLString(str(hgkey['isplayoffgame']), quote=True)+"\" />\n";
   if(hasgames is True):
    if(verbose is True):
     VerbosePrintOut("  </games>");
    xmlstring = xmlstring+"  </games>\n";
  if(verbose is True):
   VerbosePrintOut(" </league>");
  xmlstring = xmlstring+" </league>\n";
 if(verbose is True):
  VerbosePrintOut("</hockey>");
 xmlstring = xmlstring+"</hockey>\n";
 if(returndb is False):
  CloseHockeyDatabase(sqldatacon);
 if(returndb is True and returnxml is True):
  return [xmlstring, sqldatacon];
 if(returnxml is True and returndb is False):
  return xmlstring;
 if(returnxml is False and returndb is False):
  return True;
 return True;

def MakeHockeyDatabaseFromHockeyArrayWrite(inhockeyarray, sdbfile=None, outxmlfile=None, returnxml=False, verbose=True):
 if(outxmlfile is None):
  return False;
 xmlfp = open(outxmlfile, "w+");
 xmlstring = MakeHockeyDatabaseFromHockeyArray(inhockeyarray, sdbfile, True, False, verbose);
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml is True):
  return xmlstring;
 if(returnxml is False):
  return True;
 return True;

def MakeHockeyPythonFromHockeyArray(inhockeyarray, verbose=True):
 pyfilename = __name__;
 if(pyfilename=="__main__"):
  pyfilename = os.path.splitext(os.path.basename(__file__))[0];
 if(verbose is True):
  VerbosePrintOut("#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nfrom __future__ import absolute_import, division, print_function, unicode_literals;\nimport "+pyfilename+";\n");
 pystring = "#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nfrom __future__ import absolute_import, division, print_function, unicode_literals;\nimport "+pyfilename+";\n\n";
 if(verbose is True):
  VerbosePrintOut("sqldatacon = "+pyfilename+".MakeHockeyDatabase(\""+inhockeyarray['database']+"\");");
 pystring = pystring+"sqldatacon = "+pyfilename+".MakeHockeyDatabase(\""+inhockeyarray['database']+"\");\n";
 if(verbose is True):
  VerbosePrintOut(pyfilename+".MakeHockeyLeagueTable(sqldatacon);");
 pystring = pystring+pyfilename+".MakeHockeyLeagueTable(sqldatacon);\n";
 for hlkey in inhockeyarray['leaguelist']:
  HockeyLeagueHasDivisions = True;
  if(inhockeyarray[hlkey]['leagueinfo']['conferences'].lower()=="no"):
   HockeyLeagueHasDivisions = False;
  HockeyLeagueHasConferences = True;
  if(inhockeyarray[hlkey]['leagueinfo']['divisions'].lower()=="no"):
   HockeyLeagueHasConferences = False;
  if(verbose is True):
   VerbosePrintOut(pyfilename+".MakeHockeyTeamTable(sqldatacon, \""+hlkey+"\");\n"+pyfilename+".MakeHockeyConferenceTable(sqldatacon, \""+hlkey+"\");\n"+pyfilename+".MakeHockeyGameTable(sqldatacon, \""+hlkey+"\");\n"+pyfilename+".MakeHockeyDivisionTable(sqldatacon, \""+hlkey+"\");\n"+pyfilename+".MakeHockeyLeagues(sqldatacon, \""+hlkey+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullname']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['country']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullcountry']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['date']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['playofffmt']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['ordertype']+"\");");
  pystring = pystring+pyfilename+".MakeHockeyTeamTable(sqldatacon, \""+hlkey+"\");\n"+pyfilename+".MakeHockeyConferenceTable(sqldatacon, \""+hlkey+"\");\n"+pyfilename+".MakeHockeyGameTable(sqldatacon, \""+hlkey+"\");\n"+pyfilename+".MakeHockeyDivisionTable(sqldatacon, \""+hlkey+"\");\n"+pyfilename+".MakeHockeyLeagues(sqldatacon, \""+hlkey+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullname']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['country']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullcountry']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['date']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['playofffmt']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['ordertype']+"\");\n";
  for hckey in inhockeyarray[hlkey]['conferencelist']:
   if(verbose is True):
    VerbosePrintOut(pyfilename+".MakeHockeyConferences(sqldatacon, \""+hlkey+"\", \""+hckey+"\", "+str(HockeyLeagueHasConferences)+");");
   pystring = pystring+pyfilename+".MakeHockeyConferences(sqldatacon, \""+hlkey+"\", \""+hckey+"\", "+str(HockeyLeagueHasConferences)+");\n";
   for hdkey in inhockeyarray[hlkey][hckey]['divisionlist']:
    if(verbose is True):
     VerbosePrintOut(pyfilename+".MakeHockeyDivisions(sqldatacon, \""+hlkey+"\", \""+hdkey+"\", \""+hckey+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");");
    pystring = pystring+pyfilename+".MakeHockeyDivisions(sqldatacon, \""+hlkey+"\", \""+hdkey+"\", \""+hckey+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");\n";
    for htkey in inhockeyarray[hlkey][hckey][hdkey]['teamlist']:
     if(verbose is True):
      VerbosePrintOut(pyfilename+".MakeHockeyTeams(sqldatacon, \""+hlkey+"\", \""+str(inhockeyarray[hlkey]['leagueinfo']['date'])+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']+"\", \""+htkey+"\", \""+hckey+"\", \""+hdkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");");
     pystring = pystring+pyfilename+".MakeHockeyTeams(sqldatacon, \""+hlkey+"\", \""+str(inhockeyarray[hlkey]['leagueinfo']['date'])+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']+"\", \""+htkey+"\", \""+hckey+"\", \""+hdkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");\n";
   hasarenas = False;
   for hakey in inhockeyarray[hlkey]['arenas']:
    if(hakey is True):
     hasarenas = True;
     if(verbose is True):
      VerbosePrintOut(pyfilename+".MakeHockeyArena(sqldatacon, \""+hlkey+"\", \""+hakey['city']+"\", \""+hakey['area']+"\", \""+hakey['country']+"\", \""+hakey['fullcountry']+"\", \""+hakey['fullarea']+"\", \""+hakey['name']+"\");");
     pystring = pystring+pyfilename+".MakeHockeyArena(sqldatacon, \""+hlkey+"\", \""+hakey['city']+"\", \""+hakey['area']+"\", \""+hakey['country']+"\", \""+hakey['fullcountry']+"\", \""+hakey['fullarea']+"\", \""+hakey['name']+"\");\n";
   hasgames = False;
   for hgkey in inhockeyarray[hlkey]['games']:
    if(hgkey is True):
     hasgames = True;
     AtArena = hgkey['atarena'];
     '''
     if(GetTeamData(sqldatacon, getleague.attrib['name'], GetTeam2Num(sqldatacon, getleague.attrib['name'], hgkey['hometeam']), "FullArenaName", "str")==AtArena):
      AtArena = "0";
     if(GetTeamData(sqldatacon, getleague.attrib['name'], GetTeam2Num(sqldatacon, getleague.attrib['name'], hgkey['awayteam']), "FullArenaName", "str")==AtArena):
      AtArena = "1";
     '''
     if(verbose is True):
      VerbosePrintOut(pyfilename+".MakeHockeyGame(sqldatacon, \""+hlkey+"\", "+hgkey['date']+", \""+hgkey['hometeam']+"\", \""+hgkey['awayteam']+"\", \""+hgkey['goals']+"\", \""+hgkey['sogs']+"\", \""+hgkey['ppgs']+"\", \""+hgkey['shgs']+"\", \""+hgkey['penalties']+"\", \""+hgkey['pims']+"\", \""+hgkey['hits']+"\", \""+hgkey['takeaways']+"\", \""+hgkey['faceoffwins']+"\", \""+AtArena+"\", \""+hgkey['isplayoffgame']+"\");");
     pystring = pystring+pyfilename+".MakeHockeyGame(sqldatacon, \""+hlkey+"\", "+hgkey['date']+", \""+hgkey['hometeam']+"\", \""+hgkey['awayteam']+"\", \""+hgkey['goals']+"\", \""+hgkey['sogs']+"\", \""+hgkey['ppgs']+"\", \""+hgkey['shgs']+"\", \""+hgkey['penalties']+"\", \""+hgkey['pims']+"\", \""+hgkey['hits']+"\", \""+hgkey['takeaways']+"\", \""+hgkey['faceoffwins']+"\", \""+AtArena+"\", \""+hgkey['isplayoffgame']+"\");\n";
  if(verbose is True):
   VerbosePrintOut(" ");
  pystring = pystring+"\n";
 if(verbose is True):
  VerbosePrintOut(pyfilename+".CloseHockeyDatabase(sqldatacon);");
 pystring = pystring+pyfilename+".CloseHockeyDatabase(sqldatacon);\n";
 return pystring;

def MakeHockeyPythonFileFromHockeyArray(inhockeyarray, outpyfile=None, returnpy=False, verbose=True):
 if(outpyfile is None):
  return False;
 pyfp = open(outpyfile, "w+");
 pystring = MakeHockeyPythonFromHockeyArray(inhockeyarray, verbose);
 pyfp.write(pystring);
 pyfp.close();
 if(returnpy is True):
  return pystring;
 if(returnpy is False):
  return True;
 return True;

def MakeHockeyPythonAltFromHockeyArray(inhockeyarray, verbose=True):
 pyfilename = __name__;
 if(pyfilename=="__main__"):
  pyfilename = os.path.splitext(os.path.basename(__file__))[0];
 if(verbose is True):
  VerbosePrintOut("#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nfrom __future__ import absolute_import, division, print_function, unicode_literals;\nimport "+pyfilename+";\n");
 pystring = "#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nfrom __future__ import absolute_import, division, print_function, unicode_literals;\nimport "+pyfilename+";\n\n";
 if(verbose is True):
  VerbosePrintOut("hockeyarray = "+pyfilename+".CreateHockeyArray(\""+inhockeyarray['database']+"\");");
 pystring = pystring+"hockeyarray = "+pyfilename+".CreateHockeyArray(\""+inhockeyarray['database']+"\");\n";
 for hlkey in inhockeyarray['leaguelist']:
  HockeyLeagueHasDivisions = True;
  if(inhockeyarray[hlkey]['leagueinfo']['conferences'].lower()=="no"):
   HockeyLeagueHasDivisions = False;
  HockeyLeagueHasConferences = True;
  if(inhockeyarray[hlkey]['leagueinfo']['divisions'].lower()=="no"):
   HockeyLeagueHasConferences = False;
  if(verbose is True):
   VerbosePrintOut("hockeyarray = "+pyfilename+".AddHockeyLeagueToArray(hockeyarray, \""+hlkey+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullname']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['country']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullcountry']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['date']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['playofffmt']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['ordertype']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");");
  pystring = pystring+"hockeyarray = "+pyfilename+".AddHockeyLeagueToArray(hockeyarray, \""+hlkey+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullname']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['country']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullcountry']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['date']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['playofffmt']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['ordertype']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");\n";
  for hckey in inhockeyarray[hlkey]['conferencelist']:
   if(verbose is True):
    VerbosePrintOut("hockeyarray = "+pyfilename+".AddHockeyConferenceToArray(hockeyarray, \""+hlkey+"\", \""+hckey+"\");");
   pystring = pystring+"hockeyarray = "+pyfilename+".AddHockeyConferenceToArray(hockeyarray, \""+hlkey+"\", \""+hckey+"\");\n";
   for hdkey in inhockeyarray[hlkey][hckey]['divisionlist']:
    if(verbose is True):
     VerbosePrintOut("hockeyarray = "+pyfilename+".AddHockeyDivisionToArray(hockeyarray, \""+hlkey+"\", \""+hdkey+"\", \""+hckey+"\");");
    pystring = pystring+"hockeyarray = "+pyfilename+".AddHockeyDivisionToArray(hockeyarray, \""+hlkey+"\", \""+hdkey+"\", \""+hckey+"\");\n";
    for htkey in inhockeyarray[hlkey][hckey][hdkey]['teamlist']:
     if(verbose is True):
      VerbosePrintOut("hockeyarray = "+pyfilename+".AddHockeyTeamToArray(hockeyarray, \""+hlkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']+"\", \""+htkey+"\", \""+hckey+"\", \""+hdkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']+"\");");
     pystring = pystring+"hockeyarray = "+pyfilename+".AddHockeyTeamToArray(hockeyarray, \""+hlkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']+"\", \""+htkey+"\", \""+hckey+"\", \""+hdkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']+"\");\n";
   hasarenas = False;
   for hakey in inhockeyarray[hlkey]['arenas']:
    if(hakey is True):
     hasarenas = True;
     if(verbose is True):
      VerbosePrintOut("hockeyarray = "+pyfilename+".AddHockeyArenaToArray(sqldatacon, \""+hlkey+"\", \""+hakey['city']+"\", \""+hakey['area']+"\", \""+hakey['country']+"\", \""+hakey['fullcountry']+"\", \""+hakey['fullarea']+"\", \""+hakey['name']+"\");");
     pystring = pystring+"hockeyarray = "+pyfilename+".AddHockeyArenaToArray(sqldatacon, \""+hlkey+"\", \""+hakey['city']+"\", \""+hakey['area']+"\", \""+hakey['country']+"\", \""+hakey['fullcountry']+"\", \""+hakey['fullarea']+"\", \""+hakey['name']+"\");\n";
   hasgames = False;
   for hgkey in inhockeyarray[hlkey]['games']:
    if(hgkey is True):
     hasgames = True;
     AtArena = hgkey['atarena'];
     '''
     if(GetTeamData(hockeyarray, getleague.attrib['name'], GetTeam2Num(hockeyarray, getleague.attrib['name'], hgkey['hometeam']), "FullArenaName", "str")==AtArena):
      AtArena = "0";
     if(GetTeamData(hockeyarray, getleague.attrib['name'], GetTeam2Num(hockeyarray, getleague.attrib['name'], hgkey['awayteam']), "FullArenaName", "str")==AtArena):
      AtArena = "1";
     '''
     if(verbose is True):
      VerbosePrintOut("hockeyarray = "+pyfilename+".AddHockeyGameToArray(hockeyarray, \""+hlkey+"\", "+hgkey['date']+", \""+hgkey['hometeam']+"\", \""+hgkey['awayteam']+"\", \""+hgkey['goals']+"\", \""+hgkey['sogs']+"\", \""+hgkey['ppgs']+"\", \""+hgkey['shgs']+"\", \""+hgkey['penalties']+"\", \""+hgkey['pims']+"\", \""+hgkey['hits']+"\", \""+hgkey['takeaways']+"\", \""+hgkey['faceoffwins']+"\", \""+AtArena+"\", \""+hgkey['isplayoffgame']+"\");");
     pystring = pystring+"hockeyarray = "+pyfilename+".AddHockeyGameToArray(hockeyarray, \""+hlkey+"\", "+hgkey['date']+", \""+hgkey['hometeam']+"\", \""+hgkey['awayteam']+"\", \""+hgkey['goals']+"\", \""+hgkey['sogs']+"\", \""+hgkey['ppgs']+"\", \""+hgkey['shgs']+"\", \""+hgkey['penalties']+"\", \""+hgkey['pims']+"\", \""+hgkey['hits']+"\", \""+hgkey['takeaways']+"\", \""+hgkey['faceoffwins']+"\", \""+AtArena+"\", \""+hgkey['isplayoffgame']+"\");\n";
  if(verbose is True):
   VerbosePrintOut(" ");
  pystring = pystring+"\n";
 if(verbose is True):
  VerbosePrintOut("hockeyarray = "+pyfilename+".MakeHockeyDatabaseFromHockeyArray(hockeyarray, None, False, False, False);");
 pystring = pystring+pyfilename+".MakeHockeyDatabaseFromHockeyArray(hockeyarray, None, False, False, False);\n";
 return pystring;

def MakeHockeyPythonAltFileFromHockeyArray(inhockeyarray, outpyfile=None, returnpy=False, verbose=True):
 if(outpyfile is None):
  return False;
 pyfp = open(outpyfile, "w+");
 pystring = MakeHockeyPythonAltFromHockeyArray(inhockeyarray, verbose);
 pyfp.write(pystring);
 pyfp.close();
 if(returnpy is True):
  return pystring;
 if(returnpy is False):
  return True;
 return True;

def MakeHockeyArrayFromHockeyDatabase(sdbfile, verbose=True):
 if(os.path.exists(sdbfile) and os.path.isfile(sdbfile) and isinstance(sdbfile, str)):
  sqldatacon = OpenHockeyDatabase(sdbfile);
 else:
  if(sdbfile is not None and isinstance(sdbfile, (tuple, list))):
   sqldatacon = tuple(sdbfile);
  else:
   return False;
 leaguecur = sqldatacon[1].cursor();
 if(verbose is True):
  VerbosePrintOut("<?xml version=\"1.0\" encoding=\"UTF-8\"?>");
  VerbosePrintOut("<hockey database=\""+EscapeXMLString(str(sdbfile), quote=True)+"\">");
 getleague_num = leaguecur.execute("SELECT COUNT(*) FROM HockeyLeagues").fetchone()[0];
 getleague = leaguecur.execute("SELECT LeagueName, LeagueFullName, CountryName, FullCountryName, Date, PlayOffFMT, OrderType, NumberOfConferences, NumberOfDivisions FROM HockeyLeagues");
 leaguearrayout = { 'database': str(sdbfile), 'quickinfo': {'conferenceinfo': {}, 'divisioninfo': {}, 'teaminfo': {} } };
 leaguelist = [];
 for leagueinfo in getleague:
  leaguearray = {};
  HockeyLeagueHasDivisions = True;
  HockeyLeagueHasDivisionStr = "yes";
  if(int(leagueinfo[7])<=0):
   HockeyLeagueHasDivisions = False;
   HockeyLeagueHasDivisionStr = "no";
  HockeyLeagueHasConferences = True;
  HockeyLeagueHasConferenceStr = "yes";
  if(int(leagueinfo[8])<=0):
   HockeyLeagueHasConferences = False;
   HockeyLeagueHasConferenceStr = "no";
  tempdict = { 'leagueinfo': { 'name': str(leagueinfo[0]), 'fullname': str(leagueinfo[1]), 'country': str(leagueinfo[2]), 'fullcountry': str(leagueinfo[3]), 'date': str(leagueinfo[4]), 'playofffmt': str(leagueinfo[5]), 'ordertype': str(leagueinfo[6]), 'conferences': str(HockeyLeagueHasConferenceStr), 'divisions': str(HockeyLeagueHasDivisionStr) } };
  leaguearray.update( { str(leagueinfo[0]): tempdict } );
  leaguelist.append(str(leagueinfo[0]));
  if(verbose is True):
   VerbosePrintOut(" <league name=\""+EscapeXMLString(str(leagueinfo[0]), quote=True)+"\" fullname=\""+EscapeXMLString(str(leagueinfo[1]), quote=True)+"\" country=\""+EscapeXMLString(str(leagueinfo[2]), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(leagueinfo[3]), quote=True)+"\" date=\""+EscapeXMLString(str(leagueinfo[4]), quote=True)+"\" playofffmt=\""+EscapeXMLString(str(leagueinfo[5]), quote=True)+"\" ordertype=\""+EscapeXMLString(str(leagueinfo[6]), quote=True)+"\" conferences=\""+EscapeXMLString(str(HockeyLeagueHasConferenceStr), quote=True)+"\" divisions=\""+EscapeXMLString(str(HockeyLeagueHasDivisionStr), quote=True)+"\">");
  conferencecur = sqldatacon[1].cursor();
  getconference_num = conferencecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Conferences WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\"").fetchone()[0];
  getconference = conferencecur.execute("SELECT Conference FROM "+leagueinfo[0]+"Conferences WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\"");
  conferencelist = [];
  for conferenceinfo in getconference:
   leaguearray[str(leagueinfo[0])].update( { str(conferenceinfo[0]): { 'conferenceinfo': { 'name': str(conferenceinfo[0]), 'league': str(leagueinfo[0]) } } } );
   leaguearrayout['quickinfo']['conferenceinfo'].update( { str(conferenceinfo[0]): { 'league': str(leagueinfo[0]) } } );
   conferencelist.append(str(conferenceinfo[0]));
   if(verbose is True):
    VerbosePrintOut("  <conference name=\""+str(conferenceinfo[0])+"\">");
   divisioncur = sqldatacon[1].cursor();
   getdivision_num = divisioncur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Divisions WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\"").fetchone()[0];
   getdivision = divisioncur.execute("SELECT Division FROM "+leagueinfo[0]+"Divisions WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\"");
   divisionlist = [];
   for divisioninfo in getdivision:
    leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update( { str(divisioninfo[0]): { 'divisioninfo': { 'name': str(divisioninfo[0]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]) } } } );
    leaguearrayout['quickinfo']['divisioninfo'].update( { str(divisioninfo[0]): { 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]) } } );
    divisionlist.append(str(divisioninfo[0]));
    if(verbose is True):
     VerbosePrintOut("   <division name=\""+EscapeXMLString(str(divisioninfo[0]), quote=True)+"\">");
    teamcur = sqldatacon[1].cursor();
    getteam_num = teamcur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Teams WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"").fetchone()[0];
    getteam = teamcur.execute("SELECT CityName, AreaName, FullAreaName, CountryName, FullCountryName, TeamName, ArenaName, TeamPrefix, TeamSuffix FROM "+leagueinfo[0]+"Teams WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"");
    teamlist = [];
    for teaminfo in getteam:
     leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(divisioninfo[0])].update( { str(teaminfo[5]): { 'teaminfo': { 'city': str(teaminfo[0]), 'area': str(teaminfo[1]), 'fullarea': str(teaminfo[2]), 'country': str(teaminfo[3]), 'fullcountry': str(teaminfo[4]), 'name': str(teaminfo[5]), 'arena': str(teaminfo[6]), 'prefix': str(teaminfo[7]), 'suffix': str(teaminfo[8]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0]) } } } );
     leaguearrayout['quickinfo']['teaminfo'].update( { str(teaminfo[5]): { 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0]) } } );
     teamlist.append(str(teaminfo[5]));
     if(verbose is True):
      VerbosePrintOut("    <team city=\""+EscapeXMLString(str(teaminfo[0]), quote=True)+"\" area=\""+EscapeXMLString(str(teaminfo[1]), quote=True)+"\" fullarea=\""+EscapeXMLString(str(teaminfo[2]), quote=True)+"\" country=\""+EscapeXMLString(str(teaminfo[3]), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(teaminfo[4]), quote=True)+"\" name=\""+EscapeXMLString(str(teaminfo[5]), quote=True)+"\" arena=\""+EscapeXMLString(str(teaminfo[6]), quote=True)+"\" prefix=\""+EscapeXMLString(str(teaminfo[7]), quote=True)+"\" suffix=\""+EscapeXMLString(str(teaminfo[8]), quote=True)+"\" />");
    teamcur.close();
    leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(divisioninfo[0])].update( { 'teamlist': teamlist } );
    if(verbose is True):
     VerbosePrintOut("   </division>");
   divisioncur.close();
   leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update( { 'divisionlist': divisionlist } );
   if(verbose is True):
    VerbosePrintOut("  </conference>");
  conferencecur.close();
  leaguearray[str(leagueinfo[0])].update( { 'conferencelist': conferencelist } );
  arenacur = sqldatacon[1].cursor();
  getteam_num = arenacur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Arenas WHERE TeamID=0").fetchone()[0];
  getarena = arenacur.execute("SELECT CityName, AreaName, FullAreaName, CountryName, FullCountryName, ArenaName FROM "+leagueinfo[0]+"Arenas WHERE TeamID=0");
  arenalist = [];
  if(getteam_num>0):
   for arenainfo in getarena:
    if(verbose is True):
     VerbosePrintOut("   <arena city=\""+EscapeXMLString(str(arenainfo[0]), quote=True)+"\" area=\""+EscapeXMLString(str(arenainfo[1]), quote=True)+"\" fullarea=\""+EscapeXMLString(str(arenainfo[2]), quote=True)+"\" country=\""+EscapeXMLString(str(arenainfo[3]), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(arenainfo[4]), quote=True)+"\" name=\""+EscapeXMLString(str(arenainfo[5]), quote=True)+"\" />");
    arenalist.append( { 'city': str(arenainfo[0]), 'area': str(arenainfo[1]), 'fullarea': str(arenainfo[2]), 'country': str(arenainfo[3]), 'fullcountry': str(arenainfo[4]), 'name': str(arenainfo[5]) } );
    if(verbose is True):
     VerbosePrintOut("   <arena city=\""+EscapeXMLString(str(arenainfo[0]), quote=True)+"\" area=\""+EscapeXMLString(str(arenainfo[1]), quote=True)+"\" fullarea=\""+EscapeXMLString(str(arenainfo[2]), quote=True)+"\" country=\""+EscapeXMLString(str(arenainfo[3]), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(arenainfo[4]), quote=True)+"\" name=\""+EscapeXMLString(str(arenainfo[5]), quote=True)+"\" />");
   if(verbose is True):
    VerbosePrintOut("  </arenas>");
  leaguearray[str(leagueinfo[0])].update( { "arenas": arenalist } );
  gamecur = sqldatacon[1].cursor();
  getgame_num = gamecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Games").fetchone()[0];
  getgame = gamecur.execute("SELECT Date, HomeTeam, AwayTeam, TeamScorePeriods, ShotsOnGoal, PowerPlays, ShortHanded, Penalties, PenaltyMinutes, HitsPerPeriod, TakeAways, FaceoffWins, AtArena, IsPlayOffGame FROM "+leagueinfo[0]+"Games");
  gamelist = [];
  if(getgame_num>0):
   if(verbose is True):
    VerbosePrintOut("  <games>");
   for gameinfo in getgame:
    AtArena = gameinfo[12];
    if(GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[1]), "FullArenaName", "str")==AtArena):
     AtArena = "0";
    if(GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[2]), "FullArenaName", "str")==AtArena):
     AtArena = "1";
    gamelist.append( { 'date': str(gameinfo[0]), 'hometeam': str(gameinfo[1]), 'awayteam': str(gameinfo[2]), 'goals': str(gameinfo[3]), 'sogs': str(gameinfo[4]), 'ppgs': str(gameinfo[5]), 'shgs': str(gameinfo[6]), 'penalties': str(gameinfo[7]), 'pims': str(gameinfo[8]), 'hits': str(gameinfo[9]), 'takeaways': str(gameinfo[10]), 'faceoffwins': str(gameinfo[11]), 'atarena': str(AtArena), 'isplayoffgame': str(gameinfo[13]) } );
    if(verbose is True):
     VerbosePrintOut("   <game date=\""+EscapeXMLString(str(gameinfo[0]), quote=True)+"\" hometeam=\""+EscapeXMLString(str(gameinfo[1]), quote=True)+"\" awayteam=\""+EscapeXMLString(str(gameinfo[2]), quote=True)+"\" goals=\""+EscapeXMLString(str(gameinfo[3]), quote=True)+"\" sogs=\""+EscapeXMLString(str(gameinfo[4]), quote=True)+"\" ppgs=\""+EscapeXMLString(str(gameinfo[5]), quote=True)+"\" shgs=\""+EscapeXMLString(str(gameinfo[6]), quote=True)+"\" penalties=\""+EscapeXMLString(str(gameinfo[7]), quote=True)+"\" pims=\""+EscapeXMLString(str(gameinfo[8]), quote=True)+"\" hits=\""+EscapeXMLString(str(gameinfo[9]), quote=True)+"\" takeaways=\""+EscapeXMLString(str(gameinfo[10]), quote=True)+"\" faceoffwins=\""+EscapeXMLString(str(gameinfo[11]), quote=True)+"\" atarena=\""+EscapeXMLString(str(AtArena), quote=True)+"\" isplayoffgame=\""+EscapeXMLString(str(gameinfo[13]), quote=True)+"\" />");
   if(verbose is True):
    VerbosePrintOut("  </games>");
  leaguearray[str(leagueinfo[0])].update( { "games": gamelist } );
  leaguearrayout.update(leaguearray);
  if(verbose is True):
   VerbosePrintOut(" </league>");
 leaguearrayout.update( { 'leaguelist': leaguelist } );
 if(verbose is True):
  VerbosePrintOut("</hockey>");
 leaguecur.close();
 sqldatacon[1].close();
 return leaguearrayout;

def MakeHockeyJSONFromHockeyDatabase(sdbfile, returnjson=False, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(sdbfile, False);
 jsonstring = MakeHockeyJSONFromHockeyArray(hockeyarray, returnjson, verbose);
 if(verbose is True):
  VerbosePrintOut(jsonstring);
 return jsonstring;

def MakeHockeyArrayFromHockeySQL(sqlfile, sdbfile=None, sqlisfile=True, verbose=True):
 if(sqlisfile is True and (os.path.exists(sqlfile) and os.path.isfile(sqlfile))):
  sqlfp = open(sqlfile, "r");
  sqlstring = sqlfp.read();
  sqlfp.close();
 elif(sqlisfile is False):
  sqlstring = sqlfile;
 else:
  return False;
 if(sdbfile is None and len(re.findall(r"Database\:([\w\W]+)", "-- Database: ./hockey17-18.db3"))>=1):
  sdbfile = re.findall(r"Database\:([\w\W]+)", "-- Database: ./hockey17-18.db3")[0].strip();
 if(sdbfile is None and len(re.findall(r"Database\:([\w\W]+)", "-- Database: ./hockey17-18.db3"))<1):
  file_wo_extension, file_extension = os.path.splitext(sqlfile);
  sdbfile = file_wo_extension+".db3";
 sqldatacon = MakeHockeyDatabase(":memory:");
 sqldatacon[0].executescript(sqlstring);
 leaguecur = sqldatacon[1].cursor();
 if(verbose is True):
  VerbosePrintOut("<?xml version=\"1.0\" encoding=\"UTF-8\"?>");
  VerbosePrintOut("<hockey database=\""+EscapeXMLString(str(sdbfile), quote=True)+"\">");
 getleague_num = leaguecur.execute("SELECT COUNT(*) FROM HockeyLeagues").fetchone()[0];
 getleague = leaguecur.execute("SELECT LeagueName, LeagueFullName, CountryName, FullCountryName, Date, PlayOffFMT, OrderType, NumberOfConferences, NumberOfDivisions FROM HockeyLeagues");
 leaguearrayout = { 'database': str(sdbfile), 'quickinfo': {'conferenceinfo': {}, 'divisioninfo': {}, 'teaminfo': {} } };
 leaguelist = [];
 for leagueinfo in getleague:
  leaguearray = {};
  HockeyLeagueHasDivisions = True;
  HockeyLeagueHasDivisionStr = "yes";
  if(int(leagueinfo[7])<=0):
   HockeyLeagueHasDivisions = False;
   HockeyLeagueHasDivisionStr = "no";
  HockeyLeagueHasConferences = True;
  HockeyLeagueHasConferenceStr = "yes";
  if(int(leagueinfo[8])<=0):
   HockeyLeagueHasConferences = False;
   HockeyLeagueHasConferenceStr = "no";
  tempdict = { 'leagueinfo': { 'name': str(leagueinfo[0]), 'fullname': str(leagueinfo[1]), 'country': str(leagueinfo[2]), 'fullcountry': str(leagueinfo[3]), 'date': str(leagueinfo[4]), 'playofffmt': str(leagueinfo[5]), 'ordertype': str(leagueinfo[6]), 'conferences': str(HockeyLeagueHasConferenceStr), 'divisions': str(HockeyLeagueHasDivisionStr) } };
  leaguearray.update( { str(leagueinfo[0]): tempdict } );
  leaguelist.append(str(leagueinfo[0]));
  if(verbose is True):
   VerbosePrintOut(" <league name=\""+EscapeXMLString(str(leagueinfo[0]), quote=True)+"\" fullname=\""+EscapeXMLString(str(leagueinfo[1]), quote=True)+"\" country=\""+EscapeXMLString(str(leagueinfo[2]), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(leagueinfo[3]), quote=True)+"\" date=\""+EscapeXMLString(str(leagueinfo[4]), quote=True)+"\" playofffmt=\""+EscapeXMLString(str(leagueinfo[5]), quote=True)+"\" ordertype=\""+EscapeXMLString(str(leagueinfo[6]), quote=True)+"\" conferences=\""+EscapeXMLString(str(HockeyLeagueHasConferenceStr), quote=True)+"\" divisions=\""+EscapeXMLString(str(HockeyLeagueHasDivisionStr), quote=True)+"\">");
  conferencecur = sqldatacon[1].cursor();
  getconference_num = conferencecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Conferences WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\"").fetchone()[0];
  getconference = conferencecur.execute("SELECT Conference FROM "+leagueinfo[0]+"Conferences WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\"");
  conferencelist = [];
  for conferenceinfo in getconference:
   leaguearray[str(leagueinfo[0])].update( { str(conferenceinfo[0]): { 'conferenceinfo': { 'name': str(conferenceinfo[0]), 'league': str(leagueinfo[0]) } } } );
   leaguearrayout['quickinfo']['conferenceinfo'].update( { str(conferenceinfo[0]): { 'league': str(leagueinfo[0]) } } );
   conferencelist.append(str(conferenceinfo[0]));
   if(verbose is True):
    VerbosePrintOut("  <conference name=\""+str(conferenceinfo[0])+"\">");
   divisioncur = sqldatacon[1].cursor();
   getdivision_num = divisioncur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Divisions WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\"").fetchone()[0];
   getdivision = divisioncur.execute("SELECT Division FROM "+leagueinfo[0]+"Divisions WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\"");
   divisionlist = [];
   for divisioninfo in getdivision:
    leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update( { str(divisioninfo[0]): { 'divisioninfo': { 'name': str(divisioninfo[0]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]) } } } );
    leaguearrayout['quickinfo']['divisioninfo'].update( { str(divisioninfo[0]): { 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]) } } );
    divisionlist.append(str(divisioninfo[0]));
    if(verbose is True):
     VerbosePrintOut("   <division name=\""+EscapeXMLString(str(divisioninfo[0]), quote=True)+"\">");
    teamcur = sqldatacon[1].cursor();
    getteam_num = teamcur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Teams WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"").fetchone()[0];
    getteam = teamcur.execute("SELECT CityName, AreaName, FullAreaName, CountryName, FullCountryName, TeamName, ArenaName, TeamPrefix, TeamSuffix FROM "+leagueinfo[0]+"Teams WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"");
    teamlist = [];
    for teaminfo in getteam:
     leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(divisioninfo[0])].update( { str(teaminfo[5]): { 'teaminfo': { 'city': str(teaminfo[0]), 'area': str(teaminfo[1]), 'fullarea': str(teaminfo[2]), 'country': str(teaminfo[3]), 'fullcountry': str(teaminfo[4]), 'name': str(teaminfo[5]), 'arena': str(teaminfo[6]), 'prefix': str(teaminfo[7]), 'suffix': str(teaminfo[8]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0]) } } } );
     leaguearrayout['quickinfo']['teaminfo'].update( { str(teaminfo[5]): { 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0]) } } );
     teamlist.append(str(teaminfo[5]));
     if(verbose is True):
      VerbosePrintOut("    <team city=\""+EscapeXMLString(str(teaminfo[0]), quote=True)+"\" area=\""+EscapeXMLString(str(teaminfo[1]), quote=True)+"\" fullarea=\""+EscapeXMLString(str(teaminfo[2]), quote=True)+"\" country=\""+EscapeXMLString(str(teaminfo[3]), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(teaminfo[4]), quote=True)+"\" name=\""+EscapeXMLString(str(teaminfo[5]), quote=True)+"\" arena=\""+EscapeXMLString(str(teaminfo[6]), quote=True)+"\" prefix=\""+EscapeXMLString(str(teaminfo[7]), quote=True)+"\" suffix=\""+EscapeXMLString(str(teaminfo[8]), quote=True)+"\" />");
    teamcur.close();
    leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(divisioninfo[0])].update( { 'teamlist': teamlist } );
    if(verbose is True):
     VerbosePrintOut("   </division>");
   divisioncur.close();
   leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update( { 'divisionlist': divisionlist } );
   if(verbose is True):
    VerbosePrintOut("  </conference>");
  conferencecur.close();
  leaguearray[str(leagueinfo[0])].update( { 'conferencelist': conferencelist } );
  arenacur = sqldatacon[1].cursor();
  getteam_num = arenacur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Arenas WHERE TeamID=0").fetchone()[0];
  getarena = arenacur.execute("SELECT CityName, AreaName, FullAreaName, CountryName, FullCountryName, ArenaName FROM "+leagueinfo[0]+"Arenas WHERE TeamID=0");
  arenalist = [];
  if(getteam_num>0):
   for arenainfo in getarena:
    if(verbose is True):
     VerbosePrintOut("   <arena city=\""+EscapeXMLString(str(arenainfo[0]), quote=True)+"\" area=\""+EscapeXMLString(str(arenainfo[1]), quote=True)+"\" fullarea=\""+EscapeXMLString(str(arenainfo[2]), quote=True)+"\" country=\""+EscapeXMLString(str(arenainfo[3]), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(arenainfo[4]), quote=True)+"\" name=\""+EscapeXMLString(str(arenainfo[5]), quote=True)+"\" />");
    arenalist.append( { 'city': str(arenainfo[0]), 'area': str(arenainfo[1]), 'fullarea': str(arenainfo[2]), 'country': str(arenainfo[3]), 'fullcountry': str(arenainfo[4]), 'name': str(arenainfo[5]) } );
    if(verbose is True):
     VerbosePrintOut("   <arena city=\""+EscapeXMLString(str(arenainfo[0]), quote=True)+"\" area=\""+EscapeXMLString(str(arenainfo[1]), quote=True)+"\" fullarea=\""+EscapeXMLString(str(arenainfo[2]), quote=True)+"\" country=\""+EscapeXMLString(str(arenainfo[3]), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(arenainfo[4]), quote=True)+"\" name=\""+EscapeXMLString(str(arenainfo[5]), quote=True)+"\" />");
   if(verbose is True):
    VerbosePrintOut("  </arenas>");
  leaguearray[str(leagueinfo[0])].update( { "arenas": arenalist } );
  gamecur = sqldatacon[1].cursor();
  getgame_num = gamecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Games").fetchone()[0];
  getgame = gamecur.execute("SELECT Date, HomeTeam, AwayTeam, TeamScorePeriods, ShotsOnGoal, PowerPlays, ShortHanded, Penalties, PenaltyMinutes, HitsPerPeriod, TakeAways, FaceoffWins, AtArena, IsPlayOffGame FROM "+leagueinfo[0]+"Games");
  gamelist = [];
  if(getgame_num>0):
   if(verbose is True):
    VerbosePrintOut("  <games>");
   for gameinfo in getgame:
    AtArena = gameinfo[12];
    if(GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[1]), "FullArenaName", "str")==AtArena):
     AtArena = "0";
    if(GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[2]), "FullArenaName", "str")==AtArena):
     AtArena = "1";
    gamelist.append( { 'date': str(gameinfo[0]), 'hometeam': str(gameinfo[1]), 'awayteam': str(gameinfo[2]), 'goals': str(gameinfo[3]), 'sogs': str(gameinfo[4]), 'ppgs': str(gameinfo[5]), 'shgs': str(gameinfo[6]), 'penalties': str(gameinfo[7]), 'pims': str(gameinfo[8]), 'hits': str(gameinfo[9]), 'takeaways': str(gameinfo[10]), 'faceoffwins': str(gameinfo[11]), 'atarena': str(AtArena), 'isplayoffgame': str(gameinfo[13]) } );
    if(verbose is True):
     VerbosePrintOut("   <game date=\""+EscapeXMLString(str(gameinfo[0]), quote=True)+"\" hometeam=\""+EscapeXMLString(str(gameinfo[1]), quote=True)+"\" awayteam=\""+EscapeXMLString(str(gameinfo[2]), quote=True)+"\" goals=\""+EscapeXMLString(str(gameinfo[3]), quote=True)+"\" sogs=\""+EscapeXMLString(str(gameinfo[4]), quote=True)+"\" ppgs=\""+EscapeXMLString(str(gameinfo[5]), quote=True)+"\" shgs=\""+EscapeXMLString(str(gameinfo[6]), quote=True)+"\" penalties=\""+EscapeXMLString(str(gameinfo[7]), quote=True)+"\" pims=\""+EscapeXMLString(str(gameinfo[8]), quote=True)+"\" hits=\""+EscapeXMLString(str(gameinfo[9]), quote=True)+"\" takeaways=\""+EscapeXMLString(str(gameinfo[10]), quote=True)+"\" faceoffwins=\""+EscapeXMLString(str(gameinfo[11]), quote=True)+"\" atarena=\""+EscapeXMLString(str(AtArena), quote=True)+"\" isplayoffgame=\""+EscapeXMLString(str(gameinfo[13]), quote=True)+"\" />");
   if(verbose is True):
    VerbosePrintOut("  </games>");
  leaguearray[str(leagueinfo[0])].update( { "games": gamelist } );
  leaguearrayout.update(leaguearray);
  if(verbose is True):
   VerbosePrintOut(" </league>");
 leaguearrayout.update( { 'leaguelist': leaguelist } );
 if(verbose is True):
  VerbosePrintOut("</hockey>");
 leaguecur.close();
 sqldatacon[1].close();
 return leaguearrayout;

def MakeHockeyJSONFromHockeySQL(sqlfile, sdbfile=None, sqlisfile=True, returnjson=False, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeySQL(sqlfile, sdbfile, sqlisfile, False);
 jsonstring = MakeHockeyJSONFromHockeyArray(hockeyarray, returnjson, verbose);
 if(verbose is True):
  VerbosePrintOut(jsonstring);
 return jsonstring;

def MakeHockeySQLFromHockeyArray(inhockeyarray, verbose=True):
 sqldatacon = MakeHockeyDatabase(":memory:");
 leaguecount = 0;
 for hlkey in inhockeyarray['leaguelist']:
  if(leaguecount==0):
   MakeHockeyLeagueTable(sqldatacon);
  MakeHockeyTeamTable(sqldatacon, hlkey);
  MakeHockeyConferenceTable(sqldatacon, hlkey);
  MakeHockeyGameTable(sqldatacon, hlkey);
  MakeHockeyDivisionTable(sqldatacon, hlkey);
  HockeyLeagueHasDivisions = True;
  if(inhockeyarray[hlkey]['leagueinfo']['conferences'].lower()=="no"):
   HockeyLeagueHasDivisions = False;
  HockeyLeagueHasConferences = True;
  if(inhockeyarray[hlkey]['leagueinfo']['divisions'].lower()=="no"):
   HockeyLeagueHasConferences = False;
  MakeHockeyLeagues(sqldatacon, hlkey, inhockeyarray[hlkey]['leagueinfo']['fullname'], inhockeyarray[hlkey]['leagueinfo']['country'], inhockeyarray[hlkey]['leagueinfo']['fullcountry'], inhockeyarray[hlkey]['leagueinfo']['date'], inhockeyarray[hlkey]['leagueinfo']['playofffmt'], inhockeyarray[hlkey]['leagueinfo']['ordertype']);
  for hckey in inhockeyarray[hlkey]['conferencelist']:
   MakeHockeyConferences(sqldatacon, hlkey, hckey, HockeyLeagueHasConferences);
   for hdkey in inhockeyarray[hlkey][hckey]['divisionlist']:
    MakeHockeyDivisions(sqldatacon, hlkey, hdkey, hckey, HockeyLeagueHasConferences, HockeyLeagueHasDivisions);
    for htkey in inhockeyarray[hlkey][hckey][hdkey]['teamlist']:
     MakeHockeyTeams(sqldatacon, hlkey, str(inhockeyarray[hlkey]['leagueinfo']['date']), inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea'], htkey, hckey, hdkey, inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix'], HockeyLeagueHasConferences, HockeyLeagueHasDivisions);
   hasarenas = False;
   for hakey in inhockeyarray[hlkey]['arenas']:
    if(hakey is True):
     hasarenas = True;
     MakeHockeyArena(sqldatacon, hlkey, hakey['city'], hakey['area'], hakey['country'], hakey['fullcountry'], hakey['fullarea'], hakey['name']);
   hasgames = False;
   for hgkey in inhockeyarray[hlkey]['games']:
    if(hgkey is True):
     hasgames = True;
     MakeHockeyGame(sqldatacon, hlkey, hgkey['date'], hgkey['hometeam'], hgkey['awayteam'], hgkey['goals'], hgkey['sogs'], hgkey['ppgs'], hgkey['shgs'], hgkey['penalties'], hgkey['pims'], hgkey['hits'], hgkey['takeaways'], hgkey['faceoffwins'], hgkey['atarena'], hgkey['isplayoffgame']);
 sqldump = "-- "+__program_name__+" SQL Dumper\n";
 sqldump = sqldump+"-- version "+__version__+"\n";
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
 if(verbose is True):
  VerbosePrintOut("-- "+__program_name__+" SQL Dumper\n");
  VerbosePrintOut("-- version "+__version__+"\n");
  VerbosePrintOut("-- "+__project_url__+"\n");
  VerbosePrintOut("--\n");
  VerbosePrintOut("-- Generation Time: "+time.strftime("%B %d, %Y at %I:%M %p", time.localtime())+"\n");
  VerbosePrintOut("-- SQLite Server version: "+sqlite3.sqlite_version+"\n");
  VerbosePrintOut("-- PySQLite version: "+sqlite3.version+"\n");
  VerbosePrintOut("-- Python Version: "+str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2])+"\n\n");
  VerbosePrintOut("--\n");
  VerbosePrintOut("-- Database: :memory:\n");
  VerbosePrintOut("--\n\n");
  VerbosePrintOut("-- --------------------------------------------------------\n\n");
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
  sqldump = sqldump+"DROP TABLE IF EXISTS "+get_cur_tab+";\n\n"+tabresult+";\n\n";
  sqldump = sqldump+"--\n";
  sqldump = sqldump+"-- Dumping data for table "+str(get_cur_tab)+"\n";
  sqldump = sqldump+"--\n\n";
  if(verbose is True):
   VerbosePrintOut(" ");
   VerbosePrintOut("--");
   VerbosePrintOut("-- Table structure for table "+str(get_cur_tab)+"");
   VerbosePrintOut("--");
   VerbosePrintOut(" ");
   VerbosePrintOut("DROP TABLE IF EXISTS "+get_cur_tab+";\n\n"+tabresult+";");
   VerbosePrintOut(" ");
   VerbosePrintOut("--");
   VerbosePrintOut("-- Dumping data for table "+str(get_cur_tab)+"");
   VerbosePrintOut("--");
   VerbosePrintOut(" ");
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
    if(isinstance(result_val, float)):
     get_insert_stmt_val += ""+str(result_val)+", ";
   get_insert_stmt = get_insert_stmt[:-2]+") VALUES \n";
   if(verbose is True):
    VerbosePrintOut(get_insert_stmt[:-2]+") VALUES ");
   get_insert_stmt_val = get_insert_stmt_val[:-2]+");";
   if(verbose is True):
    VerbosePrintOut(get_insert_stmt_val[:-2]+");");
   get_insert_stmt_full += str(get_insert_stmt+get_insert_stmt_val)+"\n";
  sqldump = sqldump+get_insert_stmt_full+"\n-- --------------------------------------------------------\n\n";
  if(verbose is True):
   VerbosePrintOut("-- --------------------------------------------------------");
   VerbosePrintOut(" ");
 CloseHockeyDatabase(sqldatacon);
 return sqldump;

def MakeHockeySQLFileFromHockeyArray(inhockeyarray, sqlfile=None, returnsql=False, verbose=True):
 if(sqlfile is None):
  return False;
 sqlfp = open(sqlfile, "w+");
 sqlstring = MakeHockeySQLFromHockeyArray(inhockeyarray, verbose);
 sqlfp.write(sqlstring);
 sqlfp.close();
 if(returnsql is True):
  return sqlstring;
 if(returnsql is False):
  return True;
 return True;

def MakeHockeyArrayFromOldHockeyDatabase(sdbfile, verbose=True):
 if(os.path.exists(sdbfile) and os.path.isfile(sdbfile) and isinstance(sdbfile, str)):
  sqldatacon = OpenHockeyDatabase(sdbfile);
 else:
  if(sdbfile is not None and isinstance(sdbfile, (tuple, list))):
   sqldatacon = tuple(sdbfile);
  else:
   return False;
 leaguecur = sqldatacon[1].cursor();
 if(verbose is True):
  VerbosePrintOut("<?xml version=\"1.0\" encoding=\"UTF-8\"?>");
  VerbosePrintOut("<hockey database=\""+EscapeXMLString(str(sdbfile), quote=True)+"\">");
 gettablecur = sqldatacon[1].cursor();
 gettable_num = gettablecur.execute("SELECT COUNT(*) FROM sqlite_master WHERE type=\"table\" and name LIKE \"%Teams\"").fetchone()[0];
 gettable = gettablecur.execute("SELECT name FROM sqlite_master WHERE type=\"table\" and name LIKE \"%Teams\"");
 mktemptablecur = sqldatacon[1].cursor();
 mktemptablecur.execute("CREATE TEMP TABLE HockeyLeagues (\n" + \
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
 for tableinfo in gettable:
  LeagueName = re.sub("Teams$", "", tableinfo[0]);
  LeagueNameInfo = GetHockeyLeaguesInfo(LeagueName);
  getconference_num = mktemptablecur.execute("SELECT COUNT(*) FROM "+LeagueName+"Conferences").fetchone()[0];
  getdivision_num = mktemptablecur.execute("SELECT COUNT(*) FROM "+LeagueName+"Divisions").fetchone()[0];
  getteam_num = mktemptablecur.execute("SELECT COUNT(*) FROM "+LeagueName+"Teams").fetchone()[0];
  getallteam_num = getteam_num;
  mktemptablecur.execute("INSERT INTO HockeyLeagues (LeagueName, LeagueFullName, CountryName, FullCountryName, Date, PlayOffFMT, OrderType, NumberOfTeams, NumberOfConferences, NumberOfDivisions) VALUES \n" + \
  "(\""+str(LeagueNameInfo['LeagueName'])+"\", \""+str(LeagueNameInfo['FullLeagueName'])+"\", \""+str(LeagueNameInfo['CountryName'])+"\", \""+str(LeagueNameInfo['FullCountryName'])+"\", "+str(LeagueNameInfo['StartDate'])+", \""+str(LeagueNameInfo['PlayOffFMT'])+"\", \""+str(LeagueNameInfo['OrderType'])+"\", "+str(getteam_num)+", "+str(getconference_num)+", "+str(getdivision_num)+")");
 gettablecur.close();
 getleague_num = leaguecur.execute("SELECT COUNT(*) FROM HockeyLeagues").fetchone()[0];
 getleague = leaguecur.execute("SELECT LeagueName, LeagueFullName, CountryName, FullCountryName, Date, PlayOffFMT, OrderType, NumberOfTeams, NumberOfConferences, NumberOfDivisions FROM HockeyLeagues");
 leaguearrayout = { 'database': str(sdbfile), 'quickinfo': {'conferenceinfo': {}, 'divisioninfo': {}, 'teaminfo': {} } };
 leaguelist = [];
 for leagueinfo in getleague:
  leaguearray = {};
  HockeyLeagueHasDivisions = True;
  HockeyLeagueHasDivisionStr = "yes";
  if(int(leagueinfo[7])<=0):
   HockeyLeagueHasDivisions = False;
   HockeyLeagueHasDivisionStr = "no";
  HockeyLeagueHasConferences = True;
  HockeyLeagueHasConferenceStr = "yes";
  if(int(leagueinfo[8])<=0):
   HockeyLeagueHasConferences = False;
   HockeyLeagueHasConferenceStr = "no";
  tempdict = { 'leagueinfo': { 'name': str(leagueinfo[0]), 'fullname': str(leagueinfo[1]), 'country': str(leagueinfo[2]), 'fullcountry': str(leagueinfo[3]), 'date': str(leagueinfo[4]), 'playofffmt': str(leagueinfo[5]), 'ordertype': str(leagueinfo[6]), 'conferences': str(HockeyLeagueHasConferenceStr), 'divisions': str(HockeyLeagueHasDivisionStr) } };
  leaguearray.update( { str(leagueinfo[0]): tempdict } );
  leaguelist.append(str(leagueinfo[0]));
  if(verbose is True):
   VerbosePrintOut(" <league name=\""+EscapeXMLString(str(leagueinfo[0]), quote=True)+"\" fullname=\""+EscapeXMLString(str(leagueinfo[1]), quote=True)+"\" country=\""+EscapeXMLString(str(leagueinfo[2]), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(leagueinfo[3]), quote=True)+"\" date=\""+EscapeXMLString(str(leagueinfo[4]), quote=True)+"\" playofffmt=\""+EscapeXMLString(str(leagueinfo[5]), quote=True)+"\" ordertype=\""+EscapeXMLString(str(leagueinfo[6]), quote=True)+"\" conferences=\""+EscapeXMLString(str(HockeyLeagueHasConferenceStr), quote=True)+"\" divisions=\""+EscapeXMLString(str(HockeyLeagueHasDivisionStr), quote=True)+"\">");
  conferencecur = sqldatacon[1].cursor();
  getconference_num = conferencecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Conferences").fetchone()[0];
  getconference = conferencecur.execute("SELECT Conference FROM "+leagueinfo[0]+"Conferences");
  conferencelist = [];
  for conferenceinfo in getconference:
   leaguearray[str(leagueinfo[0])].update( { str(conferenceinfo[0]): { 'conferenceinfo': { 'name': str(conferenceinfo[0]), 'league': str(leagueinfo[0]) } } } );
   leaguearrayout['quickinfo']['conferenceinfo'].update( { str(conferenceinfo[0]): { 'league': str(leagueinfo[0]) } } );
   conferencelist.append(str(conferenceinfo[0]));
   if(verbose is True):
    VerbosePrintOut("  <conference name=\""+EscapeXMLString(str(conferenceinfo[0]), quote=True)+"\">");
   divisioncur = sqldatacon[1].cursor();
   getdivision_num = divisioncur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Divisions WHERE Conference=\""+conferenceinfo[0]+"\"").fetchone()[0];
   getdivision = divisioncur.execute("SELECT Division FROM "+leagueinfo[0]+"Divisions WHERE Conference=\""+conferenceinfo[0]+"\"");
   divisionlist = [];
   for divisioninfo in getdivision:
    leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update( { str(divisioninfo[0]): { 'divisioninfo': { 'name': str(divisioninfo[0]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]) } } } );
    leaguearrayout['quickinfo']['divisioninfo'].update( { str(divisioninfo[0]): { 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]) } } );
    divisionlist.append(str(divisioninfo[0]));
    if(verbose is True):
     VerbosePrintOut("   <division name=\""+EscapeXMLString(str(divisioninfo[0]), quote=True)+"\">");
    teamcur = sqldatacon[1].cursor();
    getteam_num = teamcur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Teams WHERE Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"").fetchone()[0];
    getteam = teamcur.execute("SELECT CityName, AreaName, TeamName, ArenaName, TeamPrefix FROM "+leagueinfo[0]+"Teams WHERE Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"");
    teamlist = [];
    for teaminfo in getteam:
     TeamAreaInfo = GetAreaInfoFromUSCA(teaminfo[1]);
     leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(divisioninfo[0])].update( { str(teaminfo[2]): { 'teaminfo': { 'city': str(teaminfo[0]), 'area': str(TeamAreaInfo['AreaName']), 'fullarea': str(TeamAreaInfo['FullAreaName']), 'country': str(TeamAreaInfo['CountryName']), 'fullcountry': str(TeamAreaInfo['FullCountryName']), 'name': str(teaminfo[2]), 'arena': str(teaminfo[3]), 'prefix': str(teaminfo[4]), 'suffix': "", 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0]) } } } );
     leaguearrayout['quickinfo']['teaminfo'].update( { str(teaminfo[2]): { 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0]) } } );
     teamlist.append(str(teaminfo[5]));
     if(verbose is True):
      VerbosePrintOut("    <team city=\""+EscapeXMLString(str(teaminfo[0]), quote=True)+"\" area=\""+EscapeXMLString(str(TeamAreaInfo['AreaName']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(TeamAreaInfo['FullAreaName']), quote=True)+"\" country=\""+EscapeXMLString(str(TeamAreaInfo['CountryName']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(TeamAreaInfo['FullCountryName']), quote=True)+"\" name=\""+EscapeXMLString(str(teaminfo[2]), quote=True)+"\" arena=\""+EscapeXMLString(str(teaminfo[3]), quote=True)+"\" prefix=\""+EscapeXMLString(str(teaminfo[4]), quote=True)+"\" suffix=\"\" />");
    teamcur.close();
    leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(divisioninfo[0])].update( { 'teamlist': teamlist } );
    if(verbose is True):
     VerbosePrintOut("   </division>");
   divisioncur.close();
   leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update( { 'divisionlist': divisionlist } );
   if(verbose is True):
    VerbosePrintOut("  </conference>");
  conferencecur.close();
  leaguearray[str(leagueinfo[0])].update( { 'conferencelist': conferencelist } );
  arenacur = sqldatacon[1].cursor();
  getteam_num = arenacur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Arenas WHERE id>"+str(getallteam_num)).fetchone()[0];
  getarena = arenacur.execute("SELECT CityName, AreaName, ArenaName FROM "+leagueinfo[0]+"Arenas WHERE id>"+str(getallteam_num));
  arenalist = [];
  if(getteam_num>0):
   if(verbose is True):
    VerbosePrintOut("  <arenas>");
   for arenainfo in getarena:
    ArenaAreaInfo = GetAreaInfoFromUSCA(arenainfo[1]);
    arenalist.append( { 'city': str(arenainfo[0]), 'area': str(ArenaAreaInfo['AreaName']), 'fullarea': str(ArenaAreaInfo['FullAreaName']), 'country': str(ArenaAreaInfo['CountryName']), 'fullcountry': str(ArenaAreaInfo['FullCountryName']), 'name': str(arenainfo[2]) } );
    if(verbose is True):
     VerbosePrintOut("   <arena city=\""+EscapeXMLString(str(arenainfo[0]), quote=True)+"\" area=\""+EscapeXMLString(str(ArenaAreaInfo['AreaName']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(ArenaAreaInfo['FullAreaName']), quote=True)+"\" country=\""+EscapeXMLString(str(ArenaAreaInfo['CountryName']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(ArenaAreaInfo['FullCountryName']), quote=True)+"\" name=\""+EscapeXMLString(str(arenainfo[2]), quote=True)+"\" />");
   if(verbose is True):
    VerbosePrintOut("  </arenas>");
  leaguearray[str(leagueinfo[0])].update( { "arenas": arenalist } );
  gamecur = sqldatacon[1].cursor();
  getgame_num = gamecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Games").fetchone()[0];
  getgame = gamecur.execute("SELECT Date, HomeTeam, AwayTeam, TeamScorePeriods, ShotsOnGoal, AtArena, IsPlayOffGame FROM "+leagueinfo[0]+"Games");
  gamelist = [];
  if(getgame_num>0):
   if(verbose is True):
    VerbosePrintOut("  <games>");
   for gameinfo in getgame:
    GetNumPeriods = len(gameinfo[3].split(","));
    EmptyScore = ",0:0" * (GetNumPeriods - 1);
    EmptyScore = "0:0"+EmptyScore;
    AtArena = gameinfo[5];
    if(GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[1]), "FullArenaName", "str")==AtArena):
     AtArena = "0";
    if(GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[2]), "FullArenaName", "str")==AtArena):
     AtArena = "1";
    gamelist.append( { 'date': str(gameinfo[0]), 'hometeam': str(gameinfo[1]), 'awayteam': str(gameinfo[2]), 'goals': str(gameinfo[3]), 'sogs': str(gameinfo[4]), 'ppgs': str(EmptyScore), 'shgs': str(EmptyScore), 'penalties': str(EmptyScore), 'pims': str(EmptyScore), 'hits': str(EmptyScore), 'takeaways': str(EmptyScore), 'faceoffwins': str(EmptyScore), 'atarena': str(AtArena), 'isplayoffgame': str(gameinfo[6]) } );
    if(verbose is True):
     VerbosePrintOut("   <game date=\""+EscapeXMLString(str(gameinfo[0]), quote=True)+"\" hometeam=\""+EscapeXMLString(str(gameinfo[1]), quote=True)+"\" awayteam=\""+EscapeXMLString(str(gameinfo[2]), quote=True)+"\" goals=\""+EscapeXMLString(str(gameinfo[3]), quote=True)+"\" sogs=\""+EscapeXMLString(str(gameinfo[4]), quote=True)+"\" ppgs=\""+EscapeXMLString(str(EmptyScore), quote=True)+"\" shgs=\""+EscapeXMLString(str(EmptyScore), quote=True)+"\" penalties=\""+EscapeXMLString(str(EmptyScore), quote=True)+"\" pims=\""+EscapeXMLString(str(EmptyScore), quote=True)+"\" hits=\""+EscapeXMLString(str(EmptyScore), quote=True)+"\" takeaways=\""+EscapeXMLString(str(EmptyScore), quote=True)+"\" faceoffwins=\""+EscapeXMLString(str(EmptyScore), quote=True)+"\" atarena=\""+EscapeXMLString(str(AtArena), quote=True)+"\" isplayoffgame=\""+EscapeXMLString(str(gameinfo[6]), quote=True)+"\" />");
   if(verbose is True):
    VerbosePrintOut("  </games>");
  leaguearray[str(leagueinfo[0])].update( { "games": gamelist } );
  leaguearrayout.update(leaguearray);
  if(verbose is True):
   VerbosePrintOut(" </league>");
 leaguearrayout.update( { 'leaguelist': leaguelist } );
 if(verbose is True):
  VerbosePrintOut("</hockey>");
 leaguecur.close();
 sqldatacon[1].close();
 return leaguearrayout;

def MakeHockeyJSONFromOldHockeyDatabase(sdbfile, returnjson=False, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(sdbfile, False);
 jsonstring = MakeHockeyJSONFromHockeyArray(hockeyarray, returnjson, verbose);
 if(verbose is True):
  VerbosePrintOut(jsonstring);
 return jsonstring;

def MakeHockeyDatabaseFromHockeyXML(xmlfile, sdbfile=None, xmlisfile=True, returnxml=False, returndb=False, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(xmlfile, xmlisfile, False);
 hockeydbout = MakeHockeyDatabaseFromHockeyArray(hockeyarray, sdbfile, returnxml, returndb, verbose);
 return hockeydbout;

def MakeHockeyDatabaseFromHockeyXMLWrite(inxmlfile, sdbfile=None, outxmlfile=None, xmlisfile=True, returnxml=False, verbose=True):
 if(xmlisfile is True and (not os.path.exists(inxmlfile) or not os.path.isfile(inxmlfile))):
  return False;
 if(outxmlfile is None and xmlisfile is True):
  file_wo_extension, file_extension = os.path.splitext(inxmlfile);
  outxmlfile = file_wo_extension+".xml";
 xmlfp = open(outxmlfile, "w+");
 xmlstring = MakeHockeyDatabaseFromHockeyXML(inxmlfile, sdbfile, xmlisfile, True, False, verbose);
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml is True):
  return xmlstring;
 if(returnxml is False):
  return True;
 return True;

def MakeHockeyDatabaseFromHockeySQL(sqlfile, sdbfile=None, sqlisfile=True, returnsql=False, returndb=False, verbose=True):
 if(sqlisfile is True and (os.path.exists(sqlfile) and os.path.isfile(sqlfile))):
  sqlfp = open(sqlfile, "r");
  sqlstring = sqlfp.read();
  sqlfp.close();
 elif(sqlisfile is False):
  sqlstring = sqlfile;
 else:
  return False;
 if(sdbfile is None and len(re.findall(r"Database\:([\w\W]+)", "-- Database: ./hockey17-18.db3"))>=1):
  sdbfile = re.findall(r"Database\:([\w\W]+)", "-- Database: ./hockey17-18.db3")[0].strip();
 if(sdbfile is None and len(re.findall(r"Database\:([\w\W]+)", "-- Database: ./hockey17-18.db3"))<1):
  file_wo_extension, file_extension = os.path.splitext(sqlfile);
  sdbfile = file_wo_extension+".db3";
 if(sdbfile is not None and isinstance(sdbfile, str)):
  sqldatacon = MakeHockeyDatabase(sdbfile);
 if(sdbfile is not None and isinstance(sdbfile, (tuple, list))):
  sqldatacon = tuple(sdbfile);
 if(verbose is True):
  VerbosePrintOut(sqlstring);
 sqldatacon[0].executescript(sqlstring);
 if(returndb is False):
  CloseHockeyDatabase(sqldatacon);
 if(returndb is True and returnsql is False):
  return sqldatacon;
 if(returnsql is True and returndb is False):
  return sqlstring;
 if(returnsql is True and returndb is True):
  return [sqlstring, sqldatacon];
 if(returnsql is False):
  return True;
 return True;

def MakeHockeyDatabaseFromHockeySQLWrite(insqlfile, sdbfile=None, outsqlfile=None, sqlisfile=True, returnsql=False, verbose=True):
 if(sqlisfile is True and (not os.path.exists(insqlfile) or not os.path.isfile(insqlfile))):
  return False;
 if(outsqlfile is None and sqlisfile is True):
  file_wo_extension, file_extension = os.path.splitext(insqlfile);
  outsqlfile = file_wo_extension+".db3";
 sqlfp = open(outsqlfile, "w+");
 sqlstring = MakeHockeyDatabaseFromHockeySQL(insqlfile, sdbfile, sqlisfile, True, False, verbose);
 sqlfp.write(sqlstring);
 sqlfp.close();
 if(returnsql is True):
  return sqlstring;
 if(returnsql is False):
  return True;
 return True;

def MakeHockeyPythonFromHockeyXML(xmlfile, xmlisfile=True, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(xmlfile, xmlisfile, False);
 hockeypyout = MakeHockeyPythonFromHockeyArray(hockeyarray, True);
 return hockeypyout;

def MakeHockeyPythonFileFromHockeyXML(inxmlfile, outpyfile=None, xmlisfile=True, returnpy=False, verbose=True):
 if(xmlisfile is True and (not os.path.exists(inxmlfile) or not os.path.isfile(inxmlfile))):
  return False;
 if(outpyfile is None and xmlisfile is True):
  file_wo_extension, file_extension = os.path.splitext(inxmlfile);
  outpyfile = file_wo_extension+".xml";
 pyfp = open(outpyfile, "w+");
 pystring = MakeHockeyPythonFromHockeyXML(inxmlfile, xmlisfile, verbose);
 pyfp.write(pystring);
 pyfp.close();
 if(returnpy is True):
  return pystring;
 if(returnpy is False):
  return True;
 return True;

def MakeHockeyPythonAltFromHockeyXML(xmlfile, xmlisfile=True, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(xmlfile, xmlisfile, False);
 hockeypyout = MakeHockeyPythonAltFromHockeyArray(hockeyarray, True);
 return hockeypyout;

def MakeHockeyPythonAltFileFromHockeyXML(inxmlfile, outpyfile=None, xmlisfile=True, returnpy=False, verbose=True):
 if(xmlisfile is True and (not os.path.exists(inxmlfile) or not os.path.isfile(inxmlfile))):
  return False;
 if(outpyfile is None and xmlisfile is True):
  file_wo_extension, file_extension = os.path.splitext(inxmlfile);
  outpyfile = file_wo_extension+".xml";
 pyfp = open(outpyfile, "w+");
 pystring = MakeHockeyPythonAltFromHockeyXML(inxmlfile, xmlisfile, verbose);
 pyfp.write(pystring);
 pyfp.close();
 if(returnpy is True):
  return pystring;
 if(returnpy is False):
  return True;
 return True;

def MakeHockeyXMLFromHockeyDatabase(sdbfile, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(sdbfile, False);
 hockeyxmlout = MakeHockeyXMLFromHockeyArray(hockeyarray, verbose);
 return hockeyxmlout;

def MakeHockeyXMLFileFromHockeyDatabase(sdbfile, xmlfile=None, returnxml=False, verbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(xmlfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  xmlfile = file_wo_extension+".xml";
 xmlfp = open(xmlfile, "w+");
 xmlstring = MakeHockeyXMLFromHockeyDatabase(sdbfile, verbose);
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml is True):
  return xmlstring;
 if(returnxml is False):
  return True;
 return True;

def MakeHockeyXMLFromHockeySQL(sqlfile, sdbfile=None, sqlisfile=True, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeySQL(sqlfile, sdbfile, sqlisfile, False);
 hockeyxmlout = MakeHockeyXMLFromHockeyArray(hockeyarray, verbose);
 return hockeyxmlout;

def MakeHockeyXMLFileFromHockeySQL(insqlfile, sdbfile=None, outxmlfile=None, sqlisfile=True, returnxml=False, verbose=True):
 if(sqlisfile is True and (not os.path.exists(insqlfile) or not os.path.isfile(insqlfile))):
  return False;
 if(outxmlfile is None and sqlisfile is True):
  file_wo_extension, file_extension = os.path.splitext(insqlfile);
  outxmlfile = file_wo_extension+".xml";
 sqlfp = open(outxmlfile, "w+");
 xmlstring = MakeHockeyXMLFromHockeySQL(insqlfile, sdbfile, sqlisfile, verbose);
 sqlfp.write(xmlstring);
 sqlfp.close();
 if(returnxml is True):
  return xmlstring;
 if(returnxml is False):
  return True;
 return True;

def MakeHockeyPythonFromHockeyDatabase(sdbfile, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(sdbfile, False);
 hockeypyout = MakeHockeyPythonFromHockeyArray(hockeyarray, verbose);
 return hockeypyout;

def MakeHockeyPythonFileFromHockeyDatabase(sdbfile, pyfile=None, returnpy=False, verbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(pyfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  pyfile = file_wo_extension+".xml";
 pyfp = open(pyfile, "w+");
 pystring = MakeHockeyPythonFromHockeyDatabase(sdbfile, verbose);
 pyfp.write(pystring);
 pyfp.close();
 if(returnpy is True):
  return pystring;
 if(returnpy is False):
  return True;
 return True;

def MakeHockeyPythonAltFromHockeyDatabase(sdbfile, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(sdbfile, False);
 hockeypyout = MakeHockeyPythonAltFromHockeyArray(hockeyarray, verbose);
 return hockeypyout;

def MakeHockeyPythonAltFileFromHockeyDatabase(sdbfile, pyfile=None, returnpy=False, verbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(pyfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  pyfile = file_wo_extension+".xml";
 pyfp = open(pyfile, "w+");
 pystring = MakeHockeyPythonAltFromHockeyDatabase(sdbfile, verbose);
 pyfp.write(pystring);
 pyfp.close();
 if(returnpy is True):
  return pystring;
 if(returnpy is False):
  return True;
 return True;

def MakeHockeySQLFromHockeyDatabase(sdbfile, verbose=True):
 if(os.path.exists(sdbfile) and os.path.isfile(sdbfile) and isinstance(sdbfile, str)):
  sqldatacon = OpenHockeyDatabase(sdbfile);
 else:
  if(sdbfile is not None and isinstance(sdbfile, (tuple, list))):
   sqldatacon = tuple(sdbfile);
  else:
   return False;
 sqldump = "-- "+__program_name__+" SQL Dumper\n";
 sqldump = sqldump+"-- version "+__version__+"\n";
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
 if(verbose is True):
  VerbosePrintOut("-- "+__program_name__+" SQL Dumper\n");
  VerbosePrintOut("-- version "+__version__+"\n");
  VerbosePrintOut("-- "+__project_url__+"\n");
  VerbosePrintOut("--\n");
  VerbosePrintOut("-- Generation Time: "+time.strftime("%B %d, %Y at %I:%M %p", time.localtime())+"\n");
  VerbosePrintOut("-- SQLite Server version: "+sqlite3.sqlite_version+"\n");
  VerbosePrintOut("-- PySQLite version: "+sqlite3.version+"\n");
  VerbosePrintOut("-- Python Version: "+str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2])+"\n\n");
  VerbosePrintOut("--\n");
  VerbosePrintOut("-- Database: "+sdbfile+"\n");
  VerbosePrintOut("--\n\n");
  VerbosePrintOut("-- --------------------------------------------------------\n\n");
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
  sqldump = sqldump+"DROP TABLE IF EXISTS "+get_cur_tab+";\n\n"+tabresult+";\n\n";
  sqldump = sqldump+"--\n";
  sqldump = sqldump+"-- Dumping data for table "+str(get_cur_tab)+"\n";
  sqldump = sqldump+"--\n\n";
  if(verbose is True):
   VerbosePrintOut(" ");
   VerbosePrintOut("--");
   VerbosePrintOut("-- Table structure for table "+str(get_cur_tab)+"");
   VerbosePrintOut("--");
   VerbosePrintOut(" ");
   VerbosePrintOut("DROP TABLE IF EXISTS "+get_cur_tab+";\n\n"+tabresult+";");
   VerbosePrintOut(" ");
   VerbosePrintOut("--");
   VerbosePrintOut("-- Dumping data for table "+str(get_cur_tab)+"");
   VerbosePrintOut("--");
   VerbosePrintOut(" ");
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
    if(isinstance(result_val, float)):
     get_insert_stmt_val += ""+str(result_val)+", ";
   get_insert_stmt = get_insert_stmt[:-2]+") VALUES \n";
   if(verbose is True):
    VerbosePrintOut(get_insert_stmt[:-2]+") VALUES ");
   get_insert_stmt_val = get_insert_stmt_val[:-2]+");";
   if(verbose is True):
    VerbosePrintOut(get_insert_stmt_val[:-2]+");");
   get_insert_stmt_full += str(get_insert_stmt+get_insert_stmt_val)+"\n";
  sqldump = sqldump+get_insert_stmt_full+"\n-- --------------------------------------------------------\n\n";
  if(verbose is True):
   VerbosePrintOut(" ");
   VerbosePrintOut("-- --------------------------------------------------------");
   VerbosePrintOut(" ");
 CloseHockeyDatabase(sqldatacon);
 return sqldump;

def MakeHockeySQLFileFromHockeyDatabase(sdbfile, sqlfile=None, returnsql=False, verbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(sqlfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  sqlfile = file_wo_extension+".sql";
 sqlfp = open(sqlfile, "w+");
 sqlstring = MakeHockeySQLFromHockeyDatabase(sdbfile, verbose);
 sqlfp.write(sqlstring);
 sqlfp.close();
 if(returnsql is True):
  return sqlstring;
 if(returnsql is False):
  return True;
 return True;

def MakeHockeySQLFromHockeyXML(xmlfile, xmlisfile=True, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(xmlfile, xmlisfile, False);
 hockeysqlout = MakeHockeySQLFromHockeyArray(hockeyarray, verbose);
 return hockeysqlout;

def MakeHockeySQLFileFromHockeyXML(xmlfile, sqlfile=None, xmlisfile=True, returnsql=False, verbose=True):
 if(xmlisfile is False and (not os.path.exists(xmlfile) and not os.path.isfile(xmlfile))):
  return False;
 if(sqlfile is None and xmlisfile is True):
  file_wo_extension, file_extension = os.path.splitext(xmlfile);
  sqlfile = file_wo_extension+".sql";
 sqlfp = open(sqlfile, "w+");
 sqlstring = MakeHockeySQLFromHockeyXML(xmlfile, xmlisfile, verbose);
 sqlfp.write(sqlstring);
 sqlfp.close();
 if(returnsql is True):
  return sqlstring;
 if(returnsql is False):
  return True;
 return True;

def MakeHockeyXMLFromOldHockeyDatabase(sdbfile, verbose=True):
 hockeyarray = MakeHockeyArrayFromOldHockeyDatabase(sdbfile, False);
 hockeyxmlout = MakeHockeyXMLFromHockeyArray(hockeyarray, verbose);
 return hockeyxmlout;

def MakeHockeyXMLFileFromOldHockeyDatabase(sdbfile, xmlfile=None, returnxml=False, verbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(xmlfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  xmlfile = file_wo_extension+".xml";
 xmlfp = open(xmlfile, "w+");
 xmlstring = MakeHockeyXMLFromOldHockeyDatabase(sdbfile, verbose);
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml is True):
  return xmlstring;
 if(returnxml is False):
  return True;
 return True;

def MakeHockeyPythonFromOldHockeyDatabase(sdbfile, verbose=True):
 xmlstring = MakeHockeyXMLFromOldHockeyDatabase(sdbfile, False);
 pystring = MakeHockeyPythonFromHockeyXML(xmlstring, False, verbose);
 return pystring;

def MakeHockeyPythonFileFromOldHockeyDatabase(sdbfile, pyfile=None, returnpy=False, verbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(pyfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  pyfile = file_wo_extension+".xml";
 pyfp = open(pyfile, "w+");
 pystring = MakeHockeyPythonFromOldHockeyDatabase(sdbfile, verbose);
 pyfp.write(pystring);
 pyfp.close();
 if(returnpy is True):
  return pystring;
 if(returnpy is False):
  return True;
 return True;

def MakeHockeyPythonAltFromOldHockeyDatabase(sdbfile, verbose=True):
 xmlstring = MakeHockeyXMLFromOldHockeyDatabase(sdbfile, False);
 pystring = MakeHockeyPythonAltFromHockeyXML(xmlstring, False, verbose);
 return pystring;

def MakeHockeyPythonAltFileFromOldHockeyDatabase(sdbfile, pyfile=None, returnpy=False, verbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(pyfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  pyfile = file_wo_extension+".xml";
 pyfp = open(pyfile, "w+");
 pystring = MakeHockeyPythonAltFromOldHockeyDatabase(sdbfile, verbose);
 pyfp.write(pystring);
 pyfp.close();
 if(returnpy is True):
  return pystring;
 if(returnpy is False):
  return True;
 return True;

def MakeHockeySQLFromOldHockeyDatabase(sdbfile, verbose=True):
 xmlstring = MakeHockeyXMLFromOldHockeyDatabase(sdbfile, False);
 sqldump = MakeHockeySQLFromHockeyXML(xmlstring, False, True, verbose);
 return sqldump;

def MakeHockeySQLFileFromOldHockeyDatabase(sdbfile, sqlfile=None, returnsql=False, verbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(sqlfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  sqlfile = file_wo_extension+".sql";
 sqlfp = open(sqlfile, "w+");
 sqlstring = MakeHockeySQLFromOldHockeyDatabase(sdbfile, verbose);
 sqlfp.write(sqlstring);
 sqlfp.close();
 if(returnsql is True):
  return sqlstring;
 if(returnsql is False):
  return True;
 return True;
