#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3, sys, os, re;

leaguename = "NHL";
leaguefullname = "National Hockey League";
getstartday = "01";
getforday = "07";
getformonth = "10";
getforyearshort = "17";
getforyear = "20"+getforyearshort;
getendyearshort = "18";
getendyear = "20"+getendyearshort;

def CommitHockeyDatabase(sqldatacon):
 sqldatacon[1].commit();
 return True;

def MakeHockeyDatabase(leaguename, filename="./"+leaguename.lower()+str(getforyearshort)+"-"+str(getendyearshort)+".db3"):
 print("Creating "+leaguename+" Database.");
 sqlcon = sqlite3.connect(filename);
 sqlcur = sqlcon.cursor();
 sqldatacon = (sqlcur, sqlcon);
 sqlcon.execute("PRAGMA encoding = \"UTF-8\";");
 sqlcon.execute("PRAGMA auto_vacuum = 1;");
 sqlcon.execute("PRAGMA foreign_keys = 1;");
 CommitHockeyDatabase(sqldatacon);
 return sqldatacon;

sqldatacon = MakeHockeyDatabase(leaguename, "./"+leaguename.lower()+str(getforyearshort)+"-"+str(getendyearshort)+".db3");

def GetLastTenGames(sqldatacon, leaguename, teamname):
 wins = 0;
 losses = 0;
 otlosses = 0;
 getlastninegames = sqldatacon[0].execute("SELECT NumberPeriods, TeamWin FROM "+leaguename+"Games WHERE (HomeTeam=\""+str(teamname)+"\" OR AwayTeam=\""+str(teamname)+"\") ORDER BY id DESC LIMIT 10").fetchall();
 nmax = len(getlastninegames);
 nmin = 0;
 while(nmin<nmax):
  if(teamname==str(getlastninegames[nmin][1])):
   wins = wins + 1;
  if(teamname!=str(getlastninegames[nmin][1])):
   if(int(getlastninegames[nmin][0])==3):
    losses = losses + 1;
   if(int(getlastninegames[nmin][0])>3):
    otlosses = otlosses + 1;
  nmin = nmin + 1;
 return str(wins)+":"+str(losses)+":"+str(otlosses);

def UpdateTeamData(sqldatacon, leaguename, teamid, dataname, addtodata, addtype):
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0]) + addtodata;
 if(addtype=="-"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0]) - addtodata;
 sqldatacon[0].execute("UPDATE "+leaguename+"Teams SET "+dataname+"="+str(TMPData)+" WHERE id="+str(teamid));
 CommitHockeyDatabase(sqldatacon);
 return int(TMPData);

def UpdateTeamDataString(sqldatacon, leaguename, teamid, dataname, newdata):
 sqldatacon[0].execute("UPDATE "+leaguename+"Teams SET "+dataname+"=\""+str(newdata)+"\" WHERE id="+str(teamid));
 return True;

def GetTeamData(sqldatacon, leaguename, teamid, dataname, datatype):
 if(datatype=="float"):
  TMPData = float(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0]);
 if(datatype=="int"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0]);
 if(datatype=="str"):
  TMPData = str(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0]);
 return TMPData;

def UpdateGameData(sqldatacon, leaguename, gameid, dataname, addtodata, addtype):
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Games WHERE id="+str(gameid)).fetchone()[0]) + addtodata;
 if(addtype=="-"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Games WHERE id="+str(gameid)).fetchone()[0]) - addtodata;
 sqldatacon[0].execute("UPDATE "+leaguename+"Games SET "+dataname+"="+str(TMPData)+" WHERE id="+str(gameid));
 CommitHockeyDatabase(sqldatacon);
 return int(TMPData);

def UpdateGameDataString(sqldatacon, leaguename, gameid, dataname, newdata):
 sqldatacon[0].execute("UPDATE "+leaguename+"Games SET "+dataname+"=\""+str(newdata)+"\" WHERE id="+str(gameid));
 CommitHockeyDatabase(sqldatacon);
 return True;

def GetGameData(sqldatacon, leaguename, gameid, dataname, datatype):
 if(datatype=="float"):
  TMPData = float(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Games WHERE id="+str(gameid)).fetchone()[0]);
 if(datatype=="int"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Games WHERE id="+str(gameid)).fetchone()[0]);
 if(datatype=="str"):
  TMPData = str(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Games WHERE id="+str(gameid)).fetchone()[0]);
 return TMPData;

def UpdateArenaData(sqldatacon, leaguename, arenaid, dataname, addtodata, addtype):
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0]) + addtodata;
 if(addtype=="-"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0]) - addtodata;
 sqldatacon[0].execute("UPDATE "+leaguename+"Arenas SET "+dataname+"="+str(TMPData)+" WHERE id="+str(arenaid));
 CommitHockeyDatabase(sqldatacon);
 return int(TMPData);

def UpdateArenaDataString(sqldatacon, leaguename, arenaid, dataname, newdata):
 sqldatacon[0].execute("UPDATE "+leaguename+"Arenas SET "+dataname+"=\""+str(newdata)+"\" WHERE id="+str(arenaid));
 CommitHockeyDatabase(sqldatacon);
 return True;

def GetArenaData(sqldatacon, leaguename, arenaid, dataname, datatype):
 if(datatype=="float"):
  TMPData = float(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0]);
 if(datatype=="int"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0]);
 if(datatype=="str"):
  TMPData = str(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0]);
 return TMPData;

def UpdateConferenceData(sqldatacon, leaguename, conference, dataname, addtodata, addtype):
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Conferences WHERE Conference=\""+str(conference)+"\"").fetchone()[0]) + addtodata;
 if(addtype=="-"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Conferences WHERE Conference=\""+str(conference)+"\"").fetchone()[0]) - addtodata;
 sqldatacon[0].execute("UPDATE "+leaguename+"Conferences SET "+dataname+"="+str(TMPData)+" WHERE Conference=\""+str(conference)+"\"");
 CommitHockeyDatabase(sqldatacon);
 return int(TMPData);

