#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2015-2024 Game Maker 2k - https://github.com/GameMaker2k
    Copyright 2015-2024 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: example.py - Last Update: 10/17/2024 Ver. 0.9.4 RC 1 - Author: cooldude2k $
'''

from __future__ import print_function
import os
import random
import sys
import pyhockeystats

# Ensure compatibility with both Python 2 and 3
try:
    reload(sys)  # Only required in Python 2
    sys.setdefaultencoding('utf-8')
except (NameError, AttributeError):
    pass

# Function to gather valid directories
def get_data_directories():
    potential_dirs = [
        "./data/xml", "./data/xmlalt", 
        "./data/json", "./data/jsonalt", 
        "./data/sql", "./php/data"
    ]
    return [d for d in potential_dirs if os.path.isdir(d)]

# Function to process a file based on its extension and load data
def process_file(filepath, extensions, extensionsc):
    fileinfo = os.path.splitext(filepath)
    ext = fileinfo[1].lower()
    subext = os.path.splitext(fileinfo[0])[1].lower() if ext in extensionsc else None

    if ext in extensions or subext in extensions:
        funcarray = {}
        sqlitedatatype = False
        
        if ext == ".xml" or subext == ".xml":
            if pyhockeystats.CheckXMLFile(filepath):
                if pyhockeystats.CheckHockeyXML(filepath):
                    funcarray = {'informat': "xml", 'inxmlfile': filepath}
                elif pyhockeystats.CheckHockeySQLiteXML(filepath):
                    funcarray = {'informat': "xml", 'inxmlfile': filepath}
                    sqlitedatatype = True
        elif ext == ".db3" and pyhockeystats.CheckSQLiteDatabase(filepath):
            funcarray = {'informat': "database", 'insdbfile': filepath}
        elif ext == ".sql" or subext == ".sql":
            funcarray = {'informat': "sql", 'insqlfile': filepath}
        elif ext == ".json" or subext == ".json":
            funcarray = {'informat': "json", 'injsonfile': filepath}
        else:
            return None
        
        if sqlitedatatype:
            hockeyarray = pyhockeystats.MakeHockeySQLiteArrayFromHockeySQLiteData(funcarray)
        else:
            hockeyarray = pyhockeystats.MakeHockeyArrayFromHockeyData(funcarray)

        if pyhockeystats.CheckHockeySQLiteArray(hockeyarray):
            hockeyarray = pyhockeystats.MakeHockeyArrayFromHockeySQLiteArray(hockeyarray)
        
        return hockeyarray if pyhockeystats.CheckHockeyArray(hockeyarray) else None
    return None

# Function to display hockey data
def display_hockey_data(hockeyarray):
    for hlkey in hockeyarray['leaguelist']:
        for hckey in hockeyarray[hlkey]['conferencelist']:
            for hdkey in hockeyarray[hlkey][hckey]['divisionlist']:
                for htkey in hockeyarray[hlkey][hckey][hdkey]['teamlist']:
                    conference = hockeyarray[hlkey].get('conferenceinfo', {}).get('fullname', '')
                    division = hockeyarray[hlkey][hckey].get('divisioninfo', {}).get('fullname', '')
                    team = hockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullname']
                    league = hockeyarray[hlkey]['leagueinfo']['fullname']
                    
                    if conference and division:
                        print("{league} / {conference} / {division} / {team}".format(
                            league=league, conference=conference, division=division, team=team))
                    elif conference:
                        print("{league} / {conference} / {team}".format(
                            league=league, conference=conference, team=team))
                    elif division:
                        print("{league} / {division} / {team}".format(
                            league=league, division=division, team=team))
                    else:
                        print("{league} / {team}".format(
                            league=league, team=team))

# Main function
def main():
    defroot = get_data_directories()
    if not defroot:
        print("No valid data directories found.")
        sys.exit(1)
    
    rootdir = sys.argv[1] if len(sys.argv) > 1 else random.choice(defroot)
    extensions = pyhockeystats.extensionswd
    extensionsc = pyhockeystats.outextlistwd

    if os.path.isdir(rootdir):
        for subdir, _, files in os.walk(rootdir):
            for file in files:
                filepath = os.path.join(subdir, file)
                hockeyarray = process_file(filepath, extensions, extensionsc)
                
                if hockeyarray:
                    print("\n--------------------------------------------------------------------------")
                    print("File: {}".format(filepath))
                    display_hockey_data(hockeyarray)
                    print("--------------------------------------------------------------------------\n")
    elif os.path.isfile(rootdir):
        hockeyarray = process_file(rootdir, extensions, extensionsc)
        if hockeyarray:
            print("\n--------------------------------------------------------------------------")
            print("File: {}".format(rootdir))
            display_hockey_data(hockeyarray)
            print("--------------------------------------------------------------------------\n")
    else:
        print("Invalid path provided.")
        sys.exit(1)

if __name__ == "__main__":
    main()
