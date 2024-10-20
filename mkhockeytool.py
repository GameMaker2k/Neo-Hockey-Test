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

    $FileInfo: mkhockeytool.py - Last Update: 10/17/2024 Ver. 0.9.6 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals, generators, with_statement, nested_scopes

import argparse
import logging
import os
import sys

import pyhockeystats

try:
    reload(sys)
except NameError:
    from importlib import reload
    reload(sys)
try:
    sys.setdefaultencoding('utf-8')
except AttributeError:
    pass

havereadline = False
try:
    import readline
    havereadline = True
except ImportError:
    havereadline = False

__project__ = pyhockeystats.__project__
__program_name__ = pyhockeystats.__program_name__
__project_url__ = pyhockeystats.__project_url__
__version_info__ = pyhockeystats.__version_info__
__version_date_info__ = pyhockeystats.__version_date_info__
__version_date__ = pyhockeystats.__version_date__
__version_date_plusrc__ = pyhockeystats.__version_date_plusrc__
__version__ = pyhockeystats.__version__

defxmlfile = "./data/hockeydata.xml"
defsgmlfile = "./data/hockeydata.sgml"
defsdbfile = "./data/hockeydata.db3"
defoldsdbfile = "./data/hockeydata.db3"
defsqlfile = "./data/hockeydata.sql"
defjsonfile = "./data/hockeydata.json"
defyamlfile = "./data/hockeydata.yaml"
extensions = ['.xml', '.sgml', '.json', '.yaml', '.sql', '.db3', '.db', '.sdb', '.sqlite', '.sqlite3', '.py']
extensionsin = ['.xml', '.sgml', '.json', '.yaml', '.sql', '.db3', '.db', '.sdb', '.sqlite', '.sqlite3']
extensionsc = ['.gz', '.bz2', '.zst', '.xz', '.lz4', '.lzo', '.lzop', '.lzma', '.zl', '.zz', '.zlib']
filetypes = ['xml', 'sgml', 'json', 'yaml', 'sql', 'db3', 'py', 'pyalt', 'oopy', 'oopyalt']


def get_user_input(txt):
    try:
        return raw_input(txt)
    except NameError:
        return input(txt)
    return False


argparser = argparse.ArgumentParser(
    description="A test script for managing hockey games and stats.",
    conflict_handler="resolve", add_help=True
)
argparser.add_argument(
    "-v", "--ver", "--version",
    action="version",
    version=__program_name__ + " " + __version__
)
argparser.add_argument(
    "-i", "-f", "--infile",
    nargs="?", default=None,
    help="Specify the input database file to load."
)
argparser.add_argument(
    "-e", "-n", "--empty",
    action="store_true",
    help="Create an empty database file."
)
argparser.add_argument(
    "-o", "-e", "--outfile",
    nargs="?", default=None,
    help="Specify the output database file to save."
)
argparser.add_argument(
    "-x", "-p", "--export",
    action="store_true",
    help="Export the input file to the database."
)
argparser.add_argument(
    "-t", "-y", "--type",
    nargs="?", default=None,
    help="Specify the type of file to export."
)
argparser.add_argument(
    "-V", "-d", "--verbose",
    action="store_true",
    help="Enable verbose output for debugging information."
)
argparser.add_argument(
    "-T", "-r", "--verbosetype",
    type=str, default="array",
    help="Set the verbosity type (e.g., json, yaml, sgml, xml). Default is 'array'."
)
getargs = argparser.parse_args()
verboseon = getargs.verbose
if ('VERBOSE' in os.environ or 'DEBUG' in os.environ):
    verboseon = True
if (verboseon):
    logging.basicConfig(format="%(message)s",
                        stream=sys.stdout, level=logging.DEBUG)

if (not getargs.empty and getargs.infile is None):
    premenuact = get_user_input(
        "E: Exit Hockey Tool\n1: Empty Hockey Database\n2: Import Hockey Database From File\nWhat do you want to do? ")
    if (premenuact.upper() != "E" and not premenuact.isdigit()):
        print("ERROR: Invalid Command")
        premenuact = "E"
    elif (premenuact.upper() != "E" and premenuact.isdigit() and (int(premenuact) > 2 or int(premenuact) < 1)):
        print("ERROR: Invalid Command")
        premenuact = "E"
    elif (premenuact.upper() == "E"):
        sys.exit()
if (getargs.empty and getargs.infile is None):
    premenuact = "1"
elif (getargs.infile is not None):
    premenuact = "2"
    if (getargs.empty):
        premenuact = "1"
    elif (not getargs.empty):
        premenuact = "2"
if (premenuact == "1"):
    if (getargs.infile is None):
        HockeyDatabaseFN = get_user_input(
            "Enter Hockey Database File Name For Output: ")
    elif (getargs.infile is not None):
        HockeyDatabaseFN = getargs.infile
    hockeyarray = pyhockeystats.CreateHockeyArray(HockeyDatabaseFN)
