-- PyHockeyStats SQL Dumper
-- version 0.2.1 RC 1
-- https://github.com/GameMaker2k/Neo-Hockey-Test
--
-- Generation Time: February 16, 2020 at 03:14 AM
-- SQLite Server version: 3.31.1
-- PySQLite version: 2.6.0
-- Python Version: 3.8.1

--
-- Database: :memory:
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
  NumberOfDivisions INTEGER NOT NULL DEFAULT ''
);

--
-- Dumping data for table HockeyLeagues
--

INSERT INTO HockeyLeagues (id, LeagueName, LeagueFullName, CountryName, FullCountryName, Date, PlayOffFMT, OrderType, NumberOfTeams, NumberOfConferences, NumberOfDivisions) VALUES 
(1, "HOL", "Hockey League", "USA", "United States", 20171001, "Division=1,Conference=1", "ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", 8, 2, 4);
INSERT INTO HockeyLeagues (id, LeagueName, LeagueFullName, CountryName, FullCountryName, Date, PlayOffFMT, OrderType, NumberOfTeams, NumberOfConferences, NumberOfDivisions) VALUES 
(2, "MIL", "Minor League", "USA", "United States", 20171001, "Division=1,Conference=1", "ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC", 8, 2, 4);

-- --------------------------------------------------------

--
-- Table structure for table HOLConferences
--

DROP TABLE IF EXISTS HOLConferences;

CREATE TABLE HOLConferences (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Conference TEXT NOT NULL DEFAULT '',
  LeagueName TEXT NOT NULL DEFAULT '',
  LeagueFullName TEXT NOT NULL DEFAULT '',
  NumberOfTeams INTEGER NOT NULL DEFAULT 0,
  NumberOfDivisions INTEGER NOT NULL DEFAULT ''
);

--
-- Dumping data for table HOLConferences
--

INSERT INTO HOLConferences (id, Conference, LeagueName, LeagueFullName, NumberOfTeams, NumberOfDivisions) VALUES 
(1, "Conference 1", "HOL", "Hockey League", 4, 2);
INSERT INTO HOLConferences (id, Conference, LeagueName, LeagueFullName, NumberOfTeams, NumberOfDivisions) VALUES 
(2, "Conference 2", "HOL", "Hockey League", 4, 2);

-- --------------------------------------------------------

--
-- Table structure for table HOLDivisions
--

DROP TABLE IF EXISTS HOLDivisions;

CREATE TABLE HOLDivisions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Division TEXT NOT NULL DEFAULT '',
  Conference TEXT NOT NULL DEFAULT '',
  LeagueName TEXT NOT NULL DEFAULT '',
  LeagueFullName TEXT NOT NULL DEFAULT '',
  NumberOfTeams INTEGER NOT NULL DEFAULT ''
);

--
-- Dumping data for table HOLDivisions
--

INSERT INTO HOLDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(1, "Division 1", "Conference 1", "HOL", "Hockey League", 2);
INSERT INTO HOLDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(2, "Division 2", "Conference 1", "HOL", "Hockey League", 2);
INSERT INTO HOLDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(3, "Division 3", "Conference 2", "HOL", "Hockey League", 2);
INSERT INTO HOLDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(4, "Division 4", "Conference 2", "HOL", "Hockey League", 2);

-- --------------------------------------------------------

--
-- Table structure for table HOLArenas
--

DROP TABLE IF EXISTS HOLArenas;

CREATE TABLE HOLArenas (
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
  GamesPlayed INTEGER NOT NULL DEFAULT ''
);

--
-- Dumping data for table HOLArenas
--

