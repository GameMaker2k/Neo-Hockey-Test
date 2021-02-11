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

    $FileInfo: example.py - Last Update: 1/15/2021 Ver. 0.5.0 RC 1 - Author: cooldude2k $
'''

import libhockeydata, os, sys, random;

defroot = ['./data/xml', './data/json', './data/sql', './php/data'];
randroot = random.randint(0, 3);
rootdir = defroot[randroot];
if(len(sys.argv)<2):
 rootdir = defroot[randroot];
else:
 rootdir = sys.argv[1];
extensions = ['.xml', '.json', '.sql', '.db3'];

if(os.path.isdir(rootdir)):
 for subdir, dirs, files in os.walk(rootdir):
  print("");
  print("--------------------------------------------------------------------------");
  print("");
  for file in files:
   ext = os.path.splitext(file)[-1].lower();
   if(ext==".gz" or ext==".bz2" or ext==".lzma" or ext==".xz"):
    ext = os.path.splitext(ext)[-1].lower();
   if ext in extensions:
    filepath = os.path.join(subdir, file);
    if(ext==".xml" and libhockeydata.CheckXMLFile(filepath) and libhockeydata.CheckHockeyXML(filepath)):
     hockeyarray = libhockeydata.MakeHockeyArrayFromHockeyXML(filepath);
    elif(ext==".xml" and libhockeydata.CheckXMLFile(filepath) and libhockeydata.CheckHockeySQLiteXML(filepath)):
     hockeyarray = libhockeydata.MakeHockeySQLiteArrayFromHockeyXML(filepath);
    elif(ext==".db3" and libhockeydata.CheckSQLiteDatabase(filepath)):
     hockeyarray = libhockeydata.MakeHockeyArrayFromHockeyDatabase(filepath);
    elif(ext==".sql"):
     hockeyarray = libhockeydata.MakeHockeyArrayFromHockeySQL(filepath);
    elif(ext==".json"):
     hockeyarray = libhockeydata.MakeHockeyArrayFromHockeyJSON(filepath);
    else:
     sys.exit(1);
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
 ext = os.path.splitext(rootdir)[-1].lower();
 if ext in extensions:
  filepath = rootdir;
 if(ext==".xml" and libhockeydata.CheckXMLFile(filepath)):
  hockeyarray = libhockeydata.MakeHockeyArrayFromHockeyXML(filepath);
 elif(ext==".db3" and libhockeydata.CheckSQLiteDatabase(filepath)):
   hockeyarray = libhockeydata.MakeHockeyArrayFromHockeyDatabase(filepath);
 elif(ext==".sql"):
   hockeyarray = libhockeydata.MakeHockeyArrayFromHockeySQL(filepath);
 elif(ext==".json"):
   hockeyarray = libhockeydata.MakeHockeyArrayFromHockeyJSON(filepath);
 else:
  sys.exit(1);
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