elif (premenuact == "2"):
    if (getargs.infile is None):
        HockeyDatabaseFN = get_user_input(
            "Enter Hockey Database File Name For Import: ")
    elif (getargs.infile is not None):
        HockeyDatabaseFN = getargs.infile
    fileinfo = os.path.splitext(HockeyDatabaseFN)
    ext = fileinfo[-1].lower()
    subfileinfo = None
    subext = None
    if (ext in extensionsc):
        subfileinfo = os.path.splitext(fileinfo[0])
        subext = subfileinfo[1].lower()
    else:
        subfileinfo = None
        subext = None
    if (ext in extensionsin or subext in extensions):
        verbosein = True
        if (getargs.export):
            verbosein = False
        if ((ext == ".xml" or subext == ".xml") and pyhockeystats.CheckXMLFile(HockeyDatabaseFN) and pyhockeystats.CheckHockeyXML(HockeyDatabaseFN)):
            hockeyarray = pyhockeystats.MakeHockeyArrayFromHockeyXML(
                HockeyDatabaseFN, verbose=verbosein, verbosetype=getargs.verbosetype)
        elif ((ext == ".xml" or subext == ".xml") and pyhockeystats.CheckXMLFile(HockeyDatabaseFN) and pyhockeystats.CheckHockeySQLiteXML(HockeyDatabaseFN)):
            hockeyarray = pyhockeystats.MakeHockeySQLiteArrayFromHockeyXML(
                HockeyDatabaseFN, verbose=verbosein, verbosetype=getargs.verbosetype)
        elif ((ext == ".sgml" or subext == ".sgml") and pyhockeystats.CheckSGMLFile(HockeyDatabaseFN) and pyhockeystats.CheckHockeySGML(HockeyDatabaseFN)):
            hockeyarray = pyhockeystats.MakeHockeyArrayFromHockeySGML(
                HockeyDatabaseFN, verbose=verbosein, verbosetype=getargs.verbosetype)
        elif ((ext == ".sgml" or subext == ".sgml") and pyhockeystats.CheckSGMLFile(HockeyDatabaseFN) and pyhockeystats.CheckHockeySQLiteSGML(HockeyDatabaseFN)):
            hockeyarray = pyhockeystats.MakeHockeySQLiteArrayFromHockeySGML(
                HockeyDatabaseFN, verbose=verbosein, verbosetype=getargs.verbosetype)
        elif ((ext == ".db3" or ext == ".db" or ext == ".sdb" or ext == ".sqlite" or ext == ".sqlite3") and pyhockeystats.CheckSQLiteDatabase(HockeyDatabaseFN)):
            hockeyarray = pyhockeystats.MakeHockeyArrayFromHockeyDatabase(
                HockeyDatabaseFN, verbose=verbosein, verbosetype=getargs.verbosetype)
        elif (ext == ".sql" or subext == ".sql"):
            hockeyarray = pyhockeystats.MakeHockeyArrayFromHockeySQL(
                HockeyDatabaseFN, verbose=verbosein, verbosetype=getargs.verbosetype)
        elif (ext == ".json" or subext == ".json"):
            hockeyarray = pyhockeystats.MakeHockeyArrayFromHockeyJSON(
                HockeyDatabaseFN, verbose=verbosein, verbosetype=getargs.verbosetype)
        else:
            print("ERROR: Invalid Command")
        if (pyhockeystats.CheckHockeySQLiteArray(hockeyarray)):
            hockeyarray = pyhockeystats.MakeHockeyArrayFromHockeySQLiteArray(
                hockeyarray, verbose=verbosein, verbosetype=getargs.verbosetype)
        if (not pyhockeystats.CheckHockeyArray(hockeyarray)):
            print("ERROR: Invalid Command")

if (getargs.export):
    if (getargs.type is not None and getargs.type not in filetypes):
        getargs.type = None
    if (getargs.type is not None and (getargs.type.lower() == "xml" and
      getargs.type.lower() == "xmlalt")):
        if (getargs.outfile is None):
            HockeyDatabaseFN = get_user_input(
                "Enter Hockey Database XML File Name to Export: ")
            getargs.outfile = HockeyDatabaseFN
    if (getargs.type is not None and getargs.type.lower() == "sgml"):
        if (getargs.outfile is None):
            HockeyDatabaseFN = get_user_input(
                "Enter Hockey Database SGML File Name to Export: ")
            getargs.outfile = HockeyDatabaseFN
    elif (getargs.type is not None and getargs.type.lower() == "json"):
        if (getargs.outfile is None):
            HockeyDatabaseFN = get_user_input(
                "Enter Hockey Database JSON File Name to Export: ")
            getargs.outfile = HockeyDatabaseFN
    elif (getargs.type is not None and getargs.type.lower() == "yaml"):
        if (getargs.outfile is None):
            HockeyDatabaseFN = get_user_input(
                "Enter Hockey Database YAML File Name to Export: ")
            getargs.outfile = HockeyDatabaseFN
    elif (getargs.type is not None and getargs.type.lower() == "py" or
          getargs.type is not None and getargs.type.lower() == "pyalt" or
          getargs.type is not None and getargs.type.lower() == "oopy" or
          getargs.type is not None and getargs.type.lower() == "oopyalt"):
        if (getargs.outfile is None):
            HockeyDatabaseFN = get_user_input(
                "Enter Hockey Database Python File Name to Export: ")
            getargs.outfile = HockeyDatabaseFN
    elif (getargs.type is not None and getargs.type.lower() == "sql"):
        if (getargs.outfile is None):
            HockeyDatabaseFN = get_user_input(
                "Enter Hockey Database SQL File Name to Export: ")
            getargs.outfile = HockeyDatabaseFN
    elif (getargs.type is not None and getargs.type.lower() == "db3"):
        if (getargs.outfile is None and hockeyarray['database']==":memory:"):
            HockeyDatabaseFN = get_user_input(
                "Enter Hockey Database File Name to Export: ")
            getargs.outfile = HockeyDatabaseFN
        elif (getargs.outfile is None and hockeyarray['database']!=":memory:"):
            HockeyDatabaseFN = hockeyarray['database']
            getargs.outfile = HockeyDatabaseFN
    else:
        ext = os.path.splitext(getargs.outfile)[-1].lower()
        if (ext in extensions):
            if (ext == ".xml"):
                getargs.type = "xml"
            elif (ext == ".db3" or ext == ".db" or ext == ".sdb" or ext == ".sqlite" or ext == ".sqlite3"):
                getargs.type = "db3"
            elif (ext == ".sql"):
                getargs.type = "sql"
            elif (ext == ".json"):
                getargs.type = "json"
            elif (ext == ".yaml"):
                getargs.type = "yaml"
            elif (ext == ".py"):
                getargs.type = "py"
            else:
                getargs.type = "db3"
    if (getargs.type.lower() == "xml"):
        pyhockeystats.MakeHockeyXMLFileFromHockeyArray(
            hockeyarray, getargs.outfile, verbose=verboseon, verbosetype=getargs.verbosetype)
    elif (getargs.type.lower() == "xmlalt"):
        pyhockeystats.MakeHockeyXMLAltFileFromHockeyArray(
            hockeyarray, getargs.outfile, verbose=verboseon, verbosetype=getargs.verbosetype)
    elif (getargs.type.lower() == "sgml"):
        pyhockeystats.MakeHockeySGMLFileFromHockeyArray(
            hockeyarray, getargs.outfile, verbose=verboseon, verbosetype=getargs.verbosetype)
    elif (getargs.type.lower() == "json"):
        pyhockeystats.MakeHockeyJSONFileFromHockeyArray(
            hockeyarray, getargs.outfile, verbose=verboseon, verbosetype=getargs.verbosetype)
    elif (getargs.type.lower() == "yaml"):
        pyhockeystats.MakeHockeyYAMLFileFromHockeyArray(
            hockeyarray, getargs.outfile, verbose=verboseon, verbosetype=getargs.verbosetype)
    elif (getargs.type.lower() == "py"):
        pyhockeystats.MakeHockeyPythonFileFromHockeyArray(
            hockeyarray, getargs.outfile, verbose=verboseon, verbosetype=getargs.verbosetype)
    elif (getargs.type.lower() == "pyalt"):
        pyhockeystats.MakeHockeyPythonAltFileFromHockeyArray(
            hockeyarray, getargs.outfile, verbose=verboseon, verbosetype=getargs.verbosetype)
    elif (getargs.type.lower() == "oopy"):
        pyhockeystats.MakeHockeyPythonOOPFileFromHockeyArray(
            hockeyarray, getargs.outfile, verbose=verboseon, verbosetype=getargs.verbosetype)
    elif (getargs.type.lower() == "oopyalt"):
        pyhockeystats.MakeHockeyPythonOOPAltFileFromHockeyArray(
            hockeyarray, getargs.outfile, verbose=verboseon, verbosetype=getargs.verbosetype)
    elif (getargs.type.lower() == "sql"):
        pyhockeystats.MakeHockeySQLFileFromHockeyArray(
            hockeyarray, getargs.outfile, verbose=verboseon, verbosetype=getargs.verbosetype)
    elif (getargs.type.lower() == "db3"):
        pyhockeystats.MakeHockeyDatabaseFromHockeyArray(
            hockeyarray, getargs.outfile, verbose=verboseon, verbosetype=getargs.verbosetype)
    else:
        print("ERROR: Invalid Command")
    sys.exit()

