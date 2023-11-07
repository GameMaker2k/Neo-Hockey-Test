#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals;
import libhockeydata;

hockeyarray = libhockeydata.CreateHockeyArray("./php/data/hockey17-18.db3");
hockeyarray = libhockeydata.AddHockeyLeagueToArray(hockeyarray, "NHL", "National Hockey League", "USA", "United States", "20171004", "Division=3,Conference=2", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", True, True);
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "NHL", "Eastern");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "NHL", "Atlantic", "Eastern", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Boston", "MA", "USA", "United States", "Massachusetts", "Bruins", "Eastern", "Atlantic", "TD Garden", "Boston", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Buffalo", "NY", "USA", "United States", "New York", "Sabres", "Eastern", "Atlantic", "KeyBank Center", "Buffalo", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Detroit", "MI", "USA", "United States", "Michigan", "Red Wings", "Eastern", "Atlantic", "Little Caesars Arena", "Detroit", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Sunrise", "FL", "USA", "United States", "Florida", "Panthers", "Eastern", "Atlantic", "BB&T Center", "Florida", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Montreal", "QC", "CAN", "Canada", "Quebec", "Canadiens", "Eastern", "Atlantic", "Bell Centre", "Montreal", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Ottawa", "ON", "CAN", "Canada", "Ontario", "Senators", "Eastern", "Atlantic", "Canadian Tire Centre", "Ottawa", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Tampa Bay", "FL", "USA", "United States", "Florida", "Lightning", "Eastern", "Atlantic", "Amalie Arena", "Tampa Bay", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Toronto", "ON", "CAN", "Canada", "Ontario", "Maple Leafs", "Eastern", "Atlantic", "Air Canada Centre", "Toronto", "", "");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "NHL", "Metropolitan", "Eastern", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Carolina", "NC", "USA", "United States", "North Carolina", "Hurricanes", "Eastern", "Metropolitan", "PNC Arena", "Carolina", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Columbus", "OH", "USA", "United States", "Ohio", "Blue Jackets", "Eastern", "Metropolitan", "Nationwide Arena", "Columbus", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "New Jersey", "NJ", "USA", "United States", "New Jersey", "Devils", "Eastern", "Metropolitan", "Prudential Center", "New Jersey", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "New York City", "NY", "USA", "United States", "New York", "Islanders", "Eastern", "Metropolitan", "Barclays Center", "New York", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "New York City", "NY", "USA", "United States", "New York", "Rangers", "Eastern", "Metropolitan", "Madison Square Garden", "New York", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Philadelphia", "PA", "USA", "United States", "Pennsylvania", "Flyers", "Eastern", "Metropolitan", "Wells Fargo Center", "Philadelphia", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Pittsburgh", "PA", "USA", "United States", "Pennsylvania", "Penguins", "Eastern", "Metropolitan", "PPG Paints Arena", "Pittsburgh", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Washington", "DC", "USA", "United States", "District of Columbia", "Capitals", "Eastern", "Metropolitan", "Capital One Arena", "Washington", "", "");
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "NHL", "Western");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "NHL", "Central", "Western", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Chicago", "IL", "USA", "United States", "Illinois", "Blackhawks", "Western", "Central", "United Center", "Chicago", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Denver", "CO", "USA", "United States", "Colorado", "Avalanche", "Western", "Central", "Pepsi Center", "Colorado", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Dallas", "TX", "USA", "United States", "Texas", "Stars", "Western", "Central", "American Airlines Center", "Dallas", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "St. Paul", "MN", "USA", "United States", "Minnesota", "Wild", "Western", "Central", "Xcel Energy Center", "Minnesota", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Nashville", "TN", "USA", "United States", "Tennessee", "Predators", "Western", "Central", "Bridgestone Arena", "Nashville", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "St. Louis", "MO", "USA", "United States", "Missouri", "Blues", "Western", "Central", "Scottrade Center", "St. Louis", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Winnipeg", "MB", "CAN", "Canada", "Manitoba", "Jets", "Western", "Central", "Bell MTS Place", "Winnipeg", "", "");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "NHL", "Pacific", "Western", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Anaheim", "CA", "USA", "United States", "California", "Ducks", "Western", "Pacific", "Honda Center", "Anaheim", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Glendale", "AZ", "USA", "United States", "Arizona", "Coyotes", "Western", "Pacific", "Gila River Arena", "Arizona", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Calgary", "AB", "CAN", "Canada", "Alberta", "Flames", "Western", "Pacific", "Scotiabank Saddledome", "Calgary", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Edmonton", "AB", "CAN", "Canada", "Alberta", "Oilers", "Western", "Pacific", "Rogers Place", "Edmonton", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Los Angeles", "CA", "USA", "United States", "California", "Kings", "Western", "Pacific", "Staples Center", "Los Angeles", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "San Jose", "CA", "USA", "United States", "California", "Sharks", "Western", "Pacific", "SAP Center", "San Jose", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Vancouver", "BC", "CAN", "Canada", "British Columbia", "Canucks", "Western", "Pacific", "Rogers Arena", "Vancouver", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "NHL", "Paradise", "NV", "USA", "United States", "Nevada", "Golden Knights", "Western", "Pacific", "T-Mobile Arena", "Vegas", "", "");
hockeyarray = libhockeydata.AddHockeyArenaToArray(hockeyarray, "NHL", "Stockholm", "AB", "SWE", "Sweden", "Stockholm County", "Ericsson Globe");
hockeyarray = libhockeydata.AddHockeyArenaToArray(hockeyarray, "NHL", "Ottawa", "ON", "CAN", "Canada", "Ontario", "Lansdowne Park");
hockeyarray = libhockeydata.AddHockeyArenaToArray(hockeyarray, "NHL", "New York City", "NY", "USA", "United States", "New York", "Citi Field");
hockeyarray = libhockeydata.AddHockeyArenaToArray(hockeyarray, "NHL", "Annapolis", "MD", "USA", "United States", "Maryland", "United States Naval Academy");
hockeyarray = libhockeydata.AddHockeyLeagueToArray(hockeyarray, "AHL", "American Hockey League", "USA", "United States", "20171006", "Division=4", "ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", True, True);
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "AHL", "Eastern");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "AHL", "Atlantic", "Eastern", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Bridgeport", "CT", "USA", "United States", "Connecticut", "Sound Tigers", "Eastern", "Atlantic", "Webster Bank Arena", "Bridgeport", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Charlotte", "NC", "USA", "United States", "North Carolina", "Checkers", "Eastern", "Atlantic", "Bojangles' Coliseum", "Charlotte", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Hartford", "CT", "USA", "United States", "Connecticut", "Wolf Pack", "Eastern", "Atlantic", "XL Center", "Hartford", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Hershey", "PA", "USA", "United States", "Pennsylvania", "Bears", "Eastern", "Atlantic", "Giant Center", "Hershey", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Allentown", "PA", "USA", "United States", "Pennsylvania", "Phantoms", "Eastern", "Atlantic", "PPL Center", "Lehigh Valley", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Providence", "RI", "USA", "United States", "Rhode Island", "Bruins", "Eastern", "Atlantic", "Dunkin' Donuts Center", "Providence", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Springfield", "MA", "USA", "United States", "Massachusetts", "Thunderbirds", "Eastern", "Atlantic", "MassMutual Center", "Springfield", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Wilkes-Barre", "PA", "USA", "United States", "Pennsylvania", "Penguins", "Eastern", "Atlantic", "Mohegan Sun Arena", "Wilkes-Barre/Scranton", "", "");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "AHL", "North", "Eastern", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Belleville", "ON", "CAN", "Canada", "Ontario", "Senators", "Eastern", "North", "Yardmen Arena", "Belleville", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Binghamton", "NY", "USA", "United States", "New York", "Devils", "Eastern", "North", "Veterans Memorial Arena", "Binghamton", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Laval", "QC", "CAN", "Canada", "Quebec", "Rocket", "Eastern", "North", "Place Bell", "Laval", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Rochester", "NY", "USA", "United States", "New York", "Americans", "Eastern", "North", "Blue Cross Arena", "Rochester", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Syracuse", "NY", "USA", "United States", "New York", "Crunch", "Eastern", "North", "Oncenter War Memorial Arena", "Syracuse", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Toronto", "ON", "CAN", "Canada", "Ontario", "Marlies", "Eastern", "North", "Ricoh Coliseum", "Toronto", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Utica", "NY", "USA", "United States", "New York", "Comets", "Eastern", "North", "Adirondack Bank Center", "Utica", "", "");
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "AHL", "Western");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "AHL", "Central", "Western", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Rosemont", "IL", "USA", "United States", "Illinois", "Wolves", "Western", "Central", "Allstate Arena", "Chicago", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Cleveland", "OH", "USA", "United States", "Ohio", "Monsters", "Western", "Central", "Quicken Loans Arena", "Lake Erie", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Grand Rapids", "MI", "USA", "United States", "Michigan", "Griffins", "Western", "Central", "Van Andel Arena", "Grand Rapids", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Des Moines", "IA", "USA", "United States", "Iowa", "Wild", "Western", "Central", "Wells Fargo Arena", "Iowa", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Winnipeg", "MB", "CAN", "Canada", "Manitoba", "Moose", "Western", "Central", "Bell MTS Place", "Manitoba", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Milwaukee", "WI", "USA", "United States", "Wisconsin", "Admirals", "Western", "Central", "UW-Milwaukee Panther Arena", "Milwaukee", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Rockford", "IL", "USA", "United States", "Illinois", "IceHogs", "Western", "Central", "BMO Harris Bank Center", "Rockford", "", "");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "AHL", "Pacific", "Western", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Bakersfield", "CA", "USA", "United States", "California", "Condors", "Western", "Pacific", "Rabobank Arena", "Bakersfield", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Ontario", "CA", "USA", "United States", "California", "Reign", "Western", "Pacific", "Citizens Business Bank Arena", "Ontario", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "San Antonio", "TX", "USA", "United States", "Texas", "Rampage", "Western", "Pacific", "AT&T Center", "San Antonio", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "San Diego", "CA", "USA", "United States", "California", "Gulls", "Western", "Pacific", "Valley View Casino Center", "San Diego", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "San Jose", "CA", "USA", "United States", "California", "Barracuda", "Western", "Pacific", "SAP Center", "San Jose", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Stockton", "CA", "USA", "United States", "California", "Heat", "Western", "Pacific", "Stockton Arena", "Stockton", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Cedar Park", "TX", "USA", "United States", "Texas", "Stars", "Western", "Pacific", "H-E-B Center", "Texas", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "AHL", "Tucson", "AZ", "USA", "United States", "Arizona", "Roadrunners", "Western", "Pacific", "Tucson Convention Center", "Tucson", "", "");
hockeyarray = libhockeydata.AddHockeyArenaToArray(hockeyarray, "AHL", "Hershey", "PA", "USA", "United States", "Pennsylvania", "Hersheypark Stadium");
hockeyarray = libhockeydata.AddHockeyLeagueToArray(hockeyarray, "ECHL", "ECHL", "USA", "United States", "20171013", "Division=4", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", True, True);
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "ECHL", "Eastern");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "ECHL", "North", "Eastern", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Glens Falls", "NY", "USA", "United States", "New York", "Thunder", "Eastern", "North", "Cool Insuring Arena", "Adirondack", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Brampton", "ON", "CAN", "Canada", "Ontario", "Beast", "Eastern", "North", "Powerade Centre", "Brampton", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Manchester", "NH", "USA", "United States", "New Hampshire", "Monarchs", "Eastern", "North", "SNHU Arena", "Manchester", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Reading", "PA", "USA", "United States", "Pennsylvania", "Royals", "Eastern", "North", "Santander Arena", "Reading", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Wheeling", "WV", "USA", "United States", "West Virginia", "Nailers", "Eastern", "North", "WesBanco Arena", "Wheeling", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Worcester", "MA", "USA", "United States", "Massachusetts", "Railers", "Eastern", "North", "DCU Center", "Worcester", "", "");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "ECHL", "South", "Eastern", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Duluth", "GA", "USA", "United States", "Georgia", "Gladiators", "Eastern", "South", "Infinite Energy Arena", "Atlanta", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Estero", "FL", "USA", "United States", "Florida", "Everblades", "Eastern", "South", "Germain Arena", "Florida", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Greenville", "SC", "USA", "United States", "South Carolina", "Swamp Rabbits", "Eastern", "South", "Bon Secours Wellness Arena", "Greenville", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Jacksonville", "FL", "USA", "United States", "Florida", "Icemen", "Eastern", "South", "Jacksonville Veterans Memorial Arena", "Jacksonville", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Norfolk", "VA", "USA", "United States", "Virginia", "Admirals", "Eastern", "South", "Norfolk Scope", "Norfolk", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Orlando", "FL", "USA", "United States", "Florida", "Solar Bears", "Eastern", "South", "Amway Center", "Orlando", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "North Charleston", "SC", "USA", "United States", "South Carolina", "Stingrays", "Eastern", "South", "North Charleston Coliseum", "South Carolina", "", "");
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "ECHL", "Western");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "ECHL", "Central", "Western", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Cincinnati", "OH", "USA", "United States", "Ohio", "Cyclones", "Western", "Central", "US Bank Arena", "Cincinnati", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Fort Wayne", "IN", "USA", "United States", "Indiana", "Komets", "Western", "Central", "Allen County War Memorial Coliseum", "Fort Wayne", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Indianapolis", "IN", "USA", "United States", "Indiana", "Fuel", "Western", "Central", "Indiana Farmers Coliseum", "Indy", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Kalamazoo", "MI", "USA", "United States", "Michigan", "Wings", "Western", "Central", "Wings Event Center", "Kalamazoo", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Independence", "MO", "USA", "United States", "Missouri", "Mavericks", "Western", "Central", "Silverstein Eye Centers Arena", "Kansas City", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Moline", "IL", "USA", "United States", "Illinois", "Mallards", "Western", "Central", "TaxSlayer Center", "Quad City", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Toledo", "OH", "USA", "United States", "Ohio", "Walleye", "Western", "Central", "Huntington Center", "Toledo", "", "");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "ECHL", "Mountain", "Western", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Allen", "TX", "USA", "United States", "Texas", "Americans", "Western", "Mountain", "Allen Event Center", "Allen", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Loveland", "CO", "USA", "United States", "Colorado", "Eagles", "Western", "Mountain", "Budweiser Events Center", "Colorado", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Boise", "ID", "USA", "United States", "Idaho", "Steelheads", "Western", "Mountain", "CenturyLink Arena", "Idaho", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Rapid City", "SD", "USA", "United States", "South Dakota", "Rush", "Western", "Mountain", "Rushmore Plaza Civic Center", "Rapid City", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Tulsa", "OK", "USA", "United States", "Oklahoma", "Oilers", "Western", "Mountain", "BOK Center", "Tulsa", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "West Valley City", "UT", "USA", "United States", "Utah", "Grizzlies", "Western", "Mountain", "Maverik Center", "Utah", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "ECHL", "Wichita", "KS", "USA", "United States", "Kansas", "Thunder", "Western", "Mountain", "Intrust Bank Arena", "Wichita", "", "");
hockeyarray = libhockeydata.AddHockeyLeagueToArray(hockeyarray, "FHL", "Federal Hockey League", "USA", "United States", "20171027", "League=4", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", False, False);
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "FHL", "");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "FHL", "", "", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "FHL", "Winston-Salem", "NC", "USA", "United States", "North Carolina", "Thunderbirds", "", "", "Winston-Salem Fairgrounds Annex", "Carolina", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "FHL", "Cornwall", "ON", "CAN", "Canada", "Ontario", "Nationals", "", "", "Ed Lumley Arena", "Cornwall", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "FHL", "Danville", "IL", "USA", "United States", "Illinois", "Dashers", "", "", "David S. Palmer Arena", "Danville", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "FHL", "Kingsville", "ON", "CAN", "Canada", "Ontario", "Knights", "", "", "Kingsville Arena Complex", "North Shore", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "FHL", "Port Huron", "MI", "USA", "United States", "Michigan", "Prowlers", "", "", "McMorran Place", "Port Huron", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "FHL", "Watertown", "NY", "USA", "United States", "New York", "Wolves", "", "", "Watertown Municipal Arena", "Watertown", "", "");
hockeyarray = libhockeydata.AddHockeyLeagueToArray(hockeyarray, "SPHL", "Southern Professional Hockey League", "USA", "United States", "20171020", "League=8", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", False, False);
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "SPHL", "");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "SPHL", "", "", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "SPHL", "Pelham", "AL", "USA", "United States", "Alabama", "Bulls", "", "", "Pelham Civic Center", "Birmingham", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "SPHL", "Evansville", "IN", "USA", "United States", "Indiana", "Thunderbolts", "", "", "Ford Center", "Evansville", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "SPHL", "Fayetteville", "NC", "USA", "United States", "North Carolina", "Marksmen", "", "", "Crown Coliseum", "Fayetteville", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "SPHL", "Huntsville", "AL", "USA", "United States", "Alabama", "Havoc", "", "", "Von Braun Center", "Huntsville", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "SPHL", "Knoxville", "TN", "USA", "United States", "Tennessee", "Ice Bears", "", "", "Knoxville Civic Coliseum", "Knoxville", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "SPHL", "Macon", "GA", "USA", "United States", "Georgia", "Mayhem", "", "", "Macon Coliseum", "Macon", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "SPHL", "Southaven", "MS", "USA", "United States", "Mississippi", "RiverKings", "", "", "Landers Center", "Mississippi", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "SPHL", "Pensacola", "FL", "USA", "United States", "Florida", "Ice Flyers", "", "", "Pensacola Bay Center", "Pensacola", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "SPHL", "Peoria", "IL", "USA", "United States", "Illinois", "Rivermen", "", "", "Carver Arena", "Peoria", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "SPHL", "Roanoke", "VA", "USA", "United States", "Virginia", "Rail Yard Dawgs", "", "", "Berglund Center", "Roanoke", "", "");
hockeyarray = libhockeydata.AddHockeyLeagueToArray(hockeyarray, "KHL", "Kontinental Hockey League", "RUS", "Russia", "20170821", "Conference=8", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", True, True);
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "KHL", "Western");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "KHL", "Bobrov", "Western", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Minsk", "BY", "BLR", "Belarus", "Belarus", "Dinamo Minsk", "Western", "Bobrov", "Minsk-Arena", "", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Riga", "LV", "LVA", "Latvia", "Latvia", "Dinamo Riga", "Western", "Bobrov", "Arena Riga", "", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Helsinki", "FI", "FIN", "Finland", "Finland", "Jokerit Helsinki", "Western", "Bobrov", "Hartwall Arena", "", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Saint Petersburg", "RU", "RUS", "Russia", "Russia", "SKA Saint Petersburg", "Western", "Bobrov", "Ice Palace Saint Petersburg", "", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Bratislava", "SK", "SVK", "Slovakia", "Slovakia", "Slovan Bratislava", "Western", "Bobrov", "Ondrej Nepela Arena", "", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Moscow", "RU", "RUS", "Russia", "Russia", "Spartak Moscow", "Western", "Bobrov", "Luzhniki Minor Arena", "", "", "");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "KHL", "Tarasov", "Western", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Moscow", "RU", "RUS", "Russia", "Russia", "CSKA Moscow", "Western", "Tarasov", "CSKA Ice Palace", "", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Moscow", "RU", "RUS", "Russia", "Russia", "Dynamo Moscow", "Western", "Tarasov", "VTB Ice Palace", "", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Yaroslavl", "RU", "RUS", "Russia", "Russia", "Lokomotiv Yaroslavl", "Western", "Tarasov", "Arena 2000", "", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Cherepovets", "RU", "RUS", "Russia", "Russia", "Severstal Cherepovets", "Western", "Tarasov", "Ice Palace", "", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Sochi", "RU", "RUS", "Russia", "Russia", "HC Sochi", "Western", "Tarasov", "Bolshoy Ice Dome", "", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Nizhny Novgorod", "RU", "RUS", "Russia", "Russia", "Torpedo Nizhny Novgorod", "Western", "Tarasov", "Trade Union Sport Palace", "", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Podolsk", "RU", "RUS", "Russia", "Russia", "Vityaz Moscow Oblast", "Western", "Tarasov", "Vityaz Ice Palace", "", "", "");
hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, "KHL", "Eastern");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "KHL", "Kharlamov", "Eastern", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Kazan", "RU", "RUS", "Russia", "Russia", "Ak Bars Kazan", "Eastern", "Kharlamov", "TatNeft Arena", "", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Yekaterinburg", "RU", "RUS", "Russia", "Russia", "Avtomobilist Yekaterinburg", "Eastern", "Kharlamov", "KRK Uralets", "", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Tolyatti", "RU", "RUS", "Russia", "Russia", "Lada Togliatti", "Eastern", "Kharlamov", "Lada Arena a", "", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Magnitogorsk", "RU", "RUS", "Russia", "Russia", "Metallurg Magnitogorsk", "Eastern", "Kharlamov", "Arena Metallurg", "", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Nizhnekamsk", "RU", "RUS", "Russia", "Russia", "Neftekhimik Nizhnekamsk", "Eastern", "Kharlamov", "SCC Arena", "", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Chelyabinsk", "RU", "RUS", "Russia", "Russia", "Traktor Chelyabinsk", "Eastern", "Kharlamov", "Traktor Sport Palace", "", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Khanty-Mansiysk", "RU", "RUS", "Russia", "Russia", "Yugra Khanty-Mansiysk", "Eastern", "Kharlamov", "Arena Ugra", "", "", "");
hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, "KHL", "Chernyshev", "Eastern", "", "Division");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Vladivostok", "RU", "RUS", "Russia", "Russia", "Admiral Vladivostok", "Eastern", "Chernyshev", "Fetisov Arena", "", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Khabarovsk", "RU", "RUS", "Russia", "Russia", "Amur Khabarovsk", "Eastern", "Chernyshev", "Platinum Arena", "", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Omsk", "RU", "RUS", "Russia", "Russia", "Avangard Omsk", "Eastern", "Chernyshev", "Omsk Arena", "", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Astana", "RU", "RUS", "Kazakhstan", "Kazakhstan", "Barys Astana", "Eastern", "Chernyshev", "Barys Arena", "", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Ufa", "RU", "RUS", "Russia", "Russia", "Salavat Yulaev Ufa", "Eastern", "Chernyshev", "Ufa Arena", "", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Novosibirsk", "RU", "RUS", "Russia", "Russia", "Sibir Novosibirsk", "Eastern", "Chernyshev", "Ice Sports Palace Sibir", "", "", "");
hockeyarray = libhockeydata.AddHockeyTeamToArray(hockeyarray, "KHL", "Beijing", "CN", "CHN", "China", "China", "Red Star Kunlun", "Eastern", "Chernyshev", "Cadillac Arena", "", "", "");
hockeyarray = libhockeydata.AddHockeyArenaToArray(hockeyarray, "KHL", "Helsinki", "FI", "FIN", "Finland", "Finland", "Kaisaniemi Park");
hockeyarray = libhockeydata.AddHockeyArenaToArray(hockeyarray, "KHL", "Riga", "LV", "LVA", "Latvia", "Latvia", "Riga City Council Sports Complex");

libhockeydata.MakeHockeyDatabaseFromHockeyArray(hockeyarray, None, False, True, True);
