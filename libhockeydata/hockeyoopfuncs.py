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

    $FileInfo: hockeyoopfuncs.py - Last Update: 1/15/2021 Ver. 0.5.0 RC 1 - Author: cooldude2k $
'''

from .hockeyfunctions import *;

''' // Object-oriented classes and functions by Kazuki Przyborowski '''
class MakeHockeyArray:
 def __init__(self, databasename="./hockeydatabase.db3"):
  self.hockeyarray = CreateHockeyArray(databasename);
 def AddHockeyLeague(self, leaguename, leaguefullname, countryname, fullcountryname, date, playofffmt, ordertype, hasconferences="yes", hasdivisions="yes"):
  self.hockeyarray = AddHockeyLeagueToArray(self.hockeyarray, leaguename, leaguefullname, countryname, fullcountryname, date, playofffmt, ordertype, hasconferences, hasdivisions);
 def RemoveHockeyLeague(self, leaguename):
  self.hockeyarray = RemoveHockeyLeagueFromArray(self.hockeyarray, leaguename);
 def ReplaceHockeyLeague(oldleaguename, newleaguename, leaguefullname=None, countryname=None, fullcountryname=None, date=None, playofffmt=None, ordertype=None, hasconferences=None, hasdivisions=None):
  self.hockeyarray = ReplaceHockeyLeagueFromArray(self.hockeyarray, oldleaguename, newleaguename, leaguefullname, countryname, fullcountryname, date, playofffmt, ordertype, hasconferences, hasdivisions);
 def AddHockeyConference(self, leaguename, conference, prefix="", suffix="Conference"):
  self.hockeyarray = AddHockeyConferenceToArray(self.hockeyarray, leaguename, conference, prefix, suffix);
 def RemoveHockeyConference(self, leaguename, conference):
  self.hockeyarray = RemoveHockeyConferenceFromArray(self.hockeyarray, leaguename, conference);
 def ReplaceHockeyConferenc(self, leaguename, oldconference, newconference, prefix="", suffix="Conference"):
  self.hockeyarray = ReplaceHockeyConferencFromArray(self.hockeyarray, leaguename, oldconference, newconference, prefix, suffix);
 def AddHockeyDivision(self, leaguename, division, conference, prefix="", suffix="Division"):
  self.hockeyarray = AddHockeyDivisionToArray(self.hockeyarray, leaguename, division, conference, prefix, suffix);
 def RemoveHockeyDivision(self, leaguename, division, conference):
  self.hockeyarray = RemoveHockeyDivisionFromArray(self.hockeyarray, leaguename, division, conference);
 def ReplaceHockeyDivision(self, leaguename, olddivision, newdivision, conference, prefix="", suffix="Division"):
  self.hockeyarray = ReplaceHockeyDivisionFromArray(self.hockeyarray, leaguename, olddivision, newdivision, conference, prefix, suffix);
 def MoveHockeyDivisionToConference(self, leaguename, division, oldconference, newconference):
  self.hockeyarray = MoveHockeyDivisionToConferenceFromArray(self.hockeyarray, leaguename, division, oldconference, newconference);
 def AddHockeyTeam(self, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, teamname, conference, division, arenaname, teamnameprefix="", teamnamesuffix=""):
  self.hockeyarray = AddHockeyTeamToArray(self.hockeyarray, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, teamname, conference, division, arenaname, teamnameprefix, teamnamesuffix);
 def RemoveHockeyTeam(self, leaguename, teamname, conference, division):
  self.hockeyarray = RemoveHockeyTeamFromArray(self.hockeyarray, leaguename, teamname, conference, division);
 def ReplaceHockeyTeam(self, leaguename, oldteamname, newteamname, conference, division, cityname=None, areaname=None, countryname=None, fullcountryname=None, fullareaname=None, arenaname=None, teamnameprefix=None, teamnamesuffix=None):
  self.hockeyarray = ReplaceHockeyTeamFromArray(self.hockeyarray, leaguename, oldteamname, newteamname, conference, division, cityname, areaname, countryname, fullcountryname, fullareaname, arenaname, teamnameprefix, teamnamesuffix);
 def MoveHockeyTeamToConference(self, leaguename, teamname, oldconference, newconference, division):
  self.hockeyarray = MoveHockeyTeamToConferenceFromArray(self.hockeyarray, leaguename, teamname, oldconference, newconference, division);
 def MoveHockeyTeamToDivision(self, leaguename, teamname, conference, olddivision, newdivision):
  self.hockeyarray = MoveHockeyTeamToDivisionFromArray(self.hockeyarray, leaguename, teamname, conference, olddivision, newdivision);
 def AddHockeyArena(self, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, arenaname):
  self.hockeyarray = AddHockeyArenaToArray(self.hockeyarray, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, arenaname);
 def AddHockeyGame(self, leaguename, date, time, hometeam, awayteam, periodsscore, shotsongoal, ppgoals, shgoals, periodpens, periodpims, periodhits, takeaways, faceoffwins, atarena, isplayoffgame):
  self.hockeyarray = AddHockeyGameToArray(self.hockeyarray, leaguename, date, time, hometeam, awayteam, periodsscore, shotsongoal, ppgoals, shgoals, periodpens, periodpims, periodhits, takeaways, faceoffwins, atarena, isplayoffgame);
 def LoadHockeyXML(self, inxmlfile, xmlisfile=True, verbose=True):
  self.hockeyarray = MakeHockeyArrayFromHockeyXML(inxmlfile, xmlisfile, verbose);
 def LoadHockeyDatabase(self, sdbfile, verbose=True):
  self.hockeyarray = MakeHockeyArrayFromHockeyDatabase(sdbfile, verbose);
 def LoadHockeySQL(self, sqlfile, sdbfile=None, sqlisfile=True, verbose=True):
  self.hockeyarray = MakeHockeyArrayFromHockeySQL(sqlfile, sdbfile, sqlisfile, verbose);
 def LoadOldHockeyDatabase(self, sdbfile, verbose=True):
  self.hockeyarray = MakeHockeyArrayFromOldHockeyDatabase(sdbfile, verbose);
 def MakeHockeyXML(self, verbose=True):
  return MakeHockeyXMLFromHockeyArray(self.hockeyarray, verbose);
 def MakeHockeyDatabase(self, sdbfile=None, returnxml=False, returndb=False, verbose=True):
  return MakeHockeyDatabaseFromHockeyArray(self.hockeyarray, sdbfile, returnxml, returndb, verbose);
 def MakeHockeyPython(self, verbose=True):
  return MakeHockeyPythonFromHockeyArray(self.hockeyarray, verbose=True);
 def MakeHockeyPythonAlt(self, verbose=True, verbosepy=True):
  return MakeHockeyPythonAltFromHockeyArray(self.hockeyarray, verbose, verbosepy);
 def MakeHockeySQL(self, verbose=True):
  return MakeHockeySQLFromHockeyArray(self.hockeyarray, verbose);
 def MakeHockeyXMLFile(self, outxmlfile=None, returnxml=False, verbose=True):
  return MakeHockeyXMLFileFromHockeyArray(self.hockeyarray, outxmlfile, returnxml, verbose);
 def MakeHockeyPythonFile(self, outpyfile=None, returnpy=False, verbose=True):
  return MakeHockeyPythonFileFromHockeyArray(self.hockeyarray, outpyfile, returnpy, verbose);
 def MakeHockeyPythonAltFileFromHockeyArray(self, outpyfile=None, returnpy=False, verbose=True, verbosepy=True):
  return MakeHockeyPythonAltFileFromHockeyArray(self.hockeyarray, outpyfile, returnpy, verbose, verbosepy);
 def MakeHockeySQLFile(self, sqlfile=None, returnsql=False, verbose=True):
  return MakeHockeySQLFileFromHockeyArray(self.hockeyarray, sqlfile, returnsql, verbose);

