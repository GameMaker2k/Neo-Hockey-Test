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

hockeyarray = libhockeydata.CreateHockeyArray("./php/data/fhmt1y17-18.db3");
hockeyarray = libhockeydata.AddHockeyLeagueToArray(hockeyarray, "HOL", "Hockey League", "USA", "United States", "20171001", "Division=1,Conference=1", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", True, True);
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "HOL", "Conference 1");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "HOL", "Division 1", "Conference 1", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "HOL", "Kansas City", "MO", "USA", "United States", "Missouri", "Flies", "Conference 1", "Division 1", "KAN Arena", "Kansas City", "", "MIL:Milan Dazzle");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "HOL", "Chicago", "IL", "USA", "United States", "Illionis", "Lampreys", "Conference 1", "Division 1", "CHI Arena", "Chicago", "", "MIL:Moline Expositions");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "HOL", "Division 2", "Conference 1", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "HOL", "Ft. Wayne", "IN", "USA", "United States", "Indiana", "Whitecaps", "Conference 1", "Division 2", "WHI Arena", "Ft. Wayne", "", "MIL:Kokomo Loggerheads");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "HOL", "Minneapolis", "MN", "USA", "United States", "Minnesota", "Frogs", "Conference 1", "Division 2", "MIN Arena", "Minneapolis", "", "MIL:Becker Winged Wheelers");
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "HOL", "Conference 2");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "HOL", "Division 3", "Conference 2", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "HOL", "Columbus", "OH", "USA", "United States", "Ohio", "Passion", "Conference 2", "Division 3", "COL Arena", "Columbus", "", "MIL:Toledo Pugs");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "HOL", "Akron", "OH", "USA", "United States", "Ohio", "Cattlemen", "Conference 2", "Division 3", "AKR Arena", "Akron", "", "MIL:Mason Caravans");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "HOL", "Division 4", "Conference 2", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "HOL", "Indianapolis", "IN", "USA", "United States", "Indiana", "Gears", "Conference 2", "Division 4", "IND Arena", "Indianapolis", "", "MIL:Lawrence Walkers");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "HOL", "Wichita", "KS", "USA", "United States", "Kansas", "Rail Hawks", "Conference 2", "Division 4", "WIC Arena", "Wichita", "", "MIL:Garden City Jammers");
hockeyarray = libhockeydata.AddHockeyLeagueToArray(hockeyarray, "MIL", "Minor League", "USA", "United States", "20171001", "Division=1,Conference=1", "ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", True, True);
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "MIL", "Conference 1");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "MIL", "Division 1", "Conference 1", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "MIL", "Milan", "MO", "USA", "United States", "Missouri", "Dazzle", "Conference 1", "Division 1", "MIL Arena", "Milan", "", "HOL:Kansas City Flies");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "MIL", "Moline", "IL", "USA", "United States", "Illionis", "Expositions", "Conference 1", "Division 1", "MOL Arena", "Moline", "", "HOL:Chicago Lampreys");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "MIL", "Division 2", "Conference 1", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "MIL", "Kokomo", "IN", "USA", "United States", "Indiana", "Loggerheads", "Conference 1", "Division 2", "KOK Arena", "Kokomo", "", "HOL:Ft. Wayne Whitecaps");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "MIL", "Becker", "MN", "USA", "United States", "Minnesota", "Winged Wheelers", "Conference 1", "Division 2", "BEC Arena", "Becker", "", "HOL:Minneapolis Frogs");
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "MIL", "Conference 2");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "MIL", "Division 3", "Conference 2", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "MIL", "Toledo", "OH", "USA", "United States", "Ohio", "Pugs", "Conference 2", "Division 3", "TOL Arena", "Toledo", "", "HOL:Columbus Passion");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "MIL", "Mason", "OH", "USA", "United States", "Ohio", "Caravans", "Conference 2", "Division 3", "MAS Arena", "Mason", "", "HOL:Akron Cattlemen");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "MIL", "Division 4", "Conference 2", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "MIL", "Lawrence", "IN", "USA", "United States", "Indiana", "Walkers", "Conference 2", "Division 4", "LAW Arena", "Lawrence", "", "HOL:Indianapolis Gears");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "MIL", "Garden City", "KS", "USA", "United States", "Kansas", "Jammers", "Conference 2", "Division 4", "GAR Arena", "Garden City", "", "HOL:Wichita Rail Hawks");

libhockeydata.MakeHockeyDatabaseFromHockeyArray(hockeyarray, None, False, True, True);