def UpdateDivisionData(sqldatacon, leaguename, division, dataname, addtodata, addtype):
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Divisions WHERE Division=\""+str(division)+"\"").fetchone()[0]) + addtodata;
 if(addtype=="-"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Divisions WHERE Division=\""+str(division)+"\"").fetchone()[0]) - addtodata;
 sqldatacon[0].execute("UPDATE "+leaguename+"Divisions SET "+dataname+"="+str(TMPData)+" WHERE Division=\""+str(division)+"\"");
 CommitHockeyDatabase(sqldatacon);
 return int(TMPData);

def UpdateLeagueData(sqldatacon, leaguename, dataname, addtodata, addtype):
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM Leagues WHERE LeagueName=\""+str(leaguename)+"\"").fetchone()[0]) + addtodata;
 if(addtype=="-"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM Leagues WHERE LeagueName=\""+str(leaguename)+"\"").fetchone()[0]) - addtodata;
 sqldatacon[0].execute("UPDATE Leagues SET "+dataname+"="+str(TMPData)+" WHERE LeagueName=\""+str(leaguename)+"\"");
 CommitHockeyDatabase(sqldatacon);
 return int(TMPData);

def GetLeagueName(sqldatacon, leaguename):
 TMPData = str(sqldatacon[0].execute("SELECT LeagueFullName FROM Leagues WHERE LeagueName=\""+str(leaguename)+"\"").fetchone()[0]);
 return TMPData;

def MakeHockeyLeagueTable(sqldatacon, leaguename):
 print("Creating "+leaguename+" League Table.");
 print("Inserting "+leaguename+" League Data.");
 sqldatacon[1].execute("DROP TABLE IF EXISTS Leagues");
 sqldatacon[0].execute("CREATE TABLE Leagues(id INTEGER PRIMARY KEY, LeagueName TEXT, LeagueFullName TEXT, NumberOfTeams INTEGER, NumberOfConferences INTEGER, NumberOfDivisions INTEGER)");
 CommitHockeyDatabase(sqldatacon);
 return True;

def MakeHockeyLeagues(sqldatacon, leaguename, leaguefullname):
 print("League Name: "+leaguename);
 print(" ");
 sqldatacon[0].execute("INSERT INTO Leagues(LeagueName, LeagueFullName, NumberOfTeams, NumberOfConferences, NumberOfDivisions) VALUES(\""+str(leaguename)+"\", \""+str(leaguefullname)+"\", 0, 0, 0)");
 CommitHockeyDatabase(sqldatacon);
 return True;

MakeHockeyLeagueTable(sqldatacon, leaguename);
MakeHockeyLeagues(sqldatacon, leaguename, leaguefullname);

def MakeHockeyConferenceTable(sqldatacon, leaguename):
 print("Creating "+leaguename+" Conference Table.");
 print("Inserting "+leaguename+" Conference Data.");
 sqldatacon[1].execute("DROP TABLE IF EXISTS "+leaguename+"Conferences");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Conferences(id INTEGER PRIMARY KEY, Conference TEXT, LeagueName TEXT, LeagueFullName TEXT, NumberOfTeams INTEGER, NumberOfDivisions INTEGER)");
 CommitHockeyDatabase(sqldatacon);
 return True;

def MakeHockeyConferences(sqldatacon, leaguename, conference):
 print("Conference Name: "+conference);
 print(" ");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Conferences(Conference, LeagueName, LeagueFullName, NumberOfTeams, NumberOfDivisions) VALUES(\""+str(conference)+"\", \""+leaguename+"\", \""+GetLeagueName(sqldatacon, leaguename)+"\", 0, 0)");
 CommitHockeyDatabase(sqldatacon);
 UpdateLeagueData(sqldatacon, leaguename, "NumberOfConferences", 1, "+");
 return True;

MakeHockeyConferenceTable(sqldatacon, leaguename);
MakeHockeyConferences(sqldatacon, leaguename, "Eastern");
MakeHockeyConferences(sqldatacon, leaguename, "Western");

def MakeHockeyDivisionTable(sqldatacon, leaguename):
 print("Creating "+leaguename+" Division Table.");
 print("Inserting "+leaguename+" Division Data.");
 sqldatacon[1].execute("DROP TABLE IF EXISTS "+leaguename+"Divisions");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Divisions(id INTEGER PRIMARY KEY, Division TEXT, Conference TEXT, LeagueName TEXT, LeagueFullName TEXT, NumberOfTeams INTEGER)");
 CommitHockeyDatabase(sqldatacon);
 return True;

def MakeHockeyDivisions(sqldatacon, leaguename, division, conference):
 print("Conference Name: "+conference);
 print("Division Name: "+division);
 print(" ");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Divisions(Division, Conference, LeagueName, LeagueFullName, NumberOfTeams) VALUES(\""+str(division)+"\", \""+str(conference)+"\", \""+leaguename+"\", \""+GetLeagueName(sqldatacon, leaguename)+"\", 0)");
 CommitHockeyDatabase(sqldatacon);
 UpdateConferenceData(sqldatacon, leaguename, conference, "NumberOfDivisions", 1, "+");
 UpdateLeagueData(sqldatacon, leaguename, "NumberOfDivisions", 1, "+");
 return True;

