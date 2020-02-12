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

    $FileInfo: mkhockeydata.py - Last Update: 2/9/2020 Ver. 0.2.0 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals;
import sys, os, libhockeydata, argparse;
import logging as log;

__project__ = libhockeydata.__project__;
__program_name__ = libhockeydata.__program_name__;
__project_url__ = libhockeydata.__project_url__;
__version_info__ = libhockeydata.__version_info__;
__version_date_info__ = libhockeydata.__version_date_info__;
__version_date__ = libhockeydata.__version_date__;
__version_date_plusrc__ = libhockeydata.__version_date_plusrc__;
__version__ = libhockeydata.__version__;

getactlist = ["mkhockeyxmlfile", "mkhockeyxmlfromolddatabase", "mkhockeyxmlfromsql", "mkhockeydatabase", "mkhockeydatabasefromsql", "mkhockeypyfromdatabase", "mkhockeypyfromxmlfile", "mkhockeypyaltfromdatabase", "mkhockeypyaltfromxmlfile", "mkhockeysqlfromdatabase", "mkhockeysqlfromxmlfile", "mkhockeyxmlfileclean", "help", "h", "version", "ver", "v", "mksymlinks", "mksymlink"];
getactdesc = ["convert hockey sqlite database to hockey xml file", "convert old hockey sqlite database to hockey xml file", "convert hockey sql dump file to hockey xml file", "convert hockey xml file to hockey sqlite database", "convert hockey sql dump file to sqlite database", "convert hockey sqlite database to hockey python file", "convert hockey xml file to hockey python file", "convert hockey sqlite database to hockey python alt file", "convert hockey xml file to hockey python alt file", "convert hockey sqlite database to hockey sql dump file", "convert hockey xml file to hockey sql dump file", "cleanup hockey xml files", "show this help page", "get version number of "+__project__, "make symbolic links"];
gethelplist = ["mkhockeyxmlfile", "mkhockeyxmlfromolddatabase", "mkhockeyxmlfromsql", "mkhockeydatabase", "mkhockeydatabasefromsql", "mkhockeypyfromdatabase", "mkhockeypyfromxmlfile", "mkhockeypyaltfromdatabase", "mkhockeypyaltfromxmlfile", "mkhockeysqlfromdatabase", "mkhockeysqlfromxmlfile", "mkhockeyxmlfileclean", "help", "version", "mksymlinks"];
getsymlist = ["mkhockeyxmlfile", "mkhockeyxmlfromolddatabase", "mkhockeyxmlfromsql", "mkhockeydatabase", "mkhockeydatabasefromsql", "mkhockeypyfromdatabase", "mkhockeypyfromxmlfile", "mkhockeypyaltfromdatabase", "mkhockeypyaltfromxmlfile", "mkhockeysqlfromdatabase", "mkhockeysqlfromxmlfile", "mkhockeyxmlfileclean"];
defaction = getactlist[12];
defxmlfile = "./data/hockeydata.xml";
defsdbfile = "./data/hockeydata.db3";
defoldsdbfile = "./data/hockeydata.db3";
defsqlfile = "./data/hockeydata.sql";
getactstr = "Actions: ";
getverstr = __project__+" "+__version__;
for getactsublist, getactsubdesc in zip(gethelplist, getactdesc):
 getactstr = getactstr+"\n"+getactsublist+": "+getactsubdesc+" ";
getactstr = getactstr.strip();
curaction = defaction;
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
  curaction = defaction;
 if(cursaction in getactlist):
  curaction = cursaction;
 if(len(sys.argv)>1):
  for curargact in sys.argv:
   if(curargact in getactlist):
    curaction = curargact;
    break;

if(curaction==getactlist[12] or curaction==getactlist[13]):
 print(getactstr);

if(curaction==getactlist[14] or curaction==getactlist[15] or curaction==getactlist[16]):
 print(getverstr);

