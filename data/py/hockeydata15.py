#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals;
import libhockeydata;

sqldatacon = libhockeydata.MakeHockeyDatabase("./php/data/hockey15-16.db3");
libhockeydata.MakeHockeyLeagueTable(sqldatacon);
libhockeydata.MakeHockeyTeamTable(sqldatacon, "ECHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "ECHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "ECHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "ECHL");
libhockeydata.MakeHockeyLeague(sqldatacon, "ECHL", "ECHL", "USA", "United States", "20151007", "Division=1,Conference=5", "ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.MakeHockeyConference(sqldatacon, "ECHL", "Eastern", "", "Conference", True);
libhockeydata.MakeHockeyConference(sqldatacon, "ECHL", "Western", "", "Conference", True);
libhockeydata.MakeHockeyTeamTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyLeague(sqldatacon, "AHL", "American Hockey League", "USA", "United States", "20151009", "Division=4", "ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.MakeHockeyConference(sqldatacon, "AHL", "Eastern", "", "Conference", True);
libhockeydata.MakeHockeyConference(sqldatacon, "AHL", "Western", "", "Conference", True);
libhockeydata.MakeHockeyArena(sqldatacon, "AHL", "West Sacramento", "CA", "USA", "United States", "California", "Raley Field");
libhockeydata.MakeHockeyTeamTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyLeague(sqldatacon, "NHL", "National Hockey League", "USA", "United States", "20151007", "Division=3,Conference=2", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.MakeHockeyConference(sqldatacon, "NHL", "Eastern", "", "Conference", True);
libhockeydata.MakeHockeyConference(sqldatacon, "NHL", "Western", "", "Conference", True);
libhockeydata.MakeHockeyArena(sqldatacon, "NHL", "Foxborough", "MA", "USA", "United States", "Massachusetts", "Gillette Stadium");
libhockeydata.MakeHockeyArena(sqldatacon, "NHL", "Minneapolis", "MN", "USA", "United States", "Minnesota", "TCF Bank Stadium");
libhockeydata.MakeHockeyArena(sqldatacon, "NHL", "Denver", "CO", "USA", "United States", "Colorado", "Coors Field");

libhockeydata.CloseHockeyDatabase(sqldatacon);
