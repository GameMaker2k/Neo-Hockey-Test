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

sqldatacon = libhockeydata.MakeHockeyDatabase("./php/data/hockey1942-43.db3");
libhockeydata.MakeHockeyLeagueTable(sqldatacon);
libhockeydata.MakeHockeyTeamTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyLeague(sqldatacon, "NHL", "National Hockey League", "USA", "United States", "19421031", "League=4", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.MakeHockeyConference(sqldatacon, "NHL", "", "", "Conference", False);
libhockeydata.MakeHockeyDivision(sqldatacon, "NHL", "", "", "", "Division", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "19421031", "Boston", "MA", "USA", "United States", "Massachusetts", "Bruins", "", "", "Boston Garden", "Boston", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "19421031", "Chicago", "IL", "USA", "United States", "Illinois", "Blackhawks", "", "", "Chicago Stadium", "Chicago", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "19421031", "Detroit", "MI", "USA", "United States", "Michigan", "Red Wings", "", "", "Detroit Olympia", "Detroit", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "19421031", "Montreal", "QC", "CAN", "Canada", "Quebec", "Canadiens", "", "", "Montreal Forum", "Montreal", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "19421031", "New York City", "NY", "USA", "United States", "New York", "Rangers", "", "", "Madison Square Garden", "New York", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "19421031", "Toronto", "ON", "CAN", "Canada", "Ontario", "Maple Leafs", "", "", "Maple Leaf Gardens", "Toronto", "", "", False, False);
libhockeydata.MakeHockeyTeamTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyLeague(sqldatacon, "AHL", "American Hockey League", "USA", "United States", "19421031", "League=4", "ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.MakeHockeyConference(sqldatacon, "AHL", "", "", "Conference", False);
libhockeydata.MakeHockeyDivision(sqldatacon, "AHL", "", "", "", "Division", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "19421031", "Buffalo", "NY", "USA", "United States", "New York", "Bisons", "", "", "Buffalo Memorial Auditorium", "Buffalo", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "19421031", "Cleveland", "OH", "USA", "United States", "Ohio", "Barons", "", "", "Cleveland Arena", "Cleveland", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "19421031", "Hershey", "PA", "USA", "United States", "Pennsylvania", "Red Wings", "", "", "Hersheypark Arena", "Hershey", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "19421031", "Indianapolis", "IN", "USA", "United States", "Indiana", "Capitals", "", "", "Indiana State Fairgrounds Coliseum", "Indianapolis", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "19421031", "Philadelphia", "PA", "USA", "United States", "Pennsylvania", "Rockets", "", "", "Philadelphia Arena", "Philadelphia", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "19421031", "Pittsburgh", "PA", "USA", "United States", "Pennsylvania", "Hornets", "", "", "Duquesne Gardens", "Pittsburgh", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "19421031", "Providence", "RI", "USA", "United States", "Rhode Island", "Reds", "", "", "Rhode Island Auditorium", "Providence", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "19421031", "West Springfield", "MA", "USA", "United States", "Massachusetts", "Indians", "", "", "Eastern States Coliseum", "Springfield", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "19421031", "Washington", "DC", "USA", "United States", "District of Columbia", "Lions", "", "", "Washington Coliseum", "Washington", "", "", False, False);

libhockeydata.CloseHockeyDatabase(sqldatacon);
