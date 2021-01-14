#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2015-2020 Game Maker 2k - https://github.com/GameMaker2k
    Copyright 2015-2020 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: mkhockeytool.py - Last Update: 4/4/2020 Ver. 0.4.0 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals;
import libhockeydata;

def get_user_input(txt):
 try:
  return raw_input(txt);
 except NameError:
  return input(txt);
 return False;

keep_loop = True;
#hockeydict = libhockeydata.CreateHockeyArray();
hockeydict = libhockeydata.MakeHockeyArrayFromHockeyXML("./fhmt1.xml");
while(keep_loop is True):
 menuact = get_user_input("E: Exit Hockey Tool\n1: Hockey League Tool\n2: Hockey Conference Tool\n3: Hockey Division Tool\n4: Hockey Team Tool\n5: Hockey Database Tool\nWhat do you want to do? ");
 if(menuact.upper()!="E" and not menuact.isdigit()):
  print("ERROR: Invalid Command");
  menuact = " ";
 if(menuact.upper()!="E" and menuact.isdigit() and (int(menuact)>6 or int(menuact)<1)):
  print("ERROR: Invalid Command");
  menuact = "";
 if(menuact=="1"):
  sub_keep_loop = True;
  while(sub_keep_loop is True):
   submenuact = get_user_input("E: Back to Main Menu\n1: Add Hockey League\n2: Remove Hockey League\nWhat do you want to do? ");
   if(submenuact.upper()!="E" and not submenuact.isdigit()):
    print("ERROR: Invalid Command");
    submenuact = " ";
   if(submenuact.upper()!="E" and submenuact.isdigit() and (int(submenuact)>2 or int(submenuact)<1)):
    print("ERROR: Invalid Command");
    submenuact = "";
   if(submenuact=="1"):
    HockeyLeagueSN = get_user_input("Enter Hockey League short name: ");
    if(HockeyLeagueSN in hockeydict['leaguelist']):
     print("ERROR: Hockey League with that short name exists");
    if(HockeyLeagueSN not in hockeydict['leaguelist']):
     HockeyLeagueFN = get_user_input("Enter Hockey League full name: ");
     HockeyLeagueCSN = get_user_input("Enter Hockey League country short name: ");
     HockeyLeagueCFN = get_user_input("Enter Hockey League country full name: ");
     HockeyLeagueSD = get_user_input("Enter Hockey League start date: ");
     HockeyLeaguePOF = get_user_input("Enter Hockey League playoff format: ");
     HockeyLeagueOT = get_user_input("Enter Hockey League ordertype: ");
     HockeyLeagueHC = get_user_input("Does Hockey League have conferences: ");
     HockeyLeagueHD = get_user_input("Does Hockey League have divisions: ");
     hockeydict = libhockeydata.AddHockeyLeagueToArray(hockeydict, HockeyLeagueSN, HockeyLeagueFN, HockeyLeagueCSN, HockeyLeagueCFN, HockeyLeagueSD, HockeyLeaguePOF, HockeyLeagueOT, HockeyLeagueHC, HockeyLeagueHD);
   if(submenuact=="2" and len(hockeydict['leaguelist'])<=0):
    print("ERROR: There are no Hockey Leagues to delete");
   if(submenuact=="2" and len(hockeydict['leaguelist'])>0):
    leaguec = 0;
    print("E: Back to Hockey League Tool");
    while(leaguec<len(hockeydict['leaguelist'])):
     lshn = hockeydict['leaguelist'][leaguec];
     print(str(leaguec)+": "+hockeydict[lshn]['leagueinfo']['fullname']);
     leaguec = leaguec + 1;
    HockeyLeaguePreSN = get_user_input("Enter Hockey League short name: ");
    if(HockeyLeaguePreSN.upper()!="E" and not HockeyLeaguePreSN.isdigit()):
     print("ERROR: Invalid Command");
     HockeyLeaguePreSN = "E";
    if( HockeyLeaguePreSN.upper()!="E" and HockeyLeaguePreSN.isdigit() and (int(HockeyLeaguePreSN)>6 or int(HockeyLeaguePreSN)<1)):
     print("ERROR: Invalid Command");
     HockeyLeaguePreSN = "E";
    if(HockeyLeaguePreSN.upper()!="E" and int(HockeyLeaguePreSN)<len(hockeydict['leaguelist']) and int(HockeyLeaguePreSN)>-1):
     HockeyLeaguePreSN = int(HockeyLeaguePreSN);
     HockeyLeagueSN = hockeydict['leaguelist'][HockeyLeaguePreSN];
     hockeydict = libhockeydata.RemoveHockeyLeagueFromArray(hockeydict, HockeyLeagueSN);
   if(submenuact.upper()=="E"):
    sub_keep_loop = False;
 if(menuact=="2" and len(hockeydict['leaguelist'])<=0):
  print("ERROR: There are no Hockey Leagues");
 if(menuact=="2" and len(hockeydict['leaguelist'])>0):
  sub_keep_loop = True;
  while(sub_keep_loop is True):
   leaguec = 0;
   print("E: Back to Hockey League Tool");
   while(leaguec<len(hockeydict['leaguelist'])):
    lshn = hockeydict['leaguelist'][leaguec];
    print(str(leaguec)+": "+hockeydict[lshn]['leagueinfo']['fullname']);
    if(hockeydict[lshn]['leagueinfo']['conferences']=="no"):
     print("ERROR: Hockey League can not have any conferences");
    leaguec = leaguec + 1;
   sub_keep_loop = False;
 if(menuact.upper()=="E"):
  keep_loop = False;