if((curaction==getactlist[17] or curaction==getactlist[18])):
 for cursymact in getsymlist:
  curscrpath = os.path.dirname(sys.argv[0]);
  infilename = sys.argv[0];
  infilenameinfo = os.path.splitext(sys.argv[0]);
  if(curscrpath==""):
   curscrpath = ".";
  if(os.sep=="\\"):
   curscrpath = curscrpath.replace(os.sep, "/");
   infilename = infilename.replace(os.sep, "/");
  curscrpath = curscrpath+"/";
  outfilename = curscrpath+cursymact;
  outfileext = str(infilenameinfo[1]).rstrip(".");
  outfilefull = outfilename+outfileext;
  print("'"+outfilefull+"' -> '"+infilename+"'");
  try:
   os.symlink(infilename, outfilefull);
   print("'"+outfilefull+"' -> '"+infilename+"'");
  except OSError:
   break;

if(curaction==getactlist[0]):
 argparser = argparse.ArgumentParser(description=getactdesc[0], conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--ver", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-i", "-f", "--infile", default=os.environ.get('INFILE', defsdbfile), help="sqlite database to convert");
 argparser.add_argument("-o", "-t", "--outfile", default=None, help="xml file to output");
 argparser.add_argument("-V", "-d", "--verbose", action="store_true", help="print various debugging information");
 getargs = argparser.parse_args();
 verboseon = getargs.verbose;
 if('VERBOSE' in os.environ or 'DEBUG' in os.environ):
  verboseon = True;
 if(verboseon==True):
  log.basicConfig(format="%(message)s", stream=sys.stdout, level=log.DEBUG);
 libhockeydata.MakeHockeyXMLFileFromHockeyDatabase(getargs.infile, getargs.outfile, verbose=verboseon);

if(curaction==getactlist[1]):
 argparser = argparse.ArgumentParser(description=getactdesc[1], conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--ver", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-i", "-f", "--infile", default=os.environ.get('INFILE', defoldsdbfile), help="sqlite database to convert");
 argparser.add_argument("-o", "-t", "--outfile", default=os.environ.get('OUTFILE', None), help="xml file to output");
 argparser.add_argument("-V", "-d", "--verbose", action="store_true", help="print various debugging information");
 getargs = argparser.parse_args();
 verboseon = getargs.verbose;
 if('VERBOSE' in os.environ or 'DEBUG' in os.environ):
  verboseon = True;
 if(verboseon==True):
  log.basicConfig(format="%(message)s", stream=sys.stdout, level=log.DEBUG);
 libhockeydata.MakeHockeyXMLFileFromOldHockeyDatabase(getargs.infile, getargs.outfile, verbose=verboseon);

if(curaction==getactlist[2]):
 argparser = argparse.ArgumentParser(description=getactdesc[2], conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--ver", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-i", "-f", "--infile", default=os.environ.get('INFILE', defsqlfile), help="sql dump file to import");
 argparser.add_argument("-o", "-t", "--outfile", default=os.environ.get('OUTFILE', None), help="xml file to output");
 argparser.add_argument("-V", "-d", "--verbose", action="store_true", help="print various debugging information");
 getargs = argparser.parse_args();
 verboseon = getargs.verbose;
 if('VERBOSE' in os.environ or 'DEBUG' in os.environ):
  verboseon = True;
 if(verboseon==True):
  log.basicConfig(format="%(message)s", stream=sys.stdout, level=log.DEBUG);
 libhockeydata.MakeHockeyXMLFileFromHockeySQL(getargs.infile, None, getargs.outfile, verbose=verboseon);

if(curaction==getactlist[3]):
 argparser = argparse.ArgumentParser(description=getactdesc[3], conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--ver", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-i", "-f", "--infile", default=os.environ.get('INFILE', defxmlfile), help="xml file to convert");
 argparser.add_argument("-o", "-t", "--outfile", default=os.environ.get('OUTFILE', None), help="sqlite database to output");
 argparser.add_argument("-V", "-d", "--verbose", action="store_true", help="print various debugging information");
 getargs = argparser.parse_args();
 verboseon = getargs.verbose;
 if('VERBOSE' in os.environ or 'DEBUG' in os.environ):
  verboseon = True;
 if(verboseon==True):
  log.basicConfig(format="%(message)s", stream=sys.stdout, level=log.DEBUG);
 libhockeydata.MakeHockeyDatabaseFromHockeyXML(getargs.infile, getargs.outfile, verbose=verboseon);

