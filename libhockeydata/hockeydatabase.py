#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2015-2021 Game Maker 2k - https://github.com/GameMaker2k
    Copyright 2015-2021 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: hockeydatabase.py - Last Update: 1/15/2021 Ver. 0.5.0 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals;
import sys, os, re, logging, binascii;
from .hockeydwnload import *;
from .versioninfo import __program_name__, __program_alt_name__, __project__, __project_url__, __project_release_url__, __version__, __version_date__, __version_info__, __version_date_info__, __version_date__, __revision__, __revision_id__, __version_date_plusrc__;

enable_oldsqlite = False;
enable_apsw = False;
enable_supersqlite = False;
enable_old_makegame = False;
defaultxmlfile = "./data/hockeydata.xml";
defaultsdbfile = "./data/hockeydata.db3";
defaultoldsdbfile = "./data/hockeydata.db3";
defaultpyfile = "./data/hockeydata.py";
defaultpythonfile = defaultpyfile;
defaultsqlfile = "./data/hockeydata.sql";
defaultjsonfile = "./data/hockeydata.json";

# From: https://stackoverflow.com/a/28568003
# By Phaxmohdem
def versiontuple(v):
 filled = [];
 for point in v.split("."):
  filled.append(point.zfill(8));
 return tuple(filled);

def version_check(myvercheck, newvercheck):
 overcheck = 0;
 try:
  from packaging import version;
  vercheck = 1;
 except ImportError:
  try:
   from distutils.version import LooseVersion, StrictVersion;
   vercheck = 2;
  except ImportError:
   try:
    from pkg_resources import parse_version;
    vercheck = 3;
   except ImportError:
    return 5;
 #print(myvercheck, newvercheck);
 if(vercheck==1):
  if(version.parse(myvercheck) == version.parse(newvercheck)):
   return 0;
  elif(version.parse(myvercheck) < version.parse(newvercheck)):
   return 1;
  elif(version.parse(myvercheck) > version.parse(newvercheck)):
   return 2;
  else:
   return 3;
 elif(vercheck==2):
  if(StrictVersion(myvercheck) == StrictVersion(newvercheck)):
   return 0;
  elif(StrictVersion(myvercheck) < StrictVersion(newvercheck)):
   return 1;
  elif(StrictVersion(myvercheck) > StrictVersion(newvercheck)):
   return 2;
  else:
   return 3;
 elif(vercheck==3):
  if(parse_version(myvercheck) == parse_version(newvercheck)):
   return 0;
  elif(parse_version(myvercheck) < parse_version(newvercheck)):
   return 1;
  elif(parse_version(myvercheck) > parse_version(newvercheck)):
   return 2;
  else:
   return 3;
 else:
  if(versiontuple(myvercheck) == versiontuple(newvercheck)):
   return 0;
  elif(versiontuple(myvercheck) < versiontuple(newvercheck)):
   return 1;
  elif(versiontuple(myvercheck) > versiontuple(newvercheck)):
   return 2;
  else:
   return 3;
 return 4;

def check_version_number(myversion=__version__, proname=__program_alt_name__, newverurl=__project_release_url__):
 prevercheck = download_from_url(newverurl, geturls_headers, geturls_cj);
 newvercheck = re.findall(proname+" ([0-9\.]+)<\/a\>", prevercheck['Content'].decode("UTF-8"))[0];
 myvercheck = re.findall("([0-9\.]+)", myversion)[0];
 return version_check(myvercheck, newvercheck);

teststringio = 0;
try:
 from io import BytesIO;
 from io import StringIO;
 teststringio = 3;
except ImportError:
 try:
  from cStringIO import StringIO as BytesIO;
  from cStringIO import StringIO;
  teststringio = 1;
 except ImportError:
  try:
   from StringIO import StringIO as BytesIO;
   from StringIO import StringIO;
   teststringio = 2;
  except ImportError:
   teststringio = 0;
from xml.sax.saxutils import XMLGenerator;

try:
 basestring;
except NameError:
 basestring = str;

baseint = [];
try:
 baseint.append(long);
 baseint.insert(0, int);
except NameError:
 baseint.append(int);
baseint = tuple(baseint);

if(enable_supersqlite):
 supersqlitesupport = True;
 try:
  from supersqlite import sqlite3;
 except ImportError:
  import sqlite3;
  supersqlitesupport = False;
else:
 import sqlite3;
 supersqlitesupport = False;

if(enable_apsw):
 if(supersqlitesupport):
  apswsupport = True;
  try:
   import apsw;
  except ImportError:
   apswsupport = False;
 else:
  apswsupport = True;
  try:
   from supersqlite import apsw;
  except ImportError:
   apswsupport = False;
else:
 apswsupport = False;

if(supersqlitesupport and enable_supersqlite):
 import supersqlite;

if(enable_oldsqlite):
 oldsqlitesupport = True;
 try:
  import sqlite;
 except ImportError:
  oldsqlitesupport = False;
else:
 oldsqlitesupport = False;

try:
 from xml.sax.saxutils import xml_escape;
except ImportError:
 try:
  from cgi import escape as html_escape;
 except ImportError:
  from html import escape as html_escape;

def check_if_string(strtext):
 if(sys.version[0]=="2"):
  if(isinstance(strtext, basestring)):
   return True;
 if(sys.version[0]>="3"):
  if(isinstance(strtext, str)):
   return True;
 return False;

def EscapeXMLString(inxml, quote=True):
 if(quote):
  xml_escape_dict = { "\"": "&quot;", "'": "&apos;" };
 else:
  xml_escape_dict = {};
 outxml = False;
 try:
  outxml = xml_escape(inxml, xml_escape_dict);
 except NameError:
  outxml = html_escape(inxml, quote);
 return outxml;

def VerbosePrintOut(dbgtxt, outtype="log", dbgenable=True, dgblevel=20):
 if(outtype=="print" and dbgenable):
  print(dbgtxt);
  return True;
 elif(outtype=="log" and dbgenable):
  logging.info(dbgtxt);
  return True;
 elif(outtype=="warning" and dbgenable):
  logging.warning(dbgtxt);
  return True;
 elif(outtype=="error" and dbgenable):
  logging.error(dbgtxt);
  return True;
 elif(outtype=="critical" and dbgenable):
  logging.critical(dbgtxt);
  return True;
 elif(outtype=="exception" and dbgenable):
  logging.exception(dbgtxt);
  return True;
 elif(outtype=="logalt" and dbgenable):
  logging.log(dgblevel, dbgtxt);
  return True;
 elif(outtype=="debug" and dbgenable):
  logging.debug(dbgtxt);
  return True;
 elif(not dbgenable):
  return True;
 else:
  return False;
 return False;

def VerbosePrintOutReturn(dbgtxt, outtype="log", dbgenable=True, dgblevel=20):
 VerbosePrintOut(dbgtxt, outtype, dbgenable, dgblevel);
 return dbgtxt;

def RemoveWindowsPath(dpath):
 if(os.sep!="/"):
  dpath = dpath.replace(os.path.sep, "/");
 dpath = dpath.rstrip("/");
 if(dpath=="." or dpath==".."):
  dpath = dpath + "/";
 return dpath;

def NormalizeRelativePath(inpath):
 inpath = RemoveWindowsPath(inpath);
 if(os.path.isabs(inpath)):
  outpath = inpath;
 else:
  if(inpath.startswith("./") or inpath.startswith("../")):
   outpath = inpath;
  else:
   outpath = "./" + inpath;
 return outpath;

def CheckSQLiteDatabase(infile):
 sqlfp = open(infile, "rb");
 sqlfp.seek(0, 0);
 prefp = sqlfp.read(16);
 validsqlite = False;
 if(prefp==binascii.unhexlify("53514c69746520666f726d6174203300")):
  validsqlite = True;
 sqlfp.close();
 return validsqlite;

def ConvertPythonValuesForXML(invalue):
 if(invalue):
  outvalue = "true";
 elif(not invalue):
  outvalue = "false";
 elif(invalue is None):
  outvalue = "null";
 elif(invalue=="''"):
  outvalue = "";
 else:
  outvalue = outvalue;
 return outvalue;

def ConvertXMLValuesForPython(invalue):
 if(invalue=="true"):
  outvalue = True;
 elif(invalue=="false"):
  outvalue = False;
 elif(invalue=="null"):
  outvalue = "None";
 elif(invalue==""):
  outvalue = "''";
 else:
  outvalue = outvalue;
 return outvalue;

def CheckHockeySQLiteDatabase(sdbfile, returndb=False):
 if(os.path.exists(sdbfile) and os.path.isfile(sdbfile) and isinstance(sdbfile, basestring)):
  if(not CheckSQLiteDatabase(sdbfile)):
   return [False];
  sqldatacon = OpenHockeyDatabase(sdbfile);
 else:
  if(sdbfile is not None and isinstance(sdbfile, (tuple, list))):
   sqldatacon = tuple(sdbfile);
  else:
   return [False];
 sqldatacur = sqldatacon[1].cursor();
 if(sqldatacur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='HockeyLeagues';").fetchone() is None):
  return [False];
 #all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games", "PlayoffTeams"];
 all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games"];
 table_list = ['HockeyLeagues'];
 getleague_tmp = sqldatacon[0].execute("SELECT LeagueName FROM HockeyLeagues");
 for leagueinfo_tmp in getleague_tmp:
  for cur_tab in all_table_list:
   table_list.append(leagueinfo_tmp[0]+cur_tab);
 for get_cur_tab in table_list:
  if(sqldatacur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='"+get_cur_tab+"';").fetchone() is None):
   return [False];
 if(not returndb):
  CloseHockeyDatabase(sqldatacon);
 if(returndb):
  return [True, sqldatacon];
 if(not returndb):
  return [True];
 return [True];

def MakeHockeyDatabase(sdbfile, synchronous="FULL", journal_mode="DELETE", temp_store="DEFAULT", enable_oldsqlite=False, enable_apsw=False, enable_supersqlite=False):
 if(not oldsqlitesupport and enable_oldsqlite):
  enable_oldsqlite = False;
 if(not apswsupport and enable_apsw):
  enable_apsw = False;
 if(not supersqlitesupport and enable_supersqlite):
  enable_apsw = False;
 if(os.path.exists(sdbfile) or os.path.isfile(sdbfile)):
  return False;
 if(enable_oldsqlite):
   sqlcon = sqlite.connect(sdbfile, isolation_level=None);
 else:
  if(enable_apsw and not enable_supersqlite):
   sqlcon = apsw.Connection(sdbfile);
  elif(enable_apsw and enable_supersqlite):
   sqlcon = supersqlite.SuperSQLiteConnection(sdbfile);
  else:
   sqlcon = sqlite3.connect(sdbfile, isolation_level=None);
 sqlcur = sqlcon.cursor();
 sqldatacon = (sqlcur, sqlcon);
 sqlcur.execute("PRAGMA encoding = \"UTF-8\";");
 sqlcur.execute("PRAGMA auto_vacuum = 1;");
 sqlcur.execute("PRAGMA foreign_keys = 0;");
 sqlcur.execute("PRAGMA synchronous = "+str(synchronous)+";");
 if(not enable_oldsqlite):
  sqlcur.execute("PRAGMA journal_mode = "+str(journal_mode)+";");
 sqlcur.execute("PRAGMA temp_store = "+str(temp_store)+";");
 return sqldatacon;

def CreateHockeyArray(databasename="./hockeydatabase.db3"):
 hockeyarray = { 'database': databasename, 'leaguelist': [] };
 return hockeyarray;

def CreateHockeyDatabase(sdbfile, enable_oldsqlite=False, enable_apsw=False, enable_supersqlite=False):
 if(not oldsqlitesupport and enable_oldsqlite):
  enable_oldsqlite = False;
 if(not apswsupport and enable_apsw):
  enable_apsw = False;
 if(not supersqlitesupport and enable_supersqlite):
  enable_apsw = False;
 if(os.path.exists(sdbfile) or os.path.isfile(sdbfile)):
  return False;
 if(enable_oldsqlite):
   sqlcon = sqlite.connect(sdbfile, isolation_level=None);
 else:
  if(enable_apsw and not enable_supersqlite):
   sqlcon = apsw.Connection(sdbfile);
  elif(enable_apsw and enable_supersqlite):
   sqlcon = supersqlite.SuperSQLiteConnection(sdbfile);
  else:
   sqlcon = sqlite3.connect(sdbfile, isolation_level=None);
 sqlcur = sqlcon.cursor();
 sqlcur.execute("PRAGMA encoding = \"UTF-8\";");
 sqlcur.execute("PRAGMA auto_vacuum = 1;");
 sqlcur.execute("PRAGMA foreign_keys = 0;");
 sqlcur.close();
 sqlcon.close();
 return True;

def OpenHockeyDatabase(sdbfile, enable_oldsqlite=False, enable_apsw=False, enable_supersqlite=False):
 if(not oldsqlitesupport and enable_oldsqlite):
  enable_oldsqlite = False;
 if(not apswsupport and enable_apsw):
  enable_apsw = False;
 if(not supersqlitesupport and enable_supersqlite):
  enable_apsw = False;
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(enable_oldsqlite):
   sqlcon = sqlite.connect(sdbfile, isolation_level=None);
 else:
  if(enable_apsw and not enable_supersqlite):
   sqlcon = apsw.Connection(sdbfile);
  elif(enable_apsw and enable_supersqlite):
   sqlcon = supersqlite.SuperSQLiteConnection(sdbfile);
  else:
   sqlcon = sqlite3.connect(sdbfile, isolation_level=None);
 sqlcur = sqlcon.cursor();
 sqldatacon = (sqlcur, sqlcon);
 sqlcur.execute("PRAGMA encoding = \"UTF-8\";");
 sqlcur.execute("PRAGMA auto_vacuum = 1;");
 sqlcur.execute("PRAGMA foreign_keys = 0;");
 return sqldatacon;

def GetLastGames(sqldatacon, leaguename, teamname, gamelimit=10):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
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
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
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
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
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
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
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
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 if(wheretype=="int"):
  sqldatacon[0].execute("UPDATE "+leaguename+tablename+" SET "+dataname+"=\""+str(newdata)+"\" WHERE "+wherename+"="+str(wheredata));
 if(wheretype=="str"):
  sqldatacon[0].execute("UPDATE "+leaguename+tablename+" SET "+dataname+"=\""+str(newdata)+"\" WHERE "+wherename+"=\""+str(wheredata)+"\"");
 return True;

def UpdateTeamData(sqldatacon, leaguename, teamid, dataname, addtodata, addtype):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0]) + addtodata;
 if(addtype=="-"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0]) - addtodata;
 sqldatacon[0].execute("UPDATE "+leaguename+"Teams SET "+dataname+"="+str(TMPData)+" WHERE id="+str(teamid));
 return int(TMPData);

