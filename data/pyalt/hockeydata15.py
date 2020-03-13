#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals;
import libhockeydata;

hockeyarray = libhockeydata.CreateHockeyArray("./php/data/hockey15-16.db3");
hockeyarray = libhockeydata.AddHockeyLeagueToArray(hockeyarray, "ECHL", "ECHL", "USA", "United States", "20151007", "Division=1,Conference=5", "ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", True, True);
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "ECHL", "Eastern");
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "ECHL", "Western");
hockeyarray = libhockeydata.AddHockeyLeagueToArray(hockeyarray, "AHL", "American Hockey League", "USA", "United States", "20151009", "Division=4", "ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", True, True);
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "AHL", "Eastern");
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "AHL", "Western");
hockeyarray = libhockeydata.AddHockeyArenaToArray(hockeyarray, "AHL", "West Sacramento", "CA", "USA", "United States", "California", "Raley Field");
hockeyarray = libhockeydata.AddHockeyLeagueToArray(hockeyarray, "NHL", "National Hockey League", "USA", "United States", "20151007", "Division=3,Conference=2", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", True, True);
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "NHL", "Eastern");
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "NHL", "Western");
hockeyarray = libhockeydata.AddHockeyArenaToArray(hockeyarray, "NHL", "Foxborough", "MA", "USA", "United States", "Massachusetts", "Gillette Stadium");
hockeyarray = libhockeydata.AddHockeyArenaToArray(hockeyarray, "NHL", "Minneapolis", "MN", "USA", "United States", "Minnesota", "TCF Bank Stadium");
hockeyarray = libhockeydata.AddHockeyArenaToArray(hockeyarray, "NHL", "Denver", "CO", "USA", "United States", "Colorado", "Coors Field");

libhockeydata.MakeHockeyDatabaseFromHockeyArray(hockeyarray, None, False, False, True);