INSERT INTO HOLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(1, 1, "Blasters", "Detroit Blasters", "Detroit", "MI", "USA", "United States", "Detroit, MI", "Michigan", "Detroit, Michigan", "DET Arena", "DET Arena, Detroit", 0);
INSERT INTO HOLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(2, 2, "Sabres", "Indianapolis Sabres", "Indianapolis", "IN", "USA", "United States", "Indianapolis, IN", "Indiana", "Indianapolis, Indiana", "IND Arena", "IND Arena, Indianapolis", 0);
INSERT INTO HOLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(3, 3, "River Bandits", "Chicago River Bandits", "Chicago", "IL", "USA", "United States", "Chicago, IL", "Illionis", "Chicago, Illionis", "CHI Arena", "CHI Arena, Chicago", 0);
INSERT INTO HOLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(4, 4, "Chariots", "Kansas City Chariots", "Kansas City", "MO", "USA", "United States", "Kansas City, MO", "Missouri", "Kansas City, Missouri", "KAN Arena", "KAN Arena, Kansas City", 0);
INSERT INTO HOLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(5, 5, "Smoking Guns", "St. Paul Smoking Guns", "St. Paul", "MN", "USA", "United States", "St. Paul, MN", "Minnesota", "St. Paul, Minnesota", "SMO Arena", "SMO Arena, St. Paul", 0);
INSERT INTO HOLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(6, 6, "Armada", "Minneapolis Armada", "Minneapolis", "MN", "USA", "United States", "Minneapolis, MN", "Minnesota", "Minneapolis, Minnesota", "MIN Arena", "MIN Arena, Minneapolis", 0);
INSERT INTO HOLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(7, 7, "Jammers", "Peoria Jammers", "Peoria", "IL", "USA", "United States", "Peoria, IL", "Illionis", "Peoria, Illionis", "PEO Arena", "PEO Arena, Peoria", 0);
INSERT INTO HOLArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(8, 8, "Gears", "Chicago Gears", "Joliet", "IL", "USA", "United States", "Joliet, IL", "Illionis", "Joliet, Illionis", "JOL Arena", "JOL Arena, Joliet", 0);

-- --------------------------------------------------------

--
-- Table structure for table HOLTeams
--

DROP TABLE IF EXISTS HOLTeams;