def UpdateTeamDataString(sqldatacon, leaguename, teamid, dataname, newdata):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 sqldatacon[0].execute("UPDATE "+leaguename+"Teams SET "+dataname+"=\""+str(newdata)+"\" WHERE id="+str(teamid));
 return True;

def GetTeamData(sqldatacon, leaguename, teamid, dataname, datatype):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 if(datatype=="float"):
  TMPData = float(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0]);
 if(datatype=="int"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0]);
 if(datatype=="str"):
  TMPData = str(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0]);
 return TMPData;

def UpdateGameData(sqldatacon, leaguename, gameid, dataname, addtodata, addtype):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Games WHERE id="+str(gameid)).fetchone()[0]) + addtodata;
 if(addtype=="-"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Games WHERE id="+str(gameid)).fetchone()[0]) - addtodata;
 sqldatacon[0].execute("UPDATE "+leaguename+"Games SET "+dataname+"="+str(TMPData)+" WHERE id="+str(gameid));
 return int(TMPData);

def UpdateGameDataString(sqldatacon, leaguename, gameid, dataname, newdata):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 sqldatacon[0].execute("UPDATE "+leaguename+"Games SET "+dataname+"=\""+str(newdata)+"\" WHERE id="+str(gameid));
 return True;

def GetGameData(sqldatacon, leaguename, gameid, dataname, datatype):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 if(datatype=="float"):
  TMPData = float(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Games WHERE id="+str(gameid)).fetchone()[0]);
 if(datatype=="int"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Games WHERE id="+str(gameid)).fetchone()[0]);
 if(datatype=="str"):
  TMPData = str(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Games WHERE id="+str(gameid)).fetchone()[0]);
 return TMPData;

def UpdateArenaData(sqldatacon, leaguename, arenaid, dataname, addtodata, addtype):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0]) + addtodata;
 if(addtype=="-"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0]) - addtodata;
 sqldatacon[0].execute("UPDATE "+leaguename+"Arenas SET "+dataname+"="+str(TMPData)+" WHERE id="+str(arenaid));
 return int(TMPData);

def UpdateArenaDataString(sqldatacon, leaguename, arenaid, dataname, newdata):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 sqldatacon[0].execute("UPDATE "+leaguename+"Arenas SET "+dataname+"=\""+str(newdata)+"\" WHERE id="+str(arenaid));
 return True;

def GetArenaData(sqldatacon, leaguename, arenaid, dataname, datatype):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 if(datatype=="float"):
  TMPData = float(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0]);
 if(datatype=="int"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0]);
 if(datatype=="str"):
  TMPData = str(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0]);
 return TMPData;

def UpdateConferenceData(sqldatacon, leaguename, conference, dataname, addtodata, addtype):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Conferences WHERE Conference=\""+str(conference)+"\"").fetchone()[0]) + addtodata;
 if(addtype=="-"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Conferences WHERE Conference=\""+str(conference)+"\"").fetchone()[0]) - addtodata;
 sqldatacon[0].execute("UPDATE "+leaguename+"Conferences SET "+dataname+"="+str(TMPData)+" WHERE Conference=\""+str(conference)+"\"");
 return int(TMPData);

def UpdateDivisionData(sqldatacon, leaguename, division, dataname, addtodata, addtype):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Divisions WHERE Division=\""+str(division)+"\"").fetchone()[0]) + addtodata;
 if(addtype=="-"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Divisions WHERE Division=\""+str(division)+"\"").fetchone()[0]) - addtodata;
 sqldatacon[0].execute("UPDATE "+leaguename+"Divisions SET "+dataname+"="+str(TMPData)+" WHERE Division=\""+str(division)+"\"");
 return int(TMPData);

def UpdateLeagueData(sqldatacon, leaguename, dataname, addtodata, addtype):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM HockeyLeagues WHERE LeagueName=\""+str(leaguename)+"\"").fetchone()[0]) + addtodata;
 if(addtype=="-"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM HockeyLeagues WHERE LeagueName=\""+str(leaguename)+"\"").fetchone()[0]) - addtodata;
 sqldatacon[0].execute("UPDATE HockeyLeagues SET "+dataname+"="+str(TMPData)+" WHERE LeagueName=\""+str(leaguename)+"\"");
 return int(TMPData);

def GetLeagueName(sqldatacon, leaguename):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 TMPData = str(sqldatacon[0].execute("SELECT LeagueFullName FROM HockeyLeagues WHERE LeagueName=\""+str(leaguename)+"\"").fetchone()[0]);
 return TMPData;

def GetConferenceName(sqldatacon, leaguename, conference):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 TMPData = str(sqldatacon[0].execute("SELECT FullName FROM "+leaguename+"Conferences WHERE Conference=\""+str(conference)+"\"").fetchone()[0]);
 return TMPData;

def GetDivisionName(sqldatacon, leaguename, division, conference):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 TMPData = str(sqldatacon[0].execute("SELECT FullName FROM "+leaguename+"Divisions WHERE Conference=\""+str(conference)+"\" AND Division=\""+str(division)+"\"").fetchone()[0]);
 return TMPData;

def GetNum2Team(sqldatacon, leaguename, TeamNum, ReturnVar):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 return str(sqldatacon[0].execute("SELECT "+ReturnVar+" FROM "+leaguename+"Teams WHERE id="+str(TeamNum)).fetchone()[0]);

def GetTeam2Num(sqldatacon, leaguename, TeamName):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
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
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 return str(sqldatacon[0].execute("SELECT "+ReturnVar+" FROM "+leaguename+"Arenas WHERE id="+str(ArenaNum)).fetchone()[0]);

def GetArena2Num(sqldatacon, leaguename, ArenaName):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
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

def CheckHockeyArray(inhockeyarray):
 if(isinstance(inhockeyarray, type(None)) or isinstance(inhockeyarray, type(True)) or isinstance(inhockeyarray, type(False)) or not isinstance(inhockeyarray, type({}))):
  return False;
 if "leaguelist" not in inhockeyarray.keys():
  return False;
 if "database" not in inhockeyarray.keys():
  return False;
 leaguelist = [];
 for hlkey in inhockeyarray['leaguelist']:
  if hlkey not in inhockeyarray.keys():
   return False;
  if(hlkey in leaguelist):
   return False;
  leaguelist.append(hlkey);
  for hckey in inhockeyarray[hlkey]['conferencelist']:
   if hckey not in inhockeyarray[hlkey].keys() or hckey not in inhockeyarray[hlkey]['quickinfo']['conferenceinfo'].keys():
    return False;
   for hdkey in inhockeyarray[hlkey][hckey]['divisionlist']:
    if hdkey not in inhockeyarray[hlkey][hckey].keys() or hdkey not in inhockeyarray[hlkey]['quickinfo']['divisioninfo'].keys():
     return False;
    for htkey in inhockeyarray[hlkey][hckey][hdkey]['teamlist']:
     if htkey not in inhockeyarray[hlkey][hckey][hdkey].keys() or htkey not in inhockeyarray[hlkey]['quickinfo']['teaminfo'].keys():
      return False;
 return True;

def CheckHockeySQLiteArray(inhockeyarray):
 if(isinstance(inhockeyarray, type(None)) or isinstance(inhockeyarray, type(True)) or isinstance(inhockeyarray, type(False)) or not isinstance(inhockeyarray, type({}))):
  return False;
 if "HockeyLeagues" not in inhockeyarray.keys():
  return False;
 if "database" not in inhockeyarray.keys():
  return False;
 #all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games", "PlayoffTeams"];
 all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games"];
 table_list = ['HockeyLeagues'];
 leaguelist = [];
 for leagueinfo_tmp in inhockeyarray['HockeyLeagues']['values']:
  if(leagueinfo_tmp['LeagueName'] in leaguelist):
   return False;
  leaguelist.append(leagueinfo_tmp['LeagueName']);
  for cur_tab in all_table_list:
   table_list.append(leagueinfo_tmp['LeagueName']+cur_tab);
 for get_cur_tab in table_list:
  if get_cur_tab not in inhockeyarray.keys():
   return False;
 return True;

def AddHockeyLeagueToArray(inhockeyarray, leaguename, leaguefullname, countryname, fullcountryname, date, playofffmt, ordertype, hasconferences="yes", hasdivisions="yes"):
 inchockeyarray = inhockeyarray.copy();
 if(leaguename in inchockeyarray['leaguelist']):
  return False;
 if "leaguelist" not in inchockeyarray.keys():
  inchockeyarray.update( { 'leaguelist': [] } );
 if "database" not in inchockeyarray.keys():
  inchockeyarray.update( { 'database': "./hockeydatabase.db3" } );
 if leaguename not in inchockeyarray.keys():
  inchockeyarray.update( { leaguename: { 'leagueinfo': { 'name': str(leaguename), 'fullname': str(leaguefullname), 'country': str(countryname), 'fullcountry': str(fullcountryname), 'date': str(date), 'playofffmt': str(playofffmt), 'ordertype': str(ordertype), 'conferences': str(hasconferences), 'divisions': str(hasdivisions) }, 'conferencelist': [], 'quickinfo': {'conferenceinfo': {}, 'divisioninfo': {}, 'teaminfo': {} }, 'arenas': [ {} ], 'games': [ {} ] } } );
  inchockeyarray['leaguelist'].append(str(leaguename));
 return inchockeyarray;

def RemoveHockeyLeagueFromArray(inhockeyarray, leaguename):
 inchockeyarray = inhockeyarray.copy();
 if "leaguelist" not in inchockeyarray.keys():
  inchockeyarray.update( { 'leaguelist': [] } );
 if "database" not in inchockeyarray.keys():
  inchockeyarray.update( { 'database': "./hockeydatabase.db3" } );
 if leaguename in inchockeyarray.keys():
  inchockeyarray.pop(leaguename, None);
  inchockeyarray['leaguelist'].remove(leaguename);
 return inchockeyarray;

def ReplaceHockeyLeagueFromArray(inhockeyarray, oldleaguename, newleaguename, leaguefullname=None, countryname=None, fullcountryname=None, date=None, playofffmt=None, ordertype=None, hasconferences=None, hasdivisions=None):
 inchockeyarray = inhockeyarray.copy();
 if "leaguelist" not in inchockeyarray.keys():
  inchockeyarray.update( { 'leaguelist': [] } );
 if "database" not in inchockeyarray.keys():
  inchockeyarray.update( { 'database': "./hockeydatabase.db3" } );
 if oldleaguename in inchockeyarray.keys() and newleaguename not in inchockeyarray.keys():
  inchockeyarray[newleaguename] = inchockeyarray.pop(str(oldleaguename));
  inchockeyarray[newleaguename]['leagueinfo']['name'] = str(newleaguename);
  if(leaguefullname is not None):
   inchockeyarray[newleaguename]['leagueinfo']['fullname'] =  str(leaguefullname);
  if(countryname is not None):
   inchockeyarray[newleaguename]['leagueinfo']['country'] = str(countryname);
  if(fullcountryname is not None):
   inchockeyarray[newleaguename]['leagueinfo']['fullcountry'] = str(fullcountryname);
  if(date is not None):
   inchockeyarray[newleaguename]['leagueinfo']['date'] = str(date);
  if(playofffmt is not None):
   inchockeyarray[newleaguename]['leagueinfo']['playofffmt'] = str(playofffmt);
  if(ordertype is not None):
   inchockeyarray[newleaguename]['leagueinfo']['ordertype'] = str(ordertype);
  if(hasconferences is not None):
   inchockeyarray[newleaguename]['leagueinfo']['conferences'] = str(hasconferences);
  if(hasdivisions is not None):
   inchockeyarray[newleaguename]['leagueinfo']['divisions'] = str(hasdivisions);
  if "conferencelist" not in inchockeyarray[newleaguename].keys():
   inchockeyarray[newleaguename].update( { 'conferencelist': [] } );
  hlin = inchockeyarray['leaguelist'].index(oldleaguename);
  inchockeyarray['leaguelist'][hlin] = newleaguename;
  for hlkey in inchockeyarray['leaguelist']:
   for hckey in inchockeyarray[hlkey]['conferencelist']:
    inchockeyarray[newleaguename][hckey]['conferenceinfo']['league'] = str(newleaguename);
    for hdkey in inchockeyarray[hlkey][hckey]['divisionlist']:
     inchockeyarray[newleaguename][hckey][hdkey]['divisioninfo']['league'] = str(newleaguename);
     for htkey in inchockeyarray[hlkey][hckey][hdkey]['teamlist']:
      inchockeyarray[newleaguename][hckey][hdkey][htkey]['teaminfo']['league'] = str(newleaguename);
 return inchockeyarray;

