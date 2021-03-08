#!/usr/bin/env python

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2015-2021 Game Maker 2k - https://github.com/GameMaker2k
    Copyright 2015-2021 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: setup.py - Last Update: 1/15/2021 Ver. 0.5.0 RC 1 - Author: cooldude2k $
'''

import re, os, sys, time, shutil, datetime, platform, pkg_resources;
from setuptools import setup, find_packages;

install_requires = [];
extras_requires = [];
extras_requires_dict = {};
pygenbuildinfo = True;
pyprever = platform.python_version_tuple();
pyver = str(pyprever[0]);
if(os.path.exists("."+os.sep+"scripts") and os.path.isdir("."+os.sep+"scripts")):
 shutil.rmtree("."+os.sep+"scripts");
 print("removed directory '."+os.sep+"scripts'");
if(os.path.exists("."+os.sep+"scripts") and os.path.isfile("."+os.sep+"scripts")):
 os.unlink("."+os.sep+"scripts");
 print("removed '."+os.sep+"scripts'");
os.mkdir("."+os.sep+"scripts");
print("created directory '."+os.sep+"scripts'");
shutil.copy2("."+os.sep+"mkhockeytool.py", "."+os.sep+"scripts"+os.sep+"mkhockeytool"+pyver+".py");
shutil.copy2("."+os.sep+"mkhockeydata.py", "."+os.sep+"scripts"+os.sep+"mkhockeydata"+pyver+".py");
os.chdir("."+os.sep+"scripts");
try:
 os.symlink("."+os.sep+"mkhockeytool"+pyver+".py", "."+os.sep+"mkhockeytool.py");
 print("'."+os.sep+"mkhockeytool"+pyver+".py' -> '."+os.sep+"mkhockeytool.py'");
except OSError:
 shutil.copy2("."+os.sep+"mkhockeytool"+pyver+".py", "."+os.sep+"mkhockeytool.py");
 print("'."+os.sep+"mkhockeytool"+pyver+".py' -> '."+os.sep+"mkhockeytool.py'");
except AttributeError:
 shutil.copy2("."+os.sep+"mkhockeytool"+pyver+".py", "."+os.sep+"mkhockeytool.py");
 print("'."+os.sep+"mkhockeytool"+pyver+".py' -> '."+os.sep+"mkhockeytool.py'");
try:
 os.symlink("."+os.sep+"mkhockeydata"+pyver+".py", "."+os.sep+"mkhockeydata.py");
 print("'."+os.sep+"mkhockeydata"+pyver+".py' -> '."+os.sep+"mkhockeydata.py'");
except OSError:
 shutil.copy2("."+os.sep+"mkhockeydata"+pyver+".py", "."+os.sep+"mkhockeydata.py");
 print("'."+os.sep+"mkhockeydata"+pyver+".py' -> '."+os.sep+"mkhockeydata.py'");
except AttributeError:
 shutil.copy2("."+os.sep+"mkhockeydata"+pyver+".py", "."+os.sep+"mkhockeydata.py");
 print("'."+os.sep+"mkhockeydata"+pyver+".py' -> '."+os.sep+"mkhockeydata.py'");
getsymlist = ["mkhockeyxmlfile", "mkhockeyxmlfromolddatabase", "mkhockeyxmlfromsql", "mkhockeydatabase", "mkhockeydatabasefromsql", "mkhockeypyfromdatabase", "mkhockeypyfromxmlfile", "mkhockeypyaltfromdatabase", "mkhockeypyaltfromxmlfile", "mkhockeysqlfromdatabase", "mkhockeysqlfromxmlfile", "mkhockeyjsonfromxml", "mkhockeyxmlfromjson", "mkhockeyxmlfileclean", "mkhockeyxmlfile"+pyver, "mkhockeyxmlfromolddatabase"+pyver, "mkhockeyxmlfromsql"+pyver, "mkhockeydatabase"+pyver, "mkhockeydatabasefromsql"+pyver, "mkhockeypyfromdatabase"+pyver, "mkhockeypyfromxmlfile"+pyver, "mkhockeypyaltfromdatabase"+pyver, "mkhockeypyaltfromxmlfile"+pyver, "mkhockeysqlfromdatabase"+pyver, "mkhockeysqlfromxmlfile"+pyver, "mkhockeyjsonfromxml"+pyver, "mkhockeyxmlfromjson"+pyver, "mkhockeyxmlfileclean"+pyver];
for cursymact in getsymlist:
 curscrpath = os.path.dirname(sys.argv[0]);
 infilename = "."+os.sep+"mkhockeydata"+pyver+".py";
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
 try:
  os.symlink(infilename, outfilefull);
  print("'"+outfilefull+"' -> '"+infilename+"'");
 except OSError:
  shutil.copy2(infilename, outfilefull);
  print("'"+outfilefull+"' -> '"+infilename+"'");
 except AttributeError:
  shutil.copy2(infilename, outfilefull);
  print("'"+outfilefull+"' -> '"+infilename+"'");
os.chdir("."+os.sep+"..");

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
# pymodule['pymodules'] = [y for x in os.walk("libhockeydata") for y in glob.glob(os.path.join(x[0], '*.py'))];
pymodule['pymodules'] = [];
pymodule['packages'] = find_packages();
pymodule['packagedata'] = {'libhockeydata/xml': ['*.dtd', '*.xsl', '*.xsd', '*.rng', '*.rnc']};
pymodule['datafiles'] = None;
pymodule['includepackagedata'] = True;
pymodule['installrequires'] = install_requires;
pymodule['extrasrequires'] = extras_requires_dict;
pymodule['scripts'] = ['scripts'+os.sep+'mkhockeytool.py', 'scripts'+os.sep+'mkhockeydata.py', 'scripts'+os.sep+'mkhockeydatabase.py', 'scripts'+os.sep+'mkhockeydatabasefromsql.py', 'scripts'+os.sep+'mkhockeypyfromdatabase.py', 'scripts'+os.sep+'mkhockeypyfromxmlfile.py', 'scripts'+os.sep+'mkhockeysqlfromdatabase.py', 'scripts'+os.sep+'mkhockeysqlfromxmlfile.py', 'scripts'+os.sep+'mkhockeyxmlfile.py', 'scripts'+os.sep+'mkhockeyxmlfileclean.py', 'scripts'+os.sep+'mkhockeyxmlfromolddatabase.py', 'scripts'+os.sep+'mkhockeyxmlfromsql.py', 'scripts'+os.sep+'mkhockeytool'+pyver+'.py', 'scripts'+os.sep+'mkhockeydata'+pyver+'.py', 'scripts'+os.sep+'mkhockeydatabase'+pyver+'.py', 'scripts'+os.sep+'mkhockeydatabasefromsql'+pyver+'.py', 'scripts'+os.sep+'mkhockeypyfromdatabase'+pyver+'.py', 'scripts'+os.sep+'mkhockeypyfromxmlfile'+pyver+'.py', 'scripts'+os.sep+'mkhockeysqlfromdatabase'+pyver+'.py', 'scripts'+os.sep+'mkhockeysqlfromxmlfile'+pyver+'.py', 'scripts'+os.sep+'mkhockeyxmlfile'+pyver+'.py', 'scripts'+os.sep+'mkhockeyxmlfileclean'+pyver+'.py', 'scripts'+os.sep+'mkhockeyxmlfromolddatabase'+pyver+'.py', 'scripts'+os.sep+'mkhockeyxmlfromsql'+pyver+'.py'];
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

if(pygenbuildinfo):
 mycurtime = datetime.datetime.now();
 mycurtimetuple = mycurtime.timetuple();
 mycurtimestamp = int(time.mktime(mycurtimetuple));
 '''verinfodata = verinfodata.replace('__build_time__ = {"timestamp": None, "year": None, "month": None, "day": None, "hour": None, "minute": None, "second": None};', '__build_time__ = {"timestamp": '+str(mycurtimestamp)+', "year": '+str(mycurtimetuple[0])+', "month": '+str(mycurtimetuple[1])+', "day": '+str(mycurtimetuple[2])+', "hour": '+str(mycurtimetuple[3])+', "minute": '+str(mycurtimetuple[4])+', "second": '+str(mycurtimetuple[5])+'};');'''
 verinfodata = re.sub("__build_time__ \= \{.*\}\;", '__build_time__ = {"timestamp": '+str(mycurtimestamp)+', "year": '+str(mycurtimetuple[0])+', "month": '+str(mycurtimetuple[1])+', "day": '+str(mycurtimetuple[2])+', "hour": '+str(mycurtimetuple[3])+', "minute": '+str(mycurtimetuple[4])+', "second": '+str(mycurtimetuple[5])+'};', verinfodata);
 utccurtime = datetime.datetime.utcnow();
 utccurtimetuple = utccurtime.timetuple();
 utccurtimestamp = int(time.mktime(utccurtimetuple));
 '''verinfodata = verinfodata.replace('__build_time_utc__ = {"timestamp": None, "year": None, "month": None, "day": None, "hour": None, "minute": None, "second": None};', '__build_time_utc__ = {"timestamp": '+str(utccurtimestamp)+', "year": '+str(utccurtimetuple[0])+', "month": '+str(utccurtimetuple[1])+', "day": '+str(utccurtimetuple[2])+', "hour": '+str(utccurtimetuple[3])+', "minute": '+str(utccurtimetuple[4])+', "second": '+str(utccurtimetuple[5])+'};');'''
 verinfodata = re.sub("__build_time_utc__ \= \{.*\}\;", '__build_time_utc__ = {"timestamp": '+str(utccurtimestamp)+', "year": '+str(utccurtimetuple[0])+', "month": '+str(utccurtimetuple[1])+', "day": '+str(utccurtimetuple[2])+', "hour": '+str(utccurtimetuple[3])+', "minute": '+str(utccurtimetuple[4])+', "second": '+str(utccurtimetuple[5])+'};', verinfodata);
 linuxdist = None;
 try:
  linuxdist = platform.linux_distribution();
 except AttributeError:
  linuxdist = None;
 if(sys.version[0]=="2"):
  '''verinfodata = verinfodata.replace('__build_python_info__ = {"python_branch": None, "python_build": None, "python_compiler": None, "python_implementation": None, "python_revision": None, "python_version": None, "python_version_tuple": None, "release": None, "system": None, "uname": None, "machine": None, "node": None, "platform": None, "processor": None, "version": None, "java_ver": None, "win32_ver": None, "mac_ver": None, "linux_distribution": None, "libc_ver": None};', '__build_python_info__ = '+str({'python_branch': platform.python_branch(), 'python_build': platform.python_build(), 'python_compiler': platform.python_compiler(), 'python_implementation': platform.python_implementation(), 'python_revision': platform.python_revision(), 'python_version': platform.python_version(), 'python_version_tuple': platform.python_version_tuple(), 'release': platform.release(), 'system': platform.system(), 'uname': platform.uname(), 'machine': platform.machine(), 'node': platform.node(), 'platform': platform.platform(), 'processor': platform.processor(), 'architecture': platform.architecture(), 'version': platform.version(), 'java_ver': platform.java_ver(), 'win32_ver': platform.win32_ver(), 'mac_ver': platform.mac_ver(), 'linux_distribution': linuxdist, 'libc_ver': platform.libc_ver()})+';');'''
  verinfodata = re.sub("__build_python_info__ \= \{.*\}\;", '__build_python_info__ = '+str({'python_branch': platform.python_branch(), 'python_build': platform.python_build(), 'python_compiler': platform.python_compiler(), 'python_implementation': platform.python_implementation(), 'python_revision': platform.python_revision(), 'python_version': platform.python_version(), 'python_version_tuple': platform.python_version_tuple(), 'release': platform.release(), 'system': platform.system(), 'uname': platform.uname(), 'machine': platform.machine(), 'node': platform.node(), 'platform': platform.platform(), 'processor': platform.processor(), 'architecture': platform.architecture(), 'version': platform.version(), 'java_ver': platform.java_ver(), 'win32_ver': platform.win32_ver(), 'mac_ver': platform.mac_ver(), 'linux_distribution': linuxdist, 'libc_ver': platform.libc_ver()})+';', verinfodata);
 if(sys.version[0]=="3"):
  '''verinfodata = verinfodata.replace('__build_python_info__ = {"python_branch": None, "python_build": None, "python_compiler": None, "python_implementation": None, "python_revision": None, "python_version": None, "python_version_tuple": None, "release": None, "system": None, "uname": None, "machine": None, "node": None, "platform": None, "processor": None, "version": None, "java_ver": None, "win32_ver": None, "mac_ver": None, "linux_distribution": None, "libc_ver": None};', '__build_python_info__ = '+str({'python_branch': platform.python_branch(), 'python_build': platform.python_build(), 'python_compiler': platform.python_compiler(), 'python_implementation': platform.python_implementation(), 'python_revision': platform.python_revision(), 'python_version': platform.python_version(), 'python_version_tuple': platform.python_version_tuple(), 'release': platform.release(), 'system': platform.system(), 'uname': (platform.uname()[0], platform.uname()[1], platform.uname()[2], platform.uname()[3], platform.uname()[4], platform.uname()[5]), 'machine': platform.machine(), 'node': platform.node(), 'platform': platform.platform(), 'processor': platform.processor(), 'architecture': platform.architecture(), 'version': platform.version(), 'java_ver': platform.java_ver(), 'win32_ver': platform.win32_ver(), 'mac_ver': platform.mac_ver(), 'linux_distribution': linuxdist, 'libc_ver': platform.libc_ver()})+';');'''
  verinfodata = re.sub("__build_python_info__ \= \{.*\}\;", '__build_python_info__ = '+str({'python_branch': platform.python_branch(), 'python_build': platform.python_build(), 'python_compiler': platform.python_compiler(), 'python_implementation': platform.python_implementation(), 'python_revision': platform.python_revision(), 'python_version': platform.python_version(), 'python_version_tuple': platform.python_version_tuple(), 'release': platform.release(), 'system': platform.system(), 'uname': (platform.uname()[0], platform.uname()[1], platform.uname()[2], platform.uname()[3], platform.uname()[4], platform.uname()[5]), 'machine': platform.machine(), 'node': platform.node(), 'platform': platform.platform(), 'processor': platform.processor(), 'architecture': platform.architecture(), 'version': platform.version(), 'java_ver': platform.java_ver(), 'win32_ver': platform.win32_ver(), 'mac_ver': platform.mac_ver(), 'linux_distribution': linuxdist, 'libc_ver': platform.libc_ver()})+';', verinfodata);
 '''verinfodata = verinfodata.replace('__build_python_is_set__ = False;', '__build_python_is_set__ = True;');'''
 verinfodata = re.sub("__build_python_is_set__ \= .*\;", '__build_python_is_set__ = True;', verinfodata);
 verinfofile = open(verinfofilename, "w");
 verinfofile.write(verinfodata);
 verinfofile.close();

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
 data_files = pymodule['datafiles'],
 include_package_data = pymodule['includepackagedata'],
 install_requires = pymodule['installrequires'],
 extras_require = pymodule['extrasrequires'],
 scripts = pymodule['scripts'],
 classifiers = pymodule['classifiers']
)
