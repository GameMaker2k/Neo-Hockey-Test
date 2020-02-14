#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals;
import libhockeydata.hockeyfunctions;

sqldatacon = libhockeydata.hockeyfunctions.MakeHockeyDatabase("./fhmt1y17-18.db3");
libhockeydata.hockeyfunctions.MakeHockeyLeagueTable(sqldatacon);
libhockeydata.hockeyfunctions.MakeHockeyTeamTable(sqldatacon, "HOL");
libhockeydata.hockeyfunctions.MakeHockeyConferenceTable(sqldatacon, "HOL");
libhockeydata.hockeyfunctions.MakeHockeyGameTable(sqldatacon, "HOL");
libhockeydata.hockeyfunctions.MakeHockeyDivisionTable(sqldatacon, "HOL");
libhockeydata.hockeyfunctions.MakeHockeyLeague(sqldatacon, "HOL", "Hockey League", "USA", "United States", "20171001", "Division=1,Conference=1", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.hockeyfunctions.MakeHockeyConference(sqldatacon, "HOL", "Conference 1", True);
libhockeydata.hockeyfunctions.MakeHockeyDivision(sqldatacon, "HOL", "Division 1", "Conference 1", True, True);
libhockeydata.hockeyfunctions.MakeHockeyTeam(sqldatacon, "HOL", "20171001", "Kansas City", "MO", "USA", "United States", "Missouri", "Flies", "Conference 1", "Division 1", "KAN Arena", "Kansas City", "", True, True);
libhockeydata.hockeyfunctions.MakeHockeyTeam(sqldatacon, "HOL", "20171001", "Chicago", "IL", "USA", "United States", "Illionis", "Lampreys", "Conference 1", "Division 1", "CHI Arena", "Chicago", "", True, True);
libhockeydata.hockeyfunctions.MakeHockeyDivision(sqldatacon, "HOL", "Division 2", "Conference 1", True, True);
libhockeydata.hockeyfunctions.MakeHockeyTeam(sqldatacon, "HOL", "20171001", "Ft. Wayne", "IN", "USA", "United States", "Indiana", "Whitecaps", "Conference 1", "Division 2", "WHI Arena", "Ft. Wayne", "", True, True);
libhockeydata.hockeyfunctions.MakeHockeyTeam(sqldatacon, "HOL", "20171001", "Minneapolis", "MN", "USA", "United States", "Minnesota", "Frogs", "Conference 1", "Division 2", "MIN Arena", "Minneapolis", "", True, True);
libhockeydata.hockeyfunctions.MakeHockeyConference(sqldatacon, "HOL", "Conference 2", True);
libhockeydata.hockeyfunctions.MakeHockeyDivision(sqldatacon, "HOL", "Division 3", "Conference 2", True, True);
libhockeydata.hockeyfunctions.MakeHockeyTeam(sqldatacon, "HOL", "20171001", "Columbus", "OH", "USA", "United States", "Ohio", "Passion", "Conference 2", "Division 3", "COL Arena", "Columbus", "", True, True);
libhockeydata.hockeyfunctions.MakeHockeyTeam(sqldatacon, "HOL", "20171001", "Akron", "OH", "USA", "United States", "Ohio", "Cattlemen", "Conference 2", "Division 3", "AKR Arena", "Akron", "", True, True);
libhockeydata.hockeyfunctions.MakeHockeyDivision(sqldatacon, "HOL", "Division 4", "Conference 2", True, True);
libhockeydata.hockeyfunctions.MakeHockeyTeam(sqldatacon, "HOL", "20171001", "Indianapolis", "IN", "USA", "United States", "Indiana", "Gears", "Conference 2", "Division 4", "IND Arena", "Indianapolis", "", True, True);
libhockeydata.hockeyfunctions.MakeHockeyTeam(sqldatacon, "HOL", "20171001", "Wichita", "KS", "USA", "United States", "Kansas", "Rail Hawks", "Conference 2", "Division 4", "WIC Arena", "Wichita", "", True, True);
libhockeydata.hockeyfunctions.MakeHockeyTeamTable(sqldatacon, "MIL");
libhockeydata.hockeyfunctions.MakeHockeyConferenceTable(sqldatacon, "MIL");
libhockeydata.hockeyfunctions.MakeHockeyGameTable(sqldatacon, "MIL");
libhockeydata.hockeyfunctions.MakeHockeyDivisionTable(sqldatacon, "MIL");
libhockeydata.hockeyfunctions.MakeHockeyLeague(sqldatacon, "MIL", "Minor League", "USA", "United States", "20171001", "Division=1,Conference=1", "ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.hockeyfunctions.MakeHockeyConference(sqldatacon, "MIL", "Conference 1", True);
libhockeydata.hockeyfunctions.MakeHockeyDivision(sqldatacon, "MIL", "Division 1", "Conference 1", True, True);
libhockeydata.hockeyfunctions.MakeHockeyTeam(sqldatacon, "MIL", "20171001", "Milan", "MO", "USA", "United States", "Missouri", "Dazzle", "Conference 1", "Division 1", "MIL Arena", "Milan", "", True, True);
libhockeydata.hockeyfunctions.MakeHockeyTeam(sqldatacon, "MIL", "20171001", "Moline", "IL", "USA", "United States", "Illionis", "Expositions", "Conference 1", "Division 1", "MOL Arena", "Moline", "", True, True);
libhockeydata.hockeyfunctions.MakeHockeyDivision(sqldatacon, "MIL", "Division 2", "Conference 1", True, True);
libhockeydata.hockeyfunctions.MakeHockeyTeam(sqldatacon, "MIL", "20171001", "Kokomo", "IN", "USA", "United States", "Indiana", "Loggerheads", "Conference 1", "Division 2", "KOK Arena", "Kokomo", "", True, True);
libhockeydata.hockeyfunctions.MakeHockeyTeam(sqldatacon, "MIL", "20171001", "Becker", "MN", "USA", "United States", "Minnesota", "Winged Wheelers", "Conference 1", "Division 2", "BEC Arena", "Becker", "", True, True);
libhockeydata.hockeyfunctions.MakeHockeyConference(sqldatacon, "MIL", "Conference 2", True);
libhockeydata.hockeyfunctions.MakeHockeyDivision(sqldatacon, "MIL", "Division 3", "Conference 2", True, True);
libhockeydata.hockeyfunctions.MakeHockeyTeam(sqldatacon, "MIL", "20171001", "Toledo", "OH", "USA", "United States", "Ohio", "Pugs", "Conference 2", "Division 3", "TOL Arena", "Toledo", "", True, True);
libhockeydata.hockeyfunctions.MakeHockeyTeam(sqldatacon, "MIL", "20171001", "Mason", "OH", "USA", "United States", "Ohio", "Caravans", "Conference 2", "Division 3", "MAS Arena", "Mason", "", True, True);
libhockeydata.hockeyfunctions.MakeHockeyDivision(sqldatacon, "MIL", "Division 4", "Conference 2", True, True);
libhockeydata.hockeyfunctions.MakeHockeyTeam(sqldatacon, "MIL", "20171001", "Lawrence", "IN", "USA", "United States", "Indiana", "Walkers", "Conference 2", "Division 4", "LAW Arena", "Lawrence", "", True, True);
libhockeydata.hockeyfunctions.MakeHockeyTeam(sqldatacon, "MIL", "20171001", "Garden City", "KS", "USA", "United States", "Kansas", "Jammers", "Conference 2", "Division 4", "GAR Arena", "Garden City", "", True, True);

libhockeydata.hockeyfunctions.CloseHockeyDatabase(sqldatacon);