def MakeHockeyLeagueTable(sqldatacon, droptable=True):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 if(droptable):
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
 "  NumberOfDivisions INTEGER NOT NULL DEFAULT 0\n" + \
 ");");
 return True;

def MakeHockeyLeague(sqldatacon, leaguename, leaguefullname, countryname, fullcountryname, date, playofffmt, ordertype):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 sqldatacon[0].execute("INSERT INTO HockeyLeagues (LeagueName, LeagueFullName, CountryName, FullCountryName, Date, PlayOffFMT, OrderType, NumberOfTeams, NumberOfConferences, NumberOfDivisions) VALUES \n" + \
 "(\""+str(leaguename)+"\", \""+str(leaguefullname)+"\", \""+str(countryname)+"\", \""+str(fullcountryname)+"\", \""+str(date)+"\", \""+str(playofffmt)+"\", \""+str(ordertype)+"\", 0, 0, 0)");
 return True;

def AddHockeyConferenceToArray(inhockeyarray, leaguename, conference, prefix="", suffix="Conference"):
 inchockeyarray = inhockeyarray.copy();
 if leaguename in inchockeyarray.keys() and "conferencelist" not in inchockeyarray[leaguename].keys():
  inchockeyarray[leaguename].update( { 'conferencelist': [] } );
 if "database" not in inchockeyarray.keys():
  inchockeyarray.update( { 'database': "./hockeydatabase.db3" } );
 if leaguename in inchockeyarray.keys():
  if conference not in inchockeyarray[leaguename].keys():
   ConferenceFullName = GetFullTeamName(conference, prefix, suffix);
   inchockeyarray[leaguename].update( { str(conference): { 'conferenceinfo': { 'name': str(conference), 'prefix': str(prefix), 'suffix': str(suffix), 'fullname': str(ConferenceFullName), 'league': str(leaguename) }, 'divisionlist': [] } } );
   inchockeyarray[leaguename]['quickinfo']['conferenceinfo'].update( { str(conference): { 'name': str(conference), 'fullname': str(ConferenceFullName), 'league': str(leaguename) } } );
   inchockeyarray[leaguename]['conferencelist'].append(str(conference));
 return inchockeyarray;

def RemoveHockeyConferenceFromArray(inhockeyarray, leaguename, conference):
 inchockeyarray = inhockeyarray.copy();
 if leaguename in inchockeyarray.keys() and "conferencelist" not in inchockeyarray[leaguename].keys():
  inchockeyarray[leaguename].update( { 'conferencelist': [] } );
 if "database" not in inchockeyarray.keys():
  inchockeyarray.update( { 'database': "./hockeydatabase.db3" } );
 if leaguename in inchockeyarray.keys():
  if conference in inchockeyarray[leaguename].keys():
   for hdkey in inchockeyarray[leaguename][conference]['divisionlist']:
    inchockeyarray[leaguename]['quickinfo']['divisioninfo'].pop(hdkey, None);
    for htkey in inchockeyarray[leaguename][conference][hdkey]['teamlist']:
     fullteamname = GetFullTeamName(inchockeyarray[leaguename][conference][hdkey][htkey]['teaminfo']['name'], inchockeyarray[leaguename][conference][hdkey][htkey]['teaminfo']['prefix'], inchockeyarray[leaguename][conference][hdkey][htkey]['teaminfo']['suffix']);
     newgamelist = [];
     for hgkey in inchockeyarray[leaguename]['games']:
      if(hgkey['hometeam']!=fullteamname and hgkey['awayteam']!=fullteamname):
       newgamelist.append(hgkey);
     inchockeyarray[leaguename]['games'] = newgamelist;
     inchockeyarray[leaguename]['quickinfo']['teaminfo'].pop(htkey, None);
   inchockeyarray[leaguename].pop(conference, None);
   inchockeyarray[leaguename]['quickinfo']['conferenceinfo'].pop(conference, None);
   inchockeyarray[leaguename]['conferencelist'].remove(conference);
 return inchockeyarray;

def ReplaceHockeyConferencFromArray(inhockeyarray, leaguename, oldconference, newconference, prefix="", suffix="Conference"):
 inchockeyarray = inhockeyarray.copy();
 if leaguename in inchockeyarray.keys() and "conferencelist" not in inchockeyarray[leaguename].keys():
  inchockeyarray[leaguename].update( { 'conferencelist': [] } );
 if "database" not in inchockeyarray.keys():
  inchockeyarray.update( { 'database': "./hockeydatabase.db3" } );
 if oldconference in inchockeyarray[leaguename].keys() and newconference not in inchockeyarray[leaguename].keys():
  ConferenceFullName = GetFullTeamName(newconference, prefix, suffix);
  inchockeyarray[leaguename][newconference] = inchockeyarray[leaguename].pop(str(oldconference));
  inchockeyarray[leaguename]['quickinfo']['conferenceinfo'][newconference] = inchockeyarray[leaguename]['quickinfo']['conferenceinfo'].pop(str(oldconference));
  inchockeyarray[leaguename]['quickinfo']['conferenceinfo'][newconference]['fullname'] = str(ConferenceFullName);
  inchockeyarray[leaguename][newconference]['conferenceinfo']['name'] = str(newconference);
  inchockeyarray[leaguename][newconference]['conferenceinfo']['prefix'] = str(prefix);
  inchockeyarray[leaguename][newconference]['conferenceinfo']['suffix'] = str(suffix);
  inchockeyarray[leaguename][newconference]['conferenceinfo']['fullname'] = str(ConferenceFullName);
  if "divisionlist" not in inchockeyarray[leaguename][newconference].keys():
   inchockeyarray[leaguename][newconference].update( { 'divisionlist': [] } );
  hcin = inchockeyarray[leaguename]['conferencelist'].index(oldconference);
  inchockeyarray[leaguename]['conferencelist'][hcin] = newconference;
  for hlkey in inchockeyarray['leaguelist']:
   for hckey in inchockeyarray[hlkey]['conferencelist']:
    for hdkey in inchockeyarray[hlkey][hckey]['divisionlist']:
     inchockeyarray[leaguename][newconference][hdkey]['divisioninfo']['conference'] = str(newconference);
     for htkey in inchockeyarray[hlkey][hckey][hdkey]['teamlist']:
      inchockeyarray[leaguename][newconference][hdkey][htkey]['teaminfo']['conference'] = str(newconference);
 return inchockeyarray;

def MakeHockeyConferenceTable(sqldatacon, leaguename, droptable=True):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 if(droptable):
  sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Conferences");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Conferences (\n" + \
 "  id INTEGER PRIMARY KEY AUTOINCREMENT,\n" + \
 "  Conference TEXT NOT NULL DEFAULT '',\n" + \
 "  ConferencePrefix TEXT NOT NULL DEFAULT '',\n" + \
 "  ConferenceSuffix TEXT NOT NULL DEFAULT '',\n" + \
 "  FullName TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueName TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueFullName TEXT NOT NULL DEFAULT '',\n" + \
 "  NumberOfTeams INTEGER NOT NULL DEFAULT 0,\n" + \
 "  NumberOfDivisions INTEGER NOT NULL DEFAULT 0\n" + \
 ");");
 return True;

def MakeHockeyConference(sqldatacon, leaguename, conference, prefix="", suffix="Conference", hasconferences=True):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 ConferenceFullName = GetFullTeamName(conference, prefix, suffix);
 LeagueFullName = GetLeagueName(sqldatacon, leaguename);
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Conferences (Conference, ConferencePrefix, ConferenceSuffix, FullName, LeagueName, LeagueFullName, NumberOfTeams, NumberOfDivisions) VALUES \n" + \
 "(\""+str(conference)+"\", \""+str(prefix)+"\", \""+str(suffix)+"\", \""+str(ConferenceFullName)+"\", \""+str(leaguename)+"\", \""+str(LeagueFullName)+"\", 0, 0)");
 if(hasconferences):
  UpdateLeagueData(sqldatacon, leaguename, "NumberOfConferences", 1, "+");
 return True;

def AddHockeyDivisionToArray(inhockeyarray, leaguename, division, conference, prefix="", suffix="Division"):
 inchockeyarray = inhockeyarray.copy();
 if leaguename in inchockeyarray.keys() and conference in inchockeyarray[leaguename].keys() and "divisionlist" not in inchockeyarray[leaguename][conference].keys():
  inchockeyarray[leaguename][conference].update( { 'divisionlist': [] } );
 if "database" not in inchockeyarray.keys():
  inchockeyarray.update( { 'database': "./hockeydatabase.db3" } );
 if leaguename in inchockeyarray.keys():
  if conference in inchockeyarray[leaguename].keys():
   if division not in inchockeyarray[leaguename][conference].keys():
    DivisionFullName = GetFullTeamName(division, prefix, suffix);
    inchockeyarray[leaguename][conference].update( { str(division): { 'divisioninfo': { 'name': str(division), 'prefix': str(prefix), 'suffix': str(suffix), 'fullname': str(DivisionFullName), 'league': str(leaguename), 'conference': str(conference) }, 'teamlist': [] } } );
    inchockeyarray[leaguename]['quickinfo']['divisioninfo'].update( { str(division): { 'name': str(division), 'fullname': str(DivisionFullName), 'league': str(leaguename), 'conference': str(conference) } } );
    inchockeyarray[leaguename][conference]['divisionlist'].append(str(division));
 return inchockeyarray;

def RemoveHockeyDivisionFromArray(inhockeyarray, leaguename, division, conference):
 inchockeyarray = inhockeyarray.copy();
 if leaguename in inchockeyarray.keys() and conference in inchockeyarray[leaguename].keys() and "divisionlist" not in inchockeyarray[leaguename][conference].keys():
  inchockeyarray[leaguename][conference].update( { 'divisionlist': [] } );
 if "database" not in inchockeyarray.keys():
  inchockeyarray.update( { 'database': "./hockeydatabase.db3" } );
 if leaguename in inchockeyarray.keys():
  if conference in inchockeyarray[leaguename].keys():
   if division in inchockeyarray[leaguename][conference].keys():
    for htkey in inchockeyarray[leaguename][conference][division]['teamlist']:
     fullteamname = GetFullTeamName(inchockeyarray[leaguename][conference][division][htkey]['teaminfo']['name'], inchockeyarray[leaguename][conference][division][htkey]['teaminfo']['prefix'], inchockeyarray[leaguename][conference][division][htkey]['teaminfo']['suffix']);
     newgamelist = [];
     for hgkey in inchockeyarray[leaguename]['games']:
      if(hgkey['hometeam']!=fullteamname and hgkey['awayteam']!=fullteamname):
       newgamelist.append(hgkey);
     inchockeyarray[leaguename]['games'] = newgamelist;
     inchockeyarray[leaguename]['quickinfo']['teaminfo'].pop(htkey, None);
    inchockeyarray[leaguename][conference].pop(division, None);
    inchockeyarray[leaguename]['quickinfo']['divisioninfo'].pop(division, None);
    inchockeyarray[leaguename][conference]['divisionlist'].remove(division);
 return inchockeyarray;

