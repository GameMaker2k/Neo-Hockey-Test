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
from .versioninfo import __author__, __copyright__, __credits__, __email__, __license__, __license_string__, __maintainer__, __program_name__, __program_alt_name__, __project__, __project_url__, __project_release_url__, __version__, __version_alt__, __version_date__, __version_date_alt__, __version_info__, __version_date_info__, __version_date__, __revision__, __revision_id__, __version_date_plusrc__, __status__, version_date, version_info;

try:
 basestring;
except NameError:
 basestring = str;

baseint = [];
try:
 baseint.append(long);
 baseint.insert(0, int);
except NameError:
 baseint.append(int);
baseint = tuple(baseint);

def MakeHockeySQLiteJSONFromHockeySQLiteArray(inhockeyarray, jsonindent=1, verbose=True, jsonverbose=True):
 jsonstring = MakeHockeyJSONFromHockeyArray(inhockeyarray, jsonindent, verbose, jsonverbose);
 return jsonstring;

def MakeHockeySQLiteJSONFileFromHockeySQLiteArray(inhockeyarray, outjsonfile=None, returnjson=False, jsonindent=1, verbose=True, jsonverbose=True):
 jsonstring = MakeHockeyJSONFileFromHockeyArray(inhockeyarray, outjsonfile, returnjson, jsonindent, verbose, jsonverbose);
 return jsonstring;

def MakeHockeySQLiteArrayFromHockeySQLiteJSON(injsonfile, jsonisfile=True, verbose=True, jsonverbose=True):
 jsonstring = MakeHockeyArrayFromHockeyJSON(injsonfile, jsonisfile, verbose, jsonverbose);
 return jsonstring;

def MakeHockeySQLitePickleFromHockeySQLiteArray(inhockeyarray, verbose=True, jsonverbose=True):
 picklestringp = MakeHockeyPickleFromHockeyArray(inhockeyarray, verbose, jsonverbose);
 return picklestring;

def MakeHockeySQLitePickleFileFromHockeySQLiteArray(inhockeyarray, outpicklefile=None, returnjson=False, verbose=True, jsonverbose=True):
 picklestring = MakeHockeyPickleFileFromHockeyArray(inhockeyarray, outpicklefile, returnjson, verbose, jsonverbose);
 return picklestring;

def MakeHockeySQLiteArrayFromHockeySQLitePickle(inpicklefile, pickleisfile=True, verbose=True, jsonverbose=True):
 picklestring = MakeHockeyArrayFromHockeyPickle(injsonfile, pickleisfile, verbose, jsonverbose);
 return picklestring;

def MakeHockeySQLiteMarshalFromHockeySQLiteArray(inhockeyarray, verbose=True, jsonverbose=True):
 marshalstring = MakeHockeyMarshalFromHockeyArray(inhockeyarray, verbose, jsonverbose);
 return marshalstring;

def MakeHockeySQLiteMarshalFileFromHockeySQLiteArray(inhockeyarray, outmarshalfile=None, returnjson=False, verbose=True, jsonverbose=True):
 marshalstring = MakeHockeyMarshalFileFromHockeyArray(inhockeyarray, outmarshalfile, returnjson, verbose, jsonverbose);
 return marshalstring;

def MakeHockeySQLiteArrayFromHockeySQLiteMarshal(inmarshalfile, pickleisfile=True, verbose=True, jsonverbose=True):
 marshalstring = MakeHockeyArrayFromHockeyMarshal(injsonfile, pickleisfile, verbose, jsonverbose);
 return marshalstring;

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

