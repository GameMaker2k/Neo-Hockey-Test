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

    $FileInfo: example.py - Last Update: 2/17/2020 Ver. 0.2.6 RC 1 - Author: cooldude2k $
'''

import libhockeydata, os;

rootdir = "./data/xml"
extensions = ['.xml']

for subdir, dirs, files in os.walk(rootdir):
 print("");
 print("--------------------------------------------------------------------------");
 print("");
 for file in files:
  ext = os.path.splitext(file)[-1].lower();
  if ext in extensions:
   hockeyarray = libhockeydata.MakeHockeyArrayFromHockeyXML(os.path.join(subdir, file));
   for hlkey in hockeyarray['leaguelist']:
    for hckey in hockeyarray[hlkey]['conferencelist']:
     for hdkey in hockeyarray[hlkey][hckey]['divisionlist']:
      for htkey in hockeyarray[hlkey][hckey][hdkey]['teamlist']:
       print(hlkey+" / "+hckey+" / "+hdkey+" / "+htkey);
   print("");
   print("--------------------------------------------------------------------------");
   print("");