def ReplaceHockeyDivisionFromArray(inhockeyarray, leaguename, olddivision, newdivision, conference, prefix="", suffix="Division"):
 inchockeyarray = inhockeyarray.copy();
 if leaguename in inchockeyarray.keys() and conference in inchockeyarray[leaguename].keys() and "divisionlist" not in inchockeyarray[leaguename][conference].keys():
  inchockeyarray[leaguename][conference].update( { 'divisionlist': [] } );
 if "database" not in inchockeyarray.keys():
  inchockeyarray.update( { 'database': "./hockeydatabase.db3" } );
 if olddivision in inchockeyarray[leaguename][conference].keys() and newdivision not in inchockeyarray[leaguename][conference].keys():
  DivisionFullName = GetFullTeamName(newdivision, prefix, suffix);
  inchockeyarray[leaguename][conference][newdivision] = inchockeyarray[leaguename][conference].pop(str(olddivision));
  inchockeyarray[leaguename]['quickinfo']['divisioninfo'][newdivision] = inchockeyarray[leaguename]['quickinfo']['divisioninfo'].pop(str(olddivision));
  inchockeyarray[leaguename][conference][newdivision]['divisioninfo']['name'] = str(newdivision);
  inchockeyarray[leaguename][conference][newdivision]['divisioninfo']['prefix'] = str(prefix);
  inchockeyarray[leaguename][conference][newdivision]['divisioninfo']['suffix'] = str(suffix);
  inchockeyarray[leaguename][conference][newdivision]['divisioninfo']['fullname'] = str(DivisionFullName);
  inchockeyarray[leaguename]['quickinfo']['divisioninfo'][newdivision]['fullname'] = str(DivisionFullName);
  if "teamlist" not in inchockeyarray[leaguename][conference][newdivision].keys():
   inchockeyarray[leaguename][conference][newdivision].update( { 'teamlist': [] } );
  hdin = inchockeyarray[leaguename][conference]['divisionlist'].index(olddivision);
  inchockeyarray[leaguename][conference]['divisionlist'][hdin] = newdivision;
  for hdkey in inchockeyarray[leaguename][conference][newdivision].keys():
   if(hdkey!="divisioninfo"):
    inchockeyarray[leaguename][conference][newdivision][hdkey]['teaminfo']['division'] = str(newdivision);
 return inchockeyarray;

def MoveHockeyDivisionToConferenceFromArray(inhockeyarray, leaguename, division, oldconference, newconference):
 inchockeyarray = inhockeyarray.copy();
 if leaguename in inchockeyarray.keys() and newconference in inchockeyarray[leaguename].keys() and oldconference in inchockeyarray[leaguename].keys() and division in inchockeyarray[leaguename][oldconference].keys() and division not in inchockeyarray[leaguename][newconference].keys():
  inchockeyarray[leaguename][newconference][division] = inchockeyarray[leaguename][oldconference].pop(str(division));
  inchockeyarray[leaguename][newconference][division]['divisioninfo']['conference'] = str(newconference);
  inchockeyarray[leaguename]['quickinfo']['divisioninfo'][division]['conference'] = str(newconference);
 return inchockeyarray;

def MakeHockeyDivisionTable(sqldatacon, leaguename, droptable=True):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 if(droptable):
  sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Divisions");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Divisions (\n" + \
 "  id INTEGER PRIMARY KEY AUTOINCREMENT,\n" + \
 "  Division TEXT NOT NULL DEFAULT '',\n" + \
 "  DivisionPrefix TEXT NOT NULL DEFAULT '',\n" + \
 "  DivisionSuffix TEXT NOT NULL DEFAULT '',\n" + \
 "  FullName TEXT NOT NULL DEFAULT '',\n" + \
 "  Conference TEXT NOT NULL DEFAULT '',\n" + \
 "  ConferenceFullName TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueName TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueFullName TEXT NOT NULL DEFAULT '',\n" + \
 "  NumberOfTeams INTEGER NOT NULL DEFAULT 0\n" + \
 ");");
 return True;

def MakeHockeyDivision(sqldatacon, leaguename, division, conference, prefix="", suffix="Division", hasconferences=True, hasdivisions=True):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 DivisionFullName = GetFullTeamName(division, prefix, suffix);
 ConferenceFullName = GetConferenceName(sqldatacon, leaguename, conference);
 LeagueFullName = GetLeagueName(sqldatacon, leaguename);
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Divisions (Division, DivisionPrefix, DivisionSuffix, FullName, Conference, ConferenceFullName, LeagueName, LeagueFullName, NumberOfTeams) VALUES \n" + \
 "(\""+str(division)+"\", \""+str(prefix)+"\", \""+str(suffix)+"\", \""+str(DivisionFullName)+"\", \""+str(conference)+"\", \""+str(ConferenceFullName)+"\", \""+str(leaguename)+"\", \""+str(LeagueFullName)+"\", 0)");
 if(hasconferences):
  UpdateConferenceData(sqldatacon, leaguename, conference, "NumberOfDivisions", 1, "+");
 if(hasdivisions):
  UpdateLeagueData(sqldatacon, leaguename, "NumberOfDivisions", 1, "+");
 return True;

def AddHockeyTeamToArray(inhockeyarray, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, teamname, conference, division, arenaname, teamnameprefix="", teamnamesuffix="", teamaffiliates=""):
 inchockeyarray = inhockeyarray.copy();
 if leaguename in inchockeyarray.keys() and conference in inchockeyarray[leaguename].keys() and division in inchockeyarray[leaguename][conference].keys() and "teamlist" not in inchockeyarray[leaguename][conference][division].keys():
  inchockeyarray[leaguename][conference][division].update( { 'teamlist': [] } );
 if "database" not in inchockeyarray.keys():
  inchockeyarray.update( { 'database': "./hockeydatabase.db3" } );
 if leaguename in inchockeyarray.keys():
  if conference in inchockeyarray[leaguename].keys():
   if division in inchockeyarray[leaguename][conference].keys():
    if teamname not in inchockeyarray[leaguename][conference][division].keys():
     fullteamname = GetFullTeamName(str(teamname), str(teamnameprefix), str(teamnamesuffix));
     inchockeyarray[leaguename][conference][division].update( { str(teamname): { 'teaminfo': { 'city': str(cityname), 'area': str(areaname), 'fullarea': str(fullareaname), 'country': str(countryname), 'fullcountry': str(fullcountryname), 'name': str(teamname), 'fullname': fullteamname, 'arena': str(arenaname), 'prefix': str(teamnameprefix), 'suffix': str(teamnamesuffix), 'league': str(leaguename), 'conference': str(conference), 'division': str(division) } } } );
     inchockeyarray[leaguename]['quickinfo']['teaminfo'].update( { str(teamname): { 'name': str(teamname), 'fullname': fullteamname, 'league': str(leaguename), 'conference': str(conference), 'division': str(division), 'affiliates': str(teamaffiliates) } } );
     inchockeyarray[leaguename][conference][division]['teamlist'].append(str(teamname));
 return inchockeyarray;

def RemoveHockeyTeamFromArray(inhockeyarray, leaguename, teamname, conference, division):
 inchockeyarray = inhockeyarray.copy();
 if leaguename in inchockeyarray.keys() and conference in inchockeyarray[leaguename].keys() and division in inchockeyarray[leaguename][conference].keys() and "teamlist" not in inchockeyarray[leaguename][conference][division].keys():
  inchockeyarray[leaguename][conference][division].update( { 'teamlist': [] } );
 if "database" not in inchockeyarray.keys():
  inchockeyarray.update( { 'database': "./hockeydatabase.db3" } );
 if leaguename in inchockeyarray.keys():
  if conference in inchockeyarray[leaguename].keys():
   if division in inchockeyarray[leaguename][conference].keys():
    if teamname in inchockeyarray[leaguename][conference][division].keys():
     fullteamname = GetFullTeamName(inchockeyarray[leaguename][conference][division][teamname]['teaminfo']['name'], inchockeyarray[leaguename][conference][division][teamname]['teaminfo']['prefix'], inchockeyarray[leaguename][conference][division][teamname]['teaminfo']['suffix']);
     newgamelist = [];
     for hgkey in inchockeyarray[leaguename]['games']:
      if(hgkey['hometeam']!=fullteamname and hgkey['awayteam']!=fullteamname):
       newgamelist.append(hgkey);
     inchockeyarray[leaguename]['games'] = newgamelist;
     inchockeyarray[leaguename][conference][division].pop(teamname, None);
     inchockeyarray[leaguename]['quickinfo']['teaminfo'].pop(teamname, None);
     inchockeyarray[leaguename][conference][division]['teamlist'].remove(teamname);
 return inchockeyarray;

def ReplaceHockeyTeamFromArray(inhockeyarray, leaguename, oldteamname, newteamname, conference, division, cityname=None, areaname=None, countryname=None, fullcountryname=None, fullareaname=None, arenaname=None, teamnameprefix=None, teamnamesuffix=None, teamaffiliates=None):
 inchockeyarray = inhockeyarray.copy();
 if leaguename in inchockeyarray.keys() and conference in inchockeyarray[leaguename].keys() and division in inchockeyarray[leaguename][conference].keys() and "teamlist" not in inchockeyarray[leaguename][conference][division].keys():
  inchockeyarray[leaguename][conference][division].update( { 'teamlist': [] } );
 if "database" not in inchockeyarray.keys():
  inchockeyarray.update( { 'database': "./hockeydatabase.db3" } );
 if oldteamname in inchockeyarray[leaguename][conference][division].keys() and newteamname not in inchockeyarray[leaguename][conference][division].keys():
  oldfullteamname = GetFullTeamName(inchockeyarray[leaguename][conference][division][oldteamname]['teaminfo']['name'], inchockeyarray[leaguename][conference][division][oldteamname]['teaminfo']['prefix'], inchockeyarray[leaguename][conference][division][oldteamname]['teaminfo']['suffix']);
  inchockeyarray[leaguename][conference][division][newteamname] = inchockeyarray[leaguename][conference][division].pop(str(oldteamname));
  inchockeyarray[leaguename]['quickinfo']['teaminfo'][newteamname] = inchockeyarray[leaguename]['quickinfo']['teaminfo'].pop(str(oldteamname));
  inchockeyarray[leaguename][conference][division][newteamname]['teaminfo']['name'] = str(newteamname);
  if(cityname is not None):
   inchockeyarray[leaguename][conference][division][newteamname]['teaminfo']['city'] = str(cityname);
  if(areaname is not None):
   inchockeyarray[leaguename][conference][division][newteamname]['teaminfo']['area'] = str(areaname);
  if(countryname is not None):
   inchockeyarray[leaguename][conference][division][newteamname]['teaminfo']['country'] = str(countryname);
  if(fullcountryname is not None):
   inchockeyarray[leaguename][conference][division][newteamname]['teaminfo']['fullcountry'] = str(fullcountryname);
  if(fullareaname is not None):
   inchockeyarray[leaguename][conference][division][newteamname]['teaminfo']['fullarea'] = str(fullareaname);
  if(arenaname is not None):
   inchockeyarray[leaguename][conference][division][newteamname]['teaminfo']['arena'] = str(arenaname);
  if(teamnameprefix is not None):
   inchockeyarray[leaguename][conference][division][newteamname]['teaminfo']['prefix'] = str(teamnameprefix);
  if(teamnamesuffix is not None):
   inchockeyarray[leaguename][conference][division][newteamname]['teaminfo']['suffix'] = str(teamnamesuffix);
  if(teamaffiliates is not None):
   inchockeyarray[leaguename][conference][division][newteamname]['teaminfo']['affiliates'] = str(teamaffiliates);
  htin = inchockeyarray[leaguename][conference][division]['teamlist'].index(str(oldteamname));
  inchockeyarray[leaguename][conference][division]['teamlist'][htin] = str(newteamname);
  newfullteamname = GetFullTeamName(inchockeyarray[leaguename][conference][division][newteamname]['teaminfo']['name'], inchockeyarray[leaguename][conference][division][newteamname]['teaminfo']['prefix'], inchockeyarray[leaguename][conference][division][newteamname]['teaminfo']['suffix']);
  inchockeyarray[leaguename]['quickinfo']['teaminfo'][newteamname]['fullname'] = str(newfullteamname);
  for hgkey in inchockeyarray[leaguename]['games']:
   if(hgkey['hometeam']==oldfullteamname):
    hgkey['hometeam'] = newfullteamname;
   if(hgkey['awayteam']==oldfullteamname):
    hgkey['hometeam'] = newfullteamname;
 return inchockeyarray;

def MoveHockeyTeamToConferenceFromArray(inhockeyarray, leaguename, teamname, oldconference, newconference, division):
 inchockeyarray = inhockeyarray.copy();
 if leaguename in inchockeyarray.keys() and newconference in inchockeyarray[leaguename].keys() and oldconference in inchockeyarray[leaguename].keys() and division in inchockeyarray[leaguename][oldconference].keys() and teamname in inchockeyarray[leaguename][oldconference][division].keys() and teamname not in inchockeyarray[leaguename][newconference][division].keys():
  inchockeyarray[leaguename][newconference][division][teamname] = inchockeyarray[leaguename][oldconference][division].pop(str(teamname));
  inchockeyarray[leaguename][newconference][division][teamname]['teaminfo']['conference'] = str(newconference);
  inchockeyarray[leaguename]['quickinfo']['teaminfo'][teamname]['conference'] = str(newconference);
 return inchockeyarray;

def MoveHockeyTeamToDivisionFromArray(inhockeyarray, leaguename, teamname, conference, olddivision, newdivision):
 inchockeyarray = inhockeyarray.copy();
 if leaguename in inchockeyarray.keys() and conference in inchockeyarray[leaguename].keys() and olddivision in inchockeyarray[leaguename][conference].keys() and newdivision in inchockeyarray[leaguename][conference].keys() and teamname in inchockeyarray[leaguename][conference][olddivision].keys() and teamname not in inchockeyarray[leaguename][conference][newdivision].keys():
  inchockeyarray[leaguename][conference][newdivision][teamname] = inchockeyarray[leaguename][conference][olddivision].pop(str(teamname));
  inchockeyarray[leaguename][conference][division][teamname]['teaminfo']['division'] = str(newdivision);
  inchockeyarray[leaguename]['quickinfo']['teaminfo'][teamname]['division'] = str(newdivision);
 return inchockeyarray;

