#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals;
import libhockeydata;

hockeyarray = libhockeydata.MakeHockeyArray("./php/data/fhmt2y17-18.db3");
hockeyarray = hockeyarray.AddHockeyLeague("HOL", "Hockey League", "USA", "United States", "20171001", "Division=1,Conference=1", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", True, True);
hockeyarray = hockeyarray.AddHockeyConference("HOL", "Conference 1", "", "");
hockeyarray = hockeyarray.AddHockeyDivision("HOL", "Division 1", "Conference 1", "", "");
hockeyarray = hockeyarray.AddHockeyTeam("HOL", "Detroit", "MI", "USA", "United States", "Michigan", "Blasters", "Conference 1", "Division 1", "DET Arena", "Detroit", "", "MIL:Northview Loggerheads");
hockeyarray = hockeyarray.AddHockeyTeam("HOL", "Indianapolis", "IN", "USA", "United States", "Indiana", "Sabres", "Conference 1", "Division 1", "IND Arena", "Indianapolis", "", "MIL:Gulivoire Park Caravans");
hockeyarray = hockeyarray.AddHockeyDivision("HOL", "Division 2", "Conference 1", "", "");
hockeyarray = hockeyarray.AddHockeyTeam("HOL", "Chicago", "IL", "USA", "United States", "Illionis", "River Bandits", "Conference 1", "Division 2", "CHI Arena", "Chicago", "", "MIL:Wheeling Ramblers");
hockeyarray = hockeyarray.AddHockeyTeam("HOL", "Kansas City", "MO", "USA", "United States", "Missouri", "Chariots", "Conference 1", "Division 2", "KAN Arena", "Kansas City", "", "MIL:Columbia Skychiefs");
hockeyarray = hockeyarray.AddHockeyConference("HOL", "Conference 2", "", "");
hockeyarray = hockeyarray.AddHockeyDivision("HOL", "Division 3", "Conference 2", "", "");
hockeyarray = hockeyarray.AddHockeyTeam("HOL", "St. Paul", "MN", "USA", "United States", "Minnesota", "Smoking Guns", "Conference 2", "Division 3", "SMO Arena", "St. Paul", "", "MIL:Winona Vipers");
hockeyarray = hockeyarray.AddHockeyTeam("HOL", "Minneapolis", "MN", "USA", "United States", "Minnesota", "Armada", "Conference 2", "Division 3", "MIN Arena", "Minneapolis", "", "MIL:New Hope Chaos");
hockeyarray = hockeyarray.AddHockeyDivision("HOL", "Division 4", "Conference 2", "", "");
hockeyarray = hockeyarray.AddHockeyTeam("HOL", "Peoria", "IL", "USA", "United States", "Illionis", "Jammers", "Conference 2", "Division 4", "PEO Arena", "Peoria", "", "MIL:Tinley Park Gappers");
hockeyarray = hockeyarray.AddHockeyTeam("HOL", "Joliet", "IL", "USA", "United States", "Illionis", "Gears", "Conference 2", "Division 4", "JOL Arena", "Chicago", "", "MIL:Franklin Park Spirits");
hockeyarray = hockeyarray.AddHockeyLeague("MIL", "Minor League", "USA", "United States", "20171001", "Division=1,Conference=1", "ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", True, True);
hockeyarray = hockeyarray.AddHockeyConference("MIL", "Conference 1", "", "");
hockeyarray = hockeyarray.AddHockeyDivision("MIL", "Division 1", "Conference 1", "", "");
hockeyarray = hockeyarray.AddHockeyTeam("MIL", "Northview", "MI", "USA", "United States", "Michigan", "Loggerheads", "Conference 1", "Division 1", "NOR Arena", "Northview", "", "HOL:Detroit Blasters");
hockeyarray = hockeyarray.AddHockeyTeam("MIL", "Gulivoire Park", "IN", "USA", "United States", "Indiana", "Caravans", "Conference 1", "Division 1", "GUL Arena", "Gulivoire Park", "", "HOL:Indianapolis Sabres");
hockeyarray = hockeyarray.AddHockeyDivision("MIL", "Division 2", "Conference 1", "", "");
hockeyarray = hockeyarray.AddHockeyTeam("MIL", "Wheeling", "IL", "USA", "United States", "Illionis", "Ramblers", "Conference 1", "Division 2", "WHE Arena", "Wheeling", "", "HOL:Chicago River Bandits");
hockeyarray = hockeyarray.AddHockeyTeam("MIL", "Columbia", "MO", "USA", "United States", "Missouri", "Skychiefs", "Conference 1", "Division 2", "COL Arena", "Columbia", "", "HOL:Kansas City Chariots");
hockeyarray = hockeyarray.AddHockeyConference("MIL", "Conference 2", "", "");
hockeyarray = hockeyarray.AddHockeyDivision("MIL", "Division 3", "Conference 2", "", "");
hockeyarray = hockeyarray.AddHockeyTeam("MIL", "Winona", "MN", "USA", "United States", "Minnesota", "Vipers", "Conference 2", "Division 3", "WIN Arena", "Winona", "", "HOL:St. Paul Smoking Guns");
hockeyarray = hockeyarray.AddHockeyTeam("MIL", "New Hope", "MN", "USA", "United States", "Minnesota", "Chaos", "Conference 2", "Division 3", "NEW Arena", "New Hope", "", "HOL:Minneapolis Armada");
hockeyarray = hockeyarray.AddHockeyDivision("MIL", "Division 4", "Conference 2", "", "");
hockeyarray = hockeyarray.AddHockeyTeam("MIL", "Tinley Park", "IL", "USA", "United States", "Illionis", "Gappers", "Conference 2", "Division 4", "TIN Arena", "Tinley Park", "", "HOL:Peoria Jammers");
hockeyarray = hockeyarray.AddHockeyTeam("MIL", "Franklin Park", "IL", "USA", "United States", "Illionis", "Spirits", "Conference 2", "Division 4", "FRA Arena", "Franklin Park", "", "HOL:Chicago Gears");

hockeyarray.MakeHockeyDatabase(None, False, False, True, True);
