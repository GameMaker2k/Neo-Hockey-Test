-- PyHockeyStats SQL Dumper
-- version 0.0.3 RC 1
-- https://github.com/GameMaker2k/Neo-Hockey-Test
--
-- Generation Time: February 07, 2018 at 11:08 PM
-- SQLite Server version: 3.21.0
-- PySQLite version: 2.6.0
-- Python Version: 3.6.4

--
-- Database: ./hockey17-18.db3
--

-- --------------------------------------------------------

--
-- Table structure for table HockeyLeagues
--

CREATE TABLE HockeyLeagues (
  id INTEGER PRIMARY KEY,
  LeagueName TEXT,
  LeagueFullName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  NumberOfTeams INTEGER,
  NumberOfConferences INTEGER,
  NumberOfDivisions INTEGER
);

--
-- Dumping data for table HockeyLeagues
--

INSERT INTO HockeyLeagues (id, LeagueName, LeagueFullName, CountryName, FullCountryName, NumberOfTeams, NumberOfConferences, NumberOfDivisions) VALUES 
(1, "NHL", "National Hockey League", "USA", "United States", 31, 2, 4);
INSERT INTO HockeyLeagues (id, LeagueName, LeagueFullName, CountryName, FullCountryName, NumberOfTeams, NumberOfConferences, NumberOfDivisions) VALUES 
(2, "AHL", "American Hockey League", "USA", "United States", 30, 2, 4);
INSERT INTO HockeyLeagues (id, LeagueName, LeagueFullName, CountryName, FullCountryName, NumberOfTeams, NumberOfConferences, NumberOfDivisions) VALUES 
(3, "ECHL", "ECHL", "USA", "United States", 27, 2, 4);
INSERT INTO HockeyLeagues (id, LeagueName, LeagueFullName, CountryName, FullCountryName, NumberOfTeams, NumberOfConferences, NumberOfDivisions) VALUES 
(4, "FHL", "Federal Hockey League", "USA", "United States", 6, 0, 0);
INSERT INTO HockeyLeagues (id, LeagueName, LeagueFullName, CountryName, FullCountryName, NumberOfTeams, NumberOfConferences, NumberOfDivisions) VALUES 
(5, "SPHL", "Southern Professional Hockey League", "USA", "United States", 10, 0, 0);
INSERT INTO HockeyLeagues (id, LeagueName, LeagueFullName, CountryName, FullCountryName, NumberOfTeams, NumberOfConferences, NumberOfDivisions) VALUES 
(6, "KHL", "Kontinental Hockey League", "RUS", "Russia", 27, 2, 4);

-- --------------------------------------------------------

--
-- Table structure for table NHLConferences
--

CREATE TABLE NHLConferences (
  id INTEGER PRIMARY KEY,
  Conference TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  NumberOfTeams INTEGER,
  NumberOfDivisions INTEGER
);

--
-- Dumping data for table NHLConferences
--

INSERT INTO NHLConferences (id, Conference, LeagueName, LeagueFullName, NumberOfTeams, NumberOfDivisions) VALUES 
(1, "Eastern", "NHL", "National Hockey League", 16, 2);
INSERT INTO NHLConferences (id, Conference, LeagueName, LeagueFullName, NumberOfTeams, NumberOfDivisions) VALUES 
(2, "Western", "NHL", "National Hockey League", 15, 2);

-- --------------------------------------------------------

--
-- Table structure for table NHLDivisions
--

CREATE TABLE NHLDivisions (
  id INTEGER PRIMARY KEY,
  Division TEXT,
  Conference TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  NumberOfTeams INTEGER
);

--
-- Dumping data for table NHLDivisions
--

INSERT INTO NHLDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(1, "Atlantic", "Eastern", "NHL", "National Hockey League", 8);
INSERT INTO NHLDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(2, "Metropolitan", "Eastern", "NHL", "National Hockey League", 8);
INSERT INTO NHLDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(3, "Central", "Western", "NHL", "National Hockey League", 7);
INSERT INTO NHLDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(4, "Pacific", "Western", "NHL", "National Hockey League", 8);

-- --------------------------------------------------------

--
-- Table structure for table NHLArenas
--

CREATE TABLE NHLArenas (
  id INTEGER PRIMARY KEY,
  TeamID INTEGER,
  TeamName TEXT,
  TeamFullName TEXT,
  CityName TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GamesPlayed INTEGER,
  FOREIGN KEY(TeamID) REFERENCES NHLTeams(id)
);

--
-- Dumping data for table NHLArenas
--

INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(1, 1, "Bruins", "Boston Bruins", "Boston", "MA", "USA", "United States", "Boston, MA", "Massachusetts", "Boston, Massachusetts", "TD Garden", "TD Garden, Boston", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(2, 2, "Sabres", "Buffalo Sabres", "Buffalo", "NY", "USA", "United States", "Buffalo, NY", "New York", "Buffalo, New York", "KeyBank Center", "KeyBank Center, Buffalo", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(3, 3, "Red Wings", "Detroit Red Wings", "Detroit", "MI", "USA", "United States", "Detroit, MI", "Michigan", "Detroit, Michigan", "Little Caesars Arena", "Little Caesars Arena, Detroit", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(4, 4, "Panthers", "Florida Panthers", "Sunrise", "FL", "USA", "United States", "Sunrise, FL", "Florida", "Sunrise, Florida", "BB&T Center", "BB&T Center, Sunrise", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(5, 5, "Canadiens", "Montreal Canadiens", "Montreal", "QC", "CAN", "Canada", "Montreal, QC", "Quebec", "Montreal, Quebec", "Bell Centre", "Bell Centre, Montreal", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(6, 6, "Senators", "Ottawa Senators", "Ottawa", "ON", "CAN", "Canada", "Ottawa, ON", "Ontario", "Ottawa, Ontario", "Canadian Tire Centre", "Canadian Tire Centre, Ottawa", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(7, 7, "Lightning", "Tampa Bay Lightning", "Tampa Bay", "FL", "USA", "United States", "Tampa Bay, FL", "Florida", "Tampa Bay, Florida", "Amalie Arena", "Amalie Arena, Tampa Bay", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(8, 8, "Maple Leafs", "Toronto Maple Leafs", "Toronto", "ON", "CAN", "Canada", "Toronto, ON", "Ontario", "Toronto, Ontario", "Air Canada Centre", "Air Canada Centre, Toronto", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(9, 9, "Hurricanes", "Carolina Hurricanes", "Carolina", "NC", "USA", "United States", "Carolina, NC", "North Carolina", "Carolina, North Carolina", "PNC Arena", "PNC Arena, Carolina", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(10, 10, "Blue Jackets", "Columbus Blue Jackets", "Columbus", "OH", "USA", "United States", "Columbus, OH", "Ohio", "Columbus, Ohio", "Nationwide Arena", "Nationwide Arena, Columbus", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(11, 11, "Devils", "New Jersey Devils", "New Jersey", "NJ", "USA", "United States", "New Jersey, NJ", "New Jersey", "New Jersey, New Jersey", "Prudential Center", "Prudential Center, New Jersey", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(12, 12, "Islanders", "New York Islanders", "New York City", "NY", "USA", "United States", "New York City, NY", "New York", "New York City, New York", "Barclays Center", "Barclays Center, New York City", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(13, 13, "Rangers", "New York Rangers", "New York City", "NY", "USA", "United States", "New York City, NY", "New York", "New York City, New York", "Madison Square Garden", "Madison Square Garden, New York City", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(14, 14, "Flyers", "Philadelphia Flyers", "Philadelphia", "PA", "USA", "United States", "Philadelphia, PA", "Pennsylvania", "Philadelphia, Pennsylvania", "Wells Fargo Center", "Wells Fargo Center, Philadelphia", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(15, 15, "Penguins", "Pittsburgh Penguins", "Pittsburgh", "PA", "USA", "United States", "Pittsburgh, PA", "Pennsylvania", "Pittsburgh, Pennsylvania", "PPG Paints Arena", "PPG Paints Arena, Pittsburgh", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(16, 16, "Capitals", "Washington Capitals", "Washington", "DC", "USA", "United States", "Washington, DC", "District of Columbia", "Washington, District of Columbia", "Capital One Arena", "Capital One Arena, Washington", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(17, 17, "Blackhawks", "Chicago Blackhawks", "Chicago", "IL", "USA", "United States", "Chicago, IL", "Illinois", "Chicago, Illinois", "United Center", "United Center, Chicago", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(18, 18, "Avalanche", "Colorado Avalanche", "Denver", "CO", "USA", "United States", "Denver, CO", "Colorado", "Denver, Colorado", "Pepsi Center", "Pepsi Center, Denver", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(19, 19, "Stars", "Dallas Stars", "Dallas", "TX", "USA", "United States", "Dallas, TX", "Texas", "Dallas, Texas", "American Airlines Center", "American Airlines Center, Dallas", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(20, 20, "Wild", "Minnesota Wild", "St. Paul", "MN", "USA", "United States", "St. Paul, MN", "Minnesota", "St. Paul, Minnesota", "Xcel Energy Center", "Xcel Energy Center, St. Paul", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(21, 21, "Predators", "Nashville Predators", "Nashville", "TN", "USA", "United States", "Nashville, TN", "Tennessee", "Nashville, Tennessee", "Bridgestone Arena", "Bridgestone Arena, Nashville", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(22, 22, "Blues", "St. Louis Blues", "St. Louis", "MO", "USA", "United States", "St. Louis, MO", "Missouri", "St. Louis, Missouri", "Scottrade Center", "Scottrade Center, St. Louis", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(23, 23, "Jets", "Winnipeg Jets", "Winnipeg", "MB", "CAN", "Canada", "Winnipeg, MB", "Manitoba", "Winnipeg, Manitoba", "Bell MTS Place", "Bell MTS Place, Winnipeg", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(24, 24, "Ducks", "Anaheim Ducks", "Anaheim", "CA", "USA", "United States", "Anaheim, CA", "California", "Anaheim, California", "Honda Center", "Honda Center, Anaheim", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(25, 25, "Coyotes", "Arizona Coyotes", "Glendale", "AZ", "USA", "United States", "Glendale, AZ", "Arizona", "Glendale, Arizona", "Gila River Arena", "Gila River Arena, Glendale", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(26, 26, "Flames", "Calgary Flames", "Calgary", "AB", "CAN", "Canada", "Calgary, AB", "Alberta", "Calgary, Alberta", "Scotiabank Saddledome", "Scotiabank Saddledome, Calgary", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(27, 27, "Oilers", "Edmonton Oilers", "Edmonton", "AB", "CAN", "Canada", "Edmonton, AB", "Alberta", "Edmonton, Alberta", "Rogers Place", "Rogers Place, Edmonton", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(28, 28, "Kings", "Los Angeles Kings", "Los Angeles", "CA", "USA", "United States", "Los Angeles, CA", "California", "Los Angeles, California", "Staples Center", "Staples Center, Los Angeles", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(29, 29, "Sharks", "San Jose Sharks", "San Jose", "CA", "USA", "United States", "San Jose, CA", "California", "San Jose, California", "SAP Center", "SAP Center, San Jose", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(30, 30, "Canucks", "Vancouver Canucks", "Vancouver", "BC", "CAN", "Canada", "Vancouver, BC", "British Columbia", "Vancouver, British Columbia", "Rogers Arena", "Rogers Arena, Vancouver", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(31, 31, "Golden Knights", "Vegas Golden Knights", "Paradise", "NV", "USA", "United States", "Paradise, NV", "Nevada", "Paradise, Nevada", "T-Mobile Arena", "T-Mobile Arena, Paradise", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(32, 0, "", "", "Stockholm", "AB", "SWE", "Sweden", "Stockholm, AB", "Stockholm County", "Stockholm, Stockholm County", "Ericsson Globe", "Ericsson Globe, Stockholm", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(33, 0, "", "", "Ottawa", "ON", "CAN", "Canada", "Ottawa, ON", "Ontario", "Ottawa, Ontario", "Lansdowne Park", "Lansdowne Park, Ottawa", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(34, 0, "", "", "New York City", "NY", "USA", "United States", "New York City, NY", "New York", "New York City, New York", "Citi Field", "Citi Field, New York City", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(35, 0, "", "", "Annapolis", "MD", "USA", "United States", "Annapolis, MD", "Maryland", "Annapolis, Maryland", "United States Naval Academy", "United States Naval Academy, Annapolis", 0);

-- --------------------------------------------------------

--
-- Table structure for table NHLTeams
--

CREATE TABLE NHLTeams (
  id INTEGER PRIMARY KEY,
  Date INTEGER,
  FullName TEXT,
  CityName TEXT,
  TeamPrefix TEXT,
  TeamSuffix TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  TeamName TEXT,
  Conference TEXT,
  Division TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GamesPlayed INTEGER,
  GamesPlayedHome INTEGER,
  GamesPlayedAway INTEGER,
  Ties INTEGER,
  Wins INTEGER,
  OTWins INTEGER,
  SOWins INTEGER,
  OTSOWins INTEGER,
  TWins INTEGER,
  Losses INTEGER,
  OTLosses INTEGER,
  SOLosses INTEGER,
  OTSOLosses INTEGER,
  TLosses INTEGER,
  ROW INTEGER,
  ROT INTEGER,
  ShutoutWins INTEGER,
  ShutoutLosses INTEGER,
  HomeRecord TEXT,
  AwayRecord TEXT,
  Shootouts TEXT,
  GoalsFor INTEGER,
  GoalsAgainst INTEGER,
  GoalsDifference INTEGER,
  SOGFor INTEGER,
  SOGAgainst INTEGER,
  SOGDifference INTEGER,
  ShotsBlockedFor INTEGER,
  ShotsBlockedAgainst INTEGER,
  ShotsBlockedDifference INTEGER,
  PPGFor INTEGER,
  PPGAgainst INTEGER,
  PPGDifference INTEGER,
  SHGFor INTEGER,
  SHGAgainst INTEGER,
  SHGDifference INTEGER,
  PenaltiesFor INTEGER,
  PenaltiesAgainst INTEGER,
  PenaltiesDifference INTEGER,
  PIMFor INTEGER,
  PIMAgainst INTEGER,
  PIMDifference INTEGER,
  HITSFor INTEGER,
  HITSAgainst INTEGER,
  HITSDifference INTEGER,
  TakeAways INTEGER,
  GiveAways INTEGER,
  TAGADifference INTEGER,
  FaceoffWins INTEGER,
  FaceoffLosses INTEGER,
  FaceoffDifference INTEGER,
  Points INTEGER,
  PCT REAL,
  LastTen TEXT,
  Streak TEXT
);

--
-- Dumping data for table NHLTeams
--

INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(1, 20171001, "Boston Bruins", "Boston", "Boston", "", "MA", "USA", "United States", "Boston, MA", "Massachusetts", "Boston, Massachusetts", "Bruins", "Eastern", "Atlantic", "NHL", "National Hockey League", "TD Garden", "TD Garden, Boston", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(2, 20171001, "Buffalo Sabres", "Buffalo", "Buffalo", "", "NY", "USA", "United States", "Buffalo, NY", "New York", "Buffalo, New York", "Sabres", "Eastern", "Atlantic", "NHL", "National Hockey League", "KeyBank Center", "KeyBank Center, Buffalo", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(3, 20171001, "Detroit Red Wings", "Detroit", "Detroit", "", "MI", "USA", "United States", "Detroit, MI", "Michigan", "Detroit, Michigan", "Red Wings", "Eastern", "Atlantic", "NHL", "National Hockey League", "Little Caesars Arena", "Little Caesars Arena, Detroit", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(4, 20171001, "Florida Panthers", "Sunrise", "Florida", "", "FL", "USA", "United States", "Sunrise, FL", "Florida", "Sunrise, Florida", "Panthers", "Eastern", "Atlantic", "NHL", "National Hockey League", "BB&T Center", "BB&T Center, Sunrise", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(5, 20171001, "Montreal Canadiens", "Montreal", "Montreal", "", "QC", "CAN", "Canada", "Montreal, QC", "Quebec", "Montreal, Quebec", "Canadiens", "Eastern", "Atlantic", "NHL", "National Hockey League", "Bell Centre", "Bell Centre, Montreal", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(6, 20171001, "Ottawa Senators", "Ottawa", "Ottawa", "", "ON", "CAN", "Canada", "Ottawa, ON", "Ontario", "Ottawa, Ontario", "Senators", "Eastern", "Atlantic", "NHL", "National Hockey League", "Canadian Tire Centre", "Canadian Tire Centre, Ottawa", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(7, 20171001, "Tampa Bay Lightning", "Tampa Bay", "Tampa Bay", "", "FL", "USA", "United States", "Tampa Bay, FL", "Florida", "Tampa Bay, Florida", "Lightning", "Eastern", "Atlantic", "NHL", "National Hockey League", "Amalie Arena", "Amalie Arena, Tampa Bay", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(8, 20171001, "Toronto Maple Leafs", "Toronto", "Toronto", "", "ON", "CAN", "Canada", "Toronto, ON", "Ontario", "Toronto, Ontario", "Maple Leafs", "Eastern", "Atlantic", "NHL", "National Hockey League", "Air Canada Centre", "Air Canada Centre, Toronto", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(9, 20171001, "Carolina Hurricanes", "Carolina", "Carolina", "", "NC", "USA", "United States", "Carolina, NC", "North Carolina", "Carolina, North Carolina", "Hurricanes", "Eastern", "Metropolitan", "NHL", "National Hockey League", "PNC Arena", "PNC Arena, Carolina", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(10, 20171001, "Columbus Blue Jackets", "Columbus", "Columbus", "", "OH", "USA", "United States", "Columbus, OH", "Ohio", "Columbus, Ohio", "Blue Jackets", "Eastern", "Metropolitan", "NHL", "National Hockey League", "Nationwide Arena", "Nationwide Arena, Columbus", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(11, 20171001, "New Jersey Devils", "New Jersey", "New Jersey", "", "NJ", "USA", "United States", "New Jersey, NJ", "New Jersey", "New Jersey, New Jersey", "Devils", "Eastern", "Metropolitan", "NHL", "National Hockey League", "Prudential Center", "Prudential Center, New Jersey", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(12, 20171001, "New York Islanders", "New York City", "New York", "", "NY", "USA", "United States", "New York City, NY", "New York", "New York City, New York", "Islanders", "Eastern", "Metropolitan", "NHL", "National Hockey League", "Barclays Center", "Barclays Center, New York City", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(13, 20171001, "New York Rangers", "New York City", "New York", "", "NY", "USA", "United States", "New York City, NY", "New York", "New York City, New York", "Rangers", "Eastern", "Metropolitan", "NHL", "National Hockey League", "Madison Square Garden", "Madison Square Garden, New York City", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(14, 20171001, "Philadelphia Flyers", "Philadelphia", "Philadelphia", "", "PA", "USA", "United States", "Philadelphia, PA", "Pennsylvania", "Philadelphia, Pennsylvania", "Flyers", "Eastern", "Metropolitan", "NHL", "National Hockey League", "Wells Fargo Center", "Wells Fargo Center, Philadelphia", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(15, 20171001, "Pittsburgh Penguins", "Pittsburgh", "Pittsburgh", "", "PA", "USA", "United States", "Pittsburgh, PA", "Pennsylvania", "Pittsburgh, Pennsylvania", "Penguins", "Eastern", "Metropolitan", "NHL", "National Hockey League", "PPG Paints Arena", "PPG Paints Arena, Pittsburgh", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(16, 20171001, "Washington Capitals", "Washington", "Washington", "", "DC", "USA", "United States", "Washington, DC", "District of Columbia", "Washington, District of Columbia", "Capitals", "Eastern", "Metropolitan", "NHL", "National Hockey League", "Capital One Arena", "Capital One Arena, Washington", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(17, 20171001, "Chicago Blackhawks", "Chicago", "Chicago", "", "IL", "USA", "United States", "Chicago, IL", "Illinois", "Chicago, Illinois", "Blackhawks", "Western", "Central", "NHL", "National Hockey League", "United Center", "United Center, Chicago", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(18, 20171001, "Colorado Avalanche", "Denver", "Colorado", "", "CO", "USA", "United States", "Denver, CO", "Colorado", "Denver, Colorado", "Avalanche", "Western", "Central", "NHL", "National Hockey League", "Pepsi Center", "Pepsi Center, Denver", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(19, 20171001, "Dallas Stars", "Dallas", "Dallas", "", "TX", "USA", "United States", "Dallas, TX", "Texas", "Dallas, Texas", "Stars", "Western", "Central", "NHL", "National Hockey League", "American Airlines Center", "American Airlines Center, Dallas", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(20, 20171001, "Minnesota Wild", "St. Paul", "Minnesota", "", "MN", "USA", "United States", "St. Paul, MN", "Minnesota", "St. Paul, Minnesota", "Wild", "Western", "Central", "NHL", "National Hockey League", "Xcel Energy Center", "Xcel Energy Center, St. Paul", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(21, 20171001, "Nashville Predators", "Nashville", "Nashville", "", "TN", "USA", "United States", "Nashville, TN", "Tennessee", "Nashville, Tennessee", "Predators", "Western", "Central", "NHL", "National Hockey League", "Bridgestone Arena", "Bridgestone Arena, Nashville", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(22, 20171001, "St. Louis Blues", "St. Louis", "St. Louis", "", "MO", "USA", "United States", "St. Louis, MO", "Missouri", "St. Louis, Missouri", "Blues", "Western", "Central", "NHL", "National Hockey League", "Scottrade Center", "Scottrade Center, St. Louis", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(23, 20171001, "Winnipeg Jets", "Winnipeg", "Winnipeg", "", "MB", "CAN", "Canada", "Winnipeg, MB", "Manitoba", "Winnipeg, Manitoba", "Jets", "Western", "Central", "NHL", "National Hockey League", "Bell MTS Place", "Bell MTS Place, Winnipeg", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(24, 20171001, "Anaheim Ducks", "Anaheim", "Anaheim", "", "CA", "USA", "United States", "Anaheim, CA", "California", "Anaheim, California", "Ducks", "Western", "Pacific", "NHL", "National Hockey League", "Honda Center", "Honda Center, Anaheim", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(25, 20171001, "Arizona Coyotes", "Glendale", "Arizona", "", "AZ", "USA", "United States", "Glendale, AZ", "Arizona", "Glendale, Arizona", "Coyotes", "Western", "Pacific", "NHL", "National Hockey League", "Gila River Arena", "Gila River Arena, Glendale", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(26, 20171001, "Calgary Flames", "Calgary", "Calgary", "", "AB", "CAN", "Canada", "Calgary, AB", "Alberta", "Calgary, Alberta", "Flames", "Western", "Pacific", "NHL", "National Hockey League", "Scotiabank Saddledome", "Scotiabank Saddledome, Calgary", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(27, 20171001, "Edmonton Oilers", "Edmonton", "Edmonton", "", "AB", "CAN", "Canada", "Edmonton, AB", "Alberta", "Edmonton, Alberta", "Oilers", "Western", "Pacific", "NHL", "National Hockey League", "Rogers Place", "Rogers Place, Edmonton", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(28, 20171001, "Los Angeles Kings", "Los Angeles", "Los Angeles", "", "CA", "USA", "United States", "Los Angeles, CA", "California", "Los Angeles, California", "Kings", "Western", "Pacific", "NHL", "National Hockey League", "Staples Center", "Staples Center, Los Angeles", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(29, 20171001, "San Jose Sharks", "San Jose", "San Jose", "", "CA", "USA", "United States", "San Jose, CA", "California", "San Jose, California", "Sharks", "Western", "Pacific", "NHL", "National Hockey League", "SAP Center", "SAP Center, San Jose", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(30, 20171001, "Vancouver Canucks", "Vancouver", "Vancouver", "", "BC", "CAN", "Canada", "Vancouver, BC", "British Columbia", "Vancouver, British Columbia", "Canucks", "Western", "Pacific", "NHL", "National Hockey League", "Rogers Arena", "Rogers Arena, Vancouver", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(31, 20171001, "Vegas Golden Knights", "Paradise", "Vegas", "", "NV", "USA", "United States", "Paradise, NV", "Nevada", "Paradise, Nevada", "Golden Knights", "Western", "Pacific", "NHL", "National Hockey League", "T-Mobile Arena", "T-Mobile Arena, Paradise", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");

-- --------------------------------------------------------

--
-- Table structure for table NHLStats
--

CREATE TABLE NHLStats (
  id INTEGER PRIMARY KEY,
  TeamID INTEGER,
  Date INTEGER,
  FullName TEXT,
  CityName TEXT,
  TeamPrefix TEXT,
  TeamSuffix TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  TeamName TEXT,
  Conference TEXT,
  Division TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GamesPlayed INTEGER,
  GamesPlayedHome INTEGER,
  GamesPlayedAway INTEGER,
  Ties INTEGER,
  Wins INTEGER,
  OTWins INTEGER,
  SOWins INTEGER,
  OTSOWins INTEGER,
  TWins INTEGER,
  Losses INTEGER,
  OTLosses INTEGER,
  SOLosses INTEGER,
  OTSOLosses INTEGER,
  TLosses INTEGER,
  ROW INTEGER,
  ROT INTEGER,
  ShutoutWins INTEGER,
  ShutoutLosses INTEGER,
  HomeRecord TEXT,
  AwayRecord TEXT,
  Shootouts TEXT,
  GoalsFor INTEGER,
  GoalsAgainst INTEGER,
  GoalsDifference INTEGER,
  SOGFor INTEGER,
  SOGAgainst INTEGER,
  SOGDifference INTEGER,
  ShotsBlockedFor INTEGER,
  ShotsBlockedAgainst INTEGER,
  ShotsBlockedDifference INTEGER,
  PPGFor INTEGER,
  PPGAgainst INTEGER,
  PPGDifference INTEGER,
  SHGFor INTEGER,
  SHGAgainst INTEGER,
  SHGDifference INTEGER,
  PenaltiesFor INTEGER,
  PenaltiesAgainst INTEGER,
  PenaltiesDifference INTEGER,
  PIMFor INTEGER,
  PIMAgainst INTEGER,
  PIMDifference INTEGER,
  HITSFor INTEGER,
  HITSAgainst INTEGER,
  HITSDifference INTEGER,
  TakeAways INTEGER,
  GiveAways INTEGER,
  TAGADifference INTEGER,
  FaceoffWins INTEGER,
  FaceoffLosses INTEGER,
  FaceoffDifference INTEGER,
  Points INTEGER,
  PCT REAL,
  LastTen TEXT,
  Streak TEXT,
  FOREIGN KEY(TeamID) REFERENCES NHLTeams(id)
);

--
-- Dumping data for table NHLStats
--

INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(1, 1, 20171001, "Boston Bruins", "Boston", "Boston", "", "MA", "USA", "United States", "Boston, MA", "Massachusetts", "Boston, Massachusetts", "Bruins", "Eastern", "Atlantic", "NHL", "National Hockey League", "TD Garden", "TD Garden, Boston", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(2, 2, 20171001, "Buffalo Sabres", "Buffalo", "Buffalo", "", "NY", "USA", "United States", "Buffalo, NY", "New York", "Buffalo, New York", "Sabres", "Eastern", "Atlantic", "NHL", "National Hockey League", "KeyBank Center", "KeyBank Center, Buffalo", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(3, 3, 20171001, "Detroit Red Wings", "Detroit", "Detroit", "", "MI", "USA", "United States", "Detroit, MI", "Michigan", "Detroit, Michigan", "Red Wings", "Eastern", "Atlantic", "NHL", "National Hockey League", "Little Caesars Arena", "Little Caesars Arena, Detroit", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(4, 4, 20171001, "Florida Panthers", "Sunrise", "Florida", "", "FL", "USA", "United States", "Sunrise, FL", "Florida", "Sunrise, Florida", "Panthers", "Eastern", "Atlantic", "NHL", "National Hockey League", "BB&T Center", "BB&T Center, Sunrise", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(5, 5, 20171001, "Montreal Canadiens", "Montreal", "Montreal", "", "QC", "CAN", "Canada", "Montreal, QC", "Quebec", "Montreal, Quebec", "Canadiens", "Eastern", "Atlantic", "NHL", "National Hockey League", "Bell Centre", "Bell Centre, Montreal", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(6, 6, 20171001, "Ottawa Senators", "Ottawa", "Ottawa", "", "ON", "CAN", "Canada", "Ottawa, ON", "Ontario", "Ottawa, Ontario", "Senators", "Eastern", "Atlantic", "NHL", "National Hockey League", "Canadian Tire Centre", "Canadian Tire Centre, Ottawa", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(7, 7, 20171001, "Tampa Bay Lightning", "Tampa Bay", "Tampa Bay", "", "FL", "USA", "United States", "Tampa Bay, FL", "Florida", "Tampa Bay, Florida", "Lightning", "Eastern", "Atlantic", "NHL", "National Hockey League", "Amalie Arena", "Amalie Arena, Tampa Bay", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(8, 8, 20171001, "Toronto Maple Leafs", "Toronto", "Toronto", "", "ON", "CAN", "Canada", "Toronto, ON", "Ontario", "Toronto, Ontario", "Maple Leafs", "Eastern", "Atlantic", "NHL", "National Hockey League", "Air Canada Centre", "Air Canada Centre, Toronto", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(9, 9, 20171001, "Carolina Hurricanes", "Carolina", "Carolina", "", "NC", "USA", "United States", "Carolina, NC", "North Carolina", "Carolina, North Carolina", "Hurricanes", "Eastern", "Metropolitan", "NHL", "National Hockey League", "PNC Arena", "PNC Arena, Carolina", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(10, 10, 20171001, "Columbus Blue Jackets", "Columbus", "Columbus", "", "OH", "USA", "United States", "Columbus, OH", "Ohio", "Columbus, Ohio", "Blue Jackets", "Eastern", "Metropolitan", "NHL", "National Hockey League", "Nationwide Arena", "Nationwide Arena, Columbus", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(11, 11, 20171001, "New Jersey Devils", "New Jersey", "New Jersey", "", "NJ", "USA", "United States", "New Jersey, NJ", "New Jersey", "New Jersey, New Jersey", "Devils", "Eastern", "Metropolitan", "NHL", "National Hockey League", "Prudential Center", "Prudential Center, New Jersey", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(12, 12, 20171001, "New York Islanders", "New York City", "New York", "", "NY", "USA", "United States", "New York City, NY", "New York", "New York City, New York", "Islanders", "Eastern", "Metropolitan", "NHL", "National Hockey League", "Barclays Center", "Barclays Center, New York City", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(13, 13, 20171001, "New York Rangers", "New York City", "New York", "", "NY", "USA", "United States", "New York City, NY", "New York", "New York City, New York", "Rangers", "Eastern", "Metropolitan", "NHL", "National Hockey League", "Madison Square Garden", "Madison Square Garden, New York City", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(14, 14, 20171001, "Philadelphia Flyers", "Philadelphia", "Philadelphia", "", "PA", "USA", "United States", "Philadelphia, PA", "Pennsylvania", "Philadelphia, Pennsylvania", "Flyers", "Eastern", "Metropolitan", "NHL", "National Hockey League", "Wells Fargo Center", "Wells Fargo Center, Philadelphia", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(15, 15, 20171001, "Pittsburgh Penguins", "Pittsburgh", "Pittsburgh", "", "PA", "USA", "United States", "Pittsburgh, PA", "Pennsylvania", "Pittsburgh, Pennsylvania", "Penguins", "Eastern", "Metropolitan", "NHL", "National Hockey League", "PPG Paints Arena", "PPG Paints Arena, Pittsburgh", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(16, 16, 20171001, "Washington Capitals", "Washington", "Washington", "", "DC", "USA", "United States", "Washington, DC", "District of Columbia", "Washington, District of Columbia", "Capitals", "Eastern", "Metropolitan", "NHL", "National Hockey League", "Capital One Arena", "Capital One Arena, Washington", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(17, 17, 20171001, "Chicago Blackhawks", "Chicago", "Chicago", "", "IL", "USA", "United States", "Chicago, IL", "Illinois", "Chicago, Illinois", "Blackhawks", "Western", "Central", "NHL", "National Hockey League", "United Center", "United Center, Chicago", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(18, 18, 20171001, "Colorado Avalanche", "Denver", "Colorado", "", "CO", "USA", "United States", "Denver, CO", "Colorado", "Denver, Colorado", "Avalanche", "Western", "Central", "NHL", "National Hockey League", "Pepsi Center", "Pepsi Center, Denver", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(19, 19, 20171001, "Dallas Stars", "Dallas", "Dallas", "", "TX", "USA", "United States", "Dallas, TX", "Texas", "Dallas, Texas", "Stars", "Western", "Central", "NHL", "National Hockey League", "American Airlines Center", "American Airlines Center, Dallas", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(20, 20, 20171001, "Minnesota Wild", "St. Paul", "Minnesota", "", "MN", "USA", "United States", "St. Paul, MN", "Minnesota", "St. Paul, Minnesota", "Wild", "Western", "Central", "NHL", "National Hockey League", "Xcel Energy Center", "Xcel Energy Center, St. Paul", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(21, 21, 20171001, "Nashville Predators", "Nashville", "Nashville", "", "TN", "USA", "United States", "Nashville, TN", "Tennessee", "Nashville, Tennessee", "Predators", "Western", "Central", "NHL", "National Hockey League", "Bridgestone Arena", "Bridgestone Arena, Nashville", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(22, 22, 20171001, "St. Louis Blues", "St. Louis", "St. Louis", "", "MO", "USA", "United States", "St. Louis, MO", "Missouri", "St. Louis, Missouri", "Blues", "Western", "Central", "NHL", "National Hockey League", "Scottrade Center", "Scottrade Center, St. Louis", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(23, 23, 20171001, "Winnipeg Jets", "Winnipeg", "Winnipeg", "", "MB", "CAN", "Canada", "Winnipeg, MB", "Manitoba", "Winnipeg, Manitoba", "Jets", "Western", "Central", "NHL", "National Hockey League", "Bell MTS Place", "Bell MTS Place, Winnipeg", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(24, 24, 20171001, "Anaheim Ducks", "Anaheim", "Anaheim", "", "CA", "USA", "United States", "Anaheim, CA", "California", "Anaheim, California", "Ducks", "Western", "Pacific", "NHL", "National Hockey League", "Honda Center", "Honda Center, Anaheim", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(25, 25, 20171001, "Arizona Coyotes", "Glendale", "Arizona", "", "AZ", "USA", "United States", "Glendale, AZ", "Arizona", "Glendale, Arizona", "Coyotes", "Western", "Pacific", "NHL", "National Hockey League", "Gila River Arena", "Gila River Arena, Glendale", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(26, 26, 20171001, "Calgary Flames", "Calgary", "Calgary", "", "AB", "CAN", "Canada", "Calgary, AB", "Alberta", "Calgary, Alberta", "Flames", "Western", "Pacific", "NHL", "National Hockey League", "Scotiabank Saddledome", "Scotiabank Saddledome, Calgary", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(27, 27, 20171001, "Edmonton Oilers", "Edmonton", "Edmonton", "", "AB", "CAN", "Canada", "Edmonton, AB", "Alberta", "Edmonton, Alberta", "Oilers", "Western", "Pacific", "NHL", "National Hockey League", "Rogers Place", "Rogers Place, Edmonton", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(28, 28, 20171001, "Los Angeles Kings", "Los Angeles", "Los Angeles", "", "CA", "USA", "United States", "Los Angeles, CA", "California", "Los Angeles, California", "Kings", "Western", "Pacific", "NHL", "National Hockey League", "Staples Center", "Staples Center, Los Angeles", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(29, 29, 20171001, "San Jose Sharks", "San Jose", "San Jose", "", "CA", "USA", "United States", "San Jose, CA", "California", "San Jose, California", "Sharks", "Western", "Pacific", "NHL", "National Hockey League", "SAP Center", "SAP Center, San Jose", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(30, 30, 20171001, "Vancouver Canucks", "Vancouver", "Vancouver", "", "BC", "CAN", "Canada", "Vancouver, BC", "British Columbia", "Vancouver, British Columbia", "Canucks", "Western", "Pacific", "NHL", "National Hockey League", "Rogers Arena", "Rogers Arena, Vancouver", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(31, 31, 20171001, "Vegas Golden Knights", "Paradise", "Vegas", "", "NV", "USA", "United States", "Paradise, NV", "Nevada", "Paradise, Nevada", "Golden Knights", "Western", "Pacific", "NHL", "National Hockey League", "T-Mobile Arena", "T-Mobile Arena, Paradise", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");

-- --------------------------------------------------------

--
-- Table structure for table NHLGameStats
--

CREATE TABLE NHLGameStats (
  id INTEGER PRIMARY KEY,
  GameID INTEGER,
  Date INTEGER,
  TeamID INTEGER,
  FullName TEXT,
  CityName TEXT,
  TeamPrefix TEXT,
  TeamSuffix TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  TeamName TEXT,
  Conference TEXT,
  Division TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GoalsFor INTEGER,
  GoalsAgainst INTEGER,
  GoalsDifference INTEGER,
  SOGFor INTEGER,
  SOGAgainst INTEGER,
  SOGDifference INTEGER,
  ShotsBlockedFor INTEGER,
  ShotsBlockedAgainst INTEGER,
  ShotsBlockedDifference INTEGER,
  PPGFor INTEGER,
  PPGAgainst INTEGER,
  PPGDifference INTEGER,
  SHGFor INTEGER,
  SHGAgainst INTEGER,
  SHGDifference INTEGER,
  PenaltiesFor INTEGER,
  PenaltiesAgainst INTEGER,
  PenaltiesDifference INTEGER,
  PIMFor INTEGER,
  PIMAgainst INTEGER,
  PIMDifference INTEGER,
  HITSFor INTEGER,
  HITSAgainst INTEGER,
  HITSDifference INTEGER,
  TakeAways INTEGER,
  GiveAways INTEGER,
  TAGADifference INTEGER,
  FaceoffWins INTEGER,
  FaceoffLosses INTEGER,
  FaceoffDifference INTEGER,
  FOREIGN KEY(GameID) REFERENCES NHLGames(id),
  FOREIGN KEY(TeamID) REFERENCES NHLTeams(id)
);

--
-- Dumping data for table NHLGameStats
--


-- --------------------------------------------------------

--
-- Table structure for table NHLGames
--

CREATE TABLE NHLGames (
  id INTEGER PRIMARY KEY,
  Date INTEGER,
  HomeTeam TEXT,
  AwayTeam TEXT,
  AtArena TEXT,
  TeamScorePeriods TEXT,
  TeamFullScore TEXT,
  ShotsOnGoal TEXT,
  FullShotsOnGoal TEXT,
  ShotsBlocked TEXT,
  FullShotsBlocked TEXT,
  PowerPlays TEXT,
  FullPowerPlays TEXT,
  ShortHanded TEXT,
  FullShortHanded TEXT,
  Penalties TEXT,
  FullPenalties TEXT,
  PenaltyMinutes TEXT,
  FullPenaltyMinutes TEXT,
  HitsPerPeriod TEXT,
  FullHitsPerPeriod TEXT,
  TakeAways TEXT,
  FullTakeAways TEXT,
  GiveAways TEXT,
  FullGiveAways TEXT,
  FaceoffWins TEXT,
  FullFaceoffWins TEXT,
  NumberPeriods INTEGER,
  TeamWin TEXT,
  TeamLost TEXT,
  TieGame INTEGER,
  IsPlayOffGame INTEGER
);

--
-- Dumping data for table NHLGames
--


-- --------------------------------------------------------

--
-- Table structure for table AHLConferences
--

CREATE TABLE AHLConferences (
  id INTEGER PRIMARY KEY,
  Conference TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  NumberOfTeams INTEGER,
  NumberOfDivisions INTEGER
);

--
-- Dumping data for table AHLConferences
--

INSERT INTO AHLConferences (id, Conference, LeagueName, LeagueFullName, NumberOfTeams, NumberOfDivisions) VALUES 
(1, "Eastern", "AHL", "American Hockey League", 15, 2);
INSERT INTO AHLConferences (id, Conference, LeagueName, LeagueFullName, NumberOfTeams, NumberOfDivisions) VALUES 
(2, "Western", "AHL", "American Hockey League", 15, 2);

-- --------------------------------------------------------

--
-- Table structure for table AHLDivisions
--

CREATE TABLE AHLDivisions (
  id INTEGER PRIMARY KEY,
  Division TEXT,
  Conference TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  NumberOfTeams INTEGER
);

--
-- Dumping data for table AHLDivisions
--

INSERT INTO AHLDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(1, "Atlantic", "Eastern", "AHL", "American Hockey League", 8);
INSERT INTO AHLDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(2, "North", "Eastern", "AHL", "American Hockey League", 7);
INSERT INTO AHLDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(3, "Central", "Western", "AHL", "American Hockey League", 7);
INSERT INTO AHLDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(4, "Pacific", "Western", "AHL", "American Hockey League", 8);

-- --------------------------------------------------------

--
-- Table structure for table AHLArenas
--

CREATE TABLE AHLArenas (
  id INTEGER PRIMARY KEY,
  TeamID INTEGER,
  TeamName TEXT,
  TeamFullName TEXT,
  CityName TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GamesPlayed INTEGER,
  FOREIGN KEY(TeamID) REFERENCES AHLTeams(id)
);

--
-- Dumping data for table AHLArenas
--

INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(1, 1, "Sound Tigers", "Bridgeport Sound Tigers", "Bridgeport", "CT", "USA", "United States", "Bridgeport, CT", "Connecticut", "Bridgeport, Connecticut", "Webster Bank Arena", "Webster Bank Arena, Bridgeport", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(2, 2, "Checkers", "Charlotte Checkers", "Charlotte", "NC", "USA", "United States", "Charlotte, NC", "North Carolina", "Charlotte, North Carolina", "Bojangles' Coliseum", "Bojangles' Coliseum, Charlotte", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(3, 3, "Wolf Pack", "Hartford Wolf Pack", "Hartford", "CT", "USA", "United States", "Hartford, CT", "Connecticut", "Hartford, Connecticut", "XL Center", "XL Center, Hartford", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(4, 4, "Bears", "Hershey Bears", "Hershey", "PA", "USA", "United States", "Hershey, PA", "Pennsylvania", "Hershey, Pennsylvania", "Giant Center", "Giant Center, Hershey", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(5, 5, "Phantoms", "Lehigh Valley Phantoms", "Allentown", "PA", "USA", "United States", "Allentown, PA", "Pennsylvania", "Allentown, Pennsylvania", "PPL Center", "PPL Center, Allentown", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(6, 6, "Bruins", "Providence Bruins", "Providence", "RI", "USA", "United States", "Providence, RI", "Rhode Island", "Providence, Rhode Island", "Dunkin' Donuts Center", "Dunkin' Donuts Center, Providence", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(7, 7, "Thunderbirds", "Springfield Thunderbirds", "Springfield", "MA", "USA", "United States", "Springfield, MA", "Massachusetts", "Springfield, Massachusetts", "MassMutual Center", "MassMutual Center, Springfield", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(8, 8, "Penguins", "Wilkes-Barre/Scranton Penguins", "Wilkes-Barre", "PA", "USA", "United States", "Wilkes-Barre, PA", "Pennsylvania", "Wilkes-Barre, Pennsylvania", "Mohegan Sun Arena", "Mohegan Sun Arena, Wilkes-Barre", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(9, 9, "Senators", "Belleville Senators", "Belleville", "ON", "CAN", "Canada", "Belleville, ON", "Ontario", "Belleville, Ontario", "Yardmen Arena", "Yardmen Arena, Belleville", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(10, 10, "Devils", "Binghamton Devils", "Binghamton", "NY", "USA", "United States", "Binghamton, NY", "New York", "Binghamton, New York", "Veterans Memorial Arena", "Veterans Memorial Arena, Binghamton", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(11, 11, "Rocket", "Laval Rocket", "Laval", "QC", "CAN", "Canada", "Laval, QC", "Quebec", "Laval, Quebec", "Place Bell", "Place Bell, Laval", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(12, 12, "Americans", "Rochester Americans", "Rochester", "NY", "USA", "United States", "Rochester, NY", "New York", "Rochester, New York", "Blue Cross Arena", "Blue Cross Arena, Rochester", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(13, 13, "Crunch", "Syracuse Crunch", "Syracuse", "NY", "USA", "United States", "Syracuse, NY", "New York", "Syracuse, New York", "Oncenter War Memorial Arena", "Oncenter War Memorial Arena, Syracuse", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(14, 14, "Marlies", "Toronto Marlies", "Toronto", "ON", "CAN", "Canada", "Toronto, ON", "Ontario", "Toronto, Ontario", "Ricoh Coliseum", "Ricoh Coliseum, Toronto", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(15, 15, "Comets", "Utica Comets", "Utica", "NY", "USA", "United States", "Utica, NY", "New York", "Utica, New York", "Adirondack Bank Center", "Adirondack Bank Center, Utica", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(16, 16, "Wolves", "Chicago Wolves", "Rosemont", "IL", "USA", "United States", "Rosemont, IL", "Illinois", "Rosemont, Illinois", "Allstate Arena", "Allstate Arena, Rosemont", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(17, 17, "Monsters", "Lake Erie Monsters", "Cleveland", "OH", "USA", "United States", "Cleveland, OH", "Ohio", "Cleveland, Ohio", "Quicken Loans Arena", "Quicken Loans Arena, Cleveland", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(18, 18, "Griffins", "Grand Rapids Griffins", "Grand Rapids", "MI", "USA", "United States", "Grand Rapids, MI", "Michigan", "Grand Rapids, Michigan", "Van Andel Arena", "Van Andel Arena, Grand Rapids", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(19, 19, "Wild", "Iowa Wild", "Des Moines", "IA", "USA", "United States", "Des Moines, IA", "Iowa", "Des Moines, Iowa", "Wells Fargo Arena", "Wells Fargo Arena, Des Moines", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(20, 20, "Moose", "Manitoba Moose", "Winnipeg", "MB", "CAN", "Canada", "Winnipeg, MB", "Manitoba", "Winnipeg, Manitoba", "Bell MTS Place", "Bell MTS Place, Winnipeg", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(21, 21, "Admirals", "Milwaukee Admirals", "Milwaukee", "WI", "USA", "United States", "Milwaukee, WI", "Wisconsin", "Milwaukee, Wisconsin", "UW-Milwaukee Panther Arena", "UW-Milwaukee Panther Arena, Milwaukee", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(22, 22, "IceHogs", "Rockford IceHogs", "Rockford", "IL", "USA", "United States", "Rockford, IL", "Illinois", "Rockford, Illinois", "BMO Harris Bank Center", "BMO Harris Bank Center, Rockford", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(23, 23, "Condors", "Bakersfield Condors", "Bakersfield", "CA", "USA", "United States", "Bakersfield, CA", "California", "Bakersfield, California", "Rabobank Arena", "Rabobank Arena, Bakersfield", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(24, 24, "Reign", "Ontario Reign", "Ontario", "CA", "USA", "United States", "Ontario, CA", "California", "Ontario, California", "Citizens Business Bank Arena", "Citizens Business Bank Arena, Ontario", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(25, 25, "Rampage", "San Antonio Rampage", "San Antonio", "TX", "USA", "United States", "San Antonio, TX", "Texas", "San Antonio, Texas", "AT&T Center", "AT&T Center, San Antonio", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(26, 26, "Gulls", "San Diego Gulls", "San Diego", "CA", "USA", "United States", "San Diego, CA", "California", "San Diego, California", "Valley View Casino Center", "Valley View Casino Center, San Diego", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(27, 27, "Barracuda", "San Jose Barracuda", "San Jose", "CA", "USA", "United States", "San Jose, CA", "California", "San Jose, California", "SAP Center", "SAP Center, San Jose", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(28, 28, "Heat", "Stockton Heat", "Stockton", "CA", "USA", "United States", "Stockton, CA", "California", "Stockton, California", "Stockton Arena", "Stockton Arena, Stockton", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(29, 29, "Stars", "Texas Stars", "Cedar Park", "TX", "USA", "United States", "Cedar Park, TX", "Texas", "Cedar Park, Texas", "H-E-B Center", "H-E-B Center, Cedar Park", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(30, 30, "Roadrunners", "Tucson Roadrunners", "Tucson", "AZ", "USA", "United States", "Tucson, AZ", "Arizona", "Tucson, Arizona", "Tucson Convention Center", "Tucson Convention Center, Tucson", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(31, 0, "", "", "Hershey", "PA", "USA", "United States", "Hershey, PA", "Pennsylvania", "Hershey, Pennsylvania", "Hersheypark Stadium", "Hersheypark Stadium, Hershey", 0);

-- --------------------------------------------------------

--
-- Table structure for table AHLTeams
--

CREATE TABLE AHLTeams (
  id INTEGER PRIMARY KEY,
  Date INTEGER,
  FullName TEXT,
  CityName TEXT,
  TeamPrefix TEXT,
  TeamSuffix TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  TeamName TEXT,
  Conference TEXT,
  Division TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GamesPlayed INTEGER,
  GamesPlayedHome INTEGER,
  GamesPlayedAway INTEGER,
  Ties INTEGER,
  Wins INTEGER,
  OTWins INTEGER,
  SOWins INTEGER,
  OTSOWins INTEGER,
  TWins INTEGER,
  Losses INTEGER,
  OTLosses INTEGER,
  SOLosses INTEGER,
  OTSOLosses INTEGER,
  TLosses INTEGER,
  ROW INTEGER,
  ROT INTEGER,
  ShutoutWins INTEGER,
  ShutoutLosses INTEGER,
  HomeRecord TEXT,
  AwayRecord TEXT,
  Shootouts TEXT,
  GoalsFor INTEGER,
  GoalsAgainst INTEGER,
  GoalsDifference INTEGER,
  SOGFor INTEGER,
  SOGAgainst INTEGER,
  SOGDifference INTEGER,
  ShotsBlockedFor INTEGER,
  ShotsBlockedAgainst INTEGER,
  ShotsBlockedDifference INTEGER,
  PPGFor INTEGER,
  PPGAgainst INTEGER,
  PPGDifference INTEGER,
  SHGFor INTEGER,
  SHGAgainst INTEGER,
  SHGDifference INTEGER,
  PenaltiesFor INTEGER,
  PenaltiesAgainst INTEGER,
  PenaltiesDifference INTEGER,
  PIMFor INTEGER,
  PIMAgainst INTEGER,
  PIMDifference INTEGER,
  HITSFor INTEGER,
  HITSAgainst INTEGER,
  HITSDifference INTEGER,
  TakeAways INTEGER,
  GiveAways INTEGER,
  TAGADifference INTEGER,
  FaceoffWins INTEGER,
  FaceoffLosses INTEGER,
  FaceoffDifference INTEGER,
  Points INTEGER,
  PCT REAL,
  LastTen TEXT,
  Streak TEXT
);

--
-- Dumping data for table AHLTeams
--

INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(1, 20171001, "Bridgeport Sound Tigers", "Bridgeport", "Bridgeport", "", "CT", "USA", "United States", "Bridgeport, CT", "Connecticut", "Bridgeport, Connecticut", "Sound Tigers", "Eastern", "Atlantic", "AHL", "American Hockey League", "Webster Bank Arena", "Webster Bank Arena, Bridgeport", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(2, 20171001, "Charlotte Checkers", "Charlotte", "Charlotte", "", "NC", "USA", "United States", "Charlotte, NC", "North Carolina", "Charlotte, North Carolina", "Checkers", "Eastern", "Atlantic", "AHL", "American Hockey League", "Bojangles' Coliseum", "Bojangles' Coliseum, Charlotte", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(3, 20171001, "Hartford Wolf Pack", "Hartford", "Hartford", "", "CT", "USA", "United States", "Hartford, CT", "Connecticut", "Hartford, Connecticut", "Wolf Pack", "Eastern", "Atlantic", "AHL", "American Hockey League", "XL Center", "XL Center, Hartford", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(4, 20171001, "Hershey Bears", "Hershey", "Hershey", "", "PA", "USA", "United States", "Hershey, PA", "Pennsylvania", "Hershey, Pennsylvania", "Bears", "Eastern", "Atlantic", "AHL", "American Hockey League", "Giant Center", "Giant Center, Hershey", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(5, 20171001, "Lehigh Valley Phantoms", "Allentown", "Lehigh Valley", "", "PA", "USA", "United States", "Allentown, PA", "Pennsylvania", "Allentown, Pennsylvania", "Phantoms", "Eastern", "Atlantic", "AHL", "American Hockey League", "PPL Center", "PPL Center, Allentown", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(6, 20171001, "Providence Bruins", "Providence", "Providence", "", "RI", "USA", "United States", "Providence, RI", "Rhode Island", "Providence, Rhode Island", "Bruins", "Eastern", "Atlantic", "AHL", "American Hockey League", "Dunkin' Donuts Center", "Dunkin' Donuts Center, Providence", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(7, 20171001, "Springfield Thunderbirds", "Springfield", "Springfield", "", "MA", "USA", "United States", "Springfield, MA", "Massachusetts", "Springfield, Massachusetts", "Thunderbirds", "Eastern", "Atlantic", "AHL", "American Hockey League", "MassMutual Center", "MassMutual Center, Springfield", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(8, 20171001, "Wilkes-Barre/Scranton Penguins", "Wilkes-Barre", "Wilkes-Barre/Scranton", "", "PA", "USA", "United States", "Wilkes-Barre, PA", "Pennsylvania", "Wilkes-Barre, Pennsylvania", "Penguins", "Eastern", "Atlantic", "AHL", "American Hockey League", "Mohegan Sun Arena", "Mohegan Sun Arena, Wilkes-Barre", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(9, 20171001, "Belleville Senators", "Belleville", "Belleville", "", "ON", "CAN", "Canada", "Belleville, ON", "Ontario", "Belleville, Ontario", "Senators", "Eastern", "North", "AHL", "American Hockey League", "Yardmen Arena", "Yardmen Arena, Belleville", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(10, 20171001, "Binghamton Devils", "Binghamton", "Binghamton", "", "NY", "USA", "United States", "Binghamton, NY", "New York", "Binghamton, New York", "Devils", "Eastern", "North", "AHL", "American Hockey League", "Veterans Memorial Arena", "Veterans Memorial Arena, Binghamton", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(11, 20171001, "Laval Rocket", "Laval", "Laval", "", "QC", "CAN", "Canada", "Laval, QC", "Quebec", "Laval, Quebec", "Rocket", "Eastern", "North", "AHL", "American Hockey League", "Place Bell", "Place Bell, Laval", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(12, 20171001, "Rochester Americans", "Rochester", "Rochester", "", "NY", "USA", "United States", "Rochester, NY", "New York", "Rochester, New York", "Americans", "Eastern", "North", "AHL", "American Hockey League", "Blue Cross Arena", "Blue Cross Arena, Rochester", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(13, 20171001, "Syracuse Crunch", "Syracuse", "Syracuse", "", "NY", "USA", "United States", "Syracuse, NY", "New York", "Syracuse, New York", "Crunch", "Eastern", "North", "AHL", "American Hockey League", "Oncenter War Memorial Arena", "Oncenter War Memorial Arena, Syracuse", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(14, 20171001, "Toronto Marlies", "Toronto", "Toronto", "", "ON", "CAN", "Canada", "Toronto, ON", "Ontario", "Toronto, Ontario", "Marlies", "Eastern", "North", "AHL", "American Hockey League", "Ricoh Coliseum", "Ricoh Coliseum, Toronto", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(15, 20171001, "Utica Comets", "Utica", "Utica", "", "NY", "USA", "United States", "Utica, NY", "New York", "Utica, New York", "Comets", "Eastern", "North", "AHL", "American Hockey League", "Adirondack Bank Center", "Adirondack Bank Center, Utica", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(16, 20171001, "Chicago Wolves", "Rosemont", "Chicago", "", "IL", "USA", "United States", "Rosemont, IL", "Illinois", "Rosemont, Illinois", "Wolves", "Western", "Central", "AHL", "American Hockey League", "Allstate Arena", "Allstate Arena, Rosemont", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(17, 20171001, "Lake Erie Monsters", "Cleveland", "Lake Erie", "", "OH", "USA", "United States", "Cleveland, OH", "Ohio", "Cleveland, Ohio", "Monsters", "Western", "Central", "AHL", "American Hockey League", "Quicken Loans Arena", "Quicken Loans Arena, Cleveland", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(18, 20171001, "Grand Rapids Griffins", "Grand Rapids", "Grand Rapids", "", "MI", "USA", "United States", "Grand Rapids, MI", "Michigan", "Grand Rapids, Michigan", "Griffins", "Western", "Central", "AHL", "American Hockey League", "Van Andel Arena", "Van Andel Arena, Grand Rapids", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(19, 20171001, "Iowa Wild", "Des Moines", "Iowa", "", "IA", "USA", "United States", "Des Moines, IA", "Iowa", "Des Moines, Iowa", "Wild", "Western", "Central", "AHL", "American Hockey League", "Wells Fargo Arena", "Wells Fargo Arena, Des Moines", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(20, 20171001, "Manitoba Moose", "Winnipeg", "Manitoba", "", "MB", "CAN", "Canada", "Winnipeg, MB", "Manitoba", "Winnipeg, Manitoba", "Moose", "Western", "Central", "AHL", "American Hockey League", "Bell MTS Place", "Bell MTS Place, Winnipeg", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(21, 20171001, "Milwaukee Admirals", "Milwaukee", "Milwaukee", "", "WI", "USA", "United States", "Milwaukee, WI", "Wisconsin", "Milwaukee, Wisconsin", "Admirals", "Western", "Central", "AHL", "American Hockey League", "UW-Milwaukee Panther Arena", "UW-Milwaukee Panther Arena, Milwaukee", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(22, 20171001, "Rockford IceHogs", "Rockford", "Rockford", "", "IL", "USA", "United States", "Rockford, IL", "Illinois", "Rockford, Illinois", "IceHogs", "Western", "Central", "AHL", "American Hockey League", "BMO Harris Bank Center", "BMO Harris Bank Center, Rockford", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(23, 20171001, "Bakersfield Condors", "Bakersfield", "Bakersfield", "", "CA", "USA", "United States", "Bakersfield, CA", "California", "Bakersfield, California", "Condors", "Western", "Pacific", "AHL", "American Hockey League", "Rabobank Arena", "Rabobank Arena, Bakersfield", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(24, 20171001, "Ontario Reign", "Ontario", "Ontario", "", "CA", "USA", "United States", "Ontario, CA", "California", "Ontario, California", "Reign", "Western", "Pacific", "AHL", "American Hockey League", "Citizens Business Bank Arena", "Citizens Business Bank Arena, Ontario", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(25, 20171001, "San Antonio Rampage", "San Antonio", "San Antonio", "", "TX", "USA", "United States", "San Antonio, TX", "Texas", "San Antonio, Texas", "Rampage", "Western", "Pacific", "AHL", "American Hockey League", "AT&T Center", "AT&T Center, San Antonio", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(26, 20171001, "San Diego Gulls", "San Diego", "San Diego", "", "CA", "USA", "United States", "San Diego, CA", "California", "San Diego, California", "Gulls", "Western", "Pacific", "AHL", "American Hockey League", "Valley View Casino Center", "Valley View Casino Center, San Diego", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(27, 20171001, "San Jose Barracuda", "San Jose", "San Jose", "", "CA", "USA", "United States", "San Jose, CA", "California", "San Jose, California", "Barracuda", "Western", "Pacific", "AHL", "American Hockey League", "SAP Center", "SAP Center, San Jose", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(28, 20171001, "Stockton Heat", "Stockton", "Stockton", "", "CA", "USA", "United States", "Stockton, CA", "California", "Stockton, California", "Heat", "Western", "Pacific", "AHL", "American Hockey League", "Stockton Arena", "Stockton Arena, Stockton", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(29, 20171001, "Texas Stars", "Cedar Park", "Texas", "", "TX", "USA", "United States", "Cedar Park, TX", "Texas", "Cedar Park, Texas", "Stars", "Western", "Pacific", "AHL", "American Hockey League", "H-E-B Center", "H-E-B Center, Cedar Park", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(30, 20171001, "Tucson Roadrunners", "Tucson", "Tucson", "", "AZ", "USA", "United States", "Tucson, AZ", "Arizona", "Tucson, Arizona", "Roadrunners", "Western", "Pacific", "AHL", "American Hockey League", "Tucson Convention Center", "Tucson Convention Center, Tucson", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");

-- --------------------------------------------------------

--
-- Table structure for table AHLStats
--

CREATE TABLE AHLStats (
  id INTEGER PRIMARY KEY,
  TeamID INTEGER,
  Date INTEGER,
  FullName TEXT,
  CityName TEXT,
  TeamPrefix TEXT,
  TeamSuffix TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  TeamName TEXT,
  Conference TEXT,
  Division TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GamesPlayed INTEGER,
  GamesPlayedHome INTEGER,
  GamesPlayedAway INTEGER,
  Ties INTEGER,
  Wins INTEGER,
  OTWins INTEGER,
  SOWins INTEGER,
  OTSOWins INTEGER,
  TWins INTEGER,
  Losses INTEGER,
  OTLosses INTEGER,
  SOLosses INTEGER,
  OTSOLosses INTEGER,
  TLosses INTEGER,
  ROW INTEGER,
  ROT INTEGER,
  ShutoutWins INTEGER,
  ShutoutLosses INTEGER,
  HomeRecord TEXT,
  AwayRecord TEXT,
  Shootouts TEXT,
  GoalsFor INTEGER,
  GoalsAgainst INTEGER,
  GoalsDifference INTEGER,
  SOGFor INTEGER,
  SOGAgainst INTEGER,
  SOGDifference INTEGER,
  ShotsBlockedFor INTEGER,
  ShotsBlockedAgainst INTEGER,
  ShotsBlockedDifference INTEGER,
  PPGFor INTEGER,
  PPGAgainst INTEGER,
  PPGDifference INTEGER,
  SHGFor INTEGER,
  SHGAgainst INTEGER,
  SHGDifference INTEGER,
  PenaltiesFor INTEGER,
  PenaltiesAgainst INTEGER,
  PenaltiesDifference INTEGER,
  PIMFor INTEGER,
  PIMAgainst INTEGER,
  PIMDifference INTEGER,
  HITSFor INTEGER,
  HITSAgainst INTEGER,
  HITSDifference INTEGER,
  TakeAways INTEGER,
  GiveAways INTEGER,
  TAGADifference INTEGER,
  FaceoffWins INTEGER,
  FaceoffLosses INTEGER,
  FaceoffDifference INTEGER,
  Points INTEGER,
  PCT REAL,
  LastTen TEXT,
  Streak TEXT,
  FOREIGN KEY(TeamID) REFERENCES AHLTeams(id)
);

--
-- Dumping data for table AHLStats
--

INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(1, 1, 20171001, "Bridgeport Sound Tigers", "Bridgeport", "Bridgeport", "", "CT", "USA", "United States", "Bridgeport, CT", "Connecticut", "Bridgeport, Connecticut", "Sound Tigers", "Eastern", "Atlantic", "AHL", "American Hockey League", "Webster Bank Arena", "Webster Bank Arena, Bridgeport", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(2, 2, 20171001, "Charlotte Checkers", "Charlotte", "Charlotte", "", "NC", "USA", "United States", "Charlotte, NC", "North Carolina", "Charlotte, North Carolina", "Checkers", "Eastern", "Atlantic", "AHL", "American Hockey League", "Bojangles' Coliseum", "Bojangles' Coliseum, Charlotte", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(3, 3, 20171001, "Hartford Wolf Pack", "Hartford", "Hartford", "", "CT", "USA", "United States", "Hartford, CT", "Connecticut", "Hartford, Connecticut", "Wolf Pack", "Eastern", "Atlantic", "AHL", "American Hockey League", "XL Center", "XL Center, Hartford", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(4, 4, 20171001, "Hershey Bears", "Hershey", "Hershey", "", "PA", "USA", "United States", "Hershey, PA", "Pennsylvania", "Hershey, Pennsylvania", "Bears", "Eastern", "Atlantic", "AHL", "American Hockey League", "Giant Center", "Giant Center, Hershey", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(5, 5, 20171001, "Lehigh Valley Phantoms", "Allentown", "Lehigh Valley", "", "PA", "USA", "United States", "Allentown, PA", "Pennsylvania", "Allentown, Pennsylvania", "Phantoms", "Eastern", "Atlantic", "AHL", "American Hockey League", "PPL Center", "PPL Center, Allentown", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(6, 6, 20171001, "Providence Bruins", "Providence", "Providence", "", "RI", "USA", "United States", "Providence, RI", "Rhode Island", "Providence, Rhode Island", "Bruins", "Eastern", "Atlantic", "AHL", "American Hockey League", "Dunkin' Donuts Center", "Dunkin' Donuts Center, Providence", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(7, 7, 20171001, "Springfield Thunderbirds", "Springfield", "Springfield", "", "MA", "USA", "United States", "Springfield, MA", "Massachusetts", "Springfield, Massachusetts", "Thunderbirds", "Eastern", "Atlantic", "AHL", "American Hockey League", "MassMutual Center", "MassMutual Center, Springfield", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(8, 8, 20171001, "Wilkes-Barre/Scranton Penguins", "Wilkes-Barre", "Wilkes-Barre/Scranton", "", "PA", "USA", "United States", "Wilkes-Barre, PA", "Pennsylvania", "Wilkes-Barre, Pennsylvania", "Penguins", "Eastern", "Atlantic", "AHL", "American Hockey League", "Mohegan Sun Arena", "Mohegan Sun Arena, Wilkes-Barre", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(9, 9, 20171001, "Belleville Senators", "Belleville", "Belleville", "", "ON", "CAN", "Canada", "Belleville, ON", "Ontario", "Belleville, Ontario", "Senators", "Eastern", "North", "AHL", "American Hockey League", "Yardmen Arena", "Yardmen Arena, Belleville", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(10, 10, 20171001, "Binghamton Devils", "Binghamton", "Binghamton", "", "NY", "USA", "United States", "Binghamton, NY", "New York", "Binghamton, New York", "Devils", "Eastern", "North", "AHL", "American Hockey League", "Veterans Memorial Arena", "Veterans Memorial Arena, Binghamton", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(11, 11, 20171001, "Laval Rocket", "Laval", "Laval", "", "QC", "CAN", "Canada", "Laval, QC", "Quebec", "Laval, Quebec", "Rocket", "Eastern", "North", "AHL", "American Hockey League", "Place Bell", "Place Bell, Laval", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(12, 12, 20171001, "Rochester Americans", "Rochester", "Rochester", "", "NY", "USA", "United States", "Rochester, NY", "New York", "Rochester, New York", "Americans", "Eastern", "North", "AHL", "American Hockey League", "Blue Cross Arena", "Blue Cross Arena, Rochester", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(13, 13, 20171001, "Syracuse Crunch", "Syracuse", "Syracuse", "", "NY", "USA", "United States", "Syracuse, NY", "New York", "Syracuse, New York", "Crunch", "Eastern", "North", "AHL", "American Hockey League", "Oncenter War Memorial Arena", "Oncenter War Memorial Arena, Syracuse", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(14, 14, 20171001, "Toronto Marlies", "Toronto", "Toronto", "", "ON", "CAN", "Canada", "Toronto, ON", "Ontario", "Toronto, Ontario", "Marlies", "Eastern", "North", "AHL", "American Hockey League", "Ricoh Coliseum", "Ricoh Coliseum, Toronto", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(15, 15, 20171001, "Utica Comets", "Utica", "Utica", "", "NY", "USA", "United States", "Utica, NY", "New York", "Utica, New York", "Comets", "Eastern", "North", "AHL", "American Hockey League", "Adirondack Bank Center", "Adirondack Bank Center, Utica", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(16, 16, 20171001, "Chicago Wolves", "Rosemont", "Chicago", "", "IL", "USA", "United States", "Rosemont, IL", "Illinois", "Rosemont, Illinois", "Wolves", "Western", "Central", "AHL", "American Hockey League", "Allstate Arena", "Allstate Arena, Rosemont", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(17, 17, 20171001, "Lake Erie Monsters", "Cleveland", "Lake Erie", "", "OH", "USA", "United States", "Cleveland, OH", "Ohio", "Cleveland, Ohio", "Monsters", "Western", "Central", "AHL", "American Hockey League", "Quicken Loans Arena", "Quicken Loans Arena, Cleveland", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(18, 18, 20171001, "Grand Rapids Griffins", "Grand Rapids", "Grand Rapids", "", "MI", "USA", "United States", "Grand Rapids, MI", "Michigan", "Grand Rapids, Michigan", "Griffins", "Western", "Central", "AHL", "American Hockey League", "Van Andel Arena", "Van Andel Arena, Grand Rapids", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(19, 19, 20171001, "Iowa Wild", "Des Moines", "Iowa", "", "IA", "USA", "United States", "Des Moines, IA", "Iowa", "Des Moines, Iowa", "Wild", "Western", "Central", "AHL", "American Hockey League", "Wells Fargo Arena", "Wells Fargo Arena, Des Moines", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(20, 20, 20171001, "Manitoba Moose", "Winnipeg", "Manitoba", "", "MB", "CAN", "Canada", "Winnipeg, MB", "Manitoba", "Winnipeg, Manitoba", "Moose", "Western", "Central", "AHL", "American Hockey League", "Bell MTS Place", "Bell MTS Place, Winnipeg", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(21, 21, 20171001, "Milwaukee Admirals", "Milwaukee", "Milwaukee", "", "WI", "USA", "United States", "Milwaukee, WI", "Wisconsin", "Milwaukee, Wisconsin", "Admirals", "Western", "Central", "AHL", "American Hockey League", "UW-Milwaukee Panther Arena", "UW-Milwaukee Panther Arena, Milwaukee", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(22, 22, 20171001, "Rockford IceHogs", "Rockford", "Rockford", "", "IL", "USA", "United States", "Rockford, IL", "Illinois", "Rockford, Illinois", "IceHogs", "Western", "Central", "AHL", "American Hockey League", "BMO Harris Bank Center", "BMO Harris Bank Center, Rockford", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(23, 23, 20171001, "Bakersfield Condors", "Bakersfield", "Bakersfield", "", "CA", "USA", "United States", "Bakersfield, CA", "California", "Bakersfield, California", "Condors", "Western", "Pacific", "AHL", "American Hockey League", "Rabobank Arena", "Rabobank Arena, Bakersfield", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(24, 24, 20171001, "Ontario Reign", "Ontario", "Ontario", "", "CA", "USA", "United States", "Ontario, CA", "California", "Ontario, California", "Reign", "Western", "Pacific", "AHL", "American Hockey League", "Citizens Business Bank Arena", "Citizens Business Bank Arena, Ontario", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(25, 25, 20171001, "San Antonio Rampage", "San Antonio", "San Antonio", "", "TX", "USA", "United States", "San Antonio, TX", "Texas", "San Antonio, Texas", "Rampage", "Western", "Pacific", "AHL", "American Hockey League", "AT&T Center", "AT&T Center, San Antonio", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(26, 26, 20171001, "San Diego Gulls", "San Diego", "San Diego", "", "CA", "USA", "United States", "San Diego, CA", "California", "San Diego, California", "Gulls", "Western", "Pacific", "AHL", "American Hockey League", "Valley View Casino Center", "Valley View Casino Center, San Diego", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(27, 27, 20171001, "San Jose Barracuda", "San Jose", "San Jose", "", "CA", "USA", "United States", "San Jose, CA", "California", "San Jose, California", "Barracuda", "Western", "Pacific", "AHL", "American Hockey League", "SAP Center", "SAP Center, San Jose", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(28, 28, 20171001, "Stockton Heat", "Stockton", "Stockton", "", "CA", "USA", "United States", "Stockton, CA", "California", "Stockton, California", "Heat", "Western", "Pacific", "AHL", "American Hockey League", "Stockton Arena", "Stockton Arena, Stockton", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(29, 29, 20171001, "Texas Stars", "Cedar Park", "Texas", "", "TX", "USA", "United States", "Cedar Park, TX", "Texas", "Cedar Park, Texas", "Stars", "Western", "Pacific", "AHL", "American Hockey League", "H-E-B Center", "H-E-B Center, Cedar Park", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(30, 30, 20171001, "Tucson Roadrunners", "Tucson", "Tucson", "", "AZ", "USA", "United States", "Tucson, AZ", "Arizona", "Tucson, Arizona", "Roadrunners", "Western", "Pacific", "AHL", "American Hockey League", "Tucson Convention Center", "Tucson Convention Center, Tucson", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");

-- --------------------------------------------------------

--
-- Table structure for table AHLGameStats
--

CREATE TABLE AHLGameStats (
  id INTEGER PRIMARY KEY,
  GameID INTEGER,
  Date INTEGER,
  TeamID INTEGER,
  FullName TEXT,
  CityName TEXT,
  TeamPrefix TEXT,
  TeamSuffix TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  TeamName TEXT,
  Conference TEXT,
  Division TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GoalsFor INTEGER,
  GoalsAgainst INTEGER,
  GoalsDifference INTEGER,
  SOGFor INTEGER,
  SOGAgainst INTEGER,
  SOGDifference INTEGER,
  ShotsBlockedFor INTEGER,
  ShotsBlockedAgainst INTEGER,
  ShotsBlockedDifference INTEGER,
  PPGFor INTEGER,
  PPGAgainst INTEGER,
  PPGDifference INTEGER,
  SHGFor INTEGER,
  SHGAgainst INTEGER,
  SHGDifference INTEGER,
  PenaltiesFor INTEGER,
  PenaltiesAgainst INTEGER,
  PenaltiesDifference INTEGER,
  PIMFor INTEGER,
  PIMAgainst INTEGER,
  PIMDifference INTEGER,
  HITSFor INTEGER,
  HITSAgainst INTEGER,
  HITSDifference INTEGER,
  TakeAways INTEGER,
  GiveAways INTEGER,
  TAGADifference INTEGER,
  FaceoffWins INTEGER,
  FaceoffLosses INTEGER,
  FaceoffDifference INTEGER,
  FOREIGN KEY(GameID) REFERENCES AHLGames(id),
  FOREIGN KEY(TeamID) REFERENCES AHLTeams(id)
);

--
-- Dumping data for table AHLGameStats
--


-- --------------------------------------------------------

--
-- Table structure for table AHLGames
--

CREATE TABLE AHLGames (
  id INTEGER PRIMARY KEY,
  Date INTEGER,
  HomeTeam TEXT,
  AwayTeam TEXT,
  AtArena TEXT,
  TeamScorePeriods TEXT,
  TeamFullScore TEXT,
  ShotsOnGoal TEXT,
  FullShotsOnGoal TEXT,
  ShotsBlocked TEXT,
  FullShotsBlocked TEXT,
  PowerPlays TEXT,
  FullPowerPlays TEXT,
  ShortHanded TEXT,
  FullShortHanded TEXT,
  Penalties TEXT,
  FullPenalties TEXT,
  PenaltyMinutes TEXT,
  FullPenaltyMinutes TEXT,
  HitsPerPeriod TEXT,
  FullHitsPerPeriod TEXT,
  TakeAways TEXT,
  FullTakeAways TEXT,
  GiveAways TEXT,
  FullGiveAways TEXT,
  FaceoffWins TEXT,
  FullFaceoffWins TEXT,
  NumberPeriods INTEGER,
  TeamWin TEXT,
  TeamLost TEXT,
  TieGame INTEGER,
  IsPlayOffGame INTEGER
);

--
-- Dumping data for table AHLGames
--


-- --------------------------------------------------------

--
-- Table structure for table ECHLConferences
--

CREATE TABLE ECHLConferences (
  id INTEGER PRIMARY KEY,
  Conference TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  NumberOfTeams INTEGER,
  NumberOfDivisions INTEGER
);

--
-- Dumping data for table ECHLConferences
--

INSERT INTO ECHLConferences (id, Conference, LeagueName, LeagueFullName, NumberOfTeams, NumberOfDivisions) VALUES 
(1, "Eastern", "ECHL", "ECHL", 13, 2);
INSERT INTO ECHLConferences (id, Conference, LeagueName, LeagueFullName, NumberOfTeams, NumberOfDivisions) VALUES 
(2, "Western", "ECHL", "ECHL", 14, 2);

-- --------------------------------------------------------

--
-- Table structure for table ECHLDivisions
--

CREATE TABLE ECHLDivisions (
  id INTEGER PRIMARY KEY,
  Division TEXT,
  Conference TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  NumberOfTeams INTEGER
);

--
-- Dumping data for table ECHLDivisions
--

INSERT INTO ECHLDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(1, "North", "Eastern", "ECHL", "ECHL", 6);
INSERT INTO ECHLDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(2, "South", "Eastern", "ECHL", "ECHL", 7);
INSERT INTO ECHLDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(3, "Central", "Western", "ECHL", "ECHL", 7);
INSERT INTO ECHLDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(4, "Mountain", "Western", "ECHL", "ECHL", 7);

-- --------------------------------------------------------

--
-- Table structure for table ECHLArenas
--

CREATE TABLE ECHLArenas (
  id INTEGER PRIMARY KEY,
  TeamID INTEGER,
  TeamName TEXT,
  TeamFullName TEXT,
  CityName TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GamesPlayed INTEGER,
  FOREIGN KEY(TeamID) REFERENCES ECHLTeams(id)
);

--
-- Dumping data for table ECHLArenas
--

INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(1, 1, "Thunder", "Adirondack Thunder", "Glens Falls", "NY", "USA", "United States", "Glens Falls, NY", "New York", "Glens Falls, New York", "Cool Insuring Arena", "Cool Insuring Arena, Glens Falls", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(2, 2, "Beast", "Brampton Beast", "Brampton", "ON", "CAN", "Canada", "Brampton, ON", "Ontario", "Brampton, Ontario", "Powerade Centre", "Powerade Centre, Brampton", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(3, 3, "Monarchs", "Manchester Monarchs", "Manchester", "NH", "USA", "United States", "Manchester, NH", "New Hampshire", "Manchester, New Hampshire", "SNHU Arena", "SNHU Arena, Manchester", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(4, 4, "Royals", "Reading Royals", "Reading", "PA", "USA", "United States", "Reading, PA", "Pennsylvania", "Reading, Pennsylvania", "Santander Arena", "Santander Arena, Reading", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(5, 5, "Nailers", "Wheeling Nailers", "Wheeling", "WV", "USA", "United States", "Wheeling, WV", "West Virginia", "Wheeling, West Virginia", "WesBanco Arena", "WesBanco Arena, Wheeling", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(6, 6, "Railers", "Worcester Railers", "Worcester", "MA", "USA", "United States", "Worcester, MA", "Massachusetts", "Worcester, Massachusetts", "DCU Center", "DCU Center, Worcester", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(7, 7, "Gladiators", "Atlanta Gladiators", "Duluth", "GA", "USA", "United States", "Duluth, GA", "Georgia", "Duluth, Georgia", "Infinite Energy Arena", "Infinite Energy Arena, Duluth", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(8, 8, "Everblades", "Florida Everblades", "Estero", "FL", "USA", "United States", "Estero, FL", "Florida", "Estero, Florida", "Germain Arena", "Germain Arena, Estero", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(9, 9, "Swamp Rabbits", "Greenville Swamp Rabbits", "Greenville", "SC", "USA", "United States", "Greenville, SC", "South Carolina", "Greenville, South Carolina", "Bon Secours Wellness Arena", "Bon Secours Wellness Arena, Greenville", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(10, 10, "Icemen", "Jacksonville Icemen", "Jacksonville", "FL", "USA", "United States", "Jacksonville, FL", "Florida", "Jacksonville, Florida", "Jacksonville Veterans Memorial Arena", "Jacksonville Veterans Memorial Arena, Jacksonville", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(11, 11, "Admirals", "Norfolk Admirals", "Norfolk", "VA", "USA", "United States", "Norfolk, VA", "Virginia", "Norfolk, Virginia", "Norfolk Scope", "Norfolk Scope, Norfolk", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(12, 12, "Solar Bears", "Orlando Solar Bears", "Orlando", "FL", "USA", "United States", "Orlando, FL", "Florida", "Orlando, Florida", "Amway Center", "Amway Center, Orlando", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(13, 13, "Stingrays", "South Carolina Stingrays", "North Charleston", "SC", "USA", "United States", "North Charleston, SC", "South Carolina", "North Charleston, South Carolina", "North Charleston Coliseum", "North Charleston Coliseum, North Charleston", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(14, 14, "Cyclones", "Cincinnati Cyclones", "Cincinnati", "OH", "USA", "United States", "Cincinnati, OH", "Ohio", "Cincinnati, Ohio", "US Bank Arena", "US Bank Arena, Cincinnati", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(15, 15, "Komets", "Fort Wayne Komets", "Fort Wayne", "IN", "USA", "United States", "Fort Wayne, IN", "Indiana", "Fort Wayne, Indiana", "Allen County War Memorial Coliseum", "Allen County War Memorial Coliseum, Fort Wayne", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(16, 16, "Fuel", "Indy Fuel", "Indianapolis", "IN", "USA", "United States", "Indianapolis, IN", "Indiana", "Indianapolis, Indiana", "Indiana Farmers Coliseum", "Indiana Farmers Coliseum, Indianapolis", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(17, 17, "Wings", "Kalamazoo Wings", "Kalamazoo", "MI", "USA", "United States", "Kalamazoo, MI", "Michigan", "Kalamazoo, Michigan", "Wings Event Center", "Wings Event Center, Kalamazoo", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(18, 18, "Mavericks", "Kansas City Mavericks", "Independence", "MO", "USA", "United States", "Independence, MO", "Missouri", "Independence, Missouri", "Silverstein Eye Centers Arena", "Silverstein Eye Centers Arena, Independence", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(19, 19, "Mallards", "Quad City Mallards", "Moline", "IL", "USA", "United States", "Moline, IL", "Illinois", "Moline, Illinois", "TaxSlayer Center", "TaxSlayer Center, Moline", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(20, 20, "Walleye", "Toledo Walleye", "Toledo", "OH", "USA", "United States", "Toledo, OH", "Ohio", "Toledo, Ohio", "Huntington Center", "Huntington Center, Toledo", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(21, 21, "Americans", "Allen Americans", "Allen", "TX", "USA", "United States", "Allen, TX", "Texas", "Allen, Texas", "Allen Event Center", "Allen Event Center, Allen", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(22, 22, "Eagles", "Colorado Eagles", "Loveland", "CO", "USA", "United States", "Loveland, CO", "Colorado", "Loveland, Colorado", "Budweiser Events Center", "Budweiser Events Center, Loveland", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(23, 23, "Steelheads", "Idaho Steelheads", "Boise", "ID", "USA", "United States", "Boise, ID", "Idaho", "Boise, Idaho", "CenturyLink Arena", "CenturyLink Arena, Boise", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(24, 24, "Rush", "Rapid City Rush", "Rapid City", "SD", "USA", "United States", "Rapid City, SD", "South Dakota", "Rapid City, South Dakota", "Rushmore Plaza Civic Center", "Rushmore Plaza Civic Center, Rapid City", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(25, 25, "Oilers", "Tulsa Oilers", "Tulsa", "OK", "USA", "United States", "Tulsa, OK", "Oklahoma", "Tulsa, Oklahoma", "BOK Center", "BOK Center, Tulsa", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(26, 26, "Grizzlies", "Utah Grizzlies", "West Valley City", "UT", "USA", "United States", "West Valley City, UT", "Utah", "West Valley City, Utah", "Maverik Center", "Maverik Center, West Valley City", 0);
INSERT INTO ECHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(27, 27, "Thunder", "Wichita Thunder", "Wichita", "KS", "USA", "United States", "Wichita, KS", "Kansas", "Wichita, Kansas", "Intrust Bank Arena", "Intrust Bank Arena, Wichita", 0);

-- --------------------------------------------------------

--
-- Table structure for table ECHLTeams
--

CREATE TABLE ECHLTeams (
  id INTEGER PRIMARY KEY,
  Date INTEGER,
  FullName TEXT,
  CityName TEXT,
  TeamPrefix TEXT,
  TeamSuffix TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  TeamName TEXT,
  Conference TEXT,
  Division TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GamesPlayed INTEGER,
  GamesPlayedHome INTEGER,
  GamesPlayedAway INTEGER,
  Ties INTEGER,
  Wins INTEGER,
  OTWins INTEGER,
  SOWins INTEGER,
  OTSOWins INTEGER,
  TWins INTEGER,
  Losses INTEGER,
  OTLosses INTEGER,
  SOLosses INTEGER,
  OTSOLosses INTEGER,
  TLosses INTEGER,
  ROW INTEGER,
  ROT INTEGER,
  ShutoutWins INTEGER,
  ShutoutLosses INTEGER,
  HomeRecord TEXT,
  AwayRecord TEXT,
  Shootouts TEXT,
  GoalsFor INTEGER,
  GoalsAgainst INTEGER,
  GoalsDifference INTEGER,
  SOGFor INTEGER,
  SOGAgainst INTEGER,
  SOGDifference INTEGER,
  ShotsBlockedFor INTEGER,
  ShotsBlockedAgainst INTEGER,
  ShotsBlockedDifference INTEGER,
  PPGFor INTEGER,
  PPGAgainst INTEGER,
  PPGDifference INTEGER,
  SHGFor INTEGER,
  SHGAgainst INTEGER,
  SHGDifference INTEGER,
  PenaltiesFor INTEGER,
  PenaltiesAgainst INTEGER,
  PenaltiesDifference INTEGER,
  PIMFor INTEGER,
  PIMAgainst INTEGER,
  PIMDifference INTEGER,
  HITSFor INTEGER,
  HITSAgainst INTEGER,
  HITSDifference INTEGER,
  TakeAways INTEGER,
  GiveAways INTEGER,
  TAGADifference INTEGER,
  FaceoffWins INTEGER,
  FaceoffLosses INTEGER,
  FaceoffDifference INTEGER,
  Points INTEGER,
  PCT REAL,
  LastTen TEXT,
  Streak TEXT
);

--
-- Dumping data for table ECHLTeams
--

INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(1, 20171001, "Adirondack Thunder", "Glens Falls", "Adirondack", "", "NY", "USA", "United States", "Glens Falls, NY", "New York", "Glens Falls, New York", "Thunder", "Eastern", "North", "ECHL", "ECHL", "Cool Insuring Arena", "Cool Insuring Arena, Glens Falls", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(2, 20171001, "Brampton Beast", "Brampton", "Brampton", "", "ON", "CAN", "Canada", "Brampton, ON", "Ontario", "Brampton, Ontario", "Beast", "Eastern", "North", "ECHL", "ECHL", "Powerade Centre", "Powerade Centre, Brampton", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(3, 20171001, "Manchester Monarchs", "Manchester", "Manchester", "", "NH", "USA", "United States", "Manchester, NH", "New Hampshire", "Manchester, New Hampshire", "Monarchs", "Eastern", "North", "ECHL", "ECHL", "SNHU Arena", "SNHU Arena, Manchester", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(4, 20171001, "Reading Royals", "Reading", "Reading", "", "PA", "USA", "United States", "Reading, PA", "Pennsylvania", "Reading, Pennsylvania", "Royals", "Eastern", "North", "ECHL", "ECHL", "Santander Arena", "Santander Arena, Reading", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(5, 20171001, "Wheeling Nailers", "Wheeling", "Wheeling", "", "WV", "USA", "United States", "Wheeling, WV", "West Virginia", "Wheeling, West Virginia", "Nailers", "Eastern", "North", "ECHL", "ECHL", "WesBanco Arena", "WesBanco Arena, Wheeling", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(6, 20171001, "Worcester Railers", "Worcester", "Worcester", "", "MA", "USA", "United States", "Worcester, MA", "Massachusetts", "Worcester, Massachusetts", "Railers", "Eastern", "North", "ECHL", "ECHL", "DCU Center", "DCU Center, Worcester", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(7, 20171001, "Atlanta Gladiators", "Duluth", "Atlanta", "", "GA", "USA", "United States", "Duluth, GA", "Georgia", "Duluth, Georgia", "Gladiators", "Eastern", "South", "ECHL", "ECHL", "Infinite Energy Arena", "Infinite Energy Arena, Duluth", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(8, 20171001, "Florida Everblades", "Estero", "Florida", "", "FL", "USA", "United States", "Estero, FL", "Florida", "Estero, Florida", "Everblades", "Eastern", "South", "ECHL", "ECHL", "Germain Arena", "Germain Arena, Estero", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(9, 20171001, "Greenville Swamp Rabbits", "Greenville", "Greenville", "", "SC", "USA", "United States", "Greenville, SC", "South Carolina", "Greenville, South Carolina", "Swamp Rabbits", "Eastern", "South", "ECHL", "ECHL", "Bon Secours Wellness Arena", "Bon Secours Wellness Arena, Greenville", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(10, 20171001, "Jacksonville Icemen", "Jacksonville", "Jacksonville", "", "FL", "USA", "United States", "Jacksonville, FL", "Florida", "Jacksonville, Florida", "Icemen", "Eastern", "South", "ECHL", "ECHL", "Jacksonville Veterans Memorial Arena", "Jacksonville Veterans Memorial Arena, Jacksonville", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(11, 20171001, "Norfolk Admirals", "Norfolk", "Norfolk", "", "VA", "USA", "United States", "Norfolk, VA", "Virginia", "Norfolk, Virginia", "Admirals", "Eastern", "South", "ECHL", "ECHL", "Norfolk Scope", "Norfolk Scope, Norfolk", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(12, 20171001, "Orlando Solar Bears", "Orlando", "Orlando", "", "FL", "USA", "United States", "Orlando, FL", "Florida", "Orlando, Florida", "Solar Bears", "Eastern", "South", "ECHL", "ECHL", "Amway Center", "Amway Center, Orlando", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(13, 20171001, "South Carolina Stingrays", "North Charleston", "South Carolina", "", "SC", "USA", "United States", "North Charleston, SC", "South Carolina", "North Charleston, South Carolina", "Stingrays", "Eastern", "South", "ECHL", "ECHL", "North Charleston Coliseum", "North Charleston Coliseum, North Charleston", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(14, 20171001, "Cincinnati Cyclones", "Cincinnati", "Cincinnati", "", "OH", "USA", "United States", "Cincinnati, OH", "Ohio", "Cincinnati, Ohio", "Cyclones", "Western", "Central", "ECHL", "ECHL", "US Bank Arena", "US Bank Arena, Cincinnati", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(15, 20171001, "Fort Wayne Komets", "Fort Wayne", "Fort Wayne", "", "IN", "USA", "United States", "Fort Wayne, IN", "Indiana", "Fort Wayne, Indiana", "Komets", "Western", "Central", "ECHL", "ECHL", "Allen County War Memorial Coliseum", "Allen County War Memorial Coliseum, Fort Wayne", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(16, 20171001, "Indy Fuel", "Indianapolis", "Indy", "", "IN", "USA", "United States", "Indianapolis, IN", "Indiana", "Indianapolis, Indiana", "Fuel", "Western", "Central", "ECHL", "ECHL", "Indiana Farmers Coliseum", "Indiana Farmers Coliseum, Indianapolis", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(17, 20171001, "Kalamazoo Wings", "Kalamazoo", "Kalamazoo", "", "MI", "USA", "United States", "Kalamazoo, MI", "Michigan", "Kalamazoo, Michigan", "Wings", "Western", "Central", "ECHL", "ECHL", "Wings Event Center", "Wings Event Center, Kalamazoo", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(18, 20171001, "Kansas City Mavericks", "Independence", "Kansas City", "", "MO", "USA", "United States", "Independence, MO", "Missouri", "Independence, Missouri", "Mavericks", "Western", "Central", "ECHL", "ECHL", "Silverstein Eye Centers Arena", "Silverstein Eye Centers Arena, Independence", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(19, 20171001, "Quad City Mallards", "Moline", "Quad City", "", "IL", "USA", "United States", "Moline, IL", "Illinois", "Moline, Illinois", "Mallards", "Western", "Central", "ECHL", "ECHL", "TaxSlayer Center", "TaxSlayer Center, Moline", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(20, 20171001, "Toledo Walleye", "Toledo", "Toledo", "", "OH", "USA", "United States", "Toledo, OH", "Ohio", "Toledo, Ohio", "Walleye", "Western", "Central", "ECHL", "ECHL", "Huntington Center", "Huntington Center, Toledo", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(21, 20171001, "Allen Americans", "Allen", "Allen", "", "TX", "USA", "United States", "Allen, TX", "Texas", "Allen, Texas", "Americans", "Western", "Mountain", "ECHL", "ECHL", "Allen Event Center", "Allen Event Center, Allen", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(22, 20171001, "Colorado Eagles", "Loveland", "Colorado", "", "CO", "USA", "United States", "Loveland, CO", "Colorado", "Loveland, Colorado", "Eagles", "Western", "Mountain", "ECHL", "ECHL", "Budweiser Events Center", "Budweiser Events Center, Loveland", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(23, 20171001, "Idaho Steelheads", "Boise", "Idaho", "", "ID", "USA", "United States", "Boise, ID", "Idaho", "Boise, Idaho", "Steelheads", "Western", "Mountain", "ECHL", "ECHL", "CenturyLink Arena", "CenturyLink Arena, Boise", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(24, 20171001, "Rapid City Rush", "Rapid City", "Rapid City", "", "SD", "USA", "United States", "Rapid City, SD", "South Dakota", "Rapid City, South Dakota", "Rush", "Western", "Mountain", "ECHL", "ECHL", "Rushmore Plaza Civic Center", "Rushmore Plaza Civic Center, Rapid City", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(25, 20171001, "Tulsa Oilers", "Tulsa", "Tulsa", "", "OK", "USA", "United States", "Tulsa, OK", "Oklahoma", "Tulsa, Oklahoma", "Oilers", "Western", "Mountain", "ECHL", "ECHL", "BOK Center", "BOK Center, Tulsa", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(26, 20171001, "Utah Grizzlies", "West Valley City", "Utah", "", "UT", "USA", "United States", "West Valley City, UT", "Utah", "West Valley City, Utah", "Grizzlies", "Western", "Mountain", "ECHL", "ECHL", "Maverik Center", "Maverik Center, West Valley City", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(27, 20171001, "Wichita Thunder", "Wichita", "Wichita", "", "KS", "USA", "United States", "Wichita, KS", "Kansas", "Wichita, Kansas", "Thunder", "Western", "Mountain", "ECHL", "ECHL", "Intrust Bank Arena", "Intrust Bank Arena, Wichita", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");

-- --------------------------------------------------------

--
-- Table structure for table ECHLStats
--

CREATE TABLE ECHLStats (
  id INTEGER PRIMARY KEY,
  TeamID INTEGER,
  Date INTEGER,
  FullName TEXT,
  CityName TEXT,
  TeamPrefix TEXT,
  TeamSuffix TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  TeamName TEXT,
  Conference TEXT,
  Division TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GamesPlayed INTEGER,
  GamesPlayedHome INTEGER,
  GamesPlayedAway INTEGER,
  Ties INTEGER,
  Wins INTEGER,
  OTWins INTEGER,
  SOWins INTEGER,
  OTSOWins INTEGER,
  TWins INTEGER,
  Losses INTEGER,
  OTLosses INTEGER,
  SOLosses INTEGER,
  OTSOLosses INTEGER,
  TLosses INTEGER,
  ROW INTEGER,
  ROT INTEGER,
  ShutoutWins INTEGER,
  ShutoutLosses INTEGER,
  HomeRecord TEXT,
  AwayRecord TEXT,
  Shootouts TEXT,
  GoalsFor INTEGER,
  GoalsAgainst INTEGER,
  GoalsDifference INTEGER,
  SOGFor INTEGER,
  SOGAgainst INTEGER,
  SOGDifference INTEGER,
  ShotsBlockedFor INTEGER,
  ShotsBlockedAgainst INTEGER,
  ShotsBlockedDifference INTEGER,
  PPGFor INTEGER,
  PPGAgainst INTEGER,
  PPGDifference INTEGER,
  SHGFor INTEGER,
  SHGAgainst INTEGER,
  SHGDifference INTEGER,
  PenaltiesFor INTEGER,
  PenaltiesAgainst INTEGER,
  PenaltiesDifference INTEGER,
  PIMFor INTEGER,
  PIMAgainst INTEGER,
  PIMDifference INTEGER,
  HITSFor INTEGER,
  HITSAgainst INTEGER,
  HITSDifference INTEGER,
  TakeAways INTEGER,
  GiveAways INTEGER,
  TAGADifference INTEGER,
  FaceoffWins INTEGER,
  FaceoffLosses INTEGER,
  FaceoffDifference INTEGER,
  Points INTEGER,
  PCT REAL,
  LastTen TEXT,
  Streak TEXT,
  FOREIGN KEY(TeamID) REFERENCES ECHLTeams(id)
);

--
-- Dumping data for table ECHLStats
--

INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(1, 1, 20171001, "Adirondack Thunder", "Glens Falls", "Adirondack", "", "NY", "USA", "United States", "Glens Falls, NY", "New York", "Glens Falls, New York", "Thunder", "Eastern", "North", "ECHL", "ECHL", "Cool Insuring Arena", "Cool Insuring Arena, Glens Falls", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(2, 2, 20171001, "Brampton Beast", "Brampton", "Brampton", "", "ON", "CAN", "Canada", "Brampton, ON", "Ontario", "Brampton, Ontario", "Beast", "Eastern", "North", "ECHL", "ECHL", "Powerade Centre", "Powerade Centre, Brampton", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(3, 3, 20171001, "Manchester Monarchs", "Manchester", "Manchester", "", "NH", "USA", "United States", "Manchester, NH", "New Hampshire", "Manchester, New Hampshire", "Monarchs", "Eastern", "North", "ECHL", "ECHL", "SNHU Arena", "SNHU Arena, Manchester", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(4, 4, 20171001, "Reading Royals", "Reading", "Reading", "", "PA", "USA", "United States", "Reading, PA", "Pennsylvania", "Reading, Pennsylvania", "Royals", "Eastern", "North", "ECHL", "ECHL", "Santander Arena", "Santander Arena, Reading", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(5, 5, 20171001, "Wheeling Nailers", "Wheeling", "Wheeling", "", "WV", "USA", "United States", "Wheeling, WV", "West Virginia", "Wheeling, West Virginia", "Nailers", "Eastern", "North", "ECHL", "ECHL", "WesBanco Arena", "WesBanco Arena, Wheeling", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(6, 6, 20171001, "Worcester Railers", "Worcester", "Worcester", "", "MA", "USA", "United States", "Worcester, MA", "Massachusetts", "Worcester, Massachusetts", "Railers", "Eastern", "North", "ECHL", "ECHL", "DCU Center", "DCU Center, Worcester", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(7, 7, 20171001, "Atlanta Gladiators", "Duluth", "Atlanta", "", "GA", "USA", "United States", "Duluth, GA", "Georgia", "Duluth, Georgia", "Gladiators", "Eastern", "South", "ECHL", "ECHL", "Infinite Energy Arena", "Infinite Energy Arena, Duluth", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(8, 8, 20171001, "Florida Everblades", "Estero", "Florida", "", "FL", "USA", "United States", "Estero, FL", "Florida", "Estero, Florida", "Everblades", "Eastern", "South", "ECHL", "ECHL", "Germain Arena", "Germain Arena, Estero", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(9, 9, 20171001, "Greenville Swamp Rabbits", "Greenville", "Greenville", "", "SC", "USA", "United States", "Greenville, SC", "South Carolina", "Greenville, South Carolina", "Swamp Rabbits", "Eastern", "South", "ECHL", "ECHL", "Bon Secours Wellness Arena", "Bon Secours Wellness Arena, Greenville", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(10, 10, 20171001, "Jacksonville Icemen", "Jacksonville", "Jacksonville", "", "FL", "USA", "United States", "Jacksonville, FL", "Florida", "Jacksonville, Florida", "Icemen", "Eastern", "South", "ECHL", "ECHL", "Jacksonville Veterans Memorial Arena", "Jacksonville Veterans Memorial Arena, Jacksonville", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(11, 11, 20171001, "Norfolk Admirals", "Norfolk", "Norfolk", "", "VA", "USA", "United States", "Norfolk, VA", "Virginia", "Norfolk, Virginia", "Admirals", "Eastern", "South", "ECHL", "ECHL", "Norfolk Scope", "Norfolk Scope, Norfolk", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(12, 12, 20171001, "Orlando Solar Bears", "Orlando", "Orlando", "", "FL", "USA", "United States", "Orlando, FL", "Florida", "Orlando, Florida", "Solar Bears", "Eastern", "South", "ECHL", "ECHL", "Amway Center", "Amway Center, Orlando", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(13, 13, 20171001, "South Carolina Stingrays", "North Charleston", "South Carolina", "", "SC", "USA", "United States", "North Charleston, SC", "South Carolina", "North Charleston, South Carolina", "Stingrays", "Eastern", "South", "ECHL", "ECHL", "North Charleston Coliseum", "North Charleston Coliseum, North Charleston", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(14, 14, 20171001, "Cincinnati Cyclones", "Cincinnati", "Cincinnati", "", "OH", "USA", "United States", "Cincinnati, OH", "Ohio", "Cincinnati, Ohio", "Cyclones", "Western", "Central", "ECHL", "ECHL", "US Bank Arena", "US Bank Arena, Cincinnati", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(15, 15, 20171001, "Fort Wayne Komets", "Fort Wayne", "Fort Wayne", "", "IN", "USA", "United States", "Fort Wayne, IN", "Indiana", "Fort Wayne, Indiana", "Komets", "Western", "Central", "ECHL", "ECHL", "Allen County War Memorial Coliseum", "Allen County War Memorial Coliseum, Fort Wayne", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(16, 16, 20171001, "Indy Fuel", "Indianapolis", "Indy", "", "IN", "USA", "United States", "Indianapolis, IN", "Indiana", "Indianapolis, Indiana", "Fuel", "Western", "Central", "ECHL", "ECHL", "Indiana Farmers Coliseum", "Indiana Farmers Coliseum, Indianapolis", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(17, 17, 20171001, "Kalamazoo Wings", "Kalamazoo", "Kalamazoo", "", "MI", "USA", "United States", "Kalamazoo, MI", "Michigan", "Kalamazoo, Michigan", "Wings", "Western", "Central", "ECHL", "ECHL", "Wings Event Center", "Wings Event Center, Kalamazoo", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(18, 18, 20171001, "Kansas City Mavericks", "Independence", "Kansas City", "", "MO", "USA", "United States", "Independence, MO", "Missouri", "Independence, Missouri", "Mavericks", "Western", "Central", "ECHL", "ECHL", "Silverstein Eye Centers Arena", "Silverstein Eye Centers Arena, Independence", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(19, 19, 20171001, "Quad City Mallards", "Moline", "Quad City", "", "IL", "USA", "United States", "Moline, IL", "Illinois", "Moline, Illinois", "Mallards", "Western", "Central", "ECHL", "ECHL", "TaxSlayer Center", "TaxSlayer Center, Moline", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(20, 20, 20171001, "Toledo Walleye", "Toledo", "Toledo", "", "OH", "USA", "United States", "Toledo, OH", "Ohio", "Toledo, Ohio", "Walleye", "Western", "Central", "ECHL", "ECHL", "Huntington Center", "Huntington Center, Toledo", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(21, 21, 20171001, "Allen Americans", "Allen", "Allen", "", "TX", "USA", "United States", "Allen, TX", "Texas", "Allen, Texas", "Americans", "Western", "Mountain", "ECHL", "ECHL", "Allen Event Center", "Allen Event Center, Allen", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(22, 22, 20171001, "Colorado Eagles", "Loveland", "Colorado", "", "CO", "USA", "United States", "Loveland, CO", "Colorado", "Loveland, Colorado", "Eagles", "Western", "Mountain", "ECHL", "ECHL", "Budweiser Events Center", "Budweiser Events Center, Loveland", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(23, 23, 20171001, "Idaho Steelheads", "Boise", "Idaho", "", "ID", "USA", "United States", "Boise, ID", "Idaho", "Boise, Idaho", "Steelheads", "Western", "Mountain", "ECHL", "ECHL", "CenturyLink Arena", "CenturyLink Arena, Boise", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(24, 24, 20171001, "Rapid City Rush", "Rapid City", "Rapid City", "", "SD", "USA", "United States", "Rapid City, SD", "South Dakota", "Rapid City, South Dakota", "Rush", "Western", "Mountain", "ECHL", "ECHL", "Rushmore Plaza Civic Center", "Rushmore Plaza Civic Center, Rapid City", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(25, 25, 20171001, "Tulsa Oilers", "Tulsa", "Tulsa", "", "OK", "USA", "United States", "Tulsa, OK", "Oklahoma", "Tulsa, Oklahoma", "Oilers", "Western", "Mountain", "ECHL", "ECHL", "BOK Center", "BOK Center, Tulsa", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(26, 26, 20171001, "Utah Grizzlies", "West Valley City", "Utah", "", "UT", "USA", "United States", "West Valley City, UT", "Utah", "West Valley City, Utah", "Grizzlies", "Western", "Mountain", "ECHL", "ECHL", "Maverik Center", "Maverik Center, West Valley City", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO ECHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(27, 27, 20171001, "Wichita Thunder", "Wichita", "Wichita", "", "KS", "USA", "United States", "Wichita, KS", "Kansas", "Wichita, Kansas", "Thunder", "Western", "Mountain", "ECHL", "ECHL", "Intrust Bank Arena", "Intrust Bank Arena, Wichita", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");

-- --------------------------------------------------------

--
-- Table structure for table ECHLGameStats
--

CREATE TABLE ECHLGameStats (
  id INTEGER PRIMARY KEY,
  GameID INTEGER,
  Date INTEGER,
  TeamID INTEGER,
  FullName TEXT,
  CityName TEXT,
  TeamPrefix TEXT,
  TeamSuffix TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  TeamName TEXT,
  Conference TEXT,
  Division TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GoalsFor INTEGER,
  GoalsAgainst INTEGER,
  GoalsDifference INTEGER,
  SOGFor INTEGER,
  SOGAgainst INTEGER,
  SOGDifference INTEGER,
  ShotsBlockedFor INTEGER,
  ShotsBlockedAgainst INTEGER,
  ShotsBlockedDifference INTEGER,
  PPGFor INTEGER,
  PPGAgainst INTEGER,
  PPGDifference INTEGER,
  SHGFor INTEGER,
  SHGAgainst INTEGER,
  SHGDifference INTEGER,
  PenaltiesFor INTEGER,
  PenaltiesAgainst INTEGER,
  PenaltiesDifference INTEGER,
  PIMFor INTEGER,
  PIMAgainst INTEGER,
  PIMDifference INTEGER,
  HITSFor INTEGER,
  HITSAgainst INTEGER,
  HITSDifference INTEGER,
  TakeAways INTEGER,
  GiveAways INTEGER,
  TAGADifference INTEGER,
  FaceoffWins INTEGER,
  FaceoffLosses INTEGER,
  FaceoffDifference INTEGER,
  FOREIGN KEY(GameID) REFERENCES ECHLGames(id),
  FOREIGN KEY(TeamID) REFERENCES ECHLTeams(id)
);

--
-- Dumping data for table ECHLGameStats
--


-- --------------------------------------------------------

--
-- Table structure for table ECHLGames
--

CREATE TABLE ECHLGames (
  id INTEGER PRIMARY KEY,
  Date INTEGER,
  HomeTeam TEXT,
  AwayTeam TEXT,
  AtArena TEXT,
  TeamScorePeriods TEXT,
  TeamFullScore TEXT,
  ShotsOnGoal TEXT,
  FullShotsOnGoal TEXT,
  ShotsBlocked TEXT,
  FullShotsBlocked TEXT,
  PowerPlays TEXT,
  FullPowerPlays TEXT,
  ShortHanded TEXT,
  FullShortHanded TEXT,
  Penalties TEXT,
  FullPenalties TEXT,
  PenaltyMinutes TEXT,
  FullPenaltyMinutes TEXT,
  HitsPerPeriod TEXT,
  FullHitsPerPeriod TEXT,
  TakeAways TEXT,
  FullTakeAways TEXT,
  GiveAways TEXT,
  FullGiveAways TEXT,
  FaceoffWins TEXT,
  FullFaceoffWins TEXT,
  NumberPeriods INTEGER,
  TeamWin TEXT,
  TeamLost TEXT,
  TieGame INTEGER,
  IsPlayOffGame INTEGER
);

--
-- Dumping data for table ECHLGames
--


-- --------------------------------------------------------

--
-- Table structure for table FHLConferences
--

CREATE TABLE FHLConferences (
  id INTEGER PRIMARY KEY,
  Conference TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  NumberOfTeams INTEGER,
  NumberOfDivisions INTEGER
);

--
-- Dumping data for table FHLConferences
--

INSERT INTO FHLConferences (id, Conference, LeagueName, LeagueFullName, NumberOfTeams, NumberOfDivisions) VALUES 
(1, "", "FHL", "Federal Hockey League", 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table FHLDivisions
--

CREATE TABLE FHLDivisions (
  id INTEGER PRIMARY KEY,
  Division TEXT,
  Conference TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  NumberOfTeams INTEGER
);

--
-- Dumping data for table FHLDivisions
--

INSERT INTO FHLDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(1, "", "", "FHL", "Federal Hockey League", 0);

-- --------------------------------------------------------

--
-- Table structure for table FHLArenas
--

CREATE TABLE FHLArenas (
  id INTEGER PRIMARY KEY,
  TeamID INTEGER,
  TeamName TEXT,
  TeamFullName TEXT,
  CityName TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GamesPlayed INTEGER,
  FOREIGN KEY(TeamID) REFERENCES FHLTeams(id)
);

--
-- Dumping data for table FHLArenas
--

INSERT INTO FHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(1, 1, "Thunderbirds", "Carolina Thunderbirds", "Winston-Salem", "NC", "USA", "United States", "Winston-Salem, NC", "North Carolina", "Winston-Salem, North Carolina", "Winston-Salem Fairgrounds Annex", "Winston-Salem Fairgrounds Annex, Winston-Salem", 0);
INSERT INTO FHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(2, 2, "Nationals", "Cornwall Nationals", "Cornwall", "ON", "CAN", "Canada", "Cornwall, ON", "Ontario", "Cornwall, Ontario", "Ed Lumley Arena", "Ed Lumley Arena, Cornwall", 0);
INSERT INTO FHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(3, 3, "Dashers", "Danville Dashers", "Danville", "IL", "USA", "United States", "Danville, IL", "Illinois", "Danville, Illinois", "David S. Palmer Arena", "David S. Palmer Arena, Danville", 0);
INSERT INTO FHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(4, 4, "Knights", "North Shore Knights", "Kingsville", "ON", "CAN", "Canada", "Kingsville, ON", "Ontario", "Kingsville, Ontario", "Kingsville Arena Complex", "Kingsville Arena Complex, Kingsville", 0);
INSERT INTO FHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(5, 5, "Prowlers", "Port Huron Prowlers", "Port Huron", "MI", "USA", "United States", "Port Huron, MI", "Michigan", "Port Huron, Michigan", "McMorran Place", "McMorran Place, Port Huron", 0);
INSERT INTO FHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(6, 6, "Wolves", "Watertown Wolves", "Watertown", "NY", "USA", "United States", "Watertown, NY", "New York", "Watertown, New York", "Watertown Municipal Arena", "Watertown Municipal Arena, Watertown", 0);

-- --------------------------------------------------------

--
-- Table structure for table FHLTeams
--

CREATE TABLE FHLTeams (
  id INTEGER PRIMARY KEY,
  Date INTEGER,
  FullName TEXT,
  CityName TEXT,
  TeamPrefix TEXT,
  TeamSuffix TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  TeamName TEXT,
  Conference TEXT,
  Division TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GamesPlayed INTEGER,
  GamesPlayedHome INTEGER,
  GamesPlayedAway INTEGER,
  Ties INTEGER,
  Wins INTEGER,
  OTWins INTEGER,
  SOWins INTEGER,
  OTSOWins INTEGER,
  TWins INTEGER,
  Losses INTEGER,
  OTLosses INTEGER,
  SOLosses INTEGER,
  OTSOLosses INTEGER,
  TLosses INTEGER,
  ROW INTEGER,
  ROT INTEGER,
  ShutoutWins INTEGER,
  ShutoutLosses INTEGER,
  HomeRecord TEXT,
  AwayRecord TEXT,
  Shootouts TEXT,
  GoalsFor INTEGER,
  GoalsAgainst INTEGER,
  GoalsDifference INTEGER,
  SOGFor INTEGER,
  SOGAgainst INTEGER,
  SOGDifference INTEGER,
  ShotsBlockedFor INTEGER,
  ShotsBlockedAgainst INTEGER,
  ShotsBlockedDifference INTEGER,
  PPGFor INTEGER,
  PPGAgainst INTEGER,
  PPGDifference INTEGER,
  SHGFor INTEGER,
  SHGAgainst INTEGER,
  SHGDifference INTEGER,
  PenaltiesFor INTEGER,
  PenaltiesAgainst INTEGER,
  PenaltiesDifference INTEGER,
  PIMFor INTEGER,
  PIMAgainst INTEGER,
  PIMDifference INTEGER,
  HITSFor INTEGER,
  HITSAgainst INTEGER,
  HITSDifference INTEGER,
  TakeAways INTEGER,
  GiveAways INTEGER,
  TAGADifference INTEGER,
  FaceoffWins INTEGER,
  FaceoffLosses INTEGER,
  FaceoffDifference INTEGER,
  Points INTEGER,
  PCT REAL,
  LastTen TEXT,
  Streak TEXT
);

--
-- Dumping data for table FHLTeams
--

INSERT INTO FHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(1, 20171001, "Carolina Thunderbirds", "Winston-Salem", "Carolina", "", "NC", "USA", "United States", "Winston-Salem, NC", "North Carolina", "Winston-Salem, North Carolina", "Thunderbirds", "", "", "FHL", "Federal Hockey League", "Winston-Salem Fairgrounds Annex", "Winston-Salem Fairgrounds Annex, Winston-Salem", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO FHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(2, 20171001, "Cornwall Nationals", "Cornwall", "Cornwall", "", "ON", "CAN", "Canada", "Cornwall, ON", "Ontario", "Cornwall, Ontario", "Nationals", "", "", "FHL", "Federal Hockey League", "Ed Lumley Arena", "Ed Lumley Arena, Cornwall", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO FHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(3, 20171001, "Danville Dashers", "Danville", "Danville", "", "IL", "USA", "United States", "Danville, IL", "Illinois", "Danville, Illinois", "Dashers", "", "", "FHL", "Federal Hockey League", "David S. Palmer Arena", "David S. Palmer Arena, Danville", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO FHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(4, 20171001, "North Shore Knights", "Kingsville", "North Shore", "", "ON", "CAN", "Canada", "Kingsville, ON", "Ontario", "Kingsville, Ontario", "Knights", "", "", "FHL", "Federal Hockey League", "Kingsville Arena Complex", "Kingsville Arena Complex, Kingsville", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO FHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(5, 20171001, "Port Huron Prowlers", "Port Huron", "Port Huron", "", "MI", "USA", "United States", "Port Huron, MI", "Michigan", "Port Huron, Michigan", "Prowlers", "", "", "FHL", "Federal Hockey League", "McMorran Place", "McMorran Place, Port Huron", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO FHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(6, 20171001, "Watertown Wolves", "Watertown", "Watertown", "", "NY", "USA", "United States", "Watertown, NY", "New York", "Watertown, New York", "Wolves", "", "", "FHL", "Federal Hockey League", "Watertown Municipal Arena", "Watertown Municipal Arena, Watertown", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");

-- --------------------------------------------------------

--
-- Table structure for table FHLStats
--

CREATE TABLE FHLStats (
  id INTEGER PRIMARY KEY,
  TeamID INTEGER,
  Date INTEGER,
  FullName TEXT,
  CityName TEXT,
  TeamPrefix TEXT,
  TeamSuffix TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  TeamName TEXT,
  Conference TEXT,
  Division TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GamesPlayed INTEGER,
  GamesPlayedHome INTEGER,
  GamesPlayedAway INTEGER,
  Ties INTEGER,
  Wins INTEGER,
  OTWins INTEGER,
  SOWins INTEGER,
  OTSOWins INTEGER,
  TWins INTEGER,
  Losses INTEGER,
  OTLosses INTEGER,
  SOLosses INTEGER,
  OTSOLosses INTEGER,
  TLosses INTEGER,
  ROW INTEGER,
  ROT INTEGER,
  ShutoutWins INTEGER,
  ShutoutLosses INTEGER,
  HomeRecord TEXT,
  AwayRecord TEXT,
  Shootouts TEXT,
  GoalsFor INTEGER,
  GoalsAgainst INTEGER,
  GoalsDifference INTEGER,
  SOGFor INTEGER,
  SOGAgainst INTEGER,
  SOGDifference INTEGER,
  ShotsBlockedFor INTEGER,
  ShotsBlockedAgainst INTEGER,
  ShotsBlockedDifference INTEGER,
  PPGFor INTEGER,
  PPGAgainst INTEGER,
  PPGDifference INTEGER,
  SHGFor INTEGER,
  SHGAgainst INTEGER,
  SHGDifference INTEGER,
  PenaltiesFor INTEGER,
  PenaltiesAgainst INTEGER,
  PenaltiesDifference INTEGER,
  PIMFor INTEGER,
  PIMAgainst INTEGER,
  PIMDifference INTEGER,
  HITSFor INTEGER,
  HITSAgainst INTEGER,
  HITSDifference INTEGER,
  TakeAways INTEGER,
  GiveAways INTEGER,
  TAGADifference INTEGER,
  FaceoffWins INTEGER,
  FaceoffLosses INTEGER,
  FaceoffDifference INTEGER,
  Points INTEGER,
  PCT REAL,
  LastTen TEXT,
  Streak TEXT,
  FOREIGN KEY(TeamID) REFERENCES FHLTeams(id)
);

--
-- Dumping data for table FHLStats
--

INSERT INTO FHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(1, 1, 20171001, "Carolina Thunderbirds", "Winston-Salem", "Carolina", "", "NC", "USA", "United States", "Winston-Salem, NC", "North Carolina", "Winston-Salem, North Carolina", "Thunderbirds", "", "", "FHL", "Federal Hockey League", "Winston-Salem Fairgrounds Annex", "Winston-Salem Fairgrounds Annex, Winston-Salem", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO FHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(2, 2, 20171001, "Cornwall Nationals", "Cornwall", "Cornwall", "", "ON", "CAN", "Canada", "Cornwall, ON", "Ontario", "Cornwall, Ontario", "Nationals", "", "", "FHL", "Federal Hockey League", "Ed Lumley Arena", "Ed Lumley Arena, Cornwall", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO FHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(3, 3, 20171001, "Danville Dashers", "Danville", "Danville", "", "IL", "USA", "United States", "Danville, IL", "Illinois", "Danville, Illinois", "Dashers", "", "", "FHL", "Federal Hockey League", "David S. Palmer Arena", "David S. Palmer Arena, Danville", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO FHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(4, 4, 20171001, "North Shore Knights", "Kingsville", "North Shore", "", "ON", "CAN", "Canada", "Kingsville, ON", "Ontario", "Kingsville, Ontario", "Knights", "", "", "FHL", "Federal Hockey League", "Kingsville Arena Complex", "Kingsville Arena Complex, Kingsville", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO FHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(5, 5, 20171001, "Port Huron Prowlers", "Port Huron", "Port Huron", "", "MI", "USA", "United States", "Port Huron, MI", "Michigan", "Port Huron, Michigan", "Prowlers", "", "", "FHL", "Federal Hockey League", "McMorran Place", "McMorran Place, Port Huron", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO FHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(6, 6, 20171001, "Watertown Wolves", "Watertown", "Watertown", "", "NY", "USA", "United States", "Watertown, NY", "New York", "Watertown, New York", "Wolves", "", "", "FHL", "Federal Hockey League", "Watertown Municipal Arena", "Watertown Municipal Arena, Watertown", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");

-- --------------------------------------------------------

--
-- Table structure for table FHLGameStats
--

CREATE TABLE FHLGameStats (
  id INTEGER PRIMARY KEY,
  GameID INTEGER,
  Date INTEGER,
  TeamID INTEGER,
  FullName TEXT,
  CityName TEXT,
  TeamPrefix TEXT,
  TeamSuffix TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  TeamName TEXT,
  Conference TEXT,
  Division TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GoalsFor INTEGER,
  GoalsAgainst INTEGER,
  GoalsDifference INTEGER,
  SOGFor INTEGER,
  SOGAgainst INTEGER,
  SOGDifference INTEGER,
  ShotsBlockedFor INTEGER,
  ShotsBlockedAgainst INTEGER,
  ShotsBlockedDifference INTEGER,
  PPGFor INTEGER,
  PPGAgainst INTEGER,
  PPGDifference INTEGER,
  SHGFor INTEGER,
  SHGAgainst INTEGER,
  SHGDifference INTEGER,
  PenaltiesFor INTEGER,
  PenaltiesAgainst INTEGER,
  PenaltiesDifference INTEGER,
  PIMFor INTEGER,
  PIMAgainst INTEGER,
  PIMDifference INTEGER,
  HITSFor INTEGER,
  HITSAgainst INTEGER,
  HITSDifference INTEGER,
  TakeAways INTEGER,
  GiveAways INTEGER,
  TAGADifference INTEGER,
  FaceoffWins INTEGER,
  FaceoffLosses INTEGER,
  FaceoffDifference INTEGER,
  FOREIGN KEY(GameID) REFERENCES FHLGames(id),
  FOREIGN KEY(TeamID) REFERENCES FHLTeams(id)
);

--
-- Dumping data for table FHLGameStats
--


-- --------------------------------------------------------

--
-- Table structure for table FHLGames
--

CREATE TABLE FHLGames (
  id INTEGER PRIMARY KEY,
  Date INTEGER,
  HomeTeam TEXT,
  AwayTeam TEXT,
  AtArena TEXT,
  TeamScorePeriods TEXT,
  TeamFullScore TEXT,
  ShotsOnGoal TEXT,
  FullShotsOnGoal TEXT,
  ShotsBlocked TEXT,
  FullShotsBlocked TEXT,
  PowerPlays TEXT,
  FullPowerPlays TEXT,
  ShortHanded TEXT,
  FullShortHanded TEXT,
  Penalties TEXT,
  FullPenalties TEXT,
  PenaltyMinutes TEXT,
  FullPenaltyMinutes TEXT,
  HitsPerPeriod TEXT,
  FullHitsPerPeriod TEXT,
  TakeAways TEXT,
  FullTakeAways TEXT,
  GiveAways TEXT,
  FullGiveAways TEXT,
  FaceoffWins TEXT,
  FullFaceoffWins TEXT,
  NumberPeriods INTEGER,
  TeamWin TEXT,
  TeamLost TEXT,
  TieGame INTEGER,
  IsPlayOffGame INTEGER
);

--
-- Dumping data for table FHLGames
--


-- --------------------------------------------------------

--
-- Table structure for table SPHLConferences
--

CREATE TABLE SPHLConferences (
  id INTEGER PRIMARY KEY,
  Conference TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  NumberOfTeams INTEGER,
  NumberOfDivisions INTEGER
);

--
-- Dumping data for table SPHLConferences
--

INSERT INTO SPHLConferences (id, Conference, LeagueName, LeagueFullName, NumberOfTeams, NumberOfDivisions) VALUES 
(1, "", "SPHL", "Southern Professional Hockey League", 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table SPHLDivisions
--

CREATE TABLE SPHLDivisions (
  id INTEGER PRIMARY KEY,
  Division TEXT,
  Conference TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  NumberOfTeams INTEGER
);

--
-- Dumping data for table SPHLDivisions
--

INSERT INTO SPHLDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(1, "", "", "SPHL", "Southern Professional Hockey League", 0);

-- --------------------------------------------------------

--
-- Table structure for table SPHLArenas
--

CREATE TABLE SPHLArenas (
  id INTEGER PRIMARY KEY,
  TeamID INTEGER,
  TeamName TEXT,
  TeamFullName TEXT,
  CityName TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GamesPlayed INTEGER,
  FOREIGN KEY(TeamID) REFERENCES SPHLTeams(id)
);

--
-- Dumping data for table SPHLArenas
--

INSERT INTO SPHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(1, 1, "Bulls", "Birmingham Bulls", "Pelham", "AL", "USA", "United States", "Pelham, AL", "Alabama", "Pelham, Alabama", "Pelham Civic Center", "Pelham Civic Center, Pelham", 0);
INSERT INTO SPHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(2, 2, "Thunderbolts", "Evansville Thunderbolts", "Evansville", "IN", "USA", "United States", "Evansville, IN", "Indiana", "Evansville, Indiana", "Ford Center", "Ford Center, Evansville", 0);
INSERT INTO SPHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(3, 3, "Marksmen", "Fayetteville Marksmen", "Fayetteville", "NC", "USA", "United States", "Fayetteville, NC", "North Carolina", "Fayetteville, North Carolina", "Crown Coliseum", "Crown Coliseum, Fayetteville", 0);
INSERT INTO SPHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(4, 4, "Havoc", "Huntsville Havoc", "Huntsville", "AL", "USA", "United States", "Huntsville, AL", "Alabama", "Huntsville, Alabama", "Von Braun Center", "Von Braun Center, Huntsville", 0);
INSERT INTO SPHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(5, 5, "Ice Bears", "Knoxville Ice Bears", "Knoxville", "TN", "USA", "United States", "Knoxville, TN", "Tennessee", "Knoxville, Tennessee", "Knoxville Civic Coliseum", "Knoxville Civic Coliseum, Knoxville", 0);
INSERT INTO SPHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(6, 6, "Mayhem", "Macon Mayhem", "Macon", "GA", "USA", "United States", "Macon, GA", "Georgia", "Macon, Georgia", "Macon Coliseum", "Macon Coliseum, Macon", 0);
INSERT INTO SPHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(7, 7, "RiverKings", "Mississippi RiverKings", "Southaven", "MS", "USA", "United States", "Southaven, MS", "Mississippi", "Southaven, Mississippi", "Landers Center", "Landers Center, Southaven", 0);
INSERT INTO SPHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(8, 8, "Ice Flyers", "Pensacola Ice Flyers", "Pensacola", "FL", "USA", "United States", "Pensacola, FL", "Florida", "Pensacola, Florida", "Pensacola Bay Center", "Pensacola Bay Center, Pensacola", 0);
INSERT INTO SPHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(9, 9, "Rivermen", "Peoria Rivermen", "Peoria", "IL", "USA", "United States", "Peoria, IL", "Illinois", "Peoria, Illinois", "Carver Arena", "Carver Arena, Peoria", 0);
INSERT INTO SPHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(10, 10, "Rail Yard Dawgs", "Roanoke Rail Yard Dawgs", "Roanoke", "VA", "USA", "United States", "Roanoke, VA", "Virginia", "Roanoke, Virginia", "Berglund Center", "Berglund Center, Roanoke", 0);

-- --------------------------------------------------------

--
-- Table structure for table SPHLTeams
--

CREATE TABLE SPHLTeams (
  id INTEGER PRIMARY KEY,
  Date INTEGER,
  FullName TEXT,
  CityName TEXT,
  TeamPrefix TEXT,
  TeamSuffix TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  TeamName TEXT,
  Conference TEXT,
  Division TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GamesPlayed INTEGER,
  GamesPlayedHome INTEGER,
  GamesPlayedAway INTEGER,
  Ties INTEGER,
  Wins INTEGER,
  OTWins INTEGER,
  SOWins INTEGER,
  OTSOWins INTEGER,
  TWins INTEGER,
  Losses INTEGER,
  OTLosses INTEGER,
  SOLosses INTEGER,
  OTSOLosses INTEGER,
  TLosses INTEGER,
  ROW INTEGER,
  ROT INTEGER,
  ShutoutWins INTEGER,
  ShutoutLosses INTEGER,
  HomeRecord TEXT,
  AwayRecord TEXT,
  Shootouts TEXT,
  GoalsFor INTEGER,
  GoalsAgainst INTEGER,
  GoalsDifference INTEGER,
  SOGFor INTEGER,
  SOGAgainst INTEGER,
  SOGDifference INTEGER,
  ShotsBlockedFor INTEGER,
  ShotsBlockedAgainst INTEGER,
  ShotsBlockedDifference INTEGER,
  PPGFor INTEGER,
  PPGAgainst INTEGER,
  PPGDifference INTEGER,
  SHGFor INTEGER,
  SHGAgainst INTEGER,
  SHGDifference INTEGER,
  PenaltiesFor INTEGER,
  PenaltiesAgainst INTEGER,
  PenaltiesDifference INTEGER,
  PIMFor INTEGER,
  PIMAgainst INTEGER,
  PIMDifference INTEGER,
  HITSFor INTEGER,
  HITSAgainst INTEGER,
  HITSDifference INTEGER,
  TakeAways INTEGER,
  GiveAways INTEGER,
  TAGADifference INTEGER,
  FaceoffWins INTEGER,
  FaceoffLosses INTEGER,
  FaceoffDifference INTEGER,
  Points INTEGER,
  PCT REAL,
  LastTen TEXT,
  Streak TEXT
);

--
-- Dumping data for table SPHLTeams
--

INSERT INTO SPHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(1, 20171001, "Birmingham Bulls", "Pelham", "Birmingham", "", "AL", "USA", "United States", "Pelham, AL", "Alabama", "Pelham, Alabama", "Bulls", "", "", "SPHL", "Southern Professional Hockey League", "Pelham Civic Center", "Pelham Civic Center, Pelham", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO SPHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(2, 20171001, "Evansville Thunderbolts", "Evansville", "Evansville", "", "IN", "USA", "United States", "Evansville, IN", "Indiana", "Evansville, Indiana", "Thunderbolts", "", "", "SPHL", "Southern Professional Hockey League", "Ford Center", "Ford Center, Evansville", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO SPHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(3, 20171001, "Fayetteville Marksmen", "Fayetteville", "Fayetteville", "", "NC", "USA", "United States", "Fayetteville, NC", "North Carolina", "Fayetteville, North Carolina", "Marksmen", "", "", "SPHL", "Southern Professional Hockey League", "Crown Coliseum", "Crown Coliseum, Fayetteville", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO SPHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(4, 20171001, "Huntsville Havoc", "Huntsville", "Huntsville", "", "AL", "USA", "United States", "Huntsville, AL", "Alabama", "Huntsville, Alabama", "Havoc", "", "", "SPHL", "Southern Professional Hockey League", "Von Braun Center", "Von Braun Center, Huntsville", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO SPHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(5, 20171001, "Knoxville Ice Bears", "Knoxville", "Knoxville", "", "TN", "USA", "United States", "Knoxville, TN", "Tennessee", "Knoxville, Tennessee", "Ice Bears", "", "", "SPHL", "Southern Professional Hockey League", "Knoxville Civic Coliseum", "Knoxville Civic Coliseum, Knoxville", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO SPHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(6, 20171001, "Macon Mayhem", "Macon", "Macon", "", "GA", "USA", "United States", "Macon, GA", "Georgia", "Macon, Georgia", "Mayhem", "", "", "SPHL", "Southern Professional Hockey League", "Macon Coliseum", "Macon Coliseum, Macon", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO SPHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(7, 20171001, "Mississippi RiverKings", "Southaven", "Mississippi", "", "MS", "USA", "United States", "Southaven, MS", "Mississippi", "Southaven, Mississippi", "RiverKings", "", "", "SPHL", "Southern Professional Hockey League", "Landers Center", "Landers Center, Southaven", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO SPHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(8, 20171001, "Pensacola Ice Flyers", "Pensacola", "Pensacola", "", "FL", "USA", "United States", "Pensacola, FL", "Florida", "Pensacola, Florida", "Ice Flyers", "", "", "SPHL", "Southern Professional Hockey League", "Pensacola Bay Center", "Pensacola Bay Center, Pensacola", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO SPHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(9, 20171001, "Peoria Rivermen", "Peoria", "Peoria", "", "IL", "USA", "United States", "Peoria, IL", "Illinois", "Peoria, Illinois", "Rivermen", "", "", "SPHL", "Southern Professional Hockey League", "Carver Arena", "Carver Arena, Peoria", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO SPHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(10, 20171001, "Roanoke Rail Yard Dawgs", "Roanoke", "Roanoke", "", "VA", "USA", "United States", "Roanoke, VA", "Virginia", "Roanoke, Virginia", "Rail Yard Dawgs", "", "", "SPHL", "Southern Professional Hockey League", "Berglund Center", "Berglund Center, Roanoke", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");

-- --------------------------------------------------------

--
-- Table structure for table SPHLStats
--

CREATE TABLE SPHLStats (
  id INTEGER PRIMARY KEY,
  TeamID INTEGER,
  Date INTEGER,
  FullName TEXT,
  CityName TEXT,
  TeamPrefix TEXT,
  TeamSuffix TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  TeamName TEXT,
  Conference TEXT,
  Division TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GamesPlayed INTEGER,
  GamesPlayedHome INTEGER,
  GamesPlayedAway INTEGER,
  Ties INTEGER,
  Wins INTEGER,
  OTWins INTEGER,
  SOWins INTEGER,
  OTSOWins INTEGER,
  TWins INTEGER,
  Losses INTEGER,
  OTLosses INTEGER,
  SOLosses INTEGER,
  OTSOLosses INTEGER,
  TLosses INTEGER,
  ROW INTEGER,
  ROT INTEGER,
  ShutoutWins INTEGER,
  ShutoutLosses INTEGER,
  HomeRecord TEXT,
  AwayRecord TEXT,
  Shootouts TEXT,
  GoalsFor INTEGER,
  GoalsAgainst INTEGER,
  GoalsDifference INTEGER,
  SOGFor INTEGER,
  SOGAgainst INTEGER,
  SOGDifference INTEGER,
  ShotsBlockedFor INTEGER,
  ShotsBlockedAgainst INTEGER,
  ShotsBlockedDifference INTEGER,
  PPGFor INTEGER,
  PPGAgainst INTEGER,
  PPGDifference INTEGER,
  SHGFor INTEGER,
  SHGAgainst INTEGER,
  SHGDifference INTEGER,
  PenaltiesFor INTEGER,
  PenaltiesAgainst INTEGER,
  PenaltiesDifference INTEGER,
  PIMFor INTEGER,
  PIMAgainst INTEGER,
  PIMDifference INTEGER,
  HITSFor INTEGER,
  HITSAgainst INTEGER,
  HITSDifference INTEGER,
  TakeAways INTEGER,
  GiveAways INTEGER,
  TAGADifference INTEGER,
  FaceoffWins INTEGER,
  FaceoffLosses INTEGER,
  FaceoffDifference INTEGER,
  Points INTEGER,
  PCT REAL,
  LastTen TEXT,
  Streak TEXT,
  FOREIGN KEY(TeamID) REFERENCES SPHLTeams(id)
);

--
-- Dumping data for table SPHLStats
--

INSERT INTO SPHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(1, 1, 20171001, "Birmingham Bulls", "Pelham", "Birmingham", "", "AL", "USA", "United States", "Pelham, AL", "Alabama", "Pelham, Alabama", "Bulls", "", "", "SPHL", "Southern Professional Hockey League", "Pelham Civic Center", "Pelham Civic Center, Pelham", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO SPHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(2, 2, 20171001, "Evansville Thunderbolts", "Evansville", "Evansville", "", "IN", "USA", "United States", "Evansville, IN", "Indiana", "Evansville, Indiana", "Thunderbolts", "", "", "SPHL", "Southern Professional Hockey League", "Ford Center", "Ford Center, Evansville", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO SPHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(3, 3, 20171001, "Fayetteville Marksmen", "Fayetteville", "Fayetteville", "", "NC", "USA", "United States", "Fayetteville, NC", "North Carolina", "Fayetteville, North Carolina", "Marksmen", "", "", "SPHL", "Southern Professional Hockey League", "Crown Coliseum", "Crown Coliseum, Fayetteville", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO SPHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(4, 4, 20171001, "Huntsville Havoc", "Huntsville", "Huntsville", "", "AL", "USA", "United States", "Huntsville, AL", "Alabama", "Huntsville, Alabama", "Havoc", "", "", "SPHL", "Southern Professional Hockey League", "Von Braun Center", "Von Braun Center, Huntsville", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO SPHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(5, 5, 20171001, "Knoxville Ice Bears", "Knoxville", "Knoxville", "", "TN", "USA", "United States", "Knoxville, TN", "Tennessee", "Knoxville, Tennessee", "Ice Bears", "", "", "SPHL", "Southern Professional Hockey League", "Knoxville Civic Coliseum", "Knoxville Civic Coliseum, Knoxville", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO SPHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(6, 6, 20171001, "Macon Mayhem", "Macon", "Macon", "", "GA", "USA", "United States", "Macon, GA", "Georgia", "Macon, Georgia", "Mayhem", "", "", "SPHL", "Southern Professional Hockey League", "Macon Coliseum", "Macon Coliseum, Macon", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO SPHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(7, 7, 20171001, "Mississippi RiverKings", "Southaven", "Mississippi", "", "MS", "USA", "United States", "Southaven, MS", "Mississippi", "Southaven, Mississippi", "RiverKings", "", "", "SPHL", "Southern Professional Hockey League", "Landers Center", "Landers Center, Southaven", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO SPHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(8, 8, 20171001, "Pensacola Ice Flyers", "Pensacola", "Pensacola", "", "FL", "USA", "United States", "Pensacola, FL", "Florida", "Pensacola, Florida", "Ice Flyers", "", "", "SPHL", "Southern Professional Hockey League", "Pensacola Bay Center", "Pensacola Bay Center, Pensacola", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO SPHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(9, 9, 20171001, "Peoria Rivermen", "Peoria", "Peoria", "", "IL", "USA", "United States", "Peoria, IL", "Illinois", "Peoria, Illinois", "Rivermen", "", "", "SPHL", "Southern Professional Hockey League", "Carver Arena", "Carver Arena, Peoria", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO SPHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(10, 10, 20171001, "Roanoke Rail Yard Dawgs", "Roanoke", "Roanoke", "", "VA", "USA", "United States", "Roanoke, VA", "Virginia", "Roanoke, Virginia", "Rail Yard Dawgs", "", "", "SPHL", "Southern Professional Hockey League", "Berglund Center", "Berglund Center, Roanoke", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");

-- --------------------------------------------------------

--
-- Table structure for table SPHLGameStats
--

CREATE TABLE SPHLGameStats (
  id INTEGER PRIMARY KEY,
  GameID INTEGER,
  Date INTEGER,
  TeamID INTEGER,
  FullName TEXT,
  CityName TEXT,
  TeamPrefix TEXT,
  TeamSuffix TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  TeamName TEXT,
  Conference TEXT,
  Division TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GoalsFor INTEGER,
  GoalsAgainst INTEGER,
  GoalsDifference INTEGER,
  SOGFor INTEGER,
  SOGAgainst INTEGER,
  SOGDifference INTEGER,
  ShotsBlockedFor INTEGER,
  ShotsBlockedAgainst INTEGER,
  ShotsBlockedDifference INTEGER,
  PPGFor INTEGER,
  PPGAgainst INTEGER,
  PPGDifference INTEGER,
  SHGFor INTEGER,
  SHGAgainst INTEGER,
  SHGDifference INTEGER,
  PenaltiesFor INTEGER,
  PenaltiesAgainst INTEGER,
  PenaltiesDifference INTEGER,
  PIMFor INTEGER,
  PIMAgainst INTEGER,
  PIMDifference INTEGER,
  HITSFor INTEGER,
  HITSAgainst INTEGER,
  HITSDifference INTEGER,
  TakeAways INTEGER,
  GiveAways INTEGER,
  TAGADifference INTEGER,
  FaceoffWins INTEGER,
  FaceoffLosses INTEGER,
  FaceoffDifference INTEGER,
  FOREIGN KEY(GameID) REFERENCES SPHLGames(id),
  FOREIGN KEY(TeamID) REFERENCES SPHLTeams(id)
);

--
-- Dumping data for table SPHLGameStats
--


-- --------------------------------------------------------

--
-- Table structure for table SPHLGames
--

CREATE TABLE SPHLGames (
  id INTEGER PRIMARY KEY,
  Date INTEGER,
  HomeTeam TEXT,
  AwayTeam TEXT,
  AtArena TEXT,
  TeamScorePeriods TEXT,
  TeamFullScore TEXT,
  ShotsOnGoal TEXT,
  FullShotsOnGoal TEXT,
  ShotsBlocked TEXT,
  FullShotsBlocked TEXT,
  PowerPlays TEXT,
  FullPowerPlays TEXT,
  ShortHanded TEXT,
  FullShortHanded TEXT,
  Penalties TEXT,
  FullPenalties TEXT,
  PenaltyMinutes TEXT,
  FullPenaltyMinutes TEXT,
  HitsPerPeriod TEXT,
  FullHitsPerPeriod TEXT,
  TakeAways TEXT,
  FullTakeAways TEXT,
  GiveAways TEXT,
  FullGiveAways TEXT,
  FaceoffWins TEXT,
  FullFaceoffWins TEXT,
  NumberPeriods INTEGER,
  TeamWin TEXT,
  TeamLost TEXT,
  TieGame INTEGER,
  IsPlayOffGame INTEGER
);

--
-- Dumping data for table SPHLGames
--


-- --------------------------------------------------------

--
-- Table structure for table KHLConferences
--

CREATE TABLE KHLConferences (
  id INTEGER PRIMARY KEY,
  Conference TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  NumberOfTeams INTEGER,
  NumberOfDivisions INTEGER
);

--
-- Dumping data for table KHLConferences
--

INSERT INTO KHLConferences (id, Conference, LeagueName, LeagueFullName, NumberOfTeams, NumberOfDivisions) VALUES 
(1, "Western", "KHL", "Kontinental Hockey League", 13, 2);
INSERT INTO KHLConferences (id, Conference, LeagueName, LeagueFullName, NumberOfTeams, NumberOfDivisions) VALUES 
(2, "Eastern", "KHL", "Kontinental Hockey League", 14, 2);

-- --------------------------------------------------------

--
-- Table structure for table KHLDivisions
--

CREATE TABLE KHLDivisions (
  id INTEGER PRIMARY KEY,
  Division TEXT,
  Conference TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  NumberOfTeams INTEGER
);

--
-- Dumping data for table KHLDivisions
--

INSERT INTO KHLDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(1, "Bobrov", "Western", "KHL", "Kontinental Hockey League", 6);
INSERT INTO KHLDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(2, "Tarasov", "Western", "KHL", "Kontinental Hockey League", 7);
INSERT INTO KHLDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(3, "Kharlamov", "Eastern", "KHL", "Kontinental Hockey League", 7);
INSERT INTO KHLDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(4, "Chernyshev", "Eastern", "KHL", "Kontinental Hockey League", 7);

-- --------------------------------------------------------

--
-- Table structure for table KHLArenas
--

CREATE TABLE KHLArenas (
  id INTEGER PRIMARY KEY,
  TeamID INTEGER,
  TeamName TEXT,
  TeamFullName TEXT,
  CityName TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GamesPlayed INTEGER,
  FOREIGN KEY(TeamID) REFERENCES KHLTeams(id)
);

--
-- Dumping data for table KHLArenas
--

INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(1, 1, "Dinamo Minsk", "Dinamo Minsk", "Minsk", "BY", "BLR", "Belarus", "Minsk, BY", "Belarus", "Minsk, Belarus", "Minsk-Arena", "Minsk-Arena, Minsk", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(2, 2, "Dinamo Riga", "Dinamo Riga", "Riga", "LV", "LVA", "Latvia", "Riga, LV", "Latvia", "Riga, Latvia", "Arena Riga", "Arena Riga, Riga", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(3, 3, "Jokerit Helsinki", "Jokerit Helsinki", "Helsinki", "FI", "FIN", "Finland", "Helsinki, FI", "Finland", "Helsinki, Finland", "Hartwall Arena", "Hartwall Arena, Helsinki", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(4, 4, "SKA Saint Petersburg", "SKA Saint Petersburg", "Saint Petersburg", "RU", "RUS", "Russia", "Saint Petersburg, RU", "Russia", "Saint Petersburg, Russia", "Ice Palace Saint Petersburg", "Ice Palace Saint Petersburg, Saint Petersburg", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(5, 5, "Slovan Bratislava", "Slovan Bratislava", "Bratislava", "SK", "SVK", "Slovakia", "Bratislava, SK", "Slovakia", "Bratislava, Slovakia", "Ondrej Nepela Arena", "Ondrej Nepela Arena, Bratislava", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(6, 6, "Spartak Moscow", "Spartak Moscow", "Moscow", "RU", "RUS", "Russia", "Moscow, RU", "Russia", "Moscow, Russia", "Luzhniki Minor Arena", "Luzhniki Minor Arena, Moscow", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(7, 7, "CSKA Moscow", "CSKA Moscow", "Moscow", "RU", "RUS", "Russia", "Moscow, RU", "Russia", "Moscow, Russia", "CSKA Ice Palace", "CSKA Ice Palace, Moscow", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(8, 8, "Dynamo Moscow", "Dynamo Moscow", "Moscow", "RU", "RUS", "Russia", "Moscow, RU", "Russia", "Moscow, Russia", "VTB Ice Palace", "VTB Ice Palace, Moscow", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(9, 9, "Lokomotiv Yaroslavl", "Lokomotiv Yaroslavl", "Yaroslavl", "RU", "RUS", "Russia", "Yaroslavl, RU", "Russia", "Yaroslavl, Russia", "Arena 2000", "Arena 2000, Yaroslavl", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(10, 10, "Severstal Cherepovets", "Severstal Cherepovets", "Cherepovets", "RU", "RUS", "Russia", "Cherepovets, RU", "Russia", "Cherepovets, Russia", "Ice Palace", "Ice Palace, Cherepovets", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(11, 11, "Sochi", "Sochi", "Sochi", "RU", "RUS", "Russia", "Sochi, RU", "Russia", "Sochi, Russia", "Bolshoy Ice Dome", "Bolshoy Ice Dome, Sochi", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(12, 12, "Torpedo Nizhny Novgorod", "Torpedo Nizhny Novgorod", "Nizhny Novgorod", "RU", "RUS", "Russia", "Nizhny Novgorod, RU", "Russia", "Nizhny Novgorod, Russia", "Trade Union Sport Palace", "Trade Union Sport Palace, Nizhny Novgorod", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(13, 13, "Vityaz Moscow Oblast", "Vityaz Moscow Oblast", "Podolsk", "RU", "RUS", "Russia", "Podolsk, RU", "Russia", "Podolsk, Russia", "Vityaz Ice Palace", "Vityaz Ice Palace, Podolsk", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(14, 14, "Ak Bars Kazan", "Ak Bars Kazan", "Kazan", "RU", "RUS", "Russia", "Kazan, RU", "Russia", "Kazan, Russia", "TatNeft Arena", "TatNeft Arena, Kazan", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(15, 15, "Avtomobilist Yekaterinburg", "Avtomobilist Yekaterinburg", "Yekaterinburg", "RU", "RUS", "Russia", "Yekaterinburg, RU", "Russia", "Yekaterinburg, Russia", "KRK Uralets", "KRK Uralets, Yekaterinburg", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(16, 16, "Lada Togliatti", "Lada Togliatti", "Tolyatti", "RU", "RUS", "Russia", "Tolyatti, RU", "Russia", "Tolyatti, Russia", "Lada Arena a", "Lada Arena a, Tolyatti", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(17, 17, "Metallurg Magnitogorsk", "Metallurg Magnitogorsk", "Magnitogorsk", "RU", "RUS", "Russia", "Magnitogorsk, RU", "Russia", "Magnitogorsk, Russia", "Arena Metallurg", "Arena Metallurg, Magnitogorsk", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(18, 18, "Neftekhimik Nizhnekamsk", "Neftekhimik Nizhnekamsk", "Nizhnekamsk", "RU", "RUS", "Russia", "Nizhnekamsk, RU", "Russia", "Nizhnekamsk, Russia", "SCC Arena", "SCC Arena, Nizhnekamsk", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(19, 19, "Traktor Chelyabinsk", "Traktor Chelyabinsk", "Chelyabinsk", "RU", "RUS", "Russia", "Chelyabinsk, RU", "Russia", "Chelyabinsk, Russia", "Traktor Sport Palace", "Traktor Sport Palace, Chelyabinsk", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(20, 20, "Yugra Khanty-Mansiysk", "Yugra Khanty-Mansiysk", "Khanty-Mansiysk", "RU", "RUS", "Russia", "Khanty-Mansiysk, RU", "Russia", "Khanty-Mansiysk, Russia", "Arena Ugra", "Arena Ugra, Khanty-Mansiysk", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(21, 21, "Admiral Vladivostok", "Admiral Vladivostok", "Vladivostok", "RU", "RUS", "Russia", "Vladivostok, RU", "Russia", "Vladivostok, Russia", "Fetisov Arena", "Fetisov Arena, Vladivostok", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(22, 22, "Amur Khabarovsk", "Amur Khabarovsk", "Khabarovsk", "RU", "RUS", "Russia", "Khabarovsk, RU", "Russia", "Khabarovsk, Russia", "Platinum Arena", "Platinum Arena, Khabarovsk", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(23, 23, "Avangard Omsk", "Avangard Omsk", "Omsk", "RU", "RUS", "Russia", "Omsk, RU", "Russia", "Omsk, Russia", "Omsk Arena", "Omsk Arena, Omsk", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(24, 24, "Barys Astana", "Barys Astana", "Astana", "RU", "RUS", "Kazakhstan", "Astana, RU", "Kazakhstan", "Astana, Kazakhstan", "Barys Arena", "Barys Arena, Astana", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(25, 25, "Salavat Yulaev Ufa", "Salavat Yulaev Ufa", "Ufa", "RU", "RUS", "Russia", "Ufa, RU", "Russia", "Ufa, Russia", "Ufa Arena", "Ufa Arena, Ufa", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(26, 26, "Sibir Novosibirsk", "Sibir Novosibirsk", "Novosibirsk", "RU", "RUS", "Russia", "Novosibirsk, RU", "Russia", "Novosibirsk, Russia", "Ice Sports Palace Sibir", "Ice Sports Palace Sibir, Novosibirsk", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(27, 27, "Red Star Kunlun", "Red Star Kunlun", "Beijing", "CN", "CHN", "China", "Beijing, CN", "China", "Beijing, China", "Cadillac Arena", "Cadillac Arena, Beijing", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(28, 0, "", "", "Helsinki", "FI", "FIN", "Finland", "Helsinki, FI", "Finland", "Helsinki, Finland", "Kaisaniemi Park", "Kaisaniemi Park, Helsinki", 0);
INSERT INTO KHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(29, 0, "", "", "Riga", "LV", "LVA", "Latvia", "Riga, LV", "Latvia", "Riga, Latvia", "Riga City Council Sports Complex", "Riga City Council Sports Complex, Riga", 0);

-- --------------------------------------------------------

--
-- Table structure for table KHLTeams
--

CREATE TABLE KHLTeams (
  id INTEGER PRIMARY KEY,
  Date INTEGER,
  FullName TEXT,
  CityName TEXT,
  TeamPrefix TEXT,
  TeamSuffix TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  TeamName TEXT,
  Conference TEXT,
  Division TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GamesPlayed INTEGER,
  GamesPlayedHome INTEGER,
  GamesPlayedAway INTEGER,
  Ties INTEGER,
  Wins INTEGER,
  OTWins INTEGER,
  SOWins INTEGER,
  OTSOWins INTEGER,
  TWins INTEGER,
  Losses INTEGER,
  OTLosses INTEGER,
  SOLosses INTEGER,
  OTSOLosses INTEGER,
  TLosses INTEGER,
  ROW INTEGER,
  ROT INTEGER,
  ShutoutWins INTEGER,
  ShutoutLosses INTEGER,
  HomeRecord TEXT,
  AwayRecord TEXT,
  Shootouts TEXT,
  GoalsFor INTEGER,
  GoalsAgainst INTEGER,
  GoalsDifference INTEGER,
  SOGFor INTEGER,
  SOGAgainst INTEGER,
  SOGDifference INTEGER,
  ShotsBlockedFor INTEGER,
  ShotsBlockedAgainst INTEGER,
  ShotsBlockedDifference INTEGER,
  PPGFor INTEGER,
  PPGAgainst INTEGER,
  PPGDifference INTEGER,
  SHGFor INTEGER,
  SHGAgainst INTEGER,
  SHGDifference INTEGER,
  PenaltiesFor INTEGER,
  PenaltiesAgainst INTEGER,
  PenaltiesDifference INTEGER,
  PIMFor INTEGER,
  PIMAgainst INTEGER,
  PIMDifference INTEGER,
  HITSFor INTEGER,
  HITSAgainst INTEGER,
  HITSDifference INTEGER,
  TakeAways INTEGER,
  GiveAways INTEGER,
  TAGADifference INTEGER,
  FaceoffWins INTEGER,
  FaceoffLosses INTEGER,
  FaceoffDifference INTEGER,
  Points INTEGER,
  PCT REAL,
  LastTen TEXT,
  Streak TEXT
);

--
-- Dumping data for table KHLTeams
--

INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(1, 20171001, "Dinamo Minsk", "Minsk", "", "", "BY", "BLR", "Belarus", "Minsk, BY", "Belarus", "Minsk, Belarus", "Dinamo Minsk", "Western", "Bobrov", "KHL", "Kontinental Hockey League", "Minsk-Arena", "Minsk-Arena, Minsk", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(2, 20171001, "Dinamo Riga", "Riga", "", "", "LV", "LVA", "Latvia", "Riga, LV", "Latvia", "Riga, Latvia", "Dinamo Riga", "Western", "Bobrov", "KHL", "Kontinental Hockey League", "Arena Riga", "Arena Riga, Riga", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(3, 20171001, "Jokerit Helsinki", "Helsinki", "", "", "FI", "FIN", "Finland", "Helsinki, FI", "Finland", "Helsinki, Finland", "Jokerit Helsinki", "Western", "Bobrov", "KHL", "Kontinental Hockey League", "Hartwall Arena", "Hartwall Arena, Helsinki", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(4, 20171001, "SKA Saint Petersburg", "Saint Petersburg", "", "", "RU", "RUS", "Russia", "Saint Petersburg, RU", "Russia", "Saint Petersburg, Russia", "SKA Saint Petersburg", "Western", "Bobrov", "KHL", "Kontinental Hockey League", "Ice Palace Saint Petersburg", "Ice Palace Saint Petersburg, Saint Petersburg", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(5, 20171001, "Slovan Bratislava", "Bratislava", "", "", "SK", "SVK", "Slovakia", "Bratislava, SK", "Slovakia", "Bratislava, Slovakia", "Slovan Bratislava", "Western", "Bobrov", "KHL", "Kontinental Hockey League", "Ondrej Nepela Arena", "Ondrej Nepela Arena, Bratislava", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(6, 20171001, "Spartak Moscow", "Moscow", "", "", "RU", "RUS", "Russia", "Moscow, RU", "Russia", "Moscow, Russia", "Spartak Moscow", "Western", "Bobrov", "KHL", "Kontinental Hockey League", "Luzhniki Minor Arena", "Luzhniki Minor Arena, Moscow", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(7, 20171001, "CSKA Moscow", "Moscow", "", "", "RU", "RUS", "Russia", "Moscow, RU", "Russia", "Moscow, Russia", "CSKA Moscow", "Western", "Tarasov", "KHL", "Kontinental Hockey League", "CSKA Ice Palace", "CSKA Ice Palace, Moscow", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(8, 20171001, "Dynamo Moscow", "Moscow", "", "", "RU", "RUS", "Russia", "Moscow, RU", "Russia", "Moscow, Russia", "Dynamo Moscow", "Western", "Tarasov", "KHL", "Kontinental Hockey League", "VTB Ice Palace", "VTB Ice Palace, Moscow", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(9, 20171001, "Lokomotiv Yaroslavl", "Yaroslavl", "", "", "RU", "RUS", "Russia", "Yaroslavl, RU", "Russia", "Yaroslavl, Russia", "Lokomotiv Yaroslavl", "Western", "Tarasov", "KHL", "Kontinental Hockey League", "Arena 2000", "Arena 2000, Yaroslavl", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(10, 20171001, "Severstal Cherepovets", "Cherepovets", "", "", "RU", "RUS", "Russia", "Cherepovets, RU", "Russia", "Cherepovets, Russia", "Severstal Cherepovets", "Western", "Tarasov", "KHL", "Kontinental Hockey League", "Ice Palace", "Ice Palace, Cherepovets", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(11, 20171001, "Sochi", "Sochi", "", "", "RU", "RUS", "Russia", "Sochi, RU", "Russia", "Sochi, Russia", "Sochi", "Western", "Tarasov", "KHL", "Kontinental Hockey League", "Bolshoy Ice Dome", "Bolshoy Ice Dome, Sochi", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(12, 20171001, "Torpedo Nizhny Novgorod", "Nizhny Novgorod", "", "", "RU", "RUS", "Russia", "Nizhny Novgorod, RU", "Russia", "Nizhny Novgorod, Russia", "Torpedo Nizhny Novgorod", "Western", "Tarasov", "KHL", "Kontinental Hockey League", "Trade Union Sport Palace", "Trade Union Sport Palace, Nizhny Novgorod", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(13, 20171001, "Vityaz Moscow Oblast", "Podolsk", "", "", "RU", "RUS", "Russia", "Podolsk, RU", "Russia", "Podolsk, Russia", "Vityaz Moscow Oblast", "Western", "Tarasov", "KHL", "Kontinental Hockey League", "Vityaz Ice Palace", "Vityaz Ice Palace, Podolsk", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(14, 20171001, "Ak Bars Kazan", "Kazan", "", "", "RU", "RUS", "Russia", "Kazan, RU", "Russia", "Kazan, Russia", "Ak Bars Kazan", "Eastern", "Kharlamov", "KHL", "Kontinental Hockey League", "TatNeft Arena", "TatNeft Arena, Kazan", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(15, 20171001, "Avtomobilist Yekaterinburg", "Yekaterinburg", "", "", "RU", "RUS", "Russia", "Yekaterinburg, RU", "Russia", "Yekaterinburg, Russia", "Avtomobilist Yekaterinburg", "Eastern", "Kharlamov", "KHL", "Kontinental Hockey League", "KRK Uralets", "KRK Uralets, Yekaterinburg", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(16, 20171001, "Lada Togliatti", "Tolyatti", "", "", "RU", "RUS", "Russia", "Tolyatti, RU", "Russia", "Tolyatti, Russia", "Lada Togliatti", "Eastern", "Kharlamov", "KHL", "Kontinental Hockey League", "Lada Arena a", "Lada Arena a, Tolyatti", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(17, 20171001, "Metallurg Magnitogorsk", "Magnitogorsk", "", "", "RU", "RUS", "Russia", "Magnitogorsk, RU", "Russia", "Magnitogorsk, Russia", "Metallurg Magnitogorsk", "Eastern", "Kharlamov", "KHL", "Kontinental Hockey League", "Arena Metallurg", "Arena Metallurg, Magnitogorsk", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(18, 20171001, "Neftekhimik Nizhnekamsk", "Nizhnekamsk", "", "", "RU", "RUS", "Russia", "Nizhnekamsk, RU", "Russia", "Nizhnekamsk, Russia", "Neftekhimik Nizhnekamsk", "Eastern", "Kharlamov", "KHL", "Kontinental Hockey League", "SCC Arena", "SCC Arena, Nizhnekamsk", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(19, 20171001, "Traktor Chelyabinsk", "Chelyabinsk", "", "", "RU", "RUS", "Russia", "Chelyabinsk, RU", "Russia", "Chelyabinsk, Russia", "Traktor Chelyabinsk", "Eastern", "Kharlamov", "KHL", "Kontinental Hockey League", "Traktor Sport Palace", "Traktor Sport Palace, Chelyabinsk", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(20, 20171001, "Yugra Khanty-Mansiysk", "Khanty-Mansiysk", "", "", "RU", "RUS", "Russia", "Khanty-Mansiysk, RU", "Russia", "Khanty-Mansiysk, Russia", "Yugra Khanty-Mansiysk", "Eastern", "Kharlamov", "KHL", "Kontinental Hockey League", "Arena Ugra", "Arena Ugra, Khanty-Mansiysk", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(21, 20171001, "Admiral Vladivostok", "Vladivostok", "", "", "RU", "RUS", "Russia", "Vladivostok, RU", "Russia", "Vladivostok, Russia", "Admiral Vladivostok", "Eastern", "Chernyshev", "KHL", "Kontinental Hockey League", "Fetisov Arena", "Fetisov Arena, Vladivostok", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(22, 20171001, "Amur Khabarovsk", "Khabarovsk", "", "", "RU", "RUS", "Russia", "Khabarovsk, RU", "Russia", "Khabarovsk, Russia", "Amur Khabarovsk", "Eastern", "Chernyshev", "KHL", "Kontinental Hockey League", "Platinum Arena", "Platinum Arena, Khabarovsk", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(23, 20171001, "Avangard Omsk", "Omsk", "", "", "RU", "RUS", "Russia", "Omsk, RU", "Russia", "Omsk, Russia", "Avangard Omsk", "Eastern", "Chernyshev", "KHL", "Kontinental Hockey League", "Omsk Arena", "Omsk Arena, Omsk", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(24, 20171001, "Barys Astana", "Astana", "", "", "RU", "RUS", "Kazakhstan", "Astana, RU", "Kazakhstan", "Astana, Kazakhstan", "Barys Astana", "Eastern", "Chernyshev", "KHL", "Kontinental Hockey League", "Barys Arena", "Barys Arena, Astana", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(25, 20171001, "Salavat Yulaev Ufa", "Ufa", "", "", "RU", "RUS", "Russia", "Ufa, RU", "Russia", "Ufa, Russia", "Salavat Yulaev Ufa", "Eastern", "Chernyshev", "KHL", "Kontinental Hockey League", "Ufa Arena", "Ufa Arena, Ufa", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(26, 20171001, "Sibir Novosibirsk", "Novosibirsk", "", "", "RU", "RUS", "Russia", "Novosibirsk, RU", "Russia", "Novosibirsk, Russia", "Sibir Novosibirsk", "Eastern", "Chernyshev", "KHL", "Kontinental Hockey League", "Ice Sports Palace Sibir", "Ice Sports Palace Sibir, Novosibirsk", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(27, 20171001, "Red Star Kunlun", "Beijing", "", "", "CN", "CHN", "China", "Beijing, CN", "China", "Beijing, China", "Red Star Kunlun", "Eastern", "Chernyshev", "KHL", "Kontinental Hockey League", "Cadillac Arena", "Cadillac Arena, Beijing", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");

-- --------------------------------------------------------

--
-- Table structure for table KHLStats
--

CREATE TABLE KHLStats (
  id INTEGER PRIMARY KEY,
  TeamID INTEGER,
  Date INTEGER,
  FullName TEXT,
  CityName TEXT,
  TeamPrefix TEXT,
  TeamSuffix TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  TeamName TEXT,
  Conference TEXT,
  Division TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GamesPlayed INTEGER,
  GamesPlayedHome INTEGER,
  GamesPlayedAway INTEGER,
  Ties INTEGER,
  Wins INTEGER,
  OTWins INTEGER,
  SOWins INTEGER,
  OTSOWins INTEGER,
  TWins INTEGER,
  Losses INTEGER,
  OTLosses INTEGER,
  SOLosses INTEGER,
  OTSOLosses INTEGER,
  TLosses INTEGER,
  ROW INTEGER,
  ROT INTEGER,
  ShutoutWins INTEGER,
  ShutoutLosses INTEGER,
  HomeRecord TEXT,
  AwayRecord TEXT,
  Shootouts TEXT,
  GoalsFor INTEGER,
  GoalsAgainst INTEGER,
  GoalsDifference INTEGER,
  SOGFor INTEGER,
  SOGAgainst INTEGER,
  SOGDifference INTEGER,
  ShotsBlockedFor INTEGER,
  ShotsBlockedAgainst INTEGER,
  ShotsBlockedDifference INTEGER,
  PPGFor INTEGER,
  PPGAgainst INTEGER,
  PPGDifference INTEGER,
  SHGFor INTEGER,
  SHGAgainst INTEGER,
  SHGDifference INTEGER,
  PenaltiesFor INTEGER,
  PenaltiesAgainst INTEGER,
  PenaltiesDifference INTEGER,
  PIMFor INTEGER,
  PIMAgainst INTEGER,
  PIMDifference INTEGER,
  HITSFor INTEGER,
  HITSAgainst INTEGER,
  HITSDifference INTEGER,
  TakeAways INTEGER,
  GiveAways INTEGER,
  TAGADifference INTEGER,
  FaceoffWins INTEGER,
  FaceoffLosses INTEGER,
  FaceoffDifference INTEGER,
  Points INTEGER,
  PCT REAL,
  LastTen TEXT,
  Streak TEXT,
  FOREIGN KEY(TeamID) REFERENCES KHLTeams(id)
);

--
-- Dumping data for table KHLStats
--

INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(1, 1, 20171001, "Dinamo Minsk", "Minsk", "", "", "BY", "BLR", "Belarus", "Minsk, BY", "Belarus", "Minsk, Belarus", "Dinamo Minsk", "Western", "Bobrov", "KHL", "Kontinental Hockey League", "Minsk-Arena", "Minsk-Arena, Minsk", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(2, 2, 20171001, "Dinamo Riga", "Riga", "", "", "LV", "LVA", "Latvia", "Riga, LV", "Latvia", "Riga, Latvia", "Dinamo Riga", "Western", "Bobrov", "KHL", "Kontinental Hockey League", "Arena Riga", "Arena Riga, Riga", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(3, 3, 20171001, "Jokerit Helsinki", "Helsinki", "", "", "FI", "FIN", "Finland", "Helsinki, FI", "Finland", "Helsinki, Finland", "Jokerit Helsinki", "Western", "Bobrov", "KHL", "Kontinental Hockey League", "Hartwall Arena", "Hartwall Arena, Helsinki", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(4, 4, 20171001, "SKA Saint Petersburg", "Saint Petersburg", "", "", "RU", "RUS", "Russia", "Saint Petersburg, RU", "Russia", "Saint Petersburg, Russia", "SKA Saint Petersburg", "Western", "Bobrov", "KHL", "Kontinental Hockey League", "Ice Palace Saint Petersburg", "Ice Palace Saint Petersburg, Saint Petersburg", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(5, 5, 20171001, "Slovan Bratislava", "Bratislava", "", "", "SK", "SVK", "Slovakia", "Bratislava, SK", "Slovakia", "Bratislava, Slovakia", "Slovan Bratislava", "Western", "Bobrov", "KHL", "Kontinental Hockey League", "Ondrej Nepela Arena", "Ondrej Nepela Arena, Bratislava", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(6, 6, 20171001, "Spartak Moscow", "Moscow", "", "", "RU", "RUS", "Russia", "Moscow, RU", "Russia", "Moscow, Russia", "Spartak Moscow", "Western", "Bobrov", "KHL", "Kontinental Hockey League", "Luzhniki Minor Arena", "Luzhniki Minor Arena, Moscow", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(7, 7, 20171001, "CSKA Moscow", "Moscow", "", "", "RU", "RUS", "Russia", "Moscow, RU", "Russia", "Moscow, Russia", "CSKA Moscow", "Western", "Tarasov", "KHL", "Kontinental Hockey League", "CSKA Ice Palace", "CSKA Ice Palace, Moscow", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(8, 8, 20171001, "Dynamo Moscow", "Moscow", "", "", "RU", "RUS", "Russia", "Moscow, RU", "Russia", "Moscow, Russia", "Dynamo Moscow", "Western", "Tarasov", "KHL", "Kontinental Hockey League", "VTB Ice Palace", "VTB Ice Palace, Moscow", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(9, 9, 20171001, "Lokomotiv Yaroslavl", "Yaroslavl", "", "", "RU", "RUS", "Russia", "Yaroslavl, RU", "Russia", "Yaroslavl, Russia", "Lokomotiv Yaroslavl", "Western", "Tarasov", "KHL", "Kontinental Hockey League", "Arena 2000", "Arena 2000, Yaroslavl", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(10, 10, 20171001, "Severstal Cherepovets", "Cherepovets", "", "", "RU", "RUS", "Russia", "Cherepovets, RU", "Russia", "Cherepovets, Russia", "Severstal Cherepovets", "Western", "Tarasov", "KHL", "Kontinental Hockey League", "Ice Palace", "Ice Palace, Cherepovets", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(11, 11, 20171001, "Sochi", "Sochi", "", "", "RU", "RUS", "Russia", "Sochi, RU", "Russia", "Sochi, Russia", "Sochi", "Western", "Tarasov", "KHL", "Kontinental Hockey League", "Bolshoy Ice Dome", "Bolshoy Ice Dome, Sochi", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(12, 12, 20171001, "Torpedo Nizhny Novgorod", "Nizhny Novgorod", "", "", "RU", "RUS", "Russia", "Nizhny Novgorod, RU", "Russia", "Nizhny Novgorod, Russia", "Torpedo Nizhny Novgorod", "Western", "Tarasov", "KHL", "Kontinental Hockey League", "Trade Union Sport Palace", "Trade Union Sport Palace, Nizhny Novgorod", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(13, 13, 20171001, "Vityaz Moscow Oblast", "Podolsk", "", "", "RU", "RUS", "Russia", "Podolsk, RU", "Russia", "Podolsk, Russia", "Vityaz Moscow Oblast", "Western", "Tarasov", "KHL", "Kontinental Hockey League", "Vityaz Ice Palace", "Vityaz Ice Palace, Podolsk", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(14, 14, 20171001, "Ak Bars Kazan", "Kazan", "", "", "RU", "RUS", "Russia", "Kazan, RU", "Russia", "Kazan, Russia", "Ak Bars Kazan", "Eastern", "Kharlamov", "KHL", "Kontinental Hockey League", "TatNeft Arena", "TatNeft Arena, Kazan", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(15, 15, 20171001, "Avtomobilist Yekaterinburg", "Yekaterinburg", "", "", "RU", "RUS", "Russia", "Yekaterinburg, RU", "Russia", "Yekaterinburg, Russia", "Avtomobilist Yekaterinburg", "Eastern", "Kharlamov", "KHL", "Kontinental Hockey League", "KRK Uralets", "KRK Uralets, Yekaterinburg", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(16, 16, 20171001, "Lada Togliatti", "Tolyatti", "", "", "RU", "RUS", "Russia", "Tolyatti, RU", "Russia", "Tolyatti, Russia", "Lada Togliatti", "Eastern", "Kharlamov", "KHL", "Kontinental Hockey League", "Lada Arena a", "Lada Arena a, Tolyatti", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(17, 17, 20171001, "Metallurg Magnitogorsk", "Magnitogorsk", "", "", "RU", "RUS", "Russia", "Magnitogorsk, RU", "Russia", "Magnitogorsk, Russia", "Metallurg Magnitogorsk", "Eastern", "Kharlamov", "KHL", "Kontinental Hockey League", "Arena Metallurg", "Arena Metallurg, Magnitogorsk", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(18, 18, 20171001, "Neftekhimik Nizhnekamsk", "Nizhnekamsk", "", "", "RU", "RUS", "Russia", "Nizhnekamsk, RU", "Russia", "Nizhnekamsk, Russia", "Neftekhimik Nizhnekamsk", "Eastern", "Kharlamov", "KHL", "Kontinental Hockey League", "SCC Arena", "SCC Arena, Nizhnekamsk", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(19, 19, 20171001, "Traktor Chelyabinsk", "Chelyabinsk", "", "", "RU", "RUS", "Russia", "Chelyabinsk, RU", "Russia", "Chelyabinsk, Russia", "Traktor Chelyabinsk", "Eastern", "Kharlamov", "KHL", "Kontinental Hockey League", "Traktor Sport Palace", "Traktor Sport Palace, Chelyabinsk", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(20, 20, 20171001, "Yugra Khanty-Mansiysk", "Khanty-Mansiysk", "", "", "RU", "RUS", "Russia", "Khanty-Mansiysk, RU", "Russia", "Khanty-Mansiysk, Russia", "Yugra Khanty-Mansiysk", "Eastern", "Kharlamov", "KHL", "Kontinental Hockey League", "Arena Ugra", "Arena Ugra, Khanty-Mansiysk", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(21, 21, 20171001, "Admiral Vladivostok", "Vladivostok", "", "", "RU", "RUS", "Russia", "Vladivostok, RU", "Russia", "Vladivostok, Russia", "Admiral Vladivostok", "Eastern", "Chernyshev", "KHL", "Kontinental Hockey League", "Fetisov Arena", "Fetisov Arena, Vladivostok", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(22, 22, 20171001, "Amur Khabarovsk", "Khabarovsk", "", "", "RU", "RUS", "Russia", "Khabarovsk, RU", "Russia", "Khabarovsk, Russia", "Amur Khabarovsk", "Eastern", "Chernyshev", "KHL", "Kontinental Hockey League", "Platinum Arena", "Platinum Arena, Khabarovsk", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(23, 23, 20171001, "Avangard Omsk", "Omsk", "", "", "RU", "RUS", "Russia", "Omsk, RU", "Russia", "Omsk, Russia", "Avangard Omsk", "Eastern", "Chernyshev", "KHL", "Kontinental Hockey League", "Omsk Arena", "Omsk Arena, Omsk", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(24, 24, 20171001, "Barys Astana", "Astana", "", "", "RU", "RUS", "Kazakhstan", "Astana, RU", "Kazakhstan", "Astana, Kazakhstan", "Barys Astana", "Eastern", "Chernyshev", "KHL", "Kontinental Hockey League", "Barys Arena", "Barys Arena, Astana", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(25, 25, 20171001, "Salavat Yulaev Ufa", "Ufa", "", "", "RU", "RUS", "Russia", "Ufa, RU", "Russia", "Ufa, Russia", "Salavat Yulaev Ufa", "Eastern", "Chernyshev", "KHL", "Kontinental Hockey League", "Ufa Arena", "Ufa Arena, Ufa", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(26, 26, 20171001, "Sibir Novosibirsk", "Novosibirsk", "", "", "RU", "RUS", "Russia", "Novosibirsk, RU", "Russia", "Novosibirsk, Russia", "Sibir Novosibirsk", "Eastern", "Chernyshev", "KHL", "Kontinental Hockey League", "Ice Sports Palace Sibir", "Ice Sports Palace Sibir, Novosibirsk", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");
INSERT INTO KHLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(27, 27, 20171001, "Red Star Kunlun", "Beijing", "", "", "CN", "CHN", "China", "Beijing, CN", "China", "Beijing, China", "Red Star Kunlun", "Eastern", "Chernyshev", "KHL", "Kontinental Hockey League", "Cadillac Arena", "Cadillac Arena, Beijing", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "None");

-- --------------------------------------------------------

--
-- Table structure for table KHLGameStats
--

CREATE TABLE KHLGameStats (
  id INTEGER PRIMARY KEY,
  GameID INTEGER,
  Date INTEGER,
  TeamID INTEGER,
  FullName TEXT,
  CityName TEXT,
  TeamPrefix TEXT,
  TeamSuffix TEXT,
  AreaName TEXT,
  CountryName TEXT,
  FullCountryName TEXT,
  FullCityName TEXT,
  FullAreaName TEXT,
  FullCityNameAlt TEXT,
  TeamName TEXT,
  Conference TEXT,
  Division TEXT,
  LeagueName TEXT,
  LeagueFullName TEXT,
  ArenaName TEXT,
  FullArenaName TEXT,
  GoalsFor INTEGER,
  GoalsAgainst INTEGER,
  GoalsDifference INTEGER,
  SOGFor INTEGER,
  SOGAgainst INTEGER,
  SOGDifference INTEGER,
  ShotsBlockedFor INTEGER,
  ShotsBlockedAgainst INTEGER,
  ShotsBlockedDifference INTEGER,
  PPGFor INTEGER,
  PPGAgainst INTEGER,
  PPGDifference INTEGER,
  SHGFor INTEGER,
  SHGAgainst INTEGER,
  SHGDifference INTEGER,
  PenaltiesFor INTEGER,
  PenaltiesAgainst INTEGER,
  PenaltiesDifference INTEGER,
  PIMFor INTEGER,
  PIMAgainst INTEGER,
  PIMDifference INTEGER,
  HITSFor INTEGER,
  HITSAgainst INTEGER,
  HITSDifference INTEGER,
  TakeAways INTEGER,
  GiveAways INTEGER,
  TAGADifference INTEGER,
  FaceoffWins INTEGER,
  FaceoffLosses INTEGER,
  FaceoffDifference INTEGER,
  FOREIGN KEY(GameID) REFERENCES KHLGames(id),
  FOREIGN KEY(TeamID) REFERENCES KHLTeams(id)
);

--
-- Dumping data for table KHLGameStats
--


-- --------------------------------------------------------

--
-- Table structure for table KHLGames
--

CREATE TABLE KHLGames (
  id INTEGER PRIMARY KEY,
  Date INTEGER,
  HomeTeam TEXT,
  AwayTeam TEXT,
  AtArena TEXT,
  TeamScorePeriods TEXT,
  TeamFullScore TEXT,
  ShotsOnGoal TEXT,
  FullShotsOnGoal TEXT,
  ShotsBlocked TEXT,
  FullShotsBlocked TEXT,
  PowerPlays TEXT,
  FullPowerPlays TEXT,
  ShortHanded TEXT,
  FullShortHanded TEXT,
  Penalties TEXT,
  FullPenalties TEXT,
  PenaltyMinutes TEXT,
  FullPenaltyMinutes TEXT,
  HitsPerPeriod TEXT,
  FullHitsPerPeriod TEXT,
  TakeAways TEXT,
  FullTakeAways TEXT,
  GiveAways TEXT,
  FullGiveAways TEXT,
  FaceoffWins TEXT,
  FullFaceoffWins TEXT,
  NumberPeriods INTEGER,
  TeamWin TEXT,
  TeamLost TEXT,
  TieGame INTEGER,
  IsPlayOffGame INTEGER
);

--
-- Dumping data for table KHLGames
--


-- --------------------------------------------------------