def MakeHockeyTeamTable(sqldatacon, leaguename, droptable=True):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 if(droptable):
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
 "  GamesPlayed INTEGER NOT NULL DEFAULT 0\n" + \
 ");");
 if(droptable):
  sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Teams");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Teams (\n" + \
 "  id INTEGER PRIMARY KEY AUTOINCREMENT,\n" + \
 "  Date INTEGER NOT NULL DEFAULT 0,\n" + \
 "  Time INTEGER NOT NULL DEFAULT 0,\n" + \
 "  DateTime INTEGER NOT NULL DEFAULT 0,\n" + \
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
 "  ConferenceFullName TEXT NOT NULL DEFAULT '',\n" +
 "  Division TEXT NOT NULL DEFAULT '',\n" + \
 "  DivisionFullName TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueName TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueFullName TEXT NOT NULL DEFAULT '',\n" + \
 "  ArenaName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullArenaName TEXT NOT NULL DEFAULT '',\n" + \
 "  Affiliates TEXT NOT NULL DEFAULT '',\n" + \
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
 if(droptable):
  sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Stats");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Stats (\n" + \
 "  id INTEGER PRIMARY KEY AUTOINCREMENT,\n" + \
 "  TeamID INTEGER NOT NULL DEFAULT 0,\n" + \
 "  Date INTEGER NOT NULL DEFAULT 0,\n" + \
 "  Time INTEGER NOT NULL DEFAULT 0,\n" + \
 "  DateTime INTEGER NOT NULL DEFAULT 0,\n" + \
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
 "  ConferenceFullName TEXT NOT NULL DEFAULT '',\n" +
 "  Division TEXT NOT NULL DEFAULT '',\n" + \
 "  DivisionFullName TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueName TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueFullName TEXT NOT NULL DEFAULT '',\n" + \
 "  ArenaName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullArenaName TEXT NOT NULL DEFAULT '',\n" + \
 "  Affiliates TEXT NOT NULL DEFAULT '',\n" + \
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
 if(droptable):
  sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"GameStats");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"GameStats (\n" + \
 "  id INTEGER PRIMARY KEY AUTOINCREMENT,\n" + \
 "  GameID INTEGER NOT NULL DEFAULT 0,\n" + \
 "  Date INTEGER NOT NULL DEFAULT 0,\n" + \
 "  Time INTEGER NOT NULL DEFAULT 0,\n" + \
 "  DateTime INTEGER NOT NULL DEFAULT 0,\n" + \
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
 "  ConferenceFullName TEXT NOT NULL DEFAULT '',\n" +
 "  Division TEXT NOT NULL DEFAULT '',\n" + \
 "  DivisionFullName TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueName TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueFullName TEXT NOT NULL DEFAULT '',\n" + \
 "  ArenaName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullArenaName TEXT NOT NULL DEFAULT '',\n" + \
 "  Affiliates TEXT NOT NULL DEFAULT '',\n" + \
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

def MakeHockeyTeam(sqldatacon, leaguename, date, cityname, areaname, countryname, fullcountryname, fullareaname, teamname, conference, division, arenaname, teamnameprefix="", teamnamesuffix="", teamaffiliates="", hasconferences=True, hasdivisions=True):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 date = str(date);
 chckyear = date[:4];
 chckmonth = date[4:6];
 chckday = date[6:8];
 fullteamname = GetFullTeamName(teamname, teamnameprefix, teamnamesuffix);
 conferencefullname = GetConferenceName(sqldatacon, leaguename, conference);
 divisionfullname = GetDivisionName(sqldatacon, leaguename, division, conference);
 leaguefullname = GetLeagueName(sqldatacon, leaguename);
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Teams (Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES \n" + \
 "(\""+str(chckyear+chckmonth+"00")+"\", 0, \""+str(chckyear+chckmonth+"000000")+"\", \""+str(fullteamname)+"\", \""+str(cityname)+"\", \""+str(teamnameprefix)+"\", \""+str(teamnamesuffix)+"\", \""+str(areaname)+"\", \""+str(countryname)+"\", \""+str(fullcountryname)+"\", \""+str(cityname+", "+areaname)+"\", \""+str(fullareaname)+"\", \""+str(cityname+", "+fullareaname)+"\", \""+str(teamname)+"\", \""+str(conference)+"\", \""+str(conferencefullname)+"\", \""+str(division)+"\", \""+str(divisionfullname)+"\", \""+str(leaguename)+"\", \""+str(leaguefullname)+"\", \""+str(arenaname)+"\", \""+str(arenaname+", "+cityname)+"\", \""+str(teamaffiliates)+"\", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \"0:0:0:0\", \"0:0:0:0\", \"0:0\", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \"0:0:0:0\", \"None\")");
 try:
  TeamID = int(sqldatacon[0].lastrowid);
 except AttributeError:
  TeamID = int(sqldatacon[1].last_insert_rowid());
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Stats (TeamID, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak)\n" + \
 "SELECT id, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE FullName=\""+str(fullteamname)+"\";");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Arenas (TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES \n" + \
 "("+str(TeamID)+", \""+str(teamname)+"\", \""+str(fullteamname)+"\", \""+str(cityname)+"\", \""+str(areaname)+"\", \""+str(countryname)+"\", \""+str(fullcountryname)+"\", \""+str(cityname+", "+areaname)+"\", \""+str(fullareaname)+"\", \""+str(cityname+", "+fullareaname)+"\", \""+str(arenaname)+"\", \""+str(arenaname+", "+cityname)+"\", 0)");
 if(hasconferences):
  UpdateConferenceData(sqldatacon, leaguename, conference, "NumberOfTeams", 1, "+");
 if(hasdivisions):
  UpdateDivisionData(sqldatacon, leaguename, division, "NumberOfTeams", 1, "+");
 UpdateLeagueData(sqldatacon, leaguename, "NumberOfTeams", 1, "+");
 return True;

def MakeHockeyPlayoffTeamTable(sqldatacon, leaguename, droptable=True):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 if(droptable):
  sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"PlayoffTeams");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"PlayoffTeams (\n" + \
 "  id INTEGER PRIMARY KEY AUTOINCREMENT,\n" + \
 "  TeamID INTEGER NOT NULL DEFAULT 0,\n" + \
 "  Date INTEGER NOT NULL DEFAULT 0,\n" + \
 "  Time INTEGER NOT NULL DEFAULT 0,\n" + \
 "  DateTime INTEGER NOT NULL DEFAULT 0,\n" + \
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
 "  ConferenceFullName TEXT NOT NULL DEFAULT '',\n" +
 "  Division TEXT NOT NULL DEFAULT '',\n" + \
 "  DivisionFullName TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueName TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueFullName TEXT NOT NULL DEFAULT '',\n" + \
 "  ArenaName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullArenaName TEXT NOT NULL DEFAULT '',\n" + \
 "  Affiliates TEXT NOT NULL DEFAULT '',\n" + \
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
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 playoffspl = playofffmt.split(',');
 playoffcnt = 0;
 while(playoffcnt<len(playoffspl)):
  subplayoffspl = playoffspl[playoffcnt].split('=');
  subsubplayoffspl = subplayoffspl[0].split(":")
  if(subsubplayoffspl[0]=="League"):
   sqldatacon[0].execute("INSERT INTO "+leaguename+"PlayoffTeams (TeamID, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak)\n" + \
   "SELECT id, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE NOT EXISTS(SELECT TeamID FROM "+leaguename+"PlayoffTeams WHERE "+leaguename+"PlayoffTeams.TeamID = "+leaguename+"Teams.id) ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC LIMIT "+subplayoffspl[1]+";");
  if(subsubplayoffspl[0]=="Conference"):
   conferencecur = sqldatacon[1].cursor();
   if(len(subsubplayoffspl)==1):
    getconference = conferencecur.execute("SELECT Conference FROM "+leaguename+"Conferences WHERE LeagueName=\""+str(leaguename)+"\"");
   if(len(subsubplayoffspl)>1):
    getconference = conferencecur.execute("SELECT Conference FROM "+leaguename+"Conferences WHERE LeagueName=\""+str(leaguename)+"\" AND Conference=\""+str(subsubplayoffspl[1])+"\"");
   for conferenceinfo in getconference:
    sqldatacon[0].execute("INSERT INTO "+leaguename+"PlayoffTeams (TeamID, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak)\n" + \
    "SELECT id, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE Conference=\""+str(conferenceinfo[0])+"\" AND NOT EXISTS(SELECT TeamID FROM "+leaguename+"PlayoffTeams WHERE "+leaguename+"PlayoffTeams.TeamID = "+leaguename+"Teams.id) ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC LIMIT "+str(subplayoffspl[1])+";");
   conferencecur.close();
  if(subsubplayoffspl[0]=="Division"):
   divisioncur = sqldatacon[1].cursor();
   if(len(subsubplayoffspl)==1):
    getdivision = divisioncur.execute("SELECT Division FROM "+leaguename+"Divisions WHERE LeagueName=\""+str(leaguename)+"\"");
   if(len(subsubplayoffspl)>1):
    getdivision = divisioncur.execute("SELECT Division FROM "+leaguename+"Divisions WHERE LeagueName=\""+str(leaguename)+"\" AND Division=\""+str(subsubplayoffspl[1])+"\"");
   for divisioninfo in getdivision:
    sqldatacon[0].execute("INSERT INTO "+leaguename+"PlayoffTeams (TeamID, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak)\n" + \
    "SELECT id, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE Division=\""+str(divisioninfo[0])+"\" AND NOT EXISTS(SELECT TeamID FROM "+leaguename+"PlayoffTeams WHERE "+leaguename+"PlayoffTeams.TeamID = "+leaguename+"Teams.id) ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC LIMIT "+str(subplayoffspl[1])+";");
   divisioncur.close();
  playoffcnt = playoffcnt + 1;
 return True;

def MakeHockeyStandingsTable(sqldatacon, leaguename, date, droptable=True):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 if(droptable):
  sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Standings");
 SelectWhere = "";
 try:
  if(date.isdigit()):
   date = int(date);
 except AttributeError:
  SelectWhere = "";
 if(isinstance(date, baseint) and len(str(date))==8):
  SelectWhere = "WHERE Date<="+date;
 sqldatacon[0].execute("CREATE TEMP TABLE "+leaguename+"Standings AS SELECT * FROM "+leaguename+"Stats "+SelectWhere+" GROUP BY TeamID ORDER BY TeamID ASC, Date DESC");
 return True;

def MakeHockeyStandings(sqldatacon, leaguename, date, droptable=True):
 return MakeHockeyStandingsTable(sqldatacon, leaguename, date, droptable);

def AddHockeyArenaToArray(inhockeyarray, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, arenaname):
 inchockeyarray = inhockeyarray.copy();
 if leaguename in inchockeyarray.keys():
  if "arenas" not in inchockeyarray[leaguename].keys():
   inchockeyarray[leaguename].update( { 'arenas': [ {} ] } );
  inchockeyarray[leaguename]['arenas'].append( { 'city': str(cityname), 'area': str(areaname), 'fullarea': str(fullareaname), 'country': str(countryname), 'fullcountry': str(fullcountryname), 'name': str(arenaname) } );
 return inchockeyarray;

