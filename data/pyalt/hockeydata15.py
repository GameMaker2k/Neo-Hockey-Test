#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals;
import libhockeydata;

hockeyarray = libhockeydata.MakeHockeyArray("./php/data/hockey15-16.db3");
hockeyarray = hockeyarray.AddHockeyLeague("ECHL", "ECHL", "USA", "United States", "20151007", "Division=1,Conference=5", "ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", True, True);
hockeyarray = hockeyarray.AddHockeyConference("ECHL", "Eastern", "", "Conference");
hockeyarray = hockeyarray.AddHockeyDivision("ECHL", "East", "Eastern", "", "Division");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Elmira", "NY", "USA", "United States", "New York", "Jackals", "Eastern", "East", "First Arena", "Elmira", "", "AHL:Rochester Americans,NHL:Buffalo Sabres");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Reading", "PA", "USA", "United States", "Pennsylvania", "Royals", "Eastern", "East", "Santander Arena", "Reading", "", "AHL:Lehigh Valley Phantoms,NHL:Philadelphia Flyers");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Norfolk", "VA", "USA", "United States", "Virginia", "Admirals", "Eastern", "East", "Norfolk Scope", "Norfolk", "", "AHL:Bakersfield Condors,NHL:Edmonton Oilers");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Glens Falls", "NY", "USA", "United States", "New York", "Thunder", "Eastern", "East", "Glens Falls Civic Center", "Adirondack", "", "AHL:Stockton Heat,NHL:Calgary Flames");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Manchester", "NH", "USA", "United States", "New Hampshire", "Monarchs", "Eastern", "East", "Verizon Wireless Arena", "Manchester", "", "AHL:Ontario Reign,NHL:Los Angeles Kings");
hockeyarray = hockeyarray.AddHockeyDivision("ECHL", "North", "Eastern", "", "Division");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Kalamazoo", "MI", "USA", "United States", "Michigan", "Wings", "Eastern", "North", "Wings Event Center", "Kalamazoo", "", "AHL:Lake Erie Monsters,NHL:Columbus Blue Jackets");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Toledo", "OH", "USA", "United States", "Ohio", "Walleye", "Eastern", "North", "Huntington Center", "Toledo", "", "AHL:Grand Rapids Griffins,NHL:Detroit Red Wings");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Wheeling", "WV", "USA", "United States", "West Virginia", "Nailers", "Eastern", "North", "WesBanco Arena", "Wheeling", "", "AHL:Wilkes-Barre/Scranton Penguins,NHL:Pittsburgh Penguins");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Brampton", "ON", "CAN", "Canada", "Ontario", "Beast", "Eastern", "North", "Powerade Centre", "Brampton", "", "AHL:St. John's IceCaps,NHL:Montreal Canadiens");
hockeyarray = hockeyarray.AddHockeyDivision("ECHL", "South", "Eastern", "", "Division");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Duluth", "GA", "USA", "United States", "Georgia", "Gladiators", "Eastern", "South", "Infinite Energy Arena", "Atlanta", "", "AHL:Providence Bruins,NHL:Boston Bruins");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Greenville", "SC", "USA", "United States", "South Carolina", "Swamp Rabbits", "Eastern", "South", "Bon Secours Wellness Arena", "Greenville", "", "AHL:Hartford Wolf Pack,NHL:New York Rangers");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Estero", "FL", "USA", "United States", "Florida", "Everblades", "Eastern", "South", "Germain Arena", "Florida", "", "AHL:Charlotte Checkers,NHL:Carolina Hurricanes");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Orlando", "FL", "USA", "United States", "Florida", "Solar Bears", "Eastern", "South", "Amway Center", "Orlando", "", "AHL:Toronto Marlies,NHL:Toronto Maple Leafs");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "North Charleston", "SC", "USA", "United States", "South Carolina", "Stingrays", "Eastern", "South", "North Charleston Coliseum", "South Carolina", "", "AHL:Hershey Bears,NHL:Washington Capitals");
hockeyarray = hockeyarray.AddHockeyConference("ECHL", "Western", "", "Conference");
hockeyarray = hockeyarray.AddHockeyDivision("ECHL", "Midwest", "Western", "", "Division");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Moline", "IL", "USA", "United States", "Illinois", "Mallards", "Western", "Midwest", "iWireless Center", "Quad City", "", "AHL:Iowa Wild,NHL:Minnesota Wild");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Evansville", "IN", "USA", "United States", "Indiana", "IceMen", "Western", "Midwest", "Ford Center", "Evansville", "", "AHL:Binghamton Senators,NHL:Ottawa Senators");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Indianapolis", "IN", "USA", "United States", "Indiana", "Fuel", "Western", "Midwest", "Indiana Farmers Coliseum", "Indy", "", "AHL:Rockford IceHogs,NHL:Chicago Blackhawks");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Fort Wayne", "IN", "USA", "United States", "Indiana", "Komets", "Western", "Midwest", "Allen County War Memorial Coliseum", "Fort Wayne", "", "AHL:San Antonio Rampage,NHL:Colorado Avalanche");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Cincinnati", "OH", "USA", "United States", "Ohio", "Cyclones", "Western", "Midwest", "US Bank Arena", "Cincinnati", "", "AHL:Milwaukee Admirals,NHL:Nashville Predators");
hockeyarray = hockeyarray.AddHockeyDivision("ECHL", "Central", "Western", "", "Division");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Wichita", "KS", "USA", "United States", "Kansas", "Thunder", "Western", "Central", "Intrust Bank Arena", "Wichita", "", "AHL:None,NHL:None");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Allen", "TX", "USA", "United States", "Texas", "Americans", "Western", "Central", "Allen Event Center", "Allen", "", "AHL:San Jose Barracuda,NHL:San Jose Sharks");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Tulsa", "OK", "USA", "United States", "Oklahoma", "Oilers", "Western", "Central", "BOK Center", "Tulsa", "", "AHL:Manitoba Moose,NHL:Winnipeg Jets");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Independence", "MO", "USA", "United States", "Missouri", "Mavericks", "Western", "Central", "Silverstein Eye Centers Arena", "Missouri", "", "AHL:Bridgeport Sound Tigers,NHL:New York Islanders");
hockeyarray = hockeyarray.AddHockeyDivision("ECHL", "West", "Western", "", "Division");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Anchorage", "AK", "USA", "United States", "Alaska", "Aces", "Western", "West", "Sullivan Arena", "Alaska", "", "AHL:None,NHL:None");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Boise", "ID", "USA", "United States", "Idaho", "Steelheads", "Western", "West", "CenturyLink Arena", "Idaho", "", "AHL:Texas Stars,NHL:Dallas Stars");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "West Valley City", "UT", "USA", "United States", "Utah", "Grizzlies", "Western", "West", "Maverik Center", "Utah", "", "AHL:San Diego Gulls,NHL:Anaheim Ducks");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Loveland", "CO", "USA", "United States", "Colorado", "Eagles", "Western", "West", "Budweiser Events Center", "Colorado", "", "AHL:None,NHL:None");
hockeyarray = hockeyarray.AddHockeyTeam("ECHL", "Rapid City", "SD", "USA", "United States", "South Dakota", "Rush", "Western", "West", "Rushmore Plaza Civic Center", "Rapid City", "", "AHL:Springfield Falcons,NHL:Arizona Coyotes");
hockeyarray = hockeyarray.AddHockeyLeague("AHL", "American Hockey League", "USA", "United States", "20151009", "Division=4", "ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", True, True);
hockeyarray = hockeyarray.AddHockeyConference("AHL", "Eastern", "", "Conference");
hockeyarray = hockeyarray.AddHockeyDivision("AHL", "Atlantic", "Eastern", "", "Division");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Bridgeport", "CT", "USA", "United States", "Connecticut", "Sound Tigers", "Eastern", "Atlantic", "Webster Bank Arena", "Bridgeport", "", "ECHL:Missouri Mavericks,NHL:New York Islanders");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Hartford", "CT", "USA", "United States", "Connecticut", "Wolf Pack", "Eastern", "Atlantic", "XL Center", "Hartford", "", "ECHL:Greenville Swamp Rabbits,NHL:New York Rangers");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Hershey", "PA", "USA", "United States", "Pennsylvania", "Bears", "Eastern", "Atlantic", "Giant Center", "Hershey", "", "ECHL:South Carolina Stingrays,NHL:Washington Capitals");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Allentown", "PA", "USA", "United States", "Pennsylvania", "Phantoms", "Eastern", "Atlantic", "PPL Center", "Lehigh Valley", "", "ECHL:Reading Royals,NHL:Philadelphia Flyers");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Portland", "ME", "USA", "United States", "Maine", "Pirates", "Eastern", "Atlantic", "Cross Insurance Arena", "Portland", "", "ECHL:None,NHL:Florida Panthers");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Providence", "RI", "USA", "United States", "Rhode Island", "Bruins", "Eastern", "Atlantic", "Dunkin' Donuts Center", "Providence", "", "ECHL:Atlanta Gladiators,NHL:Boston Bruins");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Springfield", "MA", "USA", "United States", "Massachusetts", "Falcons", "Eastern", "Atlantic", "MassMutual Center", "Springfield", "", "ECHL:Rapid City Rush,NHL:Arizona Coyotes");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Wilkes-Barre", "PA", "USA", "United States", "Pennsylvania", "Penguins", "Eastern", "Atlantic", "Mohegan Sun Arena", "Wilkes-Barre/Scranton", "", "ECHL:Wheeling Nailers,NHL:Pittsburgh Penguins");
hockeyarray = hockeyarray.AddHockeyDivision("AHL", "North", "Eastern", "", "Division");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Albany", "NY", "USA", "United States", "New York", "Devils", "Eastern", "North", "Times Union Center", "Albany", "", "ECHL:None,NHL:New Jersey Devils");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Binghamton", "NY", "USA", "United States", "New York", "Senators", "Eastern", "North", "Floyd L. Maines Veterans Memorial Arena", "Binghamton", "", "ECHL:Evansville IceMen,NHL:Ottawa Senators");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Rochester", "NY", "USA", "United States", "New York", "Americans", "Eastern", "North", "Blue Cross Arena", "Rochester", "", "ECHL:Elmira Jackals,NHL:Buffalo Sabres");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "St. John's", "NL", "CAN", "Canada", "Newfoundland and Labrador", "IceCaps", "Eastern", "North", "Mile One Centre", "St. John's", "", "ECHL:Brampton Beast,NHL:Montreal Canadiens");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Syracuse", "NY", "USA", "United States", "New York", "Crunch", "Eastern", "North", "Oncenter War Memorial Arena", "Syracuse", "", "ECHL:None,NHL:Tampa Bay Lightning");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Toronto", "ON", "CAN", "Canada", "Ontario", "Marlies", "Eastern", "North", "Ricoh Coliseum", "Toronto", "", "ECHL:Orlando Solar Bears,NHL:Toronto Maple Leafs");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Utica", "NY", "USA", "United States", "New York", "Comets", "Eastern", "North", "Utica Memorial Auditorium", "Utica", "", "ECHL:None,NHL:Vancouver Canucks");
hockeyarray = hockeyarray.AddHockeyConference("AHL", "Western", "", "Conference");
hockeyarray = hockeyarray.AddHockeyDivision("AHL", "Central", "Western", "", "Division");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Charlotte", "NC", "USA", "United States", "North Carolina", "Checkers", "Western", "Central", "Bojangles Coliseum", "Charlotte", "", "ECHL:Florida Everblades,NHL:Carolina Hurricanes");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Rosemont", "IL", "USA", "United States", "Illinois", "Wolves", "Western", "Central", "Allstate Arena", "Chicago", "", "ECHL:None,NHL:St. Louis Blues");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Grand Rapids", "MI", "USA", "United States", "Michigan", "Griffins", "Western", "Central", "Van Andel Arena", "Grand Rapids", "", "ECHL:Toledo Walleye,NHL:Detroit Red Wings");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Des Moines", "IA", "USA", "United States", "Iowa", "Wild", "Western", "Central", "Wells Fargo Arena", "Iowa", "", "ECHL:Quad City Mallards,NHL:Minnesota Wild");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Cleveland", "OH", "USA", "United States", "Ohio", "Monsters", "Western", "Central", "Quicken Loans Arena", "Lake Erie", "", "ECHL:Kalamazoo Wings,NHL:Columbus Blue Jackets");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Winnipeg", "MB", "CAN", "Canada", "Manitoba", "Moose", "Western", "Central", "MTS Centre", "Manitoba", "", "ECHL:Tulsa Oilers,NHL:Winnipeg Jets");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Milwaukee", "WI", "USA", "United States", "Wisconsin", "Admirals", "Western", "Central", "BMO Harris Bradley Center", "Milwaukee", "", "ECHL:Cincinnati Cyclones,NHL:Nashville Predators");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Rockford", "IL", "USA", "United States", "Illinois", "IceHogs", "Western", "Central", "BMO Harris Bank Center", "Rockford", "", "ECHL:Indy Fuel,NHL:Chicago Blackhawks");
hockeyarray = hockeyarray.AddHockeyDivision("AHL", "Pacific", "Western", "", "Division");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Bakersfield", "CA", "USA", "United States", "California", "Condors", "Western", "Pacific", "Rabobank Arena", "Bakersfield", "", "ECHL:Norfolk Admirals,NHL:Edmonton Oilers");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Ontario", "CA", "USA", "United States", "California", "Reign", "Western", "Pacific", "Citizens Business Bank Arena", "Ontario", "", "ECHL:Manchester Monarchs,NHL:Los Angeles Kings");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "San Antonio", "TX", "USA", "United States", "Texas", "Rampage", "Western", "Pacific", "AT&T Center", "San Antonio", "", "ECHL:Fort Wayne Komets,NHL:Colorado Avalanche");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "San Diego", "CA", "USA", "United States", "California", "Gulls", "Western", "Pacific", "Valley View Casino Center", "San Diego", "", "ECHL:Utah Grizzlies,NHL:Anaheim Ducks");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "San Jose", "CA", "USA", "United States", "California", "Barracuda", "Western", "Pacific", "SAP Center", "San Jose", "", "ECHL:Allen Americans,NHL:San Jose Sharks");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Stockton", "CA", "USA", "United States", "California", "Heat", "Western", "Pacific", "Stockton Arena", "Stockton", "", "ECHL:Adirondack Thunder,NHL:Calgary Flames");
hockeyarray = hockeyarray.AddHockeyTeam("AHL", "Cedar Park", "TX", "USA", "United States", "Texas", "Stars", "Western", "Pacific", "Cedar Park Center", "Texas", "", "ECHL:Idaho Steelheads,NHL:Dallas Stars");
hockeyarray = hockeyarray.AddHockeyArena("AHL", "West Sacramento", "CA", "USA", "United States", "California", "Raley Field");
hockeyarray = hockeyarray.AddHockeyLeague("NHL", "National Hockey League", "USA", "United States", "20151007", "Division=3,Conference=2", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", True, True);
hockeyarray = hockeyarray.AddHockeyConference("NHL", "Eastern", "", "Conference");
hockeyarray = hockeyarray.AddHockeyDivision("NHL", "Atlantic", "Eastern", "", "Division");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Boston", "MA", "USA", "United States", "Massachusetts", "Bruins", "Eastern", "Atlantic", "TD Garden", "Boston", "", "ECHL:Atlanta Gladiators,AHL:Providence Bruins");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Buffalo", "NY", "USA", "United States", "New York", "Sabres", "Eastern", "Atlantic", "First Niagara Center", "Buffalo", "", "ECHL:Elmira Jackals,AHL:Rochester Americans");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Detroit", "MI", "USA", "United States", "Michigan", "Red Wings", "Eastern", "Atlantic", "Joe Louis Arena", "Detroit", "", "ECHL:Toledo Walleye,AHL:Grand Rapids Griffins");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Sunrise", "FL", "USA", "United States", "Florida", "Panthers", "Eastern", "Atlantic", "BB&T Center", "Florida", "", "ECHL:None,AHL:Portland Pirates");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Montreal", "QC", "CAN", "Canada", "Quebec", "Canadiens", "Eastern", "Atlantic", "Bell Centre", "Montreal", "", "ECHL:Brampton Beast,AHL:St. John's Icecaps");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Ottawa", "ON", "CAN", "Canada", "Ontario", "Senators", "Eastern", "Atlantic", "Canadian Tire Centre", "Ottawa", "", "ECHL:Evansville IceMen,AHL:Binghamton Senators");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Tampa Bay", "FL", "USA", "United States", "Florida", "Lightning", "Eastern", "Atlantic", "Amalie Arena", "Tampa Bay", "", "ECHL:None,AHL:Syracuse Crunch");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Toronto", "ON", "CAN", "Canada", "Ontario", "Maple Leafs", "Eastern", "Atlantic", "Air Canada Centre", "Toronto", "", "ECHL:Orlando Solar Bears,AHL:Toronto Marlies");
hockeyarray = hockeyarray.AddHockeyDivision("NHL", "Metropolitan", "Eastern", "", "Division");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Carolina", "NC", "USA", "United States", "North Carolina", "Hurricanes", "Eastern", "Metropolitan", "PNC Arena", "Carolina", "", "ECHL:Florida Everblades,AHL:Charlotte Checkers");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Columbus", "OH", "USA", "United States", "Ohio", "Blue Jackets", "Eastern", "Metropolitan", "Nationwide Arena", "Columbus", "", "ECHL:Kalamazoo Wings,AHL:Lake Erie Monsters");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "New Jersey", "NJ", "USA", "United States", "New Jersey", "Devils", "Eastern", "Metropolitan", "Prudential Center", "New Jersey", "", "ECHL:None,AHL:Albany Devils");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "New York City", "NY", "USA", "United States", "New York", "Islanders", "Eastern", "Metropolitan", "Barclays Center", "New York", "", "ECHL:Missouri Mavericks,AHL:Bridgeport Sound Tigers");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "New York City", "NY", "USA", "United States", "New York", "Rangers", "Eastern", "Metropolitan", "Madison Square Garden", "New York", "", "ECHL:Greenville Swamp Rabbits,AHL:Hartford Wolf Pack");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Philadelphia", "PA", "USA", "United States", "Pennsylvania", "Flyers", "Eastern", "Metropolitan", "Wells Fargo Center", "Philadelphia", "", "ECHL:Reading Royals,AHL:Lehigh Valley Phantoms");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Pittsburgh", "PA", "USA", "United States", "Pennsylvania", "Penguins", "Eastern", "Metropolitan", "Consol Energy Center", "Pittsburgh", "", "ECHL:Wheeling Nailers,AHL:Wilkes-Barre/Scranton Penguins");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Washington", "DC", "USA", "United States", "District of Columbia", "Capitals", "Eastern", "Metropolitan", "Verizon Center", "Washington", "", "ECHL:South Carolina Stingrays,AHL:Hershey Bears");
hockeyarray = hockeyarray.AddHockeyConference("NHL", "Western", "", "Conference");
hockeyarray = hockeyarray.AddHockeyDivision("NHL", "Central", "Western", "", "Division");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Chicago", "IL", "USA", "United States", "Illinois", "Blackhawks", "Western", "Central", "United Center", "Chicago", "", "ECHL:Indy Fuel,AHL:Rockford IceHogs");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Denver", "CO", "USA", "United States", "Colorado", "Avalanche", "Western", "Central", "Pepsi Center", "Colorado", "", "ECHL:Fort Wayne Komets,AHL:San Antonio Rampage");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Dallas", "TX", "USA", "United States", "Texas", "Stars", "Western", "Central", "American Airlines Center", "Dallas", "", "ECHL:Idaho Steelheads,AHL:Texas Stars");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "St. Paul", "MN", "USA", "United States", "Minnesota", "Wild", "Western", "Central", "Xcel Energy Center", "Minnesota", "", "ECHL:Quad City Mallards,AHL:Iowa Wild");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Nashville", "TN", "USA", "United States", "Tennessee", "Predators", "Western", "Central", "Bridgestone Arena", "Nashville", "", "ECHL:Cincinnati Cyclones,AHL:Milwaukee Admirals");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "St. Louis", "MO", "USA", "United States", "Missouri", "Blues", "Western", "Central", "Scottrade Center", "St. Louis", "", "ECHL:None,AHL:Chicago Wolves");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Winnipeg", "MB", "CAN", "Canada", "Manitoba", "Jets", "Western", "Central", "MTS Centre", "Winnipeg", "", "ECHL:Tulsa Oilers,AHL:Manitoba Moose");
hockeyarray = hockeyarray.AddHockeyDivision("NHL", "Pacific", "Western", "", "Division");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Anaheim", "CA", "USA", "United States", "California", "Ducks", "Western", "Pacific", "Honda Center", "Anaheim", "", "ECHL:Utah Grizzlies,AHL:San Diego Gulls");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Glendale", "AZ", "USA", "United States", "Arizona", "Coyotes", "Western", "Pacific", "Gila River Arena", "Arizona", "", "ECHL:Rapid City Rush,AHL:Springfield Falcons");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Calgary", "AB", "CAN", "Canada", "Alberta", "Flames", "Western", "Pacific", "Scotiabank Saddledome", "Calgary", "", "ECHL:Adirondack Thunder,AHL:Stockton Heat");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Edmonton", "AB", "CAN", "Canada", "Alberta", "Oilers", "Western", "Pacific", "Rexall Place", "Edmonton", "", "ECHL:Norfolk Admirals,AHL:Bakersfield Condors");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Los Angeles", "CA", "USA", "United States", "California", "Kings", "Western", "Pacific", "Staples Center", "Los Angeles", "", "ECHL:Manchester Monarchs,AHL:Ontario Reign");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "San Jose", "CA", "USA", "United States", "California", "Sharks", "Western", "Pacific", "SAP Center", "San Jose", "", "ECHL:Allen Americans,AHL:San Jose Barracuda");
hockeyarray = hockeyarray.AddHockeyTeam("NHL", "Vancouver", "BC", "CAN", "Canada", "British Columbia", "Canucks", "Western", "Pacific", "Rogers Arena", "Vancouver", "", "ECHL:None,AHL:Utica Comets");
hockeyarray = hockeyarray.AddHockeyArena("NHL", "Foxborough", "MA", "USA", "United States", "Massachusetts", "Gillette Stadium");
hockeyarray = hockeyarray.AddHockeyArena("NHL", "Minneapolis", "MN", "USA", "United States", "Minnesota", "TCF Bank Stadium");
hockeyarray = hockeyarray.AddHockeyArena("NHL", "Denver", "CO", "USA", "United States", "Colorado", "Coors Field");

hockeyarray.MakeHockeyDatabase(None, False, False, True, True);
