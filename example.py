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

    $FileInfo: example.py - Last Update: 2/4/2020 Ver. 0.1.0 RC 1 - Author: cooldude2k $
'''

import  libhockeydata;

print("");
print("--------------------------------------------------------------------------");
print("");

hockeyarray = libhockeydata.MakeHockeyArrayFromHockeyXML("./data/fhmt1.xml");
for hlkey in hockeyarray['leaguelist']:
 for hckey in hockeyarray[hlkey]['conferencelist']:
  for hdkey in hockeyarray[hlkey][hckey]['divisionlist']:
   for htkey in hockeyarray[hlkey][hckey][hdkey]['teamlist']:
    print(hlkey+" / "+hckey+" / "+hdkey+" / "+htkey);

print("");
print("--------------------------------------------------------------------------");
print("");

hockeyarray = libhockeydata.MakeHockeyArrayFromHockeyXML("./data/fhmt2.xml");
for hlkey in hockeyarray['leaguelist']:
 for hckey in hockeyarray[hlkey]['conferencelist']:
  for hdkey in hockeyarray[hlkey][hckey]['divisionlist']:
   for htkey in hockeyarray[hlkey][hckey][hdkey]['teamlist']:
    print(hlkey+" / "+hckey+" / "+hdkey+" / "+htkey);

print("");
print("--------------------------------------------------------------------------");
print("");

hockeyarray = libhockeydata.MakeHockeyArrayFromHockeyXML("./data/hockeydata15.xml");
for hlkey in hockeyarray['leaguelist']:
 for hckey in hockeyarray[hlkey]['conferencelist']:
  for hdkey in hockeyarray[hlkey][hckey]['divisionlist']:
   for htkey in hockeyarray[hlkey][hckey][hdkey]['teamlist']:
    print(hlkey+" / "+hckey+" / "+hdkey+" / "+htkey);

print("");
print("--------------------------------------------------------------------------");
print("");

hockeyarray = libhockeydata.MakeHockeyArrayFromHockeyXML("./data/hockeydata17.xml");
for hlkey in hockeyarray['leaguelist']:
 for hckey in hockeyarray[hlkey]['conferencelist']:
  for hdkey in hockeyarray[hlkey][hckey]['divisionlist']:
   for htkey in hockeyarray[hlkey][hckey][hdkey]['teamlist']:
    print(hlkey+" / "+hckey+" / "+hdkey+" / "+htkey);

print("");
print("--------------------------------------------------------------------------");
print("");
