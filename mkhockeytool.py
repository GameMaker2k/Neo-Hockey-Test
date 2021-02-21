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

    $FileInfo: mkhockeytool.py - Last Update: 1/15/2021 Ver. 0.5.0 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals;
import libhockeydata, os, sys, readline, argparse, logging;

__project__ = libhockeydata.__project__;
__program_name__ = libhockeydata.__program_name__;
__project_url__ = libhockeydata.__project_url__;
__version_info__ = libhockeydata.__version_info__;
__version_date_info__ = libhockeydata.__version_date_info__;
__version_date__ = libhockeydata.__version_date__;
__version_date_plusrc__ = libhockeydata.__version_date_plusrc__;
__version__ = libhockeydata.__version__;

defxmlfile = "./data/hockeydata.xml";
defsdbfile = "./data/hockeydata.db3";
defoldsdbfile = "./data/hockeydata.db3";
defsqlfile = "./data/hockeydata.sql";
defjsonfile = "./data/hockeydata.json";
extensions = ['.xml', '.json', '.sql', '.db3', '.py'];
extensionsin = ['.xml', '.json', '.sql', '.db3'];
extensionsc = ['.gz', '.bz2', '.lzma', '.xz'];
filetypes = ['xml', 'json', 'sql', 'db3', 'py', 'pyalt'];

def get_user_input(txt):
 try:
  return raw_input(txt);
 except NameError:
  return input(txt);
 return False;

argparser = argparse.ArgumentParser(description="Just a test script dealing with hockey games and stats", conflict_handler="resolve", add_help=True);
argparser.add_argument("-v", "--ver", "--version", action="version", version=__program_name__+" "+__version__);
argparser.add_argument("-i", "-f", "--infile", nargs="?", default=None, help="database file to load");
argparser.add_argument("-e", "-n", "--empty", action="store_true", help="create empty database file");
argparser.add_argument("-o", "-e", "--outfile", nargs="?", default=None, help="database file to save");
argparser.add_argument("-x", "-p", "--export", action="store_true", help="export file to database");
argparser.add_argument("-t", "-y", "--type", nargs="?", default=None, help="type of file to export");
argparser.add_argument("-V", "-d", "--verbose", action="store_true", help="print various debugging information");
argparser.add_argument("-j", "-s", "--jsonverbose", action="store_true", help="print various debugging information in json");
getargs = argparser.parse_args();
verboseon = getargs.verbose;
if('VERBOSE' in os.environ or 'DEBUG' in os.environ):
 verboseon = True;
if(verboseon):
 logging.basicConfig(format="%(message)s", stream=sys.stdout, level=logging.DEBUG);

if(not getargs.empty and getargs.infile is None):
 premenuact = get_user_input("E: Exit Hockey Tool\n1: Empty Hockey Database\n2: Import Hockey Database From File\nWhat do you want to do? ");
 if(premenuact.upper()!="E" and not premenuact.isdigit()):
  print("ERROR: Invalid Command");
  premenuact = "E";
 if(premenuact.upper()!="E" and premenuact.isdigit() and (int(premenuact)>2 or int(premenuact)<1)):
  print("ERROR: Invalid Command");
  premenuact = "E";
 if(premenuact.upper()=="E"):
  sys.exit();
if(getargs.empty and getargs.infile is None):
 premenuact = "1";
if(getargs.infile is not None):
 premenuact = "2";
 if(getargs.empty):
  premenuact = "1";
 if(not getargs.empty):
  premenuact = "2";
if(premenuact=="1"):
 if(getargs.infile is None):
  HockeyDatabaseFN = get_user_input("Enter Hockey Database File Name For Output: ");
 if(getargs.infile is not None):
  HockeyDatabaseFN = getargs.infile;
 hockeyarray = libhockeydata.CreateHockeyArray(HockeyDatabaseFN);
if(premenuact=="2"):
 if(getargs.infile is None):
  HockeyDatabaseFN = get_user_input("Enter Hockey Database File Name For Import: ");
 if(getargs.infile is not None):
  HockeyDatabaseFN = getargs.infile;
 fileinfo = os.path.splitext(HockeyDatabaseFN);
 ext = fileinfo[-1].lower();
 subfileinfo = None;
 subext = None;
 if(ext in extensionsc):
  subfileinfo = os.path.splitext(fileinfo[0]);
  subext = subfileinfo[1].lower();
 else:
  subfileinfo = None;
  subext = None;
 if(ext in extensionsin or subext in extensions):
  verbosein = True;
  if(getargs.export):
   verbosein = False;
  if((ext==".xml" or subext==".xml") and libhockeydata.CheckXMLFile(HockeyDatabaseFN) and libhockeydata.CheckHockeyXML(HockeyDatabaseFN)):
   hockeyarray = libhockeydata.MakeHockeyArrayFromHockeyXML(HockeyDatabaseFN, verbose=verbosein, jsonverbose=getargs.jsonverbose);
  if((ext==".xml" or subext==".xml") and libhockeydata.CheckXMLFile(HockeyDatabaseFN) and libhockeydata.CheckHockeySQLiteXML(HockeyDatabaseFN)):
   hockeyarray = libhockeydata.MakeHockeySQLiteArrayFromHockeyXML(HockeyDatabaseFN, verbose=verbosein, jsonverbose=getargs.jsonverbose);
  elif(ext==".db3" and libhockeydata.CheckSQLiteDatabase(HockeyDatabaseFN)):
   hockeyarray = libhockeydata.MakeHockeyArrayFromHockeyDatabase(HockeyDatabaseFN, verbose=verbosein, jsonverbose=getargs.jsonverbose);
  elif(ext==".sql" or subext==".sql"):
   hockeyarray = libhockeydata.MakeHockeyArrayFromHockeySQL(HockeyDatabaseFN, verbose=verbosein, jsonverbose=getargs.jsonverbose);
  elif(ext==".json" or subext==".json"):
   hockeyarray = libhockeydata.MakeHockeyArrayFromHockeyJSON(HockeyDatabaseFN, verbose=verbosein, jsonverbose=getargs.jsonverbose);
  else:
   print("ERROR: Invalid Command");
  if(libhockeydata.CheckHockeySQLiteArray(hockeyarray)):
   hockeyarray = libhockeydata.MakeHockeyArrayFromHockeySQLiteArray(hockeyarray, verbose=verbosein, jsonverbose=getargs.jsonverbose);
  if(not libhockeydata.CheckHockeyArray(hockeyarray)):
   print("ERROR: Invalid Command");

