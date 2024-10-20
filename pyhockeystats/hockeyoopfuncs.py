#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2015-2024 Game Maker 2k - https://github.com/GameMaker2k
    Copyright 2015-2024 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: hockeyoopfuncs.py - Last Update: 10/17/2024 Ver. 0.9.6 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals, generators, with_statement, nested_scopes

from .hockeyfunctions import *


class MakeHockeyArray:
    def __init__(self, databasename="./hockeydatabase.db3"):
        self.hockeyarray = CreateHockeyArray(databasename)

    def AddHockeyLeague(self, leaguename, leaguefullname, countryname, fullcountryname,
                        date, playofffmt, ordertype, hasconferences="yes", hasdivisions="yes"):
        """
        Add a hockey league to the array.
        """
        AddHockeyLeagueToArray(
            self.hockeyarray, leaguename, leaguefullname, countryname,
            fullcountryname, date, playofffmt, ordertype, hasconferences, hasdivisions
        )

    def RemoveHockeyLeague(self, leaguename):
        """
        Remove a hockey league from the array.
        """
        RemoveHockeyLeagueFromArray(self.hockeyarray, leaguename)

    def ReplaceHockeyLeague(self, oldleaguename, newleaguename, leaguefullname=None,
                            countryname=None, fullcountryname=None, date=None,
                            playofffmt=None, ordertype=None, hasconferences=None, hasdivisions=None):
        """
        Replace a hockey league in the array.
        """
        ReplaceHockeyLeagueFromArray(
            self.hockeyarray, oldleaguename, newleaguename, leaguefullname,
            countryname, fullcountryname, date, playofffmt, ordertype,
            hasconferences, hasdivisions
        )

    def AddHockeyConference(self, leaguename, conference, prefix="", suffix="Conference"):
        """
        Add a hockey conference to the array.
        """
        AddHockeyConferenceToArray(
            self.hockeyarray, leaguename, conference, prefix, suffix
        )

    def RemoveHockeyConference(self, leaguename, conference):
        """
        Remove a hockey conference from the array.
        """
        RemoveHockeyConferenceFromArray(
            self.hockeyarray, leaguename, conference
        )

    def ReplaceHockeyConference(self, leaguename, oldconference, newconference, prefix="", suffix="Conference"):
        """
        Replace a hockey conference in the array.
        """
        ReplaceHockeyConferenceFromArray(
            self.hockeyarray, leaguename, oldconference, newconference, prefix, suffix
        )

    def AddHockeyDivision(self, leaguename, division, conference, prefix="", suffix="Division"):
        """
        Add a hockey division to the array.
        """
        AddHockeyDivisionToArray(
            self.hockeyarray, leaguename, division, conference, prefix, suffix
        )

    def RemoveHockeyDivision(self, leaguename, division, conference):
        """
        Remove a hockey division from the array.
        """
        RemoveHockeyDivisionFromArray(
            self.hockeyarray, leaguename, division, conference
        )

    def ReplaceHockeyDivision(self, leaguename, olddivision, newdivision, conference, prefix="", suffix="Division"):
        """
        Replace a hockey division in the array.
        """
        ReplaceHockeyDivisionFromArray(
            self.hockeyarray, leaguename, olddivision, newdivision, conference, prefix, suffix
        )

    def MoveHockeyDivisionToConference(self, leaguename, division, oldconference, newconference):
        """
        Move a hockey division to a different conference in the array.
        """
        MoveHockeyDivisionToConferenceFromArray(
            self.hockeyarray, leaguename, division, oldconference, newconference
        )

    def AddHockeyTeam(self, leaguename, cityname, areaname, countryname, fullcountryname,
                      fullareaname, teamname, conference, division, arenaname,
                      teamnameprefix="", teamnamesuffix="", teamaffiliates=""):
        """
        Add a hockey team to the array.
        """
        AddHockeyTeamToArray(
            self.hockeyarray, leaguename, cityname, areaname, countryname,
            fullcountryname, fullareaname, teamname, conference, division,
            arenaname, teamnameprefix, teamnamesuffix, teamaffiliates
        )

    def RemoveHockeyTeam(self, leaguename, teamname, conference, division):
        """
        Remove a hockey team from the array.
        """
        RemoveHockeyTeamFromArray(
            self.hockeyarray, leaguename, teamname, conference, division
        )

    def ReplaceHockeyTeam(self, leaguename, oldteamname, newteamname, conference, division,
                          cityname=None, areaname=None, countryname=None, fullcountryname=None,
                          fullareaname=None, arenaname=None, teamnameprefix=None, teamnamesuffix=None):
        """
        Replace a hockey team in the array.
        """
        ReplaceHockeyTeamFromArray(
            self.hockeyarray, leaguename, oldteamname, newteamname, conference,
            division, cityname, areaname, countryname, fullcountryname,
            fullareaname, arenaname, teamnameprefix, teamnamesuffix
        )

    def MoveHockeyTeamToConference(self, leaguename, teamname, oldconference, newconference, division):
        """
        Move a hockey team to a different conference in the array.
        """
        MoveHockeyTeamToConferenceFromArray(
            self.hockeyarray, leaguename, teamname, oldconference, newconference, division
        )

    def MoveHockeyTeamToDivision(self, leaguename, teamname, conference, olddivision, newdivision):
        """
        Move a hockey team to a different division in the array.
        """
        MoveHockeyTeamToDivisionFromArray(
            self.hockeyarray, leaguename, teamname, conference, olddivision, newdivision
        )

    def AddHockeyArena(self, leaguename, cityname, areaname, countryname,
                       fullcountryname, fullareaname, arenaname):
        """
        Add a hockey arena to the array.
        """
        AddHockeyArenaToArray(
            self.hockeyarray, leaguename, cityname, areaname, countryname,
            fullcountryname, fullareaname, arenaname
        )

    def AddHockeyGame(self, leaguename, date, time, hometeam, awayteam, periodsscore, shotsongoal,
                      ppgoals, shgoals, periodpens, periodpims, periodhits,
                      takeaways, faceoffwins, atarena, isplayoffgame):
        """
        Add a hockey game to the array.
        """
        AddHockeyGameToArray(
            self.hockeyarray, leaguename, date, time, hometeam, awayteam, periodsscore,
            shotsongoal, ppgoals, shgoals, periodpens, periodpims, periodhits,
            takeaways, faceoffwins, atarena, isplayoffgame
        )

    def LoadHockeyXML(self, inxmlfile, xmlisfile=True, verbose=True):
        """
        Load hockey data from an XML file into the array.
        """
        MakeHockeyArrayFromHockeyXML(inxmlfile, xmlisfile, verbose)

    def LoadHockeyDatabase(self, sdbfile, verbose=True):
        """
        Load hockey data from a database into the array.
        """
        MakeHockeyArrayFromHockeyDatabase(sdbfile, verbose)

    def LoadHockeySQL(self, sqlfile, sdbfile=None, sqlisfile=True, verbose=True):
        """
        Load hockey data from an SQL file into the array.
        """
        MakeHockeyArrayFromHockeySQL(sqlfile, sdbfile, sqlisfile, verbose)

    def LoadOldHockeyDatabase(self, sdbfile, verbose=True):
        """
        Load hockey data from an old database format into the array.
        """
        MakeHockeyArrayFromOldHockeyDatabase(sdbfile, verbose)

    def MakeHockeyXML(self, verbose=True):
        """
        Generate an XML representation of the hockey data.
        """
        return MakeHockeyXMLFromHockeyArray(self.hockeyarray, verbose)

    def MakeHockeyDatabase(self, sdbfile=None, returnxml=False, returndb=False, verbose=True):
        """
        Create a hockey database from the array.
        """
        return MakeHockeyDatabaseFromHockeyArray(
            self.hockeyarray, sdbfile, returnxml, returndb, verbose
        )

    def MakeHockeyPython(self, verbose=True):
        """
        Generate a Python script representation of the hockey data.
        """
        return MakeHockeyPythonFromHockeyArray(self.hockeyarray, verbose)

    def MakeHockeyPythonAlt(self, verbose=True, verbosepy=True):
        """
        Generate an alternative Python script representation of the hockey data.
        """
        return MakeHockeyPythonAltFromHockeyArray(self.hockeyarray, verbose, verbosepy)

    def MakeHockeySQL(self, verbose=True):
        """
        Generate an SQL script representation of the hockey data.
        """
        return MakeHockeySQLFromHockeyArray(self.hockeyarray, verbose)

    def MakeHockeyXMLFile(self, outxmlfile=None, returnxml=False, verbose=True):
        """
        Write the hockey data to an XML file.
        """
        return MakeHockeyXMLFileFromHockeyArray(self.hockeyarray, outxmlfile, returnxml, verbose)

    def MakeHockeyPythonFile(self, outpyfile=None, returnpy=False, verbose=True):
        """
        Write the hockey data to a Python script file.
        """
        return MakeHockeyPythonFileFromHockeyArray(self.hockeyarray, outpyfile, returnpy, verbose)

    def MakeHockeyPythonAltFile(self, outpyfile=None, returnpy=False, verbose=True, verbosepy=True):
        """
        Write the hockey data to an alternative Python script file.
        """
        return MakeHockeyPythonAltFileFromHockeyArray(
            self.hockeyarray, outpyfile, returnpy, verbose, verbosepy
        )

    def MakeHockeySQLFile(self, sqlfile=None, returnsql=False, verbose=True):
        """
        Write the hockey data to an SQL script file.
        """
        return MakeHockeySQLFileFromHockeyArray(self.hockeyarray, sqlfile, returnsql, verbose)