def MakeHockeyArena(sqldatacon, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, arenaname):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Arenas (TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES \n" + \
 "(0, \"\", \"\", \""+str(cityname)+"\", \""+str(areaname)+"\", \""+str(countryname)+"\", \""+str(fullcountryname)+"\", \""+str(cityname+", "+areaname)+"\", \""+str(fullareaname)+"\", \""+str(cityname+", "+fullareaname)+"\", \""+str(arenaname)+"\", \""+str(arenaname+", "+cityname)+"\", 0)");
 return True;

def AddHockeyGameToArray(inhockeyarray, leaguename, date, time, hometeam, awayteam, periodsscore, shotsongoal, ppgoals, shgoals, periodpens, periodpims, periodhits, takeaways, faceoffwins, atarena, isplayoffgame):
 inchockeyarray = inhockeyarray.copy();
 if leaguename in inchockeyarray.keys():
  if "games" not in inchockeyarray[leaguename].keys():
   inchockeyarray[leaguename].update( { 'games': [ {} ] } );
 inchockeyarray[leaguename]['games'].append( { 'date': str(date), 'time': str(date), 'hometeam': str(hometeam), 'awayteam': str(awayteam), 'goals': str(periodsscore), 'sogs': str(shotsongoal), 'ppgs': str(ppgoals), 'shgs': str(shgoals), 'penalties': str(periodpens), 'pims': str(periodpims), 'hits': str(periodhits), 'takeaways': str(takeaways), 'faceoffwins': str(faceoffwins), 'atarena': str(atarena), 'isplayoffgame': str(isplayoffgame) } );
 return inchockeyarray;

def MakeHockeyGameTable(sqldatacon, leaguename, droptable=True):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 if(droptable):
  sqldatacon[0].execute("DROP TABLE IF EXISTS "+leaguename+"Games");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Games (\n" + \
 "  id INTEGER PRIMARY KEY AUTOINCREMENT,\n" + \
 "  Date INTEGER NOT NULL DEFAULT 0,\n" + \
 "  Time INTEGER NOT NULL DEFAULT 0,\n" + \
 "  DateTime INTEGER NOT NULL DEFAULT 0,\n" + \
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
 "  IsPlayOffGame INTEGER NOT NULL DEFAULT 0\n" + \
 ");");
 return True;

def MakeHockeyGame(sqldatacon, leaguename, date, time, hometeam, awayteam, periodsscore, shotsongoal, ppgoals, shgoals, periodpens, periodpims, periodhits, takeaways, faceoffwins, atarena, isplayoffgame):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 if(isplayoffgame.isdigit()):
  isplayoffgame = int(isplayoffgame);
 if(isplayoffgame==0 or isplayoffgame=="0"):
  isplayoffgame = False;
 if(isplayoffgame==1 or isplayoffgame=="1"):
  isplayoffgame = True;
 if(isplayoffgame==2 or isplayoffgame=="2"):
  isplayoffgame = None;
 isplayoffgsql = "0";
 if(isplayoffgame):
  isplayoffgsql = "1";
 if(not isplayoffgame):
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
  if(isplayoffgame and periodcounting > 3):
   homescore = homescore + int(periodscoresplit[0]);
   awayscore = awayscore + int(periodscoresplit[1]);
  if(not isplayoffgame and periodcounting > 3):
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
 hometeaminfo = sqldatacon[0].execute("SELECT Date, GamesPlayed, GamesPlayedHome, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Ties, ShutoutWins, ShutoutLosses, ROW, ROT, Wins, TWins, Points, Losses, TLosses, OTWins, OTSOWins, OTLosses, OTSOLosses, SOWins, SOLosses, PCT, LastTen, Streak, HomeRecord, AwayRecord, Shootouts, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates FROM "+leaguename+"Teams WHERE id="+str(hometeam)).fetchone();
 awayteaminfo = sqldatacon[0].execute("SELECT Date, GamesPlayed, GamesPlayedHome, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Ties, ShutoutWins, ShutoutLosses, ROW, ROT, Wins, TWins, Points, Losses, TLosses, OTWins, OTSOWins, OTLosses, OTSOLosses, SOWins, SOLosses, PCT, LastTen, Streak, HomeRecord, AwayRecord, Shootouts, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates FROM "+leaguename+"Teams WHERE id="+str(awayteam)).fetchone();
 if(atarena.isdigit()):
  atarena = int(atarena);
 if(atarena==0):
  atarena = hometeam;
  atarenaname = hometeaminfo[73];
 if(atarena==-1):
  atarena = awayteam;
  atarenaname = awayteaminfo[73];
 if(isinstance(atarena, baseint) and atarena>0):
  atarenaname = GetNum2Arena(sqldatacon, leaguename, atarena, "FullArenaName");
 if(isinstance(atarena, basestring)):
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
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Games (Date, Time, DateTime, HomeTeam, AwayTeam, AtArena, TeamScorePeriods, TeamFullScore, ShotsOnGoal, FullShotsOnGoal, ShotsBlocked, FullShotsBlocked, PowerPlays, FullPowerPlays, ShortHanded, FullShortHanded, Penalties, FullPenalties, PenaltyMinutes, FullPenaltyMinutes, HitsPerPeriod, FullHitsPerPeriod, TakeAways, FullTakeAways, GiveAways, FullGiveAways, FaceoffWins, FullFaceoffWins, NumberPeriods, TeamWin, TeamLost, TieGame, IsPlayOffGame) VALUES \n" + \
 "("+str(date)+", "+str(time)+", "+str(str(date)+str(time))+", \""+str(hometeamname)+"\", \""+str(awayteamname)+"\", \""+str(atarenaname)+"\", \""+str(periodsscore)+"\", \""+str(totalscore)+"\", \""+str(shotsongoal)+"\", \""+str(totalsog)+"\", \""+str(sbstr)+"\", \""+str(tsbstr)+"\", \""+str(ppgoals)+"\", \""+str(totalppg)+"\", \""+str(shgoals)+"\", \""+str(totalshg)+"\", \""+str(periodpens)+"\", \""+str(totalpens)+"\", \""+str(periodpims)+"\", \""+str(totalpims)+"\", \""+str(periodhits)+"\", \""+str(totalhits)+"\", \""+str(takeaways)+"\", \""+str(totaltaws)+"\", \""+str(gaws_str)+"\", \""+str(totalgaws)+"\", \""+str(faceoffwins)+"\", \""+str(totalfows)+"\", "+str(numberofperiods)+", \""+str(winningteamname)+"\", \""+str(losingteamname)+"\", \""+str(tiegame)+"\", "+str(isplayoffgsql)+")");
 try:
  GameID = int(sqldatacon[0].lastrowid);
 except AttributeError:
  GameID = int(sqldatacon[1].last_insert_rowid());
 hometeamupdatedict = { 'Date': int(date), 'GamesPlayed': int(hometeaminfo[1]) + 1, 'GamesPlayedHome': int(hometeaminfo[2]) + 1, 'GoalsFor': int(hometeaminfo[3]) + int(teamscores[0]), 'GoalsAgainst': int(hometeaminfo[4]) + int(teamscores[1]), 'GoalsDifference': int(hometeaminfo[5]) + int(int(teamscores[0]) - int(teamscores[1])), 'SOGFor': int(hometeaminfo[6]) + int(teamssog[0]), 'SOGAgainst': int(hometeaminfo[7]) + int(teamssog[1]), 'SOGDifference': int(hometeaminfo[8]) + int(int(teamssog[0]) - int(teamssog[1])), 'ShotsBlockedFor': int(hometeaminfo[9]) + int(hometsb), 'ShotsBlockedAgainst': int(hometeaminfo[10]) + int(awaytsb), 'ShotsBlockedDifference': int(hometeaminfo[11]) + int(int(hometsb) - int(awaytsb)), 'PPGFor': int(hometeaminfo[12]) + int(homeppg), 'PPGAgainst': int(hometeaminfo[13]) + int(awayppg), 'PPGDifference': int(hometeaminfo[14]) + int(int(homeppg) - int(awayppg)), 'SHGFor': int(hometeaminfo[15]) + int(homeshg), 'SHGAgainst': int(hometeaminfo[16]) + int(awayshg), 'SHGDifference': int(hometeaminfo[17]) + int(int(homeshg) - int(awayshg)), 'PenaltiesFor': int(hometeaminfo[18]) + int(awaypens), 'PenaltiesAgainst': int(hometeaminfo[19]) + int(homepens), 'PenaltiesDifference': int(hometeaminfo[20]) + int(int(awaypens) - int(homepens)), 'PIMFor': int(hometeaminfo[21]) + int(homepims), 'PIMAgainst': int(hometeaminfo[22]) + int(awaypims), 'PIMDifference': int(hometeaminfo[23]) + int(int(homepims) - int(awaypims)), 'HITSFor': int(hometeaminfo[24]) + int(homehits), 'HITSAgainst': int(hometeaminfo[25]) + int(awayhits), 'HITSDifference': int(hometeaminfo[26]) + int(int(homehits) - int(awayhits)), 'TakeAways': int(hometeaminfo[27]) + int(hometaws), 'GiveAways': int(hometeaminfo[28]) + int(awaytaws), 'TAGADifference': int(hometeaminfo[29]) + int(int(hometaws) - int(awaytaws)), 'FaceoffWins': int(hometeaminfo[30]) + int(homefows), 'FaceoffLosses': int(hometeaminfo[31]) + int(awayfows), 'FaceoffDifference': int(hometeaminfo[32]) + int(int(homefows) - int(awayfows)) };
 awayteamupdatedict = { 'Date': int(date), 'GamesPlayed': int(awayteaminfo[1]) + 1, 'GamesPlayedHome': int(awayteaminfo[2]) + 1, 'GoalsFor': int(awayteaminfo[3]) + int(teamscores[0]), 'GoalsAgainst': int(awayteaminfo[4]) + int(teamscores[1]), 'GoalsDifference': int(awayteaminfo[5]) + int(int(teamscores[0]) - int(teamscores[1])), 'SOGFor': int(awayteaminfo[6]) + int(teamssog[0]), 'SOGAgainst': int(awayteaminfo[7]) + int(teamssog[1]), 'SOGDifference': int(awayteaminfo[8]) + int(int(teamssog[0]) - int(teamssog[1])), 'ShotsBlockedFor': int(awayteaminfo[9]) + int(hometsb), 'ShotsBlockedAgainst': int(awayteaminfo[10]) + int(awaytsb), 'ShotsBlockedDifference': int(awayteaminfo[11]) + int(int(hometsb) - int(awaytsb)), 'PPGFor': int(awayteaminfo[12]) + int(homeppg), 'PPGAgainst': int(awayteaminfo[13]) + int(awayppg), 'PPGDifference': int(awayteaminfo[14]) + int(int(homeppg) - int(awayppg)), 'SHGFor': int(awayteaminfo[15]) + int(homeshg), 'SHGAgainst': int(awayteaminfo[16]) + int(awayshg), 'SHGDifference': int(awayteaminfo[17]) + int(int(homeshg) - int(awayshg)), 'PenaltiesFor': int(awayteaminfo[18]) + int(awaypens), 'PenaltiesAgainst': int(awayteaminfo[19]) + int(homepens), 'PenaltiesDifference': int(awayteaminfo[20]) + int(int(awaypens) - int(homepens)), 'PIMFor': int(awayteaminfo[21]) + int(homepims), 'PIMAgainst': int(awayteaminfo[22]) + int(awaypims), 'PIMDifference': int(awayteaminfo[23]) + int(int(homepims) - int(awaypims)), 'HITSFor': int(awayteaminfo[24]) + int(homehits), 'HITSAgainst': int(awayteaminfo[25]) + int(awayhits), 'HITSDifference': int(awayteaminfo[26]) + int(int(homehits) - int(awayhits)), 'TakeAways': int(awayteaminfo[27]) + int(hometaws), 'GiveAways': int(awayteaminfo[28]) + int(awaytaws), 'TAGADifference': int(awayteaminfo[29]) + int(int(hometaws) - int(awaytaws)), 'FaceoffWins': int(awayteaminfo[30]) + int(homefows), 'FaceoffLosses': int(awayteaminfo[31]) + int(awayfows), 'FaceoffDifference': int(awayteaminfo[32]) + int(int(homefows) - int(awayfows)) };
 UpdateArenaData(sqldatacon, leaguename, atarena, "GamesPlayed", 1, "+");
 if(tiegame==1):
  hometeamupdatedict.update( { 'Ties': int(hometeaminfo[33]) + 1 } );
  awayteamupdatedict.update( { 'Ties': int(awayteaminfo[33]) + 1 } );
 if(winningteam==hometeam and int(teamscores[1])==0):
  hometeamupdatedict.update( { 'ShutoutWins': int(hometeaminfo[33]) + 1 } );
  awayteamupdatedict.update( { 'ShutoutLosses': int(awayteaminfo[33]) + 1 } );
 if(winningteam==awayteam and int(teamscores[0])==0):
  hometeamupdatedict.update( { 'ShutoutLosses': int(hometeaminfo[33]) + 1 } );
  awayteamupdatedict.update( { 'ShutoutWins': int(awayteaminfo[33]) + 1 } );
 hometeamupdatedict.update( { 'LastTen': GetLastGamesWithShootout(sqldatacon, leaguename, winningteamname) } );
 awayteamupdatedict.update( { 'LastTen': GetLastGamesWithShootout(sqldatacon, leaguename, losingteamname) } );
 if(tiegame==0):
  if(hometeam==winningteam):
   GetWinningStreak = hometeaminfo[51];
  if(awayteam==winningteam):
   GetWinningStreak = awayteaminfo[51];
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
  if(hometeam==winningteam):
   hometeamupdatedict.update( { 'Streak': GetWinningStreakNext } );
  if(awayteam==winningteam):
   awayteamupdatedict.update( { 'Streak': GetWinningStreakNext } );
  if(hometeam==losingteam):
   GetLosingStreak = hometeaminfo[51];
  if(awayteam==losingteam):
   GetLosingStreak = awayteaminfo[51];
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
  if(hometeam==losingteam):
   hometeamupdatedict.update( { 'Streak': GetLosingStreakNext } );
  if(awayteam==losingteam):
   awayteamupdatedict.update( { 'Streak': GetLosingStreakNext } );
 if(tiegame==1):
  GetWinningStreak = hometeaminfo[51];
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
  hometeamupdatedict.update( { 'Streak': GetWinningStreakNext } );
  GetLosingStreak = awayteaminfo[51];
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
  awayteamupdatedict.update( { 'Streak': GetLosingStreakNext } );
 if((not isplayoffgame and numberofperiods<5 and tiegame==0) or (isplayoffgame and tiegame==0)):
  if(hometeam==winningteam):
   hometeamupdatedict.update( { 'ROW': int(hometeaminfo[36]) + 1 } );
  if(awayteam==winningteam):
   awayteamupdatedict.update( { 'ROW': int(awayteaminfo[36]) + 1 } );
  if(hometeam==losingteam):
   hometeamupdatedict.update( { 'ROT': int(hometeaminfo[37]) + 1 } );
  if(awayteam==losingteam):
   awayteamupdatedict.update( { 'ROT': int(awayteaminfo[37]) + 1 } );
 if(numberofperiods==3 and tiegame==0):
  if(hometeam==winningteam):
   hometeamupdatedict.update( { 'Wins': int(hometeaminfo[38]) + 1, 'TWins': int(hometeaminfo[39]) + 1, 'Points': int(hometeaminfo[40]) + 1 } );
  if(awayteam==winningteam):
   awayteamupdatedict.update( { 'Wins': int(awayteaminfo[38]) + 1, 'TWins': int(awayteaminfo[39]) + 1, 'Points': int(awayteaminfo[40]) + 1 } );
  if(hometeam==losingteam):
   hometeamupdatedict.update( { 'Losses': int(hometeaminfo[41]) + 1, 'TLosses': int(hometeaminfo[42]) + 1, 'Points': int(hometeaminfo[40]) + 0 } );
  if(awayteam==losingteam):
   awayteamupdatedict.update( { 'Losses': int(awayteaminfo[37]) + 1, 'TLosses': int(awayteaminfo[37]) + 1, 'Points': int(awayteaminfo[40]) + 0 } );
  if(winningteam==hometeam):
   HomeTeamRecord = hometeaminfo[52];
   HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
   NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2])+":"+str(HTRSpit[3]);
   hometeamupdatedict.update( { 'HomeRecord': NewHTR } );
   AwayTeamRecord = awayteaminfo[53];
   ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
   NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1] + 1)+":"+str(ATRSpit[2])+":"+str(ATRSpit[3]);
   awayteamupdatedict.update( { 'AwayRecord': NewATR } );
  if(losingteam==hometeam):
   HomeTeamRecord = awayteaminfo[53];
   HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
   NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2])+":"+str(HTRSpit[3]);
   awayteamupdatedict.update( { 'AwayRecord': NewHTR } );
   AwayTeamRecord = hometeaminfo[52];
   ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
   NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1] + 1)+":"+str(ATRSpit[2])+":"+str(ATRSpit[3]);
   hometeamupdatedict.update( { 'HomeRecord': NewATR } );
 if(numberofperiods>3 and tiegame==0):
  if((numberofperiods==4 and not isplayoffgame) or (numberofperiods>4 and isplayoffgame)):
   if(hometeam==winningteam):
    hometeamupdatedict.update( { 'OTWins': int(hometeaminfo[43]) + 1 } );
   if(awayteam==winningteam):
    awayteamupdatedict.update( { 'OTWins': int(awayteaminfo[43]) + 1 } );
  if(hometeam==winningteam):
   hometeamupdatedict.update( { 'OTSOWins': int(hometeaminfo[44]) + 1, 'TWins': int(hometeaminfo[39]) + 1, 'Points': int(hometeaminfo[40]) + 2 } );
  if(awayteam==winningteam):
   awayteamupdatedict.update( { 'OTSOWins': int(awayteaminfo[44]) + 1, 'TWins': int(awayteaminfo[39]) + 1, 'Points': int(awayteaminfo[40]) + 2 } );
  if((numberofperiods==4 and not isplayoffgame) or (numberofperiods>4 and isplayoffgame)):
   if(hometeam==losingteam):
    hometeamupdatedict.update( { 'OTLosses': int(hometeaminfo[43]) + 1 } );
   if(awayteam==losingteam):
    awayteamupdatedict.update( { 'OTLosses': int(awayteaminfo[43]) + 1 } );
  if(hometeam==losingteam):
   hometeamupdatedict.update( { 'OTSOLosses': int(hometeaminfo[44]) + 1, 'TLosses': int(hometeaminfo[39]) + 1, 'Points': int(hometeaminfo[40]) + 1 } );
  if(awayteam==losingteam):
   awayteamupdatedict.update( { 'OTSOLosses': int(awayteaminfo[44]) + 1, 'TLosses': int(awayteaminfo[39]) + 1, 'Points': int(awayteaminfo[40]) + 1 } );
  if(isplayoffgame):
   if(winningteam==hometeam):
    HomeTeamRecord = hometeaminfo[52];
    HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
    NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2])+":"+str(HTRSpit[3]);
    hometeamupdatedict.update( { 'HomeRecord': NewHTR } );
    AwayTeamRecord = awayteaminfo[53];
    ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
    NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1])+":"+str(ATRSpit[2] + 1)+":"+str(ATRSpit[3]);
    awayteamupdatedict.update( { 'AwayRecord': NewATR } );
   if(losingteam==hometeam):
    HomeTeamRecord = awayteaminfo[53];
    HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
    NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2])+":"+str(HTRSpit[3]);
    awayteamupdatedict.update( { 'AwayRecord': NewHTR } );
    AwayTeamRecord = hometeaminfo[52];
    ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
    NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1])+":"+str(ATRSpit[2] + 1)+":"+str(ATRSpit[3]);
    hometeamupdatedict.update( { 'HomeRecord': NewATR } );
  if(not isplayoffgame and numberofperiods==4):
   if(winningteam==hometeam):
    HomeTeamRecord = hometeaminfo[52];
    HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
    NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2])+":"+str(HTRSpit[3]);
    hometeamupdatedict.update( { 'HomeRecord': NewHTR } );
    AwayTeamRecord = awayteaminfo[53];
    ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
    NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1])+":"+str(ATRSpit[2] + 1)+":"+str(ATRSpit[3]);
    awayteamupdatedict.update( { 'AwayRecord': NewATR } );
   if(losingteam==hometeam):
    HomeTeamRecord = awayteaminfo[53];
    HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
    NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2])+":"+str(HTRSpit[3]);
    awayteamupdatedict.update( { 'AwayRecord': NewHTR } );
    AwayTeamRecord = hometeaminfo[52];
    ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
    NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1])+":"+str(ATRSpit[2] + 1)+":"+str(ATRSpit[3]);
    hometeamupdatedict.update( { 'HomeRecord': NewATR } );
  if(not isplayoffgame and numberofperiods>4):
   if(winningteam==hometeam):
    HomeTeamRecord = hometeaminfo[52];
    HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
    NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2])+":"+str(HTRSpit[3]);
    hometeamupdatedict.update( { 'HomeRecord': NewHTR } );
    AwayTeamRecord = awayteaminfo[53];
    ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
    NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1])+":"+str(ATRSpit[2])+":"+str(ATRSpit[3] + 1);
    awayteamupdatedict.update( { 'AwayRecord': NewATR } );
   if(losingteam==hometeam):
    HomeTeamRecord = awayteaminfo[53];
    HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
    NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2])+":"+str(HTRSpit[3]);
    awayteamupdatedict.update( { 'AwayRecord': NewHTR } );
    AwayTeamRecord = hometeaminfo[52];
    ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
    NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1])+":"+str(ATRSpit[2])+":"+str(ATRSpit[3] + 1);
    hometeamupdatedict.update( { 'HomeRecord': NewATR } );
 if(not isplayoffgame and numberofperiods>4 and tiegame==0):
  if(hometeam==winningteam):
   hometeamupdatedict.update( { 'SOWins': int(hometeaminfo[47]) + 1 } );
  if(awayteam==winningteam):
   awayteamupdatedict.update( { 'SOWins': int(hometeaminfo[47]) + 1 } );
  if(hometeam==losingteam):
   hometeamupdatedict.update( { 'SOLosses': int(hometeaminfo[48]) + 1 } );
  if(awayteam==losingteam):
   awayteamupdatedict.update( { 'SOLosses': int(hometeaminfo[48]) + 1 } );
  if(hometeam==winningteam):
   WinningTeamShootouts = hometeaminfo[54];
   WTSoSplit = [int(n) for n in WinningTeamShootouts.split(":")];
   NewWTSo = str(WTSoSplit[0] + 1)+":"+str(WTSoSplit[1]);
   hometeamupdatedict.update( { 'Shootouts': NewWTSo } );
  if(awayteam==winningteam):
   WinningTeamShootouts = awayteaminfo[54];
   WTSoSplit = [int(n) for n in WinningTeamShootouts.split(":")];
   NewWTSo = str(WTSoSplit[0] + 1)+":"+str(WTSoSplit[1]);
   awayteamupdatedict.update( { 'Shootouts': NewWTSo } );
  if(hometeam==losingteam):
   LosingTeamShootouts = hometeaminfo[54];
   LTSoSplit = [int(n) for n in LosingTeamShootouts.split(":")];
   NewLTSo = str(LTSoSplit[0])+":"+str(LTSoSplit[1] + 1);
   hometeamupdatedict.update( { 'Shootouts': NewLTSo } );
  if(awayteam==losingteam):
   LosingTeamShootouts = awayteaminfo[54];
   LTSoSplit = [int(n) for n in LosingTeamShootouts.split(":")];
   NewLTSo = str(LTSoSplit[0])+":"+str(LTSoSplit[1] + 1);
   awayteamupdatedict.update( { 'Shootouts': NewLTSo } );
 hlist = [];
 for hkey, hvalue in hometeamupdatedict.items():
  if(isinstance(hvalue, basestring)):
   hlist.append(hkey+"=\""+str(hvalue)+"\"");
  elif(isinstance(hvalue, baseint)):
   hlist.append(hkey+"="+str(hvalue));
  elif(isinstance(hvalue, float)):
   hlist.append(hkey+"="+str(hvalue));
  else:
   hlist.append(hkey+"=\""+str(hvalue)+"\"");
 alist = [];
 for akey, avalue in awayteamupdatedict.items():
  if(isinstance(avalue, basestring)):
   alist.append(akey+"=\""+str(avalue)+"\"");
  elif(isinstance(avalue, baseint)):
   alist.append(akey+"="+str(avalue));
  elif(isinstance(avalue, float)):
   alist.append(akey+"="+str(avalue));
  else:
   alist.append(akey+"=\""+str(hvalue)+"\"");
 sqldatacon[0].execute("UPDATE "+leaguename+"Teams SET "+str(",".join(hlist))+" WHERE id="+str(hometeam));
 sqldatacon[0].execute("UPDATE "+leaguename+"Teams SET "+str(",".join(alist))+" WHERE id="+str(awayteam));
 hometeaminfon = sqldatacon[0].execute("SELECT OTSOLosses, TWins, GamesPlayed, Points FROM "+leaguename+"Teams WHERE id="+str(hometeam)).fetchone();
 awayteaminfon = sqldatacon[0].execute("SELECT OTSOLosses, TWins, GamesPlayed, Points FROM "+leaguename+"Teams WHERE id="+str(awayteam)).fetchone();
 HomeOTLossesPCT = float("%.2f" % float(float(0.5) * float(hometeaminfon[0])));
 HomeWinsPCTAlt = float("%.3f" % float(float(hometeaminfon[1] + HomeOTLossesPCT) / float(hometeaminfon[2])));
 HomeWinsPCT = float("%.3f" % float(hometeaminfon[3] / float(hometeaminfon[2] * 2)));
 AwayOTLossesPCT = float("%.2f" % float(float(0.5) * float(awayteaminfon[0])));
 AwayWinsPCTAlt = float("%.3f" % float(float(awayteaminfon[1] + AwayOTLossesPCT) / float(awayteaminfon[2])));
 AwayWinsPCT = float("%.3f" % float(awayteaminfon[3] / float(awayteaminfon[2] * 2)));
 hometeamupdatedict = {};
 awayteamupdatedict = {};
 hometeamupdatedict.update( { 'PCT': HomeWinsPCT } );
 awayteamupdatedict.update( { 'PCT': AwayWinsPCT } );
 hlist = [];
 for hkey, hvalue in hometeamupdatedict.items():
  if(isinstance(hvalue, basestring)):
   hlist.append(hkey+"=\""+str(hvalue)+"\"");
  elif(isinstance(hvalue, baseint)):
   hlist.append(hkey+"="+str(hvalue));
  elif(isinstance(hvalue, float)):
   hlist.append(hkey+"="+str(hvalue));
  else:
   hlist.append(hkey+"=\""+str(hvalue)+"\"");
 alist = [];
 for akey, avalue in awayteamupdatedict.items():
  if(isinstance(avalue, basestring)):
   alist.append(akey+"=\""+str(avalue)+"\"");
  elif(isinstance(avalue, baseint)):
   alist.append(akey+"="+str(avalue));
  elif(isinstance(avalue, float)):
   alist.append(akey+"="+str(avalue));
  else:
   alist.append(akey+"=\""+str(hvalue)+"\"");
 sqldatacon[0].execute("UPDATE "+leaguename+"Teams SET "+str(",".join(hlist))+" WHERE id="+str(hometeam));
 sqldatacon[0].execute("UPDATE "+leaguename+"Teams SET "+str(",".join(alist))+" WHERE id="+str(awayteam));
 sqldatacon[0].execute("INSERT INTO "+leaguename+"GameStats (GameID, Date, Time, DateTime, TeamID, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference) VALUES \n" + \
 "("+str(GameID)+", "+str(date)+", "+str(time)+", "+str(str(date)+str(time))+", "+str(hometeam)+", \""+str(hometeaminfo[55])+"\", \""+str(hometeaminfo[56])+"\", \""+str(hometeaminfo[57])+"\", \""+str(hometeaminfo[58])+"\", \""+str(hometeaminfo[59])+"\", \""+str(hometeaminfo[60])+"\", \""+str(hometeaminfo[61])+"\", \""+str(hometeaminfo[62])+"\", \""+str(hometeaminfo[63])+"\", \""+str(hometeaminfo[64])+"\", \""+str(hometeaminfo[65])+"\", \""+str(hometeaminfo[66])+"\", \""+str(hometeaminfo[67])+"\", \""+str(hometeaminfo[68])+"\", \""+str(hometeaminfo[69])+"\", \""+str(hometeaminfo[70])+"\", \""+str(hometeaminfo[71])+"\", \""+str(hometeaminfo[72])+"\", \""+str(hometeaminfo[73])+"\", \""+str(hometeaminfo[74])+"\", "+str(teamscores[0])+", "+str(teamscores[1])+", "+str(int(teamscores[0]) - int(teamscores[1]))+", "+str(teamssog[0])+", "+str(teamssog[1])+", "+str(int(teamssog[0]) - int(teamssog[1]))+", "+str(hometsb)+", "+str(awaytsb)+", "+str(int(hometsb) - int(awaytsb))+", "+str(homeppg)+", "+str(awayppg)+", "+str(int(homeppg) - int(awayppg))+", "+str(homeshg)+", "+str(awayshg)+", "+str(int(homeshg) - int(awayshg))+", "+str(homepens)+", "+str(awaypens)+", "+str(int(homepens) - int(awaypens))+", "+str(homepims)+", "+str(awaypims)+", "+str(int(homepims) - int(awaypims))+", "+str(homehits)+", "+str(awayhits)+", "+str(int(homehits) - int(awayhits))+", "+str(hometaws)+", "+str(awaytaws)+", "+str(int(hometaws) - int(awaytaws))+", "+str(homefows)+", "+str(awayfows)+", "+str(int(homefows) - int(awayfows))+")");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"GameStats (GameID, Date, Time, DateTime, TeamID, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference) VALUES \n" + \
 "("+str(GameID)+", "+str(date)+", "+str(time)+", "+str(str(date)+str(time))+", "+str(awayteam)+", \""+str(awayteaminfo[55])+"\", \""+str(awayteaminfo[56])+"\", \""+str(awayteaminfo[57])+"\", \""+str(awayteaminfo[58])+"\", \""+str(awayteaminfo[59])+"\", \""+str(awayteaminfo[60])+"\", \""+str(awayteaminfo[61])+"\", \""+str(awayteaminfo[62])+"\", \""+str(awayteaminfo[63])+"\", \""+str(awayteaminfo[64])+"\", \""+str(awayteaminfo[65])+"\", \""+str(awayteaminfo[66])+"\", \""+str(awayteaminfo[67])+"\", \""+str(awayteaminfo[68])+"\", \""+str(awayteaminfo[69])+"\", \""+str(awayteaminfo[70])+"\", \""+str(awayteaminfo[71])+"\", \""+str(awayteaminfo[72])+"\", \""+str(awayteaminfo[73])+"\", \""+str(awayteaminfo[74])+"\", "+str(teamscores[1])+", "+str(teamscores[0])+", "+str(int(teamscores[1]) - int(teamscores[0]))+", "+str(teamssog[1])+", "+str(teamssog[0])+", "+str(int(teamssog[1]) - int(teamssog[0]))+", "+str(awaytsb)+", "+str(hometsb)+", "+str(int(awaytsb) - int(hometsb))+", "+str(awayppg)+", "+str(homeppg)+", "+str(int(awayppg) - int(homeppg))+", "+str(awayshg)+", "+str(homeshg)+", "+str(int(awayshg) - int(homeshg))+", "+str(awaypens)+", "+str(homepens)+", "+str(int(awaypens) - int(homepens))+", "+str(awaypims)+", "+str(homepims)+", "+str(int(awaypims) - int(homepims))+", "+str(awayhits)+", "+str(homehits)+", "+str(int(awayhits) - int(homehits))+", "+str(awaytaws)+", "+str(hometaws)+", "+str(int(awaytaws) - int(hometaws))+", "+str(awayfows)+", "+str(homefows)+", "+str(int(awayfows) - int(homefows))+")");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Stats (TeamID, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak)\n" + \
 "SELECT id, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, Affiliates, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE FullName=\""+str(hometeamname)+"\";");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Stats (TeamID, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak)\n" + \
 "SELECT id, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE FullName=\""+str(awayteamname)+"\";");
 return True;

