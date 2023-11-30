-- PyHockeyStats SQL Dumper
-- version 0.7.6 RC 1
-- https://github.com/GameMaker2k/Neo-Hockey-Test
--
-- Generation Time: November 30, 2023 at 02:27 PM
-- SQLite Server version: 3.43.1
-- PySQLite version: 2.6.0
-- Python Version: 3.13.0

--
-- Database: ./php/data/hockey1942-43.db3
--

-- --------------------------------------------------------

--
-- Table structure for table HockeyLeagues
--

DROP TABLE IF EXISTS HockeyLeagues;

CREATE TABLE HockeyLeagues (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  LeagueName TEXT NOT NULL DEFAULT '',
  LeagueFullName TEXT NOT NULL DEFAULT '',
  CountryName TEXT NOT NULL DEFAULT '',
  FullCountryName TEXT NOT NULL DEFAULT '',
  Date INTEGER NOT NULL DEFAULT 0,
  PlayOffFMT TEXT NOT NULL DEFAULT '',
  OrderType TEXT NOT NULL DEFAULT '',
  NumberOfTeams INTEGER NOT NULL DEFAULT 0,
  NumberOfConferences INTEGER NOT NULL DEFAULT 0,
  NumberOfDivisions INTEGER NOT NULL DEFAULT 0
);

--
-- Dumping data for table HockeyLeagues
--

