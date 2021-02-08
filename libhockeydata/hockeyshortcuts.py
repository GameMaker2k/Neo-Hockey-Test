#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2015-2021 Game Maker 2k - https://github.com/GameMaker2k
    Copyright 2015-2021 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: hockeyshortcuts.py - Last Update: 1/15/2021 Ver. 0.5.0 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals;
import sqlite3, sys, os, re, time;
from .hockeyoopfuncs import *;
from .versioninfo import __program_name__, __project__, __project_url__, __version__, __version_date__, __version_info__, __version_date_info__, __version_date__, __revision__, __revision_id__, __version_date_plusrc__;

try:
 basestring;
except NameError:
 basestring = str;

baseint = [];
try:
 long;
 baseint.append(int);
 baseint.append(long);
except NameError:
 baseint.append(int);
baseint = tuple(baseint);

def MakeHockeyXMLFromHockeyXML(inxmlfile, xmlisfile=True, beautify=True, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(inxmlfile, xmlisfile, False);
 hockeyxmlout = MakeHockeyXMLFromHockeyArray(hockeyarray, beautify, verbose, jsonverbose);
 return hockeyxmlout;

def MakeHockeyXMLFileFromHockeyXML(inxmlfile, outxmlfile=None, xmlisfile=True, returnxml=False, beautify=True, verbose=True, jsonverbose=True):
 if(xmlisfile and (not os.path.exists(inxmlfile) or not os.path.isfile(inxmlfile))):
  return False;
 if(outxmlfile is None and xmlisfile):
  file_wo_extension, file_extension = os.path.splitext(inxmlfile);
  outxmlfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outxmlfile)[0];
 fextname = os.path.splitext(outxmlfile)[1];
 xmlfp = CompressOpenFile(outxmlfile);
 xmlstring = MakeHockeyXMLFromHockeyXML(inxmlfile, xmlisfile, beautify, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  xmlstring = xmlstring.encode();
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml):
  return xmlstring;
 if(not returnxml):
  return True;
 return True;

def MakeHockeyXMLFileFromHockeyJSON(injsonfile, outxmlfile=None, jsonisfile=True, returnxml=False, beautify=True, verbose=True, jsonverbose=True):
 if(jsonisfile and (not os.path.exists(injsonfile) or not os.path.isfile(injsonfile))):
  return False;
 if(outxmlfile is None and jsonisfile):
  file_wo_extension, file_extension = os.path.splitext(injsonfile);
  outxmlfile = file_wo_extension+".xml";
 hockeyarray = MakeHockeyArrayFromHockeyJSON(injsonfile, jsonisfile, False);
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outxmlfile)[0];
 fextname = os.path.splitext(outxmlfile)[1];
 xmlfp = CompressOpenFile(outxmlfile);
 xmlstring = MakeHockeyXMLFromHockeyArray(hockeyarray, beautify, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  xmlstring = xmlstring.encode();
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml):
  return xmlstring;
 if(not returnxml):
  return True;
 return True;