if (premenuact == "1"):
    print("Using Empty Database at Location: "+HockeyDatabaseFN)
elif (premenuact == "2"):
    print("Using Populated Database at Location: "+HockeyDatabaseFN)
keep_loop = True
while (keep_loop):
    menuact = get_user_input(
        "E: Exit Hockey Tool\n1: Hockey League Tool\n2: Hockey Conference Tool\n3: Hockey Division Tool\n4: Hockey Team Tool\n5: Hockey Arena Tool\n6: Hockey Game Tool\n7: Hockey Database Tool\nWhat do you want to do? ")
    if (menuact.upper() != "E" and not menuact.isdigit()):
        print("ERROR: Invalid Command")
        menuact = ""
    elif (menuact.upper() != "E" and menuact.isdigit() and (int(menuact) > 7 or int(menuact) < 1)):
        print("ERROR: Invalid Command")
        menuact = ""
    elif (menuact == "1"):
        sub_keep_loop = True
        while (sub_keep_loop):
            submenuact = get_user_input(
                "E: Back to Main Menu\n1: Add Hockey League\n2: Remove Hockey League\n3: Edit Hockey League\nWhat do you want to do? ")
            if (submenuact.upper() != "E" and not submenuact.isdigit()):
                print("ERROR: Invalid Command")
                submenuact = ""
            elif (submenuact.upper() != "E" and submenuact.isdigit() and (int(submenuact) > 3 or int(submenuact) < 1)):
                print("ERROR: Invalid Command")
                submenuact = ""
            elif (submenuact == "1"):
                HockeyLeagueSN = get_user_input(
                    "Enter Hockey League short name: ")
                if (HockeyLeagueSN in hockeyarray['leaguelist']):
                    print("ERROR: Hockey League with that short name exists")
                elif (HockeyLeagueSN not in hockeyarray['leaguelist']):
                    HockeyLeagueFN = get_user_input(
                        "Enter Hockey League full name: ")
                    HockeyLeagueCSN = get_user_input(
                        "Enter Hockey League country short name: ")
                    HockeyLeagueCFN = get_user_input(
                        "Enter Hockey League country full name: ")
                    HockeyLeagueSD = get_user_input(
                        "Enter Hockey League start date: ")
                    HockeyLeaguePOF = get_user_input(
                        "Enter Hockey League playoff format: ")
                    HockeyLeagueOT = get_user_input(
                        "Enter Hockey League ordertype: ")
                    HockeyLeagueHC = get_user_input(
                        "Does Hockey League have conferences: ")
                    HockeyLeagueHD = get_user_input(
                        "Does Hockey League have divisions: ")
                    hockeyarray = pyhockeystats.AddHockeyLeagueToArray(
                        hockeyarray, HockeyLeagueSN, HockeyLeagueFN, HockeyLeagueCSN, HockeyLeagueCFN, HockeyLeagueSD, HockeyLeaguePOF, HockeyLeagueOT, HockeyLeagueHC, HockeyLeagueHD)
                    if (HockeyLeagueHC == "no"):
                        hockeyarray = pyhockeystats.AddHockeyConferenceToArray(
                            hockeyarray, HockeyLeagueSN, "")
                    if (HockeyLeagueHD == "no"):
                        hockeyarray = pyhockeystats.AddHockeyDivisionToArray(
                            hockeyarray, HockeyLeagueSN, "", "")
            elif (submenuact == "2" and len(hockeyarray['leaguelist']) <= 0):
                print("ERROR: There are no Hockey Leagues to delete")
            elif (submenuact == "2" and len(hockeyarray['leaguelist']) > 0):
                leaguec = 0
                print("E: Back to Hockey League Tool")
                while (leaguec < len(hockeyarray['leaguelist'])):
                    lshn = hockeyarray['leaguelist'][leaguec]
                    print(str(leaguec)+": " +
                          hockeyarray[lshn]['leagueinfo']['fullname'])
                    leaguec = leaguec + 1
                HockeyLeaguePreSN = get_user_input(
                    "Enter Hockey League number: ")
                if (HockeyLeaguePreSN.upper() != "E" and not HockeyLeaguePreSN.isdigit()):
                    print("ERROR: Invalid Command")
                    HockeyLeaguePreSN = "E"
                elif (HockeyLeaguePreSN.upper() != "E" and HockeyLeaguePreSN.isdigit() and (int(HockeyLeaguePreSN) > len(hockeyarray['leaguelist']) or int(HockeyLeaguePreSN) < 0)):
                    print("ERROR: Invalid Command")
                    HockeyLeaguePreSN = "E"
                elif (HockeyLeaguePreSN.upper() != "E" and int(HockeyLeaguePreSN) < len(hockeyarray['leaguelist']) and int(HockeyLeaguePreSN) > -1):
                    HockeyLeagueIntSN = int(HockeyLeaguePreSN)
                    HockeyLeagueSN = hockeyarray['leaguelist'][HockeyLeagueIntSN]
                    hockeyarray = pyhockeystats.RemoveHockeyLeagueFromArray(
                        hockeyarray, HockeyLeagueSN)
            elif (submenuact == "3" and len(hockeyarray['leaguelist']) <= 0):
                print("ERROR: There are no Hockey Leagues to edit")
            elif (submenuact == "3" and len(hockeyarray['leaguelist']) > 0):
                leaguec = 0
                print("E: Back to Hockey League Tool")
                while (leaguec < len(hockeyarray['leaguelist'])):
                    lshn = hockeyarray['leaguelist'][leaguec]
                    print(str(leaguec)+": " +
                          hockeyarray[lshn]['leagueinfo']['fullname'])
                    leaguec = leaguec + 1
                HockeyLeaguePreSN = get_user_input(
                    "Enter Hockey League number: ")
                if (HockeyLeaguePreSN.upper() != "E" and not HockeyLeaguePreSN.isdigit()):
                    print("ERROR: Invalid Command")
                    HockeyLeaguePreSN = "E"
                elif (HockeyLeaguePreSN.upper() != "E" and HockeyLeaguePreSN.isdigit() and (int(HockeyLeaguePreSN) > len(hockeyarray['leaguelist']) or int(HockeyLeaguePreSN) < 0)):
                    print("ERROR: Invalid Command")
                    HockeyLeaguePreSN = "E"
                elif (HockeyLeaguePreSN.upper() != "E" and int(HockeyLeaguePreSN) < len(hockeyarray['leaguelist']) and int(HockeyLeaguePreSN) > -1):
                    HockeyLeagueIntSN = int(HockeyLeaguePreSN)
                    HockeyLeagueOldSN = hockeyarray['leaguelist'][HockeyLeagueIntSN]
                    HockeyLeagueSN = get_user_input(
                        "Enter Hockey League short name: ")
                    if (HockeyLeagueSN in hockeyarray['leaguelist']):
                        print("ERROR: Hockey League with that short name exists")
                    elif (HockeyLeagueSN not in hockeyarray['leaguelist']):
                        HockeyLeagueFN = get_user_input(
                            "Enter Hockey League full name: ")
                        HockeyLeagueCSN = get_user_input(
                            "Enter Hockey League country short name: ")
                        HockeyLeagueCFN = get_user_input(
                            "Enter Hockey League country full name: ")
                        HockeyLeagueSD = get_user_input(
                            "Enter Hockey League start date: ")
                        HockeyLeaguePOF = get_user_input(
                            "Enter Hockey League playoff format: ")
                        HockeyLeagueOT = get_user_input(
                            "Enter Hockey League ordertype: ")
                        HockeyLeagueHC = get_user_input(
                            "Does Hockey League have conferences: ")
                        HockeyLeagueHD = get_user_input(
                            "Does Hockey League have divisions: ")
                        hockeyarray = pyhockeystats.ReplaceHockeyLeagueFromArray(
                            hockeyarray, HockeyLeagueOldSN, HockeyLeagueSN, HockeyLeagueFN, HockeyLeagueCSN, HockeyLeagueCFN, HockeyLeagueSD, HockeyLeaguePOF, HockeyLeagueOT, HockeyLeagueHC, HockeyLeagueHD)
            elif (submenuact.upper() == "E"):
                sub_keep_loop = False
    elif (menuact == "2" and len(hockeyarray['leaguelist']) <= 0):
        print("ERROR: There are no Hockey Leagues")
    elif (menuact == "2" and len(hockeyarray['leaguelist']) > 0):
        sub_keep_loop = True
        while (sub_keep_loop):
            leaguec = 0
            print("E: Back to Main Menu")
            while (leaguec < len(hockeyarray['leaguelist'])):
                lshn = hockeyarray['leaguelist'][leaguec]
                print(str(leaguec)+": " +
                      hockeyarray[lshn]['leagueinfo']['fullname'])
                leaguec = leaguec + 1
            HockeyLeaguePreSN = get_user_input("Enter Hockey League number: ")
            if (HockeyLeaguePreSN.upper() != "E" and not HockeyLeaguePreSN.isdigit()):
                print("ERROR: Invalid Command")
                HockeyLeaguePreSN = "E"
            elif (HockeyLeaguePreSN.upper() != "E" and HockeyLeaguePreSN.isdigit() and (int(HockeyLeaguePreSN) > len(hockeyarray['leaguelist']) or int(HockeyLeaguePreSN) < 0)):
                print("ERROR: Invalid Command")
                HockeyLeaguePreSN = "E"
            elif (HockeyLeaguePreSN.upper() != "E" and int(HockeyLeaguePreSN) < len(hockeyarray['leaguelist']) and int(HockeyLeaguePreSN) > -1):
                HockeyLeagueIntSN = int(HockeyLeaguePreSN)
                HockeyLeagueSN = hockeyarray['leaguelist'][HockeyLeagueIntSN]
                if (hockeyarray[HockeyLeagueSN]['leagueinfo']['conferences'] == "no"):
                    print("ERROR: Hockey League can not have any conferences")
                    HockeyLeaguePreSN = "E"
                elif (hockeyarray[HockeyLeagueSN]['leagueinfo']['conferences'] == "yes"):
                    sub_sub_keep_loop = True
                    while (sub_sub_keep_loop):
                        subsubmenuact = get_user_input(
                            "E: Back to Main Menu\n1: Add Hockey Conference\n2: Remove Hockey Conference\n3: Edit Hockey Conference\nWhat do you want to do? ")
                        if (subsubmenuact.upper() != "E" and not subsubmenuact.isdigit()):
                            print("ERROR: Invalid Command")
                            subsubmenuact = ""
                        elif (subsubmenuact.upper() != "E" and subsubmenuact.isdigit() and (int(subsubmenuact) > 3 or int(subsubmenuact) < 1)):
                            print("ERROR: Invalid Command")
                            subsubmenuact = ""
                        elif (subsubmenuact.upper() == "1"):
                            HockeyConferenceCN = get_user_input(
                                "Enter Hockey Conference name: ")
                            if (HockeyConferenceCN in hockeyarray[HockeyLeagueSN]['conferencelist']):
                                print(
                                    "ERROR: Hockey Conference with that name exists")
                            elif (HockeyConferenceCN not in hockeyarray[HockeyLeagueSN]['conferencelist']):
                                HockeyConferenceCPFN = get_user_input(
                                    "Enter Hockey Conference prefix: ")
                                HockeyConferenceCSFN = get_user_input(
                                    "Enter Hockey Conference suffix: ")
                                hockeyarray = pyhockeystats.AddHockeyConferenceToArray(
                                    hockeyarray, HockeyLeagueSN, HockeyConferenceCN, HockeyConferenceCPFN, HockeyConferenceCSFN)
                        elif (subsubmenuact == "2" and (len(hockeyarray['leaguelist']) <= 0 or len(hockeyarray[HockeyLeagueSN]['conferencelist']) <= 0)):
                            print("ERROR: There are no Hockey Conferences to delete")
                        elif (subsubmenuact == "2" and len(hockeyarray['leaguelist']) > 0 and len(hockeyarray[HockeyLeagueSN]['conferencelist']) > 0):
                            conferencec = 0
                            print("E: Back to Hockey Conference Tool")
                            while (conferencec < len(hockeyarray[HockeyLeagueSN]['conferencelist'])):
                                lshn = hockeyarray[HockeyLeagueSN]['conferencelist'][conferencec]
                                print(str(
                                    conferencec)+": "+hockeyarray[HockeyLeagueSN]['quickinfo']['conferenceinfo'][lshn]['fullname'])
                                conferencec = conferencec + 1
                            HockeyConferencePreCN = get_user_input(
                                "Enter Hockey Conference number: ")
                            if (HockeyConferencePreCN.upper() != "E" and not HockeyConferencePreCN.isdigit()):
                                print("ERROR: Invalid Command")
                                HockeyConferencePreCN = "E"
                            elif (HockeyConferencePreCN.upper() != "E" and HockeyConferencePreCN.isdigit() and (int(HockeyConferencePreCN) > 6 or int(HockeyConferencePreCN) < 0)):
                                print("ERROR: Invalid Command")
                                HockeyConferencePreCN = "E"
                            elif (HockeyConferencePreCN.upper() != "E" and int(HockeyConferencePreCN) < len(hockeyarray[HockeyLeagueSN]['conferencelist']) and int(HockeyConferencePreCN) > -1):
                                HockeyConferenceIntCN = int(
                                    HockeyConferencePreCN)
                                HockeyConferenceCN = hockeyarray[HockeyLeagueSN]['conferencelist'][HockeyConferenceIntCN]
                                hockeyarray = pyhockeystats.RemoveHockeyConferenceFromArray(
                                    hockeyarray, HockeyLeagueSN, HockeyConferenceCN)
                        elif (subsubmenuact == "3" and (len(hockeyarray['leaguelist']) <= 0 or len(hockeyarray[HockeyLeagueSN]['conferencelist']) <= 0)):
                            print("ERROR: There are no Hockey Conferences to edit")
                        elif (subsubmenuact == "3" and len(hockeyarray['leaguelist']) > 0 and len(hockeyarray[HockeyLeagueSN]['conferencelist']) > 0):
                            conferencec = 0
                            print("E: Back to Hockey Conference Tool")
                            while (conferencec < len(hockeyarray[HockeyLeagueSN]['conferencelist'])):
                                lshn = hockeyarray[HockeyLeagueSN]['conferencelist'][conferencec]
                                print(str(
                                    conferencec)+": "+hockeyarray[HockeyLeagueSN]['quickinfo']['conferenceinfo'][lshn]['fullname'])
                                conferencec = conferencec + 1
                            HockeyConferencePreCN = get_user_input(
                                "Enter Hockey Conference number: ")
                            if (HockeyConferencePreCN.upper() != "E" and not HockeyConferencePreCN.isdigit()):
                                print("ERROR: Invalid Command")
                                HockeyConferencePreCN = "E"
                            elif (HockeyConferencePreCN.upper() != "E" and HockeyConferencePreCN.isdigit() and (int(HockeyConferencePreCN) > 6 or int(HockeyConferencePreCN) < 0)):
                                print("ERROR: Invalid Command")
                                HockeyConferencePreCN = "E"
                            elif (HockeyConferencePreCN.upper() != "E" and int(HockeyConferencePreCN) < len(hockeyarray[HockeyLeagueSN]['conferencelist']) and int(HockeyConferencePreCN) > -1):
                                HockeyConferenceIntCN = int(
                                    HockeyConferencePreCN)
                                HockeyConferenceOldCN = hockeyarray[HockeyLeagueSN][
                                    'conferencelist'][HockeyConferenceIntCN]
                                HockeyConferenceCN = get_user_input(
                                    "Enter Hockey Conference name: ")
                                if (HockeyConferenceCN in hockeyarray[HockeyLeagueSN]['conferencelist']):
                                    print(
                                        "ERROR: Hockey Conference with that name exists")
                                elif (HockeyConferenceCN not in hockeyarray[HockeyLeagueSN]['conferencelist']):
                                    HockeyConferenceCPFN = get_user_input(
                                        "Enter Hockey Conference prefix: ")
                                    HockeyConferenceCSFN = get_user_input(
                                        "Enter Hockey Conference suffix: ")
                                hockeyarray = pyhockeystats.ReplaceHockeyConferencFromArray(
                                    hockeyarray, HockeyLeagueSN, HockeyConferenceOldCN, HockeyConferenceCN, HockeyConferenceCPFN, HockeyConferenceCSFN)
                        elif (subsubmenuact.upper() == "E"):
                            sub_sub_keep_loop = False
            elif (HockeyLeaguePreSN.upper() == "E"):
                sub_keep_loop = False
    elif (menuact == "3" and len(hockeyarray['leaguelist']) <= 0):
        print("ERROR: There are no Hockey Leagues")
    elif (menuact == "3" and len(hockeyarray['leaguelist']) > 0):
        sub_keep_loop = True
        while (sub_keep_loop):
            leaguec = 0
            print("E: Back to Main Menu")
            while (leaguec < len(hockeyarray['leaguelist'])):
                lshn = hockeyarray['leaguelist'][leaguec]
                print(str(leaguec)+": " +
                      hockeyarray[lshn]['leagueinfo']['fullname'])
                leaguec = leaguec + 1
            HockeyLeaguePreSN = get_user_input("Enter Hockey League number: ")
            if (HockeyLeaguePreSN.upper() != "E" and not HockeyLeaguePreSN.isdigit()):
                print("ERROR: Invalid Command")
                HockeyLeaguePreSN = "E"
            elif (HockeyLeaguePreSN.upper() != "E" and HockeyLeaguePreSN.isdigit() and (int(HockeyLeaguePreSN) > len(hockeyarray['leaguelist']) or int(HockeyLeaguePreSN) < 0)):
                print("ERROR: Invalid Command")
                HockeyLeaguePreSN = "E"
            elif (HockeyLeaguePreSN.upper() != "E" and int(HockeyLeaguePreSN) < len(hockeyarray['leaguelist']) and int(HockeyLeaguePreSN) > -1):
                HockeyLeagueIntSN = int(HockeyLeaguePreSN)
                HockeyLeagueSN = hockeyarray['leaguelist'][HockeyLeagueIntSN]
                if (hockeyarray[HockeyLeagueSN]['leagueinfo']['divisions'] == "no"):
                    print("ERROR: Hockey League can not have any divisions")
                    HockeyLeaguePreSN = "E"
                elif (hockeyarray[HockeyLeagueSN]['leagueinfo']['divisions'] == "yes"):
                    if (hockeyarray[HockeyLeagueSN]['leagueinfo']['conferences'] == "no"):
                        sub_sub_keep_loop = True
                        while (sub_sub_keep_loop):
                            submenuact = get_user_input(
                                "E: Back to Main Menu\n1: Add Hockey Division\n2: Remove Hockey Division\n3: Edit Hockey Division\nWhat do you want to do? ")
                            if (submenuact.upper() != "E" and not submenuact.isdigit()):
                                print("ERROR: Invalid Command")
                                submenuact = ""
                            elif (submenuact.upper() != "E" and submenuact.isdigit() and (int(submenuact) > 3 or int(submenuact) < 1)):
                                print("ERROR: Invalid Command")
                                submenuact = ""
                            elif (submenuact.upper() == "1"):
                                HockeyDivisionDN = get_user_input(
                                    "Enter Hockey Division name: ")
                                if (HockeyDivisionDN in hockeyarray[HockeyLeagueSN]['']['divisionlist']):
                                    print(
                                        "ERROR: Hockey Division with that name exists")
                                elif (HockeyDivisionDN not in hockeyarray[HockeyLeagueSN]['']['divisionlist']):
                                    HockeyDivisionDPFN = get_user_input(
                                        "Enter Hockey Division prefix: ")
                                    HockeyDivisionDSFN = get_user_input(
                                        "Enter Hockey Division suffix: ")
                                hockeyarray = pyhockeystats.AddHockeyDivisionToArray(
                                    hockeyarray, HockeyLeagueSN, HockeyDivisionDN, "", HockeyDivisionDPFN, HockeyDivisionDSFN)
                            elif (submenuact.upper() == "2"):
                                divisionc = 0
                                print("E: Back to Hockey Division Tool")
                                while (divisionc < len(hockeyarray[HockeyLeagueSN]['']['divisionlist'])):
                                    lshn = hockeyarray[HockeyLeagueSN]['']['divisionlist'][divisionc]
                                    print(str(
                                        divisionc)+": "+hockeyarray[HockeyLeagueSN]['quickinfo']['divisioninfo'][lshn]['fullname'])
                                    divisionc = divisionc + 1
                                HockeyDivisionPreDN = get_user_input(
                                    "Enter Hockey Division number: ")
                                if (HockeyDivisionPreDN.upper() != "E" and not HockeyDivisionPreDN.isdigit()):
                                    print("ERROR: Invalid Command")
                                    HockeyDivisionPreDN = "E"
                                elif (HockeyDivisionPreDN.upper() != "E" and HockeyDivisionPreDN.isdigit() and (int(HockeyDivisionPreDN) > 6 or int(HockeyDivisionPreDN) < 0)):
                                    print("ERROR: Invalid Command")
                                    HockeyDivisionPreDN = "E"
                                elif (HockeyDivisionPreDN.upper() != "E" and int(HockeyDivisionPreDN) < len(hockeyarray[HockeyLeagueSN]['']['divisionlist']) and int(HockeyDivisionPreDN) > -1):
                                    HockeyDivisionIntCN = int(
                                        HockeyDivisionPreDN)
                                    HockeyDivisionDN = hockeyarray[HockeyLeagueSN]['']['divisionlist'][HockeyDivisionIntCN]
                                    hockeyarray = pyhockeystats.RemoveHockeyDivisionFromArray(
                                        hockeyarray, HockeyLeagueSN, HockeyDivisionDN, "")
                            elif (submenuact.upper() == "E"):
                                sub_sub_keep_loop = False
                    elif (hockeyarray[HockeyLeagueSN]['leagueinfo']['conferences'] == "yes"):
                        sub_sub_keep_loop = True
                        while (sub_sub_keep_loop):
                            conferencec = 0
                            print("E: Back to Main Menu")
                            while (conferencec < len(hockeyarray[HockeyLeagueSN]['conferencelist'])):
                                lshn = hockeyarray[HockeyLeagueSN]['conferencelist'][conferencec]
                                print(str(
                                    conferencec)+": "+hockeyarray[HockeyLeagueSN]['quickinfo']['conferenceinfo'][lshn]['fullname'])
                                conferencec = conferencec + 1
                            HockeyConferencePreSN = get_user_input(
                                "Enter Hockey Conference number: ")
                            if (HockeyConferencePreSN.upper() != "E" and not HockeyConferencePreSN.isdigit()):
                                print("ERROR: Invalid Command")
                                HockeyConferencePreSN = "E"
                            elif (HockeyConferencePreSN.upper() != "E" and HockeyConferencePreSN.isdigit() and (int(HockeyConferencePreSN) > len(hockeyarray[HockeyLeagueSN]['conferencelist']) or int(HockeyConferencePreSN) < 0)):
                                print("ERROR: Invalid Command")
                                HockeyConferencePreSN = "E"
                            elif (HockeyConferencePreSN.upper() != "E" and int(HockeyConferencePreSN) < len(hockeyarray[HockeyLeagueSN]['conferencelist']) and int(HockeyConferencePreSN) > -1):
                                HockeyConferenceIntSN = int(
                                    HockeyConferencePreSN)
                                HockeyConferenceSN = hockeyarray[HockeyLeagueSN]['conferencelist'][HockeyConferenceIntSN]
                                sub_sub_sub_keep_loop = True
                                while (sub_sub_sub_keep_loop):
                                    submenuact = get_user_input(
                                        "E: Back to Main Menu\n1: Add Hockey Division\n2: Remove Hockey Division\n3: Edit Hockey Division\nWhat do you want to do? ")
                                    if (submenuact.upper() != "E" and not submenuact.isdigit()):
                                        print("ERROR: Invalid Command")
                                        submenuact = ""
                                    elif (submenuact.upper() != "E" and submenuact.isdigit() and (int(submenuact) > 3 or int(submenuact) < 1)):
                                        print("ERROR: Invalid Command")
                                        submenuact = ""
                                    elif (submenuact.upper() == "1"):
                                        HockeyDivisionDN = get_user_input(
                                            "Enter Hockey Division name: ")
                                        if (HockeyDivisionDN in hockeyarray[HockeyLeagueSN][HockeyConferenceSN]['divisionlist']):
                                            print(
                                                "ERROR: Hockey Division with that name exists")
                                        elif (HockeyDivisionDN not in hockeyarray[HockeyLeagueSN][HockeyConferenceSN]['divisionlist']):
                                            HockeyDivisionDPFN = get_user_input(
                                                "Enter Hockey Division prefix: ")
                                            HockeyDivisionDSFN = get_user_input(
                                                "Enter Hockey Division suffix: ")
                                        hockeyarray = pyhockeystats.AddHockeyDivisionToArray(
                                            hockeyarray, HockeyLeagueSN, HockeyDivisionDN, HockeyConferenceSN, HockeyDivisionDPFN, HockeyDivisionDSFN)
                                    elif (submenuact.upper() == "2"):
                                        divisionc = 0
                                        print("E: Back to Hockey Division Tool")
                                        while (divisionc < len(hockeyarray[HockeyLeagueSN][HockeyConferenceSN]['divisionlist'])):
                                            lshn = hockeyarray[HockeyLeagueSN][HockeyConferenceSN]['divisionlist'][divisionc]
                                            print(str(
                                                divisionc)+": "+hockeyarray[HockeyLeagueSN]['quickinfo']['divisioninfo'][lshn]['fullname'])
                                            divisionc = divisionc + 1
                                        HockeyDivisionPreDN = get_user_input(
                                            "Enter Hockey Division number: ")
                                        if (HockeyDivisionPreDN.upper() != "E" and not HockeyDivisionPreDN.isdigit()):
                                            print("ERROR: Invalid Command")
                                            HockeyDivisionPreDN = "E"
                                        elif (HockeyDivisionPreDN.upper() != "E" and HockeyDivisionPreDN.isdigit() and (int(HockeyDivisionPreDN) > 6 or int(HockeyDivisionPreDN) < 0)):
                                            print("ERROR: Invalid Command")
                                            HockeyDivisionPreDN = "E"
                                        elif (HockeyDivisionPreDN.upper() != "E" and int(HockeyDivisionPreDN) < len(hockeyarray[HockeyLeagueSN][HockeyConferenceSN]['divisionlist']) and int(HockeyDivisionPreDN) > -1):
                                            HockeyDivisionIntCN = int(
                                                HockeyDivisionPreDN)
                                            HockeyDivisionDN = hockeyarray[HockeyLeagueSN][
                                                HockeyConferenceSN]['divisionlist'][HockeyDivisionIntCN]
                                            hockeyarray = pyhockeystats.RemoveHockeyDivisionFromArray(
                                                hockeyarray, HockeyLeagueSN, HockeyDivisionDN, HockeyConferenceSN)
                                    elif (submenuact.upper() == "E"):
                                        sub_sub_sub_keep_loop = False
                            elif (HockeyConferencePreSN.upper() == "E"):
                                sub_sub_keep_loop = False
            elif (HockeyLeaguePreSN.upper() == "E"):
                sub_keep_loop = False
    elif (menuact == "4" and len(hockeyarray['leaguelist']) <= 0):
        print("ERROR: There are no Hockey Leagues")
    elif (menuact == "4" and len(hockeyarray['leaguelist']) > 0):
        sub_keep_loop = True
        while (sub_keep_loop):
            submenuact = get_user_input(
                "E: Back to Main Menu\n1: Add Hockey Team\n2: Remove Hockey Team\n3: Edit Hockey Team\nWhat do you want to do? ")
            if (submenuact.upper() != "E" and not submenuact.isdigit()):
                print("ERROR: Invalid Command")
                submenuact = ""
            elif (submenuact.upper() != "E" and submenuact.isdigit() and (int(submenuact) > 3 or int(submenuact) < 1)):
                print("ERROR: Invalid Command")
                submenuact = ""
            elif (submenuact.upper() == "E"):
                sub_keep_loop = False
            print("ERROR: Sorry Command not Implemented yet")
            raise NotImplementedError
    elif (menuact == "5" and len(hockeyarray['leaguelist']) <= 0):
        print("ERROR: There are no Hockey Leagues")
    elif (menuact == "5" and len(hockeyarray['leaguelist']) > 0):
        sub_keep_loop = True
        while (sub_keep_loop):
            submenuact = get_user_input(
                "E: Back to Main Menu\n1: Add Hockey Arena\n2: Remove Hockey Arena\n3: Edit Hockey Arena\nWhat do you want to do? ")
            if (submenuact.upper() != "E" and not submenuact.isdigit()):
                print("ERROR: Invalid Command")
                submenuact = ""
            elif (submenuact.upper() != "E" and submenuact.isdigit() and (int(submenuact) > 3 or int(submenuact) < 1)):
                print("ERROR: Invalid Command")
                submenuact = ""
            elif (submenuact.upper() == "E"):
                sub_keep_loop = False
            print("ERROR: Sorry Command not Implemented yet")
            raise NotImplementedError
    elif (menuact == "6" and len(hockeyarray['leaguelist']) <= 0):
        print("ERROR: There are no Hockey Leagues")
    elif (menuact == "6" and len(hockeyarray['leaguelist']) > 0):
        sub_keep_loop = True
        while (sub_keep_loop):
            submenuact = get_user_input(
                "E: Back to Main Menu\n1: Add Hockey Game\n2: Remove Hockey Game\n3: Edit Hockey Game\nWhat do you want to do? ")
            if (submenuact.upper() != "E" and not submenuact.isdigit()):
                print("ERROR: Invalid Command")
                submenuact = ""
            elif (submenuact.upper() != "E" and submenuact.isdigit() and (int(submenuact) > 3 or int(submenuact) < 1)):
                print("ERROR: Invalid Command")
                submenuact = ""
            elif (submenuact.upper() == "E"):
                sub_keep_loop = False
            print("ERROR: Sorry Command not Implemented yet")
            raise NotImplementedError
    elif (menuact == "7"):
        sub_keep_loop = True
        while (sub_keep_loop):
            submenuact = get_user_input(
                "E: Back to Main Menu\n1: Empty Hockey Database\n2: Import Hockey Database From File\n3: Export Hockey Database to File\nWhat do you want to do? ")
            if (submenuact.upper() != "E" and not submenuact.isdigit()):
                print("ERROR: Invalid Command")
                submenuact = ""
            elif (submenuact.upper() != "E" and submenuact.isdigit() and (int(submenuact) > 3 or int(submenuact) < 1)):
                print("ERROR: Invalid Command")
                submenuact = ""
            elif (submenuact == "1"):
                HockeyDatabaseFN = get_user_input(
                    "Enter Hockey Database File Name For Output: ")
                hockeyarray = pyhockeystats.CreateHockeyArray(HockeyDatabaseFN)
            elif (submenuact == "2"):
                HockeyDatabaseFN = get_user_input(
                    "Enter Hockey Database File Name For Import: ")
                ext = os.path.splitext(HockeyDatabaseFN)[-1].lower()
                if (ext in extensions):
                    if (ext == ".xml" and pyhockeystats.CheckXMLFile(HockeyDatabaseFN)):
                        hockeyarray = pyhockeystats.MakeHockeyArrayFromHockeyXML(
                            HockeyDatabaseFN)
                    elif ((ext == ".db3" or ext == ".db" or ext == ".sdb" or ext == ".sqlite" or ext == ".sqlite3") and pyhockeystats.CheckSQLiteDatabase(HockeyDatabaseFN)):
                        hockeyarray = pyhockeystats.MakeHockeyArrayFromHockeyDatabase(
                            HockeyDatabaseFN)
                    elif (ext == ".sql"):
                        hockeyarray = pyhockeystats.MakeHockeyArrayFromHockeySQL(
                            HockeyDatabaseFN)
                    elif (ext == ".json"):
                        hockeyarray = pyhockeystats.MakeHockeyArrayFromHockeyJSON(
                            HockeyDatabaseFN)
                    else:
                        print("ERROR: Invalid Command")
                    if (pyhockeystats.CheckHockeySQLiteArray(hockeyarray)):
                        hockeyarray = pyhockeystats.MakeHockeyArrayFromHockeySQLiteArray(
                            hockeyarray)
                    if (not pyhockeystats.CheckHockeyArray(hockeyarray)):
                        print("ERROR: Invalid Command")
            elif (submenuact.upper() == "3"):
                sub_sub_keep_loop = True
                while (sub_sub_keep_loop):
                    subsubmenuact = get_user_input(
                        " E: Back to Hockey Database Tool\n 1: Export Hockey Database to Hockey XML\n 2: Export Hockey Database to Hockey SGML\n 3: Export Hockey Database to Hockey JSON\n 4: Export Hockey Database to Hockey YAML\n 5: Export Hockey Database to Hockey Py\n 6: Export Hockey Database to Hockey Py Alt\n 7: Export Hockey Database to Hockey Py OOP\n 8: Export Hockey Database to Hockey Py OOP Alt\n 9: Export Hockey Database to Hockey SQL\n10: Export Hockey Database to Hockey Database File\nWhat do you want to do? ")
                    if (subsubmenuact.upper() != "E" and not subsubmenuact.isdigit()):
                        print("ERROR: Invalid Command")
                        subsubmenuact = "E"
                    elif (subsubmenuact.upper() != "E" and subsubmenuact.isdigit() and (int(subsubmenuact) > 6 or int(subsubmenuact) < 1)):
                        print("ERROR: Invalid Command")
                        subsubmenuact = "E"
                    elif (subsubmenuact == "1"):
                        HockeyDatabaseFN = get_user_input(
                            "Enter Hockey Database XML File Name to Export: ")
                        pyhockeystats.MakeHockeyXMLFileFromHockeyArray(
                            hockeyarray, HockeyDatabaseFN)
                    elif (subsubmenuact == "2"):
                        HockeyDatabaseFN = get_user_input(
                            "Enter Hockey Database SGML File Name to Export: ")
                        pyhockeystats.MakeHockeySGMLFileFromHockeyArray(
                            hockeyarray, HockeyDatabaseFN)
                    elif (subsubmenuact == "3"):
                        HockeyDatabaseFN = get_user_input(
                            "Enter Hockey Database JSON File Name to Export: ")
                        pyhockeystats.MakeHockeyJSONFileFromHockeyArray(
                            hockeyarray, HockeyDatabaseFN)
                    elif (subsubmenuact == "4"):
                        HockeyDatabaseFN = get_user_input(
                            "Enter Hockey Database YAML File Name to Export: ")
                        pyhockeystats.MakeHockeyYAMLFileFromHockeyArray(
                            hockeyarray, HockeyDatabaseFN)
                    elif (subsubmenuact == "5"):
                        HockeyDatabaseFN = get_user_input(
                            "Enter Hockey Database Python File Name to Export: ")
                        pyhockeystats.MakeHockeyPythonFileFromHockeyArray(
                            hockeyarray, HockeyDatabaseFN)
                    elif (subsubmenuact == "6"):
                        HockeyDatabaseFN = get_user_input(
                            "Enter Hockey Database Python File Name to Export: ")
                        pyhockeystats.MakeHockeyPythonAltFileFromHockeyArray(
                            hockeyarray, HockeyDatabaseFN)
                    elif (subsubmenuact == "7"):
                        HockeyDatabaseFN = get_user_input(
                            "Enter Hockey Database Python File Name to Export: ")
                        pyhockeystats.MakeHockeyPythonOOPFileFromHockeyArray(
                            hockeyarray, HockeyDatabaseFN)
                    elif (subsubmenuact == "8"):
                        HockeyDatabaseFN = get_user_input(
                            "Enter Hockey Database Python File Name to Export: ")
                        pyhockeystats.MakeHockeyPythonOOPAltFileFromHockeyArray(
                            hockeyarray, HockeyDatabaseFN)
                    elif (subsubmenuact == "9"):
                        HockeyDatabaseFN = get_user_input(
                            "Enter Hockey Database SQL File Name to Export: ")
                        pyhockeystats.MakeHockeySQLFileFromHockeyArray(
                            hockeyarray, HockeyDatabaseFN)
                    elif (subsubmenuact == "10"):
                        HockeyDatabaseFN = get_user_input(
                            "Enter Hockey Database File Name to Export: ")
                        pyhockeystats.MakeHockeyDatabaseFromHockeyArray(
                            hockeyarray, HockeyDatabaseFN)
                    elif (subsubmenuact.upper() == "E"):
                        sub_sub_keep_loop = False
            elif (submenuact.upper() == "E"):
                sub_keep_loop = False
    if (menuact.upper() == "E"):
        keep_loop = False
        