#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals;
import libhockeydata;

hockeyarray = libhockeydata.CreateHockeyArray("./php/data/hockey17-18.db3");
hockeyarray = libhockeydata.AddHockeyLeagueToArray(hockeyarray, "NHL", "National Hockey League", "USA", "United States", "20171004", "Division=3,Conference=2", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", True, True);
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "NHL", "Eastern");
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "NHL", "Western");
hockeyarray = libhockeydata.AddHockeyArenaToArray(hockeyarray, "NHL", "Stockholm", "AB", "SWE", "Sweden", "Stockholm County", "Ericsson Globe");
hockeyarray = libhockeydata.AddHockeyArenaToArray(hockeyarray, "NHL", "Ottawa", "ON", "CAN", "Canada", "Ontario", "Lansdowne Park");
hockeyarray = libhockeydata.AddHockeyArenaToArray(hockeyarray, "NHL", "New York City", "NY", "USA", "United States", "New York", "Citi Field");
hockeyarray = libhockeydata.AddHockeyArenaToArray(hockeyarray, "NHL", "Annapolis", "MD", "USA", "United States", "Maryland", "United States Naval Academy");
hockeyarray = libhockeydata.AddHockeyLeagueToArray(hockeyarray, "AHL", "American Hockey League", "USA", "United States", "20171006", "Division=4", "ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", True, True);
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "AHL", "Eastern");
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "AHL", "Western");
hockeyarray = libhockeydata.AddHockeyArenaToArray(hockeyarray, "AHL", "Hershey", "PA", "USA", "United States", "Pennsylvania", "Hersheypark Stadium");
hockeyarray = libhockeydata.AddHockeyLeagueToArray(hockeyarray, "ECHL", "ECHL", "USA", "United States", "20171013", "Division=4", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", True, True);
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "ECHL", "Eastern");
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "ECHL", "Western");
hockeyarray = libhockeydata.AddHockeyLeagueToArray(hockeyarray, "FHL", "Federal Hockey League", "USA", "United States", "20171027", "League=4", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", False, False);
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "FHL", "");
hockeyarray = libhockeydata.AddHockeyLeagueToArray(hockeyarray, "SPHL", "Southern Professional Hockey League", "USA", "United States", "20171020", "League=8", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", False, False);
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "SPHL", "");
hockeyarray = libhockeydata.AddHockeyLeagueToArray(hockeyarray, "KHL", "Kontinental Hockey League", "RUS", "Russia", "20170821", "Conference=8", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", True, True);
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "KHL", "Western");
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "KHL", "Eastern");
hockeyarray = libhockeydata.AddHockeyArenaToArray(hockeyarray, "KHL", "Helsinki", "FI", "FIN", "Finland", "Finland", "Kaisaniemi Park");
hockeyarray = libhockeydata.AddHockeyArenaToArray(hockeyarray, "KHL", "Riga", "LV", "LVA", "Latvia", "Latvia", "Riga City Council Sports Complex");

libhockeydata.MakeHockeyDatabaseFromHockeyArray(hockeyarray, None, False, False, True);
