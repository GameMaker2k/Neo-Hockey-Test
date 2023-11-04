BEGIN TRANSACTION;
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
INSERT INTO "AHLArenas" VALUES(1,1,'Sound Tigers','Bridgeport Sound Tigers','Bridgeport','CT','USA','United States','Bridgeport, CT','Connecticut','Bridgeport, Connecticut','Webster Bank Arena','Webster Bank Arena, Bridgeport',0);
INSERT INTO "AHLArenas" VALUES(2,2,'Wolf Pack','Hartford Wolf Pack','Hartford','CT','USA','United States','Hartford, CT','Connecticut','Hartford, Connecticut','XL Center','XL Center, Hartford',0);
INSERT INTO "AHLArenas" VALUES(3,3,'Bears','Hershey Bears','Hershey','PA','USA','United States','Hershey, PA','Pennsylvania','Hershey, Pennsylvania','Giant Center','Giant Center, Hershey',0);
INSERT INTO "AHLArenas" VALUES(4,4,'Phantoms','Lehigh Valley Phantoms','Allentown','PA','USA','United States','Allentown, PA','Pennsylvania','Allentown, Pennsylvania','PPL Center','PPL Center, Allentown',0);
INSERT INTO "AHLArenas" VALUES(5,5,'Pirates','Portland Pirates','Portland','ME','USA','United States','Portland, ME','Maine','Portland, Maine','Cross Insurance Arena','Cross Insurance Arena, Portland',0);
INSERT INTO "AHLArenas" VALUES(6,6,'Bruins','Providence Bruins','Providence','RI','USA','United States','Providence, RI','Rhode Island','Providence, Rhode Island','Dunkin'' Donuts Center','Dunkin'' Donuts Center, Providence',0);
INSERT INTO "AHLArenas" VALUES(7,7,'Falcons','Springfield Falcons','Springfield','MA','USA','United States','Springfield, MA','Massachusetts','Springfield, Massachusetts','MassMutual Center','MassMutual Center, Springfield',0);
INSERT INTO "AHLArenas" VALUES(8,8,'Penguins','Wilkes-Barre/Scranton Penguins','Wilkes-Barre','PA','USA','United States','Wilkes-Barre, PA','Pennsylvania','Wilkes-Barre, Pennsylvania','Mohegan Sun Arena','Mohegan Sun Arena, Wilkes-Barre',0);
INSERT INTO "AHLArenas" VALUES(9,9,'Devils','Albany Devils','Albany','NY','USA','United States','Albany, NY','New York','Albany, New York','Times Union Center','Times Union Center, Albany',0);
INSERT INTO "AHLArenas" VALUES(10,10,'Senators','Binghamton Senators','Binghamton','NY','USA','United States','Binghamton, NY','New York','Binghamton, New York','Floyd L. Maines Veterans Memorial Arena','Floyd L. Maines Veterans Memorial Arena, Binghamton',0);
INSERT INTO "AHLArenas" VALUES(11,11,'Americans','Rochester Americans','Rochester','NY','USA','United States','Rochester, NY','New York','Rochester, New York','Blue Cross Arena','Blue Cross Arena, Rochester',0);
INSERT INTO "AHLArenas" VALUES(12,12,'IceCaps','St. John''s IceCaps','St. John''s','NL','CAN','Canada','St. John''s, NL','Newfoundland and Labrador','St. John''s, Newfoundland and Labrador','Mile One Centre','Mile One Centre, St. John''s',0);
INSERT INTO "AHLArenas" VALUES(13,13,'Crunch','Syracuse Crunch','Syracuse','NY','USA','United States','Syracuse, NY','New York','Syracuse, New York','Oncenter War Memorial Arena','Oncenter War Memorial Arena, Syracuse',0);
INSERT INTO "AHLArenas" VALUES(14,14,'Marlies','Toronto Marlies','Toronto','ON','CAN','Canada','Toronto, ON','Ontario','Toronto, Ontario','Ricoh Coliseum','Ricoh Coliseum, Toronto',0);
INSERT INTO "AHLArenas" VALUES(15,15,'Comets','Utica Comets','Utica','NY','USA','United States','Utica, NY','New York','Utica, New York','Utica Memorial Auditorium','Utica Memorial Auditorium, Utica',0);
INSERT INTO "AHLArenas" VALUES(16,16,'Checkers','Charlotte Checkers','Charlotte','NC','USA','United States','Charlotte, NC','North Carolina','Charlotte, North Carolina','Bojangles Coliseum','Bojangles Coliseum, Charlotte',0);
INSERT INTO "AHLArenas" VALUES(17,17,'Wolves','Chicago Wolves','Rosemont','IL','USA','United States','Rosemont, IL','Illinois','Rosemont, Illinois','Allstate Arena','Allstate Arena, Rosemont',0);
INSERT INTO "AHLArenas" VALUES(18,18,'Griffins','Grand Rapids Griffins','Grand Rapids','MI','USA','United States','Grand Rapids, MI','Michigan','Grand Rapids, Michigan','Van Andel Arena','Van Andel Arena, Grand Rapids',0);
INSERT INTO "AHLArenas" VALUES(19,19,'Wild','Iowa Wild','Des Moines','IA','USA','United States','Des Moines, IA','Iowa','Des Moines, Iowa','Wells Fargo Arena','Wells Fargo Arena, Des Moines',0);
INSERT INTO "AHLArenas" VALUES(20,20,'Monsters','Lake Erie Monsters','Cleveland','OH','USA','United States','Cleveland, OH','Ohio','Cleveland, Ohio','Quicken Loans Arena','Quicken Loans Arena, Cleveland',0);
INSERT INTO "AHLArenas" VALUES(21,21,'Moose','Manitoba Moose','Winnipeg','MB','CAN','Canada','Winnipeg, MB','Manitoba','Winnipeg, Manitoba','MTS Centre','MTS Centre, Winnipeg',0);
INSERT INTO "AHLArenas" VALUES(22,22,'Admirals','Milwaukee Admirals','Milwaukee','WI','USA','United States','Milwaukee, WI','Wisconsin','Milwaukee, Wisconsin','BMO Harris Bradley Center','BMO Harris Bradley Center, Milwaukee',0);
INSERT INTO "AHLArenas" VALUES(23,23,'IceHogs','Rockford IceHogs','Rockford','IL','USA','United States','Rockford, IL','Illinois','Rockford, Illinois','BMO Harris Bank Center','BMO Harris Bank Center, Rockford',0);
INSERT INTO "AHLArenas" VALUES(24,24,'Condors','Bakersfield Condors','Bakersfield','CA','USA','United States','Bakersfield, CA','California','Bakersfield, California','Rabobank Arena','Rabobank Arena, Bakersfield',0);
INSERT INTO "AHLArenas" VALUES(25,25,'Reign','Ontario Reign','Ontario','CA','USA','United States','Ontario, CA','California','Ontario, California','Citizens Business Bank Arena','Citizens Business Bank Arena, Ontario',0);
INSERT INTO "AHLArenas" VALUES(26,26,'Rampage','San Antonio Rampage','San Antonio','TX','USA','United States','San Antonio, TX','Texas','San Antonio, Texas','AT&T Center','AT&T Center, San Antonio',0);
INSERT INTO "AHLArenas" VALUES(27,27,'Gulls','San Diego Gulls','San Diego','CA','USA','United States','San Diego, CA','California','San Diego, California','Valley View Casino Center','Valley View Casino Center, San Diego',0);
INSERT INTO "AHLArenas" VALUES(28,28,'Barracuda','San Jose Barracuda','San Jose','CA','USA','United States','San Jose, CA','California','San Jose, California','SAP Center','SAP Center, San Jose',0);
INSERT INTO "AHLArenas" VALUES(29,29,'Heat','Stockton Heat','Stockton','CA','USA','United States','Stockton, CA','California','Stockton, California','Stockton Arena','Stockton Arena, Stockton',0);
INSERT INTO "AHLArenas" VALUES(30,30,'Stars','Texas Stars','Cedar Park','TX','USA','United States','Cedar Park, TX','Texas','Cedar Park, Texas','Cedar Park Center','Cedar Park Center, Cedar Park',0);
INSERT INTO "AHLArenas" VALUES(31,0,'','','West Sacramento','CA','USA','United States','West Sacramento, CA','California','West Sacramento, California','Raley Field','Raley Field, West Sacramento',0);
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
INSERT INTO "AHLConferences" VALUES(1,'Eastern','','Conference','Eastern Conference','AHL','American Hockey League',15,2);
INSERT INTO "AHLConferences" VALUES(2,'Western','','Conference','Western Conference','AHL','American Hockey League',15,2);
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
INSERT INTO "AHLDivisions" VALUES(1,'Atlantic','','Division','Atlantic Division','Eastern','Eastern Conference','AHL','American Hockey League',8);
INSERT INTO "AHLDivisions" VALUES(2,'North','','Division','North Division','Eastern','Eastern Conference','AHL','American Hockey League',7);
INSERT INTO "AHLDivisions" VALUES(3,'Central','','Division','Central Division','Western','Western Conference','AHL','American Hockey League',8);
INSERT INTO "AHLDivisions" VALUES(4,'Pacific','','Division','Pacific Division','Western','Western Conference','AHL','American Hockey League',7);
CREATE TABLE AHLGameStats (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  GameID INTEGER NOT NULL DEFAULT 0,
  Date INTEGER NOT NULL DEFAULT 0,
  Time INTEGER NOT NULL DEFAULT 0,
  DateTime INTEGER NOT NULL DEFAULT 0,
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
INSERT INTO "AHLStats" VALUES(1,1,20151000,0,201510000000,'Bridgeport Sound Tigers','Bridgeport','Bridgeport','','CT','USA','United States','Bridgeport, CT','Connecticut','Bridgeport, Connecticut','Sound Tigers','Eastern','Eastern Conference','Atlantic','Atlantic Division','AHL','American Hockey League','Webster Bank Arena','Webster Bank Arena, Bridgeport','ECHL:Missouri Mavericks,NHL:New York Islanders',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(2,2,20151000,0,201510000000,'Hartford Wolf Pack','Hartford','Hartford','','CT','USA','United States','Hartford, CT','Connecticut','Hartford, Connecticut','Wolf Pack','Eastern','Eastern Conference','Atlantic','Atlantic Division','AHL','American Hockey League','XL Center','XL Center, Hartford','ECHL:Greenville Swamp Rabbits,NHL:New York Rangers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(3,3,20151000,0,201510000000,'Hershey Bears','Hershey','Hershey','','PA','USA','United States','Hershey, PA','Pennsylvania','Hershey, Pennsylvania','Bears','Eastern','Eastern Conference','Atlantic','Atlantic Division','AHL','American Hockey League','Giant Center','Giant Center, Hershey','ECHL:South Carolina Stingrays,NHL:Washington Capitals',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(4,4,20151000,0,201510000000,'Lehigh Valley Phantoms','Allentown','Lehigh Valley','','PA','USA','United States','Allentown, PA','Pennsylvania','Allentown, Pennsylvania','Phantoms','Eastern','Eastern Conference','Atlantic','Atlantic Division','AHL','American Hockey League','PPL Center','PPL Center, Allentown','ECHL:Reading Royals,NHL:Philadelphia Flyers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(5,5,20151000,0,201510000000,'Portland Pirates','Portland','Portland','','ME','USA','United States','Portland, ME','Maine','Portland, Maine','Pirates','Eastern','Eastern Conference','Atlantic','Atlantic Division','AHL','American Hockey League','Cross Insurance Arena','Cross Insurance Arena, Portland','ECHL:None,NHL:Florida Panthers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(6,6,20151000,0,201510000000,'Providence Bruins','Providence','Providence','','RI','USA','United States','Providence, RI','Rhode Island','Providence, Rhode Island','Bruins','Eastern','Eastern Conference','Atlantic','Atlantic Division','AHL','American Hockey League','Dunkin'' Donuts Center','Dunkin'' Donuts Center, Providence','ECHL:Atlanta Gladiators,NHL:Boston Bruins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(7,7,20151000,0,201510000000,'Springfield Falcons','Springfield','Springfield','','MA','USA','United States','Springfield, MA','Massachusetts','Springfield, Massachusetts','Falcons','Eastern','Eastern Conference','Atlantic','Atlantic Division','AHL','American Hockey League','MassMutual Center','MassMutual Center, Springfield','ECHL:Rapid City Rush,NHL:Arizona Coyotes',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(8,8,20151000,0,201510000000,'Wilkes-Barre/Scranton Penguins','Wilkes-Barre','Wilkes-Barre/Scranton','','PA','USA','United States','Wilkes-Barre, PA','Pennsylvania','Wilkes-Barre, Pennsylvania','Penguins','Eastern','Eastern Conference','Atlantic','Atlantic Division','AHL','American Hockey League','Mohegan Sun Arena','Mohegan Sun Arena, Wilkes-Barre','ECHL:Wheeling Nailers,NHL:Pittsburgh Penguins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(9,9,20151000,0,201510000000,'Albany Devils','Albany','Albany','','NY','USA','United States','Albany, NY','New York','Albany, New York','Devils','Eastern','Eastern Conference','North','North Division','AHL','American Hockey League','Times Union Center','Times Union Center, Albany','ECHL:None,NHL:New Jersey Devils',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(10,10,20151000,0,201510000000,'Binghamton Senators','Binghamton','Binghamton','','NY','USA','United States','Binghamton, NY','New York','Binghamton, New York','Senators','Eastern','Eastern Conference','North','North Division','AHL','American Hockey League','Floyd L. Maines Veterans Memorial Arena','Floyd L. Maines Veterans Memorial Arena, Binghamton','ECHL:Evansville IceMen,NHL:Ottawa Senators',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(11,11,20151000,0,201510000000,'Rochester Americans','Rochester','Rochester','','NY','USA','United States','Rochester, NY','New York','Rochester, New York','Americans','Eastern','Eastern Conference','North','North Division','AHL','American Hockey League','Blue Cross Arena','Blue Cross Arena, Rochester','ECHL:Elmira Jackals,NHL:Buffalo Sabres',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(12,12,20151000,0,201510000000,'St. John''s IceCaps','St. John''s','St. John''s','','NL','CAN','Canada','St. John''s, NL','Newfoundland and Labrador','St. John''s, Newfoundland and Labrador','IceCaps','Eastern','Eastern Conference','North','North Division','AHL','American Hockey League','Mile One Centre','Mile One Centre, St. John''s','ECHL:Brampton Beast,NHL:Montreal Canadiens',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(13,13,20151000,0,201510000000,'Syracuse Crunch','Syracuse','Syracuse','','NY','USA','United States','Syracuse, NY','New York','Syracuse, New York','Crunch','Eastern','Eastern Conference','North','North Division','AHL','American Hockey League','Oncenter War Memorial Arena','Oncenter War Memorial Arena, Syracuse','ECHL:None,NHL:Tampa Bay Lightning',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(14,14,20151000,0,201510000000,'Toronto Marlies','Toronto','Toronto','','ON','CAN','Canada','Toronto, ON','Ontario','Toronto, Ontario','Marlies','Eastern','Eastern Conference','North','North Division','AHL','American Hockey League','Ricoh Coliseum','Ricoh Coliseum, Toronto','ECHL:Orlando Solar Bears,NHL:Toronto Maple Leafs',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(15,15,20151000,0,201510000000,'Utica Comets','Utica','Utica','','NY','USA','United States','Utica, NY','New York','Utica, New York','Comets','Eastern','Eastern Conference','North','North Division','AHL','American Hockey League','Utica Memorial Auditorium','Utica Memorial Auditorium, Utica','ECHL:None,NHL:Vancouver Canucks',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(16,16,20151000,0,201510000000,'Charlotte Checkers','Charlotte','Charlotte','','NC','USA','United States','Charlotte, NC','North Carolina','Charlotte, North Carolina','Checkers','Western','Western Conference','Central','Central Division','AHL','American Hockey League','Bojangles Coliseum','Bojangles Coliseum, Charlotte','ECHL:Florida Everblades,NHL:Carolina Hurricanes',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(17,17,20151000,0,201510000000,'Chicago Wolves','Rosemont','Chicago','','IL','USA','United States','Rosemont, IL','Illinois','Rosemont, Illinois','Wolves','Western','Western Conference','Central','Central Division','AHL','American Hockey League','Allstate Arena','Allstate Arena, Rosemont','ECHL:None,NHL:St. Louis Blues',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(18,18,20151000,0,201510000000,'Grand Rapids Griffins','Grand Rapids','Grand Rapids','','MI','USA','United States','Grand Rapids, MI','Michigan','Grand Rapids, Michigan','Griffins','Western','Western Conference','Central','Central Division','AHL','American Hockey League','Van Andel Arena','Van Andel Arena, Grand Rapids','ECHL:Toledo Walleye,NHL:Detroit Red Wings',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(19,19,20151000,0,201510000000,'Iowa Wild','Des Moines','Iowa','','IA','USA','United States','Des Moines, IA','Iowa','Des Moines, Iowa','Wild','Western','Western Conference','Central','Central Division','AHL','American Hockey League','Wells Fargo Arena','Wells Fargo Arena, Des Moines','ECHL:Quad City Mallards,NHL:Minnesota Wild',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(20,20,20151000,0,201510000000,'Lake Erie Monsters','Cleveland','Lake Erie','','OH','USA','United States','Cleveland, OH','Ohio','Cleveland, Ohio','Monsters','Western','Western Conference','Central','Central Division','AHL','American Hockey League','Quicken Loans Arena','Quicken Loans Arena, Cleveland','ECHL:Kalamazoo Wings,NHL:Columbus Blue Jackets',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(21,21,20151000,0,201510000000,'Manitoba Moose','Winnipeg','Manitoba','','MB','CAN','Canada','Winnipeg, MB','Manitoba','Winnipeg, Manitoba','Moose','Western','Western Conference','Central','Central Division','AHL','American Hockey League','MTS Centre','MTS Centre, Winnipeg','ECHL:Tulsa Oilers,NHL:Winnipeg Jets',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(22,22,20151000,0,201510000000,'Milwaukee Admirals','Milwaukee','Milwaukee','','WI','USA','United States','Milwaukee, WI','Wisconsin','Milwaukee, Wisconsin','Admirals','Western','Western Conference','Central','Central Division','AHL','American Hockey League','BMO Harris Bradley Center','BMO Harris Bradley Center, Milwaukee','ECHL:Cincinnati Cyclones,NHL:Nashville Predators',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(23,23,20151000,0,201510000000,'Rockford IceHogs','Rockford','Rockford','','IL','USA','United States','Rockford, IL','Illinois','Rockford, Illinois','IceHogs','Western','Western Conference','Central','Central Division','AHL','American Hockey League','BMO Harris Bank Center','BMO Harris Bank Center, Rockford','ECHL:Indy Fuel,NHL:Chicago Blackhawks',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(24,24,20151000,0,201510000000,'Bakersfield Condors','Bakersfield','Bakersfield','','CA','USA','United States','Bakersfield, CA','California','Bakersfield, California','Condors','Western','Western Conference','Pacific','Pacific Division','AHL','American Hockey League','Rabobank Arena','Rabobank Arena, Bakersfield','ECHL:Norfolk Admirals,NHL:Edmonton Oilers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(25,25,20151000,0,201510000000,'Ontario Reign','Ontario','Ontario','','CA','USA','United States','Ontario, CA','California','Ontario, California','Reign','Western','Western Conference','Pacific','Pacific Division','AHL','American Hockey League','Citizens Business Bank Arena','Citizens Business Bank Arena, Ontario','ECHL:Manchester Monarchs,NHL:Los Angeles Kings',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(26,26,20151000,0,201510000000,'San Antonio Rampage','San Antonio','San Antonio','','TX','USA','United States','San Antonio, TX','Texas','San Antonio, Texas','Rampage','Western','Western Conference','Pacific','Pacific Division','AHL','American Hockey League','AT&T Center','AT&T Center, San Antonio','ECHL:Fort Wayne Komets,NHL:Colorado Avalanche',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(27,27,20151000,0,201510000000,'San Diego Gulls','San Diego','San Diego','','CA','USA','United States','San Diego, CA','California','San Diego, California','Gulls','Western','Western Conference','Pacific','Pacific Division','AHL','American Hockey League','Valley View Casino Center','Valley View Casino Center, San Diego','ECHL:Utah Grizzlies,NHL:Anaheim Ducks',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(28,28,20151000,0,201510000000,'San Jose Barracuda','San Jose','San Jose','','CA','USA','United States','San Jose, CA','California','San Jose, California','Barracuda','Western','Western Conference','Pacific','Pacific Division','AHL','American Hockey League','SAP Center','SAP Center, San Jose','ECHL:Allen Americans,NHL:San Jose Sharks',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(29,29,20151000,0,201510000000,'Stockton Heat','Stockton','Stockton','','CA','USA','United States','Stockton, CA','California','Stockton, California','Heat','Western','Western Conference','Pacific','Pacific Division','AHL','American Hockey League','Stockton Arena','Stockton Arena, Stockton','ECHL:Adirondack Thunder,NHL:Calgary Flames',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(30,30,20151000,0,201510000000,'Texas Stars','Cedar Park','Texas','','TX','USA','United States','Cedar Park, TX','Texas','Cedar Park, Texas','Stars','Western','Western Conference','Pacific','Pacific Division','AHL','American Hockey League','Cedar Park Center','Cedar Park Center, Cedar Park','ECHL:Idaho Steelheads,NHL:Dallas Stars',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
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
INSERT INTO "AHLTeams" VALUES(1,20151000,0,201510000000,'Bridgeport Sound Tigers','Bridgeport','Bridgeport','','CT','USA','United States','Bridgeport, CT','Connecticut','Bridgeport, Connecticut','Sound Tigers','Eastern','Eastern Conference','Atlantic','Atlantic Division','AHL','American Hockey League','Webster Bank Arena','Webster Bank Arena, Bridgeport','ECHL:Missouri Mavericks,NHL:New York Islanders',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(2,20151000,0,201510000000,'Hartford Wolf Pack','Hartford','Hartford','','CT','USA','United States','Hartford, CT','Connecticut','Hartford, Connecticut','Wolf Pack','Eastern','Eastern Conference','Atlantic','Atlantic Division','AHL','American Hockey League','XL Center','XL Center, Hartford','ECHL:Greenville Swamp Rabbits,NHL:New York Rangers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(3,20151000,0,201510000000,'Hershey Bears','Hershey','Hershey','','PA','USA','United States','Hershey, PA','Pennsylvania','Hershey, Pennsylvania','Bears','Eastern','Eastern Conference','Atlantic','Atlantic Division','AHL','American Hockey League','Giant Center','Giant Center, Hershey','ECHL:South Carolina Stingrays,NHL:Washington Capitals',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(4,20151000,0,201510000000,'Lehigh Valley Phantoms','Allentown','Lehigh Valley','','PA','USA','United States','Allentown, PA','Pennsylvania','Allentown, Pennsylvania','Phantoms','Eastern','Eastern Conference','Atlantic','Atlantic Division','AHL','American Hockey League','PPL Center','PPL Center, Allentown','ECHL:Reading Royals,NHL:Philadelphia Flyers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(5,20151000,0,201510000000,'Portland Pirates','Portland','Portland','','ME','USA','United States','Portland, ME','Maine','Portland, Maine','Pirates','Eastern','Eastern Conference','Atlantic','Atlantic Division','AHL','American Hockey League','Cross Insurance Arena','Cross Insurance Arena, Portland','ECHL:None,NHL:Florida Panthers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(6,20151000,0,201510000000,'Providence Bruins','Providence','Providence','','RI','USA','United States','Providence, RI','Rhode Island','Providence, Rhode Island','Bruins','Eastern','Eastern Conference','Atlantic','Atlantic Division','AHL','American Hockey League','Dunkin'' Donuts Center','Dunkin'' Donuts Center, Providence','ECHL:Atlanta Gladiators,NHL:Boston Bruins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(7,20151000,0,201510000000,'Springfield Falcons','Springfield','Springfield','','MA','USA','United States','Springfield, MA','Massachusetts','Springfield, Massachusetts','Falcons','Eastern','Eastern Conference','Atlantic','Atlantic Division','AHL','American Hockey League','MassMutual Center','MassMutual Center, Springfield','ECHL:Rapid City Rush,NHL:Arizona Coyotes',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(8,20151000,0,201510000000,'Wilkes-Barre/Scranton Penguins','Wilkes-Barre','Wilkes-Barre/Scranton','','PA','USA','United States','Wilkes-Barre, PA','Pennsylvania','Wilkes-Barre, Pennsylvania','Penguins','Eastern','Eastern Conference','Atlantic','Atlantic Division','AHL','American Hockey League','Mohegan Sun Arena','Mohegan Sun Arena, Wilkes-Barre','ECHL:Wheeling Nailers,NHL:Pittsburgh Penguins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(9,20151000,0,201510000000,'Albany Devils','Albany','Albany','','NY','USA','United States','Albany, NY','New York','Albany, New York','Devils','Eastern','Eastern Conference','North','North Division','AHL','American Hockey League','Times Union Center','Times Union Center, Albany','ECHL:None,NHL:New Jersey Devils',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(10,20151000,0,201510000000,'Binghamton Senators','Binghamton','Binghamton','','NY','USA','United States','Binghamton, NY','New York','Binghamton, New York','Senators','Eastern','Eastern Conference','North','North Division','AHL','American Hockey League','Floyd L. Maines Veterans Memorial Arena','Floyd L. Maines Veterans Memorial Arena, Binghamton','ECHL:Evansville IceMen,NHL:Ottawa Senators',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(11,20151000,0,201510000000,'Rochester Americans','Rochester','Rochester','','NY','USA','United States','Rochester, NY','New York','Rochester, New York','Americans','Eastern','Eastern Conference','North','North Division','AHL','American Hockey League','Blue Cross Arena','Blue Cross Arena, Rochester','ECHL:Elmira Jackals,NHL:Buffalo Sabres',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(12,20151000,0,201510000000,'St. John''s IceCaps','St. John''s','St. John''s','','NL','CAN','Canada','St. John''s, NL','Newfoundland and Labrador','St. John''s, Newfoundland and Labrador','IceCaps','Eastern','Eastern Conference','North','North Division','AHL','American Hockey League','Mile One Centre','Mile One Centre, St. John''s','ECHL:Brampton Beast,NHL:Montreal Canadiens',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(13,20151000,0,201510000000,'Syracuse Crunch','Syracuse','Syracuse','','NY','USA','United States','Syracuse, NY','New York','Syracuse, New York','Crunch','Eastern','Eastern Conference','North','North Division','AHL','American Hockey League','Oncenter War Memorial Arena','Oncenter War Memorial Arena, Syracuse','ECHL:None,NHL:Tampa Bay Lightning',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(14,20151000,0,201510000000,'Toronto Marlies','Toronto','Toronto','','ON','CAN','Canada','Toronto, ON','Ontario','Toronto, Ontario','Marlies','Eastern','Eastern Conference','North','North Division','AHL','American Hockey League','Ricoh Coliseum','Ricoh Coliseum, Toronto','ECHL:Orlando Solar Bears,NHL:Toronto Maple Leafs',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(15,20151000,0,201510000000,'Utica Comets','Utica','Utica','','NY','USA','United States','Utica, NY','New York','Utica, New York','Comets','Eastern','Eastern Conference','North','North Division','AHL','American Hockey League','Utica Memorial Auditorium','Utica Memorial Auditorium, Utica','ECHL:None,NHL:Vancouver Canucks',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(16,20151000,0,201510000000,'Charlotte Checkers','Charlotte','Charlotte','','NC','USA','United States','Charlotte, NC','North Carolina','Charlotte, North Carolina','Checkers','Western','Western Conference','Central','Central Division','AHL','American Hockey League','Bojangles Coliseum','Bojangles Coliseum, Charlotte','ECHL:Florida Everblades,NHL:Carolina Hurricanes',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(17,20151000,0,201510000000,'Chicago Wolves','Rosemont','Chicago','','IL','USA','United States','Rosemont, IL','Illinois','Rosemont, Illinois','Wolves','Western','Western Conference','Central','Central Division','AHL','American Hockey League','Allstate Arena','Allstate Arena, Rosemont','ECHL:None,NHL:St. Louis Blues',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(18,20151000,0,201510000000,'Grand Rapids Griffins','Grand Rapids','Grand Rapids','','MI','USA','United States','Grand Rapids, MI','Michigan','Grand Rapids, Michigan','Griffins','Western','Western Conference','Central','Central Division','AHL','American Hockey League','Van Andel Arena','Van Andel Arena, Grand Rapids','ECHL:Toledo Walleye,NHL:Detroit Red Wings',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(19,20151000,0,201510000000,'Iowa Wild','Des Moines','Iowa','','IA','USA','United States','Des Moines, IA','Iowa','Des Moines, Iowa','Wild','Western','Western Conference','Central','Central Division','AHL','American Hockey League','Wells Fargo Arena','Wells Fargo Arena, Des Moines','ECHL:Quad City Mallards,NHL:Minnesota Wild',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(20,20151000,0,201510000000,'Lake Erie Monsters','Cleveland','Lake Erie','','OH','USA','United States','Cleveland, OH','Ohio','Cleveland, Ohio','Monsters','Western','Western Conference','Central','Central Division','AHL','American Hockey League','Quicken Loans Arena','Quicken Loans Arena, Cleveland','ECHL:Kalamazoo Wings,NHL:Columbus Blue Jackets',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(21,20151000,0,201510000000,'Manitoba Moose','Winnipeg','Manitoba','','MB','CAN','Canada','Winnipeg, MB','Manitoba','Winnipeg, Manitoba','Moose','Western','Western Conference','Central','Central Division','AHL','American Hockey League','MTS Centre','MTS Centre, Winnipeg','ECHL:Tulsa Oilers,NHL:Winnipeg Jets',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(22,20151000,0,201510000000,'Milwaukee Admirals','Milwaukee','Milwaukee','','WI','USA','United States','Milwaukee, WI','Wisconsin','Milwaukee, Wisconsin','Admirals','Western','Western Conference','Central','Central Division','AHL','American Hockey League','BMO Harris Bradley Center','BMO Harris Bradley Center, Milwaukee','ECHL:Cincinnati Cyclones,NHL:Nashville Predators',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(23,20151000,0,201510000000,'Rockford IceHogs','Rockford','Rockford','','IL','USA','United States','Rockford, IL','Illinois','Rockford, Illinois','IceHogs','Western','Western Conference','Central','Central Division','AHL','American Hockey League','BMO Harris Bank Center','BMO Harris Bank Center, Rockford','ECHL:Indy Fuel,NHL:Chicago Blackhawks',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(24,20151000,0,201510000000,'Bakersfield Condors','Bakersfield','Bakersfield','','CA','USA','United States','Bakersfield, CA','California','Bakersfield, California','Condors','Western','Western Conference','Pacific','Pacific Division','AHL','American Hockey League','Rabobank Arena','Rabobank Arena, Bakersfield','ECHL:Norfolk Admirals,NHL:Edmonton Oilers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(25,20151000,0,201510000000,'Ontario Reign','Ontario','Ontario','','CA','USA','United States','Ontario, CA','California','Ontario, California','Reign','Western','Western Conference','Pacific','Pacific Division','AHL','American Hockey League','Citizens Business Bank Arena','Citizens Business Bank Arena, Ontario','ECHL:Manchester Monarchs,NHL:Los Angeles Kings',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(26,20151000,0,201510000000,'San Antonio Rampage','San Antonio','San Antonio','','TX','USA','United States','San Antonio, TX','Texas','San Antonio, Texas','Rampage','Western','Western Conference','Pacific','Pacific Division','AHL','American Hockey League','AT&T Center','AT&T Center, San Antonio','ECHL:Fort Wayne Komets,NHL:Colorado Avalanche',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(27,20151000,0,201510000000,'San Diego Gulls','San Diego','San Diego','','CA','USA','United States','San Diego, CA','California','San Diego, California','Gulls','Western','Western Conference','Pacific','Pacific Division','AHL','American Hockey League','Valley View Casino Center','Valley View Casino Center, San Diego','ECHL:Utah Grizzlies,NHL:Anaheim Ducks',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(28,20151000,0,201510000000,'San Jose Barracuda','San Jose','San Jose','','CA','USA','United States','San Jose, CA','California','San Jose, California','Barracuda','Western','Western Conference','Pacific','Pacific Division','AHL','American Hockey League','SAP Center','SAP Center, San Jose','ECHL:Allen Americans,NHL:San Jose Sharks',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(29,20151000,0,201510000000,'Stockton Heat','Stockton','Stockton','','CA','USA','United States','Stockton, CA','California','Stockton, California','Heat','Western','Western Conference','Pacific','Pacific Division','AHL','American Hockey League','Stockton Arena','Stockton Arena, Stockton','ECHL:Adirondack Thunder,NHL:Calgary Flames',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(30,20151000,0,201510000000,'Texas Stars','Cedar Park','Texas','','TX','USA','United States','Cedar Park, TX','Texas','Cedar Park, Texas','Stars','Western','Western Conference','Pacific','Pacific Division','AHL','American Hockey League','Cedar Park Center','Cedar Park Center, Cedar Park','ECHL:Idaho Steelheads,NHL:Dallas Stars',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
CREATE TABLE ECHLArenas (
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
INSERT INTO "ECHLArenas" VALUES(1,1,'Jackals','Elmira Jackals','Elmira','NY','USA','United States','Elmira, NY','New York','Elmira, New York','First Arena','First Arena, Elmira',0);
INSERT INTO "ECHLArenas" VALUES(2,2,'Royals','Reading Royals','Reading','PA','USA','United States','Reading, PA','Pennsylvania','Reading, Pennsylvania','Santander Arena','Santander Arena, Reading',0);
INSERT INTO "ECHLArenas" VALUES(3,3,'Admirals','Norfolk Admirals','Norfolk','VA','USA','United States','Norfolk, VA','Virginia','Norfolk, Virginia','Norfolk Scope','Norfolk Scope, Norfolk',0);
INSERT INTO "ECHLArenas" VALUES(4,4,'Thunder','Adirondack Thunder','Glens Falls','NY','USA','United States','Glens Falls, NY','New York','Glens Falls, New York','Glens Falls Civic Center','Glens Falls Civic Center, Glens Falls',0);
INSERT INTO "ECHLArenas" VALUES(5,5,'Monarchs','Manchester Monarchs','Manchester','NH','USA','United States','Manchester, NH','New Hampshire','Manchester, New Hampshire','Verizon Wireless Arena','Verizon Wireless Arena, Manchester',0);
INSERT INTO "ECHLArenas" VALUES(6,6,'Wings','Kalamazoo Wings','Kalamazoo','MI','USA','United States','Kalamazoo, MI','Michigan','Kalamazoo, Michigan','Wings Event Center','Wings Event Center, Kalamazoo',0);
INSERT INTO "ECHLArenas" VALUES(7,7,'Walleye','Toledo Walleye','Toledo','OH','USA','United States','Toledo, OH','Ohio','Toledo, Ohio','Huntington Center','Huntington Center, Toledo',0);
INSERT INTO "ECHLArenas" VALUES(8,8,'Nailers','Wheeling Nailers','Wheeling','WV','USA','United States','Wheeling, WV','West Virginia','Wheeling, West Virginia','WesBanco Arena','WesBanco Arena, Wheeling',0);
INSERT INTO "ECHLArenas" VALUES(9,9,'Beast','Brampton Beast','Brampton','ON','CAN','Canada','Brampton, ON','Ontario','Brampton, Ontario','Powerade Centre','Powerade Centre, Brampton',0);
INSERT INTO "ECHLArenas" VALUES(10,10,'Gladiators','Atlanta Gladiators','Duluth','GA','USA','United States','Duluth, GA','Georgia','Duluth, Georgia','Infinite Energy Arena','Infinite Energy Arena, Duluth',0);
INSERT INTO "ECHLArenas" VALUES(11,11,'Swamp Rabbits','Greenville Swamp Rabbits','Greenville','SC','USA','United States','Greenville, SC','South Carolina','Greenville, South Carolina','Bon Secours Wellness Arena','Bon Secours Wellness Arena, Greenville',0);
INSERT INTO "ECHLArenas" VALUES(12,12,'Everblades','Florida Everblades','Estero','FL','USA','United States','Estero, FL','Florida','Estero, Florida','Germain Arena','Germain Arena, Estero',0);
INSERT INTO "ECHLArenas" VALUES(13,13,'Solar Bears','Orlando Solar Bears','Orlando','FL','USA','United States','Orlando, FL','Florida','Orlando, Florida','Amway Center','Amway Center, Orlando',0);
INSERT INTO "ECHLArenas" VALUES(14,14,'Stingrays','South Carolina Stingrays','North Charleston','SC','USA','United States','North Charleston, SC','South Carolina','North Charleston, South Carolina','North Charleston Coliseum','North Charleston Coliseum, North Charleston',0);
INSERT INTO "ECHLArenas" VALUES(15,15,'Mallards','Quad City Mallards','Moline','IL','USA','United States','Moline, IL','Illinois','Moline, Illinois','iWireless Center','iWireless Center, Moline',0);
INSERT INTO "ECHLArenas" VALUES(16,16,'IceMen','Evansville IceMen','Evansville','IN','USA','United States','Evansville, IN','Indiana','Evansville, Indiana','Ford Center','Ford Center, Evansville',0);
INSERT INTO "ECHLArenas" VALUES(17,17,'Fuel','Indy Fuel','Indianapolis','IN','USA','United States','Indianapolis, IN','Indiana','Indianapolis, Indiana','Indiana Farmers Coliseum','Indiana Farmers Coliseum, Indianapolis',0);
INSERT INTO "ECHLArenas" VALUES(18,18,'Komets','Fort Wayne Komets','Fort Wayne','IN','USA','United States','Fort Wayne, IN','Indiana','Fort Wayne, Indiana','Allen County War Memorial Coliseum','Allen County War Memorial Coliseum, Fort Wayne',0);
INSERT INTO "ECHLArenas" VALUES(19,19,'Cyclones','Cincinnati Cyclones','Cincinnati','OH','USA','United States','Cincinnati, OH','Ohio','Cincinnati, Ohio','US Bank Arena','US Bank Arena, Cincinnati',0);
INSERT INTO "ECHLArenas" VALUES(20,20,'Thunder','Wichita Thunder','Wichita','KS','USA','United States','Wichita, KS','Kansas','Wichita, Kansas','Intrust Bank Arena','Intrust Bank Arena, Wichita',0);
INSERT INTO "ECHLArenas" VALUES(21,21,'Americans','Allen Americans','Allen','TX','USA','United States','Allen, TX','Texas','Allen, Texas','Allen Event Center','Allen Event Center, Allen',0);
INSERT INTO "ECHLArenas" VALUES(22,22,'Oilers','Tulsa Oilers','Tulsa','OK','USA','United States','Tulsa, OK','Oklahoma','Tulsa, Oklahoma','BOK Center','BOK Center, Tulsa',0);
INSERT INTO "ECHLArenas" VALUES(23,23,'Mavericks','Missouri Mavericks','Independence','MO','USA','United States','Independence, MO','Missouri','Independence, Missouri','Silverstein Eye Centers Arena','Silverstein Eye Centers Arena, Independence',0);
INSERT INTO "ECHLArenas" VALUES(24,24,'Aces','Alaska Aces','Anchorage','AK','USA','United States','Anchorage, AK','Alaska','Anchorage, Alaska','Sullivan Arena','Sullivan Arena, Anchorage',0);
INSERT INTO "ECHLArenas" VALUES(25,25,'Steelheads','Idaho Steelheads','Boise','ID','USA','United States','Boise, ID','Idaho','Boise, Idaho','CenturyLink Arena','CenturyLink Arena, Boise',0);
INSERT INTO "ECHLArenas" VALUES(26,26,'Grizzlies','Utah Grizzlies','West Valley City','UT','USA','United States','West Valley City, UT','Utah','West Valley City, Utah','Maverik Center','Maverik Center, West Valley City',0);
INSERT INTO "ECHLArenas" VALUES(27,27,'Eagles','Colorado Eagles','Loveland','CO','USA','United States','Loveland, CO','Colorado','Loveland, Colorado','Budweiser Events Center','Budweiser Events Center, Loveland',0);
INSERT INTO "ECHLArenas" VALUES(28,28,'Rush','Rapid City Rush','Rapid City','SD','USA','United States','Rapid City, SD','South Dakota','Rapid City, South Dakota','Rushmore Plaza Civic Center','Rushmore Plaza Civic Center, Rapid City',0);
CREATE TABLE ECHLConferences (
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
INSERT INTO "ECHLConferences" VALUES(1,'Eastern','','Conference','Eastern Conference','ECHL','ECHL',14,3);
INSERT INTO "ECHLConferences" VALUES(2,'Western','','Conference','Western Conference','ECHL','ECHL',14,3);
CREATE TABLE ECHLDivisions (
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
INSERT INTO "ECHLDivisions" VALUES(1,'East','','Division','East Division','Eastern','Eastern Conference','ECHL','ECHL',5);
INSERT INTO "ECHLDivisions" VALUES(2,'North','','Division','North Division','Eastern','Eastern Conference','ECHL','ECHL',4);
INSERT INTO "ECHLDivisions" VALUES(3,'South','','Division','South Division','Eastern','Eastern Conference','ECHL','ECHL',5);
INSERT INTO "ECHLDivisions" VALUES(4,'Midwest','','Division','Midwest Division','Western','Western Conference','ECHL','ECHL',5);
INSERT INTO "ECHLDivisions" VALUES(5,'Central','','Division','Central Division','Western','Western Conference','ECHL','ECHL',4);
INSERT INTO "ECHLDivisions" VALUES(6,'West','','Division','West Division','Western','Western Conference','ECHL','ECHL',5);
CREATE TABLE ECHLGameStats (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  GameID INTEGER NOT NULL DEFAULT 0,
  Date INTEGER NOT NULL DEFAULT 0,
  Time INTEGER NOT NULL DEFAULT 0,
  DateTime INTEGER NOT NULL DEFAULT 0,
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
CREATE TABLE ECHLGames (
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
CREATE TABLE ECHLStats (
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
INSERT INTO "ECHLStats" VALUES(1,1,20151000,0,201510000000,'Elmira Jackals','Elmira','Elmira','','NY','USA','United States','Elmira, NY','New York','Elmira, New York','Jackals','Eastern','Eastern Conference','East','East Division','ECHL','ECHL','First Arena','First Arena, Elmira','AHL:Rochester Americans,NHL:Buffalo Sabres',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(2,2,20151000,0,201510000000,'Reading Royals','Reading','Reading','','PA','USA','United States','Reading, PA','Pennsylvania','Reading, Pennsylvania','Royals','Eastern','Eastern Conference','East','East Division','ECHL','ECHL','Santander Arena','Santander Arena, Reading','AHL:Lehigh Valley Phantoms,NHL:Philadelphia Flyers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(3,3,20151000,0,201510000000,'Norfolk Admirals','Norfolk','Norfolk','','VA','USA','United States','Norfolk, VA','Virginia','Norfolk, Virginia','Admirals','Eastern','Eastern Conference','East','East Division','ECHL','ECHL','Norfolk Scope','Norfolk Scope, Norfolk','AHL:Bakersfield Condors,NHL:Edmonton Oilers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(4,4,20151000,0,201510000000,'Adirondack Thunder','Glens Falls','Adirondack','','NY','USA','United States','Glens Falls, NY','New York','Glens Falls, New York','Thunder','Eastern','Eastern Conference','East','East Division','ECHL','ECHL','Glens Falls Civic Center','Glens Falls Civic Center, Glens Falls','AHL:Stockton Heat,NHL:Calgary Flames',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(5,5,20151000,0,201510000000,'Manchester Monarchs','Manchester','Manchester','','NH','USA','United States','Manchester, NH','New Hampshire','Manchester, New Hampshire','Monarchs','Eastern','Eastern Conference','East','East Division','ECHL','ECHL','Verizon Wireless Arena','Verizon Wireless Arena, Manchester','AHL:Ontario Reign,NHL:Los Angeles Kings',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(6,6,20151000,0,201510000000,'Kalamazoo Wings','Kalamazoo','Kalamazoo','','MI','USA','United States','Kalamazoo, MI','Michigan','Kalamazoo, Michigan','Wings','Eastern','Eastern Conference','North','North Division','ECHL','ECHL','Wings Event Center','Wings Event Center, Kalamazoo','AHL:Lake Erie Monsters,NHL:Columbus Blue Jackets',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(7,7,20151000,0,201510000000,'Toledo Walleye','Toledo','Toledo','','OH','USA','United States','Toledo, OH','Ohio','Toledo, Ohio','Walleye','Eastern','Eastern Conference','North','North Division','ECHL','ECHL','Huntington Center','Huntington Center, Toledo','AHL:Grand Rapids Griffins,NHL:Detroit Red Wings',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(8,8,20151000,0,201510000000,'Wheeling Nailers','Wheeling','Wheeling','','WV','USA','United States','Wheeling, WV','West Virginia','Wheeling, West Virginia','Nailers','Eastern','Eastern Conference','North','North Division','ECHL','ECHL','WesBanco Arena','WesBanco Arena, Wheeling','AHL:Wilkes-Barre/Scranton Penguins,NHL:Pittsburgh Penguins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(9,9,20151000,0,201510000000,'Brampton Beast','Brampton','Brampton','','ON','CAN','Canada','Brampton, ON','Ontario','Brampton, Ontario','Beast','Eastern','Eastern Conference','North','North Division','ECHL','ECHL','Powerade Centre','Powerade Centre, Brampton','AHL:St. John''s IceCaps,NHL:Montreal Canadiens',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(10,10,20151000,0,201510000000,'Atlanta Gladiators','Duluth','Atlanta','','GA','USA','United States','Duluth, GA','Georgia','Duluth, Georgia','Gladiators','Eastern','Eastern Conference','South','South Division','ECHL','ECHL','Infinite Energy Arena','Infinite Energy Arena, Duluth','AHL:Providence Bruins,NHL:Boston Bruins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(11,11,20151000,0,201510000000,'Greenville Swamp Rabbits','Greenville','Greenville','','SC','USA','United States','Greenville, SC','South Carolina','Greenville, South Carolina','Swamp Rabbits','Eastern','Eastern Conference','South','South Division','ECHL','ECHL','Bon Secours Wellness Arena','Bon Secours Wellness Arena, Greenville','AHL:Hartford Wolf Pack,NHL:New York Rangers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(12,12,20151000,0,201510000000,'Florida Everblades','Estero','Florida','','FL','USA','United States','Estero, FL','Florida','Estero, Florida','Everblades','Eastern','Eastern Conference','South','South Division','ECHL','ECHL','Germain Arena','Germain Arena, Estero','AHL:Charlotte Checkers,NHL:Carolina Hurricanes',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(13,13,20151000,0,201510000000,'Orlando Solar Bears','Orlando','Orlando','','FL','USA','United States','Orlando, FL','Florida','Orlando, Florida','Solar Bears','Eastern','Eastern Conference','South','South Division','ECHL','ECHL','Amway Center','Amway Center, Orlando','AHL:Toronto Marlies,NHL:Toronto Maple Leafs',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(14,14,20151000,0,201510000000,'South Carolina Stingrays','North Charleston','South Carolina','','SC','USA','United States','North Charleston, SC','South Carolina','North Charleston, South Carolina','Stingrays','Eastern','Eastern Conference','South','South Division','ECHL','ECHL','North Charleston Coliseum','North Charleston Coliseum, North Charleston','AHL:Hershey Bears,NHL:Washington Capitals',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(15,15,20151000,0,201510000000,'Quad City Mallards','Moline','Quad City','','IL','USA','United States','Moline, IL','Illinois','Moline, Illinois','Mallards','Western','Western Conference','Midwest','Midwest Division','ECHL','ECHL','iWireless Center','iWireless Center, Moline','AHL:Iowa Wild,NHL:Minnesota Wild',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(16,16,20151000,0,201510000000,'Evansville IceMen','Evansville','Evansville','','IN','USA','United States','Evansville, IN','Indiana','Evansville, Indiana','IceMen','Western','Western Conference','Midwest','Midwest Division','ECHL','ECHL','Ford Center','Ford Center, Evansville','AHL:Binghamton Senators,NHL:Ottawa Senators',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(17,17,20151000,0,201510000000,'Indy Fuel','Indianapolis','Indy','','IN','USA','United States','Indianapolis, IN','Indiana','Indianapolis, Indiana','Fuel','Western','Western Conference','Midwest','Midwest Division','ECHL','ECHL','Indiana Farmers Coliseum','Indiana Farmers Coliseum, Indianapolis','AHL:Rockford IceHogs,NHL:Chicago Blackhawks',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(18,18,20151000,0,201510000000,'Fort Wayne Komets','Fort Wayne','Fort Wayne','','IN','USA','United States','Fort Wayne, IN','Indiana','Fort Wayne, Indiana','Komets','Western','Western Conference','Midwest','Midwest Division','ECHL','ECHL','Allen County War Memorial Coliseum','Allen County War Memorial Coliseum, Fort Wayne','AHL:San Antonio Rampage,NHL:Colorado Avalanche',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(19,19,20151000,0,201510000000,'Cincinnati Cyclones','Cincinnati','Cincinnati','','OH','USA','United States','Cincinnati, OH','Ohio','Cincinnati, Ohio','Cyclones','Western','Western Conference','Midwest','Midwest Division','ECHL','ECHL','US Bank Arena','US Bank Arena, Cincinnati','AHL:Milwaukee Admirals,NHL:Nashville Predators',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(20,20,20151000,0,201510000000,'Wichita Thunder','Wichita','Wichita','','KS','USA','United States','Wichita, KS','Kansas','Wichita, Kansas','Thunder','Western','Western Conference','Central','Central Division','ECHL','ECHL','Intrust Bank Arena','Intrust Bank Arena, Wichita','AHL:None,NHL:None',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(21,21,20151000,0,201510000000,'Allen Americans','Allen','Allen','','TX','USA','United States','Allen, TX','Texas','Allen, Texas','Americans','Western','Western Conference','Central','Central Division','ECHL','ECHL','Allen Event Center','Allen Event Center, Allen','AHL:San Jose Barracuda,NHL:San Jose Sharks',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(22,22,20151000,0,201510000000,'Tulsa Oilers','Tulsa','Tulsa','','OK','USA','United States','Tulsa, OK','Oklahoma','Tulsa, Oklahoma','Oilers','Western','Western Conference','Central','Central Division','ECHL','ECHL','BOK Center','BOK Center, Tulsa','AHL:Manitoba Moose,NHL:Winnipeg Jets',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(23,23,20151000,0,201510000000,'Missouri Mavericks','Independence','Missouri','','MO','USA','United States','Independence, MO','Missouri','Independence, Missouri','Mavericks','Western','Western Conference','Central','Central Division','ECHL','ECHL','Silverstein Eye Centers Arena','Silverstein Eye Centers Arena, Independence','AHL:Bridgeport Sound Tigers,NHL:New York Islanders',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(24,24,20151000,0,201510000000,'Alaska Aces','Anchorage','Alaska','','AK','USA','United States','Anchorage, AK','Alaska','Anchorage, Alaska','Aces','Western','Western Conference','West','West Division','ECHL','ECHL','Sullivan Arena','Sullivan Arena, Anchorage','AHL:None,NHL:None',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(25,25,20151000,0,201510000000,'Idaho Steelheads','Boise','Idaho','','ID','USA','United States','Boise, ID','Idaho','Boise, Idaho','Steelheads','Western','Western Conference','West','West Division','ECHL','ECHL','CenturyLink Arena','CenturyLink Arena, Boise','AHL:Texas Stars,NHL:Dallas Stars',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(26,26,20151000,0,201510000000,'Utah Grizzlies','West Valley City','Utah','','UT','USA','United States','West Valley City, UT','Utah','West Valley City, Utah','Grizzlies','Western','Western Conference','West','West Division','ECHL','ECHL','Maverik Center','Maverik Center, West Valley City','AHL:San Diego Gulls,NHL:Anaheim Ducks',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(27,27,20151000,0,201510000000,'Colorado Eagles','Loveland','Colorado','','CO','USA','United States','Loveland, CO','Colorado','Loveland, Colorado','Eagles','Western','Western Conference','West','West Division','ECHL','ECHL','Budweiser Events Center','Budweiser Events Center, Loveland','AHL:None,NHL:None',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLStats" VALUES(28,28,20151000,0,201510000000,'Rapid City Rush','Rapid City','Rapid City','','SD','USA','United States','Rapid City, SD','South Dakota','Rapid City, South Dakota','Rush','Western','Western Conference','West','West Division','ECHL','ECHL','Rushmore Plaza Civic Center','Rushmore Plaza Civic Center, Rapid City','AHL:Springfield Falcons,NHL:Arizona Coyotes',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
CREATE TABLE ECHLTeams (
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
INSERT INTO "ECHLTeams" VALUES(1,20151000,0,201510000000,'Elmira Jackals','Elmira','Elmira','','NY','USA','United States','Elmira, NY','New York','Elmira, New York','Jackals','Eastern','Eastern Conference','East','East Division','ECHL','ECHL','First Arena','First Arena, Elmira','AHL:Rochester Americans,NHL:Buffalo Sabres',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(2,20151000,0,201510000000,'Reading Royals','Reading','Reading','','PA','USA','United States','Reading, PA','Pennsylvania','Reading, Pennsylvania','Royals','Eastern','Eastern Conference','East','East Division','ECHL','ECHL','Santander Arena','Santander Arena, Reading','AHL:Lehigh Valley Phantoms,NHL:Philadelphia Flyers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(3,20151000,0,201510000000,'Norfolk Admirals','Norfolk','Norfolk','','VA','USA','United States','Norfolk, VA','Virginia','Norfolk, Virginia','Admirals','Eastern','Eastern Conference','East','East Division','ECHL','ECHL','Norfolk Scope','Norfolk Scope, Norfolk','AHL:Bakersfield Condors,NHL:Edmonton Oilers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(4,20151000,0,201510000000,'Adirondack Thunder','Glens Falls','Adirondack','','NY','USA','United States','Glens Falls, NY','New York','Glens Falls, New York','Thunder','Eastern','Eastern Conference','East','East Division','ECHL','ECHL','Glens Falls Civic Center','Glens Falls Civic Center, Glens Falls','AHL:Stockton Heat,NHL:Calgary Flames',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(5,20151000,0,201510000000,'Manchester Monarchs','Manchester','Manchester','','NH','USA','United States','Manchester, NH','New Hampshire','Manchester, New Hampshire','Monarchs','Eastern','Eastern Conference','East','East Division','ECHL','ECHL','Verizon Wireless Arena','Verizon Wireless Arena, Manchester','AHL:Ontario Reign,NHL:Los Angeles Kings',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(6,20151000,0,201510000000,'Kalamazoo Wings','Kalamazoo','Kalamazoo','','MI','USA','United States','Kalamazoo, MI','Michigan','Kalamazoo, Michigan','Wings','Eastern','Eastern Conference','North','North Division','ECHL','ECHL','Wings Event Center','Wings Event Center, Kalamazoo','AHL:Lake Erie Monsters,NHL:Columbus Blue Jackets',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(7,20151000,0,201510000000,'Toledo Walleye','Toledo','Toledo','','OH','USA','United States','Toledo, OH','Ohio','Toledo, Ohio','Walleye','Eastern','Eastern Conference','North','North Division','ECHL','ECHL','Huntington Center','Huntington Center, Toledo','AHL:Grand Rapids Griffins,NHL:Detroit Red Wings',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(8,20151000,0,201510000000,'Wheeling Nailers','Wheeling','Wheeling','','WV','USA','United States','Wheeling, WV','West Virginia','Wheeling, West Virginia','Nailers','Eastern','Eastern Conference','North','North Division','ECHL','ECHL','WesBanco Arena','WesBanco Arena, Wheeling','AHL:Wilkes-Barre/Scranton Penguins,NHL:Pittsburgh Penguins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(9,20151000,0,201510000000,'Brampton Beast','Brampton','Brampton','','ON','CAN','Canada','Brampton, ON','Ontario','Brampton, Ontario','Beast','Eastern','Eastern Conference','North','North Division','ECHL','ECHL','Powerade Centre','Powerade Centre, Brampton','AHL:St. John''s IceCaps,NHL:Montreal Canadiens',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(10,20151000,0,201510000000,'Atlanta Gladiators','Duluth','Atlanta','','GA','USA','United States','Duluth, GA','Georgia','Duluth, Georgia','Gladiators','Eastern','Eastern Conference','South','South Division','ECHL','ECHL','Infinite Energy Arena','Infinite Energy Arena, Duluth','AHL:Providence Bruins,NHL:Boston Bruins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(11,20151000,0,201510000000,'Greenville Swamp Rabbits','Greenville','Greenville','','SC','USA','United States','Greenville, SC','South Carolina','Greenville, South Carolina','Swamp Rabbits','Eastern','Eastern Conference','South','South Division','ECHL','ECHL','Bon Secours Wellness Arena','Bon Secours Wellness Arena, Greenville','AHL:Hartford Wolf Pack,NHL:New York Rangers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(12,20151000,0,201510000000,'Florida Everblades','Estero','Florida','','FL','USA','United States','Estero, FL','Florida','Estero, Florida','Everblades','Eastern','Eastern Conference','South','South Division','ECHL','ECHL','Germain Arena','Germain Arena, Estero','AHL:Charlotte Checkers,NHL:Carolina Hurricanes',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(13,20151000,0,201510000000,'Orlando Solar Bears','Orlando','Orlando','','FL','USA','United States','Orlando, FL','Florida','Orlando, Florida','Solar Bears','Eastern','Eastern Conference','South','South Division','ECHL','ECHL','Amway Center','Amway Center, Orlando','AHL:Toronto Marlies,NHL:Toronto Maple Leafs',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(14,20151000,0,201510000000,'South Carolina Stingrays','North Charleston','South Carolina','','SC','USA','United States','North Charleston, SC','South Carolina','North Charleston, South Carolina','Stingrays','Eastern','Eastern Conference','South','South Division','ECHL','ECHL','North Charleston Coliseum','North Charleston Coliseum, North Charleston','AHL:Hershey Bears,NHL:Washington Capitals',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(15,20151000,0,201510000000,'Quad City Mallards','Moline','Quad City','','IL','USA','United States','Moline, IL','Illinois','Moline, Illinois','Mallards','Western','Western Conference','Midwest','Midwest Division','ECHL','ECHL','iWireless Center','iWireless Center, Moline','AHL:Iowa Wild,NHL:Minnesota Wild',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(16,20151000,0,201510000000,'Evansville IceMen','Evansville','Evansville','','IN','USA','United States','Evansville, IN','Indiana','Evansville, Indiana','IceMen','Western','Western Conference','Midwest','Midwest Division','ECHL','ECHL','Ford Center','Ford Center, Evansville','AHL:Binghamton Senators,NHL:Ottawa Senators',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(17,20151000,0,201510000000,'Indy Fuel','Indianapolis','Indy','','IN','USA','United States','Indianapolis, IN','Indiana','Indianapolis, Indiana','Fuel','Western','Western Conference','Midwest','Midwest Division','ECHL','ECHL','Indiana Farmers Coliseum','Indiana Farmers Coliseum, Indianapolis','AHL:Rockford IceHogs,NHL:Chicago Blackhawks',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(18,20151000,0,201510000000,'Fort Wayne Komets','Fort Wayne','Fort Wayne','','IN','USA','United States','Fort Wayne, IN','Indiana','Fort Wayne, Indiana','Komets','Western','Western Conference','Midwest','Midwest Division','ECHL','ECHL','Allen County War Memorial Coliseum','Allen County War Memorial Coliseum, Fort Wayne','AHL:San Antonio Rampage,NHL:Colorado Avalanche',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(19,20151000,0,201510000000,'Cincinnati Cyclones','Cincinnati','Cincinnati','','OH','USA','United States','Cincinnati, OH','Ohio','Cincinnati, Ohio','Cyclones','Western','Western Conference','Midwest','Midwest Division','ECHL','ECHL','US Bank Arena','US Bank Arena, Cincinnati','AHL:Milwaukee Admirals,NHL:Nashville Predators',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(20,20151000,0,201510000000,'Wichita Thunder','Wichita','Wichita','','KS','USA','United States','Wichita, KS','Kansas','Wichita, Kansas','Thunder','Western','Western Conference','Central','Central Division','ECHL','ECHL','Intrust Bank Arena','Intrust Bank Arena, Wichita','AHL:None,NHL:None',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(21,20151000,0,201510000000,'Allen Americans','Allen','Allen','','TX','USA','United States','Allen, TX','Texas','Allen, Texas','Americans','Western','Western Conference','Central','Central Division','ECHL','ECHL','Allen Event Center','Allen Event Center, Allen','AHL:San Jose Barracuda,NHL:San Jose Sharks',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(22,20151000,0,201510000000,'Tulsa Oilers','Tulsa','Tulsa','','OK','USA','United States','Tulsa, OK','Oklahoma','Tulsa, Oklahoma','Oilers','Western','Western Conference','Central','Central Division','ECHL','ECHL','BOK Center','BOK Center, Tulsa','AHL:Manitoba Moose,NHL:Winnipeg Jets',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(23,20151000,0,201510000000,'Missouri Mavericks','Independence','Missouri','','MO','USA','United States','Independence, MO','Missouri','Independence, Missouri','Mavericks','Western','Western Conference','Central','Central Division','ECHL','ECHL','Silverstein Eye Centers Arena','Silverstein Eye Centers Arena, Independence','AHL:Bridgeport Sound Tigers,NHL:New York Islanders',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(24,20151000,0,201510000000,'Alaska Aces','Anchorage','Alaska','','AK','USA','United States','Anchorage, AK','Alaska','Anchorage, Alaska','Aces','Western','Western Conference','West','West Division','ECHL','ECHL','Sullivan Arena','Sullivan Arena, Anchorage','AHL:None,NHL:None',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(25,20151000,0,201510000000,'Idaho Steelheads','Boise','Idaho','','ID','USA','United States','Boise, ID','Idaho','Boise, Idaho','Steelheads','Western','Western Conference','West','West Division','ECHL','ECHL','CenturyLink Arena','CenturyLink Arena, Boise','AHL:Texas Stars,NHL:Dallas Stars',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(26,20151000,0,201510000000,'Utah Grizzlies','West Valley City','Utah','','UT','USA','United States','West Valley City, UT','Utah','West Valley City, Utah','Grizzlies','Western','Western Conference','West','West Division','ECHL','ECHL','Maverik Center','Maverik Center, West Valley City','AHL:San Diego Gulls,NHL:Anaheim Ducks',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(27,20151000,0,201510000000,'Colorado Eagles','Loveland','Colorado','','CO','USA','United States','Loveland, CO','Colorado','Loveland, Colorado','Eagles','Western','Western Conference','West','West Division','ECHL','ECHL','Budweiser Events Center','Budweiser Events Center, Loveland','AHL:None,NHL:None',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "ECHLTeams" VALUES(28,20151000,0,201510000000,'Rapid City Rush','Rapid City','Rapid City','','SD','USA','United States','Rapid City, SD','South Dakota','Rapid City, South Dakota','Rush','Western','Western Conference','West','West Division','ECHL','ECHL','Rushmore Plaza Civic Center','Rushmore Plaza Civic Center, Rapid City','AHL:Springfield Falcons,NHL:Arizona Coyotes',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
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
INSERT INTO "HockeyLeagues" VALUES(1,'ECHL','ECHL','USA','United States',20151007,'Division=1,Conference=5','ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC',28,2,6);
INSERT INTO "HockeyLeagues" VALUES(2,'AHL','American Hockey League','USA','United States',20151009,'Division=4','ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC',30,2,4);
INSERT INTO "HockeyLeagues" VALUES(3,'NHL','National Hockey League','USA','United States',20151007,'Division=3,Conference=2','ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC',30,2,4);
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
INSERT INTO "NHLArenas" VALUES(1,1,'Bruins','Boston Bruins','Boston','MA','USA','United States','Boston, MA','Massachusetts','Boston, Massachusetts','TD Garden','TD Garden, Boston',0);
INSERT INTO "NHLArenas" VALUES(2,2,'Sabres','Buffalo Sabres','Buffalo','NY','USA','United States','Buffalo, NY','New York','Buffalo, New York','First Niagara Center','First Niagara Center, Buffalo',0);
INSERT INTO "NHLArenas" VALUES(3,3,'Red Wings','Detroit Red Wings','Detroit','MI','USA','United States','Detroit, MI','Michigan','Detroit, Michigan','Joe Louis Arena','Joe Louis Arena, Detroit',0);
INSERT INTO "NHLArenas" VALUES(4,4,'Panthers','Florida Panthers','Sunrise','FL','USA','United States','Sunrise, FL','Florida','Sunrise, Florida','BB&T Center','BB&T Center, Sunrise',0);
INSERT INTO "NHLArenas" VALUES(5,5,'Canadiens','Montreal Canadiens','Montreal','QC','CAN','Canada','Montreal, QC','Quebec','Montreal, Quebec','Bell Centre','Bell Centre, Montreal',0);
INSERT INTO "NHLArenas" VALUES(6,6,'Senators','Ottawa Senators','Ottawa','ON','CAN','Canada','Ottawa, ON','Ontario','Ottawa, Ontario','Canadian Tire Centre','Canadian Tire Centre, Ottawa',0);
INSERT INTO "NHLArenas" VALUES(7,7,'Lightning','Tampa Bay Lightning','Tampa Bay','FL','USA','United States','Tampa Bay, FL','Florida','Tampa Bay, Florida','Amalie Arena','Amalie Arena, Tampa Bay',0);
INSERT INTO "NHLArenas" VALUES(8,8,'Maple Leafs','Toronto Maple Leafs','Toronto','ON','CAN','Canada','Toronto, ON','Ontario','Toronto, Ontario','Air Canada Centre','Air Canada Centre, Toronto',0);
INSERT INTO "NHLArenas" VALUES(9,9,'Hurricanes','Carolina Hurricanes','Carolina','NC','USA','United States','Carolina, NC','North Carolina','Carolina, North Carolina','PNC Arena','PNC Arena, Carolina',0);
INSERT INTO "NHLArenas" VALUES(10,10,'Blue Jackets','Columbus Blue Jackets','Columbus','OH','USA','United States','Columbus, OH','Ohio','Columbus, Ohio','Nationwide Arena','Nationwide Arena, Columbus',0);
INSERT INTO "NHLArenas" VALUES(11,11,'Devils','New Jersey Devils','New Jersey','NJ','USA','United States','New Jersey, NJ','New Jersey','New Jersey, New Jersey','Prudential Center','Prudential Center, New Jersey',0);
INSERT INTO "NHLArenas" VALUES(12,12,'Islanders','New York Islanders','New York City','NY','USA','United States','New York City, NY','New York','New York City, New York','Barclays Center','Barclays Center, New York City',0);
INSERT INTO "NHLArenas" VALUES(13,13,'Rangers','New York Rangers','New York City','NY','USA','United States','New York City, NY','New York','New York City, New York','Madison Square Garden','Madison Square Garden, New York City',0);
INSERT INTO "NHLArenas" VALUES(14,14,'Flyers','Philadelphia Flyers','Philadelphia','PA','USA','United States','Philadelphia, PA','Pennsylvania','Philadelphia, Pennsylvania','Wells Fargo Center','Wells Fargo Center, Philadelphia',0);
INSERT INTO "NHLArenas" VALUES(15,15,'Penguins','Pittsburgh Penguins','Pittsburgh','PA','USA','United States','Pittsburgh, PA','Pennsylvania','Pittsburgh, Pennsylvania','Consol Energy Center','Consol Energy Center, Pittsburgh',0);
INSERT INTO "NHLArenas" VALUES(16,16,'Capitals','Washington Capitals','Washington','DC','USA','United States','Washington, DC','District of Columbia','Washington, District of Columbia','Verizon Center','Verizon Center, Washington',0);
INSERT INTO "NHLArenas" VALUES(17,17,'Blackhawks','Chicago Blackhawks','Chicago','IL','USA','United States','Chicago, IL','Illinois','Chicago, Illinois','United Center','United Center, Chicago',0);
INSERT INTO "NHLArenas" VALUES(18,18,'Avalanche','Colorado Avalanche','Denver','CO','USA','United States','Denver, CO','Colorado','Denver, Colorado','Pepsi Center','Pepsi Center, Denver',0);
INSERT INTO "NHLArenas" VALUES(19,19,'Stars','Dallas Stars','Dallas','TX','USA','United States','Dallas, TX','Texas','Dallas, Texas','American Airlines Center','American Airlines Center, Dallas',0);
INSERT INTO "NHLArenas" VALUES(20,20,'Wild','Minnesota Wild','St. Paul','MN','USA','United States','St. Paul, MN','Minnesota','St. Paul, Minnesota','Xcel Energy Center','Xcel Energy Center, St. Paul',0);
INSERT INTO "NHLArenas" VALUES(21,21,'Predators','Nashville Predators','Nashville','TN','USA','United States','Nashville, TN','Tennessee','Nashville, Tennessee','Bridgestone Arena','Bridgestone Arena, Nashville',0);
INSERT INTO "NHLArenas" VALUES(22,22,'Blues','St. Louis Blues','St. Louis','MO','USA','United States','St. Louis, MO','Missouri','St. Louis, Missouri','Scottrade Center','Scottrade Center, St. Louis',0);
INSERT INTO "NHLArenas" VALUES(23,23,'Jets','Winnipeg Jets','Winnipeg','MB','CAN','Canada','Winnipeg, MB','Manitoba','Winnipeg, Manitoba','MTS Centre','MTS Centre, Winnipeg',0);
INSERT INTO "NHLArenas" VALUES(24,24,'Ducks','Anaheim Ducks','Anaheim','CA','USA','United States','Anaheim, CA','California','Anaheim, California','Honda Center','Honda Center, Anaheim',0);
INSERT INTO "NHLArenas" VALUES(25,25,'Coyotes','Arizona Coyotes','Glendale','AZ','USA','United States','Glendale, AZ','Arizona','Glendale, Arizona','Gila River Arena','Gila River Arena, Glendale',0);
INSERT INTO "NHLArenas" VALUES(26,26,'Flames','Calgary Flames','Calgary','AB','CAN','Canada','Calgary, AB','Alberta','Calgary, Alberta','Scotiabank Saddledome','Scotiabank Saddledome, Calgary',0);
INSERT INTO "NHLArenas" VALUES(27,27,'Oilers','Edmonton Oilers','Edmonton','AB','CAN','Canada','Edmonton, AB','Alberta','Edmonton, Alberta','Rexall Place','Rexall Place, Edmonton',0);
INSERT INTO "NHLArenas" VALUES(28,28,'Kings','Los Angeles Kings','Los Angeles','CA','USA','United States','Los Angeles, CA','California','Los Angeles, California','Staples Center','Staples Center, Los Angeles',0);
INSERT INTO "NHLArenas" VALUES(29,29,'Sharks','San Jose Sharks','San Jose','CA','USA','United States','San Jose, CA','California','San Jose, California','SAP Center','SAP Center, San Jose',0);
INSERT INTO "NHLArenas" VALUES(30,30,'Canucks','Vancouver Canucks','Vancouver','BC','CAN','Canada','Vancouver, BC','British Columbia','Vancouver, British Columbia','Rogers Arena','Rogers Arena, Vancouver',0);
INSERT INTO "NHLArenas" VALUES(31,0,'','','Foxborough','MA','USA','United States','Foxborough, MA','Massachusetts','Foxborough, Massachusetts','Gillette Stadium','Gillette Stadium, Foxborough',0);
INSERT INTO "NHLArenas" VALUES(32,0,'','','Minneapolis','MN','USA','United States','Minneapolis, MN','Minnesota','Minneapolis, Minnesota','TCF Bank Stadium','TCF Bank Stadium, Minneapolis',0);
INSERT INTO "NHLArenas" VALUES(33,0,'','','Denver','CO','USA','United States','Denver, CO','Colorado','Denver, Colorado','Coors Field','Coors Field, Denver',0);
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
INSERT INTO "NHLConferences" VALUES(1,'Eastern','','Conference','Eastern Conference','NHL','National Hockey League',16,2);
INSERT INTO "NHLConferences" VALUES(2,'Western','','Conference','Western Conference','NHL','National Hockey League',14,2);
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
INSERT INTO "NHLDivisions" VALUES(1,'Atlantic','','Division','Atlantic Division','Eastern','Eastern Conference','NHL','National Hockey League',8);
INSERT INTO "NHLDivisions" VALUES(2,'Metropolitan','','Division','Metropolitan Division','Eastern','Eastern Conference','NHL','National Hockey League',8);
INSERT INTO "NHLDivisions" VALUES(3,'Central','','Division','Central Division','Western','Western Conference','NHL','National Hockey League',7);
INSERT INTO "NHLDivisions" VALUES(4,'Pacific','','Division','Pacific Division','Western','Western Conference','NHL','National Hockey League',7);
CREATE TABLE NHLGameStats (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  GameID INTEGER NOT NULL DEFAULT 0,
  Date INTEGER NOT NULL DEFAULT 0,
  Time INTEGER NOT NULL DEFAULT 0,
  DateTime INTEGER NOT NULL DEFAULT 0,
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
INSERT INTO "NHLStats" VALUES(1,1,20151000,0,201510000000,'Boston Bruins','Boston','Boston','','MA','USA','United States','Boston, MA','Massachusetts','Boston, Massachusetts','Bruins','Eastern','Eastern Conference','Atlantic','Atlantic Division','NHL','National Hockey League','TD Garden','TD Garden, Boston','ECHL:Atlanta Gladiators,AHL:Providence Bruins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(2,2,20151000,0,201510000000,'Buffalo Sabres','Buffalo','Buffalo','','NY','USA','United States','Buffalo, NY','New York','Buffalo, New York','Sabres','Eastern','Eastern Conference','Atlantic','Atlantic Division','NHL','National Hockey League','First Niagara Center','First Niagara Center, Buffalo','ECHL:Elmira Jackals,AHL:Rochester Americans',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(3,3,20151000,0,201510000000,'Detroit Red Wings','Detroit','Detroit','','MI','USA','United States','Detroit, MI','Michigan','Detroit, Michigan','Red Wings','Eastern','Eastern Conference','Atlantic','Atlantic Division','NHL','National Hockey League','Joe Louis Arena','Joe Louis Arena, Detroit','ECHL:Toledo Walleye,AHL:Grand Rapids Griffins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(4,4,20151000,0,201510000000,'Florida Panthers','Sunrise','Florida','','FL','USA','United States','Sunrise, FL','Florida','Sunrise, Florida','Panthers','Eastern','Eastern Conference','Atlantic','Atlantic Division','NHL','National Hockey League','BB&T Center','BB&T Center, Sunrise','ECHL:None,AHL:Portland Pirates',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(5,5,20151000,0,201510000000,'Montreal Canadiens','Montreal','Montreal','','QC','CAN','Canada','Montreal, QC','Quebec','Montreal, Quebec','Canadiens','Eastern','Eastern Conference','Atlantic','Atlantic Division','NHL','National Hockey League','Bell Centre','Bell Centre, Montreal','ECHL:Brampton Beast,AHL:St. John''s Icecaps',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(6,6,20151000,0,201510000000,'Ottawa Senators','Ottawa','Ottawa','','ON','CAN','Canada','Ottawa, ON','Ontario','Ottawa, Ontario','Senators','Eastern','Eastern Conference','Atlantic','Atlantic Division','NHL','National Hockey League','Canadian Tire Centre','Canadian Tire Centre, Ottawa','ECHL:Evansville IceMen,AHL:Binghamton Senators',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(7,7,20151000,0,201510000000,'Tampa Bay Lightning','Tampa Bay','Tampa Bay','','FL','USA','United States','Tampa Bay, FL','Florida','Tampa Bay, Florida','Lightning','Eastern','Eastern Conference','Atlantic','Atlantic Division','NHL','National Hockey League','Amalie Arena','Amalie Arena, Tampa Bay','ECHL:None,AHL:Syracuse Crunch',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(8,8,20151000,0,201510000000,'Toronto Maple Leafs','Toronto','Toronto','','ON','CAN','Canada','Toronto, ON','Ontario','Toronto, Ontario','Maple Leafs','Eastern','Eastern Conference','Atlantic','Atlantic Division','NHL','National Hockey League','Air Canada Centre','Air Canada Centre, Toronto','ECHL:Orlando Solar Bears,AHL:Toronto Marlies',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(9,9,20151000,0,201510000000,'Carolina Hurricanes','Carolina','Carolina','','NC','USA','United States','Carolina, NC','North Carolina','Carolina, North Carolina','Hurricanes','Eastern','Eastern Conference','Metropolitan','Metropolitan Division','NHL','National Hockey League','PNC Arena','PNC Arena, Carolina','ECHL:Florida Everblades,AHL:Charlotte Checkers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(10,10,20151000,0,201510000000,'Columbus Blue Jackets','Columbus','Columbus','','OH','USA','United States','Columbus, OH','Ohio','Columbus, Ohio','Blue Jackets','Eastern','Eastern Conference','Metropolitan','Metropolitan Division','NHL','National Hockey League','Nationwide Arena','Nationwide Arena, Columbus','ECHL:Kalamazoo Wings,AHL:Lake Erie Monsters',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(11,11,20151000,0,201510000000,'New Jersey Devils','New Jersey','New Jersey','','NJ','USA','United States','New Jersey, NJ','New Jersey','New Jersey, New Jersey','Devils','Eastern','Eastern Conference','Metropolitan','Metropolitan Division','NHL','National Hockey League','Prudential Center','Prudential Center, New Jersey','ECHL:None,AHL:Albany Devils',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(12,12,20151000,0,201510000000,'New York Islanders','New York City','New York','','NY','USA','United States','New York City, NY','New York','New York City, New York','Islanders','Eastern','Eastern Conference','Metropolitan','Metropolitan Division','NHL','National Hockey League','Barclays Center','Barclays Center, New York City','ECHL:Missouri Mavericks,AHL:Bridgeport Sound Tigers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(13,13,20151000,0,201510000000,'New York Rangers','New York City','New York','','NY','USA','United States','New York City, NY','New York','New York City, New York','Rangers','Eastern','Eastern Conference','Metropolitan','Metropolitan Division','NHL','National Hockey League','Madison Square Garden','Madison Square Garden, New York City','ECHL:Greenville Swamp Rabbits,AHL:Hartford Wolf Pack',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(14,14,20151000,0,201510000000,'Philadelphia Flyers','Philadelphia','Philadelphia','','PA','USA','United States','Philadelphia, PA','Pennsylvania','Philadelphia, Pennsylvania','Flyers','Eastern','Eastern Conference','Metropolitan','Metropolitan Division','NHL','National Hockey League','Wells Fargo Center','Wells Fargo Center, Philadelphia','ECHL:Reading Royals,AHL:Lehigh Valley Phantoms',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(15,15,20151000,0,201510000000,'Pittsburgh Penguins','Pittsburgh','Pittsburgh','','PA','USA','United States','Pittsburgh, PA','Pennsylvania','Pittsburgh, Pennsylvania','Penguins','Eastern','Eastern Conference','Metropolitan','Metropolitan Division','NHL','National Hockey League','Consol Energy Center','Consol Energy Center, Pittsburgh','ECHL:Wheeling Nailers,AHL:Wilkes-Barre/Scranton Penguins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(16,16,20151000,0,201510000000,'Washington Capitals','Washington','Washington','','DC','USA','United States','Washington, DC','District of Columbia','Washington, District of Columbia','Capitals','Eastern','Eastern Conference','Metropolitan','Metropolitan Division','NHL','National Hockey League','Verizon Center','Verizon Center, Washington','ECHL:South Carolina Stingrays,AHL:Hershey Bears',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(17,17,20151000,0,201510000000,'Chicago Blackhawks','Chicago','Chicago','','IL','USA','United States','Chicago, IL','Illinois','Chicago, Illinois','Blackhawks','Western','Western Conference','Central','Central Division','NHL','National Hockey League','United Center','United Center, Chicago','ECHL:Indy Fuel,AHL:Rockford IceHogs',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(18,18,20151000,0,201510000000,'Colorado Avalanche','Denver','Colorado','','CO','USA','United States','Denver, CO','Colorado','Denver, Colorado','Avalanche','Western','Western Conference','Central','Central Division','NHL','National Hockey League','Pepsi Center','Pepsi Center, Denver','ECHL:Fort Wayne Komets,AHL:San Antonio Rampage',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(19,19,20151000,0,201510000000,'Dallas Stars','Dallas','Dallas','','TX','USA','United States','Dallas, TX','Texas','Dallas, Texas','Stars','Western','Western Conference','Central','Central Division','NHL','National Hockey League','American Airlines Center','American Airlines Center, Dallas','ECHL:Idaho Steelheads,AHL:Texas Stars',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(20,20,20151000,0,201510000000,'Minnesota Wild','St. Paul','Minnesota','','MN','USA','United States','St. Paul, MN','Minnesota','St. Paul, Minnesota','Wild','Western','Western Conference','Central','Central Division','NHL','National Hockey League','Xcel Energy Center','Xcel Energy Center, St. Paul','ECHL:Quad City Mallards,AHL:Iowa Wild',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(21,21,20151000,0,201510000000,'Nashville Predators','Nashville','Nashville','','TN','USA','United States','Nashville, TN','Tennessee','Nashville, Tennessee','Predators','Western','Western Conference','Central','Central Division','NHL','National Hockey League','Bridgestone Arena','Bridgestone Arena, Nashville','ECHL:Cincinnati Cyclones,AHL:Milwaukee Admirals',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(22,22,20151000,0,201510000000,'St. Louis Blues','St. Louis','St. Louis','','MO','USA','United States','St. Louis, MO','Missouri','St. Louis, Missouri','Blues','Western','Western Conference','Central','Central Division','NHL','National Hockey League','Scottrade Center','Scottrade Center, St. Louis','ECHL:None,AHL:Chicago Wolves',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(23,23,20151000,0,201510000000,'Winnipeg Jets','Winnipeg','Winnipeg','','MB','CAN','Canada','Winnipeg, MB','Manitoba','Winnipeg, Manitoba','Jets','Western','Western Conference','Central','Central Division','NHL','National Hockey League','MTS Centre','MTS Centre, Winnipeg','ECHL:Tulsa Oilers,AHL:Manitoba Moose',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(24,24,20151000,0,201510000000,'Anaheim Ducks','Anaheim','Anaheim','','CA','USA','United States','Anaheim, CA','California','Anaheim, California','Ducks','Western','Western Conference','Pacific','Pacific Division','NHL','National Hockey League','Honda Center','Honda Center, Anaheim','ECHL:Utah Grizzlies,AHL:San Diego Gulls',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(25,25,20151000,0,201510000000,'Arizona Coyotes','Glendale','Arizona','','AZ','USA','United States','Glendale, AZ','Arizona','Glendale, Arizona','Coyotes','Western','Western Conference','Pacific','Pacific Division','NHL','National Hockey League','Gila River Arena','Gila River Arena, Glendale','ECHL:Rapid City Rush,AHL:Springfield Falcons',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(26,26,20151000,0,201510000000,'Calgary Flames','Calgary','Calgary','','AB','CAN','Canada','Calgary, AB','Alberta','Calgary, Alberta','Flames','Western','Western Conference','Pacific','Pacific Division','NHL','National Hockey League','Scotiabank Saddledome','Scotiabank Saddledome, Calgary','ECHL:Adirondack Thunder,AHL:Stockton Heat',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(27,27,20151000,0,201510000000,'Edmonton Oilers','Edmonton','Edmonton','','AB','CAN','Canada','Edmonton, AB','Alberta','Edmonton, Alberta','Oilers','Western','Western Conference','Pacific','Pacific Division','NHL','National Hockey League','Rexall Place','Rexall Place, Edmonton','ECHL:Norfolk Admirals,AHL:Bakersfield Condors',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(28,28,20151000,0,201510000000,'Los Angeles Kings','Los Angeles','Los Angeles','','CA','USA','United States','Los Angeles, CA','California','Los Angeles, California','Kings','Western','Western Conference','Pacific','Pacific Division','NHL','National Hockey League','Staples Center','Staples Center, Los Angeles','ECHL:Manchester Monarchs,AHL:Ontario Reign',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(29,29,20151000,0,201510000000,'San Jose Sharks','San Jose','San Jose','','CA','USA','United States','San Jose, CA','California','San Jose, California','Sharks','Western','Western Conference','Pacific','Pacific Division','NHL','National Hockey League','SAP Center','SAP Center, San Jose','ECHL:Allen Americans,AHL:San Jose Barracuda',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(30,30,20151000,0,201510000000,'Vancouver Canucks','Vancouver','Vancouver','','BC','CAN','Canada','Vancouver, BC','British Columbia','Vancouver, British Columbia','Canucks','Western','Western Conference','Pacific','Pacific Division','NHL','National Hockey League','Rogers Arena','Rogers Arena, Vancouver','ECHL:None,AHL:Utica Comets',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
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
INSERT INTO "NHLTeams" VALUES(1,20151000,0,201510000000,'Boston Bruins','Boston','Boston','','MA','USA','United States','Boston, MA','Massachusetts','Boston, Massachusetts','Bruins','Eastern','Eastern Conference','Atlantic','Atlantic Division','NHL','National Hockey League','TD Garden','TD Garden, Boston','ECHL:Atlanta Gladiators,AHL:Providence Bruins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(2,20151000,0,201510000000,'Buffalo Sabres','Buffalo','Buffalo','','NY','USA','United States','Buffalo, NY','New York','Buffalo, New York','Sabres','Eastern','Eastern Conference','Atlantic','Atlantic Division','NHL','National Hockey League','First Niagara Center','First Niagara Center, Buffalo','ECHL:Elmira Jackals,AHL:Rochester Americans',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(3,20151000,0,201510000000,'Detroit Red Wings','Detroit','Detroit','','MI','USA','United States','Detroit, MI','Michigan','Detroit, Michigan','Red Wings','Eastern','Eastern Conference','Atlantic','Atlantic Division','NHL','National Hockey League','Joe Louis Arena','Joe Louis Arena, Detroit','ECHL:Toledo Walleye,AHL:Grand Rapids Griffins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(4,20151000,0,201510000000,'Florida Panthers','Sunrise','Florida','','FL','USA','United States','Sunrise, FL','Florida','Sunrise, Florida','Panthers','Eastern','Eastern Conference','Atlantic','Atlantic Division','NHL','National Hockey League','BB&T Center','BB&T Center, Sunrise','ECHL:None,AHL:Portland Pirates',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(5,20151000,0,201510000000,'Montreal Canadiens','Montreal','Montreal','','QC','CAN','Canada','Montreal, QC','Quebec','Montreal, Quebec','Canadiens','Eastern','Eastern Conference','Atlantic','Atlantic Division','NHL','National Hockey League','Bell Centre','Bell Centre, Montreal','ECHL:Brampton Beast,AHL:St. John''s Icecaps',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(6,20151000,0,201510000000,'Ottawa Senators','Ottawa','Ottawa','','ON','CAN','Canada','Ottawa, ON','Ontario','Ottawa, Ontario','Senators','Eastern','Eastern Conference','Atlantic','Atlantic Division','NHL','National Hockey League','Canadian Tire Centre','Canadian Tire Centre, Ottawa','ECHL:Evansville IceMen,AHL:Binghamton Senators',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(7,20151000,0,201510000000,'Tampa Bay Lightning','Tampa Bay','Tampa Bay','','FL','USA','United States','Tampa Bay, FL','Florida','Tampa Bay, Florida','Lightning','Eastern','Eastern Conference','Atlantic','Atlantic Division','NHL','National Hockey League','Amalie Arena','Amalie Arena, Tampa Bay','ECHL:None,AHL:Syracuse Crunch',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(8,20151000,0,201510000000,'Toronto Maple Leafs','Toronto','Toronto','','ON','CAN','Canada','Toronto, ON','Ontario','Toronto, Ontario','Maple Leafs','Eastern','Eastern Conference','Atlantic','Atlantic Division','NHL','National Hockey League','Air Canada Centre','Air Canada Centre, Toronto','ECHL:Orlando Solar Bears,AHL:Toronto Marlies',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(9,20151000,0,201510000000,'Carolina Hurricanes','Carolina','Carolina','','NC','USA','United States','Carolina, NC','North Carolina','Carolina, North Carolina','Hurricanes','Eastern','Eastern Conference','Metropolitan','Metropolitan Division','NHL','National Hockey League','PNC Arena','PNC Arena, Carolina','ECHL:Florida Everblades,AHL:Charlotte Checkers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(10,20151000,0,201510000000,'Columbus Blue Jackets','Columbus','Columbus','','OH','USA','United States','Columbus, OH','Ohio','Columbus, Ohio','Blue Jackets','Eastern','Eastern Conference','Metropolitan','Metropolitan Division','NHL','National Hockey League','Nationwide Arena','Nationwide Arena, Columbus','ECHL:Kalamazoo Wings,AHL:Lake Erie Monsters',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(11,20151000,0,201510000000,'New Jersey Devils','New Jersey','New Jersey','','NJ','USA','United States','New Jersey, NJ','New Jersey','New Jersey, New Jersey','Devils','Eastern','Eastern Conference','Metropolitan','Metropolitan Division','NHL','National Hockey League','Prudential Center','Prudential Center, New Jersey','ECHL:None,AHL:Albany Devils',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(12,20151000,0,201510000000,'New York Islanders','New York City','New York','','NY','USA','United States','New York City, NY','New York','New York City, New York','Islanders','Eastern','Eastern Conference','Metropolitan','Metropolitan Division','NHL','National Hockey League','Barclays Center','Barclays Center, New York City','ECHL:Missouri Mavericks,AHL:Bridgeport Sound Tigers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(13,20151000,0,201510000000,'New York Rangers','New York City','New York','','NY','USA','United States','New York City, NY','New York','New York City, New York','Rangers','Eastern','Eastern Conference','Metropolitan','Metropolitan Division','NHL','National Hockey League','Madison Square Garden','Madison Square Garden, New York City','ECHL:Greenville Swamp Rabbits,AHL:Hartford Wolf Pack',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(14,20151000,0,201510000000,'Philadelphia Flyers','Philadelphia','Philadelphia','','PA','USA','United States','Philadelphia, PA','Pennsylvania','Philadelphia, Pennsylvania','Flyers','Eastern','Eastern Conference','Metropolitan','Metropolitan Division','NHL','National Hockey League','Wells Fargo Center','Wells Fargo Center, Philadelphia','ECHL:Reading Royals,AHL:Lehigh Valley Phantoms',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(15,20151000,0,201510000000,'Pittsburgh Penguins','Pittsburgh','Pittsburgh','','PA','USA','United States','Pittsburgh, PA','Pennsylvania','Pittsburgh, Pennsylvania','Penguins','Eastern','Eastern Conference','Metropolitan','Metropolitan Division','NHL','National Hockey League','Consol Energy Center','Consol Energy Center, Pittsburgh','ECHL:Wheeling Nailers,AHL:Wilkes-Barre/Scranton Penguins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(16,20151000,0,201510000000,'Washington Capitals','Washington','Washington','','DC','USA','United States','Washington, DC','District of Columbia','Washington, District of Columbia','Capitals','Eastern','Eastern Conference','Metropolitan','Metropolitan Division','NHL','National Hockey League','Verizon Center','Verizon Center, Washington','ECHL:South Carolina Stingrays,AHL:Hershey Bears',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(17,20151000,0,201510000000,'Chicago Blackhawks','Chicago','Chicago','','IL','USA','United States','Chicago, IL','Illinois','Chicago, Illinois','Blackhawks','Western','Western Conference','Central','Central Division','NHL','National Hockey League','United Center','United Center, Chicago','ECHL:Indy Fuel,AHL:Rockford IceHogs',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(18,20151000,0,201510000000,'Colorado Avalanche','Denver','Colorado','','CO','USA','United States','Denver, CO','Colorado','Denver, Colorado','Avalanche','Western','Western Conference','Central','Central Division','NHL','National Hockey League','Pepsi Center','Pepsi Center, Denver','ECHL:Fort Wayne Komets,AHL:San Antonio Rampage',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(19,20151000,0,201510000000,'Dallas Stars','Dallas','Dallas','','TX','USA','United States','Dallas, TX','Texas','Dallas, Texas','Stars','Western','Western Conference','Central','Central Division','NHL','National Hockey League','American Airlines Center','American Airlines Center, Dallas','ECHL:Idaho Steelheads,AHL:Texas Stars',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(20,20151000,0,201510000000,'Minnesota Wild','St. Paul','Minnesota','','MN','USA','United States','St. Paul, MN','Minnesota','St. Paul, Minnesota','Wild','Western','Western Conference','Central','Central Division','NHL','National Hockey League','Xcel Energy Center','Xcel Energy Center, St. Paul','ECHL:Quad City Mallards,AHL:Iowa Wild',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(21,20151000,0,201510000000,'Nashville Predators','Nashville','Nashville','','TN','USA','United States','Nashville, TN','Tennessee','Nashville, Tennessee','Predators','Western','Western Conference','Central','Central Division','NHL','National Hockey League','Bridgestone Arena','Bridgestone Arena, Nashville','ECHL:Cincinnati Cyclones,AHL:Milwaukee Admirals',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(22,20151000,0,201510000000,'St. Louis Blues','St. Louis','St. Louis','','MO','USA','United States','St. Louis, MO','Missouri','St. Louis, Missouri','Blues','Western','Western Conference','Central','Central Division','NHL','National Hockey League','Scottrade Center','Scottrade Center, St. Louis','ECHL:None,AHL:Chicago Wolves',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(23,20151000,0,201510000000,'Winnipeg Jets','Winnipeg','Winnipeg','','MB','CAN','Canada','Winnipeg, MB','Manitoba','Winnipeg, Manitoba','Jets','Western','Western Conference','Central','Central Division','NHL','National Hockey League','MTS Centre','MTS Centre, Winnipeg','ECHL:Tulsa Oilers,AHL:Manitoba Moose',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(24,20151000,0,201510000000,'Anaheim Ducks','Anaheim','Anaheim','','CA','USA','United States','Anaheim, CA','California','Anaheim, California','Ducks','Western','Western Conference','Pacific','Pacific Division','NHL','National Hockey League','Honda Center','Honda Center, Anaheim','ECHL:Utah Grizzlies,AHL:San Diego Gulls',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(25,20151000,0,201510000000,'Arizona Coyotes','Glendale','Arizona','','AZ','USA','United States','Glendale, AZ','Arizona','Glendale, Arizona','Coyotes','Western','Western Conference','Pacific','Pacific Division','NHL','National Hockey League','Gila River Arena','Gila River Arena, Glendale','ECHL:Rapid City Rush,AHL:Springfield Falcons',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(26,20151000,0,201510000000,'Calgary Flames','Calgary','Calgary','','AB','CAN','Canada','Calgary, AB','Alberta','Calgary, Alberta','Flames','Western','Western Conference','Pacific','Pacific Division','NHL','National Hockey League','Scotiabank Saddledome','Scotiabank Saddledome, Calgary','ECHL:Adirondack Thunder,AHL:Stockton Heat',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(27,20151000,0,201510000000,'Edmonton Oilers','Edmonton','Edmonton','','AB','CAN','Canada','Edmonton, AB','Alberta','Edmonton, Alberta','Oilers','Western','Western Conference','Pacific','Pacific Division','NHL','National Hockey League','Rexall Place','Rexall Place, Edmonton','ECHL:Norfolk Admirals,AHL:Bakersfield Condors',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(28,20151000,0,201510000000,'Los Angeles Kings','Los Angeles','Los Angeles','','CA','USA','United States','Los Angeles, CA','California','Los Angeles, California','Kings','Western','Western Conference','Pacific','Pacific Division','NHL','National Hockey League','Staples Center','Staples Center, Los Angeles','ECHL:Manchester Monarchs,AHL:Ontario Reign',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(29,20151000,0,201510000000,'San Jose Sharks','San Jose','San Jose','','CA','USA','United States','San Jose, CA','California','San Jose, California','Sharks','Western','Western Conference','Pacific','Pacific Division','NHL','National Hockey League','SAP Center','SAP Center, San Jose','ECHL:Allen Americans,AHL:San Jose Barracuda',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(30,20151000,0,201510000000,'Vancouver Canucks','Vancouver','Vancouver','','BC','CAN','Canada','Vancouver, BC','British Columbia','Vancouver, British Columbia','Canucks','Western','Western Conference','Pacific','Pacific Division','NHL','National Hockey League','Rogers Arena','Rogers Arena, Vancouver','ECHL:None,AHL:Utica Comets',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('HockeyLeagues',3);
INSERT INTO "sqlite_sequence" VALUES('ECHLConferences',2);
INSERT INTO "sqlite_sequence" VALUES('ECHLDivisions',6);
INSERT INTO "sqlite_sequence" VALUES('ECHLTeams',28);
INSERT INTO "sqlite_sequence" VALUES('ECHLStats',28);
INSERT INTO "sqlite_sequence" VALUES('ECHLArenas',28);
INSERT INTO "sqlite_sequence" VALUES('AHLConferences',2);
INSERT INTO "sqlite_sequence" VALUES('AHLDivisions',4);
INSERT INTO "sqlite_sequence" VALUES('AHLTeams',30);
INSERT INTO "sqlite_sequence" VALUES('AHLStats',30);
INSERT INTO "sqlite_sequence" VALUES('AHLArenas',31);
INSERT INTO "sqlite_sequence" VALUES('NHLConferences',2);
INSERT INTO "sqlite_sequence" VALUES('NHLDivisions',4);
INSERT INTO "sqlite_sequence" VALUES('NHLTeams',30);
INSERT INTO "sqlite_sequence" VALUES('NHLStats',30);
INSERT INTO "sqlite_sequence" VALUES('NHLArenas',33);
COMMIT;
