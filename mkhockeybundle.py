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

import os, sys, shutil, subprocess, tempfile, subprocess, platform;

tempdir = tempfile.gettempdir();
if(os.sep=="\\"):
 tempdir = tempdir.replace(os.sep, "/");
elif(os.path.sep=="\\"):
 tempdir = tempdir.replace(os.path.sep, "/");

pyimplementation = platform.python_implementation();

if(pyimplementation=="CPython"):
 pystring = "python"+str(sys.version_info[0]);
elif(pyimplementation=="IronPython"):
 pystring = "ipy"+str(sys.version_info[0]);
elif(pyimplementation=="PyPy"):
 if(sys.version_info[0]==2):
  pystring = "pypy";
 elif(sys.version_info[0]==3):
  pystring = "pypy"+str(sys.version_info[0]);
 else:
  sys.exit(1);
else:
 sys.exit(1);

if(os.path.exists(tempdir+"/pybundle") and os.path.isfile(tempdir+"/pybundle")):
 os.unlink(tempdir+"/pybundle");
if(os.path.exists(tempdir+"/pybundle") and os.path.isdir(tempdir+"/pybundle")):
 shutil.rmtree(tempdir+"/pybundle");
os.mkdir(tempdir+"/pybundle");
if(os.path.exists(tempdir+"/pybundle/__main__.py") and os.path.isfile(tempdir+"/pybundle/__main__.py")):
 os.unlink(tempdir+"/pybundle/__main__.py");
if(os.path.exists(tempdir+"/pybundle/__main__.py") and os.path.isdir(tempdir+"/pybundle/__main__.py")):
 shutil.rmtree(tempdir+"/pybundle/__main__.py");
shutil.copy2("./mkhockeydata.py", tempdir+"/pybundle/__main__.py");
if(os.path.exists(tempdir+"/pybundle/libhockeydata") and os.path.isfile(tempdir+"/pybundle/libhockeydata")):
 os.unlink(tempdir+"/pybundle/libhockeydata");
if(os.path.exists(tempdir+"/pybundle/libhockeydata") and os.path.isdir(tempdir+"/pybundle/libhockeydata")):
 shutil.rmtree(tempdir+"/pybundle/libhockeydata");
shutil.copytree("./libhockeydata", tempdir+"/pybundle/libhockeydata");
if(os.path.exists(tempdir+"/mkhockeydata.zip") and os.path.isfile(tempdir+"/mkhockeydata.zip")):
 os.unlink(tempdir+"/mkhockeydata.zip");
if(os.path.exists(tempdir+"/mkhockeydata.zip") and os.path.isdir(tempdir+"/mkhockeydata.zip")):
 shutil.rmtree(tempdir+"/mkhockeydata.zip");
shutil.make_archive(tempdir+"/mkhockeydata", "zip", tempdir+"/pybundle");
if(os.path.exists(tempdir+"/pybundle/mkhockeydata.zip") and os.path.isfile(tempdir+"/pybundle/mkhockeydata.zip")):
 os.unlink(tempdir+"/pybundle/mkhockeydata.zip");
if(os.path.exists(tempdir+"/pybundle/mkhockeydata.zip") and os.path.isdir(tempdir+"/pybundle/mkhockeydata.zip")):
 shutil.rmtree(tempdir+"/pybundle/mkhockeydata.zip");
shutil.move(tempdir+"/mkhockeydata.zip", tempdir+"/pybundle/mkhockeydata.zip");
if(os.path.exists(tempdir+"/pybundle/mkhockeydata") and os.path.isfile(tempdir+"/pybundle/mkhockeydata")):
 os.unlink(tempdir+"/pybundle/mkhockeydata");
if(os.path.exists(tempdir+"/pybundle/mkhockeydata") and os.path.isdir(tempdir+"/pybundle/mkhockeydata")):
 shutil.rmtree(tempdir+"/pybundle/mkhockeydata");
mkbstring = "#!/usr/bin/env "+pystring+"\n\n";
mkbfp = open(tempdir+"/pybundle/mkhockeydata", "wb+");
mkbfp.write(mkbstring.encode());
zipfp = open(tempdir+"/pybundle/mkhockeydata.zip", "rb");
mkbfp.write(zipfp.read());
mkbfp.close();
zipfp.close();
shutil.rmtree("./bundle/"+pystring);
os.mkdir("./bundle/"+pystring);
shutil.move(tempdir+"/pybundle/mkhockeydata", "./bundle/"+pystring+"/mkhockeydata");
os.chmod("./bundle/"+pystring+"/mkhockeydata", 0o755)
shutil.rmtree(tempdir+"/pybundle");
oldpath = os.getcwd();
os.chdir("./bundle/"+pystring);
curscrpath = os.path.dirname("./mkhockeydata");
if(curscrpath==""):
 curscrpath = ".";
if(os.sep=="\\"):
 curscrpath = curscrpath.replace(os.sep, "/");
elif(os.path.sep=="\\"):
 curscrpath = curscrpath.replace(os.path.sep, "/");
curscrpath = curscrpath+os.path.sep;
scrfile = curscrpath+"mkhockeydata";
if(os.path.exists(scrfile) and os.path.isfile(scrfile)):
 scrcmd = subprocess.Popen([sys.executable, scrfile, "mksymlinks"]);
 scrcmd.wait();
os.chdir(oldpath);
