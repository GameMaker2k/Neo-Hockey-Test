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

    $FileInfo: mkhockeydata.py - Last Update: 1/27/2018 Ver. 0.0.1 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals;
import sqlite3, sys, os, re, libhockeydata, argparse;
import logging as log;

__project__ = libhockeydata.__project__;
__program_name__ = libhockeydata.__program_name__;
__project_url__ = libhockeydata.__project_url__;
__version_info__ = libhockeydata.__version_info__;
__version_date_info__ = libhockeydata.__version_date_info__;
__version_date__ = libhockeydata.__version_date__;
__version_date_plusrc__ = libhockeydata.__version_date_plusrc__
__version__ = libhockeydata.__version__;
__version_date_plusrc__ = libhockeydata.__version_date_plusrc__;

argparser = argparse.ArgumentParser(description="convert hockey xml file to sqlite database", conflict_handler="resolve", add_help=True);
argparser.add_argument("-v", "--version", action="version", version=__program_name__+" "+__version__);
argparser.add_argument("-f", "--file", default="./hockeydata.xml", help="xml file to convert");
getargs = argparser.parse_args();

libhockeydata.MakeHockeyDataFromXML(getargs.file);