MakeHockeyDivisionTable(sqldatacon, leaguename);
MakeHockeyDivisions(sqldatacon, leaguename, "Atlantic", "Eastern");
MakeHockeyDivisions(sqldatacon, leaguename, "Metropolitan", "Eastern");
MakeHockeyDivisions(sqldatacon, leaguename, "Central", "Western");
MakeHockeyDivisions(sqldatacon, leaguename, "Pacific", "Western");

def MakeHockeyTeamTable(sqldatacon, leaguename):
 print("Creating "+leaguename+" Team Table.");
 print("Inserting "+leaguename+" Team Data.");
 sqldatacon[1].execute("DROP TABLE IF EXISTS "+leaguename+"Arenas");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Arenas(id INTEGER PRIMARY KEY, CityName TEXT, AreaName TEXT, FullCityName TEXT, ArenaName TEXT, FullArenaName TEXT, GamesPlayed INTEGER)");
 sqldatacon[1].execute("DROP TABLE IF EXISTS "+leaguename+"Teams");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Teams(id INTEGER PRIMARY KEY, Date INTEGER, FullName TEXT, CityName TEXT, TeamPrefix TEXT, AreaName TEXT, FullCityName TEXT, TeamName TEXT, Conference TEXT, Division TEXT, LeagueName TEXT, LeagueFullName TEXT, ArenaName TEXT, FullArenaName TEXT, GamesPlayed INTEGER, GamesPlayedHome INTEGER, GamesPlayedAway INTEGER, Wins INTEGER, OTWins INTEGER, SOWins INTEGER, OTSOWins INTEGER, TWins INTEGER, Losses INTEGER, OTLosses INTEGER, SOLosses INTEGER, OTSOLosses INTEGER, TLosses INTEGER, ROW INTEGER, ROT INTEGER, ShutoutWins INTEGER, ShutoutLosses INTEGER, HomeRecord TEXT, AwayRecord TEXT, Shootouts TEXT, GoalsFor INTEGER, GoalsAgainst INTEGER, GoalsDifference INTEGER, SOGFor INTEGER, SOGAgainst INTEGER, SOGDifference INTEGER, ShotsBlockedFor INTEGER, ShotsBlockedAgainst INTEGER, ShotsBlockedDifference INTEGER, PPGFor INTEGER, PPGAgainst INTEGER, PPGDifference INTEGER, PIMFor INTEGER, PIMAgainst INTEGER, PIMDifference INTEGER, HITSFor INTEGER, HITSAgainst INTEGER, HITSDifference INTEGER, TakeAways INTEGER, GiveAways INTEGER, TAGADifference INTEGER, FaceoffWins INTEGER, FaceoffLosses INTEGER, FaceoffDifference INTEGER, Points INTEGER, PCT REAL, LastTen TEXT, Streak TEXT)");
 sqldatacon[1].execute("DROP TABLE IF EXISTS "+leaguename+"Stats");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Stats(id INTEGER PRIMARY KEY, TeamID  INTEGER, Date INTEGER, FullName TEXT, CityName TEXT, TeamPrefix TEXT, AreaName TEXT, FullCityName TEXT, TeamName TEXT, Conference TEXT, Division TEXT, LeagueName TEXT, LeagueFullName TEXT, ArenaName TEXT, FullArenaName TEXT, GamesPlayed INTEGER, GamesPlayedHome INTEGER, GamesPlayedAway INTEGER, Wins INTEGER, OTWins INTEGER, SOWins INTEGER, OTSOWins INTEGER, TWins INTEGER, Losses INTEGER, OTLosses INTEGER, SOLosses INTEGER, OTSOLosses INTEGER, TLosses INTEGER, ROW INTEGER, ROT INTEGER, ShutoutWins INTEGER, ShutoutLosses INTEGER, HomeRecord TEXT, AwayRecord TEXT, Shootouts TEXT, GoalsFor INTEGER, GoalsAgainst INTEGER, GoalsDifference INTEGER, SOGFor INTEGER, SOGAgainst INTEGER, SOGDifference INTEGER, ShotsBlockedFor INTEGER, ShotsBlockedAgainst INTEGER, ShotsBlockedDifference INTEGER, PPGFor INTEGER, PPGAgainst INTEGER, PPGDifference INTEGER, PIMFor INTEGER, PIMAgainst INTEGER, PIMDifference INTEGER, HITSFor INTEGER, HITSAgainst INTEGER, HITSDifference INTEGER, TakeAways INTEGER, GiveAways INTEGER, TAGADifference INTEGER, FaceoffWins INTEGER, FaceoffLosses INTEGER, FaceoffDifference INTEGER, Points INTEGER, PCT REAL, LastTen TEXT, Streak TEXT)");
 CommitHockeyDatabase(sqldatacon);
 return True;

def MakeHockeyTeams(sqldatacon, leaguename, date, cityname, areaname, teamname, conference, division, arenaname, teamnameprefix):
 print("Team Name: "+teamname);
 print("Arena Name: "+arenaname);
 print("City Name: "+cityname);
 print("Full City Name: "+cityname+", "+areaname);
 print("Full Name: "+teamnameprefix+" "+teamname);
 print("Conference: "+conference);
 print("Division: "+division);
 print(" ");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Teams(Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) VALUES(\""+str(date)+"\", \""+str(teamnameprefix+" "+teamname)+"\", \""+str(cityname)+"\", \""+str(teamnameprefix)+"\", \""+str(areaname)+"\", \""+str(cityname+", "+areaname)+"\", \""+str(teamname)+"\", \""+str(conference)+"\", \""+str(division)+"\", \""+leaguename+"\", \""+GetLeagueName(sqldatacon, leaguename)+"\", \""+str(arenaname)+"\", \""+str(arenaname+", "+cityname)+"\", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \"0:0:0\", \"0:0:0\", \"0:0\", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \"0:0:0\", \"None\")");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Stats (TeamID, Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) SELECT id, Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PPGFor, PPGAgainst, PPGDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE FullName=\""+teamnameprefix+" "+teamname+"\";");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Arenas(CityName, AreaName, FullCityName, ArenaName, FullArenaName, GamesPlayed) VALUES(\""+str(cityname)+"\", \""+str(areaname)+"\", \""+str(cityname+", "+areaname)+"\", \""+str(arenaname)+"\", \""+str(arenaname+", "+cityname)+"\", 0)");
 CommitHockeyDatabase(sqldatacon);
 UpdateConferenceData(sqldatacon, leaguename, conference, "NumberOfTeams", 1, "+");
 UpdateDivisionData(sqldatacon, leaguename, division, "NumberOfTeams", 1, "+");
 UpdateLeagueData(sqldatacon, leaguename, "NumberOfTeams", 1, "+");
 return True;

