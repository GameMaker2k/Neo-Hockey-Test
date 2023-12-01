#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals;
import libhockeydata;
try:
 reload(sys);
except NameError:
 from importlib import reload;
 reload(sys);
try:
 sys.setdefaultencoding('UTF-8');
except AttributeError:
 pass;

sqldatacon = libhockeydata.MakeHockeyDatabase("./php/data/hockey1918-19.db3");
libhockeydata.MakeHockeyLeagueTable(sqldatacon);
libhockeydata.MakeHockeyTeamTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyLeague(sqldatacon, "NHL", "National Hockey League", "CAN", "Canada", "19181221", "League=2", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.MakeHockeyConference(sqldatacon, "NHL", "", "", "Conference", False);
libhockeydata.MakeHockeyDivision(sqldatacon, "NHL", "", "", "", "Division", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "19181221", "Ottawa", "ON", "CAN", "Canada", "Ontario", "Senators", "", "", "The Arena", "Ottawa", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "19181221", "Montreal", "QC", "CAN", "Canada", "Quebec", "Canadiens", "", "", "Jubilee Rink", "Montreal", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "19181221", "Toronto", "ON", "CAN", "Canada", "Ontario", "Arenas", "", "", "Arena Gardens", "Toronto", "", "", False, False);

libhockeydata.CloseHockeyDatabase(sqldatacon);