if(curaction==getactlist[4]):
 argparser = argparse.ArgumentParser(description=getactdesc[4], conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--ver", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-i", "-f", "--infile", default=os.environ.get('INFILE', defsqlfile), help="sql dump file to import");
 argparser.add_argument("-o", "-t", "--outfile", default=os.environ.get('OUTFILE', None), help="sqlite database to output");
 argparser.add_argument("-V", "-d", "--verbose", action="store_true", help="print various debugging information");
 getargs = argparser.parse_args();
 verboseon = getargs.verbose;
 if('VERBOSE' in os.environ or 'DEBUG' in os.environ):
  verboseon = True;
 if(verboseon==True):
  log.basicConfig(format="%(message)s", stream=sys.stdout, level=log.DEBUG);
 libhockeydata.MakeHockeyDatabaseFromHockeySQL(getargs.infile, getargs.outfile, verbose=verboseon);

if(curaction==getactlist[5]):
 argparser = argparse.ArgumentParser(description=getactdesc[5], conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--ver", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-i", "-f", "--infile", default=os.environ.get('INFILE', defsdbfile), help="sqlite database to convert");
 argparser.add_argument("-o", "-t", "--outfile", default=os.environ.get('OUTFILE', None), help="python file to output");
 argparser.add_argument("-V", "-d", "--verbose", action="store_true", help="print various debugging information");
 getargs = argparser.parse_args();
 verboseon = getargs.verbose;
 if('VERBOSE' in os.environ or 'DEBUG' in os.environ):
  verboseon = True;
 if(verboseon==True):
  log.basicConfig(format="%(message)s", stream=sys.stdout, level=log.DEBUG);
 libhockeydata.MakeHockeyPythonFileFromHockeyDatabase(getargs.infile, getargs.outfile, verbose=verboseon);

if(curaction==getactlist[6]):
 argparser = argparse.ArgumentParser(description=getactdesc[6], conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--ver", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-i", "-f", "--infile", default=os.environ.get('INFILE', defxmlfile), help="xml file to convert");
 argparser.add_argument("-o", "-t", "--outfile", default=os.environ.get('OUTFILE', None), help="python file to output");
 argparser.add_argument("-V", "-d", "--verbose", action="store_true", help="print various debugging information");
 getargs = argparser.parse_args();
 verboseon = getargs.verbose;
 if('VERBOSE' in os.environ or 'DEBUG' in os.environ):
  verboseon = True;
 if(verboseon==True):
  log.basicConfig(format="%(message)s", stream=sys.stdout, level=log.DEBUG);
 libhockeydata.MakeHockeyPythonFileFromHockeyXML(getargs.infile, getargs.outfile, verbose=verboseon);

if(curaction==getactlist[7]):
 argparser = argparse.ArgumentParser(description=getactdesc[5], conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--ver", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-i", "-f", "--infile", default=os.environ.get('INFILE', defsdbfile), help="sqlite database to convert");
 argparser.add_argument("-o", "-t", "--outfile", default=os.environ.get('OUTFILE', None), help="python file to output");
 argparser.add_argument("-V", "-d", "--verbose", action="store_true", help="print various debugging information");
 getargs = argparser.parse_args();
 verboseon = getargs.verbose;
 if('VERBOSE' in os.environ or 'DEBUG' in os.environ):
  verboseon = True;
 if(verboseon==True):
  log.basicConfig(format="%(message)s", stream=sys.stdout, level=log.DEBUG);
 libhockeydata.MakeHockeyAltPythonFileFromHockeyDatabase(getargs.infile, getargs.outfile, verbose=verboseon);

