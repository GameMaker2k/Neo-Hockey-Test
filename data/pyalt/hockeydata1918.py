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

hockeyarray = libhockeydata.CreateHockeyArray("./php/data/hockey1918-19.db3");
hockeyarray = libhockeydata.AddHockeyLeagueToArray(hockeyarray, "NHL", "National Hockey League", "CAN", "Canada", "19181221", "League=2", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", False, False);
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "NHL", "");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "NHL", "", "", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Ottawa", "ON", "CAN", "Canada", "Ontario", "Senators", "", "", "The Arena", "Ottawa", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Montreal", "QC", "CAN", "Canada", "Quebec", "Canadiens", "", "", "Jubilee Rink", "Montreal", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Toronto", "ON", "CAN", "Canada", "Ontario", "Arenas", "", "", "Arena Gardens", "Toronto", "", "");

libhockeydata.MakeHockeyDatabaseFromHockeyArray(hockeyarray, None, False, True, True);
