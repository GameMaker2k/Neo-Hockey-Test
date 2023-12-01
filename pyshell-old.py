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

    $FileInfo: pyshell-old.py - Last Update: 12/01/2023 Ver. 0.8.4 RC 1 - Author: cooldude2k $
'''

from __future__ import print_function
import sys, traceback, code, re, readline, libhockeydata;
from sys import argv;
from libhockeydata import *;

taskfound=False;
if(len(sys.argv)<2):
 taskfound=True;
 ps1="PyShell "+str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2])+"> ";
 cmdinput=None;
 print("PyShell "+sys.version+" on "+sys.platform+"\nLoaded Python module libhockeydata "+libhockeydata.__version__+"\n");
 while(True):
  try:
   cmdinput = code.InteractiveConsole().raw_input(ps1);
  except KeyboardInterrupt:
   print("\nKeyboardInterrupt");
  except EOFError:
   print("");
   sys.exit(0);
  except Exception:
   traceback.print_exc();
  ## exec(str(cmdinput));
  try:
   exec(code.compile_command(str(cmdinput)));
  except Exception:
   traceback.print_exc();
 sys.exit(0);

if(sys.argv[1]=="sh" or sys.argv[1]=="shell" or sys.argv[1]=="pysh" or sys.argv[1]=="pyshell" or sys.argv[1]=="python"):
 taskfound=True;
 ps1="PyShell "+str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2])+"> ";
 cmdinput=None;
 print("PyShell "+sys.version+" on "+sys.platform+"\nLoaded Python module libhockeydata "+libhockeydata.__version__+"\n");
 while(True):
  try:
   cmdinput = code.InteractiveConsole().raw_input(ps1);
  except KeyboardInterrupt:
   print("\nKeyboardInterrupt");
  except EOFError:
   print("");
   sys.exit(0);
  except Exception:
   traceback.print_exc();
  ## exec(str(cmdinput));
  try:
   exec(code.compile_command(str(cmdinput)));
  except Exception:
   traceback.print_exc();
 sys.exit(0);

if(sys.argv[1]=="shebang" or sys.argv[1]=="shabang" or sys.argv[1]=="hashbang" or sys.argv[1]=="poundbang" or sys.argv[1]=="hashexclam" or sys.argv[1]=="hashpling"):
 taskfound=True;
 if(len(sys.argv)<3):
  print(str("command: "+sys.argv[0]+"\narguments: "+sys.argv[1]+"\nerror: syntax error missing arguments"));
  sys.exit(0);
 shebang = "".join(open(sys.argv[2], "r").readlines());
 exec(compile(str(shebang), "", "exec"));
 sys.exit(0);

if(sys.argv[1]=="exec" or sys.argv[1]=="run" or sys.argv[1]=="execute"):
 taskfound=True;
 argcmd = list(sys.argv);
 argcmd[0:1] = [];
 argcmd = list(argcmd);
 argcmd[0:1] = [];
 argcmd = list(argcmd);
 argcmd = " ".join(argcmd);
 exec(argcmd);

if(not taskfound):
 print(str("command: "+sys.argv[0]+"\narguments: "+sys.argv[1]+"\nerror: syntax error missing arguments"));
 sys.exit(0);
