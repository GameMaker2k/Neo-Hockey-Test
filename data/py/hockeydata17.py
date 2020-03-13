#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals;
import libhockeydata;

sqldatacon = libhockeydata.MakeHockeyDatabase("./php/data/hockey17-18.db3");
libhockeydata.MakeHockeyLeagueTable(sqldatacon);
libhockeydata.MakeHockeyTeamTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyLeague(sqldatacon, "NHL", "National Hockey League", "USA", "United States", "20171004", "Division=3,Conference=2", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.MakeHockeyConference(sqldatacon, "NHL", "Eastern", "", "Conference", True);
libhockeydata.MakeHockeyConference(sqldatacon, "NHL", "Western", "", "Conference", True);
libhockeydata.MakeHockeyArena(sqldatacon, "NHL", "Stockholm", "AB", "SWE", "Sweden", "Stockholm County", "Ericsson Globe");
libhockeydata.MakeHockeyArena(sqldatacon, "NHL", "Ottawa", "ON", "CAN", "Canada", "Ontario", "Lansdowne Park");
libhockeydata.MakeHockeyArena(sqldatacon, "NHL", "New York City", "NY", "USA", "United States", "New York", "Citi Field");
libhockeydata.MakeHockeyArena(sqldatacon, "NHL", "Annapolis", "MD", "USA", "United States", "Maryland", "United States Naval Academy");
libhockeydata.MakeHockeyTeamTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyLeague(sqldatacon, "AHL", "American Hockey League", "USA", "United States", "20171006", "Division=4", "ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.MakeHockeyConference(sqldatacon, "AHL", "Eastern", "", "Conference", True);
libhockeydata.MakeHockeyConference(sqldatacon, "AHL", "Western", "", "Conference", True);
libhockeydata.MakeHockeyArena(sqldatacon, "AHL", "Hershey", "PA", "USA", "United States", "Pennsylvania", "Hersheypark Stadium");
libhockeydata.MakeHockeyTeamTable(sqldatacon, "ECHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "ECHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "ECHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "ECHL");
libhockeydata.MakeHockeyLeague(sqldatacon, "ECHL", "ECHL", "USA", "United States", "20171013", "Division=4", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.MakeHockeyConference(sqldatacon, "ECHL", "Eastern", "", "Conference", True);
libhockeydata.MakeHockeyConference(sqldatacon, "ECHL", "Western", "", "Conference", True);
libhockeydata.MakeHockeyTeamTable(sqldatacon, "FHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "FHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "FHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "FHL");
libhockeydata.MakeHockeyLeague(sqldatacon, "FHL", "Federal Hockey League", "USA", "United States", "20171027", "League=4", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.MakeHockeyConference(sqldatacon, "FHL", "", "", "Conference", False);
libhockeydata.MakeHockeyTeamTable(sqldatacon, "SPHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "SPHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "SPHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "SPHL");
libhockeydata.MakeHockeyLeague(sqldatacon, "SPHL", "Southern Professional Hockey League", "USA", "United States", "20171020", "League=8", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.MakeHockeyConference(sqldatacon, "SPHL", "", "", "Conference", False);
libhockeydata.MakeHockeyTeamTable(sqldatacon, "KHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "KHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "KHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "KHL");
libhockeydata.MakeHockeyLeague(sqldatacon, "KHL", "Kontinental Hockey League", "RUS", "Russia", "20170821", "Conference=8", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.MakeHockeyConference(sqldatacon, "KHL", "Western", "", "Conference", True);
libhockeydata.MakeHockeyConference(sqldatacon, "KHL", "Eastern", "", "Conference", True);
libhockeydata.MakeHockeyArena(sqldatacon, "KHL", "Helsinki", "FI", "FIN", "Finland", "Finland", "Kaisaniemi Park");
libhockeydata.MakeHockeyArena(sqldatacon, "KHL", "Riga", "LV", "LVA", "Latvia", "Latvia", "Riga City Council Sports Complex");

libhockeydata.CloseHockeyDatabase(sqldatacon);