def MakeHockeyJSONFromHockeyDatabase(insdbfile, returnjson=False, jsonindent=1, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(insdbfile, False);
 jsonstring = MakeHockeyJSONFromHockeyArray(hockeyarray, returnjson, jsonindent, verbose, jsonverbose);
 return jsonstring;

def MakeHockeyJSONFromHockeySQL(insqlfile, insdbfile=None, sqlisfile=True, returnjson=False, jsonindent=1, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeySQL(insqlfile, insdbfile, sqlisfile, False);
 jsonstring = MakeHockeyJSONFromHockeyArray(hockeyarray, returnjson, jsonindent, verbose, jsonverbose);
 return jsonstring;

def MakeHockeyJSONFromOldHockeyDatabase(insdbfile, returnjson=False, jsonindent=1, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(insdbfile, False);
 jsonstring = MakeHockeyJSONFromHockeyArray(hockeyarray, returnjson, jsonindent, verbose, jsonverbose);
 return jsonstring;

def MakeHockeyDatabaseFromHockeyXML(inxmlfile, outsdbfile=None, xmlisfile=True, returndb=False, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(inxmlfile, xmlisfile, False);
 hockeydbout = MakeHockeyDatabaseFromHockeyArray(hockeyarray, outsdbfile, returndb, verbose, jsonverbose);
 return hockeydbout;

def MakeHockeyDatabaseFromHockeySQL(insqlfile, outsdbfile=None, sqlisfile=True, returndb=False, verbose=True, jsonverbose=True):
 if(sqlisfile and (os.path.exists(insqlfile) and os.path.isfile(insqlfile))):
  sqlfp = open(insqlfile, "r");
  sqlstring = sqlfp.read();
  sqlfp.close();
 elif(not sqlisfile):
  sqlstring = insqlfile;
 else:
  return False;
 if(outsdbfile is None and len(re.findall(r"Database\:([\w\W]+)", insqlfile))>=1):
  outsdbfile = re.findall(r"Database\:([\w\W]+)", insqlfile)[0].strip();
 if(outsdbfile is None and len(re.findall(r"Database\:([\w\W]+)", insqlfile))<1):
  file_wo_extension, file_extension = os.path.splitext(insqlfile);
  outsdbfile = file_wo_extension+".db3";
 if(outsdbfile is not None and isinstance(outsdbfile, basestring)):
  sqldatacon = MakeHockeyDatabase(outsdbfile);
 if(outsdbfile is not None and isinstance(outsdbfile, (tuple, list))):
  sqldatacon = tuple(outsdbfile);
 sqldatacon[0].executescript(sqlstring);
 if(not returndb):
  CloseHockeyDatabase(sqldatacon);
 if(returndb):
  return sqldatacon;
 if(not returndb):
  return True;
 return True;

def MakeHockeyPythonOOPFromHockeyXML(inxmlfile, xmlisfile=True, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(inxmlfile, xmlisfile, False);
 hockeypyout = MakeHockeyPythonOOPFromHockeyArray(hockeyarray, verbose, jsonverbose);
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

def MakeHockeyPythonOOPAltFromHockeyXML(inxmlfile, xmlisfile=True, verbose=True, jsonverbose=True, verbosepy=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(inxmlfile, xmlisfile, False);
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

def MakeHockeyPythonFromHockeyXML(inxmlfile, xmlisfile=True, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(inxmlfile, xmlisfile, False);
 hockeypyout = MakeHockeyPythonFromHockeyArray(hockeyarray, verbose, jsonverbose);
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

def MakeHockeyPythonAltFromHockeyXML(inxmlfile, xmlisfile=True, verbose=True, jsonverbose=True, verbosepy=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(inxmlfile, xmlisfile, False);
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

def MakeHockeyXMLFromHockeyDatabase(insdbfile, beautify=True, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(insdbfile, False);
 hockeyxmlout = MakeHockeyXMLFromHockeyArray(hockeyarray, beautify, verbose, jsonverbose);
 return hockeyxmlout;

def MakeHockeyXMLFileFromHockeyDatabase(insdbfile, xmlfile=None, returnxml=False, beautify=True, verbose=True, jsonverbose=True):
 if(not os.path.exists(insdbfile) or not os.path.isfile(insdbfile)):
  return False;
 if(xmlfile is None):
  file_wo_extension, file_extension = os.path.splitext(insdbfile);
  xmlfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(xmlfile)[0];
 fextname = os.path.splitext(xmlfile)[1];
 xmlfp = CompressOpenFile(xmlfile);
 xmlstring = MakeHockeyXMLFromHockeyDatabase(insdbfile, beautify, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  xmlstring = xmlstring.encode();
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml):
  return xmlstring;
 if(not returnxml):
  return True;
 return True;

def MakeHockeyXMLFromHockeySQL(insqlfile, insdbfile=None, sqlisfile=True, beautify=True, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeySQL(insqlfile, insdbfile, sqlisfile, False);
 hockeyxmlout = MakeHockeyXMLFromHockeyArray(hockeyarray, beautify, verbose, jsonverbose);
 return hockeyxmlout;

def MakeHockeyXMLFileFromHockeySQL(insqlfile, insdbfile=None, outxmlfile=None, sqlisfile=True, returnxml=False, beautify=True, verbose=True, jsonverbose=True):
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
 xmlstring = MakeHockeyXMLFromHockeySQL(insqlfile, insdbfile, sqlisfile, beautify, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  xmlstring = xmlstring.encode();
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml):
  return xmlstring;
 if(not returnxml):
  return True;
 return True;

def MakeHockeyPythonOOPFromHockeyDatabase(insdbfile, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(insdbfile, False);
 hockeypyout = MakeHockeyPythonOOPFromHockeyArray(hockeyarray, verbose, jsonverbose);
 return hockeypyout;

def MakeHockeyPythonOOPFileFromHockeyDatabase(insdbfile, outpyfile=None, returnpy=False, verbose=True, jsonverbose=True):
 if(not os.path.exists(insdbfile) or not os.path.isfile(insdbfile)):
  return False;
 if(outpyfile is None):
  file_wo_extension, file_extension = os.path.splitext(insdbfile);
  outpyfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outpyfile)[0];
 fextname = os.path.splitext(outpyfile)[1];
 pyfp = CompressOpenFile(outpyfile);
 pystring = MakeHockeyPythonOOPFromHockeyDatabase(insdbfile, verbose, jsonverbose);
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

def MakeHockeyPythonOOPAltFromHockeyDatabase(insdbfile, verbose=True, jsonverbose=True, verbosepy=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(insdbfile, False);
 hockeypyout = MakeHockeyPythonOOPAltFromHockeyArray(hockeyarray, verbose, jsonverbose, verbosepy);
 return hockeypyout;

def MakeHockeyPythonOOPAltFileFromHockeyDatabase(insdbfile, outpyfile=None, returnpy=False, verbose=True, jsonverbose=True, verbosepy=True):
 if(not os.path.exists(insdbfile) or not os.path.isfile(insdbfile)):
  return False;
 if(outpyfile is None):
  file_wo_extension, file_extension = os.path.splitext(insdbfile);
  outpyfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outpyfile)[0];
 fextname = os.path.splitext(outpyfile)[1];
 pyfp = CompressOpenFile(outpyfile);
 pystring = MakeHockeyPythonOOPAltFromHockeyDatabase(insdbfile, verbose, jsonverbose, verbosepy);
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

def MakeHockeyPythonFromHockeyDatabase(insdbfile, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(insdbfile, False);
 hockeypyout = MakeHockeyPythonFromHockeyArray(hockeyarray, verbose, jsonverbose);
 return hockeypyout;

def MakeHockeyPythonFileFromHockeyDatabase(insdbfile, outpyfile=None, returnpy=False, verbose=True, jsonverbose=True):
 if(not os.path.exists(insdbfile) or not os.path.isfile(insdbfile)):
  return False;
 if(outpyfile is None):
  file_wo_extension, file_extension = os.path.splitext(insdbfile);
  outpyfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outpyfile)[0];
 fextname = os.path.splitext(outpyfile)[1];
 pyfp = CompressOpenFile(outpyfile);
 pystring = MakeHockeyPythonFromHockeyDatabase(insdbfile, verbose, jsonverbose);
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

def MakeHockeyPythonAltFromHockeyDatabase(insdbfile, verbose=True, jsonverbose=True, verbosepy=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(insdbfile, False);
 hockeypyout = MakeHockeyPythonAltFromHockeyArray(hockeyarray, verbose, jsonverbose, verbosepy);
 return hockeypyout;

def MakeHockeyPythonAltFileFromHockeyDatabase(insdbfile, outpyfile=None, returnpy=False, verbose=True, jsonverbose=True, verbosepy=True):
 if(not os.path.exists(insdbfile) or not os.path.isfile(insdbfile)):
  return False;
 if(outpyfile is None):
  file_wo_extension, file_extension = os.path.splitext(insdbfile);
  outpyfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outpyfile)[0];
 fextname = os.path.splitext(outpyfile)[1];
 pyfp = CompressOpenFile(outpyfile);
 pystring = MakeHockeyPythonAltFromHockeyDatabase(insdbfile, verbose, jsonverbose, verbosepy);
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

def MakeHockeySQLFromHockeyXML(inxmlfile, xmlisfile=True, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(inxmlfile, xmlisfile, False);
 sdbfilename = ":memory:";
 if(xmlisfile):
  sdbfilename = os.path.splitext(inxmlfile)[0]+".db3";
 hockeysqlout = MakeHockeySQLFromHockeyArray(hockeyarray, sdbfilename, verbose, jsonverbose);
 return hockeysqlout;

def MakeHockeySQLFileFromHockeyXML(inxmlfile, outsqlfile=None, xmlisfile=True, returnsql=False, verbose=True, jsonverbose=True):
 if(not xmlisfile and (not os.path.exists(inxmlfile) and not os.path.isfile(inxmlfile))):
  return False;
 if(outsqlfile is None and xmlisfile):
  file_wo_extension, file_extension = os.path.splitext(inxmlfile);
  outsqlfile = file_wo_extension+".sql";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outsqlfile)[0];
 fextname = os.path.splitext(outsqlfile)[1];
 sqlfp = CompressOpenFile(outsqlfile);
 sqlstring = MakeHockeySQLFromHockeyXML(inxmlfile, xmlisfile, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  sqlstring = sqlstring.encode();
 sqlfp.write(sqlstring);
 sqlfp.close();
 if(returnsql):
  return sqlstring;
 if(not returnsql):
  return True;
 return True;

def MakeHockeyXMLFromOldHockeyDatabase(insdbfile, beautify=True, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromOldHockeyDatabase(insdbfile, False);
 hockeyxmlout = MakeHockeyXMLFromHockeyArray(hockeyarray, beautify, verbose, jsonverbose);
 return hockeyxmlout;

def MakeHockeyXMLFileFromOldHockeyDatabase(insdbfile, outxmlfile=None, returnxml=False, beautify=True, verbose=True, jsonverbose=True):
 if(not os.path.exists(insdbfile) or not os.path.isfile(insdbfile)):
  return False;
 if(outxmlfile is None):
  file_wo_extension, file_extension = os.path.splitext(insdbfile);
  otxmlfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outxmlfile)[0];
 fextname = os.path.splitext(outxmlfile)[1];
 xmlfp = CompressOpenFile(outxmlfile);
 xmlstring = MakeHockeyXMLFromOldHockeyDatabase(insdbfile, beautify, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  xmlstring = xmlstring.encode();
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml):
  return xmlstring;
 if(not returnxml):
  return True;
 return True;

def MakeHockeyPythonOOPFromOldHockeyDatabase(insdbfile, beautify=True, verbose=True, jsonverbose=True):
 xmlstring = MakeHockeyXMLFromOldHockeyDatabase(insdbfile, beautify, False);
 pystring = MakeHockeyPythonOOPFromHockeyXML(xmlstring, False, verbose, jsonverbose);
 return pystring;

def MakeHockeyPythonOOPFileFromOldHockeyDatabase(insdbfile, outpyfile=None, returnpy=False, verbose=True, jsonverbose=True):
 if(not os.path.exists(insdbfile) or not os.path.isfile(insdbfile)):
  return False;
 if(outpyfile is None):
  file_wo_extension, file_extension = os.path.splitext(insdbfile);
  outpyfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outpyfile)[0];
 fextname = os.path.splitext(outpyfile)[1];
 pyfp = CompressOpenFile(outpyfile);
 pystring = MakeHockeyPythonOOPFromOldHockeyDatabase(insdbfile, verbose, jsonverbose);
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

def MakeHockeyPythonOOPAltFromOldHockeyDatabase(insdbfile, beautify=True, verbose=True, jsonverbose=True, verbosepy=True):
 xmlstring = MakeHockeyXMLFromOldHockeyDatabase(insdbfile, beautify, False);
 pystring = MakeHockeyPythonOOPAltFromHockeyXML(xmlstring, False, verbose, jsonverbose, verbosepy);
 return pystring;

def MakeHockeyPythonOOPAltFileFromOldHockeyDatabase(insdbfile, outpyfile=None, returnpy=False, verbose=True, jsonverbose=True, verbosepy=True):
 if(not os.path.exists(insdbfile) or not os.path.isfile(insdbfile)):
  return False;
 if(outpyfile is None):
  file_wo_extension, file_extension = os.path.splitext(insdbfile);
  outpyfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outpyfile)[0];
 fextname = os.path.splitext(outpyfile)[1];
 pyfp = CompressOpenFile(outpyfile);
 pystring = MakeHockeyPythonOOPAltFromOldHockeyDatabase(insdbfile, verbose, jsonverbose, verbosepy);
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

def MakeHockeyPythonFromOldHockeyDatabase(insdbfile, beautify=True, verbose=True, jsonverbose=True):
 xmlstring = MakeHockeyXMLFromOldHockeyDatabase(insdbfile, beautify, False);
 pystring = MakeHockeyPythonFromHockeyXML(xmlstring, False, verbose, jsonverbose);
 return pystring;

def MakeHockeyPythonFileFromOldHockeyDatabase(insdbfile, outpyfile=None, returnpy=False, verbose=True, jsonverbose=True):
 if(not os.path.exists(insdbfile) or not os.path.isfile(insdbfile)):
  return False;
 if(outpyfile is None):
  file_wo_extension, file_extension = os.path.splitext(insdbfile);
  outpyfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outpyfile)[0];
 fextname = os.path.splitext(outpyfile)[1];
 pyfp = CompressOpenFile(outpyfile);
 pystring = MakeHockeyPythonFromOldHockeyDatabase(insdbfile, verbose, jsonverbose);
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

def MakeHockeyPythonAltFromOldHockeyDatabase(insdbfile, beautify=True, verbose=True, jsonverbose=True, verbosepy=True):
 xmlstring = MakeHockeyXMLFromOldHockeyDatabase(insdbfile, beautify, False);
 pystring = MakeHockeyPythonAltFromHockeyXML(xmlstring, False, verbose, jsonverbose, verbosepy);
 return pystring;

def MakeHockeyPythonAltFileFromOldHockeyDatabase(insdbfile, outpyfile=None, returnpy=False, verbose=True, jsonverbose=True, verbosepy=True):
 if(not os.path.exists(insdbfile) or not os.path.isfile(insdbfile)):
  return False;
 if(outpyfile is None):
  file_wo_extension, file_extension = os.path.splitext(insdbfile);
  outpyfile = file_wo_extension+".xml";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outpyfile)[0];
 fextname = os.path.splitext(outpyfile)[1];
 pyfp = CompressOpenFile(outpyfile);
 pystring = MakeHockeyPythonAltFromOldHockeyDatabase(insdbfile, verbose, jsonverbose, verbosepy);
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

def MakeHockeySQLFromOldHockeyDatabase(insdbfile, verbose=True, jsonverbose=True):
 xmlstring = MakeHockeyXMLFromOldHockeyDatabase(insdbfile, True, False);
 sqldump = MakeHockeySQLFromHockeyXML(xmlstring, False, True, verbose, jsonverbose);
 return sqldump;

def MakeHockeySQLFileFromOldHockeyDatabase(insdbfile, outsqlfile=None, returnsql=False, verbose=True, jsonverbose=True):
 if(not os.path.exists(insdbfile) or not os.path.isfile(insdbfile)):
  return False;
 if(outsqlfile is None):
  file_wo_extension, file_extension = os.path.splitext(insdbfile);
  outsqlfile = file_wo_extension+".sql";
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outsqlfile)[0];
 fextname = os.path.splitext(outsqlfile)[1];
 sqlfp = CompressOpenFile(outsqlfile);
 sqlstring = MakeHockeySQLFromOldHockeyDatabase(insdbfile, verbose, jsonverbose);
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
 hockeydbin = MakeHockeyDatabaseFromHockeyArray(inhockeyarray, ":memory:", True, False, False);
 hockeyarray = MakeHockeySQLiteArrayFromHockeyDatabase(hockeydbin, True);
 if(not CheckHockeySQLiteArray(hockeyarray)):
  return False;
 return hockeyarray;

def MakeHockeySQLiteArrayFromHockeySQL(insqlfile, sqlisfile=True, verbose=True, jsonverbose=True):
 hockeydbin = MakeHockeyDatabaseFromHockeySQL(insqlfile, ":memory:", sqlisfile, True, False, False);
 hockeyarray = MakeHockeySQLiteArrayFromHockeyDatabase(hockeydbin, True);
 return hockeyarray;

def MakeHockeyPythonFromHockeySQLiteArray(inhockeyarray, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeySQLiteArray(inhockeyarray, verbose=True, jsonverbose=True);
 pystring = MakeHockeyPythonFromHockeyArray(hockeyarray, verbose, jsonverbose);
 return pystring;

def MakeHockeyPythonFileFromHockeySQLiteArray(inhockeyarray, outpyfile=None, returnpy=False, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeySQLiteArray(inhockeyarray, verbose=True, jsonverbose=True);
 pystring = MakeHockeyPythonFileFromHockeyArray(hockeyarray, outpyfile, returnpy, verbose, jsonverbose);
 return pystring;

def MakeHockeyPythonAltFromHockeySQLiteArray(inhockeyarray, verbose=True, jsonverbose=True, verbosepy=True):
 hockeyarray = MakeHockeyArrayFromHockeySQLiteArray(inhockeyarray, verbose=True, jsonverbose=True);
 pystring = MakeHockeyPythonAltFromHockeyArray(hockeyarray, verbose, jsonverbose, verbosepy);
 return pystring;

def MakeHockeyPythonAltFileFromHockeySQLiteArray(inhockeyarray, outpyfile=None, returnpy=False, verbose=True, jsonverbose=True, verbosepy=True):
 hockeyarray = MakeHockeyArrayFromHockeySQLiteArray(inhockeyarray, verbose=True, jsonverbose=True);
 pystring = MakeHockeyPythonAltFileFromHockeyArray(hockeyarray, outpyfile, returnpy, verbose, jsonverbose, verbosepy);
 return pystring;

def MakeHockeyPythonOOPFromHockeySQLiteArray(inhockeyarray, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeySQLiteArray(inhockeyarray, verbose=True, jsonverbose=True);
 pystring = MakeHockeyPythonOOPFromHockeyArray(hockeyarray, verbose, jsonverbose);
 return pystring;

def MakeHockeyPythonOOPFileFromHockeySQLiteArray(inhockeyarray, outpyfile=None, returnpy=False, verbose=True, jsonverbose=True):
 hockeyarray = MakeHockeyArrayFromHockeySQLiteArray(inhockeyarray, verbose=True, jsonverbose=True);
 pystring = MakeHockeyPythonOOPFileFromHockeyArray(hockeyarray, outpyfile, returnpy, verbose, jsonverbose);
 return pystring;

def MakeHockeyPythonOOPAltFromHockeySQLiteArray(inhockeyarray, verbose=True, jsonverbose=True, verbosepy=True):
 hockeyarray = MakeHockeyArrayFromHockeySQLiteArray(inhockeyarray, verbose=True, jsonverbose=True);
 pystring = MakeHockeyPythonOOPAltFromHockeyArray(hockeyarray, verbose, jsonverbose, verbosepy);
 return pystring;

def MakeHockeyPythonOOPAltFileFromHockeySQLiteArray(inhockeyarray, outpyfile=None, returnpy=False, verbose=True, jsonverbose=True, verbosepy=True):
 hockeyarray = MakeHockeyArrayFromHockeySQLiteArray(inhockeyarray, verbose=True, jsonverbose=True);
 pystring = MakeHockeyPythonOOPAltFileFromHockeyArray(hockeyarray, outpyfile, returnpy, verbose, jsonverbose, verbosepy);
 return pystring;

def MakeHockeyDatabaseFromHockeySQLiteArray(inhockeyarray, outsdbfile=None, returndb=False, verbose=True, jsonverbose=True):
 sqlstring = MakeHockeySQLFromHockeySQLiteArray(inhockeyarray, outsdbfile, False, False);
 outhockeydb = MakeHockeyDatabaseFromHockeySQL(sqlstring, outsdbfile, False, False, returndb, False, False);
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeySQLiteXMLFromHockeySQLiteArray(inhockeyarray, beautify, verbose=False, jsonverbose=True));
 if(returndb):
  return outhockeydb;
 if(not returndb):
  return True;
 return True;

def MakeHockeySQLiteArrayFromOldHockeyDatabase(insdbfile, verbose=True, jsonverbose=True):
 inhockeyarray = MakeHockeyArrayFromOldHockeyDatabase(insdbfile, False, False);
 hockeyarray = MakeHockeySQLiteArrayFromHockeyArray(inhockeyarray, verbose, jsonverbose);
 return hockeyarray;

def MakeHockeyArrayFromHockeyDataByDict(informat="xml", **funcargs):
 informat = informat.lower();
 if(informat=="xml"):
  if("infile" in funcargs and "inxmlfile" not in funcargs):
   funcargs['inxmlfile'] = funcargs['infile'];
   del funcargs['infile'];
  return MakeHockeyArrayFromHockeyXML(**funcargs);
 elif(informat=="json"):
  if("infile" in funcargs and "injsonfile" not in funcargs):
   funcargs['injsonfile'] = funcargs['infile'];
   del funcargs['infile'];
  return MakeHockeyArrayFromHockeyJSON(**funcargs);
 elif(informat=="pickle"):
  if("infile" in funcargs and "inpicklefile" not in funcargs):
   funcargs['inpicklefile'] = funcargs['infile'];
   del funcargs['infile'];
  return MakeHockeyArrayFromHockeyPickle(**funcargs);
 elif(informat=="marshal"):
  if("infile" in funcargs and "inmarshalfile" not in funcargs):
   funcargs['inmarshalfile'] = funcargs['infile'];
   del funcargs['infile'];
  return MakeHockeyArrayFromHockeyPickle(**funcargs);
 elif(informat=="database"):
  if("infile" in funcargs and "insdbfile" not in funcargs):
   funcargs['insdbfile'] = funcargs['infile'];
   del funcargs['infile'];
  return MakeHockeyArrayFromHockeyDatabase(**funcargs);
 elif(informat=="olddatabase"):
  if("infile" in funcargs and "insdbfile" not in funcargs):
   funcargs['insdbfile'] = funcargs['infile'];
   del funcargs['infile'];
  return MakeHockeyArrayFromOldHockeyDatabase(**funcargs);
 elif(informat=="sql"):
  if("infile" in funcargs and "insqlfile" not in funcargs):
   funcargs['insqlfile'] = funcargs['infile'];
   del funcargs['infile'];
  return MakeHockeyArrayFromHockeySQL(**funcargs);
 elif(informat=="array"):
  return MakeHockeyArrayFromHockeySQLiteArray(**funcargs);
 else:
  return False;
 return False;

def MakeHockeyArrayFromHockeyDataByList(informat="xml", *funcargs):
 informat = informat.lower();
 if(informat=="xml"):
  return MakeHockeyArrayFromHockeyXML(*funcargs);
 elif(informat=="json"):
  return MakeHockeyArrayFromHockeyJSON(*funcargs);
 elif(informat=="pickle"):
  return MakeHockeyArrayFromHockeyPickle(*funcargs);
 elif(informat=="marshal"):
  return MakeHockeyArrayFromHockeyPickle(*funcargs);
 elif(informat=="database"):
  return MakeHockeyArrayFromHockeyDatabase(*funcargs);
 elif(informat=="olddatabase"):
  return MakeHockeyArrayFromOldHockeyDatabase(*funcargs);
 elif(informat=="sql"):
  return MakeHockeyArrayFromHockeySQL(*funcargs);
 elif(informat=="array"):
  return MakeHockeyArrayFromHockeySQLiteArray(*funcargs);
 else:
  return False;
 return False;

def MakeHockeyArrayFromHockeyData(funcargs):
 if(funcargs is not None and isinstance(funcargs, (tuple, list))):
  return MakeHockeyArrayFromHockeyDataByList(*funcargs);
 elif(funcargs is not None and isinstance(funcargs, (dict))):
  return MakeHockeyArrayFromHockeyDataByDict(**funcargs);
 else:
  return False;
 return False;

def MakeHockeyDataFromHockeyArrayByDict(outformat="xml", **funcargs):
 outformat = outformat.lower();
 if(outformat=="xml"):
  return MakeHockeyXMLFromHockeyArray(**funcargs);
 elif(outformat=="xmlalt"):
  return MakeHockeyXMLAltFromHockeyArray(**funcargs);
 elif(outformat=="json"):
  return MakeHockeyJSONFromHockeyArray(**funcargs);
 elif(outformat=="pickle"):
  return MakeHockeyPickleFromHockeyArray(**funcargs);
 elif(outformat=="marshal"):
  return MakeHockeyMarshalFromHockeyArray(**funcargs);
 elif(outformat=="database"):
  return MakeHockeyDatabaseFromHockeyArray(**funcargs);
 elif(outformat=="py"):
  return MakeHockeyPythonFromHockeyArray(**funcargs);
 elif(outformat=="pyalt"):
  return MakeHockeyPythonAltFromHockeyArray(**funcargs);
 elif(outformat=="pyoop"):
  return MakeHockeyPythonOOPFromHockeyArray(**funcargs);
 elif(outformat=="pyoopalt"):
  return MakeHockeyPythonOOPAltFromHockeyArray(**funcargs);
 elif(outformat=="sql"):
  return MakeHockeySQLFromHockeyArray(**funcargs);
 elif(outformat=="array"):
  return MakeHockeySQLiteArrayFromHockeyArray(**funcargs);
 else:
  return False;
 return False;

def MakeHockeyDataFromHockeyArrayByList(outformat="xml", *funcargs):
 outformat = outformat.lower();
 if(outformat=="xml"):
  return MakeHockeyXMLFromHockeyArray(*funcargs);
 elif(outformat=="xmlalt"):
  return MakeHockeyXMLAltFromHockeyArray(*funcargs);
 elif(outformat=="json"):
  return MakeHockeyJSONFromHockeyArray(*funcargs);
 elif(outformat=="pickle"):
  return MakeHockeyPickleFromHockeyArray(*funcargs);
 elif(outformat=="marshal"):
  return MakeHockeyMarshalFromHockeyArray(*funcargs);
 elif(outformat=="database"):
  return MakeHockeyDatabaseFromHockeyArray(*funcargs);
 elif(outformat=="py"):
  return MakeHockeyPythonFromHockeyArray(*funcargs);
 elif(outformat=="pyalt"):
  return MakeHockeyPythonAltFromHockeyArray(*funcargs);
 elif(outformat=="pyoop"):
  return MakeHockeyPythonOOPFromHockeyArray(*funcargs);
 elif(outformat=="pyoopalt"):
  return MakeHockeyPythonOOPAltFromHockeyArray(*funcargs);
 elif(outformat=="sql"):
  return MakeHockeySQLFromHockeyArray(*funcargs);
 elif(outformat=="array"):
  return MakeHockeySQLiteArrayFromHockeyArray(*funcargs);
 else:
  return False;
 return False;

def MakeHockeyDataFromHockeyArray(funcargs):
 if(funcargs is not None and isinstance(funcargs, (tuple, list))):
  return MakeHockeyDataFromHockeyArrayByList(*funcargs);
 elif(funcargs is not None and isinstance(funcargs, (dict))):
  return MakeHockeyDataFromHockeyArrayByDict(**funcargs);
 else:
  return False;
 return False;

def MakeHockeyDataFileFromHockeyArrayByDict(outformat="xml", **funcargs):
 outformat = outformat.lower();
 if(outformat=="xml"):
  if("outfile" in funcargs and "outxmlfile" not in funcargs):
   funcargs['outxmlfile'] = funcargs['outfile'];
   del funcargs['outfile'];
  return MakeHockeyXMLFileFromHockeyArray(**funcargs);
 elif(outformat=="xmlalt"):
  if("outfile" in funcargs and "outxmlfile" not in funcargs):
   funcargs['outxmlfile'] = funcargs['outfile'];
   del funcargs['outfile'];
  return MakeHockeyXMLAltFileFromHockeyArray(**funcargs);
 elif(outformat=="json"):
  if("outfile" in funcargs and "outjsonfile" not in funcargs):
   funcargs['outjsonfile'] = funcargs['outfile'];
   del funcargs['outfile'];
  return MakeHockeyJSONFileFromHockeyArray(**funcargs);
 elif(outformat=="pickle"):
  if("outfile" in funcargs and "outpicklefile" not in funcargs):
   funcargs['outpicklefile'] = funcargs['outfile'];
   del funcargs['outfile'];
  return MakeHockeyPickleFileFromHockeyArray(**funcargs);
 elif(outformat=="marshal"):
  if("outfile" in funcargs and "outmarshalfile" not in funcargs):
   funcargs['outmarshalfile'] = funcargs['outfile'];
   del funcargs['outfile'];
  return MakeHockeyMarshalFileFromHockeyArray(**funcargs);
 elif(outformat=="py"):
  if("outfile" in funcargs and "outpyfile" not in funcargs):
   funcargs['outpyfile'] = funcargs['outfile'];
   del funcargs['outfile'];
  return MakeHockeyPythonFileFromHockeyArray(**funcargs);
 elif(outformat=="pyalt"):
  if("outfile" in funcargs and "outpyfile" not in funcargs):
   funcargs['outpyfile'] = funcargs['outfile'];
   del funcargs['outfile'];
  return MakeHockeyPythonAltFileFromHockeyArray(**funcargs);
 elif(outformat=="pyoop"):
  if("outfile" in funcargs and "outpyfile" not in funcargs):
   funcargs['outpyfile'] = funcargs['outfile'];
   del funcargs['outfile'];
  return MakeHockeyPythonOOPFileFromHockeyArray(**funcargs);
 elif(outformat=="pyoopalt"):
  if("outfile" in funcargs and "outpyfile" not in funcargs):
   funcargs['outpyfile'] = funcargs['outfile'];
   del funcargs['outfile'];
  return MakeHockeyPythonOOPAltFileFromHockeyArray(**funcargs);
 elif(outformat=="sql"):
  if("outfile" in funcargs and "outsqlfile" not in funcargs):
   funcargs['outsqlfile'] = funcargs['outfile'];
   del funcargs['outfile'];
  return MakeHockeySQLFileFromHockeyArray(**funcargs);
 else:
  return False;
 return False;

def MakeHockeyDataFileFromHockeyArrayByList(outformat="xml", *funcargs):
 outformat = outformat.lower();
 if(outformat=="xml"):
  return MakeHockeyXMLFileFromHockeyArray(*funcargs);
 elif(outformat=="xmlalt"):
  return MakeHockeyXMLAltFileFromHockeyArray(*funcargs);
 elif(outformat=="json"):
  return MakeHockeyJSONFileFromHockeyArray(*funcargs);
 elif(outformat=="pickle"):
  return MakeHockeyPickleFileFromHockeyArray(*funcargs);
 elif(outformat=="marshal"):
  return MakeHockeyMarshalFileFromHockeyArray(*funcargs);
 elif(outformat=="py"):
  return MakeHockeyPythonFileFromHockeyArray(*funcargs);
 elif(outformat=="pyalt"):
  return MakeHockeyPythonAltFileFromHockeyArray(*funcargs);
 elif(outformat=="pyoop"):
  return MakeHockeyPythonOOPFileFromHockeyArray(*funcargs);
 elif(outformat=="pyoopalt"):
  return MakeHockeyPythonOOPAltFileFromHockeyArray(*funcargs);
 elif(outformat=="sql"):
  return MakeHockeySQLFileFromHockeyArray(*funcargs);
 else:
  return False;
 return False;

def MakeHockeyDataFileFromHockeyArray(funcargs):
 if(funcargs is not None and isinstance(funcargs, (tuple, list))):
  return MakeHockeyDataFileFromHockeyArrayByList(*funcargs);
 elif(funcargs is not None and isinstance(funcargs, (dict))):
  return MakeHockeyDataFileFromHockeyArrayByDict(**funcargs);
 else:
  return False;
 return False;

def MakeHockeySQLiteArrayFromHockeySQLiteDataByDict(informat="xml", **funcargs):
 informat = informat.lower();
 if(informat=="xml"):
  if("infile" in funcargs and "inxmlfile" not in funcargs):
   funcargs['inxmlfile'] = funcargs['infile'];
   del funcargs['infile'];
  return MakeHockeySQLiteArrayFromHockeySQLiteXML(**funcargs);
 elif(informat=="json"):
  if("infile" in funcargs and "injsonfile" not in funcargs):
   funcargs['injsonfile'] = funcargs['infile'];
   del funcargs['infile'];
  return MakeHockeySQLiteArrayFromHockeySQLiteJSON(**funcargs);
 elif(informat=="pickle"):
  if("infile" in funcargs and "inpicklefile" not in funcargs):
   funcargs['inpicklefile'] = funcargs['infile'];
   del funcargs['infile'];
  return MakeHockeySQLiteArrayFromHockeySQLitePickle(**funcargs);
 elif(informat=="marshal"):
  if("infile" in funcargs and "inmarshalfile" not in funcargs):
   funcargs['inmarshalfile'] = funcargs['infile'];
   del funcargs['infile'];
  return MakeHockeySQLiteArrayFromHockeySQLitePickle(**funcargs);
 elif(informat=="database"):
  if("infile" in funcargs and "insdbfile" not in funcargs):
   funcargs['insdbfile'] = funcargs['infile'];
   del funcargs['infile'];
  return MakeHockeySQLiteArrayFromHockeyDatabase(**funcargs);
 elif(informat=="olddatabase"):
  if("infile" in funcargs and "insdbfile" not in funcargs):
   funcargs['insdbfile'] = funcargs['infile'];
   del funcargs['infile'];
  return MakeHockeySQLiteArrayFromOldHockeyDatabase(**funcargs);
 elif(informat=="sql"):
  if("infile" in funcargs and "insqlfile" not in funcargs):
   funcargs['insqlfile'] = funcargs['infile'];
   del funcargs['infile'];
  return MakeHockeySQLiteArrayFromHockeySQL(**funcargs);
 elif(informat=="array"):
  return MakeHockeySQLiteArrayFromHockeyArray(**funcargs);
 else:
  return False;
 return False;

def MakeHockeySQLiteArrayFromHockeySQLiteDataByList(informat="xml", *funcargs):
 informat = informat.lower();
 if(informat=="xml"):
  return MakeHockeySQLiteArrayFromHockeySQLiteXML(*funcargs);
 elif(informat=="json"):
  return MakeHockeySQLiteArrayFromHockeySQLiteJSON(*funcargs);
 elif(informat=="pickle"):
  return MakeHockeySQLiteArrayFromHockeySQLitePickle(*funcargs);
 elif(informat=="marshal"):
  return MakeHockeySQLiteArrayFromHockeySQLitePickle(*funcargs);
 elif(informat=="database"):
  return MakeHockeySQLiteArrayFromHockeyDatabase(*funcargs);
 elif(informat=="olddatabase"):
  return MakeHockeySQLiteArrayFromOldHockeyDatabase(*funcargs);
 elif(informat=="sql"):
  return MakeHockeySQLiteArrayFromHockeySQL(*funcargs);
 elif(informat=="array"):
  return MakeHockeySQLiteArrayFromHockeyArray(*funcargs);
 else:
  return False;
 return False;

def MakeHockeySQLiteArrayFromHockeySQLiteData(funcargs):
 if(funcargs is not None and isinstance(funcargs, (tuple, list))):
  return MakeHockeySQLiteArrayFromHockeySQLiteDataByList(*funcargs);
 elif(funcargs is not None and isinstance(funcargs, (dict))):
  return MakeHockeySQLiteArrayFromHockeySQLiteDataByDict(**funcargs);
 else:
  return False;
 return False;

def MakeHockeySQLiteDataFromHockeySQLiteArrayByDict(outformat="xml", **funcargs):
 outformat = outformat.lower();
 if(outformat=="xml"):
  return MakeHockeySQLiteXMLFromHockeySQLiteArray(**funcargs);
 elif(outformat=="xmlalt"):
  return MakeHockeySQLiteXMLAltFromHockeySQLiteArray(**funcargs);
 elif(outformat=="json"):
  return MakeHockeySQLiteJSONFromHockeySQLiteArray(**funcargs);
 elif(outformat=="pickle"):
  return MakeHockeySQLitePickleFromHockeySQLiteArray(**funcargs);
 elif(outformat=="marshal"):
  return MakeHockeySQLiteMarshalFromHockeySQLiteArray(**funcargs);
 elif(outformat=="database"):
  return MakeHockeyDatabaseFromHockeySQLiteArray(**funcargs);
 elif(outformat=="py"):
  return MakeHockeyPythonFromHockeySQLiteArray(**funcargs);
 elif(outformat=="pyalt"):
  return MakeHockeyPythonAltFromHockeySQLiteArray(**funcargs);
 elif(outformat=="pyoop"):
  return MakeHockeyPythonOOPFromHockeySQLiteArray(**funcargs);
 elif(outformat=="pyoopalt"):
  return MakeHockeyPythonOOPAltFromHockeySQLiteArray(**funcargs);
 elif(outformat=="sql"):
  return MakeHockeySQLFromHockeySQLiteArray(**funcargs);
 elif(outformat=="array"):
  return MakeHockeyArrayFromHockeySQLiteArray(**funcargs);
 else:
  return False;
 return False;

def MakeHockeySQLiteDataFromHockeySQLiteArrayByList(outformat="xml", *funcargs):
 outformat = outformat.lower();
 if(outformat=="xml"):
  return MakeHockeySQLiteXMLFromHockeySQLiteArray(*funcargs);
 elif(outformat=="xmlalt"):
  return MakeHockeySQLiteXMLAltFromHockeySQLiteArray(*funcargs);
 elif(outformat=="json"):
  return MakeHockeySQLiteJSONFromHockeySQLiteArray(*funcargs);
 elif(outformat=="pickle"):
  return MakeHockeySQLitePickleFromHockeySQLiteArray(*funcargs);
 elif(outformat=="marshal"):
  return MakeHockeySQLiteMarshalFromHockeySQLiteArray(*funcargs);
 elif(outformat=="database"):
  return MakeHockeyDatabaseFromHockeySQLiteArray(*funcargs);
 elif(outformat=="py"):
  return MakeHockeyPythonFromHockeySQLiteArray(*funcargs);
 elif(outformat=="pyalt"):
  return MakeHockeyPythonAltFromHockeySQLiteArray(*funcargs);
 elif(outformat=="pyoop"):
  return MakeHockeyPythonOOPFromHockeySQLiteArray(*funcargs);
 elif(outformat=="pyoopalt"):
  return MakeHockeyPythonOOPAltFromHockeySQLiteArray(*funcargs);
 elif(outformat=="sql"):
  return MakeHockeySQLFromHockeySQLiteArray(*funcargs);
 elif(outformat=="array"):
  return MakeHockeyArrayFromHockeySQLiteArray(*funcargs);
 else:
  return False;
 return False;

def MakeHockeySQLiteDataFromHockeySQLiteArray(funcargs):
 if(funcargs is not None and isinstance(funcargs, (tuple, list))):
  return MakeHockeySQLiteDataFromHockeySQLiteArrayByList(*funcargs);
 elif(funcargs is not None and isinstance(funcargs, (dict))):
  return MakeHockeySQLiteDataFromHockeySQLiteArrayByDict(**funcargs);
 else:
  return False;
 return False;

def MakeHockeySQLiteDataFileFromHockeySQLiteArrayByDict(outformat="xml", **funcargs):
 outformat = outformat.lower();
 if(outformat=="xml"):
  return MakeHockeySQLiteXMLFileFromHockeySQLiteArray(**funcargs);
 elif(outformat=="xmlalt"):
  return MakeHockeySQLiteXMLAltFileFromHockeySQLiteArray(**funcargs);
 elif(outformat=="json"):
  return MakeHockeySQLiteJSONFileFromHockeySQLiteArray(**funcargs);
 elif(outformat=="pickle"):
  return MakeHockeySQLitePickleFileFromHockeySQLiteArray(**funcargs);
 elif(outformat=="marshal"):
  return MakeHockeySQLiteMarshalFileFromHockeySQLiteArray(**funcargs);
 elif(outformat=="py"):
  return MakeHockeyPythonFileFromHockeySQLiteArray(**funcargs);
 elif(outformat=="pyalt"):
  return MakeHockeyPythonAltFileFromHockeySQLiteArray(**funcargs);
 elif(outformat=="pyoop"):
  return MakeHockeyPythonOOPFileFromHockeySQLiteArray(**funcargs);
 elif(outformat=="pyoopalt"):
  return MakeHockeyPythonOOPAltFileFromHockeySQLiteArray(**funcargs);
 elif(outformat=="sql"):
  return MakeHockeySQLFileFromHockeySQLiteArray(**funcargs);
 else:
  return False;
 return False;

def MakeHockeySQLiteDataFileFromHockeySQLiteArrayByList(outformat="xml", *funcargs):
 outformat = outformat.lower();
 if(outformat=="xml"):
  return MakeHockeySQLiteXMLFileFromHockeySQLiteArray(*funcargs);
 elif(outformat=="xmlalt"):
  return MakeHockeySQLiteXMLAltFileFromHockeySQLiteArray(*funcargs);
 elif(outformat=="json"):
  return MakeHockeySQLiteJSONFileFromHockeySQLiteArray(*funcargs);
 elif(outformat=="pickle"):
  return MakeHockeySQLitePickleFileFromHockeySQLiteArray(*funcargs);
 elif(outformat=="marshal"):
  return MakeHockeySQLiteMarshalFileFromHockeySQLiteArray(*funcargs);
 elif(outformat=="py"):
  return MakeHockeyPythonFileFromHockeySQLiteArray(*funcargs);
 elif(outformat=="pyalt"):
  return MakeHockeyPythonAltFileFromHockeySQLiteArray(*funcargs);
 elif(outformat=="pyoop"):
  return MakeHockeyPythonOOPFileFromHockeySQLiteArray(*funcargs);
 elif(outformat=="pyoopalt"):
  return MakeHockeyPythonOOPAltFileFromHockeySQLiteArray(*funcargs);
 elif(outformat=="sql"):
  return MakeHockeySQLFileFromHockeySQLiteArray(*funcargs);
 else:
  return False;
 return False;

def MakeHockeySQLiteDataFileFromHockeySQLiteArray(funcargs):
 if(funcargs is not None and isinstance(funcargs, (tuple, list))):
  return MakeHockeySQLiteDataFileFromHockeySQLiteArrayByList(*funcargs);
 elif(funcargs is not None and isinstance(funcargs, (dict))):
  return MakeHockeySQLiteDataFileFromHockeySQLiteArrayByDict(**funcargs);
 else:
  return False;
 return False;

def MakeHockeyDataFromHockeyData(infuncargs, outfuncargs):
 if(infuncargs is not None and isinstance(infuncargs, (tuple, list))):
  inhockeyarray = MakeHockeyArrayFromHockeyDataByList(*infuncargs);
 elif(infuncargs is not None and isinstance(infuncargs, (dict))):
  inhockeyarray = MakeHockeyArrayFromHockeyDataByDict(**infuncargs);
 else:
  return False;
 if(outfuncargs is not None and isinstance(outfuncargs, (tuple, list))):
  if(len(outfuncargs)>1):
   outfuncargs[1] = inhockeyarray;
  else:
   outfuncargs.append(inhockeyarray);
  return MakeHockeyDataFromHockeyArrayByList(*outfuncargs);
 elif(outfuncargs is not None and isinstance(outfuncargs, (dict))):
  outfuncargs.update( { 'inhockeyarray': inhockeyarray } );
  return MakeHockeyDataFromHockeyArrayByDict(**outfuncargs);
 else:
  return False;
 return False;

def MakeHockeyDataFileFromHockeyData(infuncargs, outfuncargs):
 if(infuncargs is not None and isinstance(infuncargs, (tuple, list))):
  inhockeyarray = MakeHockeyArrayFromHockeyDataByList(*infuncargs);
 elif(infuncargs is not None and isinstance(infuncargs, (dict))):
  inhockeyarray = MakeHockeyArrayFromHockeyDataByDict(**infuncargs);
 else:
  return False;
 if(outfuncargs is not None and isinstance(outfuncargs, (tuple, list))):
  if(len(outfuncargs)>1):
   outfuncargs[1] = inhockeyarray;
  else:
   outfuncargs.append(inhockeyarray);
  return MakeHockeyDataFileFromHockeyArrayByList(*outfuncargs);
 elif(outfuncargs is not None and isinstance(outfuncargs, (dict))):
  outfuncargs.update( { 'inhockeyarray': inhockeyarray } );
  return MakeHockeyDataFileFromHockeyArrayByDict(**outfuncargs);
 else:
  return False;
 return False;

def MakeHockeyDataFromHockeySQLiteData(infuncargs, outfuncargs):
 if(infuncargs is not None and isinstance(infuncargs, (tuple, list))):
  inhockeyarray = MakeHockeySQLiteArrayFromHockeySQLiteDataByList(*infuncargs);
 elif(infuncargs is not None and isinstance(infuncargs, (dict))):
  inhockeyarray = MakeHockeySQLiteArrayFromHockeySQLiteDataByDict(**infuncargs);
 else:
  return False;
 inhockeyarray = MakeHockeyArrayFromHockeySQLiteArray(inhockeyarray, False, False);
 if(outfuncargs is not None and isinstance(outfuncargs, (tuple, list))):
  if(len(outfuncargs)>1):
   outfuncargs[1] = inhockeyarray;
  else:
   outfuncargs.append(inhockeyarray);
  return MakeHockeyDataFromHockeyArrayByList(*outfuncargs);
 elif(outfuncargs is not None and isinstance(outfuncargs, (dict))):
  outfuncargs.update( { 'inhockeyarray': inhockeyarray } );
  return MakeHockeyDataFromHockeyArrayByDict(**outfuncargs);
 else:
  return False;
 return False;

def MakeHockeyDataFileFromHockeySQLiteData(infuncargs, outfuncargs):
 if(infuncargs is not None and isinstance(infuncargs, (tuple, list))):
  inhockeyarray = MakeHockeySQLiteArrayFromHockeySQLiteDataByList(*infuncargs);
 elif(infuncargs is not None and isinstance(infuncargs, (dict))):
  inhockeyarray = MakeHockeySQLiteArrayFromHockeySQLiteDataByDict(**infuncargs);
 else:
  return False;
 inhockeyarray = MakeHockeyArrayFromHockeySQLiteArray(inhockeyarray, False, False);
 if(outfuncargs is not None and isinstance(outfuncargs, (tuple, list))):
  if(len(outfuncargs)>1):
   outfuncargs[1] = inhockeyarray;
  else:
   outfuncargs.append(inhockeyarray);
  return MakeHockeyDataFileFromHockeyArrayByList(*outfuncargs);
 elif(outfuncargs is not None and isinstance(outfuncargs, (dict))):
  outfuncargs.update( { 'inhockeyarray': inhockeyarray } );
  return MakeHockeyDataFileFromHockeyArrayByDict(**outfuncargs);
 else:
  return False;
 return False;

def MakeHockeySQLiteDataFromHockeySQLiteData(infuncargs, outfuncargs):
 if(infuncargs is not None and isinstance(infuncargs, (tuple, list))):
  inhockeyarray = MakeHockeySQLiteArrayFromHockeySQLiteDataByList(*infuncargs);
 elif(infuncargs is not None and isinstance(infuncargs, (dict))):
  inhockeyarray = MakeHockeySQLiteArrayFromHockeySQLiteDataByDict(**infuncargs);
 else:
  return False;
 if(outfuncargs is not None and isinstance(outfuncargs, (tuple, list))):
  if(len(outfuncargs)>1):
   outfuncargs[1] = inhockeyarray;
  else:
   outfuncargs.append(inhockeyarray);
  return MakeHockeySQLiteDataFromHockeySQLiteArrayByList(*outfuncargs);
 elif(outfuncargs is not None and isinstance(outfuncargs, (dict))):
  outfuncargs.update( { 'inhockeyarray': inhockeyarray } );
  return MakeHockeySQLiteDataFromHockeySQLiteArrayByDict(**outfuncargs);
 else:
  return False;
 return False;

def MakeHockeySQLiteDataFileFromHockeySQLiteData(infuncargs, outfuncargs):
 if(infuncargs is not None and isinstance(infuncargs, (tuple, list))):
  inhockeyarray = MakeHockeySQLiteArrayFromHockeySQLiteDataByList(*infuncargs);
 elif(infuncargs is not None and isinstance(infuncargs, (dict))):
  inhockeyarray = MakeHockeySQLiteArrayFromHockeySQLiteDataByDict(**infuncargs);
 else:
  return False;
 if(outfuncargs is not None and isinstance(outfuncargs, (tuple, list))):
  if(len(outfuncargs)>1):
   outfuncargs[1] = inhockeyarray;
  else:
   outfuncargs.append(inhockeyarray);
  return MakeHockeySQLiteDataFileFromHockeySQLiteArrayByList(*outfuncargs);
 elif(outfuncargs is not None and isinstance(outfuncargs, (dict))):
  outfuncargs.update( { 'inhockeyarray': inhockeyarray } );
  return MakeHockeySQLiteDataFileFromHockeySQLiteArrayByDict(**outfuncargs);
 else:
  return False;
 return False;

def MakeHockeySQLiteDataFromHockeyData(infuncargs, outfuncargs):
 if(infuncargs is not None and isinstance(infuncargs, (tuple, list))):
  inhockeyarray = MakeHockeyArrayFromHockeyDataByList(*infuncargs);
 elif(infuncargs is not None and isinstance(infuncargs, (dict))):
  inhockeyarray = MakeHockeyArrayFromHockeyDataByDict(**infuncargs);
 else:
  return False;
 inhockeyarray = MakeHockeySQLiteArrayFromHockeyArray(inhockeyarray, False, False);
 if(outfuncargs is not None and isinstance(outfuncargs, (tuple, list))):
  if(len(outfuncargs)>1):
   outfuncargs[1] = inhockeyarray;
  else:
   outfuncargs.append(inhockeyarray);
  return MakeHockeySQLiteDataFromHockeySQLiteArrayByList(*outfuncargs);
 elif(outfuncargs is not None and isinstance(outfuncargs, (dict))):
  outfuncargs.update( { 'inhockeyarray': inhockeyarray } );
  return MakeHockeySQLiteDataFromHockeySQLiteArrayByDict(**outfuncargs);
 else:
  return False;
 return False;

def MakeHockeySQLiteDataFileFromHockeyData(infuncargs, outfuncargs):
 if(infuncargs is not None and isinstance(infuncargs, (tuple, list))):
  inhockeyarray = MakeHockeyArrayFromHockeyDataByList(*infuncargs);
 elif(infuncargs is not None and isinstance(infuncargs, (dict))):
  inhockeyarray = MakeHockeyArrayFromHockeyDataByDict(**infuncargs);
 else:
  return False;
 inhockeyarray = MakeHockeySQLiteArrayFromHockeyArray(inhockeyarray, False, False);
 if(outfuncargs is not None and isinstance(outfuncargs, (tuple, list))):
  if(len(outfuncargs)>1):
   outfuncargs[1] = inhockeyarray;
  else:
   outfuncargs.append(inhockeyarray);
  return MakeHockeySQLiteDataFileFromHockeySQLiteArrayByList(*outfuncargs);
 elif(outfuncargs is not None and isinstance(outfuncargs, (dict))):
  outfuncargs.update( { 'inhockeyarray': inhockeyarray } );
  return MakeHockeySQLiteDataFileFromHockeySQLiteArrayByDict(**outfuncargs);
 else:
  return False;
 return False;