def MakeHockeyArena(sqldatacon, leaguename, cityname, areaname, arenaname):
 print("Arena Name: "+arenaname);
 print("City Name: "+cityname);
 print("Full City Name: "+cityname+", "+areaname);
 print(" ");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Arenas(CityName, AreaName, FullCityName, ArenaName, FullArenaName, GamesPlayed) VALUES(\""+str(cityname)+"\", \""+str(areaname)+"\", \""+str(cityname+", "+areaname)+"\", \""+str(arenaname)+"\", \""+str(arenaname+", "+cityname)+"\", 0)");
 CommitHockeyDatabase(sqldatacon);
 return True;

MakeHockeyTeamTable(sqldatacon, leaguename);
print("Inserting "+leaguename+" Teams From Eastern Conference.");
print("Inserting "+leaguename+" Teams From Atlantic Division.\n");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Boston", "MA", "Bruins", "Eastern", "Atlantic", "TD Garden", "Boston");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Buffalo", "NY", "Sabres", "Eastern", "Atlantic", "KeyBank Center", "Buffalo");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Detroit", "MI", "Red Wings", "Eastern", "Atlantic", "Little Caesars Arena", "Detroit");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Sunrise", "FL", "Panthers", "Eastern", "Atlantic", "BB&T Center", "Florida");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Montreal", "QC", "Canadiens", "Eastern", "Atlantic", "Bell Centre", "Montreal");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Ottawa", "ON", "Senators", "Eastern", "Atlantic", "Canadian Tire Centre", "Ottawa");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Tampa Bay", "FL", "Lightning", "Eastern", "Atlantic", "Amalie Arena", "Tampa Bay");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Toronto", "ON", "Maple Leafs", "Eastern", "Atlantic", "Air Canada Centre", "Toronto");

print("Inserting "+leaguename+" Teams From Metropolitan Division.\n");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Carolina", "NC", "Hurricanes", "Eastern", "Metropolitan", "PNC Arena", "Carolina");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Columbus", "OH", "Blue Jackets", "Eastern", "Metropolitan", "Nationwide Arena", "Columbus");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "New Jersey", "NJ", "Devils", "Eastern", "Metropolitan", "Prudential Center", "New Jersey");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "New York City", "NY", "Islanders", "Eastern", "Metropolitan", "Barclays Center", "New York");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "New York City", "NY", "Rangers", "Eastern", "Metropolitan", "Madison Square Garden", "New York");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Philadelphia", "PA", "Flyers", "Eastern", "Metropolitan", "Wells Fargo Center", "Philadelphia");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Pittsburgh", "PA", "Penguins", "Eastern", "Metropolitan", "PPG Paints Arena", "Pittsburgh");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Washington", "D.C.", "Capitals", "Eastern", "Metropolitan", "Capital One Arena", "Washington");

print("Inserting "+leaguename+" Teams From Western Conference.");
print("Inserting "+leaguename+" Teams From Central Division.\n");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Chicago", "IL", "Blackhawks", "Western", "Central", "United Center", "Chicago");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Denver", "CO", "Avalanche", "Western", "Central", "Pepsi Center", "Colorado");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Dallas", "TX", "Stars", "Western", "Central", "American Airlines Center", "Dallas");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "St. Paul", "MN", "Wild", "Western", "Central", "Xcel Energy Center", "Minnesota");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Nashville", "TN", "Predators", "Western", "Central", "Bridgestone Arena", "Nashville");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "St. Louis", "MO", "Blues", "Western", "Central", "Scottrade Center", "St. Louis");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Winnipeg", "MB", "Jets", "Western", "Central", "Bell MTS Place", "Winnipeg");

print("Inserting "+leaguename+" Teams From Pacific Division.\n");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Anaheim", "CA", "Ducks", "Western", "Pacific", "Honda Center", "Anaheim");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Glendale", "AZ", "Coyotes", "Western", "Pacific", "Gila River Arena", "Arizona");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Calgary", "AB", "Flames", "Western", "Pacific", "Scotiabank Saddledome", "Calgary");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Edmonton", "AB", "Oilers", "Western", "Pacific", "Rogers Place", "Edmonton");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Los Angeles", "CA", "Kings", "Western", "Pacific", "Staples Center", "Los Angeles");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "San Jose", "CA", "Sharks", "Western", "Pacific", "SAP Center", "San Jose");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Vancouver", "BC", "Canucks", "Western", "Pacific", "Rogers Arena", "Vancouver");
MakeHockeyTeams(sqldatacon, leaguename, str(getforyear+getformonth+getstartday), "Paradise", "NV", "Golden Knights", "Western", "Pacific", "T-Mobile Arena", "Vegas");

MakeHockeyArena(sqldatacon, leaguename, "Queens", "NY", "Citi Field");
MakeHockeyArena(sqldatacon, leaguename, "Annapolis", "MD", "Navy-Marine Corps Memorial Stadium");