if(getargs.export):
 if(getargs.type is not None and getargs.type not in filetypes):
  getargs.type = None;
 if(getargs.type is not None and getargs.type.lower()=="xml"):
  if(getargs.outfile is None):
   HockeyDatabaseFN = get_user_input("Enter Hockey Database XML File Name to Export: ");
   getargs.outfile = HockeyDatabaseFN;
 elif(getargs.type is not None and getargs.type.lower()=="json"):
  if(getargs.outfile is None):
   HockeyDatabaseFN = get_user_input("Enter Hockey Database JSON File Name to Export: ");
   getargs.outfile = HockeyDatabaseFN;
 elif(getargs.type is not None and getargs.type.lower()=="py"):
  if(getargs.outfile is None):
   HockeyDatabaseFN = get_user_input("Enter Hockey Database Python File Name to Export: ");
   getargs.outfile = HockeyDatabaseFN;
 elif(getargs.type is not None and getargs.type.lower()=="pyalt"):
  if(getargs.outfile is None):
   HockeyDatabaseFN = get_user_input("Enter Hockey Database Python File Name to Export: ");
   getargs.outfile = HockeyDatabaseFN;
 elif(getargs.type is not None and getargs.type.lower()=="sql"):
  if(getargs.outfile is None):
   HockeyDatabaseFN = get_user_input("Enter Hockey Database SQL File Name to Export: ");
   getargs.outfile = HockeyDatabaseFN;
 elif(getargs.type is not None and getargs.type.lower()=="db3"):
  if(getargs.outfile is None):
   HockeyDatabaseFN = get_user_input("Enter Hockey Database File Name to Export: ");
   getargs.outfile = HockeyDatabaseFN;
 else:
  ext = os.path.splitext(getargs.outfile)[-1].lower();
  if(ext in extensions):
   if(ext==".xml"):
    getargs.type = "xml";
   elif(ext==".db3"):
    getargs.type = "db3";
   elif(ext==".sql"):
    getargs.type = "sql";
   elif(ext==".json"):
    getargs.type = "json";
   elif(ext==".py"):
    getargs.type = "py";
   else:
    getargs.type = "db3";
 if(getargs.type.lower()=="xml"):
  libhockeydata.MakeHockeyXMLFileFromHockeyArray(hockeyarray, getargs.outfile, verbose=verboseon, jsonverbose=getargs.jsonverbose);
 elif(getargs.type.lower()=="json"):
  libhockeydata.MakeHockeyJSONFileFromHockeyArray(hockeyarray, getargs.outfile, verbose=verboseon, jsonverbose=getargs.jsonverbose);
 elif(getargs.type.lower()=="py"):
  libhockeydata.MakeHockeyPythonFileFromHockeyArray(hockeyarray, getargs.outfile, verbose=verboseon, jsonverbose=getargs.jsonverbose);
 elif(getargs.type.lower()=="pyalt"):
  libhockeydata.MakeHockeyPythonAltFileFromHockeyArray(hockeyarray, getargs.outfile, verbose=verboseon, jsonverbose=getargs.jsonverbose);
 elif(getargs.type.lower()=="sql"):
  libhockeydata.MakeHockeySQLFileFromHockeyArray(hockeyarray, getargs.outfile, verbose=verboseon, jsonverbose=getargs.jsonverbose);
 elif(getargs.type.lower()=="db3"):
  libhockeydata.MakeHockeyDatabaseFromHockeyArray(hockeyarray, getargs.outfile, verbose=verboseon, jsonverbose=getargs.jsonverbose);
 else:
  print("ERROR: Invalid Command");
 sys.exit();

if(premenuact=="1"):
 print("Using Empty Database at Location: "+HockeyDatabaseFN);
if(premenuact=="2"):
 print("Using Populated Database at Location: "+HockeyDatabaseFN);
