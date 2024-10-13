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

    $FileInfo: hockeyoopfuncs.py - Last Update: 10/11/2024 Ver. 0.9.2 RC 1 - Author: cooldude2k $
'''

from .hockeyfunctions import *


class MakeHockeyArray:
    def __init__(self, databasename="./hockeydatabase.db3"):
        self.hockeyarray = CreateHockeyArray(databasename)

    def _update_hockey_array(self, update_function, *args, **kwargs):
        """Helper method to update the hockey array with a given function."""
        self.hockeyarray = update_function(self.hockeyarray, *args, **kwargs)

    def AddHockeyLeague(self, leaguename, leaguefullname, countryname, fullcountryname, date, playofffmt, ordertype, hasconferences="yes", hasdivisions="yes"):
        self._update_hockey_array(AddHockeyLeagueToArray, leaguename, leaguefullname, countryname, fullcountryname, date, playofffmt, ordertype, hasconferences, hasdivisions)

    def RemoveHockeyLeague(self, leaguename):
        self._update_hockey_array(RemoveHockeyLeagueFromArray, leaguename)

    def ReplaceHockeyLeague(self, oldleaguename, newleaguename, leaguefullname=None, countryname=None, fullcountryname=None, date=None, playofffmt=None, ordertype=None, hasconferences=None, hasdivisions=None):
        self._update_hockey_array(ReplaceHockeyLeagueFromArray, oldleaguename, newleaguename, leaguefullname, countryname, fullcountryname, date, playofffmt, ordertype, hasconferences, hasdivisions)

    def AddHockeyConference(self, leaguename, conference, prefix="", suffix="Conference"):
        self._update_hockey_array(AddHockeyConferenceToArray, leaguename, conference, prefix, suffix)

    def RemoveHockeyConference(self, leaguename, conference):
        self._update_hockey_array(RemoveHockeyConferenceFromArray, leaguename, conference)

    def ReplaceHockeyConference(self, leaguename, oldconference, newconference, prefix="", suffix="Conference"):
        self._update_hockey_array(ReplaceHockeyConferencFromArray, leaguename, oldconference, newconference, prefix, suffix)

    def AddHockeyDivision(self, leaguename, division, conference, prefix="", suffix="Division"):
        self._update_hockey_array(AddHockeyDivisionToArray, leaguename, division, conference, prefix, suffix)

    def RemoveHockeyDivision(self, leaguename, division, conference):
        self._update_hockey_array(RemoveHockeyDivisionFromArray, leaguename, division, conference)

    def ReplaceHockeyDivision(self, leaguename, olddivision, newdivision, conference, prefix="", suffix="Division"):
        self._update_hockey_array(ReplaceHockeyDivisionFromArray, leaguename, olddivision, newdivision, conference, prefix, suffix)

    def MoveHockeyDivisionToConference(self, leaguename, division, oldconference, newconference):
        self._update_hockey_array(MoveHockeyDivisionToConferenceFromArray, leaguename, division, oldconference, newconference)

    def AddHockeyTeam(self, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, teamname, conference, division, arenaname, teamnameprefix="", teamnamesuffix=""):
        self._update_hockey_array(AddHockeyTeamToArray, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, teamname, conference, division, arenaname, teamnameprefix, teamnamesuffix)

    def RemoveHockeyTeam(self, leaguename, teamname, conference, division):
        self._update_hockey_array(RemoveHockeyTeamFromArray, leaguename, teamname, conference, division)

    def ReplaceHockeyTeam(self, leaguename, oldteamname, newteamname, conference, division, cityname=None, areaname=None, countryname=None, fullcountryname=None, fullareaname=None, arenaname=None, teamnameprefix=None, teamnamesuffix=None):
        self._update_hockey_array(ReplaceHockeyTeamFromArray, leaguename, oldteamname, newteamname, conference, division, cityname, areaname, countryname, fullcountryname, fullareaname, arenaname, teamnameprefix, teamnamesuffix)

    def MoveHockeyTeamToConference(self, leaguename, teamname, oldconference, newconference, division):
        self._update_hockey_array(MoveHockeyTeamToConferenceFromArray, leaguename, teamname, oldconference, newconference, division)

    def MoveHockeyTeamToDivision(self, leaguename, teamname, conference, olddivision, newdivision):
        self._update_hockey_array(MoveHockeyTeamToDivisionFromArray, leaguename, teamname, conference, olddivision, newdivision)

    def AddHockeyArena(self, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, arenaname):
        self._update_hockey_array(AddHockeyArenaToArray, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, arenaname)

    def AddHockeyGame(self, leaguename, date, time, hometeam, awayteam, periodsscore, shotsongoal, ppgoals, shgoals, periodpens, periodpims, periodhits, takeaways, faceoffwins, atarena, isplayoffgame):
        self._update_hockey_array(AddHockeyGameToArray, leaguename, date, time, hometeam, awayteam, periodsscore, shotsongoal, ppgoals, shgoals, periodpens, periodpims, periodhits, takeaways, faceoffwins, atarena, isplayoffgame)

    def LoadHockeyXML(self, inxmlfile, xmlisfile=True, verbose=True):
        self._update_hockey_array(MakeHockeyArrayFromHockeyXML, inxmlfile, xmlisfile, verbose)

    def LoadHockeyDatabase(self, sdbfile, verbose=True):
        self._update_hockey_array(MakeHockeyArrayFromHockeyDatabase, sdbfile, verbose)

    def LoadHockeySQL(self, sqlfile, sdbfile=None, sqlisfile=True, verbose=True):
        self._update_hockey_array(MakeHockeyArrayFromHockeySQL, sqlfile, sdbfile, sqlisfile, verbose)

    def LoadOldHockeyDatabase(self, sdbfile, verbose=True):
        self._update_hockey_array(MakeHockeyArrayFromOldHockeyDatabase, sdbfile, verbose)

    def MakeHockeyXML(self, verbose=True):
        return MakeHockeyXMLFromHockeyArray(self.hockeyarray, verbose)

    def MakeHockeyDatabase(self, sdbfile=None, returnxml=False, returndb=False, verbose=True):
        return MakeHockeyDatabaseFromHockeyArray(self.hockeyarray, sdbfile, returnxml, returndb, verbose)

    def MakeHockeyPython(self, verbose=True):
        return MakeHockeyPythonFromHockeyArray(self.hockeyarray, verbose)

    def MakeHockeyPythonAlt(self, verbose=True, verbosepy=True):
        return MakeHockeyPythonAltFromHockeyArray(self.hockeyarray, verbose, verbosepy)

    def MakeHockeySQL(self, verbose=True):
        return MakeHockeySQLFromHockeyArray(self.hockeyarray, verbose)

    def MakeHockeyXMLFile(self, outxmlfile=None, returnxml=False, verbose=True):
        return MakeHockeyXMLFileFromHockeyArray(self.hockeyarray, outxmlfile, returnxml, verbose)

    def MakeHockeyPythonFile(self, outpyfile=None, returnpy=False, verbose=True):
        return MakeHockeyPythonFileFromHockeyArray(self.hockeyarray, outpyfile, returnpy, verbose)

    def MakeHockeyPythonAltFile(self, outpyfile=None, returnpy=False, verbose=True, verbosepy=True):
        return MakeHockeyPythonAltFileFromHockeyArray(self.hockeyarray, outpyfile, returnpy, verbose, verbosepy)

    def MakeHockeySQLFile(self, sqlfile=None, returnsql=False, verbose=True):
        return MakeHockeySQLFileFromHockeyArray(self.hockeyarray, sqlfile, returnsql, verbose)


''' // Object-oriented classes and functions by Kazuki Przyborowski '''


