#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals;
import libhockeydata;

sqldatacon = libhockeydata.MakeHockeyDatabase("./hockey17-18.db3");
libhockeydata.MakeHockeyLeagueTable(sqldatacon);
libhockeydata.MakeHockeyTeamTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "NHL");
libhockeydata.MakeHockeyLeagues(sqldatacon, "NHL", "National Hockey League", "USA", "United States");
libhockeydata.MakeHockeyConferences(sqldatacon, "NHL", "Eastern", True);
libhockeydata.MakeHockeyDivisions(sqldatacon, "NHL", "Atlantic", "Eastern", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Boston", "MA", "USA", "United States", "Massachusetts", "Bruins", "Eastern", "Atlantic", "TD Garden", "Boston", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Buffalo", "NY", "USA", "United States", "New York", "Sabres", "Eastern", "Atlantic", "KeyBank Center", "Buffalo", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Detroit", "MI", "USA", "United States", "Michigan", "Red Wings", "Eastern", "Atlantic", "Little Caesars Arena", "Detroit", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Sunrise", "FL", "USA", "United States", "Florida", "Panthers", "Eastern", "Atlantic", "BB&T Center", "Florida", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Montreal", "QC", "CAN", "Canada", "Quebec", "Canadiens", "Eastern", "Atlantic", "Bell Centre", "Montreal", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Ottawa", "ON", "CAN", "Canada", "Ontario", "Senators", "Eastern", "Atlantic", "Canadian Tire Centre", "Ottawa", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Tampa Bay", "FL", "USA", "United States", "Florida", "Lightning", "Eastern", "Atlantic", "Amalie Arena", "Tampa Bay", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Toronto", "ON", "CAN", "Canada", "Ontario", "Maple Leafs", "Eastern", "Atlantic", "Air Canada Centre", "Toronto", "", True, True);
libhockeydata.MakeHockeyDivisions(sqldatacon, "NHL", "Metropolitan", "Eastern", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Carolina", "NC", "USA", "United States", "North Carolina", "Hurricanes", "Eastern", "Metropolitan", "PNC Arena", "Carolina", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Columbus", "OH", "USA", "United States", "Ohio", "Blue Jackets", "Eastern", "Metropolitan", "Nationwide Arena", "Columbus", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "New Jersey", "NJ", "USA", "United States", "New Jersey", "Devils", "Eastern", "Metropolitan", "Prudential Center", "New Jersey", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "New York City", "NY", "USA", "United States", "New York", "Islanders", "Eastern", "Metropolitan", "Barclays Center", "New York", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "New York City", "NY", "USA", "United States", "New York", "Rangers", "Eastern", "Metropolitan", "Madison Square Garden", "New York", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Philadelphia", "PA", "USA", "United States", "Pennsylvania", "Flyers", "Eastern", "Metropolitan", "Wells Fargo Center", "Philadelphia", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Pittsburgh", "PA", "USA", "United States", "Pennsylvania", "Penguins", "Eastern", "Metropolitan", "PPG Paints Arena", "Pittsburgh", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Washington", "DC", "USA", "United States", "District of Columbia", "Capitals", "Eastern", "Metropolitan", "Capital One Arena", "Washington", "", True, True);
libhockeydata.MakeHockeyConferences(sqldatacon, "NHL", "Western", True);
libhockeydata.MakeHockeyDivisions(sqldatacon, "NHL", "Central", "Western", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Chicago", "IL", "USA", "United States", "Illinois", "Blackhawks", "Western", "Central", "United Center", "Chicago", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Denver", "CO", "USA", "United States", "Colorado", "Avalanche", "Western", "Central", "Pepsi Center", "Colorado", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Dallas", "TX", "USA", "United States", "Texas", "Stars", "Western", "Central", "American Airlines Center", "Dallas", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "St. Paul", "MN", "USA", "United States", "Minnesota", "Wild", "Western", "Central", "Xcel Energy Center", "Minnesota", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Nashville", "TN", "USA", "United States", "Tennessee", "Predators", "Western", "Central", "Bridgestone Arena", "Nashville", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "St. Louis", "MO", "USA", "United States", "Missouri", "Blues", "Western", "Central", "Scottrade Center", "St. Louis", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Winnipeg", "MB", "CAN", "Canada", "Manitoba", "Jets", "Western", "Central", "Bell MTS Place", "Winnipeg", "", True, True);
libhockeydata.MakeHockeyDivisions(sqldatacon, "NHL", "Pacific", "Western", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Anaheim", "CA", "USA", "United States", "California", "Ducks", "Western", "Pacific", "Honda Center", "Anaheim", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Glendale", "AZ", "USA", "United States", "Arizona", "Coyotes", "Western", "Pacific", "Gila River Arena", "Arizona", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Calgary", "AB", "CAN", "Canada", "Alberta", "Flames", "Western", "Pacific", "Scotiabank Saddledome", "Calgary", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Edmonton", "AB", "CAN", "Canada", "Alberta", "Oilers", "Western", "Pacific", "Rogers Place", "Edmonton", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Los Angeles", "CA", "USA", "United States", "California", "Kings", "Western", "Pacific", "Staples Center", "Los Angeles", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "San Jose", "CA", "USA", "United States", "California", "Sharks", "Western", "Pacific", "SAP Center", "San Jose", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Vancouver", "BC", "CAN", "Canada", "British Columbia", "Canucks", "Western", "Pacific", "Rogers Arena", "Vancouver", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "NHL", 20171001, "Paradise", "NV", "USA", "United States", "Nevada", "Golden Knights", "Western", "Pacific", "T-Mobile Arena", "Vegas", "", True, True);
libhockeydata.MakeHockeyArena(sqldatacon, "NHL", "Stockholm", "AB", "SWE", "Sweden", "Stockholm County", "Ericsson Globe");
libhockeydata.MakeHockeyArena(sqldatacon, "NHL", "Ottawa", "ON", "CAN", "Canada", "Ontario", "Lansdowne Park");
libhockeydata.MakeHockeyArena(sqldatacon, "NHL", "New York City", "NY", "USA", "United States", "New York", "Citi Field");
libhockeydata.MakeHockeyArena(sqldatacon, "NHL", "Annapolis", "MD", "USA", "United States", "Maryland", "United States Naval Academy");
libhockeydata.MakeHockeyLeagueTable(sqldatacon);
libhockeydata.MakeHockeyTeamTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "AHL");
libhockeydata.MakeHockeyLeagues(sqldatacon, "AHL", "American Hockey League", "USA", "United States");
libhockeydata.MakeHockeyConferences(sqldatacon, "AHL", "Eastern", True);
libhockeydata.MakeHockeyDivisions(sqldatacon, "AHL", "Atlantic", "Eastern", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Bridgeport", "CT", "USA", "United States", "Connecticut", "Sound Tigers", "Eastern", "Atlantic", "Webster Bank Arena", "Bridgeport", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Charlotte", "NC", "USA", "United States", "North Carolina", "Checkers", "Eastern", "Atlantic", "Bojangles' Coliseum", "Charlotte", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Hartford", "CT", "USA", "United States", "Connecticut", "Wolf Pack", "Eastern", "Atlantic", "XL Center", "Hartford", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Hershey", "PA", "USA", "United States", "Pennsylvania", "Bears", "Eastern", "Atlantic", "Giant Center", "Hershey", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Allentown", "PA", "USA", "United States", "Pennsylvania", "Phantoms", "Eastern", "Atlantic", "PPL Center", "Lehigh Valley", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Providence", "RI", "USA", "United States", "Rhode Island", "Bruins", "Eastern", "Atlantic", "Dunkin' Donuts Center", "Providence", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Springfield", "MA", "USA", "United States", "Massachusetts", "Thunderbirds", "Eastern", "Atlantic", "MassMutual Center", "Springfield", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Wilkes-Barre", "PA", "USA", "United States", "Pennsylvania", "Penguins", "Eastern", "Atlantic", "Mohegan Sun Arena", "Wilkes-Barre/Scranton", "", True, True);
libhockeydata.MakeHockeyDivisions(sqldatacon, "AHL", "North", "Eastern", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Belleville", "ON", "CAN", "Canada", "Ontario", "Senators", "Eastern", "North", "Yardmen Arena", "Belleville", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Binghamton", "NY", "USA", "United States", "New York", "Devils", "Eastern", "North", "Veterans Memorial Arena", "Binghamton", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Laval", "QC", "CAN", "Canada", "Quebec", "Rocket", "Eastern", "North", "Place Bell", "Laval", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Rochester", "NY", "USA", "United States", "New York", "Americans", "Eastern", "North", "Blue Cross Arena", "Rochester", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Syracuse", "NY", "USA", "United States", "New York", "Crunch", "Eastern", "North", "Oncenter War Memorial Arena", "Syracuse", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Toronto", "ON", "CAN", "Canada", "Ontario", "Marlies", "Eastern", "North", "Ricoh Coliseum", "Toronto", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Utica", "NY", "USA", "United States", "New York", "Comets", "Eastern", "North", "Adirondack Bank Center", "Utica", "", True, True);
libhockeydata.MakeHockeyConferences(sqldatacon, "AHL", "Western", True);
libhockeydata.MakeHockeyDivisions(sqldatacon, "AHL", "Central", "Western", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Rosemont", "IL", "USA", "United States", "Illinois", "Wolves", "Western", "Central", "Allstate Arena", "Chicago", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Cleveland", "OH", "USA", "United States", "Ohio", "Monsters", "Western", "Central", "Quicken Loans Arena", "Lake Erie", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Grand Rapids", "MI", "USA", "United States", "Michigan", "Griffins", "Western", "Central", "Van Andel Arena", "Grand Rapids", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Des Moines", "IA", "USA", "United States", "Iowa", "Wild", "Western", "Central", "Wells Fargo Arena", "Iowa", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Winnipeg", "MB", "CAN", "Canada", "Manitoba", "Moose", "Western", "Central", "Bell MTS Place", "Manitoba", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Milwaukee", "WI", "USA", "United States", "Wisconsin", "Admirals", "Western", "Central", "UW-Milwaukee Panther Arena", "Milwaukee", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Rockford", "IL", "USA", "United States", "Illinois", "IceHogs", "Western", "Central", "BMO Harris Bank Center", "Rockford", "", True, True);
libhockeydata.MakeHockeyDivisions(sqldatacon, "AHL", "Pacific", "Western", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Bakersfield", "CA", "USA", "United States", "California", "Condors", "Western", "Pacific", "Rabobank Arena", "Bakersfield", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Ontario", "CA", "USA", "United States", "California", "Reign", "Western", "Pacific", "Citizens Business Bank Arena", "Ontario", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "San Antonio", "TX", "USA", "United States", "Texas", "Rampage", "Western", "Pacific", "AT&T Center", "San Antonio", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "San Diego", "CA", "USA", "United States", "California", "Gulls", "Western", "Pacific", "Valley View Casino Center", "San Diego", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "San Jose", "CA", "USA", "United States", "California", "Barracuda", "Western", "Pacific", "SAP Center", "San Jose", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Stockton", "CA", "USA", "United States", "California", "Heat", "Western", "Pacific", "Stockton Arena", "Stockton", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Cedar Park", "TX", "USA", "United States", "Texas", "Stars", "Western", "Pacific", "H-E-B Center", "Texas", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "AHL", 20171001, "Tucson", "AZ", "USA", "United States", "Arizona", "Roadrunners", "Western", "Pacific", "Tucson Convention Center", "Tucson", "", True, True);
libhockeydata.MakeHockeyArena(sqldatacon, "AHL", "Hershey", "PA", "USA", "United States", "Pennsylvania", "Hersheypark Stadium");
libhockeydata.MakeHockeyLeagueTable(sqldatacon);
libhockeydata.MakeHockeyTeamTable(sqldatacon, "ECHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "ECHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "ECHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "ECHL");
libhockeydata.MakeHockeyLeagues(sqldatacon, "ECHL", "ECHL", "USA", "United States");
libhockeydata.MakeHockeyConferences(sqldatacon, "ECHL", "Eastern", True);
libhockeydata.MakeHockeyDivisions(sqldatacon, "ECHL", "North", "Eastern", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Glens Falls", "NY", "USA", "United States", "New York", "Thunder", "Eastern", "North", "Cool Insuring Arena", "Adirondack", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Brampton", "ON", "CAN", "Canada", "Ontario", "Beast", "Eastern", "North", "Powerade Centre", "Brampton", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Manchester", "NH", "USA", "United States", "New Hampshire", "Monarchs", "Eastern", "North", "SNHU Arena", "Manchester", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Reading", "PA", "USA", "United States", "Pennsylvania", "Royals", "Eastern", "North", "Santander Arena", "Reading", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Wheeling", "WV", "USA", "United States", "West Virginia", "Nailers", "Eastern", "North", "WesBanco Arena", "Wheeling", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Worcester", "MA", "USA", "United States", "Massachusetts", "Railers", "Eastern", "North", "DCU Center", "Worcester", "", True, True);
libhockeydata.MakeHockeyDivisions(sqldatacon, "ECHL", "South", "Eastern", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Duluth", "GA", "USA", "United States", "Georgia", "Gladiators", "Eastern", "South", "Infinite Energy Arena", "Atlanta", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Estero", "FL", "USA", "United States", "Florida", "Everblades", "Eastern", "South", "Germain Arena", "Florida", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Greenville", "SC", "USA", "United States", "South Carolina", "Swamp Rabbits", "Eastern", "South", "Bon Secours Wellness Arena", "Greenville", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Jacksonville", "FL", "USA", "United States", "Florida", "Icemen", "Eastern", "South", "Jacksonville Veterans Memorial Arena", "Jacksonville", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Norfolk", "VA", "USA", "United States", "Virginia", "Admirals", "Eastern", "South", "Norfolk Scope", "Norfolk", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Orlando", "FL", "USA", "United States", "Florida", "Solar Bears", "Eastern", "South", "Amway Center", "Orlando", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "North Charleston", "SC", "USA", "United States", "South Carolina", "Stingrays", "Eastern", "South", "North Charleston Coliseum", "South Carolina", "", True, True);
libhockeydata.MakeHockeyConferences(sqldatacon, "ECHL", "Western", True);
libhockeydata.MakeHockeyDivisions(sqldatacon, "ECHL", "Central", "Western", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Cincinnati", "OH", "USA", "United States", "Ohio", "Cyclones", "Western", "Central", "US Bank Arena", "Cincinnati", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Fort Wayne", "IN", "USA", "United States", "Indiana", "Komets", "Western", "Central", "Allen County War Memorial Coliseum", "Fort Wayne", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Indianapolis", "IN", "USA", "United States", "Indiana", "Fuel", "Western", "Central", "Indiana Farmers Coliseum", "Indy", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Kalamazoo", "MI", "USA", "United States", "Michigan", "Wings", "Western", "Central", "Wings Event Center", "Kalamazoo", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Independence", "MO", "USA", "United States", "Missouri", "Mavericks", "Western", "Central", "Silverstein Eye Centers Arena", "Kansas City", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Moline", "IL", "USA", "United States", "Illinois", "Mallards", "Western", "Central", "TaxSlayer Center", "Quad City", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Toledo", "OH", "USA", "United States", "Ohio", "Walleye", "Western", "Central", "Huntington Center", "Toledo", "", True, True);
libhockeydata.MakeHockeyDivisions(sqldatacon, "ECHL", "Mountain", "Western", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Allen", "TX", "USA", "United States", "Texas", "Americans", "Western", "Mountain", "Allen Event Center", "Allen", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Loveland", "CO", "USA", "United States", "Colorado", "Eagles", "Western", "Mountain", "Budweiser Events Center", "Colorado", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Boise", "ID", "USA", "United States", "Idaho", "Steelheads", "Western", "Mountain", "CenturyLink Arena", "Idaho", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Rapid City", "SD", "USA", "United States", "South Dakota", "Rush", "Western", "Mountain", "Rushmore Plaza Civic Center", "Rapid City", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Tulsa", "OK", "USA", "United States", "Oklahoma", "Oilers", "Western", "Mountain", "BOK Center", "Tulsa", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "West Valley City", "UT", "USA", "United States", "Utah", "Grizzlies", "Western", "Mountain", "Maverik Center", "Utah", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "ECHL", 20171001, "Wichita", "KS", "USA", "United States", "Kansas", "Thunder", "Western", "Mountain", "Intrust Bank Arena", "Wichita", "", True, True);
libhockeydata.MakeHockeyLeagueTable(sqldatacon);
libhockeydata.MakeHockeyTeamTable(sqldatacon, "FHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "FHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "FHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "FHL");
libhockeydata.MakeHockeyLeagues(sqldatacon, "FHL", "Federal Hockey League", "USA", "United States");
libhockeydata.MakeHockeyConferences(sqldatacon, "FHL", "", False);
libhockeydata.MakeHockeyDivisions(sqldatacon, "FHL", "", "", False, False);
libhockeydata.MakeHockeyTeams(sqldatacon, "FHL", 20171001, "Winston-Salem", "NC", "USA", "United States", "North Carolina", "Thunderbirds", "", "", "Winston-Salem Fairgrounds Annex", "Carolina", "", False, False);
libhockeydata.MakeHockeyTeams(sqldatacon, "FHL", 20171001, "Cornwall", "ON", "CAN", "Canada", "Ontario", "Nationals", "", "", "Ed Lumley Arena", "Cornwall", "", False, False);
libhockeydata.MakeHockeyTeams(sqldatacon, "FHL", 20171001, "Danville", "IL", "USA", "United States", "Illinois", "Dashers", "", "", "David S. Palmer Arena", "Danville", "", False, False);
libhockeydata.MakeHockeyTeams(sqldatacon, "FHL", 20171001, "Kingsville", "ON", "CAN", "Canada", "Ontario", "Knights", "", "", "Kingsville Arena Complex", "North Shore", "", False, False);
libhockeydata.MakeHockeyTeams(sqldatacon, "FHL", 20171001, "Port Huron", "MI", "USA", "United States", "Michigan", "Prowlers", "", "", "McMorran Place", "Port Huron", "", False, False);
libhockeydata.MakeHockeyTeams(sqldatacon, "FHL", 20171001, "Watertown", "NY", "USA", "United States", "New York", "Wolves", "", "", "Watertown Municipal Arena", "Watertown", "", False, False);
libhockeydata.MakeHockeyLeagueTable(sqldatacon);
libhockeydata.MakeHockeyTeamTable(sqldatacon, "SPHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "SPHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "SPHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "SPHL");
libhockeydata.MakeHockeyLeagues(sqldatacon, "SPHL", "Southern Professional Hockey League", "USA", "United States");
libhockeydata.MakeHockeyConferences(sqldatacon, "SPHL", "", False);
libhockeydata.MakeHockeyDivisions(sqldatacon, "SPHL", "", "", False, False);
libhockeydata.MakeHockeyTeams(sqldatacon, "SPHL", 20171001, "Pelham", "AL", "USA", "United States", "Alabama", "Bulls", "", "", "Pelham Civic Center", "Birmingham", "", False, False);
libhockeydata.MakeHockeyTeams(sqldatacon, "SPHL", 20171001, "Evansville", "IN", "USA", "United States", "Indiana", "Thunderbolts", "", "", "Ford Center", "Evansville", "", False, False);
libhockeydata.MakeHockeyTeams(sqldatacon, "SPHL", 20171001, "Fayetteville", "NC", "USA", "United States", "North Carolina", "Marksmen", "", "", "Crown Coliseum", "Fayetteville", "", False, False);
libhockeydata.MakeHockeyTeams(sqldatacon, "SPHL", 20171001, "Huntsville", "AL", "USA", "United States", "Alabama", "Havoc", "", "", "Von Braun Center", "Huntsville", "", False, False);
libhockeydata.MakeHockeyTeams(sqldatacon, "SPHL", 20171001, "Knoxville", "TN", "USA", "United States", "Tennessee", "Ice Bears", "", "", "Knoxville Civic Coliseum", "Knoxville", "", False, False);
libhockeydata.MakeHockeyTeams(sqldatacon, "SPHL", 20171001, "Macon", "GA", "USA", "United States", "Georgia", "Mayhem", "", "", "Macon Coliseum", "Macon", "", False, False);
libhockeydata.MakeHockeyTeams(sqldatacon, "SPHL", 20171001, "Southaven", "MS", "USA", "United States", "Mississippi", "RiverKings", "", "", "Landers Center", "Mississippi", "", False, False);
libhockeydata.MakeHockeyTeams(sqldatacon, "SPHL", 20171001, "Pensacola", "FL", "USA", "United States", "Florida", "Ice Flyers", "", "", "Pensacola Bay Center", "Pensacola", "", False, False);
libhockeydata.MakeHockeyTeams(sqldatacon, "SPHL", 20171001, "Peoria", "IL", "USA", "United States", "Illinois", "Rivermen", "", "", "Carver Arena", "Peoria", "", False, False);
libhockeydata.MakeHockeyTeams(sqldatacon, "SPHL", 20171001, "Roanoke", "VA", "USA", "United States", "Virginia", "Rail Yard Dawgs", "", "", "Berglund Center", "Roanoke", "", False, False);
libhockeydata.MakeHockeyLeagueTable(sqldatacon);
libhockeydata.MakeHockeyTeamTable(sqldatacon, "KHL");
libhockeydata.MakeHockeyConferenceTable(sqldatacon, "KHL");
libhockeydata.MakeHockeyGameTable(sqldatacon, "KHL");
libhockeydata.MakeHockeyDivisionTable(sqldatacon, "KHL");
libhockeydata.MakeHockeyLeagues(sqldatacon, "KHL", "Kontinental Hockey League", "RUS", "Russia");
libhockeydata.MakeHockeyConferences(sqldatacon, "KHL", "Western", True);
libhockeydata.MakeHockeyDivisions(sqldatacon, "KHL", "Bobrov", "Western", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Minsk", "BY", "BLR", "Belarus", "Belarus", "Dinamo Minsk", "Western", "Bobrov", "Minsk-Arena", "", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Riga", "LV", "LVA", "Latvia", "Latvia", "Dinamo Riga", "Western", "Bobrov", "Arena Riga", "", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Helsinki", "FI", "FIN", "Finland", "Finland", "Jokerit Helsinki", "Western", "Bobrov", "Hartwall Arena", "", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Saint Petersburg", "RU", "RUS", "Russia", "Russia", "SKA Saint Petersburg", "Western", "Bobrov", "Ice Palace Saint Petersburg", "", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Bratislava", "SK", "SVK", "Slovakia", "Slovakia", "Slovan Bratislava", "Western", "Bobrov", "Ondrej Nepela Arena", "", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Moscow", "RU", "RUS", "Russia", "Russia", "Spartak Moscow", "Western", "Bobrov", "Luzhniki Minor Arena", "", "", True, True);
libhockeydata.MakeHockeyDivisions(sqldatacon, "KHL", "Tarasov", "Western", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Moscow", "RU", "RUS", "Russia", "Russia", "CSKA Moscow", "Western", "Tarasov", "CSKA Ice Palace", "", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Moscow", "RU", "RUS", "Russia", "Russia", "Dynamo Moscow", "Western", "Tarasov", "VTB Ice Palace", "", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Yaroslavl", "RU", "RUS", "Russia", "Russia", "Lokomotiv Yaroslavl", "Western", "Tarasov", "Arena 2000", "", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Cherepovets", "RU", "RUS", "Russia", "Russia", "Severstal Cherepovets", "Western", "Tarasov", "Ice Palace", "", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Sochi", "RU", "RUS", "Russia", "Russia", "Sochi", "Western", "Tarasov", "Bolshoy Ice Dome", "", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Nizhny Novgorod", "RU", "RUS", "Russia", "Russia", "Torpedo Nizhny Novgorod", "Western", "Tarasov", "Trade Union Sport Palace", "", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Podolsk", "RU", "RUS", "Russia", "Russia", "Vityaz Moscow Oblast", "Western", "Tarasov", "Vityaz Ice Palace", "", "", True, True);
libhockeydata.MakeHockeyConferences(sqldatacon, "KHL", "Eastern", True);
libhockeydata.MakeHockeyDivisions(sqldatacon, "KHL", "Kharlamov", "Eastern", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Kazan", "RU", "RUS", "Russia", "Russia", "Ak Bars Kazan", "Eastern", "Kharlamov", "TatNeft Arena", "", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Yekaterinburg", "RU", "RUS", "Russia", "Russia", "Avtomobilist Yekaterinburg", "Eastern", "Kharlamov", "KRK Uralets", "", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Tolyatti", "RU", "RUS", "Russia", "Russia", "Lada Togliatti", "Eastern", "Kharlamov", "Lada Arena a", "", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Magnitogorsk", "RU", "RUS", "Russia", "Russia", "Metallurg Magnitogorsk", "Eastern", "Kharlamov", "Arena Metallurg", "", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Nizhnekamsk", "RU", "RUS", "Russia", "Russia", "Neftekhimik Nizhnekamsk", "Eastern", "Kharlamov", "SCC Arena", "", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Chelyabinsk", "RU", "RUS", "Russia", "Russia", "Traktor Chelyabinsk", "Eastern", "Kharlamov", "Traktor Sport Palace", "", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Khanty-Mansiysk", "RU", "RUS", "Russia", "Russia", "Yugra Khanty-Mansiysk", "Eastern", "Kharlamov", "Arena Ugra", "", "", True, True);
libhockeydata.MakeHockeyDivisions(sqldatacon, "KHL", "Chernyshev", "Eastern", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Vladivostok", "RU", "RUS", "Russia", "Russia", "Admiral Vladivostok", "Eastern", "Chernyshev", "Fetisov Arena", "", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Khabarovsk", "RU", "RUS", "Russia", "Russia", "Amur Khabarovsk", "Eastern", "Chernyshev", "Platinum Arena", "", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Omsk", "RU", "RUS", "Russia", "Russia", "Avangard Omsk", "Eastern", "Chernyshev", "Omsk Arena", "", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Astana", "RU", "RUS", "Kazakhstan", "Kazakhstan", "Barys Astana", "Eastern", "Chernyshev", "Barys Arena", "", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Ufa", "RU", "RUS", "Russia", "Russia", "Salavat Yulaev Ufa", "Eastern", "Chernyshev", "Ufa Arena", "", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Novosibirsk", "RU", "RUS", "Russia", "Russia", "Sibir Novosibirsk", "Eastern", "Chernyshev", "Ice Sports Palace Sibir", "", "", True, True);
libhockeydata.MakeHockeyTeams(sqldatacon, "KHL", 20171001, "Beijing", "CN", "CHN", "China", "China", "Red Star Kunlun", "Eastern", "Chernyshev", "Cadillac Arena", "", "", True, True);
libhockeydata.MakeHockeyArena(sqldatacon, "KHL", "Helsinki", "FI", "FIN", "Finland", "Finland", "Kaisaniemi Park");
libhockeydata.MakeHockeyArena(sqldatacon, "KHL", "Riga", "LV", "LVA", "Latvia", "Latvia", "Riga City Council Sports Complex");
libhockeydata.CloseHockeyDatabase(sqldatacon);
