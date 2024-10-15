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

    $FileInfo: mkhockeydata.py - Last Update: 10/11/2024 Ver. 0.9.2 RC 1 - Author: cooldude2k $
'''

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import argparse
import logging
import os
import shutil
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

__project__ = pyhockeystats.__project__
__program_name__ = pyhockeystats.__program_name__
__project_url__ = pyhockeystats.__project_url__
__version_info__ = pyhockeystats.__version_info__
__version_date_info__ = pyhockeystats.__version_date_info__
__version_date__ = pyhockeystats.__version_date__
__version_date_plusrc__ = pyhockeystats.__version_date_plusrc__
__version__ = pyhockeystats.__version__

getactlist = ["mkhockeyxmlfile", "mkhockeyxmlfromolddatabase", "mkhockeyxmlfromsql", "mkhockeydatabase", "mkhockeydatabasefromsql", "mkhockeypyfromdatabase", "mkhockeypyfromxmlfile", "mkhockeypyaltfromdatabase",
              "mkhockeypyaltfromxmlfile", "mkhockeysqlfromdatabase", "mkhockeysqlfromxmlfile", "mkhockeyjsonfromxml", "mkhockeyxmlfromjson", "mkhockeyxmlfileclean", "help", "h", "version", "ver", "v", "mksymlinks", "mksymlink"]
getactdesc = ["convert hockey sqlite database to hockey xml file", "convert old hockey sqlite database to hockey xml file", "convert hockey sql dump file to hockey xml file", "convert hockey xml file to hockey sqlite database", "convert hockey sql dump file to sqlite database", "convert hockey sqlite database to hockey python file", "convert hockey xml file to hockey python file",
              "convert hockey sqlite database to hockey python alt file", "convert hockey xml file to hockey python alt file", "convert hockey sqlite database to hockey sql dump file", "convert hockey xml file to hockey sql dump file", "convert hockey xml file to hockey json file", "convert hockey json file to hockey xml file", "cleanup hockey xml files", "show this help page", "get version number of "+__project__, "make symbolic links"]
gethelplist = ["mkhockeyxmlfile", "mkhockeyxmlfromolddatabase", "mkhockeyxmlfromsql", "mkhockeydatabase", "mkhockeydatabasefromsql", "mkhockeypyfromdatabase", "mkhockeypyfromxmlfile", "mkhockeypyaltfromdatabase",
               "mkhockeypyaltfromxmlfile", "mkhockeysqlfromdatabase", "mkhockeysqlfromxmlfile", "mkhockeyjsonfromxml", "mkhockeyxmlfromjson", "mkhockeyxmlfileclean", "help", "version", "mksymlinks"]
getsymlist = ["mkhockeyxmlfile", "mkhockeyxmlfromolddatabase", "mkhockeyxmlfromsql", "mkhockeydatabase", "mkhockeydatabasefromsql", "mkhockeypyfromdatabase", "mkhockeypyfromxmlfile",
              "mkhockeypyaltfromdatabase", "mkhockeypyaltfromxmlfile", "mkhockeysqlfromdatabase", "mkhockeysqlfromxmlfile", "mkhockeyjsonfromxml", "mkhockeyxmlfromjson", "mkhockeyxmlfileclean"]
defaction = getactlist[14]
defxmlfile = pyhockeystats.defaultxmlfile
defsdbfile = pyhockeystats.defaultsdbfile
defoldsdbfile = pyhockeystats.defaultoldsdbfile
defpyfile = pyhockeystats.defaultpyfile
defsqlfile = pyhockeystats.defaultsqlfile
defjsonfile = pyhockeystats.defaultjsonfile
getactstr = "Actions: "
getverstr = __project__+" "+__version__
for getactsublist, getactsubdesc in zip(gethelplist, getactdesc):
    getactstr = getactstr+"\n"+getactsublist+": "+getactsubdesc+" "
getactstr = getactstr.strip()
curaction = defaction
cursaction = os.path.splitext(os.path.basename(sys.argv[0]))[0]
cursactionspt = list(cursaction.split("-"))
if (len(cursactionspt) <= 1):
    cursaction = cursactionspt[0]
if (len(cursactionspt) > 1):
    for cursactionact in cursactionspt:
        if (cursactionact in getactlist):
            cursaction = cursactionact
            break
if (cursaction in getactlist):
    curaction = cursaction
if (len(sys.argv) >= 2):
    if (sys.argv[1] not in getactlist):
        curaction = defaction
    if (cursaction in getactlist):
        curaction = cursaction
    if (len(sys.argv) > 1):
        for curargact in sys.argv:
            if (curargact in getactlist):
                curaction = curargact
                break

if (curaction == getactlist[14] or curaction == getactlist[15]):
    print(getactstr)

if (curaction == getactlist[16] or curaction == getactlist[17] or curaction == getactlist[18]):
    print(getverstr)

if ((curaction == getactlist[19] or curaction == getactlist[20])):
    for cursymact in getsymlist:
        curscrpath = os.path.dirname(sys.argv[0])
        infilename = sys.argv[0]
        infilenameinfo = os.path.splitext(sys.argv[0])
        if (curscrpath == ""):
            curscrpath = "."
        if (os.sep == "\\"):
            curscrpath = curscrpath.replace(os.sep, "/")
            infilename = infilename.replace(os.sep, "/")
        curscrpath = curscrpath+"/"
        outfilename = curscrpath+cursymact
        outfileext = str(infilenameinfo[1]).rstrip(".")
        outfilefull = outfilename+outfileext
        try:
            os.symlink(infilename, outfilefull)
            print("'"+outfilefull+"' -> '"+infilename+"'")
        except OSError:
            shutil.copy2(infilename, outfilefull)
            print("'"+outfilefull+"' -> '"+infilename+"'")
        except AttributeError:
            shutil.copy2(infilename, outfilefull)
            print("'"+outfilefull+"' -> '"+infilename+"'")

if (curaction == getactlist[0]):
    argparser = argparse.ArgumentParser(
        description=getactdesc[0], conflict_handler="resolve", add_help=True)
    argparser.add_argument("-v", "--ver", "--version",
                           action="version", version=__program_name__+" "+__version__)
    argparser.add_argument('action', nargs='?', default=curaction)
    argparser.add_argument("-i", "-f", "--infile", default=os.environ.get(
        'INFILE', defsdbfile), help="sqlite database to convert")
    argparser.add_argument("-o", "-t", "--outfile",
                           default=None, help="xml file to output")
    argparser.add_argument("-V", "-d", "--verbose", action="store_true",
                           help="print various debugging information")
    argparser.add_argument("-j", "-s", "--jsonverbose", action="store_true",
                           help="print various debugging information in json")
    getargs = argparser.parse_args()
    verboseon = getargs.verbose
    if ('VERBOSE' in os.environ or 'DEBUG' in os.environ):
        verboseon = True
    if (verboseon):
        logging.basicConfig(format="%(message)s",
                            stream=sys.stdout, level=logging.DEBUG)
    pyhockeystats.MakeHockeyXMLFileFromHockeyDatabase(
        getargs.infile, getargs.outfile, verbose=verboseon, jsonverbose=getargs.jsonverbose)

if (curaction == getactlist[1]):
    argparser = argparse.ArgumentParser(
        description=getactdesc[1], conflict_handler="resolve", add_help=True)
    argparser.add_argument("-v", "--ver", "--version",
                           action="version", version=__program_name__+" "+__version__)
    argparser.add_argument('action', nargs='?', default=curaction)
    argparser.add_argument("-i", "-f", "--infile", default=os.environ.get(
        'INFILE', defoldsdbfile), help="sqlite database to convert")
    argparser.add_argument("-o", "-t", "--outfile",
                           default=os.environ.get('OUTFILE', None), help="xml file to output")
    argparser.add_argument("-V", "-d", "--verbose", action="store_true",
                           help="print various debugging information")
    argparser.add_argument("-j", "-s", "--jsonverbose", action="store_true",
                           help="print various debugging information in json")
    getargs = argparser.parse_args()
    verboseon = getargs.verbose
    if ('VERBOSE' in os.environ or 'DEBUG' in os.environ):
        verboseon = True
    if (verboseon):
        logging.basicConfig(format="%(message)s",
                            stream=sys.stdout, level=logging.DEBUG)
    pyhockeystats.MakeHockeyXMLFileFromOldHockeyDatabase(
        getargs.infile, getargs.outfile, verbose=verboseon, jsonverbose=getargs.jsonverbose)

if (curaction == getactlist[2]):
    argparser = argparse.ArgumentParser(
        description=getactdesc[2], conflict_handler="resolve", add_help=True)
    argparser.add_argument("-v", "--ver", "--version",
                           action="version", version=__program_name__+" "+__version__)
    argparser.add_argument('action', nargs='?', default=curaction)
    argparser.add_argument("-i", "-f", "--infile", default=os.environ.get(
        'INFILE', defsqlfile), help="sql dump file to import")
    argparser.add_argument("-o", "-t", "--outfile",
                           default=os.environ.get('OUTFILE', None), help="xml file to output")
    argparser.add_argument("-V", "-d", "--verbose", action="store_true",
                           help="print various debugging information")
    argparser.add_argument("-j", "-s", "--jsonverbose", action="store_true",
                           help="print various debugging information in json")
    getargs = argparser.parse_args()
    verboseon = getargs.verbose
    if ('VERBOSE' in os.environ or 'DEBUG' in os.environ):
        verboseon = True
    if (verboseon):
        logging.basicConfig(format="%(message)s",
                            stream=sys.stdout, level=logging.DEBUG)
    pyhockeystats.MakeHockeyXMLFileFromHockeySQL(
        getargs.infile, None, getargs.outfile, verbose=verboseon, jsonverbose=getargs.jsonverbose)

if (curaction == getactlist[3]):
    argparser = argparse.ArgumentParser(
        description=getactdesc[3], conflict_handler="resolve", add_help=True)
    argparser.add_argument("-v", "--ver", "--version",
                           action="version", version=__program_name__+" "+__version__)
    argparser.add_argument('action', nargs='?', default=curaction)
    argparser.add_argument("-i", "-f", "--infile", default=os.environ.get(
        'INFILE', defxmlfile), help="xml file to convert")
    argparser.add_argument("-o", "-t", "--outfile", default=os.environ.get(
        'OUTFILE', None), help="sqlite database to output")
    argparser.add_argument("-V", "-d", "--verbose", action="store_true",
                           help="print various debugging information")
    argparser.add_argument("-j", "-s", "--jsonverbose", action="store_true",
                           help="print various debugging information in json")
    getargs = argparser.parse_args()
    verboseon = getargs.verbose
    if ('VERBOSE' in os.environ or 'DEBUG' in os.environ):
        verboseon = True
    if (verboseon):
        logging.basicConfig(format="%(message)s",
                            stream=sys.stdout, level=logging.DEBUG)
    pyhockeystats.MakeHockeyDatabaseFromHockeyXML(
        getargs.infile, getargs.outfile, verbose=verboseon, jsonverbose=getargs.jsonverbose)

if (curaction == getactlist[4]):
    argparser = argparse.ArgumentParser(
        description=getactdesc[4], conflict_handler="resolve", add_help=True)
    argparser.add_argument("-v", "--ver", "--version",
                           action="version", version=__program_name__+" "+__version__)
    argparser.add_argument('action', nargs='?', default=curaction)
    argparser.add_argument("-i", "-f", "--infile", default=os.environ.get(
        'INFILE', defsqlfile), help="sql dump file to import")
    argparser.add_argument("-o", "-t", "--outfile", default=os.environ.get(
        'OUTFILE', None), help="sqlite database to output")
    argparser.add_argument("-V", "-d", "--verbose", action="store_true",
                           help="print various debugging information")
    argparser.add_argument("-j", "-s", "--jsonverbose", action="store_true",
                           help="print various debugging information in json")
    getargs = argparser.parse_args()
    verboseon = getargs.verbose
    if ('VERBOSE' in os.environ or 'DEBUG' in os.environ):
        verboseon = True
    if (verboseon):
        logging.basicConfig(format="%(message)s",
                            stream=sys.stdout, level=logging.DEBUG)
    pyhockeystats.MakeHockeyDatabaseFromHockeySQL(
        getargs.infile, getargs.outfile, verbose=verboseon, jsonverbose=getargs.jsonverbose)

if (curaction == getactlist[5]):
    argparser = argparse.ArgumentParser(
        description=getactdesc[5], conflict_handler="resolve", add_help=True)
    argparser.add_argument("-v", "--ver", "--version",
                           action="version", version=__program_name__+" "+__version__)
    argparser.add_argument('action', nargs='?', default=curaction)
    argparser.add_argument("-i", "-f", "--infile", default=os.environ.get(
        'INFILE', defsdbfile), help="sqlite database to convert")
    argparser.add_argument("-o", "-t", "--outfile",
                           default=os.environ.get('OUTFILE', None), help="python file to output")
    argparser.add_argument("-V", "-d", "--verbose", action="store_true",
                           help="print various debugging information")
    argparser.add_argument("-j", "-s", "--jsonverbose", action="store_true",
                           help="print various debugging information in json")
    getargs = argparser.parse_args()
    verboseon = getargs.verbose
    if ('VERBOSE' in os.environ or 'DEBUG' in os.environ):
        verboseon = True
    if (verboseon):
        logging.basicConfig(format="%(message)s",
                            stream=sys.stdout, level=logging.DEBUG)
    pyhockeystats.MakeHockeyPythonFileFromHockeyDatabase(
        getargs.infile, getargs.outfile, verbose=verboseon, jsonverbose=getargs.jsonverbose)

if (curaction == getactlist[6]):
    argparser = argparse.ArgumentParser(
        description=getactdesc[6], conflict_handler="resolve", add_help=True)
    argparser.add_argument("-v", "--ver", "--version",
                           action="version", version=__program_name__+" "+__version__)
    argparser.add_argument('action', nargs='?', default=curaction)
    argparser.add_argument("-i", "-f", "--infile", default=os.environ.get(
        'INFILE', defxmlfile), help="xml file to convert")
    argparser.add_argument("-o", "-t", "--outfile",
                           default=os.environ.get('OUTFILE', None), help="python file to output")
    argparser.add_argument("-V", "-d", "--verbose", action="store_true",
                           help="print various debugging information")
    argparser.add_argument("-j", "-s", "--jsonverbose", action="store_true",
                           help="print various debugging information in json")
    getargs = argparser.parse_args()
    verboseon = getargs.verbose
    if ('VERBOSE' in os.environ or 'DEBUG' in os.environ):
        verboseon = True
    if (verboseon):
        logging.basicConfig(format="%(message)s",
                            stream=sys.stdout, level=logging.DEBUG)
    pyhockeystats.MakeHockeyPythonFileFromHockeyXML(
        getargs.infile, getargs.outfile, verbose=verboseon, jsonverbose=getargs.jsonverbose)

if (curaction == getactlist[7]):
    argparser = argparse.ArgumentParser(
        description=getactdesc[5], conflict_handler="resolve", add_help=True)
    argparser.add_argument("-v", "--ver", "--version",
                           action="version", version=__program_name__+" "+__version__)
    argparser.add_argument('action', nargs='?', default=curaction)
    argparser.add_argument("-i", "-f", "--infile", default=os.environ.get(
        'INFILE', defsdbfile), help="sqlite database to convert")
    argparser.add_argument("-o", "-t", "--outfile",
                           default=os.environ.get('OUTFILE', None), help="python file to output")
    argparser.add_argument("-V", "-d", "--verbose", action="store_true",
                           help="print various debugging information")
    argparser.add_argument("-j", "-s", "--jsonverbose", action="store_true",
                           help="print various debugging information in json")
    getargs = argparser.parse_args()
    verboseon = getargs.verbose
    if ('VERBOSE' in os.environ or 'DEBUG' in os.environ):
        verboseon = True
    if (verboseon):
        logging.basicConfig(format="%(message)s",
                            stream=sys.stdout, level=logging.DEBUG)
    pyhockeystats.MakeHockeyPythonAltFileFromHockeyDatabase(
        getargs.infile, getargs.outfile, verbose=verboseon, jsonverbose=getargs.jsonverbose)

if (curaction == getactlist[8]):
    argparser = argparse.ArgumentParser(
        description=getactdesc[6], conflict_handler="resolve", add_help=True)
    argparser.add_argument("-v", "--ver", "--version",
                           action="version", version=__program_name__+" "+__version__)
    argparser.add_argument('action', nargs='?', default=curaction)
    argparser.add_argument("-i", "-f", "--infile", default=os.environ.get(
        'INFILE', defxmlfile), help="xml file to convert")
    argparser.add_argument("-o", "-t", "--outfile",
                           default=os.environ.get('OUTFILE', None), help="python file to output")
    argparser.add_argument("-V", "-d", "--verbose", action="store_true",
                           help="print various debugging information")
    argparser.add_argument("-j", "-s", "--jsonverbose", action="store_true",
                           help="print various debugging information in json")
    getargs = argparser.parse_args()
    verboseon = getargs.verbose
    if ('VERBOSE' in os.environ or 'DEBUG' in os.environ):
        verboseon = True
    if (verboseon):
        logging.basicConfig(format="%(message)s",
                            stream=sys.stdout, level=logging.DEBUG)
    pyhockeystats.MakeHockeyPythonAltFileFromHockeyXML(
        getargs.infile, getargs.outfile, verbose=verboseon, jsonverbose=getargs.jsonverbose)

if (curaction == getactlist[9]):
    argparser = argparse.ArgumentParser(
        description=getactdesc[7], conflict_handler="resolve", add_help=True)
    argparser.add_argument("-v", "--ver", "--version",
                           action="version", version=__program_name__+" "+__version__)
    argparser.add_argument('action', nargs='?', default=curaction)
    argparser.add_argument("-i", "-f", "--infile", default=os.environ.get(
        'INFILE', defsdbfile), help="sqlite database to convert")
    argparser.add_argument("-o", "-t", "--outfile", default=os.environ.get(
        'OUTFILE', None), help="sql dump file to output")
    argparser.add_argument("-V", "-d", "--verbose", action="store_true",
                           help="print various debugging information")
    argparser.add_argument("-j", "-s", "--jsonverbose", action="store_true",
                           help="print various debugging information in json")
    getargs = argparser.parse_args()
    verboseon = getargs.verbose
    if ('VERBOSE' in os.environ or 'DEBUG' in os.environ):
        verboseon = True
    if (verboseon):
        logging.basicConfig(format="%(message)s",
                            stream=sys.stdout, level=logging.DEBUG)
    pyhockeystats.MakeHockeySQLFileFromHockeyDatabase(
        getargs.infile, getargs.outfile, verbose=verboseon, jsonverbose=getargs.jsonverbose)

if (curaction == getactlist[10]):
    argparser = argparse.ArgumentParser(
        description=getactdesc[8], conflict_handler="resolve", add_help=True)
    argparser.add_argument("-v", "--ver", "--version",
                           action="version", version=__program_name__+" "+__version__)
    argparser.add_argument('action', nargs='?', default=curaction)
    argparser.add_argument("-i", "-f", "--infile", default=os.environ.get(
        'INFILE', defxmlfile), help="xml file to convert")
    argparser.add_argument("-o", "-t", "--outfile", default=os.environ.get(
        'OUTFILE', None), help="sql dump file to output")
    argparser.add_argument("-V", "-d", "--verbose", action="store_true",
                           help="print various debugging information")
    argparser.add_argument("-j", "-s", "--jsonverbose", action="store_true",
                           help="print various debugging information in json")
    getargs = argparser.parse_args()
    verboseon = getargs.verbose
    if ('VERBOSE' in os.environ or 'DEBUG' in os.environ):
        verboseon = True
    if (verboseon):
        logging.basicConfig(format="%(message)s",
                            stream=sys.stdout, level=logging.DEBUG)
    pyhockeystats.MakeHockeySQLFileFromHockeyXML(
        getargs.infile, getargs.outfile, verbose=verboseon, jsonverbose=getargs.jsonverbose)

if (curaction == getactlist[11]):
    argparser = argparse.ArgumentParser(
        description=getactdesc[6], conflict_handler="resolve", add_help=True)
    argparser.add_argument("-v", "--ver", "--version",
                           action="version", version=__program_name__+" "+__version__)
    argparser.add_argument('action', nargs='?', default=curaction)
    argparser.add_argument("-i", "-f", "--infile", default=os.environ.get(
        'INFILE', defxmlfile), help="xml file to convert")
    argparser.add_argument("-o", "-t", "--outfile", default=os.environ.get(
        'OUTFILE', defjsonfile), help="json file to output")
    argparser.add_argument("-V", "-d", "--verbose", action="store_true",
                           help="print various debugging information")
    argparser.add_argument("-j", "-s", "--jsonverbose", action="store_true",
                           help="print various debugging information in json")
    getargs = argparser.parse_args()
    verboseon = getargs.verbose
    if ('VERBOSE' in os.environ or 'DEBUG' in os.environ):
        verboseon = True
    if (verboseon):
        logging.basicConfig(format="%(message)s",
                            stream=sys.stdout, level=logging.DEBUG)
    if (getargs.outfile is None):
        pyhockeystats.MakeHockeyJSONFromHockeyXML(
            getargs.infile, verbose=verboseon, jsonverbose=getargs.jsonverbose)
    else:
        pyhockeystats.MakeHockeyJSONFileFromHockeyXML(
            getargs.infile, getargs.outfile, verbose=verboseon, jsonverbose=getargs.jsonverbose)

if (curaction == getactlist[12]):
    argparser = argparse.ArgumentParser(
        description=getactdesc[0], conflict_handler="resolve", add_help=True)
    argparser.add_argument("-v", "--ver", "--version",
                           action="version", version=__program_name__+" "+__version__)
    argparser.add_argument('action', nargs='?', default=curaction)
    argparser.add_argument("-i", "-f", "--infile", default=os.environ.get(
        'INFILE', defsdbfile), help="json file to convert")
    argparser.add_argument("-o", "-t", "--outfile", default=os.environ.get(
        'OUTFILE', defjsonfile), help="xml file to output")
    argparser.add_argument("-V", "-d", "--verbose", action="store_true",
                           help="print various debugging information")
    argparser.add_argument("-j", "-s", "--jsonverbose", action="store_true",
                           help="print various debugging information in json")
    getargs = argparser.parse_args()
    verboseon = getargs.verbose
    if ('VERBOSE' in os.environ or 'DEBUG' in os.environ):
        verboseon = True
    if (verboseon):
        logging.basicConfig(format="%(message)s",
                            stream=sys.stdout, level=logging.DEBUG)
    pyhockeystats.MakeHockeyXMLFileFromHockeyJSON(
        getargs.infile, getargs.outfile, verbose=verboseon, jsonverbose=getargs.jsonverbose)

if (curaction == getactlist[13]):
    argparser = argparse.ArgumentParser(
        description=getactdesc[9], conflict_handler="resolve", add_help=True)
    argparser.add_argument("-v", "--ver", "--version",
                           action="version", version=__program_name__+" "+__version__)
    argparser.add_argument('action', nargs='?', default=curaction)
    argparser.add_argument("-i", "-f", "--infile", default=os.environ.get(
        'INFILE', defxmlfile), help="xml file to clean")
    argparser.add_argument("-o", "-t", "--outfile", default=os.environ.get(
        'OUTFILE', None), help="clean xml file to output")
    argparser.add_argument("-V", "-d", "--verbose", action="store_true",
                           help="print various debugging information")
    argparser.add_argument("-j", "-s", "--jsonverbose", action="store_true",
                           help="print various debugging information in json")
    getargs = argparser.parse_args()
    verboseon = getargs.verbose
    if ('VERBOSE' in os.environ or 'DEBUG' in os.environ):
        verboseon = True
    if (verboseon):
        logging.basicConfig(format="%(message)s",
                            stream=sys.stdout, level=logging.DEBUG)
    if (getargs.outfile is None):
        pyhockeystats.MakeHockeyXMLFromHockeyXML(
            getargs.infile, verbose=verboseon, jsonverbose=getargs.jsonverbose)
    else:
        pyhockeystats.MakeHockeyXMLFileFromHockeyXML(
            getargs.infile, getargs.outfile, verbose=verboseon, jsonverbose=getargs.jsonverbose)
