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

sqldatacon = libhockeydata.MakeHockeyDatabase("./php/data/hockey20-21.db3");
libhockeydata.MakeHockeyLeagueTable(sqldatacon);
libhockeydata.MakeHockeyTeamTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyLeague(sqldatacon, "NHL", "National Hockey League", "USA", "United States", "20210113", "Division=4", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.MakeHockeyConference(sqldatacon, "NHL", "", "", "Conference", False);
libhockeydata.MakeHockeyDivision(sqldatacon, "NHL", "Central", "", "Discover", "Division", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Carolina", "NC", "USA", "United States", "North Carolina", "Hurricanes", "", "Central", "PNC Arena", "Carolina", "", "AHL:Chicago Wolves", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Chicago", "IL", "USA", "United States", "Illinois", "Blackhawks", "", "Central", "United Center", "Chicago", "", "AHL:Rockford IceHogs", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Columbus", "OH", "USA", "United States", "Ohio", "Blue Jackets", "", "Central", "Nationwide Arena", "Columbus", "", "AHL:Cleveland Monsters", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Dallas", "TX", "USA", "United States", "Texas", "Stars", "", "Central", "American Airlines Center", "Dallas", "", "AHL:Texas Stars", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Detroit", "MI", "USA", "United States", "Michigan", "Red Wings", "", "Central", "Little Caesars Arena", "Detroit", "", "AHL:Grand Rapids Griffins", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Sunrise", "FL", "USA", "United States", "Florida", "Panthers", "", "Central", "BB&T Center", "Florida", "", "AHL:Syracuse Crunch", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Nashville", "TN", "USA", "United States", "Tennessee", "Predators", "", "Central", "Bridgestone Arena", "Nashville", "", "AHL:Chicago Wolves", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Tampa Bay", "FL", "USA", "United States", "Florida", "Lightning", "", "Central", "Amalie Arena", "Tampa Bay", "", "AHL:Syracuse Crunch", False, True);
libhockeydata.MakeHockeyDivision(sqldatacon, "NHL", "West", "", "Honda", "Division", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Anaheim", "CA", "USA", "United States", "California", "Ducks", "", "West", "Honda Center", "Anaheim", "", "AHL:San Diego Gulls", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Glendale", "AZ", "USA", "United States", "Arizona", "Coyotes", "", "West", "Gila River Arena", "Arizona", "", "AHL:Tucson Roadrunners", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Denver", "CO", "USA", "United States", "Colorado", "Avalanche", "", "West", "Ball Arena", "Colorado", "", "AHL:Colorado Eagles", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Los Angeles", "CA", "USA", "United States", "California", "Kings", "", "West", "Staples Center", "Los Angeles", "", "AHL:Ontario Reign", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "St. Paul", "MN", "USA", "United States", "Minnesota", "Wild", "", "West", "Xcel Energy Center", "Minnesota", "", "AHL:Iowa Wild", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "St. Louis", "MO", "USA", "United States", "Missouri", "Blues", "", "West", "Enterprise Center", "St. Louis", "", "AHL:Utica Comets", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "San Jose", "CA", "USA", "United States", "California", "Sharks", "", "West", "SAP Center", "San Jose", "", "AHL:San Jose Barracuda", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Paradise", "NV", "USA", "United States", "Nevada", "Golden Knights", "", "West", "T-Mobile Arena", "Vegas", "", "AHL:Henderson Silver Knights", False, True);
libhockeydata.MakeHockeyDivision(sqldatacon, "NHL", "East", "", "Massmutual", "Division", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Boston", "MA", "USA", "United States", "Massachusetts", "Bruins", "", "East", "TD Garden", "Boston", "", "AHL:Providence Bruins", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Buffalo", "NY", "USA", "United States", "New York", "Sabres", "", "East", "KeyBank Center", "Buffalo", "", "AHL:Rochester Americans", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "New Jersey", "NJ", "USA", "United States", "New Jersey", "Devils", "", "East", "Prudential Center", "New Jersey", "", "AHL:Binghamton Devils", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Uniondale", "NY", "USA", "United States", "New York", "Islanders", "", "East", "Nassau Coliseum", "New York", "", "AHL:Bridgeport Sound Tigers", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "New York City", "NY", "USA", "United States", "New York", "Rangers", "", "East", "Madison Square Garden", "New York", "", "AHL:Hartford Wolf Pack", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Philadelphia", "PA", "USA", "United States", "Pennsylvania", "Flyers", "", "East", "Wells Fargo Center", "Philadelphia", "", "AHL:Lehigh Valley Phantoms", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Pittsburgh", "PA", "USA", "United States", "Pennsylvania", "Penguins", "", "East", "PPG Paints Arena", "Pittsburgh", "", "AHL:Wilkes-Barre/Scranton Penguins", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Washington", "DC", "USA", "United States", "District of Columbia", "Capitals", "", "East", "Capital One Arena", "Washington", "", "AHL:Hershey Bears", False, True);
libhockeydata.MakeHockeyDivision(sqldatacon, "NHL", "North", "", "Scotia", "Division", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Calgary", "AB", "CAN", "Canada", "Alberta", "Flames", "", "North", "Scotiabank Saddledome", "Calgary", "", "AHL:Stockton Heat", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Edmonton", "AB", "CAN", "Canada", "Alberta", "Oilers", "", "North", "Rogers Place", "Edmonton", "", "AHL:Bakersfield Condors", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Montreal", "QC", "CAN", "Canada", "Quebec", "Canadiens", "", "North", "Bell Centre", "Montreal", "", "AHL:Laval Rocket", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Ottawa", "ON", "CAN", "Canada", "Ontario", "Senators", "", "North", "Canadian Tire Centre", "Ottawa", "", "AHL:Belleville Senators", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Toronto", "ON", "CAN", "Canada", "Ontario", "Maple Leafs", "", "North", "Scotiabank Arena", "Toronto", "", "AHL:Toronto Marlies", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Vancouver", "BC", "CAN", "Canada", "British Columbia", "Canucks", "", "North", "Rogers Arena", "Vancouver", "", "AHL:Utica Comets", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20210113", "Winnipeg", "MB", "CAN", "Canada", "Manitoba", "Jets", "", "North", "Bell MTS Place", "Winnipeg", "", "AHL:Manitoba Moose", False, True);
libhockeydata.MakeHockeyTeamTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyLeague(sqldatacon, "AHL", "American Hockey League", "USA", "United States", "20210205", "Division=4", "ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.MakeHockeyConference(sqldatacon, "AHL", "", "", "Conference", False);
libhockeydata.MakeHockeyDivision(sqldatacon, "AHL", "Atlantic", "", "", "Division", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Bridgeport", "CT", "USA", "United States", "Connecticut", "Sound Tigers", "", "Atlantic", "Webster Bank Arena", "Bridgeport", "", "NHL:New York Islanders", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Hartford", "CT", "USA", "United States", "Connecticut", "Wolf Pack", "", "Atlantic", "XL Center", "Hartford", "", "NHL:New York Rangers", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Providence", "RI", "USA", "United States", "Rhode Island", "Bruins", "", "Atlantic", "Dunkin' Donuts Center", "Providence", "", "NHL:Boston Bruins", False, True);
libhockeydata.MakeHockeyDivision(sqldatacon, "AHL", "North", "", "", "Division", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Newark", "NJ", "USA", "United States", "New Jersey", "Devils", "", "North", "Barnabas Health Hockey House", "Binghamton", "", "NHL:New Jersey Devils", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Hershey", "PA", "USA", "United States", "Pennsylvania", "Bears", "", "North", "Giant Center", "Hershey", "", "NHL:Washington Capitals", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Allentown", "PA", "USA", "United States", "Pennsylvania", "Phantoms", "", "North", "PPL Center", "Lehigh Valley", "", "NHL:Philadelphia Flyers", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Buffalo", "NY", "USA", "United States", "New York", "Americans", "", "North", "KeyBank Center", "Rochester", "", "NHL:Buffalo Sabres", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Syracuse", "NY", "USA", "United States", "New York", "Crunch", "", "North", "Oncenter War Memorial Arena", "Syracuse", "", "NHL:Tampa Bay Lightning;Florida Panthers", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Utica", "NY", "USA", "United States", "New York", "Comets", "", "North", "Adirondack Bank Center", "Utica", "", "NHL:Vancouver Canucks;St. Louis Blues", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Wilkes-Barre", "PA", "USA", "United States", "Pennsylvania", "Penguins", "", "North", "Mohegan Sun Arena", "Wilkes-Barre/Scranton", "", "NHL:Pittsburgh Penguins", False, True);
libhockeydata.MakeHockeyDivision(sqldatacon, "AHL", "Canadian", "", "", "Division", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Ottawa", "ON", "CAN", "Canada", "Ontario", "Senators", "", "Canadian", "Canadian Tire Centre", "Belleville", "", "NHL:Ottawa Senators", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Montreal", "QC", "CAN", "Canada", "Quebec", "Rocket", "", "Canadian", "Bell Centre", "Laval", "", "NHL:Montreal Canadiens", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Winnipeg", "MB", "CAN", "Canada", "Manitoba", "Moose", "", "Canadian", "Bell MTS Iceplex", "Manitoba", "", "NHL:Winnipeg Jets", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Calgary", "AB", "CAN", "Canada", "Alberta", "Heat", "", "Canadian", "Scotiabank Saddledome", "Stockton", "", "NHL:Calgary Flames", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Toronto", "ON", "CAN", "Canada", "Ontario", "Marlies", "", "Canadian", "Scotiabank Arena", "Toronto", "", "NHL:Toronto Maple Leafs", False, True);
libhockeydata.MakeHockeyDivision(sqldatacon, "AHL", "Central", "", "", "Division", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Rosemont", "IL", "USA", "United States", "Illinois", "Wolves", "", "Central", "Allstate Arena", "Chicago", "", "NHL:Carolina Hurricanes", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Cleveland", "OH", "USA", "United States", "Ohio", "Monsters", "", "Central", "Rocket Mortgage FieldHouse", "Lake Erie", "", "NHL:Columbus Blue Jackets", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Grand Rapids", "MI", "USA", "United States", "Michigan", "Griffins", "", "Central", "Van Andel Arena", "Grand Rapids", "", "NHL:Detroit Red Wings", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Des Moines", "IA", "USA", "United States", "Iowa", "Wild", "", "Central", "Wells Fargo Arena", "Iowa", "", "NHL:Minnesota Wild", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Rockford", "IL", "USA", "United States", "Illinois", "IceHogs", "", "Central", "BMO Harris Bank Center", "Rockford", "", "NHL:Chicago Blackhawks", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Cedar Park", "TX", "USA", "United States", "Texas", "Stars", "", "Central", "H-E-B Center", "Texas", "", "NHL:Dallas Stars", False, True);
libhockeydata.MakeHockeyDivision(sqldatacon, "AHL", "Pacific", "", "", "Division", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Bakersfield", "CA", "USA", "United States", "California", "Condors", "", "Pacific", "Mechanics Bank Arena", "Bakersfield", "", "NHL:Edmonton Oilers", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Loveland", "CO", "USA", "United States", "Colorado", "Eagles", "", "Pacific", "Budweiser Events Center", "Colorado", "", "NHL:Colorado Avalanche", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Paradise", "NV", "USA", "United States", "Nevada", "Silver Knights", "", "Pacific", "Orleans Arena", "Henderson", "", "NHL:Vegas Golden Knights", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "El Segundo", "CA", "USA", "United States", "California", "Reign", "", "Pacific", "Toyota Sports Center", "Ontario", "", "NHL:Los Angeles Kings", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Irvine", "CA", "USA", "United States", "California", "Gulls", "", "Pacific", "Great Park Ice & FivePoint Arena", "San Diego", "", "NHL:Anaheim Ducks", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "San Jose", "CA", "USA", "United States", "California", "Barracuda", "", "Pacific", "SAP Center", "San Jose", "", "NHL:San Jose Sharks", False, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20210205", "Tucson", "AZ", "USA", "United States", "Arizona", "Roadrunners", "", "Pacific", "Tucson Convention Center", "Tucson", "", "NHL:Arizona Coyotes", False, True);

libhockeydata.CloseHockeyDatabase(sqldatacon);
