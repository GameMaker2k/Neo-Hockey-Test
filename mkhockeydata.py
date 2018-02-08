#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2018 Cool Dude 2k - http://idb.berlios.de/
    Copyright 2018 Game Maker 2k - http://intdb.sourceforge.net/
    Copyright 2018 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: mkhockeydata.py - Last Update: 2/7/2018 Ver. 0.0.3 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals;
import sys, os, libhockeydata, argparse, datetime;

__project__ = libhockeydata.__project__;
__program_name__ = libhockeydata.__program_name__;
__project_url__ = libhockeydata.__project_url__;
__version_info__ = libhockeydata.__version_info__;
__version_date_info__ = libhockeydata.__version_date_info__;
__version_date__ = libhockeydata.__version_date__;
__version_date_plusrc__ = libhockeydata.__version_date_plusrc__
__version__ = libhockeydata.__version__;
__version_date_plusrc__ = libhockeydata.__version_date_plusrc__;

getactlist = ["mkhockeyxmlfile", "mkhockeydatabase", "mkhockeypyfromdatabase", "mkhockeypyfromxmlfile", "mkhockeysqlfromdatabase", "mkhockeysqlfromxmlfile", "help", "h"];
getactstr = "Actions:";
for getactsublist in getactlist:
 getactstr = getactstr+" "+getactsublist;
curaction = "mkhockeydatabase";
cursaction = os.path.splitext(os.path.basename(sys.argv[0]))[0];
cursactionspt = list(cursaction.split("-"));
if(len(cursactionspt)<=1):
 cursaction = cursactionspt[0];
if(len(cursactionspt)>1):
 for cursactionact in cursactionspt:
  if(cursactionact in getactlist):
   cursaction = cursactionact;
   break;
if(cursaction in getactlist):
 curaction = cursaction;
if(len(sys.argv)>=2):
 if(sys.argv[1] not in getactlist):
  curaction = "mkhockeydatabase";
 if(cursaction in getactlist):
  curaction = cursaction;
 if(len(sys.argv)>1):
  for curargact in sys.argv:
   if(curargact in getactlist):
    curaction = curargact;
    break;

if(curaction==getactlist[6] or curaction==getactlist[7]):
 print(getactstr);

if(curaction==getactlist[0]):
 argparser = argparse.ArgumentParser(description="convert hockey sqlite database to hockey xml file", conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-f", "--file", default="./hockeydata.db3", help="sqlite database to convert");
 argparser.add_argument("-o", "--outfile", default=None, help="xml file to output");
 argparser.add_argument("-d", "--date", default=str(datetime.datetime.now().year-1)+"1001", help="start of hockey season in YYYYMMDD format");
 getargs = argparser.parse_args();
 libhockeydata.MakeHockeyXMLFileFromHockeyDatabase(getargs.file, getargs.date, getargs.outfile);

if(curaction==getactlist[1]):
 argparser = argparse.ArgumentParser(description="convert hockey xml file to hockey sqlite database", conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-f", "--file", default="./hockeydata.xml", help="xml file to convert");
 argparser.add_argument("-o", "--outfile", default=None, help="sqlite database to output");
 getargs = argparser.parse_args();
 libhockeydata.MakeHockeyDatabaseFromHockeyXML(getargs.file, getargs.outfile);

if(curaction==getactlist[2]):
 argparser = argparse.ArgumentParser(description="convert hockey sqlite database to hockey python file", conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-f", "--file", default="./hockeydata.db3", help="sqlite database to convert");
 argparser.add_argument("-o", "--outfile", default=None, help="python file to output");
 argparser.add_argument("-d", "--date", default=str(datetime.datetime.now().year-1)+"1001", help="start of hockey season in YYYYMMDD format");
 getargs = argparser.parse_args();
 libhockeydata.MakeHockeyPythonFileFromHockeyDatabase(getargs.file, getargs.date, getargs.outfile);

if(curaction==getactlist[3]):
 argparser = argparse.ArgumentParser(description="convert hockey xml file to hockey python file", conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-f", "--file", default="./hockeydata.xml", help="xml file to convert");
 argparser.add_argument("-o", "--outfile", default=None, help="python file to output");
 getargs = argparser.parse_args();
 libhockeydata.MakeHockeyPythonFileFromHockeyXML(getargs.file, getargs.outfile);

if(curaction==getactlist[4]):
 argparser = argparse.ArgumentParser(description="convert hockey sqlite database to hockey sql dump file", conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-f", "--file", default="./hockeydata.db3", help="sqlite database to convert");
 argparser.add_argument("-o", "--outfile", default=None, help="sql dump file to output");
 getargs = argparser.parse_args();
 libhockeydata.MakeHockeySQLFileFromHockeyDatabase(getargs.file, getargs.outfile);

if(curaction==getactlist[5]):
 argparser = argparse.ArgumentParser(description="convert hockey xml file to hockey sql dump file", conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-f", "--file", default="./hockeydata.xml", help="xml file to convert");
 argparser.add_argument("-o", "--outfile", default=None, help="sql dump file to output");
 getargs = argparser.parse_args();
 libhockeydata.MakeHockeySQLFileFromHockeyXML(getargs.file, getargs.outfile);