class MakeHockeyData:
    def __init__(self, databasename="./hockeydatabase.db3"):
        self.hockeycon = MakeHockeyDatabase(databasename)
        MakeHockeyLeagueTable(self.hockeycon)

    def MakeHockeyTeamTable(self, leaguename):
        """
        Create a hockey team table in the database.
        """
        MakeHockeyTeamTable(self.hockeycon, leaguename)

    def MakeHockeyConferenceTable(self, leaguename):
        """
        Create a hockey conference table in the database.
        """
        MakeHockeyConferenceTable(self.hockeycon, leaguename)

    def MakeHockeyGameTable(self, leaguename):
        """
        Create a hockey game table in the database.
        """
        MakeHockeyGameTable(self.hockeycon, leaguename)

    def MakeHockeyDivisionTable(self, leaguename):
        """
        Create a hockey division table in the database.
        """
        MakeHockeyDivisionTable(self.hockeycon, leaguename)

    def AddHockeyLeague(self, leaguename, leaguefullname, countryname,
                        fullcountryname, date, playofffmt, ordertype):
        """
        Add a hockey league to the database.
        """
        MakeHockeyLeague(
            self.hockeycon, leaguename, leaguefullname, countryname,
            fullcountryname, date, playofffmt, ordertype
        )

    def AddHockeyConference(self, leaguename, conference, prefix="",
                            suffix="Conference", hasconferences=True):
        """
        Add a hockey conference to the database.
        """
        MakeHockeyConference(
            self.hockeycon, leaguename, conference, prefix, suffix, hasconferences
        )

    def AddHockeyDivision(self, leaguename, division, conference, prefix="",
                          suffix="Division", hasconferences=True, hasdivisions=True):
        """
        Add a hockey division to the database.
        """
        MakeHockeyDivision(
            self.hockeycon, leaguename, division, conference, prefix,
            suffix, hasconferences, hasdivisions
        )

    def AddHockeyTeam(self, leaguename, date, cityname, areaname, countryname,
                      fullcountryname, fullareaname, teamname, conference,
                      division, arenaname, teamnameprefix="", teamnamesuffix="",
                      teamaffiliates="", hasconferences=True, hasdivisions=True):
        """
        Add a hockey team to the database.
        """
        MakeHockeyTeam(
            self.hockeycon, leaguename, date, cityname, areaname, countryname,
            fullcountryname, fullareaname, teamname, conference, division,
            arenaname, teamnameprefix, teamnamesuffix, teamaffiliates,
            hasconferences, hasdivisions
        )

    def AddHockeyGame(self, leaguename, date, time, hometeam, awayteam, periodsscore,
                      shotsongoal, ppgoals, shgoals, periodpens, periodpims,
                      periodhits, takeaways, faceoffwins, atarena, isplayoffgame):
        """
        Add a hockey game to the database.
        """
        MakeHockeyGame(
            self.hockeycon, leaguename, date, time, hometeam, awayteam,
            periodsscore, shotsongoal, ppgoals, shgoals, periodpens,
            periodpims, periodhits, takeaways, faceoffwins, atarena, isplayoffgame
        )

    def AddHockeyArena(self, leaguename, cityname, areaname, countryname,
                       fullcountryname, fullareaname, arenaname):
        """
        Add a hockey arena to the database.
        """
        MakeHockeyArena(
            self.hockeycon, leaguename, cityname, areaname, countryname,
            fullcountryname, fullareaname, arenaname
        )

    def OptimizeHockey(self):
        """
        Optimize the hockey database.
        """
        OptimizeHockeyDatabase(self.hockeycon)

    def Close(self, optimize=True):
        """
        Close the hockey database connection.
        """
        CloseHockeyDatabase(self.hockeycon, optimize)

    def CloseHockey(self, optimize=True):
        """
        Close the hockey database connection.
        """
        CloseHockeyDatabase(self.hockeycon, optimize)

    def CloseHockeyDatabase(self, optimize=True):
        """
        Close the hockey database connection.
        """
        CloseHockeyDatabase(self.hockeycon, optimize)
