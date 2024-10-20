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

    $FileInfo: __main__.py - Last Update: 10/17/2024 Ver. 0.9.6 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals, generators, with_statement, nested_scopes

import argparse
import os
import sys

from .versioninfo import (__author__, __copyright__, __credits__, __email__,
                          __license__, __license_string__, __maintainer__,
                          __program_alt_name__, __program_name__, __project__,
                          __project_release_url__, __project_url__,
                          __revision__, __revision_id__, __status__,
                          __version__, __version_alt__, __version_date__,
                          __version_date_alt__, __version_date_info__,
                          __version_date_plusrc__, __version_info__,
                          version_date, version_info)

try:
    reload(sys)
except NameError:
    from importlib import reload
    reload(sys)
try:
    sys.setdefaultencoding('utf-8')
except AttributeError:
    pass
hockeytestdir = os.path.dirname(__file__)
sys.path.append(hockeytestdir)
verinfotext = "{projectname} {projectver} {copyrightstr}; #Release {projectver} {projectdate}".format(
    projectname=__project__, projectver=__version__, copyrightstr=__copyright__, projectdate=__version_date__)

parser = argparse.ArgumentParser(description=verinfotext+"\nPyHockeyStats is just a test script dealing with hockey games and stats.",
                                 conflict_handler="resolve", add_help=True, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-v", "--version", action="version", version=verinfotext)
parser.add_argument("-l", "--license", action="store_true",
                    help="print license file")
parser.add_argument("-g", "--getinfo", default=None,
                    help="print info about PyHockeyStats")
getargs = parser.parse_args()

getinfolist = {'getmd': hockeytestdir, 'getmdir': hockeytestdir, 'moduledir': hockeytestdir, 'hockeytestdir': hockeytestdir, 'author': __author__, 'copyright': __copyright__, 'credits': __credits__, 'email': __email__, 'license': __license__, 'license_string': __license_string__, 'maintainer': __maintainer__,
               'project': __project__, 'project_url': __project_url__, 'revision': __revision__, 'status': __status__, 'version': __version__, 'version_alt': __version_alt__, 'version_date': __version_date__, 'version_date_alt': __version_date_alt__, 'version_date_info': __version_date_info__, 'version_info': __version_info__}

if (getargs.license is True and getargs.getinfo is not None):
    getargs.getinfo = None
if (getargs.license is False and getargs.getinfo is None):
    getargs.license = True
if (getargs.license is True):
    print("{licensestr}".format(licensestr=__license_string__))
if (getargs.getinfo is not None):
    print("{getmyinfo}".format(getmyinfo=getinfolist.get(
        getargs.getinfo, getinfolist['hockeytestdir'])))
