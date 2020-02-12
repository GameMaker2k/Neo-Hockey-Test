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

    $FileInfo: hockeyshortcuts.py - Last Update: 2/9/2020 Ver. 0.2.0 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals;
import sqlite3, sys, os, re, time;
from libhockeydata.hockeyfunctions import *;

def MakeHockeyXMLFileFromHockeyXML(inxmlfile, outxmlfile=None, xmlisfile=True, returnxml=False, verbose=True):
 if(xmlisfile is True and (not os.path.exists(inxmlfile) or not os.path.isfile(inxmlfile))):
  return False;
 if(outxmlfile is None and xmlisfile is True):
  file_wo_extension, file_extension = os.path.splitext(inxmlfile);
  outxmlfile = file_wo_extension+".xml";
 xmlfp = open(outxmlfile, "w+");
 xmlstring = MakeHockeyXMLFromHockeyXML(inxmlfile, xmlisfile, verbose);
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml is True):
  return xmlstring;
 if(returnxml is False):
  return True;
 return True;

def MakeHockeyJSONFromHockeyXML(inxmlfile, xmlisfile=True, returnjson=False, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(inxmlfile, xmlisfile, False, False);
 jsonstring = MakeHockeyJSONFromHockeyArray(hockeyarray, returnjson, verbose);
 if(verbose is True):
  VerbosePrintOut(jsonstring);
 return jsonstring;

def MakeHockeyJSONFromHockeyDatabase(sdbfile, returnjson=False, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(sdbfile, False);
 jsonstring = MakeHockeyJSONFromHockeyArray(hockeyarray, returnjson, verbose);
 if(verbose is True):
  VerbosePrintOut(jsonstring);
 return jsonstring;

def MakeHockeyJSONFromHockeySQL(sqlfile, sdbfile=None, sqlisfile=True, returnjson=False, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeySQL(sqlfile, sdbfile, sqlisfile, False);
 jsonstring = MakeHockeyJSONFromHockeyArray(hockeyarray, returnjson, verbose);
 if(verbose is True):
  VerbosePrintOut(jsonstring);
 return jsonstring;

def MakeHockeyJSONFromOldHockeyDatabase(sdbfile, returnjson=False, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(sdbfile, False);
 jsonstring = MakeHockeyJSONFromHockeyArray(hockeyarray, returnjson, verbose);
 if(verbose is True):
  VerbosePrintOut(jsonstring);
 return jsonstring;

def MakeHockeyDatabaseFromHockeyXML(xmlfile, sdbfile=None, xmlisfile=True, returnxml=False, returndb=False, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(xmlfile, xmlisfile, False);
 hockeydbout = MakeHockeyDatabaseFromHockeyArray(hockeyarray, sdbfile, returnxml, returndb, verbose);
 return hockeydbout;

def MakeHockeyDatabaseFromHockeyXMLWrite(inxmlfile, sdbfile=None, outxmlfile=None, xmlisfile=True, returnxml=False, verbose=True):
 if(xmlisfile is True and (not os.path.exists(inxmlfile) or not os.path.isfile(inxmlfile))):
  return False;
 if(outxmlfile is None and xmlisfile is True):
  file_wo_extension, file_extension = os.path.splitext(inxmlfile);
  outxmlfile = file_wo_extension+".xml";
 xmlfp = open(outxmlfile, "w+");
 xmlstring = MakeHockeyDatabaseFromHockeyXML(inxmlfile, sdbfile, xmlisfile, True, False, verbose);
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml is True):
  return xmlstring;
 if(returnxml is False):
  return True;
 return True;

def MakeHockeyDatabaseFromHockeySQL(sqlfile, sdbfile=None, sqlisfile=True, returnsql=False, returndb=False, verbose=True):
 if(sqlisfile is True and (os.path.exists(sqlfile) and os.path.isfile(sqlfile))):
  sqlfp = open(sqlfile, "r");
  sqlstring = sqlfp.read();
  sqlfp.close();
 elif(sqlisfile is False):
  sqlstring = sqlfile;
 else:
  return False;
 if(sdbfile is None and len(re.findall(r"Database\:([\w\W]+)", "-- Database: ./hockey17-18.db3"))>=1):
  sdbfile = re.findall(r"Database\:([\w\W]+)", "-- Database: ./hockey17-18.db3")[0].strip();
 if(sdbfile is None and len(re.findall(r"Database\:([\w\W]+)", "-- Database: ./hockey17-18.db3"))<1):
  file_wo_extension, file_extension = os.path.splitext(sqlfile);
  sdbfile = file_wo_extension+".db3";
 if(sdbfile is not None and isinstance(sdbfile, str)):
  sqldatacon = MakeHockeyDatabase(sdbfile);
 if(sdbfile is not None and isinstance(sdbfile, (tuple, list))):
  sqldatacon = tuple(sdbfile);
 if(verbose is True):
  VerbosePrintOut(sqlstring);
 sqldatacon[0].executescript(sqlstring);
 if(returndb is False):
  CloseHockeyDatabase(sqldatacon);
 if(returndb is True and returnsql is False):
  return sqldatacon;
 if(returnsql is True and returndb is False):
  return sqlstring;
 if(returnsql is True and returndb is True):
  return [sqlstring, sqldatacon];
 if(returnsql is False):
  return True;
 return True;

def MakeHockeyDatabaseFromHockeySQLWrite(insqlfile, sdbfile=None, outsqlfile=None, sqlisfile=True, returnsql=False, verbose=True):
 if(sqlisfile is True and (not os.path.exists(insqlfile) or not os.path.isfile(insqlfile))):
  return False;
 if(outsqlfile is None and sqlisfile is True):
  file_wo_extension, file_extension = os.path.splitext(insqlfile);
  outsqlfile = file_wo_extension+".db3";
 sqlfp = open(outsqlfile, "w+");
 sqlstring = MakeHockeyDatabaseFromHockeySQL(insqlfile, sdbfile, sqlisfile, True, False, verbose);
 sqlfp.write(sqlstring);
 sqlfp.close();
 if(returnsql is True):
  return sqlstring;
 if(returnsql is False):
  return True;
 return True;

def MakeHockeyPythonFromHockeyXML(xmlfile, xmlisfile=True, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(xmlfile, xmlisfile, False);
 hockeypyout = MakeHockeyPythonFromHockeyArray(hockeyarray, True);
 return hockeypyout;

def MakeHockeyPythonFileFromHockeyXML(inxmlfile, outpyfile=None, xmlisfile=True, returnpy=False, verbose=True):
 if(xmlisfile is True and (not os.path.exists(inxmlfile) or not os.path.isfile(inxmlfile))):
  return False;
 if(outpyfile is None and xmlisfile is True):
  file_wo_extension, file_extension = os.path.splitext(inxmlfile);
  outpyfile = file_wo_extension+".xml";
 pyfp = open(outpyfile, "w+");
 pystring = MakeHockeyPythonFromHockeyXML(inxmlfile, xmlisfile, verbose);
 pyfp.write(pystring);
 pyfp.close();
 if(returnpy is True):
  return pystring;
 if(returnpy is False):
  return True;
 return True;

def MakeHockeyPythonAltFromHockeyXML(xmlfile, xmlisfile=True, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(xmlfile, xmlisfile, False);
 hockeypyout = MakeHockeyPythonAltFromHockeyArray(hockeyarray, True);
 return hockeypyout;

def MakeHockeyPythonAltFileFromHockeyXML(inxmlfile, outpyfile=None, xmlisfile=True, returnpy=False, verbose=True):
 if(xmlisfile is True and (not os.path.exists(inxmlfile) or not os.path.isfile(inxmlfile))):
  return False;
 if(outpyfile is None and xmlisfile is True):
  file_wo_extension, file_extension = os.path.splitext(inxmlfile);
  outpyfile = file_wo_extension+".xml";
 pyfp = open(outpyfile, "w+");
 pystring = MakeHockeyPythonAltFromHockeyXML(inxmlfile, xmlisfile, verbose);
 pyfp.write(pystring);
 pyfp.close();
 if(returnpy is True):
  return pystring;
 if(returnpy is False):
  return True;
 return True;

def MakeHockeyXMLFromHockeyDatabase(sdbfile, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(sdbfile, False);
 hockeyxmlout = MakeHockeyXMLFromHockeyArray(hockeyarray, verbose);
 return hockeyxmlout;

def MakeHockeyXMLFileFromHockeyDatabase(sdbfile, xmlfile=None, returnxml=False, verbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(xmlfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  xmlfile = file_wo_extension+".xml";
 xmlfp = open(xmlfile, "w+");
 xmlstring = MakeHockeyXMLFromHockeyDatabase(sdbfile, verbose);
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml is True):
  return xmlstring;
 if(returnxml is False):
  return True;
 return True;

def MakeHockeyXMLFromHockeySQL(sqlfile, sdbfile=None, sqlisfile=True, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeySQL(sqlfile, sdbfile, sqlisfile, False);
 hockeyxmlout = MakeHockeyXMLFromHockeyArray(hockeyarray, verbose);
 return hockeyxmlout;

def MakeHockeyXMLFileFromHockeySQL(insqlfile, sdbfile=None, outxmlfile=None, sqlisfile=True, returnxml=False, verbose=True):
 if(sqlisfile is True and (not os.path.exists(insqlfile) or not os.path.isfile(insqlfile))):
  return False;
 if(outxmlfile is None and sqlisfile is True):
  file_wo_extension, file_extension = os.path.splitext(insqlfile);
  outxmlfile = file_wo_extension+".xml";
 sqlfp = open(outxmlfile, "w+");
 xmlstring = MakeHockeyXMLFromHockeySQL(insqlfile, sdbfile, sqlisfile, verbose);
 sqlfp.write(xmlstring);
 sqlfp.close();
 if(returnxml is True):
  return xmlstring;
 if(returnxml is False):
  return True;
 return True;

def MakeHockeyPythonFromHockeyDatabase(sdbfile, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(sdbfile, False);
 hockeypyout = MakeHockeyPythonFromHockeyArray(hockeyarray, verbose);
 return hockeypyout;

def MakeHockeyPythonFileFromHockeyDatabase(sdbfile, pyfile=None, returnpy=False, verbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(pyfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  pyfile = file_wo_extension+".xml";
 pyfp = open(pyfile, "w+");
 pystring = MakeHockeyPythonFromHockeyDatabase(sdbfile, verbose);
 pyfp.write(pystring);
 pyfp.close();
 if(returnpy is True):
  return pystring;
 if(returnpy is False):
  return True;
 return True;

def MakeHockeyPythonAltFromHockeyDatabase(sdbfile, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyDatabase(sdbfile, False);
 hockeypyout = MakeHockeyPythonAltFromHockeyArray(hockeyarray, verbose);
 return hockeypyout;

def MakeHockeyPythonAltFileFromHockeyDatabase(sdbfile, pyfile=None, returnpy=False, verbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(pyfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  pyfile = file_wo_extension+".xml";
 pyfp = open(pyfile, "w+");
 pystring = MakeHockeyPythonAltFromHockeyDatabase(sdbfile, verbose);
 pyfp.write(pystring);
 pyfp.close();
 if(returnpy is True):
  return pystring;
 if(returnpy is False):
  return True;
 return True;

def MakeHockeySQLFromHockeyDatabase(sdbfile, verbose=True):
 if(os.path.exists(sdbfile) and os.path.isfile(sdbfile) and isinstance(sdbfile, str)):
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
 if(verbose is True):
  VerbosePrintOut("-- "+__program_name__+" SQL Dumper\n");
  VerbosePrintOut("-- version "+__version__+"\n");
  VerbosePrintOut("-- "+__project_url__+"\n");
  VerbosePrintOut("--\n");
  VerbosePrintOut("-- Generation Time: "+time.strftime("%B %d, %Y at %I:%M %p", time.localtime())+"\n");
  VerbosePrintOut("-- SQLite Server version: "+sqlite3.sqlite_version+"\n");
  VerbosePrintOut("-- PySQLite version: "+sqlite3.version+"\n");
  VerbosePrintOut("-- Python Version: "+str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2])+"\n\n");
  VerbosePrintOut("--\n");
  VerbosePrintOut("-- Database: "+sdbfile+"\n");
  VerbosePrintOut("--\n\n");
  VerbosePrintOut("-- --------------------------------------------------------\n\n");
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
  if(verbose is True):
   VerbosePrintOut(" ");
   VerbosePrintOut("--");
   VerbosePrintOut("-- Table structure for table "+str(get_cur_tab)+"");
   VerbosePrintOut("--");
   VerbosePrintOut(" ");
   VerbosePrintOut("DROP TABLE IF EXISTS "+get_cur_tab+";\n\n"+tabresult+";");
   VerbosePrintOut(" ");
   VerbosePrintOut("--");
   VerbosePrintOut("-- Dumping data for table "+str(get_cur_tab)+"");
   VerbosePrintOut("--");
   VerbosePrintOut(" ");
  get_insert_stmt_full = "";
  for tresult_tmp in tresult:
   get_insert_stmt = "INSERT INTO "+str(get_cur_tab)+" (";
   get_insert_stmt_val = "(";
   for result_cal_val in tabresultcol:
    get_insert_stmt += str(result_cal_val)+", ";
   for result_val in tresult_tmp:
    if(isinstance(result_val, str)):
     get_insert_stmt_val += "\""+str(result_val)+"\", ";
    if(isinstance(result_val, int)):
     get_insert_stmt_val += ""+str(result_val)+", ";
    if(isinstance(result_val, float)):
     get_insert_stmt_val += ""+str(result_val)+", ";
   get_insert_stmt = get_insert_stmt[:-2]+") VALUES \n";
   if(verbose is True):
    VerbosePrintOut(get_insert_stmt[:-2]+") VALUES ");
   get_insert_stmt_val = get_insert_stmt_val[:-2]+");";
   if(verbose is True):
    VerbosePrintOut(get_insert_stmt_val[:-2]+");");
   get_insert_stmt_full += str(get_insert_stmt+get_insert_stmt_val)+"\n";
  sqldump = sqldump+get_insert_stmt_full+"\n-- --------------------------------------------------------\n\n";
  if(verbose is True):
   VerbosePrintOut(" ");
   VerbosePrintOut("-- --------------------------------------------------------");
   VerbosePrintOut(" ");
 CloseHockeyDatabase(sqldatacon);
 return sqldump;

def MakeHockeySQLFileFromHockeyDatabase(sdbfile, sqlfile=None, returnsql=False, verbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(sqlfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  sqlfile = file_wo_extension+".sql";
 sqlfp = open(sqlfile, "w+");
 sqlstring = MakeHockeySQLFromHockeyDatabase(sdbfile, verbose);
 sqlfp.write(sqlstring);
 sqlfp.close();
 if(returnsql is True):
  return sqlstring;
 if(returnsql is False):
  return True;
 return True;

def MakeHockeySQLFromHockeyXML(xmlfile, xmlisfile=True, verbose=True):
 hockeyarray = MakeHockeyArrayFromHockeyXML(xmlfile, xmlisfile, False);
 hockeysqlout = MakeHockeySQLFromHockeyArray(hockeyarray, verbose);
 return hockeysqlout;

def MakeHockeySQLFileFromHockeyXML(xmlfile, sqlfile=None, xmlisfile=True, returnsql=False, verbose=True):
 if(xmlisfile is False and (not os.path.exists(xmlfile) and not os.path.isfile(xmlfile))):
  return False;
 if(sqlfile is None and xmlisfile is True):
  file_wo_extension, file_extension = os.path.splitext(xmlfile);
  sqlfile = file_wo_extension+".sql";
 sqlfp = open(sqlfile, "w+");
 sqlstring = MakeHockeySQLFromHockeyXML(xmlfile, xmlisfile, verbose);
 sqlfp.write(sqlstring);
 sqlfp.close();
 if(returnsql is True):
  return sqlstring;
 if(returnsql is False):
  return True;
 return True;

def MakeHockeyXMLFromOldHockeyDatabase(sdbfile, verbose=True):
 hockeyarray = MakeHockeyArrayFromOldHockeyDatabase(sdbfile, False);
 hockeyxmlout = MakeHockeyXMLFromHockeyArray(hockeyarray, verbose);
 return hockeyxmlout;

def MakeHockeyXMLFileFromOldHockeyDatabase(sdbfile, xmlfile=None, returnxml=False, verbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(xmlfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  xmlfile = file_wo_extension+".xml";
 xmlfp = open(xmlfile, "w+");
 xmlstring = MakeHockeyXMLFromOldHockeyDatabase(sdbfile, verbose);
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml is True):
  return xmlstring;
 if(returnxml is False):
  return True;
 return True;

def MakeHockeyPythonFromOldHockeyDatabase(sdbfile, verbose=True):
 xmlstring = MakeHockeyXMLFromOldHockeyDatabase(sdbfile, False);
 pystring = MakeHockeyPythonFromHockeyXML(xmlstring, False, verbose);
 return pystring;

def MakeHockeyPythonFileFromOldHockeyDatabase(sdbfile, pyfile=None, returnpy=False, verbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(pyfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  pyfile = file_wo_extension+".xml";
 pyfp = open(pyfile, "w+");
 pystring = MakeHockeyPythonFromOldHockeyDatabase(sdbfile, verbose);
 pyfp.write(pystring);
 pyfp.close();
 if(returnpy is True):
  return pystring;
 if(returnpy is False):
  return True;
 return True;

def MakeHockeyPythonAltFromOldHockeyDatabase(sdbfile, verbose=True):
 xmlstring = MakeHockeyXMLFromOldHockeyDatabase(sdbfile, False);
 pystring = MakeHockeyPythonAltFromHockeyXML(xmlstring, False, verbose);
 return pystring;

def MakeHockeyPythonAltFileFromOldHockeyDatabase(sdbfile, pyfile=None, returnpy=False, verbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(pyfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  pyfile = file_wo_extension+".xml";
 pyfp = open(pyfile, "w+");
 pystring = MakeHockeyPythonAltFromOldHockeyDatabase(sdbfile, verbose);
 pyfp.write(pystring);
 pyfp.close();
 if(returnpy is True):
  return pystring;
 if(returnpy is False):
  return True;
 return True;

def MakeHockeySQLFromOldHockeyDatabase(sdbfile, verbose=True):
 xmlstring = MakeHockeyXMLFromOldHockeyDatabase(sdbfile, False);
 sqldump = MakeHockeySQLFromHockeyXML(xmlstring, False, True, verbose);
 return sqldump;

def MakeHockeySQLFileFromOldHockeyDatabase(sdbfile, sqlfile=None, returnsql=False, verbose=True):
 if(not os.path.exists(sdbfile) or not os.path.isfile(sdbfile)):
  return False;
 if(sqlfile is None):
  file_wo_extension, file_extension = os.path.splitext(sdbfile);
  sqlfile = file_wo_extension+".sql";
 sqlfp = open(sqlfile, "w+");
 sqlstring = MakeHockeySQLFromOldHockeyDatabase(sdbfile, verbose);
 sqlfp.write(sqlstring);
 sqlfp.close();
 if(returnsql is True):
  return sqlstring;
 if(returnsql is False):
  return True;
 return True;
