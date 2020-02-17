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

    $FileInfo: hockeyoopfuncs.py - Last Update: 2/17/2020 Ver. 0.2.6 RC 1 - Author: cooldude2k $
'''

from libhockeydata.hockeyfunctions import *;

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
 def AddHockeyConference(self, leaguename, conference):
  self.hockeyarray = AddHockeyConferenceToArray(self.hockeyarray, leaguename, conference);
 def RemoveHockeyConference(self, leaguename, conference):
  self.hockeyarray = RemoveHockeyConferenceFromArray(self.hockeyarray, leaguename, conference);
 def ReplaceHockeyConferenc(self, leaguename, oldconference, newconference):
  self.hockeyarray = ReplaceHockeyConferencFromArray(self.hockeyarray, leaguename, oldconference, newconference);
 def AddHockeyDivision(self, leaguename, division, conference):
  self.hockeyarray = AddHockeyDivisionToArray(self.hockeyarray, leaguename, division, conference);
 def RemoveHockeyDivision(self, leaguename, division, conference):
  self.hockeyarray = RemoveHockeyDivisionFromArray(self.hockeyarray, leaguename, division, conference);
 def ReplaceHockeyDivision(self, leaguename, olddivision, newdivision, conference):
  self.hockeyarray = ReplaceHockeyDivisionFromArray(self.hockeyarray, leaguename, olddivision, newdivision, conference);
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
 def MakeHockeyDatabaseWrite(self, sdbfile=None, outxmlfile=None, returnxml=False, verbose=True):
  return MakeHockeyDatabaseFromHockeyArrayWrite(self.hockeyarray, sdbfile, outxmlfile, returnxml, verbose);
 def MakeHockeyPythonFile(self, outpyfile=None, returnpy=False, verbose=True):
  return MakeHockeyPythonFileFromHockeyArray(self.hockeyarray, outpyfile, returnpy, verbose);
 def MakeHockeyPythonAltFileFromHockeyArray(self, outpyfile=None, returnpy=False, verbose=True, verbosepy=True):
  return MakeHockeyPythonAltFileFromHockeyArray(self.hockeyarray, outpyfile, returnpy, verbose, verbosepy);
 def MakeHockeySQLFile(self, sqlfile=None, returnsql=False, verbose=True):
  return MakeHockeySQLFileFromHockeyArray(self.hockeyarray, sqlfile, returnsql, verbose);
