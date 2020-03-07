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

    $FileInfo: example.py - Last Update: 2/26/2020 Ver. 0.3.1 RC 1 - Author: cooldude2k $
'''

import libhockeydata, os;

rootdir = "./data/xml"
extensions = ['.xml']

for subdir, dirs, files in os.walk(rootdir):
 print("");
 print("--------------------------------------------------------------------------");
 print("");                                                                                                                                                                                                                                                                                                                   for file in files:                                                                                                                                                                                                                                                                                                            ext = os.path.splitext(file)[-1].lower();                                                                                                                                                                                                                                                                                    if ext in extensions:
 hockeyarray = libhockeydata.MakeHockeyArrayFromHockeyXML(os.path.join(subdir, file));
 for hlkey in hockeyarray['leaguelist']:
  for hckey in hockeyarray[hlkey]['conferencelist']:
   for hdkey in hockeyarray[hlkey][hckey]['divisionlist']:
    for htkey in hockeyarray[hlkey][hckey][hdkey]['teamlist']:
     teamnameprefix = hockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix'];
     teamnamesuffix = hockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix'];
     htkeyfull = libhockeydata.GetFullTeamName(htkey, teamnameprefix, teamnamesuffix);
     hlkeyfull = hockeyarray[hlkey]['leagueinfo']['fullname'];
     if(len(hckey)==0 and len(hdkey)==0):
      print(hlkeyfull+" / "+htkeyfull);
     if(len(hckey)==0 and len(hdkey)>0):
      print(hlkeyfull+" / "+hdkey+" Division / "+htkeyfull);
     if(len(hckey)>0 and len(hdkey)==0):
      print(hlkeyfull+" / "+hckey+" Conference / "+htkeyfull);
     if(len(hckey)>0 and len(hdkey)>0):
      print(hlkeyfull+" / "+hckey+" Conference / "+hdkey+" Division / "+htkeyfull);
   print("");
   print("--------------------------------------------------------------------------");
   print("");
