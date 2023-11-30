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

hockeyarray = libhockeydata.CreateHockeyArray("./php/data/hockey20-21.db3");
hockeyarray = libhockeydata.AddHockeyLeagueToArray(hockeyarray, "NHL", "National Hockey League", "USA", "United States", "20210113", "Division=4", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", False, True);
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "NHL", "");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "NHL", "Central", "", "Discover", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Carolina", "NC", "USA", "United States", "North Carolina", "Hurricanes", "", "Central", "PNC Arena", "Carolina", "", "AHL:Chicago Wolves");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Chicago", "IL", "USA", "United States", "Illinois", "Blackhawks", "", "Central", "United Center", "Chicago", "", "AHL:Rockford IceHogs");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Columbus", "OH", "USA", "United States", "Ohio", "Blue Jackets", "", "Central", "Nationwide Arena", "Columbus", "", "AHL:Cleveland Monsters");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Dallas", "TX", "USA", "United States", "Texas", "Stars", "", "Central", "American Airlines Center", "Dallas", "", "AHL:Texas Stars");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Detroit", "MI", "USA", "United States", "Michigan", "Red Wings", "", "Central", "Little Caesars Arena", "Detroit", "", "AHL:Grand Rapids Griffins");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Sunrise", "FL", "USA", "United States", "Florida", "Panthers", "", "Central", "BB&T Center", "Florida", "", "AHL:Syracuse Crunch");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Nashville", "TN", "USA", "United States", "Tennessee", "Predators", "", "Central", "Bridgestone Arena", "Nashville", "", "AHL:Chicago Wolves");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Tampa Bay", "FL", "USA", "United States", "Florida", "Lightning", "", "Central", "Amalie Arena", "Tampa Bay", "", "AHL:Syracuse Crunch");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "NHL", "West", "", "Honda", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Anaheim", "CA", "USA", "United States", "California", "Ducks", "", "West", "Honda Center", "Anaheim", "", "AHL:San Diego Gulls");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Glendale", "AZ", "USA", "United States", "Arizona", "Coyotes", "", "West", "Gila River Arena", "Arizona", "", "AHL:Tucson Roadrunners");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Denver", "CO", "USA", "United States", "Colorado", "Avalanche", "", "West", "Ball Arena", "Colorado", "", "AHL:Colorado Eagles");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Los Angeles", "CA", "USA", "United States", "California", "Kings", "", "West", "Staples Center", "Los Angeles", "", "AHL:Ontario Reign");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "St. Paul", "MN", "USA", "United States", "Minnesota", "Wild", "", "West", "Xcel Energy Center", "Minnesota", "", "AHL:Iowa Wild");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "St. Louis", "MO", "USA", "United States", "Missouri", "Blues", "", "West", "Enterprise Center", "St. Louis", "", "AHL:Utica Comets");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "San Jose", "CA", "USA", "United States", "California", "Sharks", "", "West", "SAP Center", "San Jose", "", "AHL:San Jose Barracuda");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Paradise", "NV", "USA", "United States", "Nevada", "Golden Knights", "", "West", "T-Mobile Arena", "Vegas", "", "AHL:Henderson Silver Knights");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "NHL", "East", "", "Massmutual", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Boston", "MA", "USA", "United States", "Massachusetts", "Bruins", "", "East", "TD Garden", "Boston", "", "AHL:Providence Bruins");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Buffalo", "NY", "USA", "United States", "New York", "Sabres", "", "East", "KeyBank Center", "Buffalo", "", "AHL:Rochester Americans");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "New Jersey", "NJ", "USA", "United States", "New Jersey", "Devils", "", "East", "Prudential Center", "New Jersey", "", "AHL:Binghamton Devils");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Uniondale", "NY", "USA", "United States", "New York", "Islanders", "", "East", "Nassau Coliseum", "New York", "", "AHL:Bridgeport Sound Tigers");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "New York City", "NY", "USA", "United States", "New York", "Rangers", "", "East", "Madison Square Garden", "New York", "", "AHL:Hartford Wolf Pack");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Philadelphia", "PA", "USA", "United States", "Pennsylvania", "Flyers", "", "East", "Wells Fargo Center", "Philadelphia", "", "AHL:Lehigh Valley Phantoms");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Pittsburgh", "PA", "USA", "United States", "Pennsylvania", "Penguins", "", "East", "PPG Paints Arena", "Pittsburgh", "", "AHL:Wilkes-Barre/Scranton Penguins");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Washington", "DC", "USA", "United States", "District of Columbia", "Capitals", "", "East", "Capital One Arena", "Washington", "", "AHL:Hershey Bears");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "NHL", "North", "", "Scotia", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Calgary", "AB", "CAN", "Canada", "Alberta", "Flames", "", "North", "Scotiabank Saddledome", "Calgary", "", "AHL:Stockton Heat");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Edmonton", "AB", "CAN", "Canada", "Alberta", "Oilers", "", "North", "Rogers Place", "Edmonton", "", "AHL:Bakersfield Condors");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Montreal", "QC", "CAN", "Canada", "Quebec", "Canadiens", "", "North", "Bell Centre", "Montreal", "", "AHL:Laval Rocket");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Ottawa", "ON", "CAN", "Canada", "Ontario", "Senators", "", "North", "Canadian Tire Centre", "Ottawa", "", "AHL:Belleville Senators");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Toronto", "ON", "CAN", "Canada", "Ontario", "Maple Leafs", "", "North", "Scotiabank Arena", "Toronto", "", "AHL:Toronto Marlies");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Vancouver", "BC", "CAN", "Canada", "British Columbia", "Canucks", "", "North", "Rogers Arena", "Vancouver", "", "AHL:Utica Comets");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Winnipeg", "MB", "CAN", "Canada", "Manitoba", "Jets", "", "North", "Bell MTS Place", "Winnipeg", "", "AHL:Manitoba Moose");
hockeyarray = libhockeydata.AddHockeyLeagueToArray(hockeyarray, "AHL", "American Hockey League", "USA", "United States", "20210205", "Division=4", "ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", False, True);
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "AHL", "");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "AHL", "Atlantic", "", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Bridgeport", "CT", "USA", "United States", "Connecticut", "Sound Tigers", "", "Atlantic", "Webster Bank Arena", "Bridgeport", "", "NHL:New York Islanders");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Hartford", "CT", "USA", "United States", "Connecticut", "Wolf Pack", "", "Atlantic", "XL Center", "Hartford", "", "NHL:New York Rangers");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Providence", "RI", "USA", "United States", "Rhode Island", "Bruins", "", "Atlantic", "Dunkin' Donuts Center", "Providence", "", "NHL:Boston Bruins");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "AHL", "North", "", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Newark", "NJ", "USA", "United States", "New Jersey", "Devils", "", "North", "Barnabas Health Hockey House", "Binghamton", "", "NHL:New Jersey Devils");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Hershey", "PA", "USA", "United States", "Pennsylvania", "Bears", "", "North", "Giant Center", "Hershey", "", "NHL:Washington Capitals");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Allentown", "PA", "USA", "United States", "Pennsylvania", "Phantoms", "", "North", "PPL Center", "Lehigh Valley", "", "NHL:Philadelphia Flyers");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Buffalo", "NY", "USA", "United States", "New York", "Americans", "", "North", "KeyBank Center", "Rochester", "", "NHL:Buffalo Sabres");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Syracuse", "NY", "USA", "United States", "New York", "Crunch", "", "North", "Oncenter War Memorial Arena", "Syracuse", "", "NHL:Tampa Bay Lightning;Florida Panthers");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Utica", "NY", "USA", "United States", "New York", "Comets", "", "North", "Adirondack Bank Center", "Utica", "", "NHL:Vancouver Canucks;St. Louis Blues");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Wilkes-Barre", "PA", "USA", "United States", "Pennsylvania", "Penguins", "", "North", "Mohegan Sun Arena", "Wilkes-Barre/Scranton", "", "NHL:Pittsburgh Penguins");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "AHL", "Canadian", "", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Ottawa", "ON", "CAN", "Canada", "Ontario", "Senators", "", "Canadian", "Canadian Tire Centre", "Belleville", "", "NHL:Ottawa Senators");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Montreal", "QC", "CAN", "Canada", "Quebec", "Rocket", "", "Canadian", "Bell Centre", "Laval", "", "NHL:Montreal Canadiens");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Winnipeg", "MB", "CAN", "Canada", "Manitoba", "Moose", "", "Canadian", "Bell MTS Iceplex", "Manitoba", "", "NHL:Winnipeg Jets");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Calgary", "AB", "CAN", "Canada", "Alberta", "Heat", "", "Canadian", "Scotiabank Saddledome", "Stockton", "", "NHL:Calgary Flames");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Toronto", "ON", "CAN", "Canada", "Ontario", "Marlies", "", "Canadian", "Scotiabank Arena", "Toronto", "", "NHL:Toronto Maple Leafs");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "AHL", "Central", "", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Rosemont", "IL", "USA", "United States", "Illinois", "Wolves", "", "Central", "Allstate Arena", "Chicago", "", "NHL:Carolina Hurricanes");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Cleveland", "OH", "USA", "United States", "Ohio", "Monsters", "", "Central", "Rocket Mortgage FieldHouse", "Lake Erie", "", "NHL:Columbus Blue Jackets");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Grand Rapids", "MI", "USA", "United States", "Michigan", "Griffins", "", "Central", "Van Andel Arena", "Grand Rapids", "", "NHL:Detroit Red Wings");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Des Moines", "IA", "USA", "United States", "Iowa", "Wild", "", "Central", "Wells Fargo Arena", "Iowa", "", "NHL:Minnesota Wild");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Rockford", "IL", "USA", "United States", "Illinois", "IceHogs", "", "Central", "BMO Harris Bank Center", "Rockford", "", "NHL:Chicago Blackhawks");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Cedar Park", "TX", "USA", "United States", "Texas", "Stars", "", "Central", "H-E-B Center", "Texas", "", "NHL:Dallas Stars");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "AHL", "Pacific", "", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Bakersfield", "CA", "USA", "United States", "California", "Condors", "", "Pacific", "Mechanics Bank Arena", "Bakersfield", "", "NHL:Edmonton Oilers");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Loveland", "CO", "USA", "United States", "Colorado", "Eagles", "", "Pacific", "Budweiser Events Center", "Colorado", "", "NHL:Colorado Avalanche");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Paradise", "NV", "USA", "United States", "Nevada", "Silver Knights", "", "Pacific", "Orleans Arena", "Henderson", "", "NHL:Vegas Golden Knights");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "El Segundo", "CA", "USA", "United States", "California", "Reign", "", "Pacific", "Toyota Sports Center", "Ontario", "", "NHL:Los Angeles Kings");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Irvine", "CA", "USA", "United States", "California", "Gulls", "", "Pacific", "Great Park Ice & FivePoint Arena", "San Diego", "", "NHL:Anaheim Ducks");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "San Jose", "CA", "USA", "United States", "California", "Barracuda", "", "Pacific", "SAP Center", "San Jose", "", "NHL:San Jose Sharks");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Tucson", "AZ", "USA", "United States", "Arizona", "Roadrunners", "", "Pacific", "Tucson Convention Center", "Tucson", "", "NHL:Arizona Coyotes");

libhockeydata.MakeHockeyDatabaseFromHockeyArray(hockeyarray, None, False, True, True);
