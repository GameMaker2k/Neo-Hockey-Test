#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals;
import libhockeydata;

sqldatacon = libhockeydata.MakeHockeyDatabase("./php/data/fhmt2y17-18.db3");
libhockeydata.MakeHockeyLeagueTable(sqldatacon);
libhockeydata.MakeHockeyTeamTable(sqldatacon, "HOL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "HOL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "HOL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "HOL");
libhockeydata.MakeHockeyLeague(sqldatacon, "HOL", "Hockey League", "USA", "United States", "20171001", "Division=1,Conference=1", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.MakeHockeyConference(sqldatacon, "HOL", "Conference 1", "", "", True);
libhockeydata.MakeHockeyDivision(sqldatacon, "HOL", "Division 1", "Conference 1", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "HOL", "20171001", "Detroit", "MI", "USA", "United States", "Michigan", "Blasters", "Conference 1", "Division 1", "DET Arena", "Detroit", "", "MIL:Northview Loggerheads", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "HOL", "20171001", "Indianapolis", "IN", "USA", "United States", "Indiana", "Sabres", "Conference 1", "Division 1", "IND Arena", "Indianapolis", "", "MIL:Gulivoire Park Caravans", True, True);
libhockeydata.MakeHockeyDivision(sqldatacon, "HOL", "Division 2", "Conference 1", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "HOL", "20171001", "Chicago", "IL", "USA", "United States", "Illionis", "River Bandits", "Conference 1", "Division 2", "CHI Arena", "Chicago", "", "MIL:Wheeling Ramblers", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "HOL", "20171001", "Kansas City", "MO", "USA", "United States", "Missouri", "Chariots", "Conference 1", "Division 2", "KAN Arena", "Kansas City", "", "MIL:Columbia Skychiefs", True, True);
libhockeydata.MakeHockeyConference(sqldatacon, "HOL", "Conference 2", "", "", True);
libhockeydata.MakeHockeyDivision(sqldatacon, "HOL", "Division 3", "Conference 2", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "HOL", "20171001", "St. Paul", "MN", "USA", "United States", "Minnesota", "Smoking Guns", "Conference 2", "Division 3", "SMO Arena", "St. Paul", "", "MIL:Winona Vipers", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "HOL", "20171001", "Minneapolis", "MN", "USA", "United States", "Minnesota", "Armada", "Conference 2", "Division 3", "MIN Arena", "Minneapolis", "", "MIL:New Hope Chaos", True, True);
libhockeydata.MakeHockeyDivision(sqldatacon, "HOL", "Division 4", "Conference 2", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "HOL", "20171001", "Peoria", "IL", "USA", "United States", "Illionis", "Jammers", "Conference 2", "Division 4", "PEO Arena", "Peoria", "", "MIL:Tinley Park Gappers", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "HOL", "20171001", "Joliet", "IL", "USA", "United States", "Illionis", "Gears", "Conference 2", "Division 4", "JOL Arena", "Chicago", "", "MIL:Franklin Park Spirits", True, True);
libhockeydata.MakeHockeyTeamTable(sqldatacon, "MIL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "MIL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "MIL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "MIL");
libhockeydata.MakeHockeyLeague(sqldatacon, "MIL", "Minor League", "USA", "United States", "20171001", "Division=1,Conference=1", "ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.MakeHockeyConference(sqldatacon, "MIL", "Conference 1", "", "", True);
libhockeydata.MakeHockeyDivision(sqldatacon, "MIL", "Division 1", "Conference 1", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "MIL", "20171001", "Northview", "MI", "USA", "United States", "Michigan", "Loggerheads", "Conference 1", "Division 1", "NOR Arena", "Northview", "", "HOL:Detroit Blasters", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "MIL", "20171001", "Gulivoire Park", "IN", "USA", "United States", "Indiana", "Caravans", "Conference 1", "Division 1", "GUL Arena", "Gulivoire Park", "", "HOL:Indianapolis Sabres", True, True);
libhockeydata.MakeHockeyDivision(sqldatacon, "MIL", "Division 2", "Conference 1", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "MIL", "20171001", "Wheeling", "IL", "USA", "United States", "Illionis", "Ramblers", "Conference 1", "Division 2", "WHE Arena", "Wheeling", "", "HOL:Chicago River Bandits", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "MIL", "20171001", "Columbia", "MO", "USA", "United States", "Missouri", "Skychiefs", "Conference 1", "Division 2", "COL Arena", "Columbia", "", "HOL:Kansas City Chariots", True, True);
libhockeydata.MakeHockeyConference(sqldatacon, "MIL", "Conference 2", "", "", True);
libhockeydata.MakeHockeyDivision(sqldatacon, "MIL", "Division 3", "Conference 2", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "MIL", "20171001", "Winona", "MN", "USA", "United States", "Minnesota", "Vipers", "Conference 2", "Division 3", "WIN Arena", "Winona", "", "HOL:St. Paul Smoking Guns", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "MIL", "20171001", "New Hope", "MN", "USA", "United States", "Minnesota", "Chaos", "Conference 2", "Division 3", "NEW Arena", "New Hope", "", "HOL:Minneapolis Armada", True, True);
libhockeydata.MakeHockeyDivision(sqldatacon, "MIL", "Division 4", "Conference 2", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "MIL", "20171001", "Tinley Park", "IL", "USA", "United States", "Illionis", "Gappers", "Conference 2", "Division 4", "TIN Arena", "Tinley Park", "", "HOL:Peoria Jammers", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "MIL", "20171001", "Franklin Park", "IL", "USA", "United States", "Illionis", "Spirits", "Conference 2", "Division 4", "FRA Arena", "Franklin Park", "", "HOL:Chicago Gears", True, True);

libhockeydata.CloseHockeyDatabase(sqldatacon);