class MakeHockeyData:
    def __init__(self, databasename="./hockeydatabase.db3"):
        self.hockeycon = MakeHockeyDatabase(databasename)
        MakeHockeyLeagueTable(self.hockeycon)

    def _get_conference_division_flags(self, hasconferences, hasdivisions):
        """Helper method to determine whether the league has conferences and divisions."""
        return (
            hasconferences.lower() != "no",
            hasdivisions.lower() != "no"
        )

    def MakeHockeyTeamTable(self, leaguename):
        MakeHockeyTeamTable(self.hockeycon, leaguename)

    def MakeHockeyConferenceTable(self, leaguename, prefix="", suffix="Conference"):
        MakeHockeyConferenceTable(self.hockeycon, leaguename, prefix, suffix)

    def MakeHockeyGameTable(self, leaguename):
        MakeHockeyGameTable(self.hockeycon, leaguename)

    def MakeHockeyDivisionTable(self, leaguename, prefix="", suffix="Division"):
        MakeHockeyDivisionTable(self.hockeycon, leaguename, prefix, suffix)

    def AddHockeyLeague(self, leaguename, leaguefullname, countryname, fullcountryname, date, playofffmt, ordertype, hasconferences="yes", hasdivisions="yes"):
        HockeyLeagueHasConferences, HockeyLeagueHasDivisions = self._get_conference_division_flags(hasconferences, hasdivisions)
        MakeHockeyLeague(self.hockeycon, leaguename, leaguefullname, countryname, fullcountryname, date, playofffmt, ordertype, HockeyLeagueHasConferences, HockeyLeagueHasDivisions)

    def AddHockeyConference(self, leaguename, conference, prefix="", suffix="Conference", hasconferences="yes"):
        HockeyLeagueHasConferences, _ = self._get_conference_division_flags(hasconferences, "yes")
        MakeHockeyConference(self.hockeycon, leaguename, conference, prefix, suffix, HockeyLeagueHasConferences)

    def AddHockeyDivision(self, leaguename, division, conference, prefix="", suffix="Division", hasconferences="yes", hasdivisions="yes"):
        HockeyLeagueHasConferences, HockeyLeagueHasDivisions = self._get_conference_division_flags(hasconferences, hasdivisions)
        MakeHockeyDivision(self.hockeycon, leaguename, division, conference, prefix, suffix, HockeyLeagueHasConferences, HockeyLeagueHasDivisions)

    def AddHockeyTeam(self, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, teamname, conference, division, arenaname, teamnameprefix="", teamnamesuffix="", hasconferences="yes", hasdivisions="yes"):
        HockeyLeagueHasConferences, HockeyLeagueHasDivisions = self._get_conference_division_flags(hasconferences, hasdivisions)
        MakeHockeyTeam(self.hockeycon, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, teamname, conference, division, arenaname, teamnameprefix, teamnamesuffix, HockeyLeagueHasConferences, HockeyLeagueHasDivisions)

    def AddHockeyGame(self, leaguename, date, time, hometeam, awayteam, periodsscore, shotsongoal, ppgoals, shgoals, periodpens, periodpims, periodhits, takeaways, faceoffwins, atarena, isplayoffgame):
        MakeHockeyGame(self.hockeycon, leaguename, date, time, hometeam, awayteam, periodsscore, shotsongoal, ppgoals, shgoals, periodpens, periodpims, periodhits, takeaways, faceoffwins, atarena, isplayoffgame)

    def AddHockeyArena(self, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, arenaname):
        MakeHockeyArena(self.hockeycon, leaguename, cityname, areaname, countryname, fullcountryname, fullareaname, arenaname)

    def OptimizeHockey(self, optimize=True):
        return self.OptimizeHockeyDatabase(optimize)

    def OptimizeHockeyDatabase(self, optimize=True):
        return OptimizeHockeyDatabase(self.hockeycon)

    def Close(self, optimize=True):
        return self.CloseHockeyDatabase(optimize)

    def CloseHockey(self, optimize=True):
        return self.CloseHockeyDatabase(optimize)

    def CloseHockeyDatabase(self, optimize=True):
        return CloseHockeyDatabase(self.hockeycon, optimize)