''' // Object-oriented classes and functions by Kazuki Przyborowski '''
class MakeHockeyData:
 def __init__(self, databasename="./hockeydatabase.db3"):
  self.hockeycon = MakeHockeyDatabase(databasename);
  MakeHockeyLeagueTable(self.hockeycon);
 def MakeHockeyTeamTable(self, leaguename):
  MakeHockeyTeamTable(self.hockeycon, leaguename);
 def MakeHockeyConferenceTable(self, leaguename, prefix="", suffix="Conference"):
  MakeHockeyConferenceTable(self.hockeycon, leaguename, prefix, suffix);
 def MakeHockeyGameTable(self, leaguename):
  MakeHockeyGameTable(self.hockeycon, leaguename);
 def MakeHockeyDivisionTable(self, leaguename, prefix="", suffix="Division"):
  MakeHockeyDivisionTable(self.hockeycon, leaguename, prefix, suffix);
 def AddHockeyLeague(self, leaguename, leaguefullname, countryname, fullcountryname, date, playofffmt, ordertype, hasconferences="yes", hasdivisions="yes"):
  HockeyLeagueHasDivisions = True;
  if(hasdivisions.lower()=="no"):
   HockeyLeagueHasDivisions = False;
  HockeyLeagueHasConferences = True;
  if(hasconferences.lower()=="no"):
   HockeyLeagueHasConferences = False;
  MakeHockeyLeague(self.hockeycon, leaguename, leaguefullname, countryname, fullcountryname, date, playofffmt, ordertype, HockeyLeagueHasConferences, HockeyLeagueHasDivisions);
 def AddHockeyConference(self, leaguename, conference, prefix="", suffix="Conference", hasconferences="yes"):
  HockeyLeagueHasConferences = True;
  if(hasconferences.lower()=="no"):
   HockeyLeagueHasConferences = False;
  MakeHockeyConference(self.hockeycon, leaguename, conference, prefix, suffix, HockeyLeagueHasConferences);
 def AddHockeyDivision(self, leaguename, division, conference, prefix="", suffix="Division", hasconferences="yes", hasdivisions="yes"):
  HockeyLeagueHasDivisions = True;
  if(hasdivisions.lower()=="no"):
   HockeyLeagueHasDivisions = False;
  HockeyLeagueHasConferences = True;
  if(hasconferences.lower()=="no"):
   HockeyLeagueHasConferences = False;
  MakeHockeyDivision(self.hockeycon, leaguename, division, conference, prefix, suffix, HockeyLeagueHasConferences, HockeyLeagueHasDivisions);
 def AddHockeyTeam(self, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, teamname, conference, division, arenaname, teamnameprefix="", teamnamesuffix="", hasconferences="yes", hasdivisions="yes"):
  HockeyLeagueHasDivisions = True;
  if(hasdivisions.lower()=="no"):
   HockeyLeagueHasDivisions = False;
  HockeyLeagueHasConferences = True;
  if(hasconferences.lower()=="no"):
   HockeyLeagueHasConferences = False;
  MakeHockeyTeam(self.hockeycon, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, teamname, conference, division, arenaname, teamnameprefix, teamnamesuffix, HockeyLeagueHasConferences, HockeyLeagueHasDivisions);
 def AddHockeyGame(self, leaguename, date, time, hometeam, awayteam, periodsscore, shotsongoal, ppgoals, shgoals, periodpens, periodpims, periodhits, takeaways, faceoffwins, atarena, isplayoffgame):
  MakeHockeyGame(self.hockeycon, leaguename, date, time, hometeam, awayteam, periodsscore, shotsongoal, ppgoals, shgoals, periodpens, periodpims, periodhits, takeaways, faceoffwins, atarena, isplayoffgame);
 def AddHockeyArena(self, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, arenaname):
  MakeHockeyArena(self.hockeycon, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, arenaname);
 def Close(self):
  return CloseHockeyDatabase(self.hockeycon);
 def CloseHockey(self):
  return CloseHockeyDatabase(self.hockeycon);
 def CloseHockeyDatabase(self):
  return CloseHockeyDatabase(self.hockeycon);
