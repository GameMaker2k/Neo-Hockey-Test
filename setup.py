#!/usr/bin/env python

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2015-2020 Game Maker 2k - https://github.com/GameMaker2k
    Copyright 2015-2020 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: setup.py - Last Update: 4/4/2020 Ver. 0.4.0 RC 1 - Author: cooldude2k $
'''

import re, os, sys, time, datetime, platform, pkg_resources;
from setuptools import setup, find_packages;

verinfofilename = os.path.realpath("."+os.path.sep+"libhockeydata"+os.path.sep+"versioninfo.py");
verinfofile = open(verinfofilename, "r");
verinfodata = verinfofile.read();
verinfofile.close();
setuppy_verinfo_esc = re.escape("__version_info__ = (")+"(.*)"+re.escape(");");
setuppy_verinfo = re.findall(setuppy_verinfo_esc, verinfodata)[0];
setuppy_verinfo_exp = [vergetspt.strip().replace("\"", "") for vergetspt in setuppy_verinfo.split(',')];
setuppy_dateinfo_esc = re.escape("__version_date_info__ = (")+"(.*)"+re.escape(");");
setuppy_dateinfo = re.findall(setuppy_dateinfo_esc, verinfodata)[0];
setuppy_dateinfo_exp = [vergetspt.strip().replace("\"", "") for vergetspt in setuppy_dateinfo.split(',')];
pymodule = {};
pymodule['version'] = str(setuppy_verinfo_exp[0])+"."+str(setuppy_verinfo_exp[1])+"."+str(setuppy_verinfo_exp[2]);
pymodule['versionrc'] = int(setuppy_verinfo_exp[4]);
pymodule['versionlist'] = (int(setuppy_verinfo_exp[0]), int(setuppy_verinfo_exp[1]), int(setuppy_verinfo_exp[2]), str(setuppy_verinfo_exp[3]), int(setuppy_verinfo_exp[4]));
pymodule['verdate'] = str(setuppy_dateinfo_exp[0])+"."+str(setuppy_dateinfo_exp[1])+"."+str(setuppy_dateinfo_exp[2]);
pymodule['verdaterc'] = int(setuppy_dateinfo_exp[4]);
pymodule['verdatelist'] = (int(setuppy_dateinfo_exp[0]), int(setuppy_dateinfo_exp[1]), int(setuppy_dateinfo_exp[2]), str(setuppy_dateinfo_exp[3]), int(setuppy_dateinfo_exp[4]));
pymodule['name'] = 'PyHockeyStats';
pymodule['author'] = 'Kazuki Przyborowski';
pymodule['authoremail'] = 'kazuki.przyborowski@gmail.com';
pymodule['maintainer'] = 'Kazuki Przyborowski';
pymodule['maintaineremail'] = 'kazuki.przyborowski@gmail.com';
pymodule['description'] = 'Just a test script dealing with hockey games and stats.';
pymodule['license'] = 'Revised BSD License';
pymodule['keywords'] = 'hockeystats pyhockeystats python python-hockeystats';
pymodule['url'] = 'https://github.com/GameMaker2k/Neo-Hockey-Test';
pymodule['downloadurl'] = 'https://github.com/GameMaker2k/Neo-Hockey-Test/archive/master.tar.gz';
pymodule['longdescription'] = 'Just a test script dealing with hockey games and stats.';
pymodule['platforms'] = 'OS Independent';
pymodule['zipsafe'] = True;
# pymodule['pymodules'] = [y for x in os.walk("upcean") for y in glob.glob(os.path.join(x[0], '*.py'))];
pymodule['pymodules'] = [];
pymodule['packages'] = find_packages();
pymodule['packagedata'] = {'libhockeydata/xml': ['*.dtd', '*.xsl', '*.xsd', '*.rng', '*.rnc']};
pymodule['scripts'] = ['mkhockeydata.py', 'mkhockeydatabase.py', 'mkhockeydatabasefromsql.py', 'mkhockeypyfromdatabase.py', 'mkhockeypyfromxmlfile.py', 'mkhockeysqlfromdatabase.py', 'mkhockeysqlfromxmlfile.py', 'mkhockeyxmlfile.py', 'mkhockeyxmlfileclean.py', 'mkhockeyxmlfromolddatabase.py', 'mkhockeyxmlfromsql.py'];
pymodule['classifiers'] = [
 'Development Status :: 5 - Production/Stable',
 'Intended Audience :: Developers',
 'Intended Audience :: Other Audience',
 'License :: OSI Approved',
 'License :: OSI Approved :: BSD License',
 'Natural Language :: English',
 'Operating System :: MacOS',
 'Operating System :: MacOS :: MacOS X',
 'Operating System :: Microsoft',
 'Operating System :: Microsoft :: Windows',
 'Operating System :: OS/2',
 'Operating System :: OS Independent',
 'Operating System :: POSIX',
 'Operating System :: Unix',
 'Programming Language :: Python',
 'Topic :: Utilities',
 'Topic :: Software Development',
 'Topic :: Software Development :: Libraries',
 'Topic :: Software Development :: Libraries :: Python Modules'
];
if(len(sys.argv)>1 and (sys.argv[1]=="versioninfo" or sys.argv[1]=="getversioninfo")):
 import json;
 pymodule_data = json.dumps(pymodule);
 print(pymodule_data);
 sys.exit();
if(len(sys.argv)>1 and (sys.argv[1]=="sourceinfo" or sys.argv[1]=="getsourceinfo")):
 srcinfofilename = os.path.realpath("."+os.path.sep+pkg_resources.to_filename(pymodule['name'])+".egg-info"+os.path.sep+"SOURCES.txt");
 srcinfofile = open(srcinfofilename, "r");
 srcinfodata = srcinfofile.read();
 srcinfofile.close();
 srcinfolist = srcinfodata.split('\n');
 srcfilelist = "";
 srcpdir = os.path.basename(os.path.dirname(os.path.realpath(__file__)));
 for ifile in srcinfolist:
  srcfilelist = "."+os.path.sep+srcpdir+os.path.sep+ifile+" "+srcfilelist;
 print(srcfilelist);
 sys.exit();
if(len(sys.argv)>1 and sys.argv[1]=="cleansourceinfo"):
 os.system("rm -rfv \""+os.path.realpath("."+os.path.sep+"dist\""));
 os.system("rm -rfv \""+os.path.realpath("."+os.path.sep+pkg_resources.to_filename(pymodule['name'])+".egg-info\""));
 sys.exit();

setup(
 name = pymodule['name'],
 version = pymodule['version'],
 author = pymodule['author'],
 author_email = pymodule['authoremail'],
 maintainer = pymodule['maintainer'],
 maintainer_email = pymodule['maintaineremail'],
 description = pymodule['description'],
 license = pymodule['license'],
 keywords = pymodule['keywords'],
 url = pymodule['url'],
 download_url = pymodule['downloadurl'],
 long_description = pymodule['longdescription'],
 platforms = pymodule['platforms'],
 zip_safe = pymodule['zipsafe'],
 py_modules = pymodule['pymodules'],
 packages = pymodule['packages'],
 package_data = pymodule['packagedata'],
 scripts = pymodule['scripts'],
 classifiers = pymodule['classifiers']
)