CREATE TABLE HOLTeams (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Date INTEGER NOT NULL DEFAULT 0,
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
  Division TEXT NOT NULL DEFAULT '',
  LeagueName TEXT NOT NULL DEFAULT '',
  LeagueFullName TEXT NOT NULL DEFAULT '',
  ArenaName TEXT NOT NULL DEFAULT '',
  FullArenaName TEXT NOT NULL DEFAULT '',
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
-- Dumping data for table HOLTeams
--

INSERT INTO HOLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(1, 20171000, "Detroit Blasters", "Detroit", "Detroit", "", "MI", "USA", "United States", "Detroit, MI", "Michigan", "Detroit, Michigan", "Blasters", "Conference 1", "Division 1", "HOL", "Hockey League", "DET Arena", "DET Arena, Detroit", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO HOLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(2, 20171000, "Indianapolis Sabres", "Indianapolis", "Indianapolis", "", "IN", "USA", "United States", "Indianapolis, IN", "Indiana", "Indianapolis, Indiana", "Sabres", "Conference 1", "Division 1", "HOL", "Hockey League", "IND Arena", "IND Arena, Indianapolis", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO HOLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(3, 20171000, "Chicago River Bandits", "Chicago", "Chicago", "", "IL", "USA", "United States", "Chicago, IL", "Illionis", "Chicago, Illionis", "River Bandits", "Conference 1", "Division 2", "HOL", "Hockey League", "CHI Arena", "CHI Arena, Chicago", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO HOLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(4, 20171000, "Kansas City Chariots", "Kansas City", "Kansas City", "", "MO", "USA", "United States", "Kansas City, MO", "Missouri", "Kansas City, Missouri", "Chariots", "Conference 1", "Division 2", "HOL", "Hockey League", "KAN Arena", "KAN Arena, Kansas City", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO HOLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(5, 20171000, "St. Paul Smoking Guns", "St. Paul", "St. Paul", "", "MN", "USA", "United States", "St. Paul, MN", "Minnesota", "St. Paul, Minnesota", "Smoking Guns", "Conference 2", "Division 3", "HOL", "Hockey League", "SMO Arena", "SMO Arena, St. Paul", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO HOLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(6, 20171000, "Minneapolis Armada", "Minneapolis", "Minneapolis", "", "MN", "USA", "United States", "Minneapolis, MN", "Minnesota", "Minneapolis, Minnesota", "Armada", "Conference 2", "Division 3", "HOL", "Hockey League", "MIN Arena", "MIN Arena, Minneapolis", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO HOLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(7, 20171000, "Peoria Jammers", "Peoria", "Peoria", "", "IL", "USA", "United States", "Peoria, IL", "Illionis", "Peoria, Illionis", "Jammers", "Conference 2", "Division 4", "HOL", "Hockey League", "PEO Arena", "PEO Arena, Peoria", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO HOLTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(8, 20171000, "Chicago Gears", "Joliet", "Chicago", "", "IL", "USA", "United States", "Joliet, IL", "Illionis", "Joliet, Illionis", "Gears", "Conference 2", "Division 4", "HOL", "Hockey League", "JOL Arena", "JOL Arena, Joliet", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");

-- --------------------------------------------------------

--
-- Table structure for table HOLStats
--

DROP TABLE IF EXISTS HOLStats;

CREATE TABLE HOLStats (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  TeamID INTEGER NOT NULL DEFAULT 0,
  Date INTEGER NOT NULL DEFAULT 0,
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
  Division TEXT NOT NULL DEFAULT '',
  LeagueName TEXT NOT NULL DEFAULT '',
  LeagueFullName TEXT NOT NULL DEFAULT '',
  ArenaName TEXT NOT NULL DEFAULT '',
  FullArenaName TEXT NOT NULL DEFAULT '',
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
-- Dumping data for table HOLStats
--

INSERT INTO HOLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(1, 1, 20171000, "Detroit Blasters", "Detroit", "Detroit", "", "MI", "USA", "United States", "Detroit, MI", "Michigan", "Detroit, Michigan", "Blasters", "Conference 1", "Division 1", "HOL", "Hockey League", "DET Arena", "DET Arena, Detroit", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO HOLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(2, 2, 20171000, "Indianapolis Sabres", "Indianapolis", "Indianapolis", "", "IN", "USA", "United States", "Indianapolis, IN", "Indiana", "Indianapolis, Indiana", "Sabres", "Conference 1", "Division 1", "HOL", "Hockey League", "IND Arena", "IND Arena, Indianapolis", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO HOLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(3, 3, 20171000, "Chicago River Bandits", "Chicago", "Chicago", "", "IL", "USA", "United States", "Chicago, IL", "Illionis", "Chicago, Illionis", "River Bandits", "Conference 1", "Division 2", "HOL", "Hockey League", "CHI Arena", "CHI Arena, Chicago", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO HOLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(4, 4, 20171000, "Kansas City Chariots", "Kansas City", "Kansas City", "", "MO", "USA", "United States", "Kansas City, MO", "Missouri", "Kansas City, Missouri", "Chariots", "Conference 1", "Division 2", "HOL", "Hockey League", "KAN Arena", "KAN Arena, Kansas City", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO HOLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(5, 5, 20171000, "St. Paul Smoking Guns", "St. Paul", "St. Paul", "", "MN", "USA", "United States", "St. Paul, MN", "Minnesota", "St. Paul, Minnesota", "Smoking Guns", "Conference 2", "Division 3", "HOL", "Hockey League", "SMO Arena", "SMO Arena, St. Paul", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO HOLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(6, 6, 20171000, "Minneapolis Armada", "Minneapolis", "Minneapolis", "", "MN", "USA", "United States", "Minneapolis, MN", "Minnesota", "Minneapolis, Minnesota", "Armada", "Conference 2", "Division 3", "HOL", "Hockey League", "MIN Arena", "MIN Arena, Minneapolis", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO HOLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(7, 7, 20171000, "Peoria Jammers", "Peoria", "Peoria", "", "IL", "USA", "United States", "Peoria, IL", "Illionis", "Peoria, Illionis", "Jammers", "Conference 2", "Division 4", "HOL", "Hockey League", "PEO Arena", "PEO Arena, Peoria", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO HOLStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(8, 8, 20171000, "Chicago Gears", "Joliet", "Chicago", "", "IL", "USA", "United States", "Joliet, IL", "Illionis", "Joliet, Illionis", "Gears", "Conference 2", "Division 4", "HOL", "Hockey League", "JOL Arena", "JOL Arena, Joliet", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");

-- --------------------------------------------------------

--
-- Table structure for table HOLGameStats
--

DROP TABLE IF EXISTS HOLGameStats;

CREATE TABLE HOLGameStats (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  GameID INTEGER NOT NULL DEFAULT 0,
  Date INTEGER NOT NULL DEFAULT 0,
  TeamID INTEGER NOT NULL DEFAULT 0,
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
  Division TEXT NOT NULL DEFAULT '',
  LeagueName TEXT NOT NULL DEFAULT '',
  LeagueFullName TEXT NOT NULL DEFAULT '',
  ArenaName TEXT NOT NULL DEFAULT '',
  FullArenaName TEXT NOT NULL DEFAULT '',
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
-- Dumping data for table HOLGameStats
--


-- --------------------------------------------------------

--
-- Table structure for table HOLGames
--

DROP TABLE IF EXISTS HOLGames;

CREATE TABLE HOLGames (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Date INTEGER NOT NULL DEFAULT 0,
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
  IsPlayOffGame INTEGER NOT NULL DEFAULT ''
);

--
-- Dumping data for table HOLGames
--


-- --------------------------------------------------------

--
-- Table structure for table MILConferences
--

DROP TABLE IF EXISTS MILConferences;

CREATE TABLE MILConferences (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Conference TEXT NOT NULL DEFAULT '',
  LeagueName TEXT NOT NULL DEFAULT '',
  LeagueFullName TEXT NOT NULL DEFAULT '',
  NumberOfTeams INTEGER NOT NULL DEFAULT 0,
  NumberOfDivisions INTEGER NOT NULL DEFAULT ''
);

--
-- Dumping data for table MILConferences
--

INSERT INTO MILConferences (id, Conference, LeagueName, LeagueFullName, NumberOfTeams, NumberOfDivisions) VALUES 
(1, "Conference 1", "MIL", "Minor League", 4, 2);
INSERT INTO MILConferences (id, Conference, LeagueName, LeagueFullName, NumberOfTeams, NumberOfDivisions) VALUES 
(2, "Conference 2", "MIL", "Minor League", 4, 2);

-- --------------------------------------------------------

--
-- Table structure for table MILDivisions
--

DROP TABLE IF EXISTS MILDivisions;

CREATE TABLE MILDivisions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Division TEXT NOT NULL DEFAULT '',
  Conference TEXT NOT NULL DEFAULT '',
  LeagueName TEXT NOT NULL DEFAULT '',
  LeagueFullName TEXT NOT NULL DEFAULT '',
  NumberOfTeams INTEGER NOT NULL DEFAULT ''
);

--
-- Dumping data for table MILDivisions
--

INSERT INTO MILDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(1, "Division 1", "Conference 1", "MIL", "Minor League", 2);
INSERT INTO MILDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(2, "Division 2", "Conference 1", "MIL", "Minor League", 2);
INSERT INTO MILDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(3, "Division 3", "Conference 2", "MIL", "Minor League", 2);
INSERT INTO MILDivisions (id, Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES 
(4, "Division 4", "Conference 2", "MIL", "Minor League", 2);

-- --------------------------------------------------------

--
-- Table structure for table MILArenas
--

DROP TABLE IF EXISTS MILArenas;

CREATE TABLE MILArenas (
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
  GamesPlayed INTEGER NOT NULL DEFAULT ''
);

--
-- Dumping data for table MILArenas
--

INSERT INTO MILArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(1, 1, "Loggerheads", "Northview Loggerheads", "Northview", "MI", "USA", "United States", "Northview, MI", "Michigan", "Northview, Michigan", "NOR Arena", "NOR Arena, Northview", 0);
INSERT INTO MILArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(2, 2, "Caravans", "Gulivoire Park Caravans", "Gulivoire Park", "IN", "USA", "United States", "Gulivoire Park, IN", "Indiana", "Gulivoire Park, Indiana", "GUL Arena", "GUL Arena, Gulivoire Park", 0);
INSERT INTO MILArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(3, 3, "Ramblers", "Wheeling Ramblers", "Wheeling", "IL", "USA", "United States", "Wheeling, IL", "Illionis", "Wheeling, Illionis", "WHE Arena", "WHE Arena, Wheeling", 0);
INSERT INTO MILArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(4, 4, "Skychiefs", "Columbia Skychiefs", "Columbia", "MO", "USA", "United States", "Columbia, MO", "Missouri", "Columbia, Missouri", "COL Arena", "COL Arena, Columbia", 0);
INSERT INTO MILArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(5, 5, "Vipers", "Winona Vipers", "Winona", "MN", "USA", "United States", "Winona, MN", "Minnesota", "Winona, Minnesota", "WIN Arena", "WIN Arena, Winona", 0);
INSERT INTO MILArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(6, 6, "Chaos", "New Hope Chaos", "New Hope", "MN", "USA", "United States", "New Hope, MN", "Minnesota", "New Hope, Minnesota", "NEW Arena", "NEW Arena, New Hope", 0);
INSERT INTO MILArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(7, 7, "Gappers", "Tinley Park Gappers", "Tinley Park", "IL", "USA", "United States", "Tinley Park, IL", "Illionis", "Tinley Park, Illionis", "TIN Arena", "TIN Arena, Tinley Park", 0);
INSERT INTO MILArenas (id, TeamID, TeamName, TeamFullName, CityName, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, ArenaName, FullArenaName, GamesPlayed) VALUES 
(8, 8, "Spirits", "Franklin Park Spirits", "Franklin Park", "IL", "USA", "United States", "Franklin Park, IL", "Illionis", "Franklin Park, Illionis", "FRA Arena", "FRA Arena, Franklin Park", 0);

-- --------------------------------------------------------

--
-- Table structure for table MILTeams
--

DROP TABLE IF EXISTS MILTeams;

CREATE TABLE MILTeams (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Date INTEGER NOT NULL DEFAULT 0,
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
  Division TEXT NOT NULL DEFAULT '',
  LeagueName TEXT NOT NULL DEFAULT '',
  LeagueFullName TEXT NOT NULL DEFAULT '',
  ArenaName TEXT NOT NULL DEFAULT '',
  FullArenaName TEXT NOT NULL DEFAULT '',
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
-- Dumping data for table MILTeams
--

INSERT INTO MILTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(1, 20171000, "Northview Loggerheads", "Northview", "Northview", "", "MI", "USA", "United States", "Northview, MI", "Michigan", "Northview, Michigan", "Loggerheads", "Conference 1", "Division 1", "MIL", "Minor League", "NOR Arena", "NOR Arena, Northview", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO MILTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(2, 20171000, "Gulivoire Park Caravans", "Gulivoire Park", "Gulivoire Park", "", "IN", "USA", "United States", "Gulivoire Park, IN", "Indiana", "Gulivoire Park, Indiana", "Caravans", "Conference 1", "Division 1", "MIL", "Minor League", "GUL Arena", "GUL Arena, Gulivoire Park", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO MILTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(3, 20171000, "Wheeling Ramblers", "Wheeling", "Wheeling", "", "IL", "USA", "United States", "Wheeling, IL", "Illionis", "Wheeling, Illionis", "Ramblers", "Conference 1", "Division 2", "MIL", "Minor League", "WHE Arena", "WHE Arena, Wheeling", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO MILTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(4, 20171000, "Columbia Skychiefs", "Columbia", "Columbia", "", "MO", "USA", "United States", "Columbia, MO", "Missouri", "Columbia, Missouri", "Skychiefs", "Conference 1", "Division 2", "MIL", "Minor League", "COL Arena", "COL Arena, Columbia", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO MILTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(5, 20171000, "Winona Vipers", "Winona", "Winona", "", "MN", "USA", "United States", "Winona, MN", "Minnesota", "Winona, Minnesota", "Vipers", "Conference 2", "Division 3", "MIL", "Minor League", "WIN Arena", "WIN Arena, Winona", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO MILTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(6, 20171000, "New Hope Chaos", "New Hope", "New Hope", "", "MN", "USA", "United States", "New Hope, MN", "Minnesota", "New Hope, Minnesota", "Chaos", "Conference 2", "Division 3", "MIL", "Minor League", "NEW Arena", "NEW Arena, New Hope", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO MILTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(7, 20171000, "Tinley Park Gappers", "Tinley Park", "Tinley Park", "", "IL", "USA", "United States", "Tinley Park, IL", "Illionis", "Tinley Park, Illionis", "Gappers", "Conference 2", "Division 4", "MIL", "Minor League", "TIN Arena", "TIN Arena, Tinley Park", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO MILTeams (id, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(8, 20171000, "Franklin Park Spirits", "Franklin Park", "Franklin Park", "", "IL", "USA", "United States", "Franklin Park, IL", "Illionis", "Franklin Park, Illionis", "Spirits", "Conference 2", "Division 4", "MIL", "Minor League", "FRA Arena", "FRA Arena, Franklin Park", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");

-- --------------------------------------------------------

--
-- Table structure for table MILStats
--

DROP TABLE IF EXISTS MILStats;

CREATE TABLE MILStats (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  TeamID INTEGER NOT NULL DEFAULT 0,
  Date INTEGER NOT NULL DEFAULT 0,
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
  Division TEXT NOT NULL DEFAULT '',
  LeagueName TEXT NOT NULL DEFAULT '',
  LeagueFullName TEXT NOT NULL DEFAULT '',
  ArenaName TEXT NOT NULL DEFAULT '',
  FullArenaName TEXT NOT NULL DEFAULT '',
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
-- Dumping data for table MILStats
--

INSERT INTO MILStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(1, 1, 20171000, "Northview Loggerheads", "Northview", "Northview", "", "MI", "USA", "United States", "Northview, MI", "Michigan", "Northview, Michigan", "Loggerheads", "Conference 1", "Division 1", "MIL", "Minor League", "NOR Arena", "NOR Arena, Northview", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO MILStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(2, 2, 20171000, "Gulivoire Park Caravans", "Gulivoire Park", "Gulivoire Park", "", "IN", "USA", "United States", "Gulivoire Park, IN", "Indiana", "Gulivoire Park, Indiana", "Caravans", "Conference 1", "Division 1", "MIL", "Minor League", "GUL Arena", "GUL Arena, Gulivoire Park", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO MILStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(3, 3, 20171000, "Wheeling Ramblers", "Wheeling", "Wheeling", "", "IL", "USA", "United States", "Wheeling, IL", "Illionis", "Wheeling, Illionis", "Ramblers", "Conference 1", "Division 2", "MIL", "Minor League", "WHE Arena", "WHE Arena, Wheeling", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO MILStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(4, 4, 20171000, "Columbia Skychiefs", "Columbia", "Columbia", "", "MO", "USA", "United States", "Columbia, MO", "Missouri", "Columbia, Missouri", "Skychiefs", "Conference 1", "Division 2", "MIL", "Minor League", "COL Arena", "COL Arena, Columbia", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO MILStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(5, 5, 20171000, "Winona Vipers", "Winona", "Winona", "", "MN", "USA", "United States", "Winona, MN", "Minnesota", "Winona, Minnesota", "Vipers", "Conference 2", "Division 3", "MIL", "Minor League", "WIN Arena", "WIN Arena, Winona", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO MILStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(6, 6, 20171000, "New Hope Chaos", "New Hope", "New Hope", "", "MN", "USA", "United States", "New Hope, MN", "Minnesota", "New Hope, Minnesota", "Chaos", "Conference 2", "Division 3", "MIL", "Minor League", "NEW Arena", "NEW Arena, New Hope", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO MILStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(7, 7, 20171000, "Tinley Park Gappers", "Tinley Park", "Tinley Park", "", "IL", "USA", "United States", "Tinley Park, IL", "Illionis", "Tinley Park, Illionis", "Gappers", "Conference 2", "Division 4", "MIL", "Minor League", "TIN Arena", "TIN Arena, Tinley Park", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");
INSERT INTO MILStats (id, TeamID, Date, FullName, CityName, TeamPrefix, TeamSuffix, AreaName, CountryName, FullCountryName, FullCityName, FullAreaName, FullCityNameAlt, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Ties, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, SHGFor, SHGAgainst, SHGDifference, PenaltiesFor, PenaltiesAgainst, PenaltiesDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES 
(8, 8, 20171000, "Franklin Park Spirits", "Franklin Park", "Franklin Park", "", "IL", "USA", "United States", "Franklin Park, IL", "Illionis", "Franklin Park, Illionis", "Spirits", "Conference 2", "Division 4", "MIL", "Minor League", "FRA Arena", "FRA Arena, Franklin Park", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0:0:0:0", "0:0:0:0", "0:0", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, "0:0:0:0", "None");

-- --------------------------------------------------------

--
-- Table structure for table MILGameStats
--

DROP TABLE IF EXISTS MILGameStats;

CREATE TABLE MILGameStats (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  GameID INTEGER NOT NULL DEFAULT 0,
  Date INTEGER NOT NULL DEFAULT 0,
  TeamID INTEGER NOT NULL DEFAULT 0,
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
  Division TEXT NOT NULL DEFAULT '',
  LeagueName TEXT NOT NULL DEFAULT '',
  LeagueFullName TEXT NOT NULL DEFAULT '',
  ArenaName TEXT NOT NULL DEFAULT '',
  FullArenaName TEXT NOT NULL DEFAULT '',
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
-- Dumping data for table MILGameStats
--


-- --------------------------------------------------------

--
-- Table structure for table MILGames
--

DROP TABLE IF EXISTS MILGames;

CREATE TABLE MILGames (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Date INTEGER NOT NULL DEFAULT 0,
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
  IsPlayOffGame INTEGER NOT NULL DEFAULT ''
);

--
-- Dumping data for table MILGames
--


-- --------------------------------------------------------