def GetNum2Team(sqldatacon, leaguename, TeamNum, ReturnVar):
 return str(sqldatacon[0].execute("SELECT "+ReturnVar+" FROM "+leaguename+"Teams WHERE id="+str(TeamNum)).fetchone()[0]);

def GetTeam2Num(sqldatacon, leaguename, TeamName):
 return int(sqldatacon[0].execute("SELECT id FROM "+leaguename+"Teams WHERE FullName=\""+str(TeamName)+"\"").fetchone()[0]);

def GetNum2Arena(sqldatacon, leaguename, ArenaNum, ReturnVar):
 return str(sqldatacon[0].execute("SELECT "+ReturnVar+" FROM "+leaguename+"Arenas WHERE id="+str(ArenaNum)).fetchone()[0]);

def GetArena2Num(sqldatacon, leaguename, ArenaName):
 return int(sqldatacon[0].execute("SELECT id FROM "+leaguename+"Arenas WHERE FullArenaName=\""+str(ArenaName)+"\"").fetchone()[0]);

print("DONE! All Team Data Inserted.");

def MakeHockeyGameTable(sqldatacon, leaguename):
 print("Creating "+leaguename+" Game Table.");
 sqldatacon[1].execute("DROP TABLE IF EXISTS "+leaguename+"Games");
 sqldatacon[0].execute("CREATE TABLE "+leaguename+"Games(id INTEGER PRIMARY KEY, Date INTEGER, HomeTeam TEXT, AwayTeam TEXT, AtArena TEXT, TeamScorePeriods TEXT, TeamFullScore TEXT, ShotsOnGoal TEXT, FullShotsOnGoal TEXT, ShotsBlocked TEXT, FullShotsBlocked TEXT, PowerPlays TEXT, FullPowerPlays TEXT, PenaltyMinutes TEXT, FullPenaltyMinutes TEXT, HitsPerPeriod TEXT, FullHitsPerPeriod TEXT, TakeAways TEXT, FullTakeAways TEXT, FaceoffWins TEXT, FullFaceoffWins TEXT, NumberPeriods INTEGER, TeamWin TEXT, TeamLost TEXT, IsPlayOffGame INTEGER)");
 CommitHockeyDatabase(sqldatacon);
 return True;

