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

    $FileInfo: mkbundle.py - Last Update: 2/17/2020 Ver. 0.2.6 RC 1 - Author: cooldude2k $
'''

import os, sys, shutil, subprocess, tempfile, subprocess;

tempdir = tempfile.gettempdir();

if(os.path.exists(tempdir+os.path.sep+"pybundle") and os.path.isfile(tempdir+os.path.sep+"pybundle")):
 os.unlink(tempdir+os.path.sep+"pybundle");
if(os.path.exists(tempdir+os.path.sep+"pybundle") and os.path.isdir(tempdir+os.path.sep+"pybundle")):
 shutil.rmtree(tempdir+os.path.sep+"pybundle");
os.mkdir(tempdir+os.path.sep+"pybundle");
if(os.path.exists(tempdir+os.path.sep+"pybundle"+os.path.sep+"__main__.py") and os.path.isfile(tempdir+os.path.sep+"pybundle"+os.path.sep+"__main__.py")):
 os.unlink(tempdir+os.path.sep+"pybundle"+os.path.sep+"__main__.py");
if(os.path.exists(tempdir+os.path.sep+"pybundle"+os.path.sep+"__main__.py") and os.path.isdir(tempdir+os.path.sep+"pybundle"+os.path.sep+"__main__.py")):
 shutil.rmtree(tempdir+os.path.sep+"pybundle"+os.path.sep+"__main__.py");
shutil.copy2("."+os.path.sep+"mkhockeydata.py", tempdir+os.path.sep+"pybundle"+os.path.sep+"__main__.py");
if(os.path.exists(tempdir+os.path.sep+"pybundle"+os.path.sep+"libhockeydata") and os.path.isfile(tempdir+os.path.sep+"pybundle"+os.path.sep+"libhockeydata")):
 os.unlink(tempdir+os.path.sep+"pybundle"+os.path.sep+"libhockeydata");
if(os.path.exists(tempdir+os.path.sep+"pybundle"+os.path.sep+"libhockeydata") and os.path.isdir(tempdir+os.path.sep+"pybundle"+os.path.sep+"libhockeydata")):
 shutil.rmtree(tempdir+os.path.sep+"pybundle"+os.path.sep+"libhockeydata");
shutil.copytree("."+os.path.sep+"libhockeydata", tempdir+os.path.sep+"pybundle"+os.path.sep+"libhockeydata");
if(os.path.exists(tempdir+os.path.sep+"mkhockeydata.zip") and os.path.isfile(tempdir+os.path.sep+"mkhockeydata.zip")):
 os.unlink(tempdir+os.path.sep+"mkhockeydata.zip");
if(os.path.exists(tempdir+os.path.sep+"mkhockeydata.zip") and os.path.isdir(tempdir+os.path.sep+"mkhockeydata.zip")):
 shutil.rmtree(tempdir+os.path.sep+"mkhockeydata.zip");
shutil.make_archive(tempdir+os.path.sep+"mkhockeydata", "zip", tempdir+os.path.sep+"pybundle");
if(os.path.exists(tempdir+os.path.sep+"pybundle"+os.path.sep+"mkhockeydata.zip") and os.path.isfile(tempdir+os.path.sep+"pybundle"+os.path.sep+"mkhockeydata.zip")):
 os.unlink(tempdir+os.path.sep+"pybundle"+os.path.sep+"mkhockeydata.zip");
if(os.path.exists(tempdir+os.path.sep+"pybundle"+os.path.sep+"mkhockeydata.zip") and os.path.isdir(tempdir+os.path.sep+"pybundle"+os.path.sep+"mkhockeydata.zip")):
 shutil.rmtree(tempdir+os.path.sep+"pybundle"+os.path.sep+"mkhockeydata.zip");
shutil.move(tempdir+os.path.sep+"mkhockeydata.zip", tempdir+os.path.sep+"pybundle"+os.path.sep+"mkhockeydata.zip");
if(os.path.exists(tempdir+os.path.sep+"pybundle"+os.path.sep+"mkhockeydata") and os.path.isfile(tempdir+os.path.sep+"pybundle"+os.path.sep+"mkhockeydata")):
 os.unlink(tempdir+os.path.sep+"pybundle"+os.path.sep+"mkhockeydata");
if(os.path.exists(tempdir+os.path.sep+"pybundle"+os.path.sep+"mkhockeydata") and os.path.isdir(tempdir+os.path.sep+"pybundle"+os.path.sep+"mkhockeydata")):
 shutil.rmtree(tempdir+os.path.sep+"pybundle"+os.path.sep+"mkhockeydata");
mkbstring = "#!/usr/bin/env python"+str(sys.version_info[0])+"\n\n";
mkbfp = open(tempdir+os.path.sep+"pybundle"+os.path.sep+"mkhockeydata", "wb+");
mkbfp.write(mkbstring.encode());
zipfp = open(tempdir+os.path.sep+"pybundle"+os.path.sep+"mkhockeydata.zip", "rb");
mkbfp.write(zipfp.read());
mkbfp.close();
zipfp.close();
shutil.rmtree("."+os.path.sep+"bundle"+os.path.sep+"python"+str(sys.version_info[0]));
os.mkdir("."+os.path.sep+"bundle"+os.path.sep+"python"+str(sys.version_info[0]));
shutil.move(tempdir+os.path.sep+"pybundle"+os.path.sep+"mkhockeydata", "."+os.path.sep+"bundle"+os.path.sep+"python"+str(sys.version_info[0])+os.path.sep+"mkhockeydata");
os.chmod("."+os.path.sep+"bundle"+os.path.sep+"python"+str(sys.version_info[0])+os.path.sep+"mkhockeydata", 0o755)
shutil.rmtree(tempdir+os.path.sep+"pybundle");
oldpath = os.getcwd();
os.chdir("."+os.path.sep+"bundle"+os.path.sep+"python"+str(sys.version_info[0]));
curscrpath = os.path.dirname("."+os.path.sep+"mkhockeydata.py");
if(curscrpath==""):
 curscrpath = ".";
curscrpath = curscrpath+os.path.sep;
scrfile = curscrpath+"mkhockeydata.py";
if(os.path.exists(scrfile) and os.path.isfile(scrfile)):
 scrcmd = subprocess.Popen([sys.executable, scrfile, "mksymlinks"]);
 scrcmd.wait();
os.chdir(oldpath);
