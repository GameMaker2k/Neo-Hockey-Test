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
INSERT INTO "AHLArenas" VALUES(3,3,'Bruins','Providence Bruins','Providence','RI','USA','United States','Providence, RI','Rhode Island','Providence, Rhode Island','Dunkin'' Donuts Center','Dunkin'' Donuts Center, Providence',0);
INSERT INTO "AHLArenas" VALUES(4,4,'Devils','Binghamton Devils','Newark','NJ','USA','United States','Newark, NJ','New Jersey','Newark, New Jersey','Barnabas Health Hockey House','Barnabas Health Hockey House, Newark',0);
INSERT INTO "AHLArenas" VALUES(5,5,'Bears','Hershey Bears','Hershey','PA','USA','United States','Hershey, PA','Pennsylvania','Hershey, Pennsylvania','Giant Center','Giant Center, Hershey',0);
INSERT INTO "AHLArenas" VALUES(6,6,'Phantoms','Lehigh Valley Phantoms','Allentown','PA','USA','United States','Allentown, PA','Pennsylvania','Allentown, Pennsylvania','PPL Center','PPL Center, Allentown',0);
INSERT INTO "AHLArenas" VALUES(7,7,'Americans','Rochester Americans','Buffalo','NY','USA','United States','Buffalo, NY','New York','Buffalo, New York','KeyBank Center','KeyBank Center, Buffalo',0);
INSERT INTO "AHLArenas" VALUES(8,8,'Crunch','Syracuse Crunch','Syracuse','NY','USA','United States','Syracuse, NY','New York','Syracuse, New York','Oncenter War Memorial Arena','Oncenter War Memorial Arena, Syracuse',0);
INSERT INTO "AHLArenas" VALUES(9,9,'Comets','Utica Comets','Utica','NY','USA','United States','Utica, NY','New York','Utica, New York','Adirondack Bank Center','Adirondack Bank Center, Utica',0);
INSERT INTO "AHLArenas" VALUES(10,10,'Penguins','Wilkes-Barre/Scranton Penguins','Wilkes-Barre','PA','USA','United States','Wilkes-Barre, PA','Pennsylvania','Wilkes-Barre, Pennsylvania','Mohegan Sun Arena','Mohegan Sun Arena, Wilkes-Barre',0);
INSERT INTO "AHLArenas" VALUES(11,11,'Senators','Belleville Senators','Ottawa','ON','CAN','Canada','Ottawa, ON','Ontario','Ottawa, Ontario','Canadian Tire Centre','Canadian Tire Centre, Ottawa',0);
INSERT INTO "AHLArenas" VALUES(12,12,'Rocket','Laval Rocket','Montreal','QC','CAN','Canada','Montreal, QC','Quebec','Montreal, Quebec','Bell Centre','Bell Centre, Montreal',0);
INSERT INTO "AHLArenas" VALUES(13,13,'Moose','Manitoba Moose','Winnipeg','MB','CAN','Canada','Winnipeg, MB','Manitoba','Winnipeg, Manitoba','Bell MTS Iceplex','Bell MTS Iceplex, Winnipeg',0);
INSERT INTO "AHLArenas" VALUES(14,14,'Heat','Stockton Heat','Calgary','AB','CAN','Canada','Calgary, AB','Alberta','Calgary, Alberta','Scotiabank Saddledome','Scotiabank Saddledome, Calgary',0);
INSERT INTO "AHLArenas" VALUES(15,15,'Marlies','Toronto Marlies','Toronto','ON','CAN','Canada','Toronto, ON','Ontario','Toronto, Ontario','Scotiabank Arena','Scotiabank Arena, Toronto',0);
INSERT INTO "AHLArenas" VALUES(16,16,'Wolves','Chicago Wolves','Rosemont','IL','USA','United States','Rosemont, IL','Illinois','Rosemont, Illinois','Allstate Arena','Allstate Arena, Rosemont',0);
INSERT INTO "AHLArenas" VALUES(17,17,'Monsters','Lake Erie Monsters','Cleveland','OH','USA','United States','Cleveland, OH','Ohio','Cleveland, Ohio','Rocket Mortgage FieldHouse','Rocket Mortgage FieldHouse, Cleveland',0);
INSERT INTO "AHLArenas" VALUES(18,18,'Griffins','Grand Rapids Griffins','Grand Rapids','MI','USA','United States','Grand Rapids, MI','Michigan','Grand Rapids, Michigan','Van Andel Arena','Van Andel Arena, Grand Rapids',0);
INSERT INTO "AHLArenas" VALUES(19,19,'Wild','Iowa Wild','Des Moines','IA','USA','United States','Des Moines, IA','Iowa','Des Moines, Iowa','Wells Fargo Arena','Wells Fargo Arena, Des Moines',0);
INSERT INTO "AHLArenas" VALUES(20,20,'IceHogs','Rockford IceHogs','Rockford','IL','USA','United States','Rockford, IL','Illinois','Rockford, Illinois','BMO Harris Bank Center','BMO Harris Bank Center, Rockford',0);
INSERT INTO "AHLArenas" VALUES(21,21,'Stars','Texas Stars','Cedar Park','TX','USA','United States','Cedar Park, TX','Texas','Cedar Park, Texas','H-E-B Center','H-E-B Center, Cedar Park',0);
INSERT INTO "AHLArenas" VALUES(22,22,'Condors','Bakersfield Condors','Bakersfield','CA','USA','United States','Bakersfield, CA','California','Bakersfield, California','Mechanics Bank Arena','Mechanics Bank Arena, Bakersfield',0);
INSERT INTO "AHLArenas" VALUES(23,23,'Eagles','Colorado Eagles','Loveland','CO','USA','United States','Loveland, CO','Colorado','Loveland, Colorado','Budweiser Events Center','Budweiser Events Center, Loveland',0);
INSERT INTO "AHLArenas" VALUES(24,24,'Silver Knights','Henderson Silver Knights','Paradise','NV','USA','United States','Paradise, NV','Nevada','Paradise, Nevada','Orleans Arena','Orleans Arena, Paradise',0);
INSERT INTO "AHLArenas" VALUES(25,25,'Reign','Ontario Reign','El Segundo','CA','USA','United States','El Segundo, CA','California','El Segundo, California','Toyota Sports Center','Toyota Sports Center, El Segundo',0);
INSERT INTO "AHLArenas" VALUES(26,26,'Gulls','San Diego Gulls','Irvine','CA','USA','United States','Irvine, CA','California','Irvine, California','Great Park Ice & FivePoint Arena','Great Park Ice & FivePoint Arena, Irvine',0);
INSERT INTO "AHLArenas" VALUES(27,27,'Barracuda','San Jose Barracuda','San Jose','CA','USA','United States','San Jose, CA','California','San Jose, California','SAP Center','SAP Center, San Jose',0);
INSERT INTO "AHLArenas" VALUES(28,28,'Roadrunners','Tucson Roadrunners','Tucson','AZ','USA','United States','Tucson, AZ','Arizona','Tucson, Arizona','Tucson Convention Center','Tucson Convention Center, Tucson',0);
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
INSERT INTO "AHLConferences" VALUES(1,'','','Conference',' Conference','AHL','American Hockey League',0,0);
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
INSERT INTO "AHLDivisions" VALUES(1,'Atlantic','','Division','Atlantic Division','',' Conference','AHL','American Hockey League',3);
INSERT INTO "AHLDivisions" VALUES(2,'North','','Division','North Division','',' Conference','AHL','American Hockey League',7);
INSERT INTO "AHLDivisions" VALUES(3,'Canadian','','Division','Canadian Division','',' Conference','AHL','American Hockey League',5);
INSERT INTO "AHLDivisions" VALUES(4,'Central','','Division','Central Division','',' Conference','AHL','American Hockey League',6);
INSERT INTO "AHLDivisions" VALUES(5,'Pacific','','Division','Pacific Division','',' Conference','AHL','American Hockey League',7);
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
INSERT INTO "AHLStats" VALUES(1,1,20210200,0,202102000000,'Bridgeport Sound Tigers','Bridgeport','Bridgeport','','CT','USA','United States','Bridgeport, CT','Connecticut','Bridgeport, Connecticut','Sound Tigers','',' Conference','Atlantic','Atlantic Division','AHL','American Hockey League','Webster Bank Arena','Webster Bank Arena, Bridgeport','NHL:New York Islanders',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(2,2,20210200,0,202102000000,'Hartford Wolf Pack','Hartford','Hartford','','CT','USA','United States','Hartford, CT','Connecticut','Hartford, Connecticut','Wolf Pack','',' Conference','Atlantic','Atlantic Division','AHL','American Hockey League','XL Center','XL Center, Hartford','NHL:New York Rangers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(3,3,20210200,0,202102000000,'Providence Bruins','Providence','Providence','','RI','USA','United States','Providence, RI','Rhode Island','Providence, Rhode Island','Bruins','',' Conference','Atlantic','Atlantic Division','AHL','American Hockey League','Dunkin'' Donuts Center','Dunkin'' Donuts Center, Providence','NHL:Boston Bruins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(4,4,20210200,0,202102000000,'Binghamton Devils','Newark','Binghamton','','NJ','USA','United States','Newark, NJ','New Jersey','Newark, New Jersey','Devils','',' Conference','North','North Division','AHL','American Hockey League','Barnabas Health Hockey House','Barnabas Health Hockey House, Newark','NHL:New Jersey Devils',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(5,5,20210200,0,202102000000,'Hershey Bears','Hershey','Hershey','','PA','USA','United States','Hershey, PA','Pennsylvania','Hershey, Pennsylvania','Bears','',' Conference','North','North Division','AHL','American Hockey League','Giant Center','Giant Center, Hershey','NHL:Washington Capitals',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(6,6,20210200,0,202102000000,'Lehigh Valley Phantoms','Allentown','Lehigh Valley','','PA','USA','United States','Allentown, PA','Pennsylvania','Allentown, Pennsylvania','Phantoms','',' Conference','North','North Division','AHL','American Hockey League','PPL Center','PPL Center, Allentown','NHL:Philadelphia Flyers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(7,7,20210200,0,202102000000,'Rochester Americans','Buffalo','Rochester','','NY','USA','United States','Buffalo, NY','New York','Buffalo, New York','Americans','',' Conference','North','North Division','AHL','American Hockey League','KeyBank Center','KeyBank Center, Buffalo','NHL:Buffalo Sabres',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(8,8,20210200,0,202102000000,'Syracuse Crunch','Syracuse','Syracuse','','NY','USA','United States','Syracuse, NY','New York','Syracuse, New York','Crunch','',' Conference','North','North Division','AHL','American Hockey League','Oncenter War Memorial Arena','Oncenter War Memorial Arena, Syracuse','NHL:Tampa Bay Lightning;Florida Panthers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(9,9,20210200,0,202102000000,'Utica Comets','Utica','Utica','','NY','USA','United States','Utica, NY','New York','Utica, New York','Comets','',' Conference','North','North Division','AHL','American Hockey League','Adirondack Bank Center','Adirondack Bank Center, Utica','NHL:Vancouver Canucks;St. Louis Blues',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(10,10,20210200,0,202102000000,'Wilkes-Barre/Scranton Penguins','Wilkes-Barre','Wilkes-Barre/Scranton','','PA','USA','United States','Wilkes-Barre, PA','Pennsylvania','Wilkes-Barre, Pennsylvania','Penguins','',' Conference','North','North Division','AHL','American Hockey League','Mohegan Sun Arena','Mohegan Sun Arena, Wilkes-Barre','NHL:Pittsburgh Penguins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(11,11,20210200,0,202102000000,'Belleville Senators','Ottawa','Belleville','','ON','CAN','Canada','Ottawa, ON','Ontario','Ottawa, Ontario','Senators','',' Conference','Canadian','Canadian Division','AHL','American Hockey League','Canadian Tire Centre','Canadian Tire Centre, Ottawa','NHL:Ottawa Senators',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(12,12,20210200,0,202102000000,'Laval Rocket','Montreal','Laval','','QC','CAN','Canada','Montreal, QC','Quebec','Montreal, Quebec','Rocket','',' Conference','Canadian','Canadian Division','AHL','American Hockey League','Bell Centre','Bell Centre, Montreal','NHL:Montreal Canadiens',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(13,13,20210200,0,202102000000,'Manitoba Moose','Winnipeg','Manitoba','','MB','CAN','Canada','Winnipeg, MB','Manitoba','Winnipeg, Manitoba','Moose','',' Conference','Canadian','Canadian Division','AHL','American Hockey League','Bell MTS Iceplex','Bell MTS Iceplex, Winnipeg','NHL:Winnipeg Jets',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(14,14,20210200,0,202102000000,'Stockton Heat','Calgary','Stockton','','AB','CAN','Canada','Calgary, AB','Alberta','Calgary, Alberta','Heat','',' Conference','Canadian','Canadian Division','AHL','American Hockey League','Scotiabank Saddledome','Scotiabank Saddledome, Calgary','NHL:Calgary Flames',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(15,15,20210200,0,202102000000,'Toronto Marlies','Toronto','Toronto','','ON','CAN','Canada','Toronto, ON','Ontario','Toronto, Ontario','Marlies','',' Conference','Canadian','Canadian Division','AHL','American Hockey League','Scotiabank Arena','Scotiabank Arena, Toronto','NHL:Toronto Maple Leafs',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(16,16,20210200,0,202102000000,'Chicago Wolves','Rosemont','Chicago','','IL','USA','United States','Rosemont, IL','Illinois','Rosemont, Illinois','Wolves','',' Conference','Central','Central Division','AHL','American Hockey League','Allstate Arena','Allstate Arena, Rosemont','NHL:Carolina Hurricanes',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(17,17,20210200,0,202102000000,'Lake Erie Monsters','Cleveland','Lake Erie','','OH','USA','United States','Cleveland, OH','Ohio','Cleveland, Ohio','Monsters','',' Conference','Central','Central Division','AHL','American Hockey League','Rocket Mortgage FieldHouse','Rocket Mortgage FieldHouse, Cleveland','NHL:Columbus Blue Jackets',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(18,18,20210200,0,202102000000,'Grand Rapids Griffins','Grand Rapids','Grand Rapids','','MI','USA','United States','Grand Rapids, MI','Michigan','Grand Rapids, Michigan','Griffins','',' Conference','Central','Central Division','AHL','American Hockey League','Van Andel Arena','Van Andel Arena, Grand Rapids','NHL:Detroit Red Wings',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(19,19,20210200,0,202102000000,'Iowa Wild','Des Moines','Iowa','','IA','USA','United States','Des Moines, IA','Iowa','Des Moines, Iowa','Wild','',' Conference','Central','Central Division','AHL','American Hockey League','Wells Fargo Arena','Wells Fargo Arena, Des Moines','NHL:Minnesota Wild',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(20,20,20210200,0,202102000000,'Rockford IceHogs','Rockford','Rockford','','IL','USA','United States','Rockford, IL','Illinois','Rockford, Illinois','IceHogs','',' Conference','Central','Central Division','AHL','American Hockey League','BMO Harris Bank Center','BMO Harris Bank Center, Rockford','NHL:Chicago Blackhawks',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(21,21,20210200,0,202102000000,'Texas Stars','Cedar Park','Texas','','TX','USA','United States','Cedar Park, TX','Texas','Cedar Park, Texas','Stars','',' Conference','Central','Central Division','AHL','American Hockey League','H-E-B Center','H-E-B Center, Cedar Park','NHL:Dallas Stars',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(22,22,20210200,0,202102000000,'Bakersfield Condors','Bakersfield','Bakersfield','','CA','USA','United States','Bakersfield, CA','California','Bakersfield, California','Condors','',' Conference','Pacific','Pacific Division','AHL','American Hockey League','Mechanics Bank Arena','Mechanics Bank Arena, Bakersfield','NHL:Edmonton Oilers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(23,23,20210200,0,202102000000,'Colorado Eagles','Loveland','Colorado','','CO','USA','United States','Loveland, CO','Colorado','Loveland, Colorado','Eagles','',' Conference','Pacific','Pacific Division','AHL','American Hockey League','Budweiser Events Center','Budweiser Events Center, Loveland','NHL:Colorado Avalanche',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(24,24,20210200,0,202102000000,'Henderson Silver Knights','Paradise','Henderson','','NV','USA','United States','Paradise, NV','Nevada','Paradise, Nevada','Silver Knights','',' Conference','Pacific','Pacific Division','AHL','American Hockey League','Orleans Arena','Orleans Arena, Paradise','NHL:Vegas Golden Knights',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(25,25,20210200,0,202102000000,'Ontario Reign','El Segundo','Ontario','','CA','USA','United States','El Segundo, CA','California','El Segundo, California','Reign','',' Conference','Pacific','Pacific Division','AHL','American Hockey League','Toyota Sports Center','Toyota Sports Center, El Segundo','NHL:Los Angeles Kings',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(26,26,20210200,0,202102000000,'San Diego Gulls','Irvine','San Diego','','CA','USA','United States','Irvine, CA','California','Irvine, California','Gulls','',' Conference','Pacific','Pacific Division','AHL','American Hockey League','Great Park Ice & FivePoint Arena','Great Park Ice & FivePoint Arena, Irvine','NHL:Anaheim Ducks',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(27,27,20210200,0,202102000000,'San Jose Barracuda','San Jose','San Jose','','CA','USA','United States','San Jose, CA','California','San Jose, California','Barracuda','',' Conference','Pacific','Pacific Division','AHL','American Hockey League','SAP Center','SAP Center, San Jose','NHL:San Jose Sharks',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLStats" VALUES(28,28,20210200,0,202102000000,'Tucson Roadrunners','Tucson','Tucson','','AZ','USA','United States','Tucson, AZ','Arizona','Tucson, Arizona','Roadrunners','',' Conference','Pacific','Pacific Division','AHL','American Hockey League','Tucson Convention Center','Tucson Convention Center, Tucson','NHL:Arizona Coyotes',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
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
INSERT INTO "AHLTeams" VALUES(1,20210200,0,202102000000,'Bridgeport Sound Tigers','Bridgeport','Bridgeport','','CT','USA','United States','Bridgeport, CT','Connecticut','Bridgeport, Connecticut','Sound Tigers','',' Conference','Atlantic','Atlantic Division','AHL','American Hockey League','Webster Bank Arena','Webster Bank Arena, Bridgeport','NHL:New York Islanders',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(2,20210200,0,202102000000,'Hartford Wolf Pack','Hartford','Hartford','','CT','USA','United States','Hartford, CT','Connecticut','Hartford, Connecticut','Wolf Pack','',' Conference','Atlantic','Atlantic Division','AHL','American Hockey League','XL Center','XL Center, Hartford','NHL:New York Rangers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(3,20210200,0,202102000000,'Providence Bruins','Providence','Providence','','RI','USA','United States','Providence, RI','Rhode Island','Providence, Rhode Island','Bruins','',' Conference','Atlantic','Atlantic Division','AHL','American Hockey League','Dunkin'' Donuts Center','Dunkin'' Donuts Center, Providence','NHL:Boston Bruins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(4,20210200,0,202102000000,'Binghamton Devils','Newark','Binghamton','','NJ','USA','United States','Newark, NJ','New Jersey','Newark, New Jersey','Devils','',' Conference','North','North Division','AHL','American Hockey League','Barnabas Health Hockey House','Barnabas Health Hockey House, Newark','NHL:New Jersey Devils',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(5,20210200,0,202102000000,'Hershey Bears','Hershey','Hershey','','PA','USA','United States','Hershey, PA','Pennsylvania','Hershey, Pennsylvania','Bears','',' Conference','North','North Division','AHL','American Hockey League','Giant Center','Giant Center, Hershey','NHL:Washington Capitals',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(6,20210200,0,202102000000,'Lehigh Valley Phantoms','Allentown','Lehigh Valley','','PA','USA','United States','Allentown, PA','Pennsylvania','Allentown, Pennsylvania','Phantoms','',' Conference','North','North Division','AHL','American Hockey League','PPL Center','PPL Center, Allentown','NHL:Philadelphia Flyers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(7,20210200,0,202102000000,'Rochester Americans','Buffalo','Rochester','','NY','USA','United States','Buffalo, NY','New York','Buffalo, New York','Americans','',' Conference','North','North Division','AHL','American Hockey League','KeyBank Center','KeyBank Center, Buffalo','NHL:Buffalo Sabres',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(8,20210200,0,202102000000,'Syracuse Crunch','Syracuse','Syracuse','','NY','USA','United States','Syracuse, NY','New York','Syracuse, New York','Crunch','',' Conference','North','North Division','AHL','American Hockey League','Oncenter War Memorial Arena','Oncenter War Memorial Arena, Syracuse','NHL:Tampa Bay Lightning;Florida Panthers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(9,20210200,0,202102000000,'Utica Comets','Utica','Utica','','NY','USA','United States','Utica, NY','New York','Utica, New York','Comets','',' Conference','North','North Division','AHL','American Hockey League','Adirondack Bank Center','Adirondack Bank Center, Utica','NHL:Vancouver Canucks;St. Louis Blues',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(10,20210200,0,202102000000,'Wilkes-Barre/Scranton Penguins','Wilkes-Barre','Wilkes-Barre/Scranton','','PA','USA','United States','Wilkes-Barre, PA','Pennsylvania','Wilkes-Barre, Pennsylvania','Penguins','',' Conference','North','North Division','AHL','American Hockey League','Mohegan Sun Arena','Mohegan Sun Arena, Wilkes-Barre','NHL:Pittsburgh Penguins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(11,20210200,0,202102000000,'Belleville Senators','Ottawa','Belleville','','ON','CAN','Canada','Ottawa, ON','Ontario','Ottawa, Ontario','Senators','',' Conference','Canadian','Canadian Division','AHL','American Hockey League','Canadian Tire Centre','Canadian Tire Centre, Ottawa','NHL:Ottawa Senators',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(12,20210200,0,202102000000,'Laval Rocket','Montreal','Laval','','QC','CAN','Canada','Montreal, QC','Quebec','Montreal, Quebec','Rocket','',' Conference','Canadian','Canadian Division','AHL','American Hockey League','Bell Centre','Bell Centre, Montreal','NHL:Montreal Canadiens',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(13,20210200,0,202102000000,'Manitoba Moose','Winnipeg','Manitoba','','MB','CAN','Canada','Winnipeg, MB','Manitoba','Winnipeg, Manitoba','Moose','',' Conference','Canadian','Canadian Division','AHL','American Hockey League','Bell MTS Iceplex','Bell MTS Iceplex, Winnipeg','NHL:Winnipeg Jets',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(14,20210200,0,202102000000,'Stockton Heat','Calgary','Stockton','','AB','CAN','Canada','Calgary, AB','Alberta','Calgary, Alberta','Heat','',' Conference','Canadian','Canadian Division','AHL','American Hockey League','Scotiabank Saddledome','Scotiabank Saddledome, Calgary','NHL:Calgary Flames',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(15,20210200,0,202102000000,'Toronto Marlies','Toronto','Toronto','','ON','CAN','Canada','Toronto, ON','Ontario','Toronto, Ontario','Marlies','',' Conference','Canadian','Canadian Division','AHL','American Hockey League','Scotiabank Arena','Scotiabank Arena, Toronto','NHL:Toronto Maple Leafs',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(16,20210200,0,202102000000,'Chicago Wolves','Rosemont','Chicago','','IL','USA','United States','Rosemont, IL','Illinois','Rosemont, Illinois','Wolves','',' Conference','Central','Central Division','AHL','American Hockey League','Allstate Arena','Allstate Arena, Rosemont','NHL:Carolina Hurricanes',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(17,20210200,0,202102000000,'Lake Erie Monsters','Cleveland','Lake Erie','','OH','USA','United States','Cleveland, OH','Ohio','Cleveland, Ohio','Monsters','',' Conference','Central','Central Division','AHL','American Hockey League','Rocket Mortgage FieldHouse','Rocket Mortgage FieldHouse, Cleveland','NHL:Columbus Blue Jackets',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(18,20210200,0,202102000000,'Grand Rapids Griffins','Grand Rapids','Grand Rapids','','MI','USA','United States','Grand Rapids, MI','Michigan','Grand Rapids, Michigan','Griffins','',' Conference','Central','Central Division','AHL','American Hockey League','Van Andel Arena','Van Andel Arena, Grand Rapids','NHL:Detroit Red Wings',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(19,20210200,0,202102000000,'Iowa Wild','Des Moines','Iowa','','IA','USA','United States','Des Moines, IA','Iowa','Des Moines, Iowa','Wild','',' Conference','Central','Central Division','AHL','American Hockey League','Wells Fargo Arena','Wells Fargo Arena, Des Moines','NHL:Minnesota Wild',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(20,20210200,0,202102000000,'Rockford IceHogs','Rockford','Rockford','','IL','USA','United States','Rockford, IL','Illinois','Rockford, Illinois','IceHogs','',' Conference','Central','Central Division','AHL','American Hockey League','BMO Harris Bank Center','BMO Harris Bank Center, Rockford','NHL:Chicago Blackhawks',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(21,20210200,0,202102000000,'Texas Stars','Cedar Park','Texas','','TX','USA','United States','Cedar Park, TX','Texas','Cedar Park, Texas','Stars','',' Conference','Central','Central Division','AHL','American Hockey League','H-E-B Center','H-E-B Center, Cedar Park','NHL:Dallas Stars',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(22,20210200,0,202102000000,'Bakersfield Condors','Bakersfield','Bakersfield','','CA','USA','United States','Bakersfield, CA','California','Bakersfield, California','Condors','',' Conference','Pacific','Pacific Division','AHL','American Hockey League','Mechanics Bank Arena','Mechanics Bank Arena, Bakersfield','NHL:Edmonton Oilers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(23,20210200,0,202102000000,'Colorado Eagles','Loveland','Colorado','','CO','USA','United States','Loveland, CO','Colorado','Loveland, Colorado','Eagles','',' Conference','Pacific','Pacific Division','AHL','American Hockey League','Budweiser Events Center','Budweiser Events Center, Loveland','NHL:Colorado Avalanche',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(24,20210200,0,202102000000,'Henderson Silver Knights','Paradise','Henderson','','NV','USA','United States','Paradise, NV','Nevada','Paradise, Nevada','Silver Knights','',' Conference','Pacific','Pacific Division','AHL','American Hockey League','Orleans Arena','Orleans Arena, Paradise','NHL:Vegas Golden Knights',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(25,20210200,0,202102000000,'Ontario Reign','El Segundo','Ontario','','CA','USA','United States','El Segundo, CA','California','El Segundo, California','Reign','',' Conference','Pacific','Pacific Division','AHL','American Hockey League','Toyota Sports Center','Toyota Sports Center, El Segundo','NHL:Los Angeles Kings',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(26,20210200,0,202102000000,'San Diego Gulls','Irvine','San Diego','','CA','USA','United States','Irvine, CA','California','Irvine, California','Gulls','',' Conference','Pacific','Pacific Division','AHL','American Hockey League','Great Park Ice & FivePoint Arena','Great Park Ice & FivePoint Arena, Irvine','NHL:Anaheim Ducks',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(27,20210200,0,202102000000,'San Jose Barracuda','San Jose','San Jose','','CA','USA','United States','San Jose, CA','California','San Jose, California','Barracuda','',' Conference','Pacific','Pacific Division','AHL','American Hockey League','SAP Center','SAP Center, San Jose','NHL:San Jose Sharks',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "AHLTeams" VALUES(28,20210200,0,202102000000,'Tucson Roadrunners','Tucson','Tucson','','AZ','USA','United States','Tucson, AZ','Arizona','Tucson, Arizona','Roadrunners','',' Conference','Pacific','Pacific Division','AHL','American Hockey League','Tucson Convention Center','Tucson Convention Center, Tucson','NHL:Arizona Coyotes',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
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
INSERT INTO "HockeyLeagues" VALUES(1,'NHL','National Hockey League','USA','United States',20210113,'Division=4','ORDER BY Points DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC',31,0,4);
INSERT INTO "HockeyLeagues" VALUES(2,'AHL','American Hockey League','USA','United States',20210205,'Division=4','ORDER BY PCT DESC, GamesPlayed ASC, TWins DESC, Losses ASC, GoalsDifference DESC',28,0,5);
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
INSERT INTO "NHLArenas" VALUES(1,1,'Hurricanes','Carolina Hurricanes','Carolina','NC','USA','United States','Carolina, NC','North Carolina','Carolina, North Carolina','PNC Arena','PNC Arena, Carolina',0);
INSERT INTO "NHLArenas" VALUES(2,2,'Blackhawks','Chicago Blackhawks','Chicago','IL','USA','United States','Chicago, IL','Illinois','Chicago, Illinois','United Center','United Center, Chicago',0);
INSERT INTO "NHLArenas" VALUES(3,3,'Blue Jackets','Columbus Blue Jackets','Columbus','OH','USA','United States','Columbus, OH','Ohio','Columbus, Ohio','Nationwide Arena','Nationwide Arena, Columbus',0);
INSERT INTO "NHLArenas" VALUES(4,4,'Stars','Dallas Stars','Dallas','TX','USA','United States','Dallas, TX','Texas','Dallas, Texas','American Airlines Center','American Airlines Center, Dallas',0);
INSERT INTO "NHLArenas" VALUES(5,5,'Red Wings','Detroit Red Wings','Detroit','MI','USA','United States','Detroit, MI','Michigan','Detroit, Michigan','Little Caesars Arena','Little Caesars Arena, Detroit',0);
INSERT INTO "NHLArenas" VALUES(6,6,'Panthers','Florida Panthers','Sunrise','FL','USA','United States','Sunrise, FL','Florida','Sunrise, Florida','BB&T Center','BB&T Center, Sunrise',0);
INSERT INTO "NHLArenas" VALUES(7,7,'Predators','Nashville Predators','Nashville','TN','USA','United States','Nashville, TN','Tennessee','Nashville, Tennessee','Bridgestone Arena','Bridgestone Arena, Nashville',0);
INSERT INTO "NHLArenas" VALUES(8,8,'Lightning','Tampa Bay Lightning','Tampa Bay','FL','USA','United States','Tampa Bay, FL','Florida','Tampa Bay, Florida','Amalie Arena','Amalie Arena, Tampa Bay',0);
INSERT INTO "NHLArenas" VALUES(9,9,'Ducks','Anaheim Ducks','Anaheim','CA','USA','United States','Anaheim, CA','California','Anaheim, California','Honda Center','Honda Center, Anaheim',0);
INSERT INTO "NHLArenas" VALUES(10,10,'Coyotes','Arizona Coyotes','Glendale','AZ','USA','United States','Glendale, AZ','Arizona','Glendale, Arizona','Gila River Arena','Gila River Arena, Glendale',0);
INSERT INTO "NHLArenas" VALUES(11,11,'Avalanche','Colorado Avalanche','Denver','CO','USA','United States','Denver, CO','Colorado','Denver, Colorado','Ball Arena','Ball Arena, Denver',0);
INSERT INTO "NHLArenas" VALUES(12,12,'Kings','Los Angeles Kings','Los Angeles','CA','USA','United States','Los Angeles, CA','California','Los Angeles, California','Staples Center','Staples Center, Los Angeles',0);
INSERT INTO "NHLArenas" VALUES(13,13,'Wild','Minnesota Wild','St. Paul','MN','USA','United States','St. Paul, MN','Minnesota','St. Paul, Minnesota','Xcel Energy Center','Xcel Energy Center, St. Paul',0);
INSERT INTO "NHLArenas" VALUES(14,14,'Blues','St. Louis Blues','St. Louis','MO','USA','United States','St. Louis, MO','Missouri','St. Louis, Missouri','Enterprise Center','Enterprise Center, St. Louis',0);
INSERT INTO "NHLArenas" VALUES(15,15,'Sharks','San Jose Sharks','San Jose','CA','USA','United States','San Jose, CA','California','San Jose, California','SAP Center','SAP Center, San Jose',0);
INSERT INTO "NHLArenas" VALUES(16,16,'Golden Knights','Vegas Golden Knights','Paradise','NV','USA','United States','Paradise, NV','Nevada','Paradise, Nevada','T-Mobile Arena','T-Mobile Arena, Paradise',0);
INSERT INTO "NHLArenas" VALUES(17,17,'Bruins','Boston Bruins','Boston','MA','USA','United States','Boston, MA','Massachusetts','Boston, Massachusetts','TD Garden','TD Garden, Boston',0);
INSERT INTO "NHLArenas" VALUES(18,18,'Sabres','Buffalo Sabres','Buffalo','NY','USA','United States','Buffalo, NY','New York','Buffalo, New York','KeyBank Center','KeyBank Center, Buffalo',0);
INSERT INTO "NHLArenas" VALUES(19,19,'Devils','New Jersey Devils','New Jersey','NJ','USA','United States','New Jersey, NJ','New Jersey','New Jersey, New Jersey','Prudential Center','Prudential Center, New Jersey',0);
INSERT INTO "NHLArenas" VALUES(20,20,'Islanders','New York Islanders','Uniondale','NY','USA','United States','Uniondale, NY','New York','Uniondale, New York','Nassau Coliseum','Nassau Coliseum, Uniondale',0);
INSERT INTO "NHLArenas" VALUES(21,21,'Rangers','New York Rangers','New York City','NY','USA','United States','New York City, NY','New York','New York City, New York','Madison Square Garden','Madison Square Garden, New York City',0);
INSERT INTO "NHLArenas" VALUES(22,22,'Flyers','Philadelphia Flyers','Philadelphia','PA','USA','United States','Philadelphia, PA','Pennsylvania','Philadelphia, Pennsylvania','Wells Fargo Center','Wells Fargo Center, Philadelphia',0);
INSERT INTO "NHLArenas" VALUES(23,23,'Penguins','Pittsburgh Penguins','Pittsburgh','PA','USA','United States','Pittsburgh, PA','Pennsylvania','Pittsburgh, Pennsylvania','PPG Paints Arena','PPG Paints Arena, Pittsburgh',0);
INSERT INTO "NHLArenas" VALUES(24,24,'Capitals','Washington Capitals','Washington','DC','USA','United States','Washington, DC','District of Columbia','Washington, District of Columbia','Capital One Arena','Capital One Arena, Washington',0);
INSERT INTO "NHLArenas" VALUES(25,25,'Flames','Calgary Flames','Calgary','AB','CAN','Canada','Calgary, AB','Alberta','Calgary, Alberta','Scotiabank Saddledome','Scotiabank Saddledome, Calgary',0);
INSERT INTO "NHLArenas" VALUES(26,26,'Oilers','Edmonton Oilers','Edmonton','AB','CAN','Canada','Edmonton, AB','Alberta','Edmonton, Alberta','Rogers Place','Rogers Place, Edmonton',0);
INSERT INTO "NHLArenas" VALUES(27,27,'Canadiens','Montreal Canadiens','Montreal','QC','CAN','Canada','Montreal, QC','Quebec','Montreal, Quebec','Bell Centre','Bell Centre, Montreal',0);
INSERT INTO "NHLArenas" VALUES(28,28,'Senators','Ottawa Senators','Ottawa','ON','CAN','Canada','Ottawa, ON','Ontario','Ottawa, Ontario','Canadian Tire Centre','Canadian Tire Centre, Ottawa',0);
INSERT INTO "NHLArenas" VALUES(29,29,'Maple Leafs','Toronto Maple Leafs','Toronto','ON','CAN','Canada','Toronto, ON','Ontario','Toronto, Ontario','Scotiabank Arena','Scotiabank Arena, Toronto',0);
INSERT INTO "NHLArenas" VALUES(30,30,'Canucks','Vancouver Canucks','Vancouver','BC','CAN','Canada','Vancouver, BC','British Columbia','Vancouver, British Columbia','Rogers Arena','Rogers Arena, Vancouver',0);
INSERT INTO "NHLArenas" VALUES(31,31,'Jets','Winnipeg Jets','Winnipeg','MB','CAN','Canada','Winnipeg, MB','Manitoba','Winnipeg, Manitoba','Bell MTS Place','Bell MTS Place, Winnipeg',0);
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
INSERT INTO "NHLConferences" VALUES(1,'','','Conference',' Conference','NHL','National Hockey League',0,0);
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
INSERT INTO "NHLDivisions" VALUES(1,'Central','Discover','Division','Discover Central Division','',' Conference','NHL','National Hockey League',8);
INSERT INTO "NHLDivisions" VALUES(2,'West','Honda','Division','Honda West Division','',' Conference','NHL','National Hockey League',8);
INSERT INTO "NHLDivisions" VALUES(3,'East','Massmutual','Division','Massmutual East Division','',' Conference','NHL','National Hockey League',8);
INSERT INTO "NHLDivisions" VALUES(4,'North','Scotia','Division','Scotia North Division','',' Conference','NHL','National Hockey League',7);
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
INSERT INTO "NHLStats" VALUES(1,1,20210100,0,202101000000,'Carolina Hurricanes','Carolina','Carolina','','NC','USA','United States','Carolina, NC','North Carolina','Carolina, North Carolina','Hurricanes','',' Conference','Central','Discover Central Division','NHL','National Hockey League','PNC Arena','PNC Arena, Carolina','AHL:Chicago Wolves',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(2,2,20210100,0,202101000000,'Chicago Blackhawks','Chicago','Chicago','','IL','USA','United States','Chicago, IL','Illinois','Chicago, Illinois','Blackhawks','',' Conference','Central','Discover Central Division','NHL','National Hockey League','United Center','United Center, Chicago','AHL:Rockford IceHogs',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(3,3,20210100,0,202101000000,'Columbus Blue Jackets','Columbus','Columbus','','OH','USA','United States','Columbus, OH','Ohio','Columbus, Ohio','Blue Jackets','',' Conference','Central','Discover Central Division','NHL','National Hockey League','Nationwide Arena','Nationwide Arena, Columbus','AHL:Cleveland Monsters',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(4,4,20210100,0,202101000000,'Dallas Stars','Dallas','Dallas','','TX','USA','United States','Dallas, TX','Texas','Dallas, Texas','Stars','',' Conference','Central','Discover Central Division','NHL','National Hockey League','American Airlines Center','American Airlines Center, Dallas','AHL:Texas Stars',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(5,5,20210100,0,202101000000,'Detroit Red Wings','Detroit','Detroit','','MI','USA','United States','Detroit, MI','Michigan','Detroit, Michigan','Red Wings','',' Conference','Central','Discover Central Division','NHL','National Hockey League','Little Caesars Arena','Little Caesars Arena, Detroit','AHL:Grand Rapids Griffins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(6,6,20210100,0,202101000000,'Florida Panthers','Sunrise','Florida','','FL','USA','United States','Sunrise, FL','Florida','Sunrise, Florida','Panthers','',' Conference','Central','Discover Central Division','NHL','National Hockey League','BB&T Center','BB&T Center, Sunrise','AHL:Syracuse Crunch',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(7,7,20210100,0,202101000000,'Nashville Predators','Nashville','Nashville','','TN','USA','United States','Nashville, TN','Tennessee','Nashville, Tennessee','Predators','',' Conference','Central','Discover Central Division','NHL','National Hockey League','Bridgestone Arena','Bridgestone Arena, Nashville','AHL:Chicago Wolves',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(8,8,20210100,0,202101000000,'Tampa Bay Lightning','Tampa Bay','Tampa Bay','','FL','USA','United States','Tampa Bay, FL','Florida','Tampa Bay, Florida','Lightning','',' Conference','Central','Discover Central Division','NHL','National Hockey League','Amalie Arena','Amalie Arena, Tampa Bay','AHL:Syracuse Crunch',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(9,9,20210100,0,202101000000,'Anaheim Ducks','Anaheim','Anaheim','','CA','USA','United States','Anaheim, CA','California','Anaheim, California','Ducks','',' Conference','West','Honda West Division','NHL','National Hockey League','Honda Center','Honda Center, Anaheim','AHL:San Diego Gulls',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(10,10,20210100,0,202101000000,'Arizona Coyotes','Glendale','Arizona','','AZ','USA','United States','Glendale, AZ','Arizona','Glendale, Arizona','Coyotes','',' Conference','West','Honda West Division','NHL','National Hockey League','Gila River Arena','Gila River Arena, Glendale','AHL:Tucson Roadrunners',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(11,11,20210100,0,202101000000,'Colorado Avalanche','Denver','Colorado','','CO','USA','United States','Denver, CO','Colorado','Denver, Colorado','Avalanche','',' Conference','West','Honda West Division','NHL','National Hockey League','Ball Arena','Ball Arena, Denver','AHL:Colorado Eagles',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(12,12,20210100,0,202101000000,'Los Angeles Kings','Los Angeles','Los Angeles','','CA','USA','United States','Los Angeles, CA','California','Los Angeles, California','Kings','',' Conference','West','Honda West Division','NHL','National Hockey League','Staples Center','Staples Center, Los Angeles','AHL:Ontario Reign',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(13,13,20210100,0,202101000000,'Minnesota Wild','St. Paul','Minnesota','','MN','USA','United States','St. Paul, MN','Minnesota','St. Paul, Minnesota','Wild','',' Conference','West','Honda West Division','NHL','National Hockey League','Xcel Energy Center','Xcel Energy Center, St. Paul','AHL:Iowa Wild',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(14,14,20210100,0,202101000000,'St. Louis Blues','St. Louis','St. Louis','','MO','USA','United States','St. Louis, MO','Missouri','St. Louis, Missouri','Blues','',' Conference','West','Honda West Division','NHL','National Hockey League','Enterprise Center','Enterprise Center, St. Louis','AHL:Utica Comets',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(15,15,20210100,0,202101000000,'San Jose Sharks','San Jose','San Jose','','CA','USA','United States','San Jose, CA','California','San Jose, California','Sharks','',' Conference','West','Honda West Division','NHL','National Hockey League','SAP Center','SAP Center, San Jose','AHL:San Jose Barracuda',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(16,16,20210100,0,202101000000,'Vegas Golden Knights','Paradise','Vegas','','NV','USA','United States','Paradise, NV','Nevada','Paradise, Nevada','Golden Knights','',' Conference','West','Honda West Division','NHL','National Hockey League','T-Mobile Arena','T-Mobile Arena, Paradise','AHL:Henderson Silver Knights',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(17,17,20210100,0,202101000000,'Boston Bruins','Boston','Boston','','MA','USA','United States','Boston, MA','Massachusetts','Boston, Massachusetts','Bruins','',' Conference','East','Massmutual East Division','NHL','National Hockey League','TD Garden','TD Garden, Boston','AHL:Providence Bruins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(18,18,20210100,0,202101000000,'Buffalo Sabres','Buffalo','Buffalo','','NY','USA','United States','Buffalo, NY','New York','Buffalo, New York','Sabres','',' Conference','East','Massmutual East Division','NHL','National Hockey League','KeyBank Center','KeyBank Center, Buffalo','AHL:Rochester Americans',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(19,19,20210100,0,202101000000,'New Jersey Devils','New Jersey','New Jersey','','NJ','USA','United States','New Jersey, NJ','New Jersey','New Jersey, New Jersey','Devils','',' Conference','East','Massmutual East Division','NHL','National Hockey League','Prudential Center','Prudential Center, New Jersey','AHL:Binghamton Devils',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(20,20,20210100,0,202101000000,'New York Islanders','Uniondale','New York','','NY','USA','United States','Uniondale, NY','New York','Uniondale, New York','Islanders','',' Conference','East','Massmutual East Division','NHL','National Hockey League','Nassau Coliseum','Nassau Coliseum, Uniondale','AHL:Bridgeport Sound Tigers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(21,21,20210100,0,202101000000,'New York Rangers','New York City','New York','','NY','USA','United States','New York City, NY','New York','New York City, New York','Rangers','',' Conference','East','Massmutual East Division','NHL','National Hockey League','Madison Square Garden','Madison Square Garden, New York City','AHL:Hartford Wolf Pack',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(22,22,20210100,0,202101000000,'Philadelphia Flyers','Philadelphia','Philadelphia','','PA','USA','United States','Philadelphia, PA','Pennsylvania','Philadelphia, Pennsylvania','Flyers','',' Conference','East','Massmutual East Division','NHL','National Hockey League','Wells Fargo Center','Wells Fargo Center, Philadelphia','AHL:Lehigh Valley Phantoms',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(23,23,20210100,0,202101000000,'Pittsburgh Penguins','Pittsburgh','Pittsburgh','','PA','USA','United States','Pittsburgh, PA','Pennsylvania','Pittsburgh, Pennsylvania','Penguins','',' Conference','East','Massmutual East Division','NHL','National Hockey League','PPG Paints Arena','PPG Paints Arena, Pittsburgh','AHL:Wilkes-Barre/Scranton Penguins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(24,24,20210100,0,202101000000,'Washington Capitals','Washington','Washington','','DC','USA','United States','Washington, DC','District of Columbia','Washington, District of Columbia','Capitals','',' Conference','East','Massmutual East Division','NHL','National Hockey League','Capital One Arena','Capital One Arena, Washington','AHL:Hershey Bears',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(25,25,20210100,0,202101000000,'Calgary Flames','Calgary','Calgary','','AB','CAN','Canada','Calgary, AB','Alberta','Calgary, Alberta','Flames','',' Conference','North','Scotia North Division','NHL','National Hockey League','Scotiabank Saddledome','Scotiabank Saddledome, Calgary','AHL:Stockton Heat',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(26,26,20210100,0,202101000000,'Edmonton Oilers','Edmonton','Edmonton','','AB','CAN','Canada','Edmonton, AB','Alberta','Edmonton, Alberta','Oilers','',' Conference','North','Scotia North Division','NHL','National Hockey League','Rogers Place','Rogers Place, Edmonton','AHL:Bakersfield Condors',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(27,27,20210100,0,202101000000,'Montreal Canadiens','Montreal','Montreal','','QC','CAN','Canada','Montreal, QC','Quebec','Montreal, Quebec','Canadiens','',' Conference','North','Scotia North Division','NHL','National Hockey League','Bell Centre','Bell Centre, Montreal','AHL:Laval Rocket',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(28,28,20210100,0,202101000000,'Ottawa Senators','Ottawa','Ottawa','','ON','CAN','Canada','Ottawa, ON','Ontario','Ottawa, Ontario','Senators','',' Conference','North','Scotia North Division','NHL','National Hockey League','Canadian Tire Centre','Canadian Tire Centre, Ottawa','AHL:Belleville Senators',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(29,29,20210100,0,202101000000,'Toronto Maple Leafs','Toronto','Toronto','','ON','CAN','Canada','Toronto, ON','Ontario','Toronto, Ontario','Maple Leafs','',' Conference','North','Scotia North Division','NHL','National Hockey League','Scotiabank Arena','Scotiabank Arena, Toronto','AHL:Toronto Marlies',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(30,30,20210100,0,202101000000,'Vancouver Canucks','Vancouver','Vancouver','','BC','CAN','Canada','Vancouver, BC','British Columbia','Vancouver, British Columbia','Canucks','',' Conference','North','Scotia North Division','NHL','National Hockey League','Rogers Arena','Rogers Arena, Vancouver','AHL:Utica Comets',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLStats" VALUES(31,31,20210100,0,202101000000,'Winnipeg Jets','Winnipeg','Winnipeg','','MB','CAN','Canada','Winnipeg, MB','Manitoba','Winnipeg, Manitoba','Jets','',' Conference','North','Scotia North Division','NHL','National Hockey League','Bell MTS Place','Bell MTS Place, Winnipeg','AHL:Manitoba Moose',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
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
INSERT INTO "NHLTeams" VALUES(1,20210100,0,202101000000,'Carolina Hurricanes','Carolina','Carolina','','NC','USA','United States','Carolina, NC','North Carolina','Carolina, North Carolina','Hurricanes','',' Conference','Central','Discover Central Division','NHL','National Hockey League','PNC Arena','PNC Arena, Carolina','AHL:Chicago Wolves',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(2,20210100,0,202101000000,'Chicago Blackhawks','Chicago','Chicago','','IL','USA','United States','Chicago, IL','Illinois','Chicago, Illinois','Blackhawks','',' Conference','Central','Discover Central Division','NHL','National Hockey League','United Center','United Center, Chicago','AHL:Rockford IceHogs',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(3,20210100,0,202101000000,'Columbus Blue Jackets','Columbus','Columbus','','OH','USA','United States','Columbus, OH','Ohio','Columbus, Ohio','Blue Jackets','',' Conference','Central','Discover Central Division','NHL','National Hockey League','Nationwide Arena','Nationwide Arena, Columbus','AHL:Cleveland Monsters',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(4,20210100,0,202101000000,'Dallas Stars','Dallas','Dallas','','TX','USA','United States','Dallas, TX','Texas','Dallas, Texas','Stars','',' Conference','Central','Discover Central Division','NHL','National Hockey League','American Airlines Center','American Airlines Center, Dallas','AHL:Texas Stars',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(5,20210100,0,202101000000,'Detroit Red Wings','Detroit','Detroit','','MI','USA','United States','Detroit, MI','Michigan','Detroit, Michigan','Red Wings','',' Conference','Central','Discover Central Division','NHL','National Hockey League','Little Caesars Arena','Little Caesars Arena, Detroit','AHL:Grand Rapids Griffins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(6,20210100,0,202101000000,'Florida Panthers','Sunrise','Florida','','FL','USA','United States','Sunrise, FL','Florida','Sunrise, Florida','Panthers','',' Conference','Central','Discover Central Division','NHL','National Hockey League','BB&T Center','BB&T Center, Sunrise','AHL:Syracuse Crunch',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(7,20210100,0,202101000000,'Nashville Predators','Nashville','Nashville','','TN','USA','United States','Nashville, TN','Tennessee','Nashville, Tennessee','Predators','',' Conference','Central','Discover Central Division','NHL','National Hockey League','Bridgestone Arena','Bridgestone Arena, Nashville','AHL:Chicago Wolves',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(8,20210100,0,202101000000,'Tampa Bay Lightning','Tampa Bay','Tampa Bay','','FL','USA','United States','Tampa Bay, FL','Florida','Tampa Bay, Florida','Lightning','',' Conference','Central','Discover Central Division','NHL','National Hockey League','Amalie Arena','Amalie Arena, Tampa Bay','AHL:Syracuse Crunch',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(9,20210100,0,202101000000,'Anaheim Ducks','Anaheim','Anaheim','','CA','USA','United States','Anaheim, CA','California','Anaheim, California','Ducks','',' Conference','West','Honda West Division','NHL','National Hockey League','Honda Center','Honda Center, Anaheim','AHL:San Diego Gulls',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(10,20210100,0,202101000000,'Arizona Coyotes','Glendale','Arizona','','AZ','USA','United States','Glendale, AZ','Arizona','Glendale, Arizona','Coyotes','',' Conference','West','Honda West Division','NHL','National Hockey League','Gila River Arena','Gila River Arena, Glendale','AHL:Tucson Roadrunners',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(11,20210100,0,202101000000,'Colorado Avalanche','Denver','Colorado','','CO','USA','United States','Denver, CO','Colorado','Denver, Colorado','Avalanche','',' Conference','West','Honda West Division','NHL','National Hockey League','Ball Arena','Ball Arena, Denver','AHL:Colorado Eagles',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(12,20210100,0,202101000000,'Los Angeles Kings','Los Angeles','Los Angeles','','CA','USA','United States','Los Angeles, CA','California','Los Angeles, California','Kings','',' Conference','West','Honda West Division','NHL','National Hockey League','Staples Center','Staples Center, Los Angeles','AHL:Ontario Reign',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(13,20210100,0,202101000000,'Minnesota Wild','St. Paul','Minnesota','','MN','USA','United States','St. Paul, MN','Minnesota','St. Paul, Minnesota','Wild','',' Conference','West','Honda West Division','NHL','National Hockey League','Xcel Energy Center','Xcel Energy Center, St. Paul','AHL:Iowa Wild',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(14,20210100,0,202101000000,'St. Louis Blues','St. Louis','St. Louis','','MO','USA','United States','St. Louis, MO','Missouri','St. Louis, Missouri','Blues','',' Conference','West','Honda West Division','NHL','National Hockey League','Enterprise Center','Enterprise Center, St. Louis','AHL:Utica Comets',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(15,20210100,0,202101000000,'San Jose Sharks','San Jose','San Jose','','CA','USA','United States','San Jose, CA','California','San Jose, California','Sharks','',' Conference','West','Honda West Division','NHL','National Hockey League','SAP Center','SAP Center, San Jose','AHL:San Jose Barracuda',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(16,20210100,0,202101000000,'Vegas Golden Knights','Paradise','Vegas','','NV','USA','United States','Paradise, NV','Nevada','Paradise, Nevada','Golden Knights','',' Conference','West','Honda West Division','NHL','National Hockey League','T-Mobile Arena','T-Mobile Arena, Paradise','AHL:Henderson Silver Knights',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(17,20210100,0,202101000000,'Boston Bruins','Boston','Boston','','MA','USA','United States','Boston, MA','Massachusetts','Boston, Massachusetts','Bruins','',' Conference','East','Massmutual East Division','NHL','National Hockey League','TD Garden','TD Garden, Boston','AHL:Providence Bruins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(18,20210100,0,202101000000,'Buffalo Sabres','Buffalo','Buffalo','','NY','USA','United States','Buffalo, NY','New York','Buffalo, New York','Sabres','',' Conference','East','Massmutual East Division','NHL','National Hockey League','KeyBank Center','KeyBank Center, Buffalo','AHL:Rochester Americans',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(19,20210100,0,202101000000,'New Jersey Devils','New Jersey','New Jersey','','NJ','USA','United States','New Jersey, NJ','New Jersey','New Jersey, New Jersey','Devils','',' Conference','East','Massmutual East Division','NHL','National Hockey League','Prudential Center','Prudential Center, New Jersey','AHL:Binghamton Devils',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(20,20210100,0,202101000000,'New York Islanders','Uniondale','New York','','NY','USA','United States','Uniondale, NY','New York','Uniondale, New York','Islanders','',' Conference','East','Massmutual East Division','NHL','National Hockey League','Nassau Coliseum','Nassau Coliseum, Uniondale','AHL:Bridgeport Sound Tigers',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(21,20210100,0,202101000000,'New York Rangers','New York City','New York','','NY','USA','United States','New York City, NY','New York','New York City, New York','Rangers','',' Conference','East','Massmutual East Division','NHL','National Hockey League','Madison Square Garden','Madison Square Garden, New York City','AHL:Hartford Wolf Pack',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(22,20210100,0,202101000000,'Philadelphia Flyers','Philadelphia','Philadelphia','','PA','USA','United States','Philadelphia, PA','Pennsylvania','Philadelphia, Pennsylvania','Flyers','',' Conference','East','Massmutual East Division','NHL','National Hockey League','Wells Fargo Center','Wells Fargo Center, Philadelphia','AHL:Lehigh Valley Phantoms',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(23,20210100,0,202101000000,'Pittsburgh Penguins','Pittsburgh','Pittsburgh','','PA','USA','United States','Pittsburgh, PA','Pennsylvania','Pittsburgh, Pennsylvania','Penguins','',' Conference','East','Massmutual East Division','NHL','National Hockey League','PPG Paints Arena','PPG Paints Arena, Pittsburgh','AHL:Wilkes-Barre/Scranton Penguins',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(24,20210100,0,202101000000,'Washington Capitals','Washington','Washington','','DC','USA','United States','Washington, DC','District of Columbia','Washington, District of Columbia','Capitals','',' Conference','East','Massmutual East Division','NHL','National Hockey League','Capital One Arena','Capital One Arena, Washington','AHL:Hershey Bears',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(25,20210100,0,202101000000,'Calgary Flames','Calgary','Calgary','','AB','CAN','Canada','Calgary, AB','Alberta','Calgary, Alberta','Flames','',' Conference','North','Scotia North Division','NHL','National Hockey League','Scotiabank Saddledome','Scotiabank Saddledome, Calgary','AHL:Stockton Heat',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(26,20210100,0,202101000000,'Edmonton Oilers','Edmonton','Edmonton','','AB','CAN','Canada','Edmonton, AB','Alberta','Edmonton, Alberta','Oilers','',' Conference','North','Scotia North Division','NHL','National Hockey League','Rogers Place','Rogers Place, Edmonton','AHL:Bakersfield Condors',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(27,20210100,0,202101000000,'Montreal Canadiens','Montreal','Montreal','','QC','CAN','Canada','Montreal, QC','Quebec','Montreal, Quebec','Canadiens','',' Conference','North','Scotia North Division','NHL','National Hockey League','Bell Centre','Bell Centre, Montreal','AHL:Laval Rocket',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(28,20210100,0,202101000000,'Ottawa Senators','Ottawa','Ottawa','','ON','CAN','Canada','Ottawa, ON','Ontario','Ottawa, Ontario','Senators','',' Conference','North','Scotia North Division','NHL','National Hockey League','Canadian Tire Centre','Canadian Tire Centre, Ottawa','AHL:Belleville Senators',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(29,20210100,0,202101000000,'Toronto Maple Leafs','Toronto','Toronto','','ON','CAN','Canada','Toronto, ON','Ontario','Toronto, Ontario','Maple Leafs','',' Conference','North','Scotia North Division','NHL','National Hockey League','Scotiabank Arena','Scotiabank Arena, Toronto','AHL:Toronto Marlies',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(30,20210100,0,202101000000,'Vancouver Canucks','Vancouver','Vancouver','','BC','CAN','Canada','Vancouver, BC','British Columbia','Vancouver, British Columbia','Canucks','',' Conference','North','Scotia North Division','NHL','National Hockey League','Rogers Arena','Rogers Arena, Vancouver','AHL:Utica Comets',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
INSERT INTO "NHLTeams" VALUES(31,20210100,0,202101000000,'Winnipeg Jets','Winnipeg','Winnipeg','','MB','CAN','Canada','Winnipeg, MB','Manitoba','Winnipeg, Manitoba','Jets','',' Conference','North','Scotia North Division','NHL','National Hockey League','Bell MTS Place','Bell MTS Place, Winnipeg','AHL:Manitoba Moose',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'0:0:0:0','0:0:0:0','0:0',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.0,'0:0:0:0','None');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('HockeyLeagues',2);
INSERT INTO "sqlite_sequence" VALUES('NHLConferences',1);
INSERT INTO "sqlite_sequence" VALUES('NHLDivisions',4);
INSERT INTO "sqlite_sequence" VALUES('NHLTeams',31);
INSERT INTO "sqlite_sequence" VALUES('NHLStats',31);
INSERT INTO "sqlite_sequence" VALUES('NHLArenas',31);
INSERT INTO "sqlite_sequence" VALUES('AHLConferences',1);
INSERT INTO "sqlite_sequence" VALUES('AHLDivisions',5);
INSERT INTO "sqlite_sequence" VALUES('AHLTeams',28);
INSERT INTO "sqlite_sequence" VALUES('AHLStats',28);
INSERT INTO "sqlite_sequence" VALUES('AHLArenas',28);
COMMIT;
