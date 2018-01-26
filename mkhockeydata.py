#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2018 Cool Dude 2k - http://idb.berlios.de/
    Copyright 2018 Game Maker 2k - http://intdb.sourceforge.net/
    Copyright 2018 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: mkhockeydata.py - Last Update: 1/25/2018 Ver. 0.0.1 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals;
import sqlite3, sys, os, re, libhockeydata;

leaguename = "NHL";
leaguefullname = "National Hockey League";
getstartday = "01";
getforday = "07";
getformonth = "10";
getforyearshort = "17";
getforyear = "20"+getforyearshort;
getendyearshort = "18";
getendyear = "20"+getendyearshort;

sqldatacon = libhockeydata.MakeHockeyDatabase(leaguename, "./"+leaguename.lower()+str(getforyearshort)+"-"+str(getendyearshort)+".db3");
libhockeydata.MakeHockeyLeagueTable(sqldatacon, leaguename);
libhockeydata.MakeHockeyLeagues(sqldatacon, leaguename, leaguefullname);
libhockeydata.MakeHockeyConferenceTable(sqldatacon, leaguename);
libhockeydata.MakeHockeyConferences(sqldatacon, leaguename, "Eastern");
libhockeydata.MakeHockeyConferences(sqldatacon, leaguename, "Western");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, leaguename);
libhockeydata.MakeHockeyDivisions(sqldatacon, leaguename, "Atlantic", "Eastern");
libhockeydata.MakeHockeyDivisions(sqldatacon, leaguename, "Metropolitan", "Eastern");
libhockeydata.MakeHockeyDivisions(sqldatacon, leaguename, "Central", "Western");
libhockeydata.MakeHockeyDivisions(sqldatacon, leaguename, "Pacific", "Western");
libhockeydata.MakeHockeyTeamTable(sqldatacon, leaguename);
print("Inserting "+leaguename+" Teams From Eastern Conference.");
print("Inserting "+leaguename+" Teams From Atlantic Division.\n");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Boston", "MA", "Bruins", "Eastern", "Atlantic", "TD Garden", "Boston");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Buffalo", "NY", "Sabres", "Eastern", "Atlantic", "KeyBank Center", "Buffalo");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Detroit", "MI", "Red Wings", "Eastern", "Atlantic", "Little Caesars Arena", "Detroit");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Sunrise", "FL", "Panthers", "Eastern", "Atlantic", "BB&T Center", "Florida");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Montreal", "QC", "Canadiens", "Eastern", "Atlantic", "Bell Centre", "Montreal");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Ottawa", "ON", "Senators", "Eastern", "Atlantic", "Canadian Tire Centre", "Ottawa");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Tampa Bay", "FL", "Lightning", "Eastern", "Atlantic", "Amalie Arena", "Tampa Bay");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Toronto", "ON", "Maple Leafs", "Eastern", "Atlantic", "Air Canada Centre", "Toronto");
print("Inserting "+leaguename+" Teams From Metropolitan Division.\n");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Carolina", "NC", "Hurricanes", "Eastern", "Metropolitan", "PNC Arena", "Carolina");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Columbus", "OH", "Blue Jackets", "Eastern", "Metropolitan", "Nationwide Arena", "Columbus");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "New Jersey", "NJ", "Devils", "Eastern", "Metropolitan", "Prudential Center", "New Jersey");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "New York City", "NY", "Islanders", "Eastern", "Metropolitan", "Barclays Center", "New York");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "New York City", "NY", "Rangers", "Eastern", "Metropolitan", "Madison Square Garden", "New York");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Philadelphia", "PA", "Flyers", "Eastern", "Metropolitan", "Wells Fargo Center", "Philadelphia");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Pittsburgh", "PA", "Penguins", "Eastern", "Metropolitan", "PPG Paints Arena", "Pittsburgh");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Washington", "D.C.", "Capitals", "Eastern", "Metropolitan", "Capital One Arena", "Washington");
print("Inserting "+leaguename+" Teams From Western Conference.");
print("Inserting "+leaguename+" Teams From Central Division.\n");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Chicago", "IL", "Blackhawks", "Western", "Central", "United Center", "Chicago");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Denver", "CO", "Avalanche", "Western", "Central", "Pepsi Center", "Colorado");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Dallas", "TX", "Stars", "Western", "Central", "American Airlines Center", "Dallas");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "St. Paul", "MN", "Wild", "Western", "Central", "Xcel Energy Center", "Minnesota");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Nashville", "TN", "Predators", "Western", "Central", "Bridgestone Arena", "Nashville");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "St. Louis", "MO", "Blues", "Western", "Central", "Scottrade Center", "St. Louis");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Winnipeg", "MB", "Jets", "Western", "Central", "Bell MTS Place", "Winnipeg");
print("Inserting "+leaguename+" Teams From Pacific Division.\n");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Anaheim", "CA", "Ducks", "Western", "Pacific", "Honda Center", "Anaheim");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Glendale", "AZ", "Coyotes", "Western", "Pacific", "Gila River Arena", "Arizona");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Calgary", "AB", "Flames", "Western", "Pacific", "Scotiabank Saddledome", "Calgary");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Edmonton", "AB", "Oilers", "Western", "Pacific", "Rogers Place", "Edmonton");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Los Angeles", "CA", "Kings", "Western", "Pacific", "Staples Center", "Los Angeles");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "San Jose", "CA", "Sharks", "Western", "Pacific", "SAP Center", "San Jose");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Vancouver", "BC", "Canucks", "Western", "Pacific", "Rogers Arena", "Vancouver");
libhockeydata.MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Paradise", "NV", "Golden Knights", "Western", "Pacific", "T-Mobile Arena", "Vegas");
libhockeydata.MakeHockeyArena(sqldatacon, leaguename, "Queens", "NY", "Citi Field");
libhockeydata.MakeHockeyArena(sqldatacon, leaguename, "Annapolis", "MD", "Navy-Marine Corps Memorial Stadium");
libhockeydata.MakeHockeyGameTable(sqldatacon, leaguename);
libhockeydata.CloseHockeyDatabase(sqldatacon, leaguename);