if(curaction==getactlist[8]):
 argparser = argparse.ArgumentParser(description=getactdesc[6], conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--ver", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-i", "-f", "--infile", default=os.environ.get('INFILE', defxmlfile), help="xml file to convert");
 argparser.add_argument("-o", "-t", "--outfile", default=os.environ.get('OUTFILE', None), help="python file to output");
 argparser.add_argument("-V", "-d", "--verbose", action="store_true", help="print various debugging information");
 getargs = argparser.parse_args();
 verboseon = getargs.verbose;
 if('VERBOSE' in os.environ or 'DEBUG' in os.environ):
  verboseon = True;
 if(verboseon==True):
  log.basicConfig(format="%(message)s", stream=sys.stdout, level=log.DEBUG);
 libhockeydata.MakeHockeyAltPythonFileFromHockeyXML(getargs.infile, getargs.outfile, verbose=verboseon);

if(curaction==getactlist[9]):
 argparser = argparse.ArgumentParser(description=getactdesc[7], conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--ver", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-i", "-f", "--infile", default=os.environ.get('INFILE', defsdbfile), help="sqlite database to convert");
 argparser.add_argument("-o", "-t", "--outfile", default=os.environ.get('OUTFILE', None), help="sql dump file to output");
 argparser.add_argument("-V", "-d", "--verbose", action="store_true", help="print various debugging information");
 getargs = argparser.parse_args();
 verboseon = getargs.verbose;
 if('VERBOSE' in os.environ or 'DEBUG' in os.environ):
  verboseon = True;
 if(verboseon==True):
  log.basicConfig(format="%(message)s", stream=sys.stdout, level=log.DEBUG);
 libhockeydata.MakeHockeySQLFileFromHockeyDatabase(getargs.infile, getargs.outfile, verbose=verboseon);

if(curaction==getactlist[10]):
 argparser = argparse.ArgumentParser(description=getactdesc[8], conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--ver", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-i", "-f", "--infile", default=os.environ.get('INFILE', defxmlfile), help="xml file to convert");
 argparser.add_argument("-o", "-t", "--outfile", default=os.environ.get('OUTFILE', None), help="sql dump file to output");
 argparser.add_argument("-V", "-d", "--verbose", action="store_true", help="print various debugging information");
 getargs = argparser.parse_args();
 verboseon = getargs.verbose;
 if('VERBOSE' in os.environ or 'DEBUG' in os.environ):
  verboseon = True;
 if(verboseon==True):
  log.basicConfig(format="%(message)s", stream=sys.stdout, level=log.DEBUG);
 libhockeydata.MakeHockeySQLFileFromHockeyXML(getargs.infile, getargs.outfile, verbose=verboseon);

if(curaction==getactlist[11]):
 argparser = argparse.ArgumentParser(description=getactdesc[9], conflict_handler="resolve", add_help=True);
 argparser.add_argument("-v", "--ver", "--version", action="version", version=__program_name__+" "+__version__);
 argparser.add_argument('action', nargs='?', default=curaction);
 argparser.add_argument("-i", "-f", "--infile", default=os.environ.get('INFILE', defxmlfile), help="xml file to clean");
 argparser.add_argument("-o", "-t", "--outfile", default=os.environ.get('OUTFILE', None), help="clean xml file to output");
 argparser.add_argument("-V", "-d", "--verbose", action="store_true", help="print various debugging information");
 getargs = argparser.parse_args();
 verboseon = getargs.verbose;
 if('VERBOSE' in os.environ or 'DEBUG' in os.environ):
  verboseon = True;
 if(verboseon==True):
  log.basicConfig(format="%(message)s", stream=sys.stdout, level=log.DEBUG);
 if(getargs.outfile is None):
  libhockeydata.MakeHockeyXMLFromHockeyXML(getargs.infile, verbose=verboseon);
 else:
  libhockeydata.MakeHockeyXMLFileFromHockeyXML(getargs.infile, getargs.outfile, verbose=verboseon);
