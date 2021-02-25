#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals;
import libhockeydata;

sqldatacon = libhockeydata.MakeHockeyDatabase("./php/data/hockey17-18.db3");
libhockeydata.MakeHockeyLeagueTable(sqldatacon);
libhockeydata.MakeHockeyTeamTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyLeague(sqldatacon, "NHL", "National Hockey League", "USA", "United States", "20171004", "Division=3,Conference=2", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.MakeHockeyConference(sqldatacon, "NHL", "Eastern", "", "Conference", True);
libhockeydata.MakeHockeyDivision(sqldatacon, "NHL", "Atlantic", "Eastern", "", "Division", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Boston", "MA", "USA", "United States", "Massachusetts", "Bruins", "Eastern", "Atlantic", "TD Garden", "Boston", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Buffalo", "NY", "USA", "United States", "New York", "Sabres", "Eastern", "Atlantic", "KeyBank Center", "Buffalo", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Detroit", "MI", "USA", "United States", "Michigan", "Red Wings", "Eastern", "Atlantic", "Little Caesars Arena", "Detroit", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Sunrise", "FL", "USA", "United States", "Florida", "Panthers", "Eastern", "Atlantic", "BB&T Center", "Florida", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Montreal", "QC", "CAN", "Canada", "Quebec", "Canadiens", "Eastern", "Atlantic", "Bell Centre", "Montreal", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Ottawa", "ON", "CAN", "Canada", "Ontario", "Senators", "Eastern", "Atlantic", "Canadian Tire Centre", "Ottawa", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Tampa Bay", "FL", "USA", "United States", "Florida", "Lightning", "Eastern", "Atlantic", "Amalie Arena", "Tampa Bay", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Toronto", "ON", "CAN", "Canada", "Ontario", "Maple Leafs", "Eastern", "Atlantic", "Air Canada Centre", "Toronto", "", "", True, True);
libhockeydata.MakeHockeyDivision(sqldatacon, "NHL", "Metropolitan", "Eastern", "", "Division", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Carolina", "NC", "USA", "United States", "North Carolina", "Hurricanes", "Eastern", "Metropolitan", "PNC Arena", "Carolina", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Columbus", "OH", "USA", "United States", "Ohio", "Blue Jackets", "Eastern", "Metropolitan", "Nationwide Arena", "Columbus", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "New Jersey", "NJ", "USA", "United States", "New Jersey", "Devils", "Eastern", "Metropolitan", "Prudential Center", "New Jersey", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "New York City", "NY", "USA", "United States", "New York", "Islanders", "Eastern", "Metropolitan", "Barclays Center", "New York", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "New York City", "NY", "USA", "United States", "New York", "Rangers", "Eastern", "Metropolitan", "Madison Square Garden", "New York", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Philadelphia", "PA", "USA", "United States", "Pennsylvania", "Flyers", "Eastern", "Metropolitan", "Wells Fargo Center", "Philadelphia", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Pittsburgh", "PA", "USA", "United States", "Pennsylvania", "Penguins", "Eastern", "Metropolitan", "PPG Paints Arena", "Pittsburgh", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Washington", "DC", "USA", "United States", "District of Columbia", "Capitals", "Eastern", "Metropolitan", "Capital One Arena", "Washington", "", "", True, True);
libhockeydata.MakeHockeyConference(sqldatacon, "NHL", "Western", "", "Conference", True);
libhockeydata.MakeHockeyDivision(sqldatacon, "NHL", "Central", "Western", "", "Division", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Chicago", "IL", "USA", "United States", "Illinois", "Blackhawks", "Western", "Central", "United Center", "Chicago", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Denver", "CO", "USA", "United States", "Colorado", "Avalanche", "Western", "Central", "Pepsi Center", "Colorado", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Dallas", "TX", "USA", "United States", "Texas", "Stars", "Western", "Central", "American Airlines Center", "Dallas", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "St. Paul", "MN", "USA", "United States", "Minnesota", "Wild", "Western", "Central", "Xcel Energy Center", "Minnesota", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Nashville", "TN", "USA", "United States", "Tennessee", "Predators", "Western", "Central", "Bridgestone Arena", "Nashville", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "St. Louis", "MO", "USA", "United States", "Missouri", "Blues", "Western", "Central", "Scottrade Center", "St. Louis", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Winnipeg", "MB", "CAN", "Canada", "Manitoba", "Jets", "Western", "Central", "Bell MTS Place", "Winnipeg", "", "", True, True);
libhockeydata.MakeHockeyDivision(sqldatacon, "NHL", "Pacific", "Western", "", "Division", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Anaheim", "CA", "USA", "United States", "California", "Ducks", "Western", "Pacific", "Honda Center", "Anaheim", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Glendale", "AZ", "USA", "United States", "Arizona", "Coyotes", "Western", "Pacific", "Gila River Arena", "Arizona", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Calgary", "AB", "CAN", "Canada", "Alberta", "Flames", "Western", "Pacific", "Scotiabank Saddledome", "Calgary", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Edmonton", "AB", "CAN", "Canada", "Alberta", "Oilers", "Western", "Pacific", "Rogers Place", "Edmonton", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Los Angeles", "CA", "USA", "United States", "California", "Kings", "Western", "Pacific", "Staples Center", "Los Angeles", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "San Jose", "CA", "USA", "United States", "California", "Sharks", "Western", "Pacific", "SAP Center", "San Jose", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Vancouver", "BC", "CAN", "Canada", "British Columbia", "Canucks", "Western", "Pacific", "Rogers Arena", "Vancouver", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "NHL", "20171004", "Paradise", "NV", "USA", "United States", "Nevada", "Golden Knights", "Western", "Pacific", "T-Mobile Arena", "Vegas", "", "", True, True);
libhockeydata.MakeHockeyArena(sqldatacon, "NHL", "Stockholm", "AB", "SWE", "Sweden", "Stockholm County", "Ericsson Globe");
libhockeydata.MakeHockeyArena(sqldatacon, "NHL", "Ottawa", "ON", "CAN", "Canada", "Ontario", "Lansdowne Park");
libhockeydata.MakeHockeyArena(sqldatacon, "NHL", "New York City", "NY", "USA", "United States", "New York", "Citi Field");
libhockeydata.MakeHockeyArena(sqldatacon, "NHL", "Annapolis", "MD", "USA", "United States", "Maryland", "United States Naval Academy");
libhockeydata.MakeHockeyTeamTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyLeague(sqldatacon, "AHL", "American Hockey League", "USA", "United States", "20171006", "Division=4", "ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.MakeHockeyConference(sqldatacon, "AHL", "Eastern", "", "Conference", True);
libhockeydata.MakeHockeyDivision(sqldatacon, "AHL", "Atlantic", "Eastern", "", "Division", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Bridgeport", "CT", "USA", "United States", "Connecticut", "Sound Tigers", "Eastern", "Atlantic", "Webster Bank Arena", "Bridgeport", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Charlotte", "NC", "USA", "United States", "North Carolina", "Checkers", "Eastern", "Atlantic", "Bojangles' Coliseum", "Charlotte", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Hartford", "CT", "USA", "United States", "Connecticut", "Wolf Pack", "Eastern", "Atlantic", "XL Center", "Hartford", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Hershey", "PA", "USA", "United States", "Pennsylvania", "Bears", "Eastern", "Atlantic", "Giant Center", "Hershey", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Allentown", "PA", "USA", "United States", "Pennsylvania", "Phantoms", "Eastern", "Atlantic", "PPL Center", "Lehigh Valley", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Providence", "RI", "USA", "United States", "Rhode Island", "Bruins", "Eastern", "Atlantic", "Dunkin' Donuts Center", "Providence", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Springfield", "MA", "USA", "United States", "Massachusetts", "Thunderbirds", "Eastern", "Atlantic", "MassMutual Center", "Springfield", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Wilkes-Barre", "PA", "USA", "United States", "Pennsylvania", "Penguins", "Eastern", "Atlantic", "Mohegan Sun Arena", "Wilkes-Barre/Scranton", "", "", True, True);
libhockeydata.MakeHockeyDivision(sqldatacon, "AHL", "North", "Eastern", "", "Division", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Belleville", "ON", "CAN", "Canada", "Ontario", "Senators", "Eastern", "North", "Yardmen Arena", "Belleville", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Binghamton", "NY", "USA", "United States", "New York", "Devils", "Eastern", "North", "Veterans Memorial Arena", "Binghamton", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Laval", "QC", "CAN", "Canada", "Quebec", "Rocket", "Eastern", "North", "Place Bell", "Laval", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Rochester", "NY", "USA", "United States", "New York", "Americans", "Eastern", "North", "Blue Cross Arena", "Rochester", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Syracuse", "NY", "USA", "United States", "New York", "Crunch", "Eastern", "North", "Oncenter War Memorial Arena", "Syracuse", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Toronto", "ON", "CAN", "Canada", "Ontario", "Marlies", "Eastern", "North", "Ricoh Coliseum", "Toronto", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Utica", "NY", "USA", "United States", "New York", "Comets", "Eastern", "North", "Adirondack Bank Center", "Utica", "", "", True, True);
libhockeydata.MakeHockeyConference(sqldatacon, "AHL", "Western", "", "Conference", True);
libhockeydata.MakeHockeyDivision(sqldatacon, "AHL", "Central", "Western", "", "Division", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Rosemont", "IL", "USA", "United States", "Illinois", "Wolves", "Western", "Central", "Allstate Arena", "Chicago", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Cleveland", "OH", "USA", "United States", "Ohio", "Monsters", "Western", "Central", "Quicken Loans Arena", "Lake Erie", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Grand Rapids", "MI", "USA", "United States", "Michigan", "Griffins", "Western", "Central", "Van Andel Arena", "Grand Rapids", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Des Moines", "IA", "USA", "United States", "Iowa", "Wild", "Western", "Central", "Wells Fargo Arena", "Iowa", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Winnipeg", "MB", "CAN", "Canada", "Manitoba", "Moose", "Western", "Central", "Bell MTS Place", "Manitoba", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Milwaukee", "WI", "USA", "United States", "Wisconsin", "Admirals", "Western", "Central", "UW-Milwaukee Panther Arena", "Milwaukee", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Rockford", "IL", "USA", "United States", "Illinois", "IceHogs", "Western", "Central", "BMO Harris Bank Center", "Rockford", "", "", True, True);
libhockeydata.MakeHockeyDivision(sqldatacon, "AHL", "Pacific", "Western", "", "Division", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Bakersfield", "CA", "USA", "United States", "California", "Condors", "Western", "Pacific", "Rabobank Arena", "Bakersfield", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Ontario", "CA", "USA", "United States", "California", "Reign", "Western", "Pacific", "Citizens Business Bank Arena", "Ontario", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "San Antonio", "TX", "USA", "United States", "Texas", "Rampage", "Western", "Pacific", "AT&T Center", "San Antonio", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "San Diego", "CA", "USA", "United States", "California", "Gulls", "Western", "Pacific", "Valley View Casino Center", "San Diego", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "San Jose", "CA", "USA", "United States", "California", "Barracuda", "Western", "Pacific", "SAP Center", "San Jose", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Stockton", "CA", "USA", "United States", "California", "Heat", "Western", "Pacific", "Stockton Arena", "Stockton", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Cedar Park", "TX", "USA", "United States", "Texas", "Stars", "Western", "Pacific", "H-E-B Center", "Texas", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "AHL", "20171006", "Tucson", "AZ", "USA", "United States", "Arizona", "Roadrunners", "Western", "Pacific", "Tucson Convention Center", "Tucson", "", "", True, True);
libhockeydata.MakeHockeyArena(sqldatacon, "AHL", "Hershey", "PA", "USA", "United States", "Pennsylvania", "Hersheypark Stadium");
libhockeydata.MakeHockeyTeamTable(sqldatacon, "ECHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "ECHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "ECHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "ECHL");
libhockeydata.MakeHockeyLeague(sqldatacon, "ECHL", "ECHL", "USA", "United States", "20171013", "Division=4", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.MakeHockeyConference(sqldatacon, "ECHL", "Eastern", "", "Conference", True);
libhockeydata.MakeHockeyDivision(sqldatacon, "ECHL", "North", "Eastern", "", "Division", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Glens Falls", "NY", "USA", "United States", "New York", "Thunder", "Eastern", "North", "Cool Insuring Arena", "Adirondack", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Brampton", "ON", "CAN", "Canada", "Ontario", "Beast", "Eastern", "North", "Powerade Centre", "Brampton", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Manchester", "NH", "USA", "United States", "New Hampshire", "Monarchs", "Eastern", "North", "SNHU Arena", "Manchester", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Reading", "PA", "USA", "United States", "Pennsylvania", "Royals", "Eastern", "North", "Santander Arena", "Reading", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Wheeling", "WV", "USA", "United States", "West Virginia", "Nailers", "Eastern", "North", "WesBanco Arena", "Wheeling", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Worcester", "MA", "USA", "United States", "Massachusetts", "Railers", "Eastern", "North", "DCU Center", "Worcester", "", "", True, True);
libhockeydata.MakeHockeyDivision(sqldatacon, "ECHL", "South", "Eastern", "", "Division", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Duluth", "GA", "USA", "United States", "Georgia", "Gladiators", "Eastern", "South", "Infinite Energy Arena", "Atlanta", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Estero", "FL", "USA", "United States", "Florida", "Everblades", "Eastern", "South", "Germain Arena", "Florida", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Greenville", "SC", "USA", "United States", "South Carolina", "Swamp Rabbits", "Eastern", "South", "Bon Secours Wellness Arena", "Greenville", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Jacksonville", "FL", "USA", "United States", "Florida", "Icemen", "Eastern", "South", "Jacksonville Veterans Memorial Arena", "Jacksonville", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Norfolk", "VA", "USA", "United States", "Virginia", "Admirals", "Eastern", "South", "Norfolk Scope", "Norfolk", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Orlando", "FL", "USA", "United States", "Florida", "Solar Bears", "Eastern", "South", "Amway Center", "Orlando", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "North Charleston", "SC", "USA", "United States", "South Carolina", "Stingrays", "Eastern", "South", "North Charleston Coliseum", "South Carolina", "", "", True, True);
libhockeydata.MakeHockeyConference(sqldatacon, "ECHL", "Western", "", "Conference", True);
libhockeydata.MakeHockeyDivision(sqldatacon, "ECHL", "Central", "Western", "", "Division", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Cincinnati", "OH", "USA", "United States", "Ohio", "Cyclones", "Western", "Central", "US Bank Arena", "Cincinnati", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Fort Wayne", "IN", "USA", "United States", "Indiana", "Komets", "Western", "Central", "Allen County War Memorial Coliseum", "Fort Wayne", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Indianapolis", "IN", "USA", "United States", "Indiana", "Fuel", "Western", "Central", "Indiana Farmers Coliseum", "Indy", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Kalamazoo", "MI", "USA", "United States", "Michigan", "Wings", "Western", "Central", "Wings Event Center", "Kalamazoo", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Independence", "MO", "USA", "United States", "Missouri", "Mavericks", "Western", "Central", "Silverstein Eye Centers Arena", "Kansas City", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Moline", "IL", "USA", "United States", "Illinois", "Mallards", "Western", "Central", "TaxSlayer Center", "Quad City", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Toledo", "OH", "USA", "United States", "Ohio", "Walleye", "Western", "Central", "Huntington Center", "Toledo", "", "", True, True);
libhockeydata.MakeHockeyDivision(sqldatacon, "ECHL", "Mountain", "Western", "", "Division", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Allen", "TX", "USA", "United States", "Texas", "Americans", "Western", "Mountain", "Allen Event Center", "Allen", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Loveland", "CO", "USA", "United States", "Colorado", "Eagles", "Western", "Mountain", "Budweiser Events Center", "Colorado", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Boise", "ID", "USA", "United States", "Idaho", "Steelheads", "Western", "Mountain", "CenturyLink Arena", "Idaho", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Rapid City", "SD", "USA", "United States", "South Dakota", "Rush", "Western", "Mountain", "Rushmore Plaza Civic Center", "Rapid City", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Tulsa", "OK", "USA", "United States", "Oklahoma", "Oilers", "Western", "Mountain", "BOK Center", "Tulsa", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "West Valley City", "UT", "USA", "United States", "Utah", "Grizzlies", "Western", "Mountain", "Maverik Center", "Utah", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "ECHL", "20171013", "Wichita", "KS", "USA", "United States", "Kansas", "Thunder", "Western", "Mountain", "Intrust Bank Arena", "Wichita", "", "", True, True);
libhockeydata.MakeHockeyTeamTable(sqldatacon, "FHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "FHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "FHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "FHL");
libhockeydata.MakeHockeyLeague(sqldatacon, "FHL", "Federal Hockey League", "USA", "United States", "20171027", "League=4", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.MakeHockeyConference(sqldatacon, "FHL", "", "", "Conference", False);
libhockeydata.MakeHockeyDivision(sqldatacon, "FHL", "", "", "", "Division", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "FHL", "20171027", "Winston-Salem", "NC", "USA", "United States", "North Carolina", "Thunderbirds", "", "", "Winston-Salem Fairgrounds Annex", "Carolina", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "FHL", "20171027", "Cornwall", "ON", "CAN", "Canada", "Ontario", "Nationals", "", "", "Ed Lumley Arena", "Cornwall", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "FHL", "20171027", "Danville", "IL", "USA", "United States", "Illinois", "Dashers", "", "", "David S. Palmer Arena", "Danville", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "FHL", "20171027", "Kingsville", "ON", "CAN", "Canada", "Ontario", "Knights", "", "", "Kingsville Arena Complex", "North Shore", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "FHL", "20171027", "Port Huron", "MI", "USA", "United States", "Michigan", "Prowlers", "", "", "McMorran Place", "Port Huron", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "FHL", "20171027", "Watertown", "NY", "USA", "United States", "New York", "Wolves", "", "", "Watertown Municipal Arena", "Watertown", "", "", False, False);
libhockeydata.MakeHockeyTeamTable(sqldatacon, "SPHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "SPHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "SPHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "SPHL");
libhockeydata.MakeHockeyLeague(sqldatacon, "SPHL", "Southern Professional Hockey League", "USA", "United States", "20171020", "League=8", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.MakeHockeyConference(sqldatacon, "SPHL", "", "", "Conference", False);
libhockeydata.MakeHockeyDivision(sqldatacon, "SPHL", "", "", "", "Division", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "SPHL", "20171020", "Pelham", "AL", "USA", "United States", "Alabama", "Bulls", "", "", "Pelham Civic Center", "Birmingham", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "SPHL", "20171020", "Evansville", "IN", "USA", "United States", "Indiana", "Thunderbolts", "", "", "Ford Center", "Evansville", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "SPHL", "20171020", "Fayetteville", "NC", "USA", "United States", "North Carolina", "Marksmen", "", "", "Crown Coliseum", "Fayetteville", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "SPHL", "20171020", "Huntsville", "AL", "USA", "United States", "Alabama", "Havoc", "", "", "Von Braun Center", "Huntsville", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "SPHL", "20171020", "Knoxville", "TN", "USA", "United States", "Tennessee", "Ice Bears", "", "", "Knoxville Civic Coliseum", "Knoxville", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "SPHL", "20171020", "Macon", "GA", "USA", "United States", "Georgia", "Mayhem", "", "", "Macon Coliseum", "Macon", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "SPHL", "20171020", "Southaven", "MS", "USA", "United States", "Mississippi", "RiverKings", "", "", "Landers Center", "Mississippi", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "SPHL", "20171020", "Pensacola", "FL", "USA", "United States", "Florida", "Ice Flyers", "", "", "Pensacola Bay Center", "Pensacola", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "SPHL", "20171020", "Peoria", "IL", "USA", "United States", "Illinois", "Rivermen", "", "", "Carver Arena", "Peoria", "", "", False, False);
libhockeydata.MakeHockeyTeam(sqldatacon, "SPHL", "20171020", "Roanoke", "VA", "USA", "United States", "Virginia", "Rail Yard Dawgs", "", "", "Berglund Center", "Roanoke", "", "", False, False);
libhockeydata.MakeHockeyTeamTable(sqldatacon, "KHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "KHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "KHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "KHL");
libhockeydata.MakeHockeyLeague(sqldatacon, "KHL", "Kontinental Hockey League", "RUS", "Russia", "20170821", "Conference=8", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC");
libhockeydata.MakeHockeyConference(sqldatacon, "KHL", "Western", "", "Conference", True);
libhockeydata.MakeHockeyDivision(sqldatacon, "KHL", "Bobrov", "Western", "", "Division", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Minsk", "BY", "BLR", "Belarus", "Belarus", "Dinamo Minsk", "Western", "Bobrov", "Minsk-Arena", "", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Riga", "LV", "LVA", "Latvia", "Latvia", "Dinamo Riga", "Western", "Bobrov", "Arena Riga", "", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Helsinki", "FI", "FIN", "Finland", "Finland", "Jokerit Helsinki", "Western", "Bobrov", "Hartwall Arena", "", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Saint Petersburg", "RU", "RUS", "Russia", "Russia", "SKA Saint Petersburg", "Western", "Bobrov", "Ice Palace Saint Petersburg", "", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Bratislava", "SK", "SVK", "Slovakia", "Slovakia", "Slovan Bratislava", "Western", "Bobrov", "Ondrej Nepela Arena", "", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Moscow", "RU", "RUS", "Russia", "Russia", "Spartak Moscow", "Western", "Bobrov", "Luzhniki Minor Arena", "", "", "", True, True);
libhockeydata.MakeHockeyDivision(sqldatacon, "KHL", "Tarasov", "Western", "", "Division", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Moscow", "RU", "RUS", "Russia", "Russia", "CSKA Moscow", "Western", "Tarasov", "CSKA Ice Palace", "", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Moscow", "RU", "RUS", "Russia", "Russia", "Dynamo Moscow", "Western", "Tarasov", "VTB Ice Palace", "", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Yaroslavl", "RU", "RUS", "Russia", "Russia", "Lokomotiv Yaroslavl", "Western", "Tarasov", "Arena 2000", "", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Cherepovets", "RU", "RUS", "Russia", "Russia", "Severstal Cherepovets", "Western", "Tarasov", "Ice Palace", "", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Sochi", "RU", "RUS", "Russia", "Russia", "HC Sochi", "Western", "Tarasov", "Bolshoy Ice Dome", "", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Nizhny Novgorod", "RU", "RUS", "Russia", "Russia", "Torpedo Nizhny Novgorod", "Western", "Tarasov", "Trade Union Sport Palace", "", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Podolsk", "RU", "RUS", "Russia", "Russia", "Vityaz Moscow Oblast", "Western", "Tarasov", "Vityaz Ice Palace", "", "", "", True, True);
libhockeydata.MakeHockeyConference(sqldatacon, "KHL", "Eastern", "", "Conference", True);
libhockeydata.MakeHockeyDivision(sqldatacon, "KHL", "Kharlamov", "Eastern", "", "Division", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Kazan", "RU", "RUS", "Russia", "Russia", "Ak Bars Kazan", "Eastern", "Kharlamov", "TatNeft Arena", "", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Yekaterinburg", "RU", "RUS", "Russia", "Russia", "Avtomobilist Yekaterinburg", "Eastern", "Kharlamov", "KRK Uralets", "", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Tolyatti", "RU", "RUS", "Russia", "Russia", "Lada Togliatti", "Eastern", "Kharlamov", "Lada Arena a", "", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Magnitogorsk", "RU", "RUS", "Russia", "Russia", "Metallurg Magnitogorsk", "Eastern", "Kharlamov", "Arena Metallurg", "", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Nizhnekamsk", "RU", "RUS", "Russia", "Russia", "Neftekhimik Nizhnekamsk", "Eastern", "Kharlamov", "SCC Arena", "", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Chelyabinsk", "RU", "RUS", "Russia", "Russia", "Traktor Chelyabinsk", "Eastern", "Kharlamov", "Traktor Sport Palace", "", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Khanty-Mansiysk", "RU", "RUS", "Russia", "Russia", "Yugra Khanty-Mansiysk", "Eastern", "Kharlamov", "Arena Ugra", "", "", "", True, True);
libhockeydata.MakeHockeyDivision(sqldatacon, "KHL", "Chernyshev", "Eastern", "", "Division", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Vladivostok", "RU", "RUS", "Russia", "Russia", "Admiral Vladivostok", "Eastern", "Chernyshev", "Fetisov Arena", "", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Khabarovsk", "RU", "RUS", "Russia", "Russia", "Amur Khabarovsk", "Eastern", "Chernyshev", "Platinum Arena", "", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Omsk", "RU", "RUS", "Russia", "Russia", "Avangard Omsk", "Eastern", "Chernyshev", "Omsk Arena", "", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Astana", "RU", "RUS", "Kazakhstan", "Kazakhstan", "Barys Astana", "Eastern", "Chernyshev", "Barys Arena", "", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Ufa", "RU", "RUS", "Russia", "Russia", "Salavat Yulaev Ufa", "Eastern", "Chernyshev", "Ufa Arena", "", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Novosibirsk", "RU", "RUS", "Russia", "Russia", "Sibir Novosibirsk", "Eastern", "Chernyshev", "Ice Sports Palace Sibir", "", "", "", True, True);
libhockeydata.MakeHockeyTeam(sqldatacon, "KHL", "20170821", "Beijing", "CN", "CHN", "China", "China", "Red Star Kunlun", "Eastern", "Chernyshev", "Cadillac Arena", "", "", "", True, True);
libhockeydata.MakeHockeyArena(sqldatacon, "KHL", "Helsinki", "FI", "FIN", "Finland", "Finland", "Kaisaniemi Park");
libhockeydata.MakeHockeyArena(sqldatacon, "KHL", "Riga", "LV", "LVA", "Latvia", "Latvia", "Riga City Council Sports Complex");

libhockeydata.CloseHockeyDatabase(sqldatacon);