INSERT INTO HockeyLeagues (id, LeagueName, LeagueFullName, CountryName, FullCountryName, Date, PlayOffFMT, OrderType, NumberOfTeams, NumberOfConferences, NumberOfDivisions) VALUES 
(1, "NHL", "National Hockey League", "USA", "United States", 19421031, "League=4", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", 6, 0, 0);
INSERT INTO HockeyLeagues (id, LeagueName, LeagueFullName, CountryName, FullCountryName, Date, PlayOffFMT, OrderType, NumberOfTeams, NumberOfConferences, NumberOfDivisions) VALUES 
(2, "AHL", "American Hockey League", "USA", "United States", 19421031, "League=4", "ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", 9, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table NHLConferences
--

DROP TABLE IF EXISTS NHLConferences;

CREATE TABLE NHLConferences (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Conference TEXT NOT NULL DEFAULT '',
  ConferencePrefix TEXT NOT NULL DEFAULT '',
  ConferenceSuffix TEXT NOT NULL DEFAULT '',
  FullName TEXT NOT NULL DEFAULT '',
  LeagueName TEXT NOT NULL DEFAULT '',
  LeagueFullName TEXT NOT NULL DEFAULT '',
  NumberOfTeams INTEGER NOT NULL DEFAULT 0,
  NumberOfDivisions INTEGER NOT NULL DEFAULT 0
);

--
-- Dumping data for table NHLConferences
--

INSERT INTO NHLConferences (id, Conference, ConferencePrefix, ConferenceSuffix, FullName, LeagueName, LeagueFullName, NumberOfTeams, NumberOfDivisions) VALUES 
(1, "", "", "Conference", " Conference", "NHL", "National Hockey League", 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table NHLDivisions
--

DROP TABLE IF EXISTS NHLDivisions;

CREATE TABLE NHLDivisions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Division TEXT NOT NULL DEFAULT '',
  DivisionPrefix TEXT NOT NULL DEFAULT '',
  DivisionSuffix TEXT NOT NULL DEFAULT '',
  FullName TEXT NOT NULL DEFAULT '',
  Conference TEXT NOT NULL DEFAULT '',
  ConferenceFullName TEXT NOT NULL DEFAULT '',
  LeagueName TEXT NOT NULL DEFAULT '',
  LeagueFullName TEXT NOT NULL DEFAULT '',
  NumberOfTeams INTEGER NOT NULL DEFAULT 0
);

--
-- Dumping data for table NHLDivisions
--

INSERT INTO NHLDivisions (id, Division, DivisionPrefix, DivisionSuffix, FullName, Conference, ConferenceFullName, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(1, "", "", "Division", " Division", "", " Conference", "NHL", "National Hockey League", 0);

-- --------------------------------------------------------

--
-- Table structure for table NHLArenas
--

DROP TABLE IF EXISTS NHLArenas;

CREATE TABLE NHLArenas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  TeamID INTEGER NOT NULL DEFAULT 0,
  TeamName TEXT NOT NULL DEFAULT '',
  TeamFullName TEXT NOT NULL DEFAULT '',
  CityName TEXT NOT NULL DEFAULT '',
  AreaName TEXT NOT NULL DEFAULT '',
  CountryName TEXT NOT NULL DEFAULT '',
  FullCountryName TEXT NOT NULL DEFAULT '',
  FullCityName TEXT NOT NULL DEFAULT '',
  FullAreaName TEXT NOT NULL DEFAULT '',
  FullCityNameAlt TEXT NOT NULL DEFAULT '',
  ArenaName TEXT NOT NULL DEFAULT '',
  FullArenaName TEXT NOT NULL DEFAULT '',
  GamesPlayed INTEGER NOT NULL DEFAULT 0
);

--
-- Dumping data for table NHLArenas
--

INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(1, 1, "Bruins", "Boston Bruins", "Boston", "MA", "USA", "United States", "Boston, MA", "Massachusetts", "Boston, Massachusetts", "Boston Garden", "Boston Garden, Boston", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(2, 2, "Blackhawks", "Chicago Blackhawks", "Chicago", "IL", "USA", "United States", "Chicago, IL", "Illinois", "Chicago, Illinois", "Chicago Stadium", "Chicago Stadium, Chicago", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(3, 3, "Red Wings", "Detroit Red Wings", "Detroit", "MI", "USA", "United States", "Detroit, MI", "Michigan", "Detroit, Michigan", "Detroit Olympia", "Detroit Olympia, Detroit", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(4, 4, "Canadiens", "Montreal Canadiens", "Montreal", "QC", "CAN", "Canada", "Montreal, QC", "Quebec", "Montreal, Quebec", "Montreal Forum", "Montreal Forum, Montreal", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(5, 5, "Rangers", "New York Rangers", "New York City", "NY", "USA", "United States", "New York City, NY", "New York", "New York City, New York", "Madison Square Garden", "Madison Square Garden, New York City", 0);
INSERT INTO NHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(6, 6, "Maple Leafs", "Toronto Maple Leafs", "Toronto", "ON", "CAN", "Canada", "Toronto, ON", "Ontario", "Toronto, Ontario", "Maple Leaf Gardens", "Maple Leaf Gardens, Toronto", 0);

-- --------------------------------------------------------

--
-- Table structure for table NHLTeams
--

DROP TABLE IF EXISTS NHLTeams;

CREATE TABLE NHLTeams (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Date INTEGER NOT NULL DEFAULT 0,
  Time INTEGER NOT NULL DEFAULT 0,
  DateTime INTEGER NOT NULL DEFAULT 0,
  FullName TEXT NOT NULL DEFAULT '',
  CityName TEXT NOT NULL DEFAULT '',
  TeamPrefix TEXT NOT NULL DEFAULT '',
  TeamSuffix TEXT NOT NULL DEFAULT '',
  AreaName TEXT NOT NULL DEFAULT '',
  CountryName TEXT NOT NULL DEFAULT '',
  FullCountryName TEXT NOT NULL DEFAULT '',
  FullCityName TEXT NOT NULL DEFAULT '',
  FullAreaName TEXT NOT NULL DEFAULT '',
  FullCityNameAlt TEXT NOT NULL DEFAULT '',
  TeamName TEXT NOT NULL DEFAULT '',
  Conference TEXT NOT NULL DEFAULT '',
  ConferenceFullName TEXT NOT NULL DEFAULT '',
  Division TEXT NOT NULL DEFAULT '',
  DivisionFullName TEXT NOT NULL DEFAULT '',
  LeagueName TEXT NOT NULL DEFAULT '',
  LeagueFullName TEXT NOT NULL DEFAULT '',
  ArenaName TEXT NOT NULL DEFAULT '',
  FullArenaName TEXT NOT NULL DEFAULT '',
  Affiliates TEXT NOT NULL DEFAULT '',
  GamesPlayed INTEGER NOT NULL DEFAULT 0,
  GamesPlayedHome INTEGER NOT NULL DEFAULT 0,
  GamesPlayedAway INTEGER NOT NULL DEFAULT 0,
  Ties INTEGER NOT NULL DEFAULT 0,
  Wins INTEGER NOT NULL DEFAULT 0,
  OTWins INTEGER NOT NULL DEFAULT 0,
  SOWins INTEGER NOT NULL DEFAULT 0,
  OTSOWins INTEGER NOT NULL DEFAULT 0,
  TWins INTEGER NOT NULL DEFAULT 0,
  Losses INTEGER NOT NULL DEFAULT 0,
  OTLosses INTEGER NOT NULL DEFAULT 0,
  SOLosses INTEGER NOT NULL DEFAULT 0,
  OTSOLosses INTEGER NOT NULL DEFAULT 0,
  TLosses INTEGER NOT NULL DEFAULT 0,
  ROW INTEGER NOT NULL DEFAULT 0,
  ROT INTEGER NOT NULL DEFAULT 0,
  ShutoutWins INTEGER NOT NULL DEFAULT 0,
  ShutoutLosses INTEGER NOT NULL DEFAULT 0,
  HomeRecord TEXT NOT NULL DEFAULT '0:0:0:0',
  AwayRecord TEXT NOT NULL DEFAULT '0:0:0:0',
  Shootouts TEXT NOT NULL DEFAULT '0:0',
  GoalsFor INTEGER NOT NULL DEFAULT 0,
  GoalsAgainst INTEGER NOT NULL DEFAULT 0,
  GoalsDifference INTEGER NOT NULL DEFAULT 0,
  SOGFor INTEGER NOT NULL DEFAULT 0,
  SOGAgainst INTEGER NOT NULL DEFAULT 0,
  SOGDifference INTEGER NOT NULL DEFAULT 0,
  ShotsBlockedFor INTEGER NOT NULL DEFAULT 0,
  ShotsBlockedAgainst INTEGER NOT NULL DEFAULT 0,
  ShotsBlockedDifference INTEGER NOT NULL DEFAULT 0,
  PPGFor INTEGER NOT NULL DEFAULT 0,
  PPGAgainst INTEGER NOT NULL DEFAULT 0,
  PPGDifference INTEGER NOT NULL DEFAULT 0,
  SHGFor INTEGER NOT NULL DEFAULT 0,
  SHGAgainst INTEGER NOT NULL DEFAULT 0,
  SHGDifference INTEGER NOT NULL DEFAULT 0,
  PenaltiesFor INTEGER NOT NULL DEFAULT 0,
  PenaltiesAgainst INTEGER NOT NULL DEFAULT 0,
  PenaltiesDifference INTEGER NOT NULL DEFAULT 0,
  PIMFor INTEGER NOT NULL DEFAULT 0,
  PIMAgainst INTEGER NOT NULL DEFAULT 0,
  PIMDifference INTEGER NOT NULL DEFAULT 0,
  HITSFor INTEGER NOT NULL DEFAULT 0,
  HITSAgainst INTEGER NOT NULL DEFAULT 0,
  HITSDifference INTEGER NOT NULL DEFAULT 0,
  TakeAways INTEGER NOT NULL DEFAULT 0,
  GiveAways INTEGER NOT NULL DEFAULT 0,
  TAGADifference INTEGER NOT NULL DEFAULT 0,
  FaceoffWins INTEGER NOT NULL DEFAULT 0,
  FaceoffLosses INTEGER NOT NULL DEFAULT 0,
  FaceoffDifference INTEGER NOT NULL DEFAULT 0,
  Points INTEGER NOT NULL DEFAULT 0,
  PCT REAL NOT NULL DEFAULT 0,
  LastTen TEXT NOT NULL DEFAULT '0:0:0:0',
  Streak TEXT NOT NULL DEFAULT 'None'
);

--
-- Dumping data for table NHLTeams
--

INSERT INTO NHLTeams (id, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(1, 19421000, 0, 194210000000, "Boston Bruins", "Boston", "Boston", "", "MA", "USA", "United States", "Boston, MA", "Massachusetts", "Boston, Massachusetts", "Bruins", "", " Conference", "", " Division", "NHL", "National Hockey League", "Boston Garden", "Boston Garden, Boston", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(2, 19421000, 0, 194210000000, "Chicago Blackhawks", "Chicago", "Chicago", "", "IL", "USA", "United States", "Chicago, IL", "Illinois", "Chicago, Illinois", "Blackhawks", "", " Conference", "", " Division", "NHL", "National Hockey League", "Chicago Stadium", "Chicago Stadium, Chicago", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(3, 19421000, 0, 194210000000, "Detroit Red Wings", "Detroit", "Detroit", "", "MI", "USA", "United States", "Detroit, MI", "Michigan", "Detroit, Michigan", "Red Wings", "", " Conference", "", " Division", "NHL", "National Hockey League", "Detroit Olympia", "Detroit Olympia, Detroit", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(4, 19421000, 0, 194210000000, "Montreal Canadiens", "Montreal", "Montreal", "", "QC", "CAN", "Canada", "Montreal, QC", "Quebec", "Montreal, Quebec", "Canadiens", "", " Conference", "", " Division", "NHL", "National Hockey League", "Montreal Forum", "Montreal Forum, Montreal", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(5, 19421000, 0, 194210000000, "New York Rangers", "New York City", "New York", "", "NY", "USA", "United States", "New York City, NY", "New York", "New York City, New York", "Rangers", "", " Conference", "", " Division", "NHL", "National Hockey League", "Madison Square Garden", "Madison Square Garden, New York City", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO NHLTeams (id, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(6, 19421000, 0, 194210000000, "Toronto Maple Leafs", "Toronto", "Toronto", "", "ON", "CAN", "Canada", "Toronto, ON", "Ontario", "Toronto, Ontario", "Maple Leafs", "", " Conference", "", " Division", "NHL", "National Hockey League", "Maple Leaf Gardens", "Maple Leaf Gardens, Toronto", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");

-- --------------------------------------------------------

--
-- Table structure for table NHLStats
--

DROP TABLE IF EXISTS NHLStats;

CREATE TABLE NHLStats (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  TeamID INTEGER NOT NULL DEFAULT 0,
  Date INTEGER NOT NULL DEFAULT 0,
  Time INTEGER NOT NULL DEFAULT 0,
  DateTime INTEGER NOT NULL DEFAULT 0,
  FullName TEXT NOT NULL DEFAULT '',
  CityName TEXT NOT NULL DEFAULT '',
  TeamPrefix TEXT NOT NULL DEFAULT '',
  TeamSuffix TEXT NOT NULL DEFAULT '',
  AreaName TEXT NOT NULL DEFAULT '',
  CountryName TEXT NOT NULL DEFAULT '',
  FullCountryName TEXT NOT NULL DEFAULT '',
  FullCityName TEXT NOT NULL DEFAULT '',
  FullAreaName TEXT NOT NULL DEFAULT '',
  FullCityNameAlt TEXT NOT NULL DEFAULT '',
  TeamName TEXT NOT NULL DEFAULT '',
  Conference TEXT NOT NULL DEFAULT '',
  ConferenceFullName TEXT NOT NULL DEFAULT '',
  Division TEXT NOT NULL DEFAULT '',
  DivisionFullName TEXT NOT NULL DEFAULT '',
  LeagueName TEXT NOT NULL DEFAULT '',
  LeagueFullName TEXT NOT NULL DEFAULT '',
  ArenaName TEXT NOT NULL DEFAULT '',
  FullArenaName TEXT NOT NULL DEFAULT '',
  Affiliates TEXT NOT NULL DEFAULT '',
  GamesPlayed INTEGER NOT NULL DEFAULT 0,
  GamesPlayedHome INTEGER NOT NULL DEFAULT 0,
  GamesPlayedAway INTEGER NOT NULL DEFAULT 0,
  Ties INTEGER NOT NULL DEFAULT 0,
  Wins INTEGER NOT NULL DEFAULT 0,
  OTWins INTEGER NOT NULL DEFAULT 0,
  SOWins INTEGER NOT NULL DEFAULT 0,
  OTSOWins INTEGER NOT NULL DEFAULT 0,
  TWins INTEGER NOT NULL DEFAULT 0,
  Losses INTEGER NOT NULL DEFAULT 0,
  OTLosses INTEGER NOT NULL DEFAULT 0,
  SOLosses INTEGER NOT NULL DEFAULT 0,
  OTSOLosses INTEGER NOT NULL DEFAULT 0,
  TLosses INTEGER NOT NULL DEFAULT 0,
  ROW INTEGER NOT NULL DEFAULT 0,
  ROT INTEGER NOT NULL DEFAULT 0,
  ShutoutWins INTEGER NOT NULL DEFAULT 0,
  ShutoutLosses INTEGER NOT NULL DEFAULT 0,
  HomeRecord TEXT NOT NULL DEFAULT '0:0:0:0',
  AwayRecord TEXT NOT NULL DEFAULT '0:0:0:0',
  Shootouts TEXT NOT NULL DEFAULT '0:0',
  GoalsFor INTEGER NOT NULL DEFAULT 0,
  GoalsAgainst INTEGER NOT NULL DEFAULT 0,
  GoalsDifference INTEGER NOT NULL DEFAULT 0,
  SOGFor INTEGER NOT NULL DEFAULT 0,
  SOGAgainst INTEGER NOT NULL DEFAULT 0,
  SOGDifference INTEGER NOT NULL DEFAULT 0,
  ShotsBlockedFor INTEGER NOT NULL DEFAULT 0,
  ShotsBlockedAgainst INTEGER NOT NULL DEFAULT 0,
  ShotsBlockedDifference INTEGER NOT NULL DEFAULT 0,
  PPGFor INTEGER NOT NULL DEFAULT 0,
  PPGAgainst INTEGER NOT NULL DEFAULT 0,
  PPGDifference INTEGER NOT NULL DEFAULT 0,
  SHGFor INTEGER NOT NULL DEFAULT 0,
  SHGAgainst INTEGER NOT NULL DEFAULT 0,
  SHGDifference INTEGER NOT NULL DEFAULT 0,
  PenaltiesFor INTEGER NOT NULL DEFAULT 0,
  PenaltiesAgainst INTEGER NOT NULL DEFAULT 0,
  PenaltiesDifference INTEGER NOT NULL DEFAULT 0,
  PIMFor INTEGER NOT NULL DEFAULT 0,
  PIMAgainst INTEGER NOT NULL DEFAULT 0,
  PIMDifference INTEGER NOT NULL DEFAULT 0,
  HITSFor INTEGER NOT NULL DEFAULT 0,
  HITSAgainst INTEGER NOT NULL DEFAULT 0,
  HITSDifference INTEGER NOT NULL DEFAULT 0,
  TakeAways INTEGER NOT NULL DEFAULT 0,
  GiveAways INTEGER NOT NULL DEFAULT 0,
  TAGADifference INTEGER NOT NULL DEFAULT 0,
  FaceoffWins INTEGER NOT NULL DEFAULT 0,
  FaceoffLosses INTEGER NOT NULL DEFAULT 0,
  FaceoffDifference INTEGER NOT NULL DEFAULT 0,
  Points INTEGER NOT NULL DEFAULT 0,
  PCT REAL NOT NULL DEFAULT 0,
  LastTen TEXT NOT NULL DEFAULT '0:0:0:0',
  Streak TEXT NOT NULL DEFAULT 'None'
);

--
-- Dumping data for table NHLStats
--

INSERT INTO NHLStats (id, TeamID, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(1, 1, 19421000, 0, 194210000000, "Boston Bruins", "Boston", "Boston", "", "MA", "USA", "United States", "Boston, MA", "Massachusetts", "Boston, Massachusetts", "Bruins", "", " Conference", "", " Division", "NHL", "National Hockey League", "Boston Garden", "Boston Garden, Boston", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(2, 2, 19421000, 0, 194210000000, "Chicago Blackhawks", "Chicago", "Chicago", "", "IL", "USA", "United States", "Chicago, IL", "Illinois", "Chicago, Illinois", "Blackhawks", "", " Conference", "", " Division", "NHL", "National Hockey League", "Chicago Stadium", "Chicago Stadium, Chicago", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(3, 3, 19421000, 0, 194210000000, "Detroit Red Wings", "Detroit", "Detroit", "", "MI", "USA", "United States", "Detroit, MI", "Michigan", "Detroit, Michigan", "Red Wings", "", " Conference", "", " Division", "NHL", "National Hockey League", "Detroit Olympia", "Detroit Olympia, Detroit", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(4, 4, 19421000, 0, 194210000000, "Montreal Canadiens", "Montreal", "Montreal", "", "QC", "CAN", "Canada", "Montreal, QC", "Quebec", "Montreal, Quebec", "Canadiens", "", " Conference", "", " Division", "NHL", "National Hockey League", "Montreal Forum", "Montreal Forum, Montreal", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(5, 5, 19421000, 0, 194210000000, "New York Rangers", "New York City", "New York", "", "NY", "USA", "United States", "New York City, NY", "New York", "New York City, New York", "Rangers", "", " Conference", "", " Division", "NHL", "National Hockey League", "Madison Square Garden", "Madison Square Garden, New York City", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO NHLStats (id, TeamID, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(6, 6, 19421000, 0, 194210000000, "Toronto Maple Leafs", "Toronto", "Toronto", "", "ON", "CAN", "Canada", "Toronto, ON", "Ontario", "Toronto, Ontario", "Maple Leafs", "", " Conference", "", " Division", "NHL", "National Hockey League", "Maple Leaf Gardens", "Maple Leaf Gardens, Toronto", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");

-- --------------------------------------------------------

--
-- Table structure for table NHLGameStats
--

DROP TABLE IF EXISTS NHLGameStats;

CREATE TABLE NHLGameStats (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  GameID INTEGER NOT NULL DEFAULT 0,
  TeamID INTEGER NOT NULL DEFAULT 0,
  Date INTEGER NOT NULL DEFAULT 0,
  Time INTEGER NOT NULL DEFAULT 0,
  DateTime INTEGER NOT NULL DEFAULT 0,
  FullName TEXT NOT NULL DEFAULT '',
  CityName TEXT NOT NULL DEFAULT '',
  TeamPrefix TEXT NOT NULL DEFAULT '',
  TeamSuffix TEXT NOT NULL DEFAULT '',
  AreaName TEXT NOT NULL DEFAULT '',
  CountryName TEXT NOT NULL DEFAULT '',
  FullCountryName TEXT NOT NULL DEFAULT '',
  FullCityName TEXT NOT NULL DEFAULT '',
  FullAreaName TEXT NOT NULL DEFAULT '',
  FullCityNameAlt TEXT NOT NULL DEFAULT '',
  TeamName TEXT NOT NULL DEFAULT '',
  Conference TEXT NOT NULL DEFAULT '',
  ConferenceFullName TEXT NOT NULL DEFAULT '',
  Division TEXT NOT NULL DEFAULT '',
  DivisionFullName TEXT NOT NULL DEFAULT '',
  LeagueName TEXT NOT NULL DEFAULT '',
  LeagueFullName TEXT NOT NULL DEFAULT '',
  ArenaName TEXT NOT NULL DEFAULT '',
  FullArenaName TEXT NOT NULL DEFAULT '',
  Affiliates TEXT NOT NULL DEFAULT '',
  GoalsFor INTEGER NOT NULL DEFAULT 0,
  GoalsAgainst INTEGER NOT NULL DEFAULT 0,
  GoalsDifference INTEGER NOT NULL DEFAULT 0,
  SOGFor INTEGER NOT NULL DEFAULT 0,
  SOGAgainst INTEGER NOT NULL DEFAULT 0,
  SOGDifference INTEGER NOT NULL DEFAULT 0,
  ShotsBlockedFor INTEGER NOT NULL DEFAULT 0,
  ShotsBlockedAgainst INTEGER NOT NULL DEFAULT 0,
  ShotsBlockedDifference INTEGER NOT NULL DEFAULT 0,
  PPGFor INTEGER NOT NULL DEFAULT 0,
  PPGAgainst INTEGER NOT NULL DEFAULT 0,
  PPGDifference INTEGER NOT NULL DEFAULT 0,
  SHGFor INTEGER NOT NULL DEFAULT 0,
  SHGAgainst INTEGER NOT NULL DEFAULT 0,
  SHGDifference INTEGER NOT NULL DEFAULT 0,
  PenaltiesFor INTEGER NOT NULL DEFAULT 0,
  PenaltiesAgainst INTEGER NOT NULL DEFAULT 0,
  PenaltiesDifference INTEGER NOT NULL DEFAULT 0,
  PIMFor INTEGER NOT NULL DEFAULT 0,
  PIMAgainst INTEGER NOT NULL DEFAULT 0,
  PIMDifference INTEGER NOT NULL DEFAULT 0,
  HITSFor INTEGER NOT NULL DEFAULT 0,
  HITSAgainst INTEGER NOT NULL DEFAULT 0,
  HITSDifference INTEGER NOT NULL DEFAULT 0,
  TakeAways INTEGER NOT NULL DEFAULT 0,
  GiveAways INTEGER NOT NULL DEFAULT 0,
  TAGADifference INTEGER NOT NULL DEFAULT 0,
  FaceoffWins INTEGER NOT NULL DEFAULT 0,
  FaceoffLosses INTEGER NOT NULL DEFAULT 0,
  FaceoffDifference INTEGER NOT NULL DEFAULT 0
);

--
-- Dumping data for table NHLGameStats
--


-- --------------------------------------------------------

--
-- Table structure for table NHLGames
--

DROP TABLE IF EXISTS NHLGames;

CREATE TABLE NHLGames (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Date INTEGER NOT NULL DEFAULT 0,
  Time INTEGER NOT NULL DEFAULT 0,
  DateTime INTEGER NOT NULL DEFAULT 0,
  HomeTeam TEXT NOT NULL DEFAULT '',
  AwayTeam TEXT NOT NULL DEFAULT '',
  AtArena TEXT NOT NULL DEFAULT '',
  TeamScorePeriods TEXT NOT NULL DEFAULT '',
  TeamFullScore TEXT NOT NULL DEFAULT '',
  ShotsOnGoal TEXT NOT NULL DEFAULT '',
  FullShotsOnGoal TEXT NOT NULL DEFAULT '',
  ShotsBlocked TEXT NOT NULL DEFAULT '',
  FullShotsBlocked TEXT NOT NULL DEFAULT '',
  PowerPlays TEXT NOT NULL DEFAULT '',
  FullPowerPlays TEXT NOT NULL DEFAULT '',
  ShortHanded TEXT NOT NULL DEFAULT '',
  FullShortHanded TEXT NOT NULL DEFAULT '',
  Penalties TEXT NOT NULL DEFAULT '',
  FullPenalties TEXT NOT NULL DEFAULT '',
  PenaltyMinutes TEXT NOT NULL DEFAULT '',
  FullPenaltyMinutes TEXT NOT NULL DEFAULT '',
  HitsPerPeriod TEXT NOT NULL DEFAULT '',
  FullHitsPerPeriod TEXT NOT NULL DEFAULT '',
  TakeAways TEXT NOT NULL DEFAULT '',
  FullTakeAways TEXT NOT NULL DEFAULT '',
  GiveAways TEXT NOT NULL DEFAULT '',
  FullGiveAways TEXT NOT NULL DEFAULT '',
  FaceoffWins TEXT NOT NULL DEFAULT '',
  FullFaceoffWins TEXT NOT NULL DEFAULT '',
  NumberPeriods INTEGER NOT NULL DEFAULT 0,
  TeamWin TEXT NOT NULL DEFAULT '',
  TeamLost TEXT NOT NULL DEFAULT '',
  TieGame INTEGER NOT NULL DEFAULT 0,
  IsPlayOffGame INTEGER NOT NULL DEFAULT 0
);

--
-- Dumping data for table NHLGames
--


-- --------------------------------------------------------

--
-- Table structure for table AHLConferences
--

DROP TABLE IF EXISTS AHLConferences;

CREATE TABLE AHLConferences (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Conference TEXT NOT NULL DEFAULT '',
  ConferencePrefix TEXT NOT NULL DEFAULT '',
  ConferenceSuffix TEXT NOT NULL DEFAULT '',
  FullName TEXT NOT NULL DEFAULT '',
  LeagueName TEXT NOT NULL DEFAULT '',
  LeagueFullName TEXT NOT NULL DEFAULT '',
  NumberOfTeams INTEGER NOT NULL DEFAULT 0,
  NumberOfDivisions INTEGER NOT NULL DEFAULT 0
);

--
-- Dumping data for table AHLConferences
--

INSERT INTO AHLConferences (id, Conference, ConferencePrefix, ConferenceSuffix, FullName, LeagueName, LeagueFullName, NumberOfTeams, NumberOfDivisions) VALUES 
(1, "", "", "Conference", " Conference", "AHL", "American Hockey League", 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table AHLDivisions
--

DROP TABLE IF EXISTS AHLDivisions;

CREATE TABLE AHLDivisions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Division TEXT NOT NULL DEFAULT '',
  DivisionPrefix TEXT NOT NULL DEFAULT '',
  DivisionSuffix TEXT NOT NULL DEFAULT '',
  FullName TEXT NOT NULL DEFAULT '',
  Conference TEXT NOT NULL DEFAULT '',
  ConferenceFullName TEXT NOT NULL DEFAULT '',
  LeagueName TEXT NOT NULL DEFAULT '',
  LeagueFullName TEXT NOT NULL DEFAULT '',
  NumberOfTeams INTEGER NOT NULL DEFAULT 0
);

--
-- Dumping data for table AHLDivisions
--

INSERT INTO AHLDivisions (id, Division, DivisionPrefix, DivisionSuffix, FullName, Conference, ConferenceFullName, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(1, "", "", "Division", " Division", "", " Conference", "AHL", "American Hockey League", 0);

-- --------------------------------------------------------

--
-- Table structure for table AHLArenas
--

DROP TABLE IF EXISTS AHLArenas;

CREATE TABLE AHLArenas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  TeamID INTEGER NOT NULL DEFAULT 0,
  TeamName TEXT NOT NULL DEFAULT '',
  TeamFullName TEXT NOT NULL DEFAULT '',
  CityName TEXT NOT NULL DEFAULT '',
  AreaName TEXT NOT NULL DEFAULT '',
  CountryName TEXT NOT NULL DEFAULT '',
  FullCountryName TEXT NOT NULL DEFAULT '',
  FullCityName TEXT NOT NULL DEFAULT '',
  FullAreaName TEXT NOT NULL DEFAULT '',
  FullCityNameAlt TEXT NOT NULL DEFAULT '',
  ArenaName TEXT NOT NULL DEFAULT '',
  FullArenaName TEXT NOT NULL DEFAULT '',
  GamesPlayed INTEGER NOT NULL DEFAULT 0
);

--
-- Dumping data for table AHLArenas
--

INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(1, 1, "Bisons", "Buffalo Bisons", "Buffalo", "NY", "USA", "United States", "Buffalo, NY", "New York", "Buffalo, New York", "Buffalo Memorial Auditorium", "Buffalo Memorial Auditorium, Buffalo", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(2, 2, "Barons", "Cleveland Barons", "Cleveland", "OH", "USA", "United States", "Cleveland, OH", "Ohio", "Cleveland, Ohio", "Cleveland Arena", "Cleveland Arena, Cleveland", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(3, 3, "Red Wings", "Hershey Red Wings", "Hershey", "PA", "USA", "United States", "Hershey, PA", "Pennsylvania", "Hershey, Pennsylvania", "Hersheypark Arena", "Hersheypark Arena, Hershey", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(4, 4, "Capitals", "Indianapolis Capitals", "Indianapolis", "IN", "USA", "United States", "Indianapolis, IN", "Indiana", "Indianapolis, Indiana", "Indiana State Fairgrounds Coliseum", "Indiana State Fairgrounds Coliseum, Indianapolis", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(5, 5, "Rockets", "Philadelphia Rockets", "Philadelphia", "PA", "USA", "United States", "Philadelphia, PA", "Pennsylvania", "Philadelphia, Pennsylvania", "Philadelphia Arena", "Philadelphia Arena, Philadelphia", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(6, 6, "Hornets", "Pittsburgh Hornets", "Pittsburgh", "PA", "USA", "United States", "Pittsburgh, PA", "Pennsylvania", "Pittsburgh, Pennsylvania", "Duquesne Gardens", "Duquesne Gardens, Pittsburgh", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(7, 7, "Reds", "Providence Reds", "Providence", "RI", "USA", "United States", "Providence, RI", "Rhode Island", "Providence, Rhode Island", "Rhode Island Auditorium", "Rhode Island Auditorium, Providence", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(8, 8, "Indians", "Springfield Indians", "West Springfield", "MA", "USA", "United States", "West Springfield, MA", "Massachusetts", "West Springfield, Massachusetts", "Eastern States Coliseum", "Eastern States Coliseum, West Springfield", 0);
INSERT INTO AHLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(9, 9, "Lions", "Washington Lions", "Washington", "DC", "USA", "United States", "Washington, DC", "District of Columbia", "Washington, District of Columbia", "Washington Coliseum", "Washington Coliseum, Washington", 0);

-- --------------------------------------------------------

--
-- Table structure for table AHLTeams
--

DROP TABLE IF EXISTS AHLTeams;

CREATE TABLE AHLTeams (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Date INTEGER NOT NULL DEFAULT 0,
  Time INTEGER NOT NULL DEFAULT 0,
  DateTime INTEGER NOT NULL DEFAULT 0,
  FullName TEXT NOT NULL DEFAULT '',
  CityName TEXT NOT NULL DEFAULT '',
  TeamPrefix TEXT NOT NULL DEFAULT '',
  TeamSuffix TEXT NOT NULL DEFAULT '',
  AreaName TEXT NOT NULL DEFAULT '',
  CountryName TEXT NOT NULL DEFAULT '',
  FullCountryName TEXT NOT NULL DEFAULT '',
  FullCityName TEXT NOT NULL DEFAULT '',
  FullAreaName TEXT NOT NULL DEFAULT '',
  FullCityNameAlt TEXT NOT NULL DEFAULT '',
  TeamName TEXT NOT NULL DEFAULT '',
  Conference TEXT NOT NULL DEFAULT '',
  ConferenceFullName TEXT NOT NULL DEFAULT '',
  Division TEXT NOT NULL DEFAULT '',
  DivisionFullName TEXT NOT NULL DEFAULT '',
  LeagueName TEXT NOT NULL DEFAULT '',
  LeagueFullName TEXT NOT NULL DEFAULT '',
  ArenaName TEXT NOT NULL DEFAULT '',
  FullArenaName TEXT NOT NULL DEFAULT '',
  Affiliates TEXT NOT NULL DEFAULT '',
  GamesPlayed INTEGER NOT NULL DEFAULT 0,
  GamesPlayedHome INTEGER NOT NULL DEFAULT 0,
  GamesPlayedAway INTEGER NOT NULL DEFAULT 0,
  Ties INTEGER NOT NULL DEFAULT 0,
  Wins INTEGER NOT NULL DEFAULT 0,
  OTWins INTEGER NOT NULL DEFAULT 0,
  SOWins INTEGER NOT NULL DEFAULT 0,
  OTSOWins INTEGER NOT NULL DEFAULT 0,
  TWins INTEGER NOT NULL DEFAULT 0,
  Losses INTEGER NOT NULL DEFAULT 0,
  OTLosses INTEGER NOT NULL DEFAULT 0,
  SOLosses INTEGER NOT NULL DEFAULT 0,
  OTSOLosses INTEGER NOT NULL DEFAULT 0,
  TLosses INTEGER NOT NULL DEFAULT 0,
  ROW INTEGER NOT NULL DEFAULT 0,
  ROT INTEGER NOT NULL DEFAULT 0,
  ShutoutWins INTEGER NOT NULL DEFAULT 0,
  ShutoutLosses INTEGER NOT NULL DEFAULT 0,
  HomeRecord TEXT NOT NULL DEFAULT '0:0:0:0',
  AwayRecord TEXT NOT NULL DEFAULT '0:0:0:0',
  Shootouts TEXT NOT NULL DEFAULT '0:0',
  GoalsFor INTEGER NOT NULL DEFAULT 0,
  GoalsAgainst INTEGER NOT NULL DEFAULT 0,
  GoalsDifference INTEGER NOT NULL DEFAULT 0,
  SOGFor INTEGER NOT NULL DEFAULT 0,
  SOGAgainst INTEGER NOT NULL DEFAULT 0,
  SOGDifference INTEGER NOT NULL DEFAULT 0,
  ShotsBlockedFor INTEGER NOT NULL DEFAULT 0,
  ShotsBlockedAgainst INTEGER NOT NULL DEFAULT 0,
  ShotsBlockedDifference INTEGER NOT NULL DEFAULT 0,
  PPGFor INTEGER NOT NULL DEFAULT 0,
  PPGAgainst INTEGER NOT NULL DEFAULT 0,
  PPGDifference INTEGER NOT NULL DEFAULT 0,
  SHGFor INTEGER NOT NULL DEFAULT 0,
  SHGAgainst INTEGER NOT NULL DEFAULT 0,
  SHGDifference INTEGER NOT NULL DEFAULT 0,
  PenaltiesFor INTEGER NOT NULL DEFAULT 0,
  PenaltiesAgainst INTEGER NOT NULL DEFAULT 0,
  PenaltiesDifference INTEGER NOT NULL DEFAULT 0,
  PIMFor INTEGER NOT NULL DEFAULT 0,
  PIMAgainst INTEGER NOT NULL DEFAULT 0,
  PIMDifference INTEGER NOT NULL DEFAULT 0,
  HITSFor INTEGER NOT NULL DEFAULT 0,
  HITSAgainst INTEGER NOT NULL DEFAULT 0,
  HITSDifference INTEGER NOT NULL DEFAULT 0,
  TakeAways INTEGER NOT NULL DEFAULT 0,
  GiveAways INTEGER NOT NULL DEFAULT 0,
  TAGADifference INTEGER NOT NULL DEFAULT 0,
  FaceoffWins INTEGER NOT NULL DEFAULT 0,
  FaceoffLosses INTEGER NOT NULL DEFAULT 0,
  FaceoffDifference INTEGER NOT NULL DEFAULT 0,
  Points INTEGER NOT NULL DEFAULT 0,
  PCT REAL NOT NULL DEFAULT 0,
  LastTen TEXT NOT NULL DEFAULT '0:0:0:0',
  Streak TEXT NOT NULL DEFAULT 'None'
);

--
-- Dumping data for table AHLTeams
--

INSERT INTO AHLTeams (id, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(1, 19421000, 0, 194210000000, "Buffalo Bisons", "Buffalo", "Buffalo", "", "NY", "USA", "United States", "Buffalo, NY", "New York", "Buffalo, New York", "Bisons", "", " Conference", "", " Division", "AHL", "American Hockey League", "Buffalo Memorial Auditorium", "Buffalo Memorial Auditorium, Buffalo", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(2, 19421000, 0, 194210000000, "Cleveland Barons", "Cleveland", "Cleveland", "", "OH", "USA", "United States", "Cleveland, OH", "Ohio", "Cleveland, Ohio", "Barons", "", " Conference", "", " Division", "AHL", "American Hockey League", "Cleveland Arena", "Cleveland Arena, Cleveland", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(3, 19421000, 0, 194210000000, "Hershey Red Wings", "Hershey", "Hershey", "", "PA", "USA", "United States", "Hershey, PA", "Pennsylvania", "Hershey, Pennsylvania", "Red Wings", "", " Conference", "", " Division", "AHL", "American Hockey League", "Hersheypark Arena", "Hersheypark Arena, Hershey", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(4, 19421000, 0, 194210000000, "Indianapolis Capitals", "Indianapolis", "Indianapolis", "", "IN", "USA", "United States", "Indianapolis, IN", "Indiana", "Indianapolis, Indiana", "Capitals", "", " Conference", "", " Division", "AHL", "American Hockey League", "Indiana State Fairgrounds Coliseum", "Indiana State Fairgrounds Coliseum, Indianapolis", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(5, 19421000, 0, 194210000000, "Philadelphia Rockets", "Philadelphia", "Philadelphia", "", "PA", "USA", "United States", "Philadelphia, PA", "Pennsylvania", "Philadelphia, Pennsylvania", "Rockets", "", " Conference", "", " Division", "AHL", "American Hockey League", "Philadelphia Arena", "Philadelphia Arena, Philadelphia", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(6, 19421000, 0, 194210000000, "Pittsburgh Hornets", "Pittsburgh", "Pittsburgh", "", "PA", "USA", "United States", "Pittsburgh, PA", "Pennsylvania", "Pittsburgh, Pennsylvania", "Hornets", "", " Conference", "", " Division", "AHL", "American Hockey League", "Duquesne Gardens", "Duquesne Gardens, Pittsburgh", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(7, 19421000, 0, 194210000000, "Providence Reds", "Providence", "Providence", "", "RI", "USA", "United States", "Providence, RI", "Rhode Island", "Providence, Rhode Island", "Reds", "", " Conference", "", " Division", "AHL", "American Hockey League", "Rhode Island Auditorium", "Rhode Island Auditorium, Providence", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(8, 19421000, 0, 194210000000, "Springfield Indians", "West Springfield", "Springfield", "", "MA", "USA", "United States", "West Springfield, MA", "Massachusetts", "West Springfield, Massachusetts", "Indians", "", " Conference", "", " Division", "AHL", "American Hockey League", "Eastern States Coliseum", "Eastern States Coliseum, West Springfield", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO AHLTeams (id, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(9, 19421000, 0, 194210000000, "Washington Lions", "Washington", "Washington", "", "DC", "USA", "United States", "Washington, DC", "District of Columbia", "Washington, District of Columbia", "Lions", "", " Conference", "", " Division", "AHL", "American Hockey League", "Washington Coliseum", "Washington Coliseum, Washington", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");

-- --------------------------------------------------------

--
-- Table structure for table AHLStats
--

DROP TABLE IF EXISTS AHLStats;

CREATE TABLE AHLStats (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  TeamID INTEGER NOT NULL DEFAULT 0,
  Date INTEGER NOT NULL DEFAULT 0,
  Time INTEGER NOT NULL DEFAULT 0,
  DateTime INTEGER NOT NULL DEFAULT 0,
  FullName TEXT NOT NULL DEFAULT '',
  CityName TEXT NOT NULL DEFAULT '',
  TeamPrefix TEXT NOT NULL DEFAULT '',
  TeamSuffix TEXT NOT NULL DEFAULT '',
  AreaName TEXT NOT NULL DEFAULT '',
  CountryName TEXT NOT NULL DEFAULT '',
  FullCountryName TEXT NOT NULL DEFAULT '',
  FullCityName TEXT NOT NULL DEFAULT '',
  FullAreaName TEXT NOT NULL DEFAULT '',
  FullCityNameAlt TEXT NOT NULL DEFAULT '',
  TeamName TEXT NOT NULL DEFAULT '',
  Conference TEXT NOT NULL DEFAULT '',
  ConferenceFullName TEXT NOT NULL DEFAULT '',
  Division TEXT NOT NULL DEFAULT '',
  DivisionFullName TEXT NOT NULL DEFAULT '',
  LeagueName TEXT NOT NULL DEFAULT '',
  LeagueFullName TEXT NOT NULL DEFAULT '',
  ArenaName TEXT NOT NULL DEFAULT '',
  FullArenaName TEXT NOT NULL DEFAULT '',
  Affiliates TEXT NOT NULL DEFAULT '',
  GamesPlayed INTEGER NOT NULL DEFAULT 0,
  GamesPlayedHome INTEGER NOT NULL DEFAULT 0,
  GamesPlayedAway INTEGER NOT NULL DEFAULT 0,
  Ties INTEGER NOT NULL DEFAULT 0,
  Wins INTEGER NOT NULL DEFAULT 0,
  OTWins INTEGER NOT NULL DEFAULT 0,
  SOWins INTEGER NOT NULL DEFAULT 0,
  OTSOWins INTEGER NOT NULL DEFAULT 0,
  TWins INTEGER NOT NULL DEFAULT 0,
  Losses INTEGER NOT NULL DEFAULT 0,
  OTLosses INTEGER NOT NULL DEFAULT 0,
  SOLosses INTEGER NOT NULL DEFAULT 0,
  OTSOLosses INTEGER NOT NULL DEFAULT 0,
  TLosses INTEGER NOT NULL DEFAULT 0,
  ROW INTEGER NOT NULL DEFAULT 0,
  ROT INTEGER NOT NULL DEFAULT 0,
  ShutoutWins INTEGER NOT NULL DEFAULT 0,
  ShutoutLosses INTEGER NOT NULL DEFAULT 0,
  HomeRecord TEXT NOT NULL DEFAULT '0:0:0:0',
  AwayRecord TEXT NOT NULL DEFAULT '0:0:0:0',
  Shootouts TEXT NOT NULL DEFAULT '0:0',
  GoalsFor INTEGER NOT NULL DEFAULT 0,
  GoalsAgainst INTEGER NOT NULL DEFAULT 0,
  GoalsDifference INTEGER NOT NULL DEFAULT 0,
  SOGFor INTEGER NOT NULL DEFAULT 0,
  SOGAgainst INTEGER NOT NULL DEFAULT 0,
  SOGDifference INTEGER NOT NULL DEFAULT 0,
  ShotsBlockedFor INTEGER NOT NULL DEFAULT 0,
  ShotsBlockedAgainst INTEGER NOT NULL DEFAULT 0,
  ShotsBlockedDifference INTEGER NOT NULL DEFAULT 0,
  PPGFor INTEGER NOT NULL DEFAULT 0,
  PPGAgainst INTEGER NOT NULL DEFAULT 0,
  PPGDifference INTEGER NOT NULL DEFAULT 0,
  SHGFor INTEGER NOT NULL DEFAULT 0,
  SHGAgainst INTEGER NOT NULL DEFAULT 0,
  SHGDifference INTEGER NOT NULL DEFAULT 0,
  PenaltiesFor INTEGER NOT NULL DEFAULT 0,
  PenaltiesAgainst INTEGER NOT NULL DEFAULT 0,
  PenaltiesDifference INTEGER NOT NULL DEFAULT 0,
  PIMFor INTEGER NOT NULL DEFAULT 0,
  PIMAgainst INTEGER NOT NULL DEFAULT 0,
  PIMDifference INTEGER NOT NULL DEFAULT 0,
  HITSFor INTEGER NOT NULL DEFAULT 0,
  HITSAgainst INTEGER NOT NULL DEFAULT 0,
  HITSDifference INTEGER NOT NULL DEFAULT 0,
  TakeAways INTEGER NOT NULL DEFAULT 0,
  GiveAways INTEGER NOT NULL DEFAULT 0,
  TAGADifference INTEGER NOT NULL DEFAULT 0,
  FaceoffWins INTEGER NOT NULL DEFAULT 0,
  FaceoffLosses INTEGER NOT NULL DEFAULT 0,
  FaceoffDifference INTEGER NOT NULL DEFAULT 0,
  Points INTEGER NOT NULL DEFAULT 0,
  PCT REAL NOT NULL DEFAULT 0,
  LastTen TEXT NOT NULL DEFAULT '0:0:0:0',
  Streak TEXT NOT NULL DEFAULT 'None'
);

--
-- Dumping data for table AHLStats
--

INSERT INTO AHLStats (id, TeamID, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(1, 1, 19421000, 0, 194210000000, "Buffalo Bisons", "Buffalo", "Buffalo", "", "NY", "USA", "United States", "Buffalo, NY", "New York", "Buffalo, New York", "Bisons", "", " Conference", "", " Division", "AHL", "American Hockey League", "Buffalo Memorial Auditorium", "Buffalo Memorial Auditorium, Buffalo", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(2, 2, 19421000, 0, 194210000000, "Cleveland Barons", "Cleveland", "Cleveland", "", "OH", "USA", "United States", "Cleveland, OH", "Ohio", "Cleveland, Ohio", "Barons", "", " Conference", "", " Division", "AHL", "American Hockey League", "Cleveland Arena", "Cleveland Arena, Cleveland", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(3, 3, 19421000, 0, 194210000000, "Hershey Red Wings", "Hershey", "Hershey", "", "PA", "USA", "United States", "Hershey, PA", "Pennsylvania", "Hershey, Pennsylvania", "Red Wings", "", " Conference", "", " Division", "AHL", "American Hockey League", "Hersheypark Arena", "Hersheypark Arena, Hershey", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(4, 4, 19421000, 0, 194210000000, "Indianapolis Capitals", "Indianapolis", "Indianapolis", "", "IN", "USA", "United States", "Indianapolis, IN", "Indiana", "Indianapolis, Indiana", "Capitals", "", " Conference", "", " Division", "AHL", "American Hockey League", "Indiana State Fairgrounds Coliseum", "Indiana State Fairgrounds Coliseum, Indianapolis", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(5, 5, 19421000, 0, 194210000000, "Philadelphia Rockets", "Philadelphia", "Philadelphia", "", "PA", "USA", "United States", "Philadelphia, PA", "Pennsylvania", "Philadelphia, Pennsylvania", "Rockets", "", " Conference", "", " Division", "AHL", "American Hockey League", "Philadelphia Arena", "Philadelphia Arena, Philadelphia", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(6, 6, 19421000, 0, 194210000000, "Pittsburgh Hornets", "Pittsburgh", "Pittsburgh", "", "PA", "USA", "United States", "Pittsburgh, PA", "Pennsylvania", "Pittsburgh, Pennsylvania", "Hornets", "", " Conference", "", " Division", "AHL", "American Hockey League", "Duquesne Gardens", "Duquesne Gardens, Pittsburgh", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(7, 7, 19421000, 0, 194210000000, "Providence Reds", "Providence", "Providence", "", "RI", "USA", "United States", "Providence, RI", "Rhode Island", "Providence, Rhode Island", "Reds", "", " Conference", "", " Division", "AHL", "American Hockey League", "Rhode Island Auditorium", "Rhode Island Auditorium, Providence", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(8, 8, 19421000, 0, 194210000000, "Springfield Indians", "West Springfield", "Springfield", "", "MA", "USA", "United States", "West Springfield, MA", "Massachusetts", "West Springfield, Massachusetts", "Indians", "", " Conference", "", " Division", "AHL", "American Hockey League", "Eastern States Coliseum", "Eastern States Coliseum, West Springfield", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO AHLStats (id, TeamID, Date, Time, DateTime, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, ConferenceFullName, Division, DivisionFullName, LeagueName, LeagueFullName, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(9, 9, 19421000, 0, 194210000000, "Washington Lions", "Washington", "Washington", "", "DC", "USA", "United States", "Washington, DC", "District of Columbia", "Washington, District of Columbia", "Lions", "", " Conference", "", " Division", "AHL", "American Hockey League", "Washington Coliseum", "Washington Coliseum, Washington", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");

-- --------------------------------------------------------

--
-- Table structure for table AHLGameStats
--

DROP TABLE IF EXISTS AHLGameStats;

CREATE TABLE AHLGameStats (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  GameID INTEGER NOT NULL DEFAULT 0,
  TeamID INTEGER NOT NULL DEFAULT 0,
  Date INTEGER NOT NULL DEFAULT 0,
  Time INTEGER NOT NULL DEFAULT 0,
  DateTime INTEGER NOT NULL DEFAULT 0,
  FullName TEXT NOT NULL DEFAULT '',
  CityName TEXT NOT NULL DEFAULT '',
  TeamPrefix TEXT NOT NULL DEFAULT '',
  TeamSuffix TEXT NOT NULL DEFAULT '',
  AreaName TEXT NOT NULL DEFAULT '',
  CountryName TEXT NOT NULL DEFAULT '',
  FullCountryName TEXT NOT NULL DEFAULT '',
  FullCityName TEXT NOT NULL DEFAULT '',
  FullAreaName TEXT NOT NULL DEFAULT '',
  FullCityNameAlt TEXT NOT NULL DEFAULT '',
  TeamName TEXT NOT NULL DEFAULT '',
  Conference TEXT NOT NULL DEFAULT '',
  ConferenceFullName TEXT NOT NULL DEFAULT '',
  Division TEXT NOT NULL DEFAULT '',
  DivisionFullName TEXT NOT NULL DEFAULT '',
  LeagueName TEXT NOT NULL DEFAULT '',
  LeagueFullName TEXT NOT NULL DEFAULT '',
  ArenaName TEXT NOT NULL DEFAULT '',
  FullArenaName TEXT NOT NULL DEFAULT '',
  Affiliates TEXT NOT NULL DEFAULT '',
  GoalsFor INTEGER NOT NULL DEFAULT 0,
  GoalsAgainst INTEGER NOT NULL DEFAULT 0,
  GoalsDifference INTEGER NOT NULL DEFAULT 0,
  SOGFor INTEGER NOT NULL DEFAULT 0,
  SOGAgainst INTEGER NOT NULL DEFAULT 0,
  SOGDifference INTEGER NOT NULL DEFAULT 0,
  ShotsBlockedFor INTEGER NOT NULL DEFAULT 0,
  ShotsBlockedAgainst INTEGER NOT NULL DEFAULT 0,
  ShotsBlockedDifference INTEGER NOT NULL DEFAULT 0,
  PPGFor INTEGER NOT NULL DEFAULT 0,
  PPGAgainst INTEGER NOT NULL DEFAULT 0,
  PPGDifference INTEGER NOT NULL DEFAULT 0,
  SHGFor INTEGER NOT NULL DEFAULT 0,
  SHGAgainst INTEGER NOT NULL DEFAULT 0,
  SHGDifference INTEGER NOT NULL DEFAULT 0,
  PenaltiesFor INTEGER NOT NULL DEFAULT 0,
  PenaltiesAgainst INTEGER NOT NULL DEFAULT 0,
  PenaltiesDifference INTEGER NOT NULL DEFAULT 0,
  PIMFor INTEGER NOT NULL DEFAULT 0,
  PIMAgainst INTEGER NOT NULL DEFAULT 0,
  PIMDifference INTEGER NOT NULL DEFAULT 0,
  HITSFor INTEGER NOT NULL DEFAULT 0,
  HITSAgainst INTEGER NOT NULL DEFAULT 0,
  HITSDifference INTEGER NOT NULL DEFAULT 0,
  TakeAways INTEGER NOT NULL DEFAULT 0,
  GiveAways INTEGER NOT NULL DEFAULT 0,
  TAGADifference INTEGER NOT NULL DEFAULT 0,
  FaceoffWins INTEGER NOT NULL DEFAULT 0,
  FaceoffLosses INTEGER NOT NULL DEFAULT 0,
  FaceoffDifference INTEGER NOT NULL DEFAULT 0
);

--
-- Dumping data for table AHLGameStats
--


-- --------------------------------------------------------

--
-- Table structure for table AHLGames
--

DROP TABLE IF EXISTS AHLGames;

CREATE TABLE AHLGames (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Date INTEGER NOT NULL DEFAULT 0,
  Time INTEGER NOT NULL DEFAULT 0,
  DateTime INTEGER NOT NULL DEFAULT 0,
  HomeTeam TEXT NOT NULL DEFAULT '',
  AwayTeam TEXT NOT NULL DEFAULT '',
  AtArena TEXT NOT NULL DEFAULT '',
  TeamScorePeriods TEXT NOT NULL DEFAULT '',
  TeamFullScore TEXT NOT NULL DEFAULT '',
  ShotsOnGoal TEXT NOT NULL DEFAULT '',
  FullShotsOnGoal TEXT NOT NULL DEFAULT '',
  ShotsBlocked TEXT NOT NULL DEFAULT '',
  FullShotsBlocked TEXT NOT NULL DEFAULT '',
  PowerPlays TEXT NOT NULL DEFAULT '',
  FullPowerPlays TEXT NOT NULL DEFAULT '',
  ShortHanded TEXT NOT NULL DEFAULT '',
  FullShortHanded TEXT NOT NULL DEFAULT '',
  Penalties TEXT NOT NULL DEFAULT '',
  FullPenalties TEXT NOT NULL DEFAULT '',
  PenaltyMinutes TEXT NOT NULL DEFAULT '',
  FullPenaltyMinutes TEXT NOT NULL DEFAULT '',
  HitsPerPeriod TEXT NOT NULL DEFAULT '',
  FullHitsPerPeriod TEXT NOT NULL DEFAULT '',
  TakeAways TEXT NOT NULL DEFAULT '',
  FullTakeAways TEXT NOT NULL DEFAULT '',
  GiveAways TEXT NOT NULL DEFAULT '',
  FullGiveAways TEXT NOT NULL DEFAULT '',
  FaceoffWins TEXT NOT NULL DEFAULT '',
  FullFaceoffWins TEXT NOT NULL DEFAULT '',
  NumberPeriods INTEGER NOT NULL DEFAULT 0,
  TeamWin TEXT NOT NULL DEFAULT '',
  TeamLost TEXT NOT NULL DEFAULT '',
  TieGame INTEGER NOT NULL DEFAULT 0,
  IsPlayOffGame INTEGER NOT NULL DEFAULT 0
);

--
-- Dumping data for table AHLGames
--


-- --------------------------------------------------------

