#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2015-2021 Game Maker 2k - https://github.com/GameMaker2k
    Copyright 2015-2021 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: example.py - Last Update: 11/14/2023 Ver. 0.7.2 RC 1 - Author: cooldude2k $
'''

import libhockeydata, os, sys, random;
try:
 reload(sys);
except NameError:
 from importlib import reload;
 reload(sys);
try:
 sys.setdefaultencoding('utf-8');
except AttributeError:
 pass;

defroot = [];
if(os.path.exists("./data/xml") and os.path.isdir("./data/xml")):
 defroot.append("./data/xml");
if(os.path.exists("./data/xmlalt") and os.path.isdir("./data/xmlalt")):
 defroot.append("./data/xmlalt");
if(os.path.exists("./data/json") and os.path.isdir("./data/json")):
 defroot.append("./data/json");
if(os.path.exists("./data/jsonalt") and os.path.isdir("./data/jsonalt")):
 defroot.append("./data/jsonalt");
if(os.path.exists("./data/sql") and os.path.isdir("./data/sql")):
 defroot.append("./data/sql");
if(os.path.exists("./php/data") and os.path.isdir("./php/data")):
 defroot.append("./php/data");
randroot = random.randint(0, len(defroot)-1);
rootdir = defroot[randroot];
if(len(sys.argv)<2):
 rootdir = defroot[randroot];
else:
 rootdir = sys.argv[1];
extensions = libhockeydata.extensionswd;
extensionsc = libhockeydata.outextlistwd;

if(os.path.isdir(rootdir)):
 for subdir, dirs, files in os.walk(rootdir):
  print("");
  print("--------------------------------------------------------------------------");
  print("");
  for file in files:
   fileinfo = os.path.splitext(file);
   ext = fileinfo[1].lower();
   subfileinfo = None;
   subext = None;
   if ext in extensionsc:
    subfileinfo = os.path.splitext(fileinfo[0]);
    subext = subfileinfo[1].lower();
   else:
    subfileinfo = None;
    subext = None;
   if ext in extensions or subext in extensions:
    filepath = os.path.join(subdir, file);
    if((ext==".xml" or subext==".xml") and libhockeydata.CheckXMLFile(filepath) and libhockeydata.CheckHockeyXML(filepath)):
     sqlitedatatype = False;
     funcarray = { 'informat': "xml", 'inxmlfile': filepath }
    elif((ext==".xml" or subext==".xml") and libhockeydata.CheckXMLFile(filepath) and libhockeydata.CheckHockeySQLiteXML(filepath)):
     sqlitedatatype = True;
     funcarray = { 'informat': "xml", 'inxmlfile': filepath }
    elif(ext==".db3" and libhockeydata.CheckSQLiteDatabase(filepath)):
     sqlitedatatype = False;
     funcarray = { 'informat': "database", 'insdbfile': filepath }
    elif(ext==".sql" or subext==".sql"):
     sqlitedatatype = False;
     funcarray = { 'informat': "sql", 'insqlfile': filepath }
    elif(ext==".json" or subext==".json"):
     sqlitedatatype = False;
     funcarray = { 'informat': "json", 'injsonfile': filepath }
    else:
     sys.exit(1);
    if(sqlitedatatype):
     hockeyarray = libhockeydata.MakeHockeySQLiteArrayFromHockeySQLiteData(funcarray);
    else:
     hockeyarray = libhockeydata.MakeHockeyArrayFromHockeyData(funcarray);
    if(libhockeydata.CheckHockeySQLiteArray(hockeyarray)):
     hockeyarray = libhockeydata.MakeHockeyArrayFromHockeySQLiteArray(hockeyarray);
    if(not libhockeydata.CheckHockeyArray(hockeyarray)):
     sys.exit(1);
    print("File: "+filepath);
    print("");
    print("--------------------------------------------------------------------------");
    print("");
    for hlkey in hockeyarray['leaguelist']:
     for hckey in hockeyarray[hlkey]['conferencelist']:
      for hdkey in hockeyarray[hlkey][hckey]['divisionlist']:
       for htkey in hockeyarray[hlkey][hckey][hdkey]['teamlist']:
        if(len(hckey)==0 and len(hdkey)==0):
         print(hockeyarray[hlkey]['leagueinfo']['fullname']+" / "+hockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullname']);
        if(len(hckey)==0 and len(hdkey)>0):
         print(hockeyarray[hlkey]['leagueinfo']['fullname']+" / "+hockeyarray[hlkey][hckey][hdkey]['divisioninfo']['fullname']+" / "+hockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullname']);
        if(len(hckey)>0 and len(hdkey)==0):
         print(hockeyarray[hlkey]['leagueinfo']['fullname']+" / "+hockeyarray[hlkey][hckey]['conferenceinfo']['fullname']+" / "+hockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullname']);
        if(len(hckey)>0 and len(hdkey)>0):
         print(hockeyarray[hlkey]['leagueinfo']['fullname']+" / "+hockeyarray[hlkey][hckey]['conferenceinfo']['fullname']+" / "+hockeyarray[hlkey][hckey][hdkey]['divisioninfo']['fullname']+" / "+hockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullname']);
    print("");
    print("--------------------------------------------------------------------------");
    print("");
elif(os.path.isfile(rootdir)):
 fileinfo = os.path.splitext(rootdir);
 ext = fileinfo[1].lower();
 subfileinfo = None;
 subext = None;
 if ext in extensionsc:
  subfileinfo = os.path.splitext(fileinfo[0]);
  subext = subfileinfo[1].lower();
 else:
  subfileinfo = None;
  subext = None;
 if ext in extensions or subext in extensions:
  filepath = rootdir;
 if((ext==".xml" or subext==".xml") and libhockeydata.CheckXMLFile(filepath) and libhockeydata.CheckHockeyXML(filepath)):
  sqlitedatatype = False;
  funcarray = { 'informat': "xml", 'inxmlfile': filepath }
 elif((ext==".xml" or subext==".xml") and libhockeydata.CheckXMLFile(filepath) and libhockeydata.CheckHockeySQLiteXML(filepath)):
  sqlitedatatype = True;
  funcarray = { 'informat': "xml", 'inxmlfile': filepath }
 elif(ext==".db3" and libhockeydata.CheckSQLiteDatabase(filepath)):
  sqlitedatatype = False;
  funcarray = { 'informat': "database", 'insdbfile': filepath }
 elif(ext==".sql" or subext==".sql"):
  sqlitedatatype = False;
  funcarray = { 'informat': "sql", 'insqlfile': filepath }
 elif(ext==".json" or subext==".json"):
  sqlitedatatype = False;
  funcarray = { 'informat': "json", 'injsonfile': filepath }
 else:
  sys.exit(1);
 if(sqlitedatatype):
  hockeyarray = libhockeydata.MakeHockeySQLiteArrayFromHockeySQLiteData(funcarray);
 else:
  hockeyarray = libhockeydata.MakeHockeyArrayFromHockeyData(funcarray);
 if(libhockeydata.CheckHockeySQLiteArray(hockeyarray)):
  hockeyarray = libhockeydata.MakeHockeyArrayFromHockeySQLiteArray(hockeyarray);
 if(not libhockeydata.CheckHockeyArray(hockeyarray)):
  sys.exit(1);
 print("");
 print("--------------------------------------------------------------------------");
 print("");
 print("File: "+filepath);
 print("");
 print("--------------------------------------------------------------------------");
 print("");
 for hlkey in hockeyarray['leaguelist']:
  for hckey in hockeyarray[hlkey]['conferencelist']:
   for hdkey in hockeyarray[hlkey][hckey]['divisionlist']:
    for htkey in hockeyarray[hlkey][hckey][hdkey]['teamlist']:
     if(len(hckey)==0 and len(hdkey)==0):
      print(hockeyarray[hlkey]['leagueinfo']['fullname']+" / "+hockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullname']);
     if(len(hckey)==0 and len(hdkey)>0):
      print(hockeyarray[hlkey]['leagueinfo']['fullname']+" / "+hockeyarray[hlkey][hckey][hdkey]['divisioninfo']['fullname']+" / "+hockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullname']);
     if(len(hckey)>0 and len(hdkey)==0):
      print(hockeyarray[hlkey]['leagueinfo']['fullname']+" / "+hockeyarray[hlkey][hckey]['conferenceinfo']['fullname']+" / "+hockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullname']);
     if(len(hckey)>0 and len(hdkey)>0):
      print(hockeyarray[hlkey]['leagueinfo']['fullname']+" / "+hockeyarray[hlkey][hckey]['conferenceinfo']['fullname']+" / "+hockeyarray[hlkey][hckey][hdkey]['divisioninfo']['fullname']+" / "+hockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullname']);
 print("");
 print("--------------------------------------------------------------------------");
 print("");
else:
 sys.exit(1);