keep_loop = True;
while(keep_loop):
 menuact = get_user_input("E: Exit Hockey Tool\n1: Hockey League Tool\n2: Hockey Conference Tool\n3: Hockey Division Tool\n4: Hockey Team Tool\n5: Hockey Arena Tool\n6: Hockey Game Tool\n7: Hockey Database Tool\nWhat do you want to do? ");
 if(menuact.upper()!="E" and not menuact.isdigit()):
  print("ERROR: Invalid Command");
  menuact = "";
 if(menuact.upper()!="E" and menuact.isdigit() and (int(menuact)>7 or int(menuact)<1)):
  print("ERROR: Invalid Command");
  menuact = "";
 if(menuact=="1"):
  sub_keep_loop = True;
  while(sub_keep_loop):
   submenuact = get_user_input("E: Back to Main Menu\n1: Add Hockey League\n2: Remove Hockey League\n3: Edit Hockey League\nWhat do you want to do? ");
   if(submenuact.upper()!="E" and not submenuact.isdigit()):
    print("ERROR: Invalid Command");
    submenuact = "";
   if(submenuact.upper()!="E" and submenuact.isdigit() and (int(submenuact)>3 or int(submenuact)<1)):
    print("ERROR: Invalid Command");
    submenuact = "";
   if(submenuact=="1"):
    HockeyLeagueSN = get_user_input("Enter Hockey League short name: ");
    if(HockeyLeagueSN in hockeyarray['leaguelist']):
     print("ERROR: Hockey League with that short name exists");
    if(HockeyLeagueSN not in hockeyarray['leaguelist']):
     HockeyLeagueFN = get_user_input("Enter Hockey League full name: ");
     HockeyLeagueCSN = get_user_input("Enter Hockey League country short name: ");
     HockeyLeagueCFN = get_user_input("Enter Hockey League country full name: ");
     HockeyLeagueSD = get_user_input("Enter Hockey League start date: ");
     HockeyLeaguePOF = get_user_input("Enter Hockey League playoff format: ");
     HockeyLeagueOT = get_user_input("Enter Hockey League ordertype: ");
     HockeyLeagueHC = get_user_input("Does Hockey League have conferences: ");
     HockeyLeagueHD = get_user_input("Does Hockey League have divisions: ");
     hockeyarray = libhockeydata.AddHockeyLeagueToArray(hockeyarray, HockeyLeagueSN, HockeyLeagueFN, HockeyLeagueCSN, HockeyLeagueCFN, HockeyLeagueSD, HockeyLeaguePOF, HockeyLeagueOT, HockeyLeagueHC, HockeyLeagueHD);
     if(HockeyLeagueHC=="no"):
      hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, HockeyLeagueSN, "");
     if(HockeyLeagueHD=="no"):
      hockeyarray = libhockeydata.AddHockeyDivisionToArray(hockeyarray, HockeyLeagueSN, "", "");
   if(submenuact=="2" and len(hockeyarray['leaguelist'])<=0):
    print("ERROR: There are no Hockey Leagues to delete");
   if(submenuact=="2" and len(hockeyarray['leaguelist'])>0):
    leaguec = 0;
    print("E: Back to Hockey League Tool");
    while(leaguec<len(hockeyarray['leaguelist'])):
     lshn = hockeyarray['leaguelist'][leaguec];
     print(str(leaguec)+": "+hockeyarray[lshn]['leagueinfo']['fullname']);
     leaguec = leaguec + 1;
    HockeyLeaguePreSN = get_user_input("Enter Hockey League number: ");
    if(HockeyLeaguePreSN.upper()!="E" and not HockeyLeaguePreSN.isdigit()):
     print("ERROR: Invalid Command");
     HockeyLeaguePreSN = "E";
    if(HockeyLeaguePreSN.upper()!="E" and HockeyLeaguePreSN.isdigit() and (int(HockeyLeaguePreSN)>len(hockeyarray['leaguelist']) or int(HockeyLeaguePreSN)<0)):
     print("ERROR: Invalid Command");
     HockeyLeaguePreSN = "E";
    if(HockeyLeaguePreSN.upper()!="E" and int(HockeyLeaguePreSN)<len(hockeyarray['leaguelist']) and int(HockeyLeaguePreSN)>-1):
     HockeyLeagueIntSN = int(HockeyLeaguePreSN);
     HockeyLeagueSN = hockeyarray['leaguelist'][HockeyLeagueIntSN];
     hockeyarray = libhockeydata.RemoveHockeyLeagueFromArray(hockeyarray, HockeyLeagueSN);
   if(submenuact=="3" and len(hockeyarray['leaguelist'])<=0):
    print("ERROR: There are no Hockey Leagues to edit");
   if(submenuact=="3" and len(hockeyarray['leaguelist'])>0):
    leaguec = 0;
    print("E: Back to Hockey League Tool");
    while(leaguec<len(hockeyarray['leaguelist'])):
     lshn = hockeyarray['leaguelist'][leaguec];
     print(str(leaguec)+": "+hockeyarray[lshn]['leagueinfo']['fullname']);
     leaguec = leaguec + 1;
    HockeyLeaguePreSN = get_user_input("Enter Hockey League number: ");
    if(HockeyLeaguePreSN.upper()!="E" and not HockeyLeaguePreSN.isdigit()):
     print("ERROR: Invalid Command");
     HockeyLeaguePreSN = "E";
    if( HockeyLeaguePreSN.upper()!="E" and HockeyLeaguePreSN.isdigit() and (int(HockeyLeaguePreSN)>len(hockeyarray['leaguelist']) or int(HockeyLeaguePreSN)<0)):
     print("ERROR: Invalid Command");
     HockeyLeaguePreSN = "E";
    if(HockeyLeaguePreSN.upper()!="E" and int(HockeyLeaguePreSN)<len(hockeyarray['leaguelist']) and int(HockeyLeaguePreSN)>-1):
     HockeyLeagueIntSN = int(HockeyLeaguePreSN);
     HockeyLeagueOldSN = hockeyarray['leaguelist'][HockeyLeagueIntSN];
     HockeyLeagueSN = get_user_input("Enter Hockey League short name: ");
     if(HockeyLeagueSN in hockeyarray['leaguelist']):
      print("ERROR: Hockey League with that short name exists");
     if(HockeyLeagueSN not in hockeyarray['leaguelist']):
      HockeyLeagueFN = get_user_input("Enter Hockey League full name: ");
      HockeyLeagueCSN = get_user_input("Enter Hockey League country short name: ");
      HockeyLeagueCFN = get_user_input("Enter Hockey League country full name: ");
      HockeyLeagueSD = get_user_input("Enter Hockey League start date: ");
      HockeyLeaguePOF = get_user_input("Enter Hockey League playoff format: ");
      HockeyLeagueOT = get_user_input("Enter Hockey League ordertype: ");
      HockeyLeagueHC = get_user_input("Does Hockey League have conferences: ");
      HockeyLeagueHD = get_user_input("Does Hockey League have divisions: ");
      hockeyarray = libhockeydata.ReplaceHockeyLeagueFromArray(hockeyarray, HockeyLeagueOldSN, HockeyLeagueSN, HockeyLeagueFN, HockeyLeagueCSN, HockeyLeagueCFN, HockeyLeagueSD, HockeyLeaguePOF, HockeyLeagueOT, HockeyLeagueHC, HockeyLeagueHD);
   if(submenuact.upper()=="E"):
    sub_keep_loop = False;
 if(menuact=="2" and len(hockeyarray['leaguelist'])<=0):
  print("ERROR: There are no Hockey Leagues");
 if(menuact=="2" and len(hockeyarray['leaguelist'])>0):
  sub_keep_loop = True;
  while(sub_keep_loop):
   leaguec = 0;
   print("E: Back to Main Menu");
   while(leaguec<len(hockeyarray['leaguelist'])):
    lshn = hockeyarray['leaguelist'][leaguec];
    print(str(leaguec)+": "+hockeyarray[lshn]['leagueinfo']['fullname']);
    leaguec = leaguec + 1;
   HockeyLeaguePreSN = get_user_input("Enter Hockey League number: ");
   if(HockeyLeaguePreSN.upper()!="E" and not HockeyLeaguePreSN.isdigit()):
    print("ERROR: Invalid Command");
    HockeyLeaguePreSN = "E";
   if(HockeyLeaguePreSN.upper()!="E" and HockeyLeaguePreSN.isdigit() and (int(HockeyLeaguePreSN)>len(hockeyarray['leaguelist']) or int(HockeyLeaguePreSN)<0)):
    print("ERROR: Invalid Command");
    HockeyLeaguePreSN = "E";
   if(HockeyLeaguePreSN.upper()!="E" and int(HockeyLeaguePreSN)<len(hockeyarray['leaguelist']) and int(HockeyLeaguePreSN)>-1):
    HockeyLeagueIntSN = int(HockeyLeaguePreSN);
    HockeyLeagueSN = hockeyarray['leaguelist'][HockeyLeagueIntSN];
    if(hockeyarray[HockeyLeagueSN]['leagueinfo']['conferences']=="no"):
     print("ERROR: Hockey League can not have any conferences");
     HockeyLeaguePreSN = "E";
    if(hockeyarray[HockeyLeagueSN]['leagueinfo']['conferences']=="yes"):
     sub_sub_keep_loop = True;
     while(sub_sub_keep_loop):
      subsubmenuact = get_user_input("E: Back to Main Menu\n1: Add Hockey Conference\n2: Remove Hockey Conference\n3: Edit Hockey Conference\nWhat do you want to do? ");
      if(subsubmenuact.upper()!="E" and not subsubmenuact.isdigit()):
       print("ERROR: Invalid Command");
       subsubmenuact = "";
      if(subsubmenuact.upper()!="E" and subsubmenuact.isdigit() and (int(subsubmenuact)>3 or int(subsubmenuact)<1)):
       print("ERROR: Invalid Command");
       subsubmenuact = "";
      if(subsubmenuact.upper()=="1"):
       HockeyConferenceCN = get_user_input("Enter Hockey Conference name: ");
       if(HockeyConferenceCN in hockeyarray[HockeyLeagueSN]['conferencelist']):
        print("ERROR: Hockey Conference with that name exists");
       if(HockeyConferenceCN not in hockeyarray[HockeyLeagueSN]['conferencelist']):
        HockeyConferenceCPFN = get_user_input("Enter Hockey Conference prefix: ");
        HockeyConferenceCSFN = get_user_input("Enter Hockey Conference suffix: ");
        hockeyarray = libhockeydata.AddHockeyConferenceToArray(hockeyarray, HockeyLeagueSN, HockeyConferenceCN, HockeyConferenceCPFN, HockeyConferenceCSFN);
      if(subsubmenuact=="2" and (len(hockeyarray['leaguelist'])<=0 or len(hockeyarray[HockeyLeagueSN]['conferencelist'])<=0)):
       print("ERROR: There are no Hockey Conferences to delete");
      if(subsubmenuact=="2" and len(hockeyarray['leaguelist'])>0 and len(hockeyarray[HockeyLeagueSN]['conferencelist'])>0):
       conferencec = 0;
       print("E: Back to Hockey Conference Tool");
       while(conferencec<len(hockeyarray[HockeyLeagueSN]['conferencelist'])):
        lshn = hockeyarray[HockeyLeagueSN]['conferencelist'][conferencec];
        print(str(conferencec)+": "+hockeyarray[HockeyLeagueSN]['quickinfo']['conferenceinfo'][lshn]['fullname']);
        conferencec = conferencec + 1;
       HockeyConferencePreCN = get_user_input("Enter Hockey Conference number: ");
       if(HockeyConferencePreCN.upper()!="E" and not HockeyConferencePreCN.isdigit()):
        print("ERROR: Invalid Command");
        HockeyConferencePreCN = "E";
       if(HockeyConferencePreCN.upper()!="E" and HockeyConferencePreCN.isdigit() and (int(HockeyConferencePreCN)>6 or int(HockeyConferencePreCN)<0)):
        print("ERROR: Invalid Command");
        HockeyConferencePreCN = "E";
       if(HockeyConferencePreCN.upper()!="E" and int(HockeyConferencePreCN)<len(hockeyarray[HockeyLeagueSN]['conferencelist']) and int(HockeyConferencePreCN)>-1):
        HockeyConferenceIntCN = int(HockeyConferencePreCN);
        HockeyConferenceCN = hockeyarray[HockeyLeagueSN]['conferencelist'][HockeyConferenceIntCN];
        hockeyarray = libhockeydata.RemoveHockeyConferenceFromArray(hockeyarray, HockeyLeagueSN, HockeyConferenceCN);
      if(subsubmenuact=="3" and (len(hockeyarray['leaguelist'])<=0 or len(hockeyarray[HockeyLeagueSN]['conferencelist'])<=0)):
       print("ERROR: There are no Hockey Conferences to edit");
      if(subsubmenuact=="3" and len(hockeyarray['leaguelist'])>0 and len(hockeyarray[HockeyLeagueSN]['conferencelist'])>0):
       conferencec = 0;
       print("E: Back to Hockey Conference Tool");
       while(conferencec<len(hockeyarray[HockeyLeagueSN]['conferencelist'])):
        lshn = hockeyarray[HockeyLeagueSN]['conferencelist'][conferencec];
        print(str(conferencec)+": "+hockeyarray[HockeyLeagueSN]['quickinfo']['conferenceinfo'][lshn]['fullname']);
        conferencec = conferencec + 1;
       HockeyConferencePreCN = get_user_input("Enter Hockey Conference number: ");
       if(HockeyConferencePreCN.upper()!="E" and not HockeyConferencePreCN.isdigit()):
        print("ERROR: Invalid Command");
        HockeyConferencePreCN = "E";
       if(HockeyConferencePreCN.upper()!="E" and HockeyConferencePreCN.isdigit() and (int(HockeyConferencePreCN)>6 or int(HockeyConferencePreCN)<0)):
        print("ERROR: Invalid Command");
        HockeyConferencePreCN = "E";
       if(HockeyConferencePreCN.upper()!="E" and int(HockeyConferencePreCN)<len(hockeyarray[HockeyLeagueSN]['conferencelist']) and int(HockeyConferencePreCN)>-1):
        HockeyConferenceIntCN = int(HockeyConferencePreCN);
        HockeyConferenceOldCN = hockeyarray[HockeyLeagueSN]['conferencelist'][HockeyConferenceIntCN];
        HockeyConferenceCN = get_user_input("Enter Hockey Conference name: ");
        if(HockeyConferenceCN in hockeyarray[HockeyLeagueSN]['conferencelist']):
         print("ERROR: Hockey Conference with that name exists");
        if(HockeyConferenceCN not in hockeyarray[HockeyLeagueSN]['conferencelist']):
         HockeyConferenceCPFN = get_user_input("Enter Hockey Conference prefix: ");
         HockeyConferenceCSFN = get_user_input("Enter Hockey Conference suffix: ");
        hockeyarray = libhockeydata.ReplaceHockeyConferencFromArray(hockeyarray, HockeyLeagueSN, HockeyConferenceOldCN, HockeyConferenceCN, HockeyConferenceCPFN, HockeyConferenceCSFN);
      if(subsubmenuact.upper()=="E"):
       sub_sub_keep_loop = False;
   if(HockeyLeaguePreSN.upper()=="E"):
    sub_keep_loop = False;
 if(menuact=="3" and len(hockeyarray['leaguelist'])<=0):
  print("ERROR: There are no Hockey Leagues");
 if(menuact=="3" and len(hockeyarray['leaguelist'])>0):
  sub_keep_loop = True;
  while(sub_keep_loop):
   leaguec = 0;
   print("E: Back to Main Menu");
   while(leaguec<len(hockeyarray['leaguelist'])):
    lshn = hockeyarray['leaguelist'][leaguec];
    print(str(leaguec)+": "+hockeyarray[lshn]['leagueinfo']['fullname']);
    leaguec = leaguec + 1;
   HockeyLeaguePreSN = get_user_input("Enter Hockey League number: ");
   if(HockeyLeaguePreSN.upper()!="E" and not HockeyLeaguePreSN.isdigit()):
    print("ERROR: Invalid Command");
    HockeyLeaguePreSN = "E";
   if(HockeyLeaguePreSN.upper()!="E" and HockeyLeaguePreSN.isdigit() and (int(HockeyLeaguePreSN)>len(hockeyarray['leaguelist']) or int(HockeyLeaguePreSN)<0)):
    print("ERROR: Invalid Command");
    HockeyLeaguePreSN = "E";
   if(HockeyLeaguePreSN.upper()!="E" and int(HockeyLeaguePreSN)<len(hockeyarray['leaguelist']) and int(HockeyLeaguePreSN)>-1):
    HockeyLeagueIntSN = int(HockeyLeaguePreSN);
    HockeyLeagueSN = hockeyarray['leaguelist'][HockeyLeagueIntSN];
    if(hockeyarray[HockeyLeagueSN]['leagueinfo']['divisions']=="no"):
     print("ERROR: Hockey League can not have any divisions");
     HockeyLeaguePreSN = "E";
    if(hockeyarray[HockeyLeagueSN]['leagueinfo']['divisions']=="yes"):
     if(hockeyarray[HockeyLeagueSN]['leagueinfo']['conferences']=="no"):
      sub_sub_keep_loop = True;
      while(sub_sub_keep_loop):
       submenuact = get_user_input("E: Back to Main Menu\n1: Add Hockey Division\n2: Remove Hockey Division\n3: Edit Hockey Division\nWhat do you want to do? ");
       if(submenuact.upper()!="E" and not submenuact.isdigit()):
        print("ERROR: Invalid Command");
        submenuact = "";
       if(submenuact.upper()!="E" and submenuact.isdigit() and (int(submenuact)>3 or int(submenuact)<1)):
        print("ERROR: Invalid Command");
        submenuact = "";
       if(submenuact.upper()=="1"):
        HockeyDivisionDN = get_user_input("Enter Hockey Division name: ");
        if(HockeyDivisionDN in hockeyarray[HockeyLeagueSN]['']['divisionlist']):
         print("ERROR: Hockey Division with that name exists");
        if(HockeyDivisionDN not in hockeyarray[HockeyLeagueSN]['']['divisionlist']):
         HockeyDivisionDPFN = get_user_input("Enter Hockey Division prefix: ");
         HockeyDivisionDSFN = get_user_input("Enter Hockey Division suffix: ");
        libhockeydata.AddHockeyDivisionToArray(hockeyarray, HockeyLeagueSN, HockeyDivisionDN, "", HockeyDivisionDPFN, HockeyDivisionDSFN);
       if(submenuact.upper()=="2"):
        divisionc = 0;
        print("E: Back to Hockey Division Tool");
        while(divisionc<len(hockeyarray[HockeyLeagueSN]['']['divisionlist'])):
         lshn = hockeyarray[HockeyLeagueSN]['']['divisionlist'][divisionc];
         print(str(divisionc)+": "+hockeyarray[HockeyLeagueSN]['quickinfo']['divisioninfo'][lshn]['fullname']);
         divisionc = divisionc + 1;
        HockeyDivisionPreDN = get_user_input("Enter Hockey Division number: ");
        if(HockeyDivisionPreDN.upper()!="E" and not HockeyDivisionPreDN.isdigit()):
         print("ERROR: Invalid Command");
         HockeyDivisionPreDN = "E";
        if(HockeyDivisionPreDN.upper()!="E" and HockeyDivisionPreDN.isdigit() and (int(HockeyDivisionPreDN)>6 or int(HockeyDivisionPreDN)<0)):
         print("ERROR: Invalid Command");
         HockeyDivisionPreDN = "E";
        if(HockeyDivisionPreDN.upper()!="E" and int(HockeyDivisionPreDN)<len(hockeyarray[HockeyLeagueSN]['']['divisionlist']) and int(HockeyDivisionPreDN)>-1):
         HockeyDivisionIntCN = int(HockeyDivisionPreDN);
         HockeyDivisionDN = hockeyarray[HockeyLeagueSN]['']['divisionlist'][HockeyDivisionIntCN];
         hockeyarray = libhockeydata.RemoveHockeyDivisionFromArray(hockeyarray, HockeyLeagueSN, HockeyDivisionDN, "");
       if(submenuact.upper()=="E"):
        sub_sub_keep_loop = False;
     if(hockeyarray[HockeyLeagueSN]['leagueinfo']['conferences']=="yes"):
      sub_sub_keep_loop = True;
      while(sub_sub_keep_loop):
       conferencec = 0;
       print("E: Back to Main Menu");
       while(conferencec<len(hockeyarray[HockeyLeagueSN]['conferencelist'])):
        lshn = hockeyarray[HockeyLeagueSN]['conferencelist'][conferencec];
        print(str(conferencec)+": "+hockeyarray[HockeyLeagueSN]['quickinfo']['conferenceinfo'][lshn]['fullname']);
        conferencec = conferencec + 1;
       HockeyConferencePreSN = get_user_input("Enter Hockey Conference number: ");
       if(HockeyConferencePreSN.upper()!="E" and not HockeyConferencePreSN.isdigit()):
        print("ERROR: Invalid Command");
        HockeyConferencePreSN = "E";
       if(HockeyConferencePreSN.upper()!="E" and HockeyConferencePreSN.isdigit() and (int(HockeyConferencePreSN)>len(hockeyarray[HockeyLeagueSN]['conferencelist']) or int(HockeyConferencePreSN)<0)):
        print("ERROR: Invalid Command");
        HockeyConferencePreSN = "E";
       if(HockeyConferencePreSN.upper()!="E" and int(HockeyConferencePreSN)<len(hockeyarray[HockeyLeagueSN]['conferencelist']) and int(HockeyConferencePreSN)>-1):
        HockeyConferenceIntSN = int(HockeyConferencePreSN);
        HockeyConferenceSN = hockeyarray[HockeyLeagueSN]['conferencelist'][HockeyConferenceIntSN];
        sub_sub_sub_keep_loop = True;
        while(sub_sub_sub_keep_loop):
         submenuact = get_user_input("E: Back to Main Menu\n1: Add Hockey Division\n2: Remove Hockey Division\n3: Edit Hockey Division\nWhat do you want to do? ");
         if(submenuact.upper()!="E" and not submenuact.isdigit()):
          print("ERROR: Invalid Command");
          submenuact = "";
         if(submenuact.upper()!="E" and submenuact.isdigit() and (int(submenuact)>3 or int(submenuact)<1)):
          print("ERROR: Invalid Command");
          submenuact = "";
         if(submenuact.upper()=="1"):
          HockeyDivisionDN = get_user_input("Enter Hockey Division name: ");
          if(HockeyDivisionDN in hockeyarray[HockeyLeagueSN][HockeyConferenceSN]['divisionlist']):
           print("ERROR: Hockey Division with that name exists");
          if(HockeyDivisionDN not in hockeyarray[HockeyLeagueSN][HockeyConferenceSN]['divisionlist']):
           HockeyDivisionDPFN = get_user_input("Enter Hockey Division prefix: ");
           HockeyDivisionDSFN = get_user_input("Enter Hockey Division suffix: ");
          libhockeydata.AddHockeyDivisionToArray(hockeyarray, HockeyLeagueSN, HockeyDivisionDN, HockeyConferenceSN, HockeyDivisionDPFN, HockeyDivisionDSFN);
         if(submenuact.upper()=="2"):
          divisionc = 0;
          print("E: Back to Hockey Division Tool");
          while(divisionc<len(hockeyarray[HockeyLeagueSN][HockeyConferenceSN]['divisionlist'])):
           lshn = hockeyarray[HockeyLeagueSN][HockeyConferenceSN]['divisionlist'][divisionc];
           print(str(divisionc)+": "+hockeyarray[HockeyLeagueSN]['quickinfo']['divisioninfo'][lshn]['fullname']);
           divisionc = divisionc + 1;
          HockeyDivisionPreDN = get_user_input("Enter Hockey Division number: ");
          if(HockeyDivisionPreDN.upper()!="E" and not HockeyDivisionPreDN.isdigit()):
           print("ERROR: Invalid Command");
           HockeyDivisionPreDN = "E";
          if(HockeyDivisionPreDN.upper()!="E" and HockeyDivisionPreDN.isdigit() and (int(HockeyDivisionPreDN)>6 or int(HockeyDivisionPreDN)<0)):
           print("ERROR: Invalid Command");
           HockeyDivisionPreDN = "E";
          if(HockeyDivisionPreDN.upper()!="E" and int(HockeyDivisionPreDN)<len(hockeyarray[HockeyLeagueSN][HockeyConferenceSN]['divisionlist']) and int(HockeyDivisionPreDN)>-1):
           HockeyDivisionIntCN = int(HockeyDivisionPreDN);
           HockeyDivisionDN = hockeyarray[HockeyLeagueSN][HockeyConferenceSN]['divisionlist'][HockeyDivisionIntCN];
           hockeyarray = libhockeydata.RemoveHockeyDivisionFromArray(hockeyarray, HockeyLeagueSN, HockeyDivisionDN, HockeyConferenceSN);
         if(submenuact.upper()=="E"):
          sub_sub_sub_keep_loop = False;
       if(HockeyConferencePreSN.upper()=="E"):
        sub_sub_keep_loop = False;
   if(HockeyLeaguePreSN.upper()=="E"):
    sub_keep_loop = False;
 if(menuact=="4" and len(hockeyarray['leaguelist'])<=0):
  print("ERROR: There are no Hockey Leagues");
 if(menuact=="4" and len(hockeyarray['leaguelist'])>0):
  sub_keep_loop = True;
  while(sub_keep_loop):
   submenuact = get_user_input("E: Back to Main Menu\n1: Add Hockey Team\n2: Remove Hockey Team\n3: Edit Hockey Team\nWhat do you want to do? ");
   if(submenuact.upper()!="E" and not submenuact.isdigit()):
    print("ERROR: Invalid Command");
    submenuact = "";
   if(submenuact.upper()!="E" and submenuact.isdigit() and (int(submenuact)>3 or int(submenuact)<1)):
    print("ERROR: Invalid Command");
    submenuact = "";
   if(submenuact.upper()=="E"):
    sub_keep_loop = False;
   print("ERROR: Sorry Command not Implemented yet");
   raise NotImplementedError;
 if(menuact=="5" and len(hockeyarray['leaguelist'])<=0):
  print("ERROR: There are no Hockey Leagues");
 if(menuact=="5" and len(hockeyarray['leaguelist'])>0):
  sub_keep_loop = True;
  while(sub_keep_loop):
   submenuact = get_user_input("E: Back to Main Menu\n1: Add Hockey Arena\n2: Remove Hockey Arena\n3: Edit Hockey Arena\nWhat do you want to do? ");
   if(submenuact.upper()!="E" and not submenuact.isdigit()):
    print("ERROR: Invalid Command");
    submenuact = "";
   if(submenuact.upper()!="E" and submenuact.isdigit() and (int(submenuact)>3 or int(submenuact)<1)):
    print("ERROR: Invalid Command");
    submenuact = "";
   if(submenuact.upper()=="E"):
    sub_keep_loop = False;
   print("ERROR: Sorry Command not Implemented yet");
   raise NotImplementedError;
 if(menuact=="6" and len(hockeyarray['leaguelist'])<=0):
  print("ERROR: There are no Hockey Leagues");
 if(menuact=="6" and len(hockeyarray['leaguelist'])>0):
  sub_keep_loop = True;
  while(sub_keep_loop):
   submenuact = get_user_input("E: Back to Main Menu\n1: Add Hockey Game\n2: Remove Hockey Game\n3: Edit Hockey Game\nWhat do you want to do? ");
   if(submenuact.upper()!="E" and not submenuact.isdigit()):
    print("ERROR: Invalid Command");
    submenuact = "";
   if(submenuact.upper()!="E" and submenuact.isdigit() and (int(submenuact)>3 or int(submenuact)<1)):
    print("ERROR: Invalid Command");
    submenuact = "";
   if(submenuact.upper()=="E"):
    sub_keep_loop = False;
   print("ERROR: Sorry Command not Implemented yet");
   raise NotImplementedError;
 if(menuact=="7"):
  sub_keep_loop = True;
  while(sub_keep_loop):
   submenuact = get_user_input("E: Back to Main Menu\n1: Empty Hockey Database\n2: Import Hockey Database From File\n3: Export Hockey Database to File\nWhat do you want to do? ");
   if(submenuact.upper()!="E" and not submenuact.isdigit()):
    print("ERROR: Invalid Command");
    submenuact = "";
   if(submenuact.upper()!="E" and submenuact.isdigit() and (int(submenuact)>3 or int(submenuact)<1)):
    print("ERROR: Invalid Command");
    submenuact = "";
   if(submenuact=="1"):
    HockeyDatabaseFN = get_user_input("Enter Hockey Database File Name For Output: ");
    hockeyarray = libhockeydata.CreateHockeyArray(HockeyDatabaseFN);
   if(submenuact=="2"):
    HockeyDatabaseFN = get_user_input("Enter Hockey Database File Name For Import: ");
    ext = os.path.splitext(HockeyDatabaseFN)[-1].lower();
    if(ext in extensions):
     if(ext==".xml" and libhockeydata.CheckXMLFile(HockeyDatabaseFN)):
      hockeyarray = libhockeydata.MakeHockeyArrayFromHockeyXML(HockeyDatabaseFN);
     elif(ext==".db3" and libhockeydata.CheckSQLiteDatabase(HockeyDatabaseFN)):
      hockeyarray = libhockeydata.MakeHockeyArrayFromHockeyDatabase(HockeyDatabaseFN);
     elif(ext==".sql"):
      hockeyarray = libhockeydata.MakeHockeyArrayFromHockeySQL(HockeyDatabaseFN);
     elif(ext==".json"):
      hockeyarray = libhockeydata.MakeHockeyArrayFromHockeyJSON(HockeyDatabaseFN);
     else:
      print("ERROR: Invalid Command");
     if(libhockeydata.CheckHockeySQLiteArray(hockeyarray)):
      hockeyarray = libhockeydata.MakeHockeyArrayFromHockeySQLiteArray(hockeyarray);
     if(not libhockeydata.CheckHockeyArray(hockeyarray)):
      print("ERROR: Invalid Command");
   if(submenuact.upper()=="3"):
    sub_sub_keep_loop = True;
    while(sub_sub_keep_loop):
     subsubmenuact = get_user_input("E: Back to Hockey Database Tool\n1: Export Hockey Database to Hockey XML\n2: Export Hockey Database to Hockey JSON\n3: Export Hockey Database to Hockey Py\n4: Export Hockey Database to Hockey Py Alt\n5: Export Hockey Database to Hockey SQL\n6: Export Hockey Database to Hockey Database File\nWhat do you want to do? ");
     if(subsubmenuact.upper()!="E" and not subsubmenuact.isdigit()):
      print("ERROR: Invalid Command");
      subsubmenuact = "E";
     if(subsubmenuact.upper()!="E" and subsubmenuact.isdigit() and (int(subsubmenuact)>6 or int(subsubmenuact)<1)):
      print("ERROR: Invalid Command");
      subsubmenuact = "E";
     if(subsubmenuact=="1"):
      HockeyDatabaseFN = get_user_input("Enter Hockey Database XML File Name to Export: ");
      libhockeydata.MakeHockeyXMLFileFromHockeyArray(hockeyarray, HockeyDatabaseFN);
     if(subsubmenuact=="2"):
      HockeyDatabaseFN = get_user_input("Enter Hockey Database JSON File Name to Export: ");
      libhockeydata.MakeHockeyJSONFileFromHockeyArray(hockeyarray, HockeyDatabaseFN);
     if(subsubmenuact=="3"):
      HockeyDatabaseFN = get_user_input("Enter Hockey Database Python File Name to Export: ");
      libhockeydata.MakeHockeyPythonFileFromHockeyArray(hockeyarray, HockeyDatabaseFN);
     if(subsubmenuact=="4"):
      HockeyDatabaseFN = get_user_input("Enter Hockey Database Python File Name to Export: ");
      libhockeydata.MakeHockeyPythonAltFileFromHockeyArray(hockeyarray, HockeyDatabaseFN);
     if(subsubmenuact=="5"):
      HockeyDatabaseFN = get_user_input("Enter Hockey Database SQL File Name to Export: ");
      libhockeydata.MakeHockeySQLFileFromHockeyArray(hockeyarray, HockeyDatabaseFN);
     if(subsubmenuact=="6"):
      HockeyDatabaseFN = get_user_input("Enter Hockey Database File Name to Export: ");
      libhockeydata.MakeHockeyDatabaseFromHockeyArray(hockeyarray, HockeyDatabaseFN);
     if(subsubmenuact.upper()=="E"):
      sub_sub_keep_loop = False;
   if(submenuact.upper()=="E"):
    sub_keep_loop = False;
 if(menuact.upper()=="E"):
  keep_loop = False;