def MakeHockeyJSONFromHockeyXML(inxmlfile, xmlisfile=True, jsonindent=1, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(inxmlfile, xmlisfile, False);
 jsonstring = MakeHockeyJSONFromHockeyArray(hockeyarray, jsonindent, verbose, jsonverbose);
 return jsonstring;

def MakeHockeyJSONFileFromHockeyXML(inxmlfile, outjsonfile=None, xmlisfile=True, returnjson=False, jsonindent=1, verbose=True, jsonverbose=True):
 if(xmlisfile and (not os.path.exists(inxmlfile) or not os.path.isfile(inxmlfile))):
  return False;
 if(outjsonfile is None and xmlisfile):
  file_wo_extension, file_extension = os.path.splitext(inxmlfile);
  outjsonfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outjsonfile)[0];
 fextname = os.path.splitext(outjsonfile)[1];
 jsonfp = CompressOpenFile(outjsonfile);
 jsonstring = MakeHockeyJSONFromHockeyXML(inxmlfile, xmlisfile, jsonindent, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  jsonstring = jsonstring.encode();
 jsonfp.write(jsonstring);
 jsonfp.close();
 if(returnjson):
  return jsonstring;
 if(not returnjson):
  return True;
 return True;

def MakeHockeyJSONFromHockeyDatabase(sdbfile, returnjson=False, jsonindent=1, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(sdbfile, False);
 jsonstring = MakeHockeyJSONFromHockeyArray(hockeyarray, returnjson, jsonindent, verbose, jsonverbose);
 return jsonstring;

def MakeHockeyJSONFromHockeySQL(sqlfile, sdbfile=None, sqlisfile=True, returnjson=False, jsonindent=1, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeySQL(sqlfile, sdbfile, sqlisfile, False);
 jsonstring = MakeHockeyJSONFromHockeyArray(hockeyarray, returnjson, jsonindent, verbose, jsonverbose);
 return jsonstring;

def MakeHockeyJSONFromOldHockeyDatabase(sdbfile, returnjson=False, jsonindent=1, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(sdbfile, False);
 jsonstring = MakeHockeyJSONFromHockeyArray(hockeyarray, returnjson, jsonindent, verbose, jsonverbose);
 return jsonstring;

def MakeHockeyDatabaseFromHockeyXML(xmlfile, sdbfile=None, xmlisfile=True, returnxml=False, returndb=False, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(xmlfile, xmlisfile, False);
 hockeydbout = MakeHockeyDatabaseFromHockeyArray(hockeyarray, sdbfile, returnxml, returndb, verbose, jsonverbose);
 return hockeydbout;

def MakeHockeyDatabaseFromHockeyXMLWrite(inxmlfile, sdbfile=None, outxmlfile=None, xmlisfile=True, returnxml=False, verbose=True, jsonverbose=True):
 if(xmlisfile and (not os.path.exists(inxmlfile) or not os.path.isfile(inxmlfile))):
  return False;
 if(outxmlfile is None and xmlisfile):
  file_wo_extension, file_extension = os.path.splitext(inxmlfile);
  outxmlfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outxmlfile)[0];
 fextname = os.path.splitext(outxmlfile)[1];
 xmlfp = CompressOpenFile(outxmlfile);
 xmlstring = MakeHockeyDatabaseFromHockeyXML(inxmlfile, sdbfile, xmlisfile, True, False, verbose, jsonverbose)[0];
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  xmlstring = xmlstring.encode();
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml):
  return xmlstring;
 if(not returnxml):
  return True;
 return True;

def MakeHockeyDatabaseFromHockeySQL(sqlfile, sdbfile=None, sqlisfile=True, returnsql=False, returndb=False, verbose=True, jsonverbose=True):
 if(sqlisfile and (os.path.exists(sqlfile) and os.path.isfile(sqlfile))):
  sqlfp = open(sqlfile, "r");
  sqlstring = sqlfp.read();
  sqlfp.close();
 elif(not sqlisfile):
  sqlstring = sqlfile;
 else:
  return False;
 if(sdbfile is None and len(re.findall(r"Database\:([\w\W]+)", sqlfile))>=1):
  sdbfile = re.findall(r"Database\:([\w\W]+)", sqlfile)[0].strip();
 if(sdbfile is None and len(re.findall(r"Database\:([\w\W]+)", sqlfile))<1):
  file_wo_extension, file_extension = os.path.splitext(sqlfile);
  sdbfile = file_wo_extension+".db3";
 if(sdbfile is not None and isinstance(sdbfile, basestring)):
  sqldatacon = MakeHockeyDatabase(sdbfile);
 if(sdbfile is not None and isinstance(sdbfile, (tuple, list))):
  sqldatacon = tuple(sdbfile);
 sqldatacon[0].executescript(sqlstring);
 if(not returndb):
  CloseHockeyDatabase(sqldatacon);
 if(returndb and not returnsql):
  return [sqldatacon];
 if(returnsql and not returndb):
  return [sqlstring];
 if(returnsql and returndb):
  return [sqlstring, sqldatacon];
 if(not returnsql):
  return True;
 return True;

def MakeHockeyDatabaseFromHockeySQLWrite(insqlfile, sdbfile=None, outsqlfile=None, sqlisfile=True, returnsql=False, verbose=True, jsonverbose=True):
 if(sqlisfile and (not os.path.exists(insqlfile) or not os.path.isfile(insqlfile))):
  return False;
 if(outsqlfile is None and sqlisfile):
  file_wo_extension, file_extension = os.path.splitext(insqlfile);
  outsqlfile = file_wo_extension+".db3";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outsqlfile)[0];
 fextname = os.path.splitext(outsqlfile)[1];
 sqlfp = CompressOpenFile(outsqlfile);
 sqlstring = MakeHockeyDatabaseFromHockeySQL(insqlfile, sdbfile, sqlisfile, True, False, verbose, jsonverbose)[0];
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  sqlstring = sqlstring.encode();
 sqlfp.write(sqlstring);
 sqlfp.close();
 if(returnsql):
  return sqlstring;
 if(not returnsql):
  return True;
 return True;

def MakeHockeyPythonOOPFromHockeyXML(xmlfile, xmlisfile=True, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(xmlfile, xmlisfile, False);
 hockeypyout = MakeHockeyPythonOOPFromHockeyArray(hockeyarray, True);
 return hockeypyout;

def MakeHockeyPythonOOPFileFromHockeyXML(inxmlfile, outpyfile=None, xmlisfile=True, returnpy=False, verbose=True, jsonverbose=True):
 if(xmlisfile and (not os.path.exists(inxmlfile) or not os.path.isfile(inxmlfile))):
  return False;
 if(outpyfile is None and xmlisfile):
  file_wo_extension, file_extension = os.path.splitext(inxmlfile);
  outpyfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outpyfile)[0];
 fextname = os.path.splitext(outpyfile)[1];
 pyfp = CompressOpenFile(outpyfile);
 pystring = MakeHockeyPythonOOPFromHockeyXML(inxmlfile, xmlisfile, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  pystring = pystring.encode();
 pyfp.write(pystring);
 pyfp.close();
 if(fextname not in outextlistwd):
  os.chmod(outpyfile, 0o755);
 if(returnpy):
  return pystring;
 if(not returnpy):
  return True;
 return True;

def MakeHockeyPythonOOPAltFromHockeyXML(xmlfile, xmlisfile=True, verbose=True, jsonverbose=True, verbosepy=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(xmlfile, xmlisfile, False);
 hockeypyout = MakeHockeyPythonOOPAltFromHockeyArray(hockeyarray, verbose, jsonverbose, verbosepy);
 return hockeypyout;

def MakeHockeyPythonOOPAltFileFromHockeyXML(inxmlfile, outpyfile=None, xmlisfile=True, returnpy=False, verbose=True, jsonverbose=True, verbosepy=True):
 if(xmlisfile and (not os.path.exists(inxmlfile) or not os.path.isfile(inxmlfile))):
  return False;
 if(outpyfile is None and xmlisfile):
  file_wo_extension, file_extension = os.path.splitext(inxmlfile);
  outpyfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outpyfile)[0];
 fextname = os.path.splitext(outpyfile)[1];
 pyfp = CompressOpenFile(outpyfile);
 pystring = MakeHockeyPythonOOPAltFromHockeyXML(inxmlfile, xmlisfile, verbose, jsonverbose, verbosepy);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  pystring = pystring.encode();
 pyfp.write(pystring);
 pyfp.close();
 if(fextname not in outextlistwd):
  os.chmod(outpyfile, 0o755);
 if(returnpy):
  return pystring;
 if(not returnpy):
  return True;
 return True;

def MakeHockeyPythonFromHockeyXML(xmlfile, xmlisfile=True, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(xmlfile, xmlisfile, False);
 hockeypyout = MakeHockeyPythonFromHockeyArray(hockeyarray, True);
 return hockeypyout;

def MakeHockeyPythonFileFromHockeyXML(inxmlfile, outpyfile=None, xmlisfile=True, returnpy=False, verbose=True, jsonverbose=True):
 if(xmlisfile and (not os.path.exists(inxmlfile) or not os.path.isfile(inxmlfile))):
  return False;
 if(outpyfile is None and xmlisfile):
  file_wo_extension, file_extension = os.path.splitext(inxmlfile);
  outpyfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outpyfile)[0];
 fextname = os.path.splitext(outpyfile)[1];
 pyfp = CompressOpenFile(outpyfile);
 pystring = MakeHockeyPythonFromHockeyXML(inxmlfile, xmlisfile, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  pystring = pystring.encode();
 pyfp.write(pystring);
 pyfp.close();
 if(fextname not in outextlistwd):
  os.chmod(outpyfile, 0o755);
 if(returnpy):
  return pystring;
 if(not returnpy):
  return True;
 return True;

def MakeHockeyPythonAltFromHockeyXML(xmlfile, xmlisfile=True, verbose=True, jsonverbose=True, verbosepy=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(xmlfile, xmlisfile, False);
 hockeypyout = MakeHockeyPythonAltFromHockeyArray(hockeyarray, verbose, jsonverbose, verbosepy);
 return hockeypyout;

def MakeHockeyPythonAltFileFromHockeyXML(inxmlfile, outpyfile=None, xmlisfile=True, returnpy=False, verbose=True, jsonverbose=True, verbosepy=True):
 if(xmlisfile and (not os.path.exists(inxmlfile) or not os.path.isfile(inxmlfile))):
  return False;
 if(outpyfile is None and xmlisfile):
  file_wo_extension, file_extension = os.path.splitext(inxmlfile);
  outpyfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outpyfile)[0];
 fextname = os.path.splitext(outpyfile)[1];
 pyfp = CompressOpenFile(outpyfile);
 pystring = MakeHockeyPythonAltFromHockeyXML(inxmlfile, xmlisfile, verbose, jsonverbose, verbosepy);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  pystring = pystring.encode();
 pyfp.write(pystring);
 pyfp.close();
 if(fextname not in outextlistwd):
  os.chmod(outpyfile, 0o755);
 if(returnpy):
  return pystring;
 if(not returnpy):
  return True;
 return True;

def MakeHockeyXMLFromHockeyDatabase(sdbfile, beautify=True, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(sdbfile, False);
 hockeyxmlout = MakeHockeyXMLFromHockeyArray(hockeyarray, beautify, verbose, jsonverbose);
 return hockeyxmlout;

def MakeHockeyXMLFileFromHockeyDatabase(sdbfile, xmlfile=None, returnxml=False, beautify=True, verbose=True, jsonverbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(xmlfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  xmlfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(xmlfile)[0];
 fextname = os.path.splitext(xmlfile)[1];
 xmlfp = CompressOpenFile(xmlfile);
 xmlstring = MakeHockeyXMLFromHockeyDatabase(sdbfile, beautify, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  xmlstring = xmlstring.encode();
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml):
  return xmlstring;
 if(not returnxml):
  return True;
 return True;

def MakeHockeyXMLFromHockeySQL(sqlfile, sdbfile=None, sqlisfile=True, beautify=True, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeySQL(sqlfile, sdbfile, sqlisfile, False);
 hockeyxmlout = MakeHockeyXMLFromHockeyArray(hockeyarray, beautify, verbose, jsonverbose);
 return hockeyxmlout;

def MakeHockeyXMLFileFromHockeySQL(insqlfile, sdbfile=None, outxmlfile=None, sqlisfile=True, returnxml=False, beautify=True, verbose=True, jsonverbose=True):
 if(sqlisfile and (not os.path.exists(insqlfile) or not os.path.isfile(insqlfile))):
  return False;
 if(outxmlfile is None and sqlisfile):
  file_wo_extension, file_extension = os.path.splitext(insqlfile);
  outxmlfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outxmlfile)[0];
 fextname = os.path.splitext(outxmlfile)[1];
 xmlfp = CompressOpenFile(outxmlfile);
 xmlstring = MakeHockeyXMLFromHockeySQL(insqlfile, sdbfile, sqlisfile, beautify, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  xmlstring = xmlstring.encode();
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml):
  return xmlstring;
 if(not returnxml):
  return True;
 return True;

def MakeHockeyPythonOOPFromHockeyDatabase(sdbfile, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(sdbfile, False);
 hockeypyout = MakeHockeyPythonOOPFromHockeyArray(hockeyarray, verbose, jsonverbose);
 return hockeypyout;

def MakeHockeyPythonOOPFileFromHockeyDatabase(sdbfile, pyfile=None, returnpy=False, verbose=True, jsonverbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(pyfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  pyfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(pyfile)[0];
 fextname = os.path.splitext(pyfile)[1];
 pyfp = CompressOpenFile(pyfile);
 pystring = MakeHockeyPythonOOPFromHockeyDatabase(sdbfile, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  pystring = pystring.encode();
 pyfp.write(pystring);
 pyfp.close();
 if(fextname not in outextlistwd):
  os.chmod(pyfile, 0o755);
 if(returnpy):
  return pystring;
 if(not returnpy):
  return True;
 return True;

def MakeHockeyPythonOOPAltFromHockeyDatabase(sdbfile, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(sdbfile, False);
 hockeypyout = MakeHockeyPythonOOPAltFromHockeyArray(hockeyarray, verbose, jsonverbose);
 return hockeypyout;

def MakeHockeyPythonOOPAltFileFromHockeyDatabase(sdbfile, pyfile=None, returnpy=False, verbose=True, jsonverbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(pyfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  pyfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(pyfile)[0];
 fextname = os.path.splitext(pyfile)[1];
 pyfp = CompressOpenFile(pyfile);
 pystring = MakeHockeyPythonOOPAltFromHockeyDatabase(sdbfile, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  pystring = pystring.encode();
 pyfp.write(pystring);
 pyfp.close();
 if(fextname not in outextlistwd):
  os.chmod(pyfile, 0o755);
 if(returnpy):
  return pystring;
 if(not returnpy):
  return True;
 return True;

def MakeHockeyPythonFromHockeyDatabase(sdbfile, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(sdbfile, False);
 hockeypyout = MakeHockeyPythonFromHockeyArray(hockeyarray, verbose, jsonverbose);
 return hockeypyout;

def MakeHockeyPythonFileFromHockeyDatabase(sdbfile, pyfile=None, returnpy=False, verbose=True, jsonverbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(pyfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  pyfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(pyfile)[0];
 fextname = os.path.splitext(pyfile)[1];
 pyfp = CompressOpenFile(pyfile);
 pystring = MakeHockeyPythonFromHockeyDatabase(sdbfile, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  pystring = pystring.encode();
 pyfp.write(pystring);
 pyfp.close();
 if(fextname not in outextlistwd):
  os.chmod(pyfile, 0o755);
 if(returnpy):
  return pystring;
 if(not returnpy):
  return True;
 return True;

def MakeHockeyPythonAltFromHockeyDatabase(sdbfile, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(sdbfile, False);
 hockeypyout = MakeHockeyPythonAltFromHockeyArray(hockeyarray, verbose, jsonverbose);
 return hockeypyout;

def MakeHockeyPythonAltFileFromHockeyDatabase(sdbfile, pyfile=None, returnpy=False, verbose=True, jsonverbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(pyfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  pyfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(pyfile)[0];
 fextname = os.path.splitext(pyfile)[1];
 pyfp = CompressOpenFile(pyfile);
 pystring = MakeHockeyPythonAltFromHockeyDatabase(sdbfile, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  pystring = pystring.encode();
 pyfp.write(pystring);
 pyfp.close();
 if(fextname not in outextlistwd):
  os.chmod(pyfile, 0o755);
 if(returnpy):
  return pystring;
 if(not returnpy):
  return True;
 return True;

def MakeHockeySQLFromHockeyDatabase(sdbfile, verbose=True, jsonverbose=True):
 if(os.path.exists(sdbfile) and os.path.isfile(sdbfile) and isinstance(sdbfile, basestring)):
  sqldatacon = OpenHockeyDatabase(sdbfile);
 else:
  if(sdbfile is not None and isinstance(sdbfile, (tuple, list))):
   sqldatacon = tuple(sdbfile);
  else:
   return False;
 sqldump = "-- "+__program_name__+" SQL Dumper\n";
 sqldump = sqldump+"-- version "+__version__+"\n";
 sqldump = sqldump+"-- "+__project_url__+"\n";
 sqldump = sqldump+"--\n";
 sqldump = sqldump+"-- Generation Time: "+time.strftime("%B %d, %Y at %I:%M %p", time.localtime())+"\n";
 sqldump = sqldump+"-- SQLite Server version: "+sqlite3.sqlite_version+"\n";
 sqldump = sqldump+"-- PySQLite version: "+sqlite3.version+"\n";
 sqldump = sqldump+"-- Python Version: "+str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2])+"\n\n";
 sqldump = sqldump+"--\n";
 sqldump = sqldump+"-- Database: "+sdbfile+"\n";
 sqldump = sqldump+"--\n\n";
 sqldump = sqldump+"-- --------------------------------------------------------\n\n";
 all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games"];
 table_list = ['HockeyLeagues'];
 getleague_num_tmp = sqldatacon[0].execute("SELECT COUNT(*) FROM HockeyLeagues").fetchone()[0];
 getleague_tmp = sqldatacon[0].execute("SELECT LeagueName FROM HockeyLeagues");
 for leagueinfo_tmp in getleague_tmp:
  for cur_tab in all_table_list:
   table_list.append(leagueinfo_tmp[0]+cur_tab);
 for get_cur_tab in table_list:
  tresult = sqldatacon[0].execute("SELECT * FROM "+get_cur_tab);
  tmbcor = sqldatacon[1].cursor();
  tabresult = tmbcor.execute("SELECT * FROM sqlite_master WHERE type=\"table\" and tbl_name=\""+get_cur_tab+"\";").fetchone()[4];
  tabresultcol = list(map(lambda x: x[0], sqldatacon[0].description));
  tresult_list = [];
  sqldump = sqldump+"--\n";
  sqldump = sqldump+"-- Table structure for table "+str(get_cur_tab)+"\n";
  sqldump = sqldump+"--\n\n";
  sqldump = sqldump+"DROP TABLE IF EXISTS "+get_cur_tab+";\n\n"+tabresult+";\n\n";
  sqldump = sqldump+"--\n";
  sqldump = sqldump+"-- Dumping data for table "+str(get_cur_tab)+"\n";
  sqldump = sqldump+"--\n\n";
  get_insert_stmt_full = "";
  for tresult_tmp in tresult:
   get_insert_stmt = "INSERT INTO "+str(get_cur_tab)+" (";
   get_insert_stmt_val = "(";
   for result_cal_val in tabresultcol:
    get_insert_stmt += str(result_cal_val)+", ";
   for result_val in tresult_tmp:
    if(isinstance(result_val, basestring)):
     get_insert_stmt_val += "\""+str(result_val)+"\", ";
    if(isinstance(result_val, baseint)):
     get_insert_stmt_val += ""+str(result_val)+", ";
    if(isinstance(result_val, float)):
     get_insert_stmt_val += ""+str(result_val)+", ";
   get_insert_stmt = get_insert_stmt[:-2]+") VALUES \n";
   get_insert_stmt_val = get_insert_stmt_val[:-2]+");";
   get_insert_stmt_full += str(get_insert_stmt+get_insert_stmt_val)+"\n";
  sqldump = sqldump+get_insert_stmt_full+"\n-- --------------------------------------------------------\n\n";
 CloseHockeyDatabase(sqldatacon);
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(MakeHockeyArrayFromHockeyDatabase(leaguearrayout, verbose=False, jsonverbose=True), verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(MakeHockeyArrayFromHockeyDatabase(leaguearrayout, verbose=False, jsonverbose=True), verbose=False, jsonverbose=True));
 return sqldump;

def MakeHockeySQLFileFromHockeyDatabase(sdbfile, sqlfile=None, returnsql=False, verbose=True, jsonverbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(sqlfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  sqlfile = file_wo_extension+".sql";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outsqlfile)[0];
 fextname = os.path.splitext(outsqlfile)[1];
 sqlfp = CompressOpenFile(outsqlfile);
 sqlstring = MakeHockeySQLFromHockeyDatabase(sdbfile, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  sqlstring = sqlstring.encode();
 sqlfp.write(sqlstring);
 sqlfp.close();
 if(returnsql):
  return sqlstring;
 if(not returnsql):
  return True;
 return True;

def MakeHockeySQLFromHockeyXML(xmlfile, xmlisfile=True, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(xmlfile, xmlisfile, False);
 sdbfilename = ":memory:";
 if(xmlisfile):
  sdbfilename = os.path.splitext(xmlfile)[0]+".db3";
 hockeysqlout = MakeHockeySQLFromHockeyArray(hockeyarray, sdbfilename, verbose, jsonverbose);
 return hockeysqlout;

def MakeHockeySQLFileFromHockeyXML(xmlfile, sqlfile=None, xmlisfile=True, returnsql=False, verbose=True, jsonverbose=True):
 if(not xmlisfile and (not os.path.exists(xmlfile) and not os.path.isfile(xmlfile))):
  return False;
 if(sqlfile is None and xmlisfile):
  file_wo_extension, file_extension = os.path.splitext(xmlfile);
  sqlfile = file_wo_extension+".sql";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outsqlfile)[0];
 fextname = os.path.splitext(outsqlfile)[1];
 sqlfp = CompressOpenFile(outsqlfile);
 sqlstring = MakeHockeySQLFromHockeyXML(xmlfile, xmlisfile, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  sqlstring = sqlstring.encode();
 sqlfp.write(sqlstring);
 sqlfp.close();
 if(returnsql):
  return sqlstring;
 if(not returnsql):
  return True;
 return True;

def MakeHockeyXMLFromOldHockeyDatabase(sdbfile, beautify=True, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromOldHockeyDatabase(sdbfile, False);
 hockeyxmlout = MakeHockeyXMLFromHockeyArray(hockeyarray, beautify, verbose, jsonverbose);
 return hockeyxmlout;

def MakeHockeyXMLFileFromOldHockeyDatabase(sdbfile, xmlfile=None, returnxml=False, beautify=True, verbose=True, jsonverbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(xmlfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  xmlfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(xmlfile)[0];
 fextname = os.path.splitext(xmlfile)[1];
 xmlfp = CompressOpenFile(xmlfile);
 xmlstring = MakeHockeyXMLFromOldHockeyDatabase(sdbfile, beautify, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  xmlstring = xmlstring.encode();
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml):
  return xmlstring;
 if(not returnxml):
  return True;
 return True;

def MakeHockeyPythonOOPFromOldHockeyDatabase(sdbfile, beautify=True, verbose=True, jsonverbose=True):
 xmlstring = MakeHockeyXMLFromOldHockeyDatabase(sdbfile, beautify, False);
 pystring = MakeHockeyPythonOOPFromHockeyXML(xmlstring, False, verbose, jsonverbose);
 return pystring;

def MakeHockeyPythonOOPFileFromOldHockeyDatabase(sdbfile, pyfile=None, returnpy=False, verbose=True, jsonverbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(pyfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  pyfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(pyfile)[0];
 fextname = os.path.splitext(pyfile)[1];
 pyfp = CompressOpenFile(pyfile);
 pystring = MakeHockeyPythonOOPFromOldHockeyDatabase(sdbfile, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  pystring = pystring.encode();
 pyfp.write(pystring);
 pyfp.close();
 if(fextname not in outextlistwd):
  os.chmod(pyfile, 0o755);
 if(returnpy):
  return pystring;
 if(not returnpy):
  return True;
 return True;

def MakeHockeyPythonOOPAltFromOldHockeyDatabase(sdbfile, beautify=True, verbose=True, jsonverbose=True):
 xmlstring = MakeHockeyXMLFromOldHockeyDatabase(sdbfile, beautify, False);
 pystring = MakeHockeyPythonOOPAltFromHockeyXML(xmlstring, False, verbose, jsonverbose);
 return pystring;

def MakeHockeyPythonOOPAltFileFromOldHockeyDatabase(sdbfile, pyfile=None, returnpy=False, verbose=True, jsonverbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(pyfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  pyfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(pyfile)[0];
 fextname = os.path.splitext(pyfile)[1];
 pyfp = CompressOpenFile(pyfile);
 pystring = MakeHockeyPythonOOPAltFromOldHockeyDatabase(sdbfile, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  pystring = pystring.encode();
 pyfp.write(pystring);
 pyfp.close();
 if(fextname not in outextlistwd):
  os.chmod(pyfile, 0o755);
 if(returnpy):
  return pystring;
 if(not returnpy):
  return True;
 return True;

def MakeHockeyPythonFromOldHockeyDatabase(sdbfile, beautify=True, verbose=True, jsonverbose=True):
 xmlstring = MakeHockeyXMLFromOldHockeyDatabase(sdbfile, beautify, False);
 pystring = MakeHockeyPythonFromHockeyXML(xmlstring, False, verbose, jsonverbose);
 return pystring;

def MakeHockeyPythonFileFromOldHockeyDatabase(sdbfile, pyfile=None, returnpy=False, verbose=True, jsonverbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(pyfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  pyfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(pyfile)[0];
 fextname = os.path.splitext(pyfile)[1];
 pyfp = CompressOpenFile(pyfile);
 pystring = MakeHockeyPythonFromOldHockeyDatabase(sdbfile, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  pystring = pystring.encode();
 pyfp.write(pystring);
 pyfp.close();
 if(fextname not in outextlistwd):
  os.chmod(pyfile, 0o755);
 if(returnpy):
  return pystring;
 if(not returnpy):
  return True;
 return True;

def MakeHockeyPythonAltFromOldHockeyDatabase(sdbfile, beautify=True, verbose=True, jsonverbose=True):
 xmlstring = MakeHockeyXMLFromOldHockeyDatabase(sdbfile, beautify, False);
 pystring = MakeHockeyPythonAltFromHockeyXML(xmlstring, False, verbose, jsonverbose);
 return pystring;

def MakeHockeyPythonAltFileFromOldHockeyDatabase(sdbfile, pyfile=None, returnpy=False, verbose=True, jsonverbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(pyfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  pyfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(pyfile)[0];
 fextname = os.path.splitext(pyfile)[1];
 pyfp = CompressOpenFile(pyfile);
 pystring = MakeHockeyPythonAltFromOldHockeyDatabase(sdbfile, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  pystring = pystring.encode();
 pyfp.write(pystring);
 pyfp.close();
 if(fextname not in outextlistwd):
  os.chmod(pyfile, 0o755);
 if(returnpy):
  return pystring;
 if(not returnpy):
  return True;
 return True;

def MakeHockeySQLFromOldHockeyDatabase(sdbfile, beautify=True, verbose=True, jsonverbose=True):
 xmlstring = MakeHockeyXMLFromOldHockeyDatabase(sdbfile, beautify, False);
 sqldump = MakeHockeySQLFromHockeyXML(xmlstring, False, True, verbose, jsonverbose);
 return sqldump;

def MakeHockeySQLFileFromOldHockeyDatabase(sdbfile, sqlfile=None, returnsql=False, verbose=True, jsonverbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(sqlfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  sqlfile = file_wo_extension+".sql";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outsqlfile)[0];
 fextname = os.path.splitext(outsqlfile)[1];
 sqlfp = CompressOpenFile(outsqlfile);
 sqlstring = MakeHockeySQLFromOldHockeyDatabase(sdbfile, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  sqlstring = sqlstring.encode();
 sqlfp.write(sqlstring);
 sqlfp.close();
 if(returnsql):
  return sqlstring;
 if(not returnsql):
  return True;
 return True;

def MakeHockeySQLiteArrayFromHockeyArray(inhockeyarray, verbose=True, jsonverbose=True):
 if(not CheckHockeyArray(inhockeyarray)):
  return False;
 hockeydbin = MakeHockeyDatabaseFromHockeyArray(inhockeyarray, ":memory:", True, True, False);
 hockeyarray = MakeHockeySQLiteArrayFromHockeyDatabase(hockeydbin[1], True);
 if(not CheckHockeySQLiteArray(hockeyarray)):
  return False;
 return hockeyarray;