def MakeHockeyGame(sqldatacon, leaguename, date, hometeam, awayteam, periodsscore, shotsongoal, ppgoals, periodpims, periodhits, takeaways, faceoffwins, atarena, isplayoffgame):
 isplayoffgsql = "0";
 if(isplayoffgame==True):
  isplayoffgsql = "1";
 if(isplayoffgame==False):
  isplayoffsql = "0";
 periodssplit = periodsscore.split(",");
 periodcounting = 0;
 numberofperiods=int(len(periodssplit));
 homescore = 0;
 awayscore = 0;
 homeperiodscore = "";
 awayperiodscore = "";
 while(periodcounting<numberofperiods):
  periodscoresplit = periodssplit[periodcounting].split(":");
  homeperiodscore = homeperiodscore+" "+str(periodscoresplit[0]);
  awayperiodscore = awayperiodscore+" "+str(periodscoresplit[1]);
  if(periodcounting <= 3):
   homescore = homescore + int(periodscoresplit[0]);
   awayscore = awayscore + int(periodscoresplit[1]);
  if(isplayoffgame==True and periodcounting > 3):
   homescore = homescore + int(periodscoresplit[0]);
   awayscore = awayscore + int(periodscoresplit[1]);
  if(isplayoffgame==False and periodcounting > 3):
   if(periodscoresplit[0] > periodscoresplit[1]):
    homescore = homescore + 1;
   if(periodscoresplit[0] < periodscoresplit[1]):
    awayscore = awayscore + 1;
  periodcounting = periodcounting + 1;
 totalscore = str(homescore)+":"+str(awayscore);
 teamscores=totalscore.split(":");
 shotsongoalsplit = shotsongoal.split(",");
 periodssplits = periodsscore.split(",");
 ppgoalssplits = ppgoals.split(",");
 periodpimssplits = periodpims.split(",");
 periodhitssplits = periodhits.split(",");
 takeawayssplits = takeaways.split(",");
 faceoffwinssplits = faceoffwins.split(",");
 numberofsogperiods=int(len(shotsongoalsplit));
 periodsogcounting = 0;
 homesog = 0;
 awaysog = 0;
 hometsb = 0;
 awaytsb = 0;
 homeppg = 0;
 awayppg = 0;
 homepims = 0;
 awaypims = 0;
 homehits = 0;
 awayhits = 0;
 hometaws = 0;
 awaytaws = 0;
 homefows = 0;
 awayfows = 0;
 sbstr = "";
 homeperiodsog = "";
 awayperiodsog = "";
 while(periodsogcounting<numberofsogperiods):
  periodsogsplit = shotsongoalsplit[periodsogcounting].split(":");
  periodscoresplit = periodssplits[periodsogcounting].split(":");
  periodppgsplit = ppgoalssplits[periodsogcounting].split(":");
  periodpimsplit = periodpimssplits[periodsogcounting].split(":");
  periodhitsplit = periodhitssplits[periodsogcounting].split(":");
  periodtawsplit = takeawayssplits[periodsogcounting].split(":");
  periodfowsplit = faceoffwinssplits[periodsogcounting].split(":");
  homesog = homesog + int(periodsogsplit[0]);
  homesb = int(periodsogsplit[0]) - int(periodscoresplit[0]);
  hometsb = homesb + hometsb;
  homeppg = homeppg + int(periodppgsplit[0]);
  homepims = homepims + int(periodpimsplit[0]);
  homehits = homehits + int(periodhitsplit[0]);
  hometaws = hometaws + int(periodtawsplit[0]);
  homefows = homefows + int(periodfowsplit[0]);
  awaysog = awaysog + int(periodsogsplit[1]);
  awaysb = int(periodsogsplit[1]) - int(periodscoresplit[1]);
  awaytsb = awaysb + awaytsb;
  awayppg = awayppg + int(periodppgsplit[1]);
  awaypims = awaypims + int(periodpimsplit[1]);
  awayhits = awayhits + int(periodhitsplit[1]);
  awaytaws = awaytaws + int(periodtawsplit[1]);
  awayfows = awayfows + int(periodfowsplit[1]);
  sbstr = sbstr+str(homesb)+":"+str(awaysb)+" ";
  periodsogcounting = periodsogcounting + 1;
 sbstr = sbstr.rstrip();
 sbstr = sbstr.replace(" ", ",");
 tsbstr = str(hometsb)+":"+str(awaytsb);
 totalsog = str(homesog)+":"+str(awaysog);
 totalppg = str(homeppg)+":"+str(awayppg);
 totalpims = str(homepims)+":"+str(awaypims);
 totalhits = str(homehits)+":"+str(awayhits);
 totaltaws = str(hometaws)+":"+str(awaytaws);
 totalfows = str(homefows)+":"+str(awayfows);
 teamssog=totalsog.split(":");
 hometeamname = hometeam;
 hometeam = GetTeam2Num(sqldatacon, leaguename, hometeam);
 awayteamname = awayteam;
 awayteam = GetTeam2Num(sqldatacon, leaguename, awayteam);
 if(atarena==0):
  atarena = hometeam;
  atarenaname = GetTeamData(sqldatacon, leaguename, hometeam, "FullArenaName", "str");
 if(isinstance(atarena, int) and atarena>0):
  atarenaname = GetNum2Arena(sqldatacon, leaguename, atarena, "FullArenaName");
 if(isinstance(atarena, str)):
  atarenaname = atarena;
  atarena = GetArena2Num(sqldatacon, leaguename, atarenaname);
 print("Home Arena: "+str(atarenaname));
 print("Home Team: "+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullName"));
 print("Home Period Scores:"+homeperiodscore);
 print("Home Score: "+str(teamscores[0]));
 print("Away Team: "+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullName"));
 print("Away Period Scores:"+awayperiodscore);
 print("Away Score: "+str(teamscores[1]));
 print("Number Of Periods: "+str(numberofperiods));
 if(teamscores[0] > teamscores[1]):
  print("Winning Team: "+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullName"));
  print("Losing Team: "+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullName"));
  losingteam = awayteam;
  winningteam = hometeam;
  winningteamname = hometeamname;
  losingteamname = awayteamname;
 if(teamscores[0] < teamscores[1]):
  print("Winning Team: "+GetNum2Team(sqldatacon, leaguename, int(awayteam), "FullName"));
  print("Losing Team: "+GetNum2Team(sqldatacon, leaguename, int(hometeam), "FullName"));
  losingteam = hometeam;
  winningteam = awayteam;
  winningteamname = awayteamname;
  losingteamname = hometeamname;
 print(" ");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Games(Date, HomeTeam, AwayTeam, AtArena, TeamScorePeriods, TeamFullScore, ShotsOnGoal, FullShotsOnGoal, ShotsBlocked, FullShotsBlocked, PowerPlays, FullPowerPlays, PenaltyMinutes, FullPenaltyMinutes, HitsPerPeriod, FullHitsPerPeriod, TakeAways, FullTakeAways, FaceoffWins, FullFaceoffWins, NumberPeriods, TeamWin, TeamLost, IsPlayOffGame) VALUES("+str(date)+", \""+str(hometeamname)+"\", \""+str(awayteamname)+"\", \""+str(atarenaname)+"\", \""+str(periodsscore)+"\", \""+str(totalscore)+"\", \""+str(shotsongoal)+"\", \""+str(totalsog)+"\", \""+str(sbstr)+"\", \""+str(tsbstr)+"\", \""+str(ppgoals)+"\", \""+str(totalppg)+"\", \""+str(periodpims)+"\", \""+str(totalpims)+"\", \""+str(periodhits)+"\", \""+str(totalhits)+"\", \""+str(takeaways)+"\", \""+str(totaltaws)+"\", \""+str(faceoffwins)+"\", \""+str(totalfows)+"\", "+str(numberofperiods)+", \""+str(winningteamname)+"\", \""+str(losingteamname)+"\", "+str(isplayoffgsql)+")");
 UpdateArenaData(sqldatacon, leaguename, atarena, "GamesPlayed", 1, "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "Date", int(date), "=");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "GamesPlayed", 1, "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "GamesPlayedHome", 1, "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "GoalsFor", int(teamscores[0]), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "GoalsAgainst", int(teamscores[1]), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "GoalsDifference", int(int(teamscores[0]) - int(teamscores[1])), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "SOGFor", int(teamssog[0]), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "SOGAgainst", int(teamssog[1]), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "SOGDifference", int(int(teamssog[0]) - int(teamssog[1])), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "ShotsBlockedFor", int(hometsb), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "ShotsBlockedAgainst", int(awaytsb), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "ShotsBlockedDifference", int(int(hometsb) - int(awaytsb)), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PPGFor", int(homeppg), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PPGAgainst", int(awayppg), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PPGDifference", int(int(homeppg) - int(awayppg)), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PIMFor", int(homepims), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PIMAgainst", int(awaypims), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PIMDifference", int(int(homepims) - int(awaypims)), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "HITSFor", int(homehits), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "HITSAgainst", int(awayhits), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "HITSDifference", int(int(homehits) - int(awayhits)), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "TakeAways", int(hometaws), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "GiveAways", int(awaytaws), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "TAGADifference", int(int(hometaws) - int(awaytaws)), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "FaceoffWins", int(homefows), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "FaceoffLosses", int(awayfows), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "FaceoffDifference", int(int(homefows) - int(awayfows)), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "Date", int(date), "=");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "GamesPlayed", 1, "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "GamesPlayedAway", 1, "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "GoalsFor", int(teamscores[1]), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "GoalsAgainst", int(teamscores[0]), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "GoalsDifference", int(int(teamscores[1]) - int(teamscores[0])), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "SOGFor", int(teamssog[1]), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "SOGAgainst", int(teamssog[0]), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "SOGDifference", int(int(teamssog[1]) - int(teamssog[0])), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "ShotsBlockedFor", int(awaytsb), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "ShotsBlockedAgainst", int(hometsb), "+");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "ShotsBlockedDifference", int(int(awaytsb) - int(hometsb)), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PPGFor", int(awayppg), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PPGAgainst", int(homeppg), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PPGDifference", int(int(awayppg) - int(homeppg)), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PIMFor", int(awaypims), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PIMAgainst", int(homepims), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PIMDifference", int(int(awaypims) - int(homepims)), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "HITSFor", int(awayhits), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "HITSAgainst", int(homehits), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "HITSDifference", int(int(awayhits) - int(homehits)), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "TakeAways", int(awaytaws), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "GiveAways", int(hometaws), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "TAGADifference", int(int(awaytaws) - int(hometaws)), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "FaceoffWins", int(awayfows), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "FaceoffLosses", int(homefows), "+");
 UpdateTeamData(sqldatacon, leaguename, hometeam, "FaceoffDifference", int(int(awayfows) - int(homefows)), "+");
 if(winningteam==hometeam and int(teamscores[1])==0):
  UpdateTeamData(sqldatacon, leaguename, hometeam, "ShutoutWins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, awayteam, "ShutoutLosses", 1, "+");
 if(winningteam==awayteam and int(teamscores[0])==0):
  UpdateTeamData(sqldatacon, leaguename, awayteam, "ShutoutWins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, hometeam, "ShutoutLosses", 1, "+");
 UpdateTeamDataString(sqldatacon, leaguename, winningteam, "LastTen", GetLastTenGames(sqldatacon, leaguename, winningteamname));
 UpdateTeamDataString(sqldatacon, leaguename, losingteam, "LastTen", GetLastTenGames(sqldatacon, leaguename, losingteamname));
 GetWinningStreak = GetTeamData(sqldatacon, leaguename, winningteam, "Streak", "str");
 GetWinningStreakNext = "Won 1";
 if(GetWinningStreak!="None"):
  GetWinningStreakSplit = re.findall("([a-zA-Z]+) ([0-9]+)", GetWinningStreak);
  if(GetWinningStreakSplit[0][0]=="Won"):
   GetWinningStreakNext = "Won "+str(int(GetWinningStreakSplit[0][1]) + 1);
  if(GetWinningStreakSplit[0][0]=="Lost"):
   GetWinningStreakNext = "Won 1";
  if(GetWinningStreakSplit[0][0]=="OT"):
   GetWinningStreakNext = "Won 1";
 UpdateTeamDataString(sqldatacon, leaguename, winningteam, "Streak", GetWinningStreakNext);
 GetLosingStreak = GetTeamData(sqldatacon, leaguename, losingteam, "Streak", "str");
 if(numberofperiods==3):
  GetLosingStreakNext = "Lost 1";
 if(numberofperiods>3):
  GetLosingStreakNext = "OT 1";
 if(GetLosingStreak!="None"):
  GetLosingStreakSplit = re.findall("([a-zA-Z]+) ([0-9]+)", GetLosingStreak);
  if(GetLosingStreakSplit[0][0]=="Won"):
   if(numberofperiods==3):
    GetLosingStreakNext = "Lost 1";
   if(numberofperiods>3):
    GetLosingStreakNext = "OT 1";
  if(GetLosingStreakSplit[0][0]=="Lost"):
   if(numberofperiods==3):
    GetLosingStreakNext = "Lost "+str(int(GetLosingStreakSplit[0][1]) + 1);
   if(numberofperiods>3):
    GetLosingStreakNext = "OT 1";
  if(GetLosingStreakSplit[0][0]=="OS"):
   if(numberofperiods==3):
    GetLosingStreakNext = "Lost 1";
   if(numberofperiods>3):
    GetLosingStreakNext = "OT "+str(int(GetLosingStreakSplit[0][1]) + 1);
 UpdateTeamDataString(sqldatacon, leaguename, losingteam, "Streak", GetLosingStreakNext);
 if((isplayoffgame==False and numberofperiods<5) or (isplayoffgame==True)):
  UpdateTeamData(sqldatacon, leaguename, winningteam, "ROW", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "ROT", 1, "+");
 if(numberofperiods==3):
  UpdateTeamData(sqldatacon, leaguename, winningteam, "Wins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, winningteam, "TWins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, winningteam, "Points", 2, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "Losses", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "TLosses", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "Points", 0, "+");
  if(winningteam==hometeam):
   HomeTeamRecord = GetTeamData(sqldatacon, leaguename, winningteam, "HomeRecord", "str");
   HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
   NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2]);
   UpdateTeamDataString(sqldatacon, leaguename, winningteam, "HomeRecord", NewHTR);
   AwayTeamRecord = GetTeamData(sqldatacon, leaguename, losingteam, "AwayRecord", "str");
   ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
   NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1] + 1)+":"+str(ATRSpit[2]);
   UpdateTeamDataString(sqldatacon, leaguename, losingteam, "AwayRecord", NewATR);
  if(losingteam==hometeam):
   HomeTeamRecord = GetTeamData(sqldatacon, leaguename, winningteam, "AwayRecord", "str");
   HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
   NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2]);
   UpdateTeamDataString(sqldatacon, leaguename, winningteam, "AwayRecord", NewHTR);
   AwayTeamRecord = GetTeamData(sqldatacon, leaguename, losingteam, "HomeRecord", "str");
   ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
   NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1] + 1)+":"+str(ATRSpit[2]);
   UpdateTeamDataString(sqldatacon, leaguename, losingteam, "HomeRecord", NewATR);
 if(numberofperiods>3):
  if((numberofperiods==4 and isplayoffgame==False) or (numberofperiods>4 and isplayoffgame==True)):
   UpdateTeamData(sqldatacon, leaguename, winningteam, "OTWins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, winningteam, "OTSOWins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, winningteam, "TWins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, winningteam, "Points", 2, "+");
  if((numberofperiods==4 and isplayoffgame==False) or (numberofperiods>4 and isplayoffgame==True)):
   UpdateTeamData(sqldatacon, leaguename, losingteam, "OTLosses", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "OTSOLosses", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "TLosses", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "Points", 1, "+");
  if(winningteam==hometeam):
   HomeTeamRecord = GetTeamData(sqldatacon, leaguename, winningteam, "HomeRecord", "str");
   HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
   NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2]);
   UpdateTeamDataString(sqldatacon, leaguename, winningteam, "HomeRecord", NewHTR);
   AwayTeamRecord = GetTeamData(sqldatacon, leaguename, losingteam, "AwayRecord", "str");
   ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
   NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1])+":"+str(ATRSpit[2] + 1);
   UpdateTeamDataString(sqldatacon, leaguename, losingteam, "AwayRecord", NewATR);
  if(losingteam==hometeam):
   HomeTeamRecord = GetTeamData(sqldatacon, leaguename, winningteam, "AwayRecord", "str");
   HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
   NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2]);
   UpdateTeamDataString(sqldatacon, leaguename, winningteam, "AwayRecord", NewHTR);
   AwayTeamRecord = GetTeamData(sqldatacon, leaguename, losingteam, "HomeRecord", "str");
   ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
   NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1])+":"+str(ATRSpit[2] + 1);
   UpdateTeamDataString(sqldatacon, leaguename, losingteam, "HomeRecord", NewATR);
 if(isplayoffgame==False and numberofperiods>4):
  UpdateTeamData(sqldatacon, leaguename, winningteam, "SOWins", 1, "+");
  UpdateTeamData(sqldatacon, leaguename, losingteam, "SOLosses", 1, "+");
  WinningTeamShootouts = GetTeamData(sqldatacon, leaguename, winningteam, "Shootouts", "str");
  WTSoSplit = [int(n) for n in WinningTeamShootouts.split(":")];
  NewWTSo = str(WTSoSplit[0] + 1)+":"+str(WTSoSplit[1]);
  UpdateTeamDataString(sqldatacon, leaguename, winningteam, "Shootouts", NewWTSo);
  LosingTeamShootouts = GetTeamData(sqldatacon, leaguename, losingteam, "Shootouts", "str");
  LTSoSplit = [int(n) for n in LosingTeamShootouts.split(":")];
  NewLTSo = str(LTSoSplit[0])+":"+str(LTSoSplit[1] + 1);
  UpdateTeamDataString(sqldatacon, leaguename, losingteam, "Shootouts", NewLTSo);
 HomeOTLossesPCT = float("%.2f" % float(float(0.5) * float(GetTeamData(sqldatacon, leaguename, hometeam, "OTSOLosses", "float"))));
 HomeWinsPCT = float("%.3f" % float(float(GetTeamData(sqldatacon, leaguename, hometeam, "TWins", "float") + HomeOTLossesPCT) / float(GetTeamData(sqldatacon, leaguename, hometeam, "GamesPlayed", "float"))));
 AwayOTLossesPCT = float("%.2f" % float(float(0.5) * float(GetTeamData(sqldatacon, leaguename, awayteam, "OTSOLosses", "float"))));
 AwayWinsPCT = float("%.3f" % float(float(GetTeamData(sqldatacon, leaguename, awayteam, "TWins", "float") + AwayOTLossesPCT) / float(GetTeamData(sqldatacon, leaguename, awayteam, "GamesPlayed", "float"))));
 UpdateTeamData(sqldatacon, leaguename, hometeam, "PCT", HomeWinsPCT, "=");
 UpdateTeamData(sqldatacon, leaguename, awayteam, "PCT", AwayWinsPCT, "=");
 CommitHockeyDatabase(sqldatacon);
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Stats (TeamID, Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) SELECT id, Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE FullName=\""+hometeamname+"\";");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Stats (TeamID, Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak) SELECT id, Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, LeagueName, LeagueFullName, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, PPGFor, PPGAgainst, PPGDifference, PIMFor, PIMAgainst, PIMDifference, HITSFor, HITSAgainst, HITSDifference, TakeAways, GiveAways, TAGADifference, FaceoffWins, FaceoffLosses, FaceoffDifference, Points, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE FullName=\""+awayteamname+"\";");
 CommitHockeyDatabase(sqldatacon);
 return True;

MakeHockeyGameTable(sqldatacon, leaguename);

def CloseHockeyDatabase(sqldatacon, leaguename):
 print("Database Check Return: "+str(sqldatacon[0].execute("PRAGMA integrity_check(100);").fetchone()[0])+"\n");
 CommitHockeyDatabase(sqldatacon);
 sqldatacon[0].close();
 print("DONE! All Game Data Inserted.");
 print("DONE! "+leaguename+" Database Created.");
 return True;

CloseHockeyDatabase(sqldatacon, leaguename);
