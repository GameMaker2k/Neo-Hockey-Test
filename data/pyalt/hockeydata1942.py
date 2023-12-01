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

hockeyarray = libhockeydata.CreateHockeyArray("./php/data/hockey1942-43.db3");
hockeyarray = libhockeydata.AddHockeyLeagueToArray(hockeyarray, "NHL", "National Hockey League", "USA", "United States", "19421031", "League=4", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", False, False);
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "NHL", "");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "NHL", "", "", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Boston", "MA", "USA", "United States", "Massachusetts", "Bruins", "", "", "Boston Garden", "Boston", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Chicago", "IL", "USA", "United States", "Illinois", "Blackhawks", "", "", "Chicago Stadium", "Chicago", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Detroit", "MI", "USA", "United States", "Michigan", "Red Wings", "", "", "Detroit Olympia", "Detroit", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Montreal", "QC", "CAN", "Canada", "Quebec", "Canadiens", "", "", "Montreal Forum", "Montreal", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "New York City", "NY", "USA", "United States", "New York", "Rangers", "", "", "Madison Square Garden", "New York", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Toronto", "ON", "CAN", "Canada", "Ontario", "Maple Leafs", "", "", "Maple Leaf Gardens", "Toronto", "", "");
hockeyarray = libhockeydata.AddHockeyLeagueToArray(hockeyarray, "AHL", "American Hockey League", "USA", "United States", "19421031", "League=4", "ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", False, False);
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "AHL", "");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "AHL", "", "", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Buffalo", "NY", "USA", "United States", "New York", "Bisons", "", "", "Buffalo Memorial Auditorium", "Buffalo", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Cleveland", "OH", "USA", "United States", "Ohio", "Barons", "", "", "Cleveland Arena", "Cleveland", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Hershey", "PA", "USA", "United States", "Pennsylvania", "Red Wings", "", "", "Hersheypark Arena", "Hershey", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Indianapolis", "IN", "USA", "United States", "Indiana", "Capitals", "", "", "Indiana State Fairgrounds Coliseum", "Indianapolis", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Philadelphia", "PA", "USA", "United States", "Pennsylvania", "Rockets", "", "", "Philadelphia Arena", "Philadelphia", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Pittsburgh", "PA", "USA", "United States", "Pennsylvania", "Hornets", "", "", "Duquesne Gardens", "Pittsburgh", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Providence", "RI", "USA", "United States", "Rhode Island", "Reds", "", "", "Rhode Island Auditorium", "Providence", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "West Springfield", "MA", "USA", "United States", "Massachusetts", "Indians", "", "", "Eastern States Coliseum", "Springfield", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Washington", "DC", "USA", "United States", "District of Columbia", "Lions", "", "", "Washington Coliseum", "Washington", "", "");

libhockeydata.MakeHockeyDatabaseFromHockeyArray(hockeyarray, None, False, True, True);
