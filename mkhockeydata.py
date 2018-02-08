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

    $FileInfo: mkhockeydata.py - Last Update: 2/8/2018 Ver. 0.0.4 RC 1 - Author: cooldude2k $
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

getactlist = ["mkhockeyxmlfile", "mkhockeyxmlfromsql", "mkhockeydatabase", "mkhockeydatabasefromsql", "mkhockeypyfromdatabase", "mkhockeypyfromxmlfile", "mkhockeysqlfromdatabase", "mkhockeysqlfromxmlfile", "help", "h"];
getactdesc = ["convert hockey sqlite database to hockey xml file", "convert hockey sql dump file to hockey xml file", "convert hockey sqlite database to hockey xml file", "convert hockey xml file to hockey sqlite database", "convert hockey sql dump file to sqlite database", "convert hockey sqlite database to hockey python file", "convert hockey xml file to hockey python file", "convert hockey sqlite database to hockey sql dump file", "convert hockey xml file to hockey sql dump file"];
gethelplist = ["mkhockeyxmlfile", "mkhockeyxmlfromsql", "mkhockeydatabase", "mkhockeydatabasefromsql", "mkhockeypyfromdatabase", "mkhockeypyfromxmlfile", "mkhockeysqlfromdatabase", "mkhockeysqlfromxmlfile", "help"];
getactstr = "Actions: ";
for getactsublist, getactsubdesc in zip(gethelplist, getactdesc):
 getactstr = getactstr+"\n"+getactsublist+": "+getactsubdesc+" ";
getactstr = getactstr.strip();
curaction = "help";
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
  curaction = "help";
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
 argparser = argparse.ArgumentParser(description=getactdesc[0], conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-i", "-f", "--infile", default="./hockeydata.db3", help="sqlite database to convert");
 argparser.add_argument("-o", "--outfile", default=None, help="xml file to output");
 argparser.add_argument("-d", "--date", default=str(datetime.datetime.now().year-1)+"1001", help="start of hockey season in YYYYMMDD format");
 getargs = argparser.parse_args();
 libhockeydata.MakeHockeyXMLFileFromHockeyDatabase(getargs.infile, getargs.date, getargs.outfile);

if(curaction==getactlist[1]):
 argparser = argparse.ArgumentParser(description=getactdesc[1], conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-i", "-f", "--infile", default="./hockeydata.sql", help="sql dump file to import");
 argparser.add_argument("-o", "--outfile", default=None, help="xml file to output");
 argparser.add_argument("-d", "--date", default=str(datetime.datetime.now().year-1)+"1001", help="start of hockey season in YYYYMMDD format");
 getargs = argparser.parse_args();
 libhockeydata.MakeHockeyXMLFileFromHockeySQL(getargs.infile, getargs.date, None, getargs.outfile);

if(curaction==getactlist[2]):
 argparser = argparse.ArgumentParser(description=getactdesc[2], conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-i", "-f", "--infile", default="./hockeydata.xml", help="xml file to convert");
 argparser.add_argument("-o", "--outfile", default=None, help="sqlite database to output");
 getargs = argparser.parse_args();
 libhockeydata.MakeHockeyDatabaseFromHockeyXML(getargs.infile, getargs.outfile);

if(curaction==getactlist[3]):
 argparser = argparse.ArgumentParser(description=getactdesc[3], conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-i", "-f", "--infile", default="./hockeydata.sql", help="sql dump file to import");
 argparser.add_argument("-o", "--outfile", default=None, help="sqlite database to output");
 getargs = argparser.parse_args();
 libhockeydata.MakeHockeyDatabaseFromHockeySQL(getargs.infile, getargs.outfile);

if(curaction==getactlist[4]):
 argparser = argparse.ArgumentParser(description=getactdesc[4], conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-i", "-f", "--infile", default="./hockeydata.db3", help="sqlite database to convert");
 argparser.add_argument("-o", "--outfile", default=None, help="python file to output");
 argparser.add_argument("-d", "--date", default=str(datetime.datetime.now().year-1)+"1001", help="start of hockey season in YYYYMMDD format");
 getargs = argparser.parse_args();
 libhockeydata.MakeHockeyPythonFileFromHockeyDatabase(getargs.infile, getargs.date, getargs.outfile);

if(curaction==getactlist[5]):
 argparser = argparse.ArgumentParser(description=getactdesc[5], conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-i", "-f", "--infile", default="./hockeydata.xml", help="xml file to convert");
 argparser.add_argument("-o", "--outfile", default=None, help="python file to output");
 getargs = argparser.parse_args();
 libhockeydata.MakeHockeyPythonFileFromHockeyXML(getargs.infile, getargs.outfile);

if(curaction==getactlist[6]):
 argparser = argparse.ArgumentParser(description=getactdesc[6], conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-i", "-f", "--infile", default="./hockeydata.db3", help="sqlite database to convert");
 argparser.add_argument("-o", "--outfile", default=None, help="sql dump file to output");
 getargs = argparser.parse_args();
 libhockeydata.MakeHockeySQLFileFromHockeyDatabase(getargs.infile, getargs.outfile);

if(curaction==getactlist[7]):
 argparser = argparse.ArgumentParser(description=getactdesc[7], conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-i", "-f", "--infile", default="./hockeydata.xml", help="xml file to convert");
 argparser.add_argument("-o", "--outfile", default=None, help="sql dump file to output");
 getargs = argparser.parse_args();
 libhockeydata.MakeHockeySQLFileFromHockeyXML(getargs.infile, getargs.outfile);