def MakeHockeyGameOld(sqldatacon, leaguename, date, time, hometeam, awayteam, periodsscore, shotsongoal, ppgoals, shgoals, periodpens, periodpims, periodhits, takeaways, faceoffwins, atarena, isplayoffgame):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 if(isplayoffgame.isdigit()):
  isplayoffgame = int(isplayoffgame);
 if(isplayoffgame==0 or isplayoffgame=="0"):
  isplayoffgame = False;
 if(isplayoffgame==1 or isplayoffgame=="1"):
  isplayoffgame = True;
 if(isplayoffgame==2 or isplayoffgame=="2"):
  isplayoffgame = None;
 isplayoffgsql = "0";
 if(isplayoffgame):
  isplayoffgsql = "1";
 if(not isplayoffgame):
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
  if(isplayoffgame and periodcounting > 3):
   homescore = homescore + int(periodscoresplit[0]);
   awayscore = awayscore + int(periodscoresplit[1]);
  if(not isplayoffgame and periodcounting > 3):
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
 if(isinstance(atarena, baseint) and atarena>0):
  atarenaname = GetNum2Arena(sqldatacon, leaguename, atarena, "FullArenaName");
 if(isinstance(atarena, basestring)):
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
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Games (Date, Time, DateTime, HomeTeam, AwayTeam, AtArena, TeamScorePeriods, TeamFullScore, ShotsOnGoal, FullShotsOnGoal, ShotsBlocked, FullShotsBlocked, PowerPlays, FullPowerPlays, ShortHanded, FullShortHanded, Penalties, FullPenalties, PenaltyMinutes, FullPenaltyMinutes, HitsPerPeriod, FullHitsPerPeriod, TakeAways, FullTakeAways, GiveAways, FullGiveAways, FaceoffWins, FullFaceoffWins, NumberPeriods, TeamWin, TeamLost, TieGame, IsPlayOffGame) VALUES \n" + \
 "("+str(date)+", "+str(time)+", "+str(str(date)+str(time))+", \""+str(hometeamname)+"\", \""+str(awayteamname)+"\", \""+str(atarenaname)+"\", \""+str(periodsscore)+"\", \""+str(totalscore)+"\", \""+str(shotsongoal)+"\", \""+str(totalsog)+"\", \""+str(sbstr)+"\", \""+str(tsbstr)+"\", \""+str(ppgoals)+"\", \""+str(totalppg)+"\", \""+str(shgoals)+"\", \""+str(totalshg)+"\", \""+str(periodpens)+"\", \""+str(totalpens)+"\", \""+str(periodpims)+"\", \""+str(totalpims)+"\", \""+str(periodhits)+"\", \""+str(totalhits)+"\", \""+str(takeaways)+"\", \""+str(totaltaws)+"\", \""+str(gaws_str)+"\", \""+str(totalgaws)+"\", \""+str(faceoffwins)+"\", \""+str(totalfows)+"\", "+str(numberofperiods)+", \""+str(winningteamname)+"\", \""+str(losingteamname)+"\", \""+str(tiegame)+"\", "+str(isplayoffgsql)+")");
 try:
  GameID = int(sqldatacon[0].lastrowid);
 except AttributeError:
  GameID = int(sqldatacon[1].last_insert_rowid());
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
 if((not isplayoffgame and numberofperiods<5 and tiegame==0) or (isplayoffgame and tiegame==0)):
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
  if((numberofperiods==4 and not isplayoffgame) or (numberofperiods>4 and isplayoffgame)):
   UpdateTeamData(sqldatacon, leaguename, winningteam, "OTWins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, winningteam, "OTSOWins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, winningteam, "TWins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, winningteam, "Points", 2, "+");
  if((numberofperiods==4 and not isplayoffgame) or (numberofperiods>4 and isplayoffgame)):
   UpdateTeamData(sqldatacon, leaguename, losingteam, "OTLosses", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "OTSOLosses", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "TLosses", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "Points", 1, "+");
  if(isplayoffgame):
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
  if(not isplayoffgame and numberofperiods==4):
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
  if(not isplayoffgame and numberofperiods>4):
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
 if(not isplayoffgame and numberofperiods>4 and tiegame==0):
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
 sqldatacon[0].execute("INSERT INTO "+leaguename+"GameStats (GameID, Date, Time, DateTime, TeamID, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference) VALUES \n" + \
 "("+str(GameID)+", "+str(date)+", "+str(time)+", "+str(str(date)+str(time))+", "+str(hometeam)+", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "CityName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "TeamPrefix")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "TeamSuffix")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "AreaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "CountryName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullCountryName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullCityName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullAreaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullCityNameAlt")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "TeamName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "Conference")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "ConferenceFullName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "Division")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "DivisionFullName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "LeagueName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "LeagueFullName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "ArenaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullArenaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(hometeam), "Affiliates")+"\", "+str(teamscores[0])+", "+str(teamscores[1])+", "+str(int(teamscores[0]) - int(teamscores[1]))+", "+str(teamssog[0])+", "+str(teamssog[1])+", "+str(int(teamssog[0]) - int(teamssog[1]))+", "+str(hometsb)+", "+str(awaytsb)+", "+str(int(hometsb) - int(awaytsb))+", "+str(homeppg)+", "+str(awayppg)+", "+str(int(homeppg) - int(awayppg))+", "+str(homeshg)+", "+str(awayshg)+", "+str(int(homeshg) - int(awayshg))+", "+str(homepens)+", "+str(awaypens)+", "+str(int(homepens) - int(awaypens))+", "+str(homepims)+", "+str(awaypims)+", "+str(int(homepims) - int(awaypims))+", "+str(homehits)+", "+str(awayhits)+", "+str(int(homehits) - int(awayhits))+", "+str(hometaws)+", "+str(awaytaws)+", "+str(int(hometaws) - int(awaytaws))+", "+str(homefows)+", "+str(awayfows)+", "+str(int(homefows) - int(awayfows))+")");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"GameStats (GameID, Date, Time, DateTime, TeamID, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference) VALUES \n" + \
 "("+str(GameID)+", "+str(date)+", "+str(time)+", "+str(str(date)+str(time))+", "+str(awayteam)+", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "CityName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "TeamPrefix")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "TeamSuffix")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "AreaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "CountryName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullCountryName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullCityName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullAreaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullCityNameAlt")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "TeamName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "Conference")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "ConferenceFullName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "Division")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "DivisionFullName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "LeagueName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "LeagueFullName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "ArenaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullArenaName")+"\", \""+GetNum2Team(sqldatacon, leaguename, int(awayteam), "Affiliates")+"\", "+str(teamscores[1])+", "+str(teamscores[0])+", "+str(int(teamscores[1]) - int(teamscores[0]))+", "+str(teamssog[1])+", "+str(teamssog[0])+", "+str(int(teamssog[1]) - int(teamssog[0]))+", "+str(awaytsb)+", "+str(hometsb)+", "+str(int(awaytsb) - int(hometsb))+", "+str(awayppg)+", "+str(homeppg)+", "+str(int(awayppg) - int(homeppg))+", "+str(awayshg)+", "+str(homeshg)+", "+str(int(awayshg) - int(homeshg))+", "+str(awaypens)+", "+str(homepens)+", "+str(int(awaypens) - int(homepens))+", "+str(awaypims)+", "+str(homepims)+", "+str(int(awaypims) - int(homepims))+", "+str(awayhits)+", "+str(homehits)+", "+str(int(awayhits) - int(homehits))+", "+str(awaytaws)+", "+str(hometaws)+", "+str(int(awaytaws) - int(hometaws))+", "+str(awayfows)+", "+str(homefows)+", "+str(int(awayfows) - int(homefows))+")");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Stats (TeamID, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak)\n" + \
 "SELECT id, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, Affiliates, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE FullName=\""+str(hometeamname)+"\";");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Stats (TeamID, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak)\n" + \
 "SELECT id, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE FullName=\""+str(awayteamname)+"\";");
 return True;

if(not enable_old_makegame):
 MakeHockeyGame = MakeHockeyGameOld;

def CloseHockeyDatabase(sqldatacon):
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 db_integrity_check = sqldatacon[0].execute("PRAGMA integrity_check(100);").fetchone()[0];
 sqldatacon[0].execute("PRAGMA optimize;");
 sqldatacon[0].close();
 sqldatacon[1].close();
 if(db_integrity_check=="ok"):
  return True;
 else:
  return False;
