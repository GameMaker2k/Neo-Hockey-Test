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

    $FileInfo: hockeyfunctions.py - Last Update: 4/4/2020 Ver. 0.4.0 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals;
import sqlite3, sys, os, re, time, json, pickle, marshal, platform;

try:
 import xml.etree.cElementTree as cElementTree;
except ImportError:
 import xml.etree.ElementTree as cElementTree;

from .hockeydatabase import *;
from .versioninfo import __program_name__, __project__, __project_url__, __version__, __version_alt__, __version_date__, __version_date_alt__, __version_info__, __version_date_info__, __version_date__, __revision__, __revision_id__, __version_date_plusrc__;

''' // User-Agent string for http/https requests '''
useragent_string = "Mozilla/5.0 (compatible; {proname}/{prover}; +{prourl})".format(proname=__project__, prover=__version_alt__, prourl=__project_url__);
if(platform.python_implementation()!=""):
 useragent_string_alt = "Mozilla/5.0 ({osver}; {archtype}; +{prourl}) {pyimp}/{pyver} (KHTML, like Gecko) {proname}/{prover}".format(osver=platform.system()+" "+platform.release(), archtype=platform.machine(), prourl=__project_url__, pyimp=platform.python_implementation(), pyver=platform.python_version(), proname=__project__, prover=__version_alt__);
if(platform.python_implementation()==""):
 useragent_string_alt = "Mozilla/5.0 ({osver}; {archtype}; +{prourl}) {pyimp}/{pyver} (KHTML, like Gecko) {proname}/{prover}".format(osver=platform.system()+" "+platform.release(), archtype=platform.machine(), prourl=__project_url__, pyimp="Python", pyver=platform.python_version(), proname=__project__, prover=__version_alt__);

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

def CopyHockeyDatabase(insdbfile, outsdbfile, returninsdbfile=True, returnoutsdbfile=True):
 if(not CheckHockeySQLiteDatabase(insdbfile)[0]):
  return False;
 if(insdbfile is None):
  insqldatacon = OpenHockeyDatabase(":memory:");
 if(insdbfile is not None and isinstance(insdbfile, basestring)):
  insqldatacon = OpenHockeyDatabase(insdbfile);
 if(insdbfile is not None and isinstance(insdbfile, (tuple, list))):
  insqldatacon = tuple(insdbfile);
 if(outsdbfile is None):
  outsqldatacon = MakeHockeyDatabase(":memory:");
 if(outsdbfile is not None and isinstance(outsdbfile, basestring)):
  outsqldatacon = MakeHockeyDatabase(outsdbfile);
 if(outsdbfile is not None and isinstance(outsdbfile, (tuple, list))):
  outsqldatacon = tuple(outsdbfile);
 if(not isinstance(insqldatacon, (tuple, list)) and not insqldatacon):
  return False;
 if(not isinstance(outsqldatacon, (tuple, list)) and not outsqldatacon):
  return False;
 insqldatacon[1].backup(outsqldatacon);
 if(returninsdbfile and returnoutsdbfile):
  return [insqldatacon, outsqldatacon];
 elif(returninsdbfile and not returnoutsdbfile):
  CloseHockeyDatabase(outsqldatacon);
  return [insqldatacon];
 elif(not returninsdbfile and returnoutsdbfile):
  CloseHockeyDatabase(insqldatacon);
  return [outsqldatacon];
 elif(not returninsdbfile and not returnoutsdbfile):
  CloseHockeyDatabase(insqldatacon);
  CloseHockeyDatabase(outsqldatacon);
  return None;
 else:
  return False;
 return False;

def DumpHockeyDatabase(insdbfile, returninsdbfile=True):
 if(not CheckHockeySQLiteDatabase(insdbfile)[0]):
  return False;
 if(insdbfile is None):
  insqldatacon = OpenHockeyDatabase(":memory:");
 if(insdbfile is not None and isinstance(insdbfile, basestring)):
  insqldatacon = OpenHockeyDatabase(insdbfile);
 if(insdbfile is not None and isinstance(insdbfile, (tuple, list))):
  insqldatacon = tuple(insdbfile);
 if(not isinstance(insqldatacon, (tuple, list)) and not insqldatacon):
  return False;
 dbdumplist = [];
 for line in insqldatacon[1].iterdump():
  dbdumplist.append(line+"\n");
 sqloutstring = ''.join(dbdumplist);
 if(returninsdbfile):
  return [sqloutstring, insqldatacon];
 elif(not returninsdbfile):
  CloseHockeyDatabase(insqldatacon);
  return [sqloutstring];
 else:
  return False;
 return False;

def DumpHockeyDatabaseToSQLFile(insdbfile, outsqlfile, returninsdbfile=True):
 if(not CheckHockeySQLiteDatabase(insdbfile)[0]):
  return False;
 if(insdbfile is None):
  insqldatacon = OpenHockeyDatabase(":memory:");
 if(insdbfile is not None and isinstance(insdbfile, basestring)):
  insqldatacon = OpenHockeyDatabase(insdbfile);
 if(insdbfile is not None and isinstance(insdbfile, (tuple, list))):
  insqldatacon = tuple(insdbfile);
 if(not isinstance(insqldatacon, (tuple, list)) and not insqldatacon):
  return False;
 with open(outsqlfile, 'w+') as f:
  for line in insqldatacon[1].iterdump():
   f.write('%s\n' % line);
 if(returninsdbfile):
  return [insqldatacon];
 elif(not returninsdbfile):
  CloseHockeyDatabase(insqldatacon);
  return None;
 else:
  return False;
 return False;

def RestoreHockeyDatabaseFromSQL(insqlstring, outsdbfile, returnoutsdbfile=True):
 if(outsdbfile is None):
  insqldatacon = MakeHockeyDatabase(":memory:");
 if(outsdbfile is not None and isinstance(outsdbfile, basestring)):
  insqldatacon = MakeHockeyDatabase(outsdbfile);
 if(outsdbfile is not None and isinstance(outsdbfile, (tuple, list))):
  insqldatacon = tuple(outsdbfile);
 if(not isinstance(insqldatacon, (tuple, list)) and not insqldatacon):
  return False;
 insqldatacon[1].executescript(insqlstring);
 if(returnoutsdbfile):
  return [insqldatacon];
 elif(not returnoutsdbfile):
  CloseHockeyDatabase(insqldatacon);
  return None;
 else:
  return False;
 return False;

def RestoreHockeyDatabaseFromSQLFile(insqlfile, outsdbfile, returnoutsdbfile=True):
 if(outsdbfile is None):
  insqldatacon = MakeHockeyDatabase(":memory:");
 if(outsdbfile is not None and isinstance(outsdbfile, basestring)):
  insqldatacon = MakeHockeyDatabase(outsdbfile);
 if(outsdbfile is not None and isinstance(outsdbfile, (tuple, list))):
  insqldatacon = tuple(outsdbfile);
 if(not isinstance(insqldatacon, (tuple, list)) and not insqldatacon):
  return False;
 with open(insqlfile, 'r') as f:
  sqlinput = f.read();
 insqldatacon[1].executescript(sqlinput);
 if(returnoutsdbfile):
  return [insqldatacon];
 elif(not returnoutsdbfile):
  CloseHockeyDatabase(insqldatacon);
  return None;
 else:
  return False;
 return False;

def MakeHockeyXMLFromHockeyArray(inhockeyarray, verbose=True):
 if(not CheckHockeyArray(inhockeyarray)):
  return False;
 if(verbose):
  VerbosePrintOut("<?xml version=\"1.0\" encoding=\"UTF-8\"?>");
 xmlstring = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
 if "database" in inhockeyarray.keys():
  if(verbose):
   VerbosePrintOut("<hockey database=\""+EscapeXMLString(str(inhockeyarray['database']), quote=True)+"\">");
  xmlstring = xmlstring+"<hockey database=\""+EscapeXMLString(str(inhockeyarray['database']), quote=True)+"\">\n";
 if "database" not in inhockeyarray.keys():
  if(verbose):
   VerbosePrintOut("<hockey database=\"./hockeydatabase.db3\">");
  xmlstring = xmlstring+"<hockey database=\"./hockeydatabase.db3\">\n";
 for hlkey in inhockeyarray['leaguelist']:
  if(verbose):
   VerbosePrintOut(" <league name=\""+EscapeXMLString(str(hlkey), quote=True)+"\" fullname=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['fullname']), quote=True)+"\" country=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['fullcountry']), quote=True)+"\" date=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['date']), quote=True)+"\" playofffmt=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['playofffmt']), quote=True)+"\" ordertype=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['ordertype']), quote=True)+"\" conferences=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['conferences']), quote=True)+"\" divisions=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['divisions']), quote=True)+"\">");
  xmlstring = xmlstring+" <league name=\""+EscapeXMLString(str(hlkey), quote=True)+"\" fullname=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['fullname']), quote=True)+"\" country=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['fullcountry']), quote=True)+"\" date=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['date']), quote=True)+"\" playofffmt=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['playofffmt']), quote=True)+"\" ordertype=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['ordertype']), quote=True)+"\" conferences=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['conferences']), quote=True)+"\" divisions=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['divisions']), quote=True)+"\">\n";
  conferencecount = 0;
  conferenceend = len(inhockeyarray[hlkey]['conferencelist']);
  for hckey in inhockeyarray[hlkey]['conferencelist']:
   if(verbose):
    VerbosePrintOut("  <conference name=\""+EscapeXMLString(str(hckey), quote=True)+"\" prefix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey]['conferenceinfo']['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey]['conferenceinfo']['suffix']), quote=True)+"\">");
   xmlstring = xmlstring+"  <conference name=\""+EscapeXMLString(str(hckey), quote=True)+"\" prefix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey]['conferenceinfo']['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey]['conferenceinfo']['suffix']), quote=True)+"\">\n";
   for hdkey in inhockeyarray[hlkey][hckey]['divisionlist']:
    if(verbose):
     VerbosePrintOut("   <division name=\""+EscapeXMLString(str(hdkey), quote=True)+"\" prefix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix']), quote=True)+"\">");
    xmlstring = xmlstring+"   <division name=\""+EscapeXMLString(str(hdkey), quote=True)+"\" prefix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix']), quote=True)+"\">\n";
    for htkey in inhockeyarray[hlkey][hckey][hdkey]['teamlist']:
     if(verbose):
      VerbosePrintOut("    <team city=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']), quote=True)+"\" area=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(htkey), quote=True)+"\" arena=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']), quote=True)+"\" prefix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']), quote=True)+"\" />");
     xmlstring = xmlstring+"    <team city=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']), quote=True)+"\" area=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(htkey), quote=True)+"\" arena=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']), quote=True)+"\" prefix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']), quote=True)+"\" />\n";
    if(verbose):
     VerbosePrintOut("   </division>");
    xmlstring = xmlstring+"   </division>\n";
   if(verbose):
    VerbosePrintOut("  </conference>");
   xmlstring = xmlstring+"  </conference>\n";
   conferencecount = conferencecount + 1;
  if(conferencecount>=conferenceend):
   hasarenas = False;
   if(len(inhockeyarray[hlkey]['arenas'])>0):
    hasarenas = True;
    if(verbose):
     VerbosePrintOut("  <arenas>");
    xmlstring = xmlstring+"  <arenas>\n";
   for hakey in inhockeyarray[hlkey]['arenas']:
    if(hakey):
     hasarenas = True;
     if(verbose):
      VerbosePrintOut("   <arena city=\""+EscapeXMLString(str(hakey['city']), quote=True)+"\" area=\""+EscapeXMLString(str(hakey['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(hakey['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(hakey['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(hakey['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(hakey['name']), quote=True)+"\" />");
     xmlstring = xmlstring+"   <arena city=\""+EscapeXMLString(str(hakey['city']), quote=True)+"\" area=\""+EscapeXMLString(str(hakey['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(hakey['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(hakey['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(hakey['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(hakey['name']), quote=True)+"\" />\n";
   if(hasarenas):
    if(verbose):
     VerbosePrintOut("  </arenas>");
    xmlstring = xmlstring+"  </arenas>\n";
   hasgames = False;
   if(len(inhockeyarray[hlkey]['games'])>0):
    hasgames = True;
    if(verbose):
     VerbosePrintOut("  <games>");
    xmlstring = xmlstring+"  <games>\n";
   for hgkey in inhockeyarray[hlkey]['games']:
    if(hgkey):
     hasgames = True;
     if(verbose):
      VerbosePrintOut("   <game date=\""+EscapeXMLString(str(hgkey['date']), quote=True)+"\" hometeam=\""+EscapeXMLString(str(hgkey['hometeam']), quote=True)+"\" awayteam=\""+EscapeXMLString(str(hgkey['awayteam']), quote=True)+"\" goals=\""+EscapeXMLString(str(hgkey['goals']), quote=True)+"\" sogs=\""+EscapeXMLString(str(hgkey['sogs']), quote=True)+"\" ppgs=\""+EscapeXMLString(str(hgkey['ppgs']), quote=True)+"\" shgs=\""+EscapeXMLString(str(hgkey['shgs']), quote=True)+"\" penalties=\""+EscapeXMLString(str(hgkey['penalties']), quote=True)+"\" pims=\""+EscapeXMLString(str(hgkey['pims']), quote=True)+"\" hits=\""+EscapeXMLString(str(hgkey['hits']), quote=True)+"\" takeaways=\""+EscapeXMLString(str(hgkey['takeaways']), quote=True)+"\" faceoffwins=\""+EscapeXMLString(str(hgkey['faceoffwins']), quote=True)+"\" atarena=\""+EscapeXMLString(str(hgkey['atarena']), quote=True)+"\" isplayoffgame=\""+EscapeXMLString(str(hgkey['isplayoffgame']), quote=True)+"\" />");
     xmlstring = xmlstring+"   <game date=\""+EscapeXMLString(str(hgkey['date']), quote=True)+"\" hometeam=\""+EscapeXMLString(str(hgkey['hometeam']), quote=True)+"\" awayteam=\""+EscapeXMLString(str(hgkey['awayteam']), quote=True)+"\" goals=\""+EscapeXMLString(str(hgkey['goals']), quote=True)+"\" sogs=\""+EscapeXMLString(str(hgkey['sogs']), quote=True)+"\" ppgs=\""+EscapeXMLString(str(hgkey['ppgs']), quote=True)+"\" shgs=\""+EscapeXMLString(str(hgkey['shgs']), quote=True)+"\" penalties=\""+EscapeXMLString(str(hgkey['penalties']), quote=True)+"\" pims=\""+EscapeXMLString(str(hgkey['pims']), quote=True)+"\" hits=\""+EscapeXMLString(str(hgkey['hits']), quote=True)+"\" takeaways=\""+EscapeXMLString(str(hgkey['takeaways']), quote=True)+"\" faceoffwins=\""+EscapeXMLString(str(hgkey['faceoffwins']), quote=True)+"\" atarena=\""+EscapeXMLString(str(hgkey['atarena']), quote=True)+"\" isplayoffgame=\""+EscapeXMLString(str(hgkey['isplayoffgame']), quote=True)+"\" />\n";
   if(hasgames):
    if(verbose):
     VerbosePrintOut("  </games>");
    xmlstring = xmlstring+"  </games>\n";
  if(verbose):
   VerbosePrintOut(" </league>");
  xmlstring = xmlstring+" </league>\n";
 if(verbose):
  VerbosePrintOut("</hockey>");
 xmlstring = xmlstring+"</hockey>\n";
 return xmlstring;

def MakeHockeyXMLFileFromHockeyArray(inhockeyarray, outxmlfile=None, returnxml=False, verbose=True):
 if(outxmlfile is None):
  return False;
 xmlfp = open(outxmlfile, "w+");
 xmlstring = MakeHockeyXMLFromHockeyArray(inhockeyarray, verbose);
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml):
  return xmlstring;
 if(not returnxml):
  return True;
 return True;

def MakeHockeyJSONFromHockeyArray(inhockeyarray, jsonindent=1, verbose=True):
 if(not CheckHockeyArray(inhockeyarray) and not CheckHockeySQLiteArray(inhockeyarray)):
  return False;
 jsonstring = json.dumps(inhockeyarray, indent=jsonindent);
 if(verbose):
  VerbosePrintOut(jsonstring);
 return jsonstring;

def MakeHockeyJSONFileFromHockeyArray(inhockeyarray, outjsonfile=None, returnjson=False, jsonindent=1, verbose=True):
 if(outjsonfile is None):
  return False;
 jsonfp = open(outjsonfile, "w+");
 jsonstring = MakeHockeyJSONFromHockeyArray(inhockeyarray, jsonindent, verbose);
 jsonfp.write(jsonstring);
 jsonfp.close();
 if(returnjson):
  return jsonstring;
 if(not returnjson):
  return True;
 return True;

def MakeHockeyArrayFromHockeyJSON(injsonfile, jsonisfile=True, verbose=True):
 if(jsonisfile and ((os.path.exists(injsonfile) and os.path.isfile(injsonfile)) or re.findall("^(http|https)\:\/\/", injsonfile))):
  if(re.findall("^(http|https)\:\/\/", injsonfile)):
   jsonheaders = {'User-Agent': useragent_string};
   hockeyarray = json.load(urllib2.urlopen(urllib2.Request(injsonfile, None, jsonheaders)));
  else:
   jsonfp = open(injsonfile, "r");
   hockeyarray = json.load(jsonfp);
   jsonfp.close();
 elif(not jsonisfile):
  hockeyarray = json.loads(injsonfile);
 else:
  return False;
 if(not CheckHockeyArray(hockeyarray) and not CheckHockeySQLiteArray(hockeyarray)):
  return False;
 if(verbose):
  xmlstring = MakeHockeyXMLFromHockeyArray(hockeyarray, True);
  del xmlstring;
 return hockeyarray;

def MakeHockeyPickleFromHockeyArray(inhockeyarray, verbose=True):
 if(not CheckHockeyArray(inhockeyarray) and not CheckHockeySQLiteArray(inhockeyarray)):
  return False;
 picklestring = pickle.dumps(inhockeyarray);
 if(verbose):
  VerbosePrintOut(picklestring);
 return picklestring;

def MakeHockeyPickleFileFromHockeyArray(inhockeyarray, outpicklefile=None, returnpickle=False, verbose=True):
 if(outpicklefile is None):
  return False;
 picklefp = open(outpicklefile, "w+");
 picklestring = MakeHockeyPickleFromHockeyArray(inhockeyarray, verbose);
 picklefp.write(picklestring);
 picklefp.close();
 if(returnpickle):
  return picklestring;
 if(not returnpickle):
  return True;
 return True;

def MakeHockeyArrayFromHockeyPickle(inpicklefile, pickleisfile=True, verbose=True):
 if(pickleisfile and ((os.path.exists(inpicklefile) and os.path.isfile(inpicklefile)) or re.findall("^(http|https)\:\/\/", inpicklefile))):
  if(re.findall("^(http|https)\:\/\/", inpicklefile)):
   pickleheaders = {'User-Agent': useragent_string};
   hockeyarray = pickle.load(urllib2.urlopen(urllib2.Request(inpicklefile, None, pickleheaders)));
  else:
   picklefp = open(inpicklefile, "r");
   hockeyarray = pickle.load(picklefp);
   picklefp.close();
 elif(not pickleisfile):
  hockeyarray = pickle.loads(inpicklefile);
 else:
  return False;
 if(not CheckHockeyArray(hockeyarray) and not CheckHockeySQLiteArray(hockeyarray)):
  return False;
 if(verbose):
  xmlstring = MakeHockeyXMLFromHockeyArray(hockeyarray, True);
  del xmlstring;
 return hockeyarray;

def MakeHockeyMarshalFromHockeyArray(inhockeyarray, verbose=True):
 if(not CheckHockeyArray(inhockeyarray) and not CheckHockeySQLiteArray(inhockeyarray)):
  return False;
 marshalstring = marshal.dumps(inhockeyarray);
 if(verbose):
  VerbosePrintOut(marshalstring);
 return marshalstring;

def MakeHockeyMarshalFileFromHockeyArray(inhockeyarray, outmarshalfile=None, returnmarshal=False, verbose=True):
 if(outmarshalfile is None):
  return False;
 marshalfp = open(outmarshalfile, "w+");
 marshalstring = MakeHockeyMarshalFromHockeyArray(inhockeyarray, verbose);
 marshalfp.write(marshalstring);
 marshalfp.close();
 if(returnmarshal):
  return marshalstring;
 if(not returnmarshal):
  return True;
 return True;

def MakeHockeyArrayFromHockeyMarshal(inmarshalfile, marshalisfile=True, verbose=True):
 if(marshalisfile and ((os.path.exists(inmarshalfile) and os.path.isfile(inmarshalfile)) or re.findall("^(http|https)\:\/\/", inmarshalfile))):
  if(re.findall("^(http|https)\:\/\/", inmarshalfile)):
   marshalheaders = {'User-Agent': useragent_string};
   hockeyarray = marshal.load(urllib2.urlopen(urllib2.Request(inmarshalfile, None, marshalheaders)));
  else:
   marshalfp = open(inmarshalfile, "r");
   hockeyarray = marshal.load(marshalfp);
   marshalfp.close();
 elif(not marshalisfile):
  hockeyarray = marshal.loads(inmarshalfile);
 else:
  return False;
 if(not CheckHockeyArray(hockeyarray) and not CheckHockeySQLiteArray(hockeyarray)):
  return False;
 if(verbose):
  xmlstring = MakeHockeyXMLFromHockeyArray(hockeyarray, True);
  del xmlstring;
 return hockeyarray;

def MakeHockeyArrayFromHockeyXML(inxmlfile, xmlisfile=True, verbose=True):
 if(xmlisfile and ((os.path.exists(inxmlfile) and os.path.isfile(inxmlfile)) or re.findall("^(http|https)\:\/\/", inxmlfile))):
  xmlheaders = {'User-Agent': useragent_string};
  try:
   if(re.findall("^(http|https)\:\/\/", inxmlfile)):
    hockeyfile = cElementTree.ElementTree(file=urllib2.urlopen(urllib2.Request(inxmlfile, None, xmlheaders)));
   else:
    hockeyfile = cElementTree.ElementTree(file=inxmlfile);
  except cElementTree.ParseError: 
   return False;
 elif(not xmlisfile):
  try:
   hockeyfile = cElementTree.ElementTree(cElementTree.fromstring(inxmlfile));
  except cElementTree.ParseError: 
   return False;
 else:
  return False;
 gethockey = hockeyfile.getroot();
 if(verbose):
  VerbosePrintOut("<?xml version=\"1.0\" encoding=\"UTF-8\"?>");
 if(gethockey.tag == "hockey"):
  if(verbose):
   VerbosePrintOut("<hockey database=\""+EscapeXMLString(str(gethockey.attrib['database']), quote=True)+"\">");
 leaguearrayout = { 'database': str(gethockey.attrib['database']) };
 leaguelist = [];
 for getleague in gethockey:
  leaguearray = {};
  arenalist = [];
  gamelist = [];
  if(getleague.tag=="league"):
   if(verbose):
    VerbosePrintOut(" <league name=\""+EscapeXMLString(str(getleague.attrib['name']), quote=True)+"\" fullname=\""+EscapeXMLString(str(getleague.attrib['fullname']), quote=True)+"\" country=\""+EscapeXMLString(str(getleague.attrib['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(getleague.attrib['fullcountry']), quote=True)+"\" date=\""+EscapeXMLString(str(getleague.attrib['date']), quote=True)+"\" playofffmt=\""+EscapeXMLString(str(getleague.attrib['playofffmt']), quote=True)+"\" ordertype=\""+EscapeXMLString(str(getleague.attrib['ordertype']), quote=True)+"\" conferences=\""+EscapeXMLString(str(getleague.attrib['conferences']), quote=True)+"\" divisions=\""+EscapeXMLString(str(getleague.attrib['divisions']), quote=True)+"\">");
   tempdict = { 'leagueinfo': { 'name': str(getleague.attrib['name']), 'fullname': str(getleague.attrib['fullname']), 'country': str(getleague.attrib['country']), 'fullcountry': str(getleague.attrib['fullcountry']), 'date': str(getleague.attrib['date']), 'playofffmt': str(getleague.attrib['playofffmt']), 'ordertype': str(getleague.attrib['ordertype']), 'conferences': str(getleague.attrib['conferences']), 'divisions': str(getleague.attrib['divisions']) }, 'quickinfo': {'conferenceinfo': {}, 'divisioninfo': {}, 'teaminfo': {} } };
   leaguearray.update( { str(getleague.attrib['name']): tempdict } );
   leaguelist.append(str(getleague.attrib['name']));
  if(getleague.tag == "league"):
   conferencelist = [];
   for getconference in getleague:
    if(getconference.tag == "conference"):
     if(verbose):
      VerbosePrintOut("  <conference name=\""+EscapeXMLString(str(getconference.attrib['name']), quote=True)+"\" prefix=\""+EscapeXMLString(str(getconference.attrib['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(getconference.attrib['suffix']), quote=True)+"\">");
     ConferenceFullName = GetFullTeamName(str(getconference.attrib['name']), str(getconference.attrib['prefix']), str(getconference.attrib['suffix']));
     leaguearray[str(getleague.attrib['name'])].update( { str(getconference.attrib['name']): { 'conferenceinfo': { 'name': str(getconference.attrib['name']), 'prefix': str(getconference.attrib['prefix']), 'suffix': str(getconference.attrib['suffix']), 'fullname': str(ConferenceFullName), 'league': str(getleague.attrib['name']) } } } );
     leaguearray[str(getleague.attrib['name'])]['quickinfo']['conferenceinfo'].update( { str(getconference.attrib['name']): { 'name': str(getconference.attrib['name']), 'fullname': str(ConferenceFullName), 'league': str(getleague.attrib['name']) } } );
     conferencelist.append(str(getconference.attrib['name']));
    divisiondict = {};
    divisionlist = [];
    if(getconference.tag == "conference"):
     for getdivision in getconference:
      if(verbose):
       VerbosePrintOut("   <division name=\""+str(getdivision.attrib['name'])+"\" prefix=\""+EscapeXMLString(str(getdivision.attrib['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(getdivision.attrib['suffix']), quote=True)+"\">");
      DivisionFullName = GetFullTeamName(str(getdivision.attrib['name']), str(getdivision.attrib['prefix']), str(getdivision.attrib['suffix']));
      leaguearray[str(getleague.attrib['name'])][str(getconference.attrib['name'])].update( { str(getdivision.attrib['name']): { 'divisioninfo': { 'name': str(getdivision.attrib['name']), 'prefix': str(getdivision.attrib['prefix']), 'suffix': str(getdivision.attrib['suffix']), 'fullname': str(DivisionFullName), 'league': str(getleague.attrib['name']), 'conference': str(getconference.attrib['name']) } } } );
      leaguearray[str(getleague.attrib['name'])]['quickinfo']['divisioninfo'].update( { str(getdivision.attrib['name']): { 'name': str(getdivision.attrib['name']), 'fullname': str(DivisionFullName), 'league': str(getleague.attrib['name']), 'conference': str(getconference.attrib['name']) } } );
      divisionlist.append(str(getdivision.attrib['name']));
      teamdist = {};
      teamlist = [];
      if(getdivision.tag == "division"):
       for getteam in getdivision:
        if(getteam.tag == "team"):
         if(verbose):
          VerbosePrintOut("    <team city=\""+EscapeXMLString(str(getteam.attrib['city']), quote=True)+"\" area=\""+EscapeXMLString(str(getteam.attrib['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(getteam.attrib['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(getteam.attrib['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(getteam.attrib['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(getteam.attrib['name']), quote=True)+"\" arena=\""+EscapeXMLString(str(getteam.attrib['arena']), quote=True)+"\" prefix=\""+EscapeXMLString(str(getteam.attrib['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(getteam.attrib['suffix']), quote=True)+"\" />");
         fullteamname = GetFullTeamName(str(getteam.attrib['name']), str(getteam.attrib['prefix']), str(getteam.attrib['suffix']));
         leaguearray[str(getleague.attrib['name'])][str(getconference.attrib['name'])][str(getdivision.attrib['name'])].update( { str(getteam.attrib['name']): { 'teaminfo': { 'city': str(getteam.attrib['city']), 'area': str(getteam.attrib['area']), 'fullarea': str(getteam.attrib['fullarea']), 'country': str(getteam.attrib['country']), 'fullcountry': str(getteam.attrib['fullcountry']), 'name': str(getteam.attrib['name']), 'fullname': fullteamname, 'arena': str(getteam.attrib['arena']), 'prefix': str(getteam.attrib['prefix']), 'suffix': str(getteam.attrib['suffix']), 'league': str(getleague.attrib['name']), 'conference': str(getconference.attrib['name']), 'division': str(getdivision.attrib['name']) } } } );
         leaguearray[str(getleague.attrib['name'])]['quickinfo']['teaminfo'].update( { str(getteam.attrib['name']): { 'name': str(getteam.attrib['name']), 'fullname': fullteamname, 'league': str(getleague.attrib['name']), 'conference': str(getconference.attrib['name']), 'division': str(getdivision.attrib['name']) } } );
         teamlist.append(str(getteam.attrib['name']));
       leaguearray[str(getleague.attrib['name'])][str(getconference.attrib['name'])][str(getdivision.attrib['name'])].update( { 'teamlist': teamlist } );
       if(verbose):
        VerbosePrintOut("   </division>");
     leaguearray[str(getleague.attrib['name'])][str(getconference.attrib['name'])].update( { 'divisionlist': divisionlist } );
     if(verbose):
      VerbosePrintOut("  </conference>");
    if(getconference.tag == "arenas"):
     if(verbose):
      VerbosePrintOut("  <arenas>");
     for getarenas in getconference:
      if(verbose):
       VerbosePrintOut("   <arena city=\""+EscapeXMLString(str(getarenas.attrib['city']), quote=True)+"\" area=\""+EscapeXMLString(str(getarenas.attrib['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(getarenas.attrib['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(getarenas.attrib['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(getarenas.attrib['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(getarenas.attrib['name']), quote=True)+"\" />");
      arenalist.append( { 'city': str(getarenas.attrib['city']), 'area': str(getarenas.attrib['area']), 'fullarea': str(getarenas.attrib['fullarea']), 'country': str(getarenas.attrib['country']), 'fullcountry': str(getarenas.attrib['fullcountry']), 'name': str(getarenas.attrib['name']) } );
     if(verbose):
      VerbosePrintOut("  </arenas>");
    leaguearray[str(getleague.attrib['name'])].update( { "arenas": arenalist } );
    if(getconference.tag == "games"):
     if(verbose):
      VerbosePrintOut("  <games>");
     for getgame in getconference:
      if(verbose):
       VerbosePrintOut("   <game date=\""+EscapeXMLString(str(getgame.attrib['date']), quote=True)+"\" hometeam=\""+EscapeXMLString(str(getgame.attrib['hometeam']), quote=True)+"\" awayteam=\""+EscapeXMLString(str(getgame.attrib['awayteam']), quote=True)+"\" goals=\""+EscapeXMLString(str(getgame.attrib['goals']), quote=True)+"\" sogs=\""+EscapeXMLString(str(getgame.attrib['sogs']), quote=True)+"\" ppgs=\""+EscapeXMLString(str(getgame.attrib['ppgs']), quote=True)+"\" shgs=\""+EscapeXMLString(str(getgame.attrib['shgs']), quote=True)+"\" penalties=\""+EscapeXMLString(str(getgame.attrib['penalties']), quote=True)+"\" pims=\""+EscapeXMLString(str(getgame.attrib['pims']), quote=True)+"\" hits=\""+EscapeXMLString(str(getgame.attrib['hits']), quote=True)+"\" takeaways=\""+EscapeXMLString(str(getgame.attrib['takeaways']), quote=True)+"\" faceoffwins=\""+EscapeXMLString(str(getgame.attrib['faceoffwins']), quote=True)+"\" atarena=\""+EscapeXMLString(str(getgame.attrib['atarena']), quote=True)+"\" isplayoffgame=\""+EscapeXMLString(str(getgame.attrib['isplayoffgame']), quote=True)+"\" />");
      gamelist.append( { 'date': str(getgame.attrib['date']), 'hometeam': str(getgame.attrib['hometeam']), 'awayteam': str(getgame.attrib['awayteam']), 'goals': str(getgame.attrib['goals']), 'sogs': str(getgame.attrib['sogs']), 'ppgs': str(getgame.attrib['ppgs']), 'shgs': str(getgame.attrib['shgs']), 'penalties': str(getgame.attrib['penalties']), 'pims': str(getgame.attrib['pims']), 'hits': str(getgame.attrib['hits']), 'takeaways': str(getgame.attrib['takeaways']), 'faceoffwins': str(getgame.attrib['faceoffwins']), 'atarena': str(getgame.attrib['atarena']), 'isplayoffgame': str(getgame.attrib['isplayoffgame']) } );
     if(verbose):
      VerbosePrintOut("  </games>");
    leaguearray[str(getleague.attrib['name'])].update( { "games": gamelist } );
   leaguearray[str(getleague.attrib['name'])].update( { 'conferencelist': conferencelist } );
   leaguearrayout.update(leaguearray);
   if(verbose):
    VerbosePrintOut(" </league>");
 leaguearrayout.update( { 'leaguelist': leaguelist } );
 if(verbose):
  VerbosePrintOut("</hockey>");
 if(not CheckHockeyArray(leaguearrayout)):
  return False;
 return leaguearrayout;

def MakeHockeyDatabaseFromHockeyArray(inhockeyarray, sdbfile=None, returnxml=False, returndb=False, verbose=True):
 if(not CheckHockeyArray(inhockeyarray)):
  return False;
 if(sdbfile is None and "database" in inhockeyarray.keys()):
  sqldatacon = MakeHockeyDatabase(inhockeyarray['database']);
 if(sdbfile is None and "database" not in inhockeyarray.keys()):
  sqldatacon = MakeHockeyDatabase(":memory:");
 if(sdbfile is not None and isinstance(sdbfile, basestring)):
  sqldatacon = MakeHockeyDatabase(sdbfile);
 if(sdbfile is not None and isinstance(sdbfile, (tuple, list))):
  sqldatacon = tuple(sdbfile);
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(verbose):
  VerbosePrintOut("<?xml version=\"1.0\" encoding=\"UTF-8\"?>");
 xmlstring = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
 if(verbose):
  VerbosePrintOut("<hockey database=\""+EscapeXMLString(str(inhockeyarray['database']), quote=True)+"\">");
 xmlstring = xmlstring+"<hockey database=\""+EscapeXMLString(str(inhockeyarray['database']), quote=True)+"\">\n";
 leaguecount = 0;
 for hlkey in inhockeyarray['leaguelist']:
  if(leaguecount==0):
   MakeHockeyLeagueTable(sqldatacon);
  MakeHockeyTeamTable(sqldatacon, hlkey);
  MakeHockeyConferenceTable(sqldatacon, hlkey);
  MakeHockeyGameTable(sqldatacon, hlkey);
  MakeHockeyDivisionTable(sqldatacon, hlkey);
  HockeyLeagueHasDivisions = True;
  if(inhockeyarray[hlkey]['leagueinfo']['conferences'].lower()=="no"):
   HockeyLeagueHasDivisions = False;
  HockeyLeagueHasConferences = True;
  if(inhockeyarray[hlkey]['leagueinfo']['divisions'].lower()=="no"):
   HockeyLeagueHasConferences = False;
  MakeHockeyLeague(sqldatacon, hlkey, inhockeyarray[hlkey]['leagueinfo']['fullname'], inhockeyarray[hlkey]['leagueinfo']['country'], inhockeyarray[hlkey]['leagueinfo']['fullcountry'], inhockeyarray[hlkey]['leagueinfo']['date'], inhockeyarray[hlkey]['leagueinfo']['playofffmt'], inhockeyarray[hlkey]['leagueinfo']['ordertype']);
  if(verbose):
   VerbosePrintOut(" <league name=\""+EscapeXMLString(str(hlkey), quote=True)+"\" fullname=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['fullname']), quote=True)+"\" country=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['fullcountry']), quote=True)+"\" date=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['date']), quote=True)+"\" playofffmt=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['playofffmt']), quote=True)+"\" ordertype=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['ordertype']), quote=True)+"\" conferences=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['conferences']), quote=True)+"\" divisions=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['divisions']), quote=True)+"\">");
  xmlstring = xmlstring+" <league name=\""+EscapeXMLString(str(hlkey), quote=True)+"\" fullname=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['fullname']), quote=True)+"\" country=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['fullcountry']), quote=True)+"\" date=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['date']), quote=True)+"\" playofffmt=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['playofffmt']), quote=True)+"\" ordertype=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['ordertype']), quote=True)+"\" conferences=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['conferences']), quote=True)+"\" divisions=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['divisions']), quote=True)+"\">\n";
  leaguecount = leaguecount + 1;
  conferencecount = 0;
  conferenceend = len(inhockeyarray[hlkey]['conferencelist']);
  for hckey in inhockeyarray[hlkey]['conferencelist']:
   MakeHockeyConference(sqldatacon, hlkey, hckey, inhockeyarray[hlkey][hckey]['conferenceinfo']['prefix'], inhockeyarray[hlkey][hckey]['conferenceinfo']['suffix'], HockeyLeagueHasConferences);
   if(verbose):
    VerbosePrintOut("  <conference name=\""+EscapeXMLString(str(hckey), quote=True)+"\" prefix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey]['conferenceinfo']['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey]['conferenceinfo']['suffix']), quote=True)+"\">");
   xmlstring = xmlstring+"  <conference name=\""+EscapeXMLString(str(hckey), quote=True)+"\" prefix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey]['conferenceinfo']['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey]['conferenceinfo']['suffix']), quote=True)+"\">\n";
   for hdkey in inhockeyarray[hlkey][hckey]['divisionlist']:
    MakeHockeyDivision(sqldatacon, hlkey, hdkey, hckey, inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix'], inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix'], HockeyLeagueHasConferences, HockeyLeagueHasDivisions);
    if(verbose):
     VerbosePrintOut("   <division name=\""+EscapeXMLString(str(hdkey), quote=True)+"\" prefix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix']), quote=True)+"\">");
    xmlstring = xmlstring+"   <division name=\""+EscapeXMLString(str(hdkey), quote=True)+"\" prefix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix']), quote=True)+"\">\n";
    for htkey in inhockeyarray[hlkey][hckey][hdkey]['teamlist']:
     MakeHockeyTeam(sqldatacon, hlkey, str(inhockeyarray[hlkey]['leagueinfo']['date']), inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea'], htkey, inhockeyarray[hlkey][hckey]['conferenceinfo']['name'], inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['name'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix'], HockeyLeagueHasConferences, HockeyLeagueHasDivisions);
     if(verbose):
      VerbosePrintOut("    <team city=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']), quote=True)+"\" area=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(htkey), quote=True)+"\" arena=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']), quote=True)+"\" prefix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']), quote=True)+"\" />");
     xmlstring = xmlstring+"    <team city=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']), quote=True)+"\" area=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(htkey), quote=True)+"\" arena=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']), quote=True)+"\" prefix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']), quote=True)+"\" />\n";
    if(verbose):
     VerbosePrintOut("   </division>");
    xmlstring = xmlstring+"   </division>\n";
   if(verbose):
    VerbosePrintOut("  </conference>");
   xmlstring = xmlstring+"  </conference>\n";
   conferencecount = conferencecount + 1;
  if(conferencecount>=conferenceend):
   hasarenas = False;
   if(len(inhockeyarray[hlkey]['arenas'])>0):
    hasarenas = True;
    if(verbose):
     VerbosePrintOut("  <arenas>");
    xmlstring = xmlstring+"  <arenas>\n";
   for hakey in inhockeyarray[hlkey]['arenas']:
    if(hakey):
     hasarenas = True;
     MakeHockeyArena(sqldatacon, hlkey, hakey['city'], hakey['area'], hakey['country'], hakey['fullcountry'], hakey['fullarea'], hakey['name']);
     if(verbose):
      VerbosePrintOut("   <arena city=\""+EscapeXMLString(str(hakey['city']), quote=True)+"\" area=\""+EscapeXMLString(str(hakey['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(hakey['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(hakey['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(hakey['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(hakey['name']), quote=True)+"\" />");
     xmlstring = xmlstring+"   <arena city=\""+EscapeXMLString(str(hakey['city']), quote=True)+"\" area=\""+EscapeXMLString(str(hakey['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(hakey['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(hakey['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(hakey['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(hakey['name']), quote=True)+"\" />\n";
   if(hasarenas):
    if(verbose):
     VerbosePrintOut("  </arenas>");
    xmlstring = xmlstring+"  </arenas>\n";
   hasgames = False;
   if(len(inhockeyarray[hlkey]['games'])>0):
    hasgames = True;
    if(verbose):
     VerbosePrintOut("  <games>");
    xmlstring = xmlstring+"  <games>\n";
   for hgkey in inhockeyarray[hlkey]['games']:
    if(hgkey):
     hasgames = True;
     MakeHockeyGame(sqldatacon, hlkey, hgkey['date'], hgkey['hometeam'], hgkey['awayteam'], hgkey['goals'], hgkey['sogs'], hgkey['ppgs'], hgkey['shgs'], hgkey['penalties'], hgkey['pims'], hgkey['hits'], hgkey['takeaways'], hgkey['faceoffwins'], hgkey['atarena'], hgkey['isplayoffgame']);
     if(verbose):
      VerbosePrintOut("   <game date=\""+EscapeXMLString(str(hgkey['date']), quote=True)+"\" hometeam=\""+EscapeXMLString(str(hgkey['hometeam']), quote=True)+"\" awayteam=\""+EscapeXMLString(str(hgkey['awayteam']), quote=True)+"\" goals=\""+EscapeXMLString(str(hgkey['goals']), quote=True)+"\" sogs=\""+EscapeXMLString(str(hgkey['sogs']), quote=True)+"\" ppgs=\""+EscapeXMLString(str(hgkey['ppgs']), quote=True)+"\" shgs=\""+EscapeXMLString(str(hgkey['shgs']), quote=True)+"\" penalties=\""+EscapeXMLString(str(hgkey['penalties']), quote=True)+"\" pims=\""+EscapeXMLString(str(hgkey['pims']), quote=True)+"\" hits=\""+EscapeXMLString(str(hgkey['hits']), quote=True)+"\" takeaways=\""+EscapeXMLString(str(hgkey['takeaways']), quote=True)+"\" faceoffwins=\""+EscapeXMLString(str(hgkey['faceoffwins']), quote=True)+"\" atarena=\""+EscapeXMLString(str(hgkey['atarena']), quote=True)+"\" isplayoffgame=\""+EscapeXMLString(str(hgkey['isplayoffgame']), quote=True)+"\" />");
     xmlstring = xmlstring+"   <game date=\""+EscapeXMLString(str(hgkey['date']), quote=True)+"\" hometeam=\""+EscapeXMLString(str(hgkey['hometeam']), quote=True)+"\" awayteam=\""+EscapeXMLString(str(hgkey['awayteam']), quote=True)+"\" goals=\""+EscapeXMLString(str(hgkey['goals']), quote=True)+"\" sogs=\""+EscapeXMLString(str(hgkey['sogs']), quote=True)+"\" ppgs=\""+EscapeXMLString(str(hgkey['ppgs']), quote=True)+"\" shgs=\""+EscapeXMLString(str(hgkey['shgs']), quote=True)+"\" penalties=\""+EscapeXMLString(str(hgkey['penalties']), quote=True)+"\" pims=\""+EscapeXMLString(str(hgkey['pims']), quote=True)+"\" hits=\""+EscapeXMLString(str(hgkey['hits']), quote=True)+"\" takeaways=\""+EscapeXMLString(str(hgkey['takeaways']), quote=True)+"\" faceoffwins=\""+EscapeXMLString(str(hgkey['faceoffwins']), quote=True)+"\" atarena=\""+EscapeXMLString(str(hgkey['atarena']), quote=True)+"\" isplayoffgame=\""+EscapeXMLString(str(hgkey['isplayoffgame']), quote=True)+"\" />\n";
   if(hasgames):
    if(verbose):
     VerbosePrintOut("  </games>");
    xmlstring = xmlstring+"  </games>\n";
 if(verbose):
  VerbosePrintOut(" </league>");
 xmlstring = xmlstring+" </league>\n";
 if(verbose):
  VerbosePrintOut("</hockey>");
 xmlstring = xmlstring+"</hockey>\n";
 if(not returndb):
  CloseHockeyDatabase(sqldatacon);
 if(returndb and returnxml):
  return [xmlstring, sqldatacon];
 if(returnxml and not returndb):
  return [xmlstring];
 if(not returnxml and returndb):
  return [sqldatacon];
 if(not returnxml and not returndb):
  return True;
 return True;

def HockeyDatabaseFromHockeyArrayWrite(inhockeyarray, sdbfile=None, outxmlfile=None, returnxml=False, verbose=True):
 if(outxmlfile is None):
  return False;
 xmlfp = open(outxmlfile, "w+");
 xmlstring = MakeHockeyDatabaseFromHockeyArray(inhockeyarray, sdbfile, True, False, verbose);
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml):
  return xmlstring;
 if(not returnxml):
  return True;
 return True;

def MakeHockeyPythonFromHockeyArray(inhockeyarray, verbose=True):
 if(not CheckHockeyArray(inhockeyarray)):
  return False;
 pyfilename = __package__;
 if(pyfilename=="__main__"):
  pyfilename = os.path.splitext(os.path.basename(__file__))[0];
 if(verbose):
  VerbosePrintOut("#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nfrom __future__ import absolute_import, division, print_function, unicode_literals;\nimport "+pyfilename+";\n");
 pystring = "#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nfrom __future__ import absolute_import, division, print_function, unicode_literals;\nimport "+pyfilename+";\n\n";
 if(verbose):
  VerbosePrintOut("sqldatacon = "+pyfilename+".MakeHockeyDatabase(\""+inhockeyarray['database']+"\");");
 pystring = pystring+"sqldatacon = "+pyfilename+".MakeHockeyDatabase(\""+inhockeyarray['database']+"\");\n";
 if(verbose):
  VerbosePrintOut(pyfilename+".MakeHockeyLeagueTable(sqldatacon);");
 pystring = pystring+pyfilename+".MakeHockeyLeagueTable(sqldatacon);\n";
 for hlkey in inhockeyarray['leaguelist']:
  HockeyLeagueHasDivisions = True;
  if(inhockeyarray[hlkey]['leagueinfo']['conferences'].lower()=="no"):
   HockeyLeagueHasDivisions = False;
  HockeyLeagueHasConferences = True;
  if(inhockeyarray[hlkey]['leagueinfo']['divisions'].lower()=="no"):
   HockeyLeagueHasConferences = False;
  if(verbose):
   VerbosePrintOut(pyfilename+".MakeHockeyTeamTable(sqldatacon, \""+hlkey+"\");\n"+pyfilename+".MakeHockeyConferenceTable(sqldatacon, \""+hlkey+"\");\n"+pyfilename+".MakeHockeyGameTable(sqldatacon, \""+hlkey+"\");\n"+pyfilename+".MakeHockeyDivisionTable(sqldatacon, \""+hlkey+"\");\n"+pyfilename+".MakeHockeyLeague(sqldatacon, \""+hlkey+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullname']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['country']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullcountry']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['date']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['playofffmt']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['ordertype']+"\");");
  pystring = pystring+pyfilename+".MakeHockeyTeamTable(sqldatacon, \""+hlkey+"\");\n"+pyfilename+".MakeHockeyConferenceTable(sqldatacon, \""+hlkey+"\");\n"+pyfilename+".MakeHockeyGameTable(sqldatacon, \""+hlkey+"\");\n"+pyfilename+".MakeHockeyDivisionTable(sqldatacon, \""+hlkey+"\");\n"+pyfilename+".MakeHockeyLeague(sqldatacon, \""+hlkey+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullname']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['country']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullcountry']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['date']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['playofffmt']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['ordertype']+"\");\n";
  conferencecount = 0;
  conferenceend = len(inhockeyarray[hlkey]['conferencelist']);
  for hckey in inhockeyarray[hlkey]['conferencelist']:
   if(verbose):
    VerbosePrintOut(pyfilename+".MakeHockeyConference(sqldatacon, \""+hlkey+"\", \""+hckey+"\", \""+inhockeyarray[hlkey][hckey]['conferenceinfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey]['conferenceinfo']['suffix']+"\", "+str(HockeyLeagueHasConferences)+");");
   pystring = pystring+pyfilename+".MakeHockeyConference(sqldatacon, \""+hlkey+"\", \""+hckey+"\", \""+inhockeyarray[hlkey][hckey]['conferenceinfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey]['conferenceinfo']['suffix']+"\", "+str(HockeyLeagueHasConferences)+");\n";
   for hdkey in inhockeyarray[hlkey][hckey]['divisionlist']:
    if(verbose):
     VerbosePrintOut(pyfilename+".MakeHockeyDivision(sqldatacon, \""+hlkey+"\", \""+hdkey+"\", \""+hckey+"\", \""+inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");");
    pystring = pystring+pyfilename+".MakeHockeyDivision(sqldatacon, \""+hlkey+"\", \""+hdkey+"\", \""+hckey+"\", \""+inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");\n";
    for htkey in inhockeyarray[hlkey][hckey][hdkey]['teamlist']:
     if(verbose):
      VerbosePrintOut(pyfilename+".MakeHockeyTeam(sqldatacon, \""+hlkey+"\", \""+str(inhockeyarray[hlkey]['leagueinfo']['date'])+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']+"\", \""+htkey+"\", \""+hckey+"\", \""+hdkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");");
     pystring = pystring+pyfilename+".MakeHockeyTeam(sqldatacon, \""+hlkey+"\", \""+str(inhockeyarray[hlkey]['leagueinfo']['date'])+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']+"\", \""+htkey+"\", \""+hckey+"\", \""+hdkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");\n";
   conferencecount = conferencecount + 1;
  if(conferencecount>=conferenceend):
   hasarenas = False;
   if(len(inhockeyarray[hlkey]['arenas'])>0):
    hasarenas = True;
   for hakey in inhockeyarray[hlkey]['arenas']:
    if(hakey):
     hasarenas = True;
     if(verbose):
      VerbosePrintOut(pyfilename+".MakeHockeyArena(sqldatacon, \""+hlkey+"\", \""+hakey['city']+"\", \""+hakey['area']+"\", \""+hakey['country']+"\", \""+hakey['fullcountry']+"\", \""+hakey['fullarea']+"\", \""+hakey['name']+"\");");
     pystring = pystring+pyfilename+".MakeHockeyArena(sqldatacon, \""+hlkey+"\", \""+hakey['city']+"\", \""+hakey['area']+"\", \""+hakey['country']+"\", \""+hakey['fullcountry']+"\", \""+hakey['fullarea']+"\", \""+hakey['name']+"\");\n";
   hasgames = False;
   if(len(inhockeyarray[hlkey]['games'])>0):
    hasgames = True;
   for hgkey in inhockeyarray[hlkey]['games']:
    if(hgkey):
     hasgames = True;
     if(verbose):
      VerbosePrintOut(pyfilename+".MakeHockeyGame(sqldatacon, \""+hlkey+"\", "+hgkey['date']+", \""+hgkey['hometeam']+"\", \""+hgkey['awayteam']+"\", \""+hgkey['goals']+"\", \""+hgkey['sogs']+"\", \""+hgkey['ppgs']+"\", \""+hgkey['shgs']+"\", \""+hgkey['penalties']+"\", \""+hgkey['pims']+"\", \""+hgkey['hits']+"\", \""+hgkey['takeaways']+"\", \""+hgkey['faceoffwins']+"\", \""+hgkey['atarena']+"\", \""+hgkey['isplayoffgame']+"\");");
     pystring = pystring+pyfilename+".MakeHockeyGame(sqldatacon, \""+hlkey+"\", "+hgkey['date']+", \""+hgkey['hometeam']+"\", \""+hgkey['awayteam']+"\", \""+hgkey['goals']+"\", \""+hgkey['sogs']+"\", \""+hgkey['ppgs']+"\", \""+hgkey['shgs']+"\", \""+hgkey['penalties']+"\", \""+hgkey['pims']+"\", \""+hgkey['hits']+"\", \""+hgkey['takeaways']+"\", \""+hgkey['faceoffwins']+"\", \""+hgkey['atarena']+"\", \""+hgkey['isplayoffgame']+"\");\n";
 if(verbose):
  VerbosePrintOut(" ");
 pystring = pystring+"\n";
 if(verbose):
  VerbosePrintOut(pyfilename+".CloseHockeyDatabase(sqldatacon);");
 pystring = pystring+pyfilename+".CloseHockeyDatabase(sqldatacon);\n";
 return pystring;

def MakeHockeyPythonFileFromHockeyArray(inhockeyarray, outpyfile=None, returnpy=False, verbose=True):
 if(outpyfile is None):
  return False;
 pyfp = open(outpyfile, "w+");
 pystring = MakeHockeyPythonFromHockeyArray(inhockeyarray, verbose);
 pyfp.write(pystring);
 pyfp.close();
 os.chmod(outpyfile, 0o755);
 if(returnpy):
  return pystring;
 if(not returnpy):
  return True;
 return True;

def MakeHockeyPythonAltFromHockeyArray(inhockeyarray, verbose=True, verbosepy=True):
 if(not CheckHockeyArray(inhockeyarray)):
  return False;
 pyfilename = __package__;
 if(pyfilename=="__main__"):
  pyfilename = os.path.splitext(os.path.basename(__file__))[0];
 if(verbose):
  VerbosePrintOut("#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nfrom __future__ import absolute_import, division, print_function, unicode_literals;\nimport "+pyfilename+";\n");
 pystring = "#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nfrom __future__ import absolute_import, division, print_function, unicode_literals;\nimport "+pyfilename+";\n\n";
 if(verbose):
  VerbosePrintOut("hockeyarray = "+pyfilename+".CreateHockeyArray(\""+inhockeyarray['database']+"\");");
 pystring = pystring+"hockeyarray = "+pyfilename+".CreateHockeyArray(\""+inhockeyarray['database']+"\");\n";
 for hlkey in inhockeyarray['leaguelist']:
  HockeyLeagueHasDivisions = True;
  if(inhockeyarray[hlkey]['leagueinfo']['conferences'].lower()=="no"):
   HockeyLeagueHasDivisions = False;
  HockeyLeagueHasConferences = True;
  if(inhockeyarray[hlkey]['leagueinfo']['divisions'].lower()=="no"):
   HockeyLeagueHasConferences = False;
  if(verbose):
   VerbosePrintOut("hockeyarray = "+pyfilename+".AddHockeyLeagueToArray(hockeyarray, \""+hlkey+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullname']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['country']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullcountry']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['date']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['playofffmt']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['ordertype']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");");
  pystring = pystring+"hockeyarray = "+pyfilename+".AddHockeyLeagueToArray(hockeyarray, \""+hlkey+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullname']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['country']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullcountry']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['date']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['playofffmt']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['ordertype']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");\n";
  conferencecount = 0;
  conferenceend = len(inhockeyarray[hlkey]['conferencelist']);
  for hckey in inhockeyarray[hlkey]['conferencelist']:
   if(verbose):
    VerbosePrintOut("hockeyarray = "+pyfilename+".AddHockeyConferenceToArray(hockeyarray, \""+hlkey+"\", \""+hckey+"\", \""+inhockeyarray[hlkey][hckey]['conferenceinfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey]['conferenceinfo']['suffix']+"\");");
   pystring = pystring+"hockeyarray = "+pyfilename+".AddHockeyConferenceToArray(hockeyarray, \""+hlkey+"\", \""+hckey+"\");\n";
   for hdkey in inhockeyarray[hlkey][hckey]['divisionlist']:
    if(verbose):
     VerbosePrintOut("hockeyarray = "+pyfilename+".AddHockeyDivisionToArray(hockeyarray, \""+hlkey+"\", \""+hdkey+"\", \""+hckey+"\", \""+inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix']+"\");");
    pystring = pystring+"hockeyarray = "+pyfilename+".AddHockeyDivisionToArray(hockeyarray, \""+hlkey+"\", \""+hdkey+"\", \""+hckey+"\", \""+inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix']+"\");\n";
    for htkey in inhockeyarray[hlkey][hckey][hdkey]['teamlist']:
     if(verbose):
      VerbosePrintOut("hockeyarray = "+pyfilename+".AddHockeyTeamToArray(hockeyarray, \""+hlkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']+"\", \""+htkey+"\", \""+hckey+"\", \""+hdkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']+"\");");
     pystring = pystring+"hockeyarray = "+pyfilename+".AddHockeyTeamToArray(hockeyarray, \""+hlkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']+"\", \""+htkey+"\", \""+hckey+"\", \""+hdkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']+"\");\n";
   conferencecount = conferencecount + 1;
  if(conferencecount>=conferenceend):
   hasarenas = False;
   if(len(inhockeyarray[hlkey]['arenas'])>0):
    hasarenas = True;
   for hakey in inhockeyarray[hlkey]['arenas']:
    if(hakey):
     hasarenas = True;
     if(verbose):
      VerbosePrintOut("hockeyarray = "+pyfilename+".AddHockeyArenaToArray(hockeyarray, \""+hlkey+"\", \""+hakey['city']+"\", \""+hakey['area']+"\", \""+hakey['country']+"\", \""+hakey['fullcountry']+"\", \""+hakey['fullarea']+"\", \""+hakey['name']+"\");");
     pystring = pystring+"hockeyarray = "+pyfilename+".AddHockeyArenaToArray(hockeyarray, \""+hlkey+"\", \""+hakey['city']+"\", \""+hakey['area']+"\", \""+hakey['country']+"\", \""+hakey['fullcountry']+"\", \""+hakey['fullarea']+"\", \""+hakey['name']+"\");\n";
   hasgames = False;
   if(len(inhockeyarray[hlkey]['games'])>0):
    hasgames = True;
   for hgkey in inhockeyarray[hlkey]['games']:
    if(hgkey):
     hasgames = True;
     if(verbose):
      VerbosePrintOut("hockeyarray = "+pyfilename+".AddHockeyGameToArray(hockeyarray, \""+hlkey+"\", "+hgkey['date']+", \""+hgkey['hometeam']+"\", \""+hgkey['awayteam']+"\", \""+hgkey['goals']+"\", \""+hgkey['sogs']+"\", \""+hgkey['ppgs']+"\", \""+hgkey['shgs']+"\", \""+hgkey['penalties']+"\", \""+hgkey['pims']+"\", \""+hgkey['hits']+"\", \""+hgkey['takeaways']+"\", \""+hgkey['faceoffwins']+"\", \""+hgkey['atarena']+"\", \""+hgkey['isplayoffgame']+"\");");
     pystring = pystring+"hockeyarray = "+pyfilename+".AddHockeyGameToArray(hockeyarray, \""+hlkey+"\", "+hgkey['date']+", \""+hgkey['hometeam']+"\", \""+hgkey['awayteam']+"\", \""+hgkey['goals']+"\", \""+hgkey['sogs']+"\", \""+hgkey['ppgs']+"\", \""+hgkey['shgs']+"\", \""+hgkey['penalties']+"\", \""+hgkey['pims']+"\", \""+hgkey['hits']+"\", \""+hgkey['takeaways']+"\", \""+hgkey['faceoffwins']+"\", \""+hgkey['atarena']+"\", \""+hgkey['isplayoffgame']+"\");\n";
 if(verbose):
  VerbosePrintOut(" ");
 pystring = pystring+"\n";
 if(verbosepy):
  pyverbose = "True";
 elif(not verbosepy):
  pyverbose = "False";
 else:
  pyverbose = "False";
 if(verbose):
  VerbosePrintOut(pyfilename+".MakeHockeyDatabaseFromHockeyArray(hockeyarray, None, False, False, "+pyverbose+");");
 pystring = pystring+pyfilename+".MakeHockeyDatabaseFromHockeyArray(hockeyarray, None, False, False, "+pyverbose+");\n";
 return pystring;

def MakeHockeyPythonAltFileFromHockeyArray(inhockeyarray, outpyfile=None, returnpy=False, verbose=True, verbosepy=True):
 if(outpyfile is None):
  return False;
 pyfp = open(outpyfile, "w+");
 pystring = MakeHockeyPythonAltFromHockeyArray(inhockeyarray, verbose, verbosepy);
 pyfp.write(pystring);
 pyfp.close();
 os.chmod(outpyfile, 0o755);
 if(returnpy):
  return pystring;
 if(not returnpy):
  return True;
 return True;

def MakeHockeyPythonOOPFromHockeyArray(inhockeyarray, verbose=True):
 if(not CheckHockeyArray(inhockeyarray)):
  return False;
 pyfilename = __package__;
 if(pyfilename=="__main__"):
  pyfilename = os.path.splitext(os.path.basename(__file__))[0];
 if(verbose):
  VerbosePrintOut("#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nfrom __future__ import absolute_import, division, print_function, unicode_literals;\nimport "+pyfilename+";\n");
 pystring = "#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nfrom __future__ import absolute_import, division, print_function, unicode_literals;\nimport "+pyfilename+";\n\n";
 if(verbose):
  VerbosePrintOut("sqldatacon = "+pyfilename+".MakeHockeyClass(\""+inhockeyarray['database']+"\");");
 pystring = pystring+"sqldatacon = "+pyfilename+".MakeHockeyClass(\""+inhockeyarray['database']+"\");\n";
 if(verbose):
  VerbosePrintOut("sqldatacon.MakeHockeyLeagueTable(sqldatacon);");
 pystring = pystring+"sqldatacon.MakeHockeyLeagueTable(sqldatacon);\n";
 for hlkey in inhockeyarray['leaguelist']:
  HockeyLeagueHasDivisions = True;
  if(inhockeyarray[hlkey]['leagueinfo']['conferences'].lower()=="no"):
   HockeyLeagueHasDivisions = False;
  HockeyLeagueHasConferences = True;
  if(inhockeyarray[hlkey]['leagueinfo']['divisions'].lower()=="no"):
   HockeyLeagueHasConferences = False;
  if(verbose):
   VerbosePrintOut("sqldatacon.MakeHockeyTeamTable(sqldatacon, \""+hlkey+"\");\n"+"sqldatacon.MakeHockeyConferenceTable(sqldatacon, \""+hlkey+"\");\n"+"sqldatacon.MakeHockeyGameTable(sqldatacon, \""+hlkey+"\");\n"+"sqldatacon.MakeHockeyDivisionTable(sqldatacon, \""+hlkey+"\");\n"+"sqldatacon.AddHockeyLeague(sqldatacon, \""+hlkey+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullname']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['country']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullcountry']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['date']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['playofffmt']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['ordertype']+"\");");
  pystring = pystring+"sqldatacon.MakeHockeyTeamTable(sqldatacon, \""+hlkey+"\");\n"+"sqldatacon.MakeHockeyConferenceTable(sqldatacon, \""+hlkey+"\");\n"+"sqldatacon.MakeHockeyGameTable(sqldatacon, \""+hlkey+"\");\n"+"sqldatacon.MakeHockeyDivisionTable(sqldatacon, \""+hlkey+"\");\n"+"sqldatacon.AddHockeyLeague(sqldatacon, \""+hlkey+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullname']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['country']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullcountry']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['date']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['playofffmt']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['ordertype']+"\");\n";
  conferencecount = 0;
  conferenceend = len(inhockeyarray[hlkey]['conferencelist']);
  for hckey in inhockeyarray[hlkey]['conferencelist']:
   if(verbose):
    VerbosePrintOut("sqldatacon.AddHockeyConference(sqldatacon, \""+hlkey+"\", \""+hckey+"\", \""+inhockeyarray[hlkey][hckey]['conferenceinfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey]['conferenceinfo']['suffix']+"\", "+str(HockeyLeagueHasConferences)+");");
   pystring = pystring+"sqldatacon.AddHockeyConference(sqldatacon, \""+hlkey+"\", \""+hckey+"\", \""+inhockeyarray[hlkey][hckey]['conferenceinfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey]['conferenceinfo']['suffix']+"\", "+str(HockeyLeagueHasConferences)+");\n";
   for hdkey in inhockeyarray[hlkey][hckey]['divisionlist']:
    if(verbose):
     VerbosePrintOut("sqldatacon.AddHockeyDivision(sqldatacon, \""+hlkey+"\", \""+hdkey+"\", \""+hckey+"\", \""+inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");");
    pystring = pystring+"sqldatacon.AddHockeyDivision(sqldatacon, \""+hlkey+"\", \""+hdkey+"\", \""+hckey+"\", \""+inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");\n";
    for htkey in inhockeyarray[hlkey][hckey][hdkey]['teamlist']:
     if(verbose):
      VerbosePrintOut("sqldatacon.AddHockeyTeam(sqldatacon, \""+hlkey+"\", \""+str(inhockeyarray[hlkey]['leagueinfo']['date'])+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']+"\", \""+htkey+"\", \""+hckey+"\", \""+hdkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");");
     pystring = pystring+"sqldatacon.AddHockeyTeam(sqldatacon, \""+hlkey+"\", \""+str(inhockeyarray[hlkey]['leagueinfo']['date'])+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']+"\", \""+htkey+"\", \""+hckey+"\", \""+hdkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");\n";
   conferencecount = conferencecount + 1;
  if(conferencecount>=conferenceend):
   hasarenas = False;
   if(len(inhockeyarray[hlkey]['arenas'])>0):
    hasarenas = True;
   for hakey in inhockeyarray[hlkey]['arenas']:
    if(hakey):
     hasarenas = True;
     if(verbose):
      VerbosePrintOut("sqldatacon.AddHockeyArena(sqldatacon, \""+hlkey+"\", \""+hakey['city']+"\", \""+hakey['area']+"\", \""+hakey['country']+"\", \""+hakey['fullcountry']+"\", \""+hakey['fullarea']+"\", \""+hakey['name']+"\");");
     pystring = pystring+"sqldatacon.AddHockeyArena(sqldatacon, \""+hlkey+"\", \""+hakey['city']+"\", \""+hakey['area']+"\", \""+hakey['country']+"\", \""+hakey['fullcountry']+"\", \""+hakey['fullarea']+"\", \""+hakey['name']+"\");\n";
   hasgames = False;
   if(len(inhockeyarray[hlkey]['games'])>0):
    hasgames = True;
   for hgkey in inhockeyarray[hlkey]['games']:
    if(hgkey):
     hasgames = True;
     if(verbose):
      VerbosePrintOut("sqldatacon.AddHockeyGame(sqldatacon, \""+hlkey+"\", "+hgkey['date']+", \""+hgkey['hometeam']+"\", \""+hgkey['awayteam']+"\", \""+hgkey['goals']+"\", \""+hgkey['sogs']+"\", \""+hgkey['ppgs']+"\", \""+hgkey['shgs']+"\", \""+hgkey['penalties']+"\", \""+hgkey['pims']+"\", \""+hgkey['hits']+"\", \""+hgkey['takeaways']+"\", \""+hgkey['faceoffwins']+"\", \""+hgkey['atarena']+"\", \""+hgkey['isplayoffgame']+"\");");
     pystring = pystring+"sqldatacon.AddHockeyGame(sqldatacon, \""+hlkey+"\", "+hgkey['date']+", \""+hgkey['hometeam']+"\", \""+hgkey['awayteam']+"\", \""+hgkey['goals']+"\", \""+hgkey['sogs']+"\", \""+hgkey['ppgs']+"\", \""+hgkey['shgs']+"\", \""+hgkey['penalties']+"\", \""+hgkey['pims']+"\", \""+hgkey['hits']+"\", \""+hgkey['takeaways']+"\", \""+hgkey['faceoffwins']+"\", \""+hgkey['atarena']+"\", \""+hgkey['isplayoffgame']+"\");\n";
 if(verbose):
  VerbosePrintOut(" ");
 pystring = pystring+"\n";
 if(verbose):
  VerbosePrintOut("sqldatacon.CloseHockeyDatabase(sqldatacon);");
 pystring = pystring+"sqldatacon.CloseHockeyDatabase(sqldatacon);\n";
 return pystring;

def MakeHockeyPythonOOPFileFromHockeyArray(inhockeyarray, outpyfile=None, returnpy=False, verbose=True):
 if(outpyfile is None):
  return False;
 pyfp = open(outpyfile, "w+");
 pystring = MakeHockeyPythonOOPFromHockeyArray(inhockeyarray, verbose);
 pyfp.write(pystring);
 pyfp.close();
 os.chmod(outpyfile, 0o755);
 if(returnpy):
  return pystring;
 if(not returnpy):
  return True;
 return True;

def MakeHockeyPythonOOPAltFromHockeyArray(inhockeyarray, verbose=True, verbosepy=True):
 if(not CheckHockeyArray(inhockeyarray)):
  return False;
 pyfilename = __package__;
 if(pyfilename=="__main__"):
  pyfilename = os.path.splitext(os.path.basename(__file__))[0];
 if(verbose):
  VerbosePrintOut("#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nfrom __future__ import absolute_import, division, print_function, unicode_literals;\nimport "+pyfilename+";\n");
 pystring = "#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nfrom __future__ import absolute_import, division, print_function, unicode_literals;\nimport "+pyfilename+";\n\n";
 if(verbose):
  VerbosePrintOut("hockeyarray = "+pyfilename+".MakeHockeyArray(\""+inhockeyarray['database']+"\");");
 pystring = pystring+"hockeyarray = "+pyfilename+".MakeHockeyArray(\""+inhockeyarray['database']+"\");\n";
 for hlkey in inhockeyarray['leaguelist']:
  HockeyLeagueHasDivisions = True;
  if(inhockeyarray[hlkey]['leagueinfo']['conferences'].lower()=="no"):
   HockeyLeagueHasDivisions = False;
  HockeyLeagueHasConferences = True;
  if(inhockeyarray[hlkey]['leagueinfo']['divisions'].lower()=="no"):
   HockeyLeagueHasConferences = False;
  if(verbose):
   VerbosePrintOut("hockeyarray = hockeyarray.AddHockeyLeague(\""+hlkey+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullname']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['country']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullcountry']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['date']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['playofffmt']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['ordertype']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");");
  pystring = pystring+"hockeyarray = hockeyarray.AddHockeyLeague(\""+hlkey+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullname']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['country']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullcountry']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['date']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['playofffmt']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['ordertype']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");\n";
  conferencecount = 0;
  conferenceend = len(inhockeyarray[hlkey]['conferencelist']);
  for hckey in inhockeyarray[hlkey]['conferencelist']:
   if(verbose):
    VerbosePrintOut("hockeyarray = hockeyarray.AddHockeyConference(\""+hlkey+"\", \""+hckey+"\", \""+inhockeyarray[hlkey][hckey]['conferenceinfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey]['conferenceinfo']['suffix']+"\");");
   pystring = pystring+"hockeyarray = hockeyarray.AddHockeyConference(\""+hlkey+"\", \""+hckey+"\", \""+inhockeyarray[hlkey][hckey]['conferenceinfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey]['conferenceinfo']['suffix']+"\");\n";
   for hdkey in inhockeyarray[hlkey][hckey]['divisionlist']:
    if(verbose):
     VerbosePrintOut("hockeyarray = hockeyarray.AddHockeyDivision(\""+hlkey+"\", \""+hdkey+"\", \""+hckey+"\", \""+inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix']+"\");");
    pystring = pystring+"hockeyarray = hockeyarray.AddHockeyDivision(\""+hlkey+"\", \""+hdkey+"\", \""+hckey+"\", \""+inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix']+"\");\n";
    for htkey in inhockeyarray[hlkey][hckey][hdkey]['teamlist']:
     if(verbose):
      VerbosePrintOut("hockeyarray = hockeyarray.AddHockeyTeam(\""+hlkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']+"\", \""+htkey+"\", \""+hckey+"\", \""+hdkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']+"\");");
     pystring = pystring+"hockeyarray = hockeyarray.AddHockeyTeam(\""+hlkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']+"\", \""+htkey+"\", \""+hckey+"\", \""+hdkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']+"\");\n";
   conferencecount = conferencecount + 1;
  if(conferencecount>=conferenceend):
   hasarenas = False;
   if(len(inhockeyarray[hlkey]['arenas'])>0):
    hasarenas = True;
   for hakey in inhockeyarray[hlkey]['arenas']:
    if(hakey):
     hasarenas = True;
     if(verbose):
      VerbosePrintOut("hockeyarray = hockeyarray.AddHockeyArena(\""+hlkey+"\", \""+hakey['city']+"\", \""+hakey['area']+"\", \""+hakey['country']+"\", \""+hakey['fullcountry']+"\", \""+hakey['fullarea']+"\", \""+hakey['name']+"\");");
     pystring = pystring+"hockeyarray = hockeyarray.AddHockeyArena(\""+hlkey+"\", \""+hakey['city']+"\", \""+hakey['area']+"\", \""+hakey['country']+"\", \""+hakey['fullcountry']+"\", \""+hakey['fullarea']+"\", \""+hakey['name']+"\");\n";
   hasgames = False;
   if(len(inhockeyarray[hlkey]['games'])>0):
    hasgames = True;
   for hgkey in inhockeyarray[hlkey]['games']:
    if(hgkey):
     hasgames = True;
     if(verbose):
      VerbosePrintOut("hockeyarray = hockeyarray.AddHockeyGame(\""+hlkey+"\", "+hgkey['date']+", \""+hgkey['hometeam']+"\", \""+hgkey['awayteam']+"\", \""+hgkey['goals']+"\", \""+hgkey['sogs']+"\", \""+hgkey['ppgs']+"\", \""+hgkey['shgs']+"\", \""+hgkey['penalties']+"\", \""+hgkey['pims']+"\", \""+hgkey['hits']+"\", \""+hgkey['takeaways']+"\", \""+hgkey['faceoffwins']+"\", \""+hgkey['atarena']+"\", \""+hgkey['isplayoffgame']+"\");");
     pystring = pystring+"hockeyarray = hockeyarray.AddHockeyGame(\""+hlkey+"\", "+hgkey['date']+", \""+hgkey['hometeam']+"\", \""+hgkey['awayteam']+"\", \""+hgkey['goals']+"\", \""+hgkey['sogs']+"\", \""+hgkey['ppgs']+"\", \""+hgkey['shgs']+"\", \""+hgkey['penalties']+"\", \""+hgkey['pims']+"\", \""+hgkey['hits']+"\", \""+hgkey['takeaways']+"\", \""+hgkey['faceoffwins']+"\", \""+hgkey['atarena']+"\", \""+hgkey['isplayoffgame']+"\");\n";
 if(verbose):
  VerbosePrintOut(" ");
 pystring = pystring+"\n";
 if(verbosepy):
  pyverbose = "True";
 elif(not verbosepy):
  pyverbose = "False";
 else:
  pyverbose = "False";
 if(verbose):
  VerbosePrintOut("hockeyarray.MakeHockeyDatabase(None, False, False, "+pyverbose+");");
 pystring = pystring+"hockeyarray.MakeHockeyDatabase(None, False, False, "+pyverbose+");\n";
 return pystring;

def MakeHockeyPythonOOPAltFileFromHockeyArray(inhockeyarray, outpyfile=None, returnpy=False, verbose=True, verbosepy=True):
 if(outpyfile is None):
  return False;
 pyfp = open(outpyfile, "w+");
 pystring = MakeHockeyPythonOOPAltFromHockeyArray(inhockeyarray, verbose, verbosepy);
 pyfp.write(pystring);
 pyfp.close();
 os.chmod(outpyfile, 0o755);
 if(returnpy):
  return pystring;
 if(not returnpy):
  return True;
 return True;

def MakeHockeyArrayFromHockeyDatabase(sdbfile, verbose=True):
 if(os.path.exists(sdbfile) and os.path.isfile(sdbfile) and isinstance(sdbfile, basestring)):
  if(not CheckHockeySQLiteDatabase(sdbfile)[0]):
   return False;
  sqldatacon = OpenHockeyDatabase(sdbfile);
 else:
  if(sdbfile is not None and isinstance(sdbfile, (tuple, list))):
   sqldatacon = tuple(sdbfile);
  else:
   return False;
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 leaguecur = sqldatacon[1].cursor();
 if(verbose):
  VerbosePrintOut("<?xml version=\"1.0\" encoding=\"UTF-8\"?>");
  VerbosePrintOut("<hockey database=\""+EscapeXMLString(str(sdbfile), quote=True)+"\">");
 getleague_num = leaguecur.execute("SELECT COUNT(*) FROM HockeyLeagues").fetchone()[0];
 getleague = leaguecur.execute("SELECT LeagueName, LeagueFullName, CountryName, FullCountryName, Date, PlayOffFMT, OrderType, NumberOfConferences, NumberOfDivisions FROM HockeyLeagues");
 leaguearrayout = { 'database': str(sdbfile) };
 leaguelist = [];
 for leagueinfo in getleague:
  leaguearray = {};
  arenalist = [];
  gamelist = [];
  HockeyLeagueHasConferences = True;
  HockeyLeagueHasConferenceStr = "yes";
  if(int(leagueinfo[7])<=0):
   HockeyLeagueHasConferences = False;
   HockeyLeagueHasConferenceStr = "no";
  HockeyLeagueHasDivisions = True;
  HockeyLeagueHasDivisionStr = "yes";
  if(int(leagueinfo[8])<=0):
   HockeyLeagueHasDivisions = False;
   HockeyLeagueHasDivisionStr = "no";
  tempdict = { 'leagueinfo': { 'name': str(leagueinfo[0]), 'fullname': str(leagueinfo[1]), 'country': str(leagueinfo[2]), 'fullcountry': str(leagueinfo[3]), 'date': str(leagueinfo[4]), 'playofffmt': str(leagueinfo[5]), 'ordertype': str(leagueinfo[6]), 'conferences': str(HockeyLeagueHasConferenceStr), 'divisions': str(HockeyLeagueHasDivisionStr) }, 'quickinfo': {'conferenceinfo': {}, 'divisioninfo': {}, 'teaminfo': {} } };
  leaguearray.update( { str(leagueinfo[0]): tempdict } );
  leaguelist.append(str(leagueinfo[0]));
  if(verbose):
   VerbosePrintOut(" <league name=\""+EscapeXMLString(str(leagueinfo[0]), quote=True)+"\" fullname=\""+EscapeXMLString(str(leagueinfo[1]), quote=True)+"\" country=\""+EscapeXMLString(str(leagueinfo[2]), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(leagueinfo[3]), quote=True)+"\" date=\""+EscapeXMLString(str(leagueinfo[4]), quote=True)+"\" playofffmt=\""+EscapeXMLString(str(leagueinfo[5]), quote=True)+"\" ordertype=\""+EscapeXMLString(str(leagueinfo[6]), quote=True)+"\" conferences=\""+EscapeXMLString(str(HockeyLeagueHasConferenceStr), quote=True)+"\" divisions=\""+EscapeXMLString(str(HockeyLeagueHasDivisionStr), quote=True)+"\">");
  conferencecur = sqldatacon[1].cursor();
  getconference_num = conferencecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Conferences WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\"").fetchone()[0];
  getconference = conferencecur.execute("SELECT Conference, ConferencePrefix, ConferenceSuffix, FullName FROM "+leagueinfo[0]+"Conferences WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\"");
  conferencelist = [];
  for conferenceinfo in getconference:
   leaguearray[str(leagueinfo[0])].update( { str(conferenceinfo[0]): { 'conferenceinfo': { 'name': str(conferenceinfo[0]), 'prefix': str(conferenceinfo[1]), 'suffix': str(conferenceinfo[2]), 'fullname': str(conferenceinfo[3]), 'league': str(leagueinfo[0]) } } } );
   leaguearray[str(leagueinfo[0])]['quickinfo']['conferenceinfo'].update( { str(conferenceinfo[0]): { 'name': str(conferenceinfo[0]), 'fullname': str(conferenceinfo[3]), 'league': str(leagueinfo[0]) } } );
   conferencelist.append(str(conferenceinfo[0]));
   if(verbose):
    VerbosePrintOut("  <conference name=\""+str(conferenceinfo[0])+"\" prefix=\""+EscapeXMLString(str(conferenceinfo[1]), quote=True)+"\" suffix=\""+EscapeXMLString(str(conferenceinfo[2]), quote=True)+"\">");
   divisioncur = sqldatacon[1].cursor();
   getdivision_num = divisioncur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Divisions WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\"").fetchone()[0];
   getdivision = divisioncur.execute("SELECT Division, DivisionPrefix, DivisionSuffix, FullName FROM "+leagueinfo[0]+"Divisions WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\"");
   divisionlist = [];
   for divisioninfo in getdivision:
    leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update( { str(divisioninfo[0]): { 'divisioninfo': { 'name': str(divisioninfo[0]), 'prefix': str(divisioninfo[1]), 'suffix': str(divisioninfo[2]), 'fullname': str(divisioninfo[3]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]) } } } );
    leaguearray[str(leagueinfo[0])]['quickinfo']['divisioninfo'].update( { str(divisioninfo[0]): { 'name': str(divisioninfo[0]), 'fullname': str(divisioninfo[3]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]) } } );
    divisionlist.append(str(divisioninfo[0]));
    if(verbose):
     VerbosePrintOut("   <division name=\""+EscapeXMLString(str(divisioninfo[0]), quote=True)+"\" prefix=\""+EscapeXMLString(str(divisioninfo[1]), quote=True)+"\" suffix=\""+EscapeXMLString(str(divisioninfo[2]), quote=True)+"\">");
    teamcur = sqldatacon[1].cursor();
    getteam_num = teamcur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Teams WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"").fetchone()[0];
    getteam = teamcur.execute("SELECT CityName, AreaName, FullAreaName, CountryName, FullCountryName, TeamName, ArenaName, TeamPrefix, TeamSuffix FROM "+leagueinfo[0]+"Teams WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"");
    teamlist = [];
    for teaminfo in getteam:
     fullteamname = GetFullTeamName(str(teaminfo[5]), str(teaminfo[7]), str(teaminfo[8]));
     leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(divisioninfo[0])].update( { str(teaminfo[5]): { 'teaminfo': { 'city': str(teaminfo[0]), 'area': str(teaminfo[1]), 'fullarea': str(teaminfo[2]), 'country': str(teaminfo[3]), 'fullcountry': str(teaminfo[4]), 'name': str(teaminfo[5]), 'fullname': fullteamname, 'arena': str(teaminfo[6]), 'prefix': str(teaminfo[7]), 'suffix': str(teaminfo[8]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0]) } } } );
     leaguearray[str(leagueinfo[0])]['quickinfo']['teaminfo'].update( { str(teaminfo[5]): { 'name': str(teaminfo[5]), 'fullname': fullteamname, 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0]) } } );
     teamlist.append(str(teaminfo[5]));
     if(verbose):
      VerbosePrintOut("    <team city=\""+EscapeXMLString(str(teaminfo[0]), quote=True)+"\" area=\""+EscapeXMLString(str(teaminfo[1]), quote=True)+"\" fullarea=\""+EscapeXMLString(str(teaminfo[2]), quote=True)+"\" country=\""+EscapeXMLString(str(teaminfo[3]), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(teaminfo[4]), quote=True)+"\" name=\""+EscapeXMLString(str(teaminfo[5]), quote=True)+"\" arena=\""+EscapeXMLString(str(teaminfo[6]), quote=True)+"\" prefix=\""+EscapeXMLString(str(teaminfo[7]), quote=True)+"\" suffix=\""+EscapeXMLString(str(teaminfo[8]), quote=True)+"\" />");
    teamcur.close();
    leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(divisioninfo[0])].update( { 'teamlist': teamlist } );
    if(verbose):
     VerbosePrintOut("   </division>");
   divisioncur.close();
   leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update( { 'divisionlist': divisionlist } );
   if(verbose):
    VerbosePrintOut("  </conference>");
  conferencecur.close();
  leaguearray[str(leagueinfo[0])].update( { 'conferencelist': conferencelist } );
  arenacur = sqldatacon[1].cursor();
  getteam_num = arenacur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Arenas WHERE TeamID=0").fetchone()[0];
  getarena = arenacur.execute("SELECT CityName, AreaName, FullAreaName, CountryName, FullCountryName, ArenaName FROM "+leagueinfo[0]+"Arenas WHERE TeamID=0");
  if(getteam_num>0):
   for arenainfo in getarena:
    if(verbose):
     VerbosePrintOut("   <arena city=\""+EscapeXMLString(str(arenainfo[0]), quote=True)+"\" area=\""+EscapeXMLString(str(arenainfo[1]), quote=True)+"\" fullarea=\""+EscapeXMLString(str(arenainfo[2]), quote=True)+"\" country=\""+EscapeXMLString(str(arenainfo[3]), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(arenainfo[4]), quote=True)+"\" name=\""+EscapeXMLString(str(arenainfo[5]), quote=True)+"\" />");
    arenalist.append( { 'city': str(arenainfo[0]), 'area': str(arenainfo[1]), 'fullarea': str(arenainfo[2]), 'country': str(arenainfo[3]), 'fullcountry': str(arenainfo[4]), 'name': str(arenainfo[5]) } );
    if(verbose):
     VerbosePrintOut("   <arena city=\""+EscapeXMLString(str(arenainfo[0]), quote=True)+"\" area=\""+EscapeXMLString(str(arenainfo[1]), quote=True)+"\" fullarea=\""+EscapeXMLString(str(arenainfo[2]), quote=True)+"\" country=\""+EscapeXMLString(str(arenainfo[3]), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(arenainfo[4]), quote=True)+"\" name=\""+EscapeXMLString(str(arenainfo[5]), quote=True)+"\" />");
   if(verbose):
    VerbosePrintOut("  </arenas>");
  leaguearray[str(leagueinfo[0])].update( { "arenas": arenalist } );
  gamecur = sqldatacon[1].cursor();
  getgame_num = gamecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Games").fetchone()[0];
  getgame = gamecur.execute("SELECT Date, HomeTeam, AwayTeam, TeamScorePeriods, ShotsOnGoal, PowerPlays, ShortHanded, Penalties, PenaltyMinutes, HitsPerPeriod, TakeAways, FaceoffWins, AtArena, IsPlayOffGame FROM "+leagueinfo[0]+"Games");
  if(getgame_num>0):
   if(verbose):
    VerbosePrintOut("  <games>");
   for gameinfo in getgame:
    AtArena = gameinfo[12];
    if(GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[1]), "FullArenaName", "str")==AtArena):
     AtArena = "0";
    if(GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[2]), "FullArenaName", "str")==AtArena):
     AtArena = "1";
    gamelist.append( { 'date': str(gameinfo[0]), 'hometeam': str(gameinfo[1]), 'awayteam': str(gameinfo[2]), 'goals': str(gameinfo[3]), 'sogs': str(gameinfo[4]), 'ppgs': str(gameinfo[5]), 'shgs': str(gameinfo[6]), 'penalties': str(gameinfo[7]), 'pims': str(gameinfo[8]), 'hits': str(gameinfo[9]), 'takeaways': str(gameinfo[10]), 'faceoffwins': str(gameinfo[11]), 'atarena': str(AtArena), 'isplayoffgame': str(gameinfo[13]) } );
    if(verbose):
     VerbosePrintOut("   <game date=\""+EscapeXMLString(str(gameinfo[0]), quote=True)+"\" hometeam=\""+EscapeXMLString(str(gameinfo[1]), quote=True)+"\" awayteam=\""+EscapeXMLString(str(gameinfo[2]), quote=True)+"\" goals=\""+EscapeXMLString(str(gameinfo[3]), quote=True)+"\" sogs=\""+EscapeXMLString(str(gameinfo[4]), quote=True)+"\" ppgs=\""+EscapeXMLString(str(gameinfo[5]), quote=True)+"\" shgs=\""+EscapeXMLString(str(gameinfo[6]), quote=True)+"\" penalties=\""+EscapeXMLString(str(gameinfo[7]), quote=True)+"\" pims=\""+EscapeXMLString(str(gameinfo[8]), quote=True)+"\" hits=\""+EscapeXMLString(str(gameinfo[9]), quote=True)+"\" takeaways=\""+EscapeXMLString(str(gameinfo[10]), quote=True)+"\" faceoffwins=\""+EscapeXMLString(str(gameinfo[11]), quote=True)+"\" atarena=\""+EscapeXMLString(str(AtArena), quote=True)+"\" isplayoffgame=\""+EscapeXMLString(str(gameinfo[13]), quote=True)+"\" />");
   if(verbose):
    VerbosePrintOut("  </games>");
  leaguearray[str(leagueinfo[0])].update( { "games": gamelist } );
  leaguearrayout.update(leaguearray);
  if(verbose):
   VerbosePrintOut(" </league>");
 leaguearrayout.update( { 'leaguelist': leaguelist } );
 if(verbose):
  VerbosePrintOut("</hockey>");
 leaguecur.close();
 sqldatacon[1].close();
 if(not CheckHockeyArray(leaguearrayout)):
  return False;
 return leaguearrayout;

def MakeHockeyArrayFromHockeySQL(sqlfile, sdbfile=None, sqlisfile=True, verbose=True):
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
 sqldatacon = MakeHockeyDatabase(":memory:");
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 sqldatacon[0].executescript(sqlstring);
 leaguecur = sqldatacon[1].cursor();
 if(verbose):
  VerbosePrintOut("<?xml version=\"1.0\" encoding=\"UTF-8\"?>");
  VerbosePrintOut("<hockey database=\""+EscapeXMLString(str(sdbfile), quote=True)+"\">");
 getleague_num = leaguecur.execute("SELECT COUNT(*) FROM HockeyLeagues").fetchone()[0];
 getleague = leaguecur.execute("SELECT LeagueName, LeagueFullName, CountryName, FullCountryName, Date, PlayOffFMT, OrderType, NumberOfConferences, NumberOfDivisions FROM HockeyLeagues");
 leaguearrayout = { 'database': str(sdbfile) };
 leaguelist = [];
 for leagueinfo in getleague:
  leaguearray = {};
  arenalist = [];
  gamelist = [];
  HockeyLeagueHasConferences = True;
  HockeyLeagueHasConferenceStr = "yes";
  if(int(leagueinfo[7])<=0):
   HockeyLeagueHasConferences = False;
   HockeyLeagueHasConferenceStr = "no";
  HockeyLeagueHasDivisions = True;
  HockeyLeagueHasDivisionStr = "yes";
  if(int(leagueinfo[8])<=0):
   HockeyLeagueHasDivisions = False;
   HockeyLeagueHasDivisionStr = "no";
  tempdict = { 'leagueinfo': { 'name': str(leagueinfo[0]), 'fullname': str(leagueinfo[1]), 'country': str(leagueinfo[2]), 'fullcountry': str(leagueinfo[3]), 'date': str(leagueinfo[4]), 'playofffmt': str(leagueinfo[5]), 'ordertype': str(leagueinfo[6]), 'conferences': str(HockeyLeagueHasConferenceStr), 'divisions': str(HockeyLeagueHasDivisionStr) }, 'quickinfo': {'conferenceinfo': {}, 'divisioninfo': {}, 'teaminfo': {} } };
  leaguearray.update( { str(leagueinfo[0]): tempdict } );
  leaguelist.append(str(leagueinfo[0]));
  if(verbose):
   VerbosePrintOut(" <league name=\""+EscapeXMLString(str(leagueinfo[0]), quote=True)+"\" fullname=\""+EscapeXMLString(str(leagueinfo[1]), quote=True)+"\" country=\""+EscapeXMLString(str(leagueinfo[2]), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(leagueinfo[3]), quote=True)+"\" date=\""+EscapeXMLString(str(leagueinfo[4]), quote=True)+"\" playofffmt=\""+EscapeXMLString(str(leagueinfo[5]), quote=True)+"\" ordertype=\""+EscapeXMLString(str(leagueinfo[6]), quote=True)+"\" conferences=\""+EscapeXMLString(str(HockeyLeagueHasConferenceStr), quote=True)+"\" divisions=\""+EscapeXMLString(str(HockeyLeagueHasDivisionStr), quote=True)+"\">");
  conferencecur = sqldatacon[1].cursor();
  getconference_num = conferencecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Conferences WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\"").fetchone()[0];
  getconference = conferencecur.execute("SELECT Conference, ConferencePrefix, ConferenceSuffix, FullName FROM "+leagueinfo[0]+"Conferences WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\"");
  conferencelist = [];
  for conferenceinfo in getconference:
   leaguearray[str(leagueinfo[0])].update( { str(conferenceinfo[0]): { 'conferenceinfo': { 'name': str(conferenceinfo[0]), 'prefix': str(conferenceinfo[1]), 'suffix': str(conferenceinfo[2]), 'fullname': str(conferenceinfo[3]), 'league': str(leagueinfo[0]) } } } );
   leaguearray[str(leagueinfo[0])]['quickinfo']['conferenceinfo'].update( { str(conferenceinfo[0]): { 'name': str(conferenceinfo[0]), 'fullname': str(conferenceinfo[3]), 'league': str(leagueinfo[0]) } } );
   conferencelist.append(str(conferenceinfo[0]));
   if(verbose):
    VerbosePrintOut("  <conference name=\""+str(conferenceinfo[0])+"\" prefix=\""+EscapeXMLString(str(conferenceinfo[1]), quote=True)+"\" suffix=\""+EscapeXMLString(str(conferenceinfo[2]), quote=True)+"\">");
   divisioncur = sqldatacon[1].cursor();
   getdivision_num = divisioncur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Divisions WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\"").fetchone()[0];
   getdivision = divisioncur.execute("SELECT Division, DivisionPrefix, DivisionSuffix, FullName FROM "+leagueinfo[0]+"Divisions WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\"");
   divisionlist = [];
   for divisioninfo in getdivision:
    leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update( { str(divisioninfo[0]): { 'divisioninfo': { 'name': str(divisioninfo[0]), 'prefix': str(divisioninfo[1]), 'suffix': str(divisioninfo[2]), 'fullname': str(divisioninfo[3]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]) } } } );
    leaguearray[str(leagueinfo[0])]['quickinfo']['divisioninfo'].update( { str(divisioninfo[0]): { 'name': str(divisioninfo[0]), 'fullname': str(divisioninfo[3]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]) } } );
    divisionlist.append(str(divisioninfo[0]));
    if(verbose):
     VerbosePrintOut("   <division name=\""+EscapeXMLString(str(divisioninfo[0]), quote=True)+"\" prefix=\""+EscapeXMLString(str(divisioninfo[1]), quote=True)+"\" suffix=\""+EscapeXMLString(str(divisioninfo[2]), quote=True)+"\">");
    teamcur = sqldatacon[1].cursor();
    getteam_num = teamcur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Teams WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"").fetchone()[0];
    getteam = teamcur.execute("SELECT CityName, AreaName, FullAreaName, CountryName, FullCountryName, TeamName, ArenaName, TeamPrefix, TeamSuffix FROM "+leagueinfo[0]+"Teams WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"");
    teamlist = [];
    for teaminfo in getteam:
     fullteamname = GetFullTeamName(str(teaminfo[5]), str(teaminfo[7]), str(teaminfo[8]));
     leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(divisioninfo[0])].update( { str(teaminfo[5]): { 'teaminfo': { 'city': str(teaminfo[0]), 'area': str(teaminfo[1]), 'fullarea': str(teaminfo[2]), 'country': str(teaminfo[3]), 'fullcountry': str(teaminfo[4]), 'name': str(teaminfo[5]), 'fullname': fullteamname, 'arena': str(teaminfo[6]), 'prefix': str(teaminfo[7]), 'suffix': str(teaminfo[8]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0]) } } } );
     leaguearray[str(leagueinfo[0])]['quickinfo']['teaminfo'].update( { str(teaminfo[5]): { 'name': str(teaminfo[5]), 'fullname': fullteamname, 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0]) } } );
     teamlist.append(str(teaminfo[5]));
     if(verbose):
      VerbosePrintOut("    <team city=\""+EscapeXMLString(str(teaminfo[0]), quote=True)+"\" area=\""+EscapeXMLString(str(teaminfo[1]), quote=True)+"\" fullarea=\""+EscapeXMLString(str(teaminfo[2]), quote=True)+"\" country=\""+EscapeXMLString(str(teaminfo[3]), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(teaminfo[4]), quote=True)+"\" name=\""+EscapeXMLString(str(teaminfo[5]), quote=True)+"\" arena=\""+EscapeXMLString(str(teaminfo[6]), quote=True)+"\" prefix=\""+EscapeXMLString(str(teaminfo[7]), quote=True)+"\" suffix=\""+EscapeXMLString(str(teaminfo[8]), quote=True)+"\" />");
    teamcur.close();
    leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(divisioninfo[0])].update( { 'teamlist': teamlist } );
    if(verbose):
     VerbosePrintOut("   </division>");
   divisioncur.close();
   leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update( { 'divisionlist': divisionlist } );
   if(verbose):
    VerbosePrintOut("  </conference>");
  conferencecur.close();
  leaguearray[str(leagueinfo[0])].update( { 'conferencelist': conferencelist } );
  arenacur = sqldatacon[1].cursor();
  getteam_num = arenacur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Arenas WHERE TeamID=0").fetchone()[0];
  getarena = arenacur.execute("SELECT CityName, AreaName, FullAreaName, CountryName, FullCountryName, ArenaName FROM "+leagueinfo[0]+"Arenas WHERE TeamID=0");
  if(getteam_num>0):
   for arenainfo in getarena:
    if(verbose):
     VerbosePrintOut("   <arena city=\""+EscapeXMLString(str(arenainfo[0]), quote=True)+"\" area=\""+EscapeXMLString(str(arenainfo[1]), quote=True)+"\" fullarea=\""+EscapeXMLString(str(arenainfo[2]), quote=True)+"\" country=\""+EscapeXMLString(str(arenainfo[3]), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(arenainfo[4]), quote=True)+"\" name=\""+EscapeXMLString(str(arenainfo[5]), quote=True)+"\" />");
    arenalist.append( { 'city': str(arenainfo[0]), 'area': str(arenainfo[1]), 'fullarea': str(arenainfo[2]), 'country': str(arenainfo[3]), 'fullcountry': str(arenainfo[4]), 'name': str(arenainfo[5]) } );
    if(verbose):
     VerbosePrintOut("   <arena city=\""+EscapeXMLString(str(arenainfo[0]), quote=True)+"\" area=\""+EscapeXMLString(str(arenainfo[1]), quote=True)+"\" fullarea=\""+EscapeXMLString(str(arenainfo[2]), quote=True)+"\" country=\""+EscapeXMLString(str(arenainfo[3]), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(arenainfo[4]), quote=True)+"\" name=\""+EscapeXMLString(str(arenainfo[5]), quote=True)+"\" />");
   if(verbose):
    VerbosePrintOut("  </arenas>");
  leaguearray[str(leagueinfo[0])].update( { "arenas": arenalist } );
  gamecur = sqldatacon[1].cursor();
  getgame_num = gamecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Games").fetchone()[0];
  getgame = gamecur.execute("SELECT Date, HomeTeam, AwayTeam, TeamScorePeriods, ShotsOnGoal, PowerPlays, ShortHanded, Penalties, PenaltyMinutes, HitsPerPeriod, TakeAways, FaceoffWins, AtArena, IsPlayOffGame FROM "+leagueinfo[0]+"Games");
  if(getgame_num>0):
   if(verbose):
    VerbosePrintOut("  <games>");
   for gameinfo in getgame:
    AtArena = gameinfo[12];
    if(GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[1]), "FullArenaName", "str")==AtArena):
     AtArena = "0";
    if(GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[2]), "FullArenaName", "str")==AtArena):
     AtArena = "1";
    gamelist.append( { 'date': str(gameinfo[0]), 'hometeam': str(gameinfo[1]), 'awayteam': str(gameinfo[2]), 'goals': str(gameinfo[3]), 'sogs': str(gameinfo[4]), 'ppgs': str(gameinfo[5]), 'shgs': str(gameinfo[6]), 'penalties': str(gameinfo[7]), 'pims': str(gameinfo[8]), 'hits': str(gameinfo[9]), 'takeaways': str(gameinfo[10]), 'faceoffwins': str(gameinfo[11]), 'atarena': str(AtArena), 'isplayoffgame': str(gameinfo[13]) } );
    if(verbose):
     VerbosePrintOut("   <game date=\""+EscapeXMLString(str(gameinfo[0]), quote=True)+"\" hometeam=\""+EscapeXMLString(str(gameinfo[1]), quote=True)+"\" awayteam=\""+EscapeXMLString(str(gameinfo[2]), quote=True)+"\" goals=\""+EscapeXMLString(str(gameinfo[3]), quote=True)+"\" sogs=\""+EscapeXMLString(str(gameinfo[4]), quote=True)+"\" ppgs=\""+EscapeXMLString(str(gameinfo[5]), quote=True)+"\" shgs=\""+EscapeXMLString(str(gameinfo[6]), quote=True)+"\" penalties=\""+EscapeXMLString(str(gameinfo[7]), quote=True)+"\" pims=\""+EscapeXMLString(str(gameinfo[8]), quote=True)+"\" hits=\""+EscapeXMLString(str(gameinfo[9]), quote=True)+"\" takeaways=\""+EscapeXMLString(str(gameinfo[10]), quote=True)+"\" faceoffwins=\""+EscapeXMLString(str(gameinfo[11]), quote=True)+"\" atarena=\""+EscapeXMLString(str(AtArena), quote=True)+"\" isplayoffgame=\""+EscapeXMLString(str(gameinfo[13]), quote=True)+"\" />");
   if(verbose):
    VerbosePrintOut("  </games>");
  leaguearray[str(leagueinfo[0])].update( { "games": gamelist } );
  leaguearrayout.update(leaguearray);
  if(verbose):
   VerbosePrintOut(" </league>");
 leaguearrayout.update( { 'leaguelist': leaguelist } );
 if(verbose):
  VerbosePrintOut("</hockey>");
 leaguecur.close();
 sqldatacon[1].close();
 if(not CheckHockeyArray(leaguearrayout)):
  return False;
 return leaguearrayout;

def MakeHockeySQLFromHockeyArray(inhockeyarray, sdbfile=":memory:", verbose=True):
 if(not CheckHockeyArray(inhockeyarray)):
  return False;
 if(sdbfile is None):
  sdbfile = ":memory:";
 sqldatacon = MakeHockeyDatabaseFromHockeyArray(inhockeyarray, ":memory:", False, True, False)[0];
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 sqldump = "-- "+__program_name__+" SQL Dumper\n";
 sqldump = sqldump+"-- version "+__version__+"\n";
 sqldump = sqldump+"-- "+__project_url__+"\n";
 sqldump = sqldump+"--\n";
 sqldump = sqldump+"-- Generation Time: "+time.strftime("%B %d, %Y at %I:%M %p", time.localtime())+"\n";
 sqldump = sqldump+"-- SQLite Server version: "+sqlite3.sqlite_version+"\n";
 sqldump = sqldump+"-- PySQLite version: "+sqlite3.version+"\n";
 sqldump = sqldump+"-- Python Version: "+str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2])+"\n";
 sqldump = sqldump+"--\n";
 sqldump = sqldump+"-- Database: "+sdbfile+"\n";
 sqldump = sqldump+"--\n\n";
 sqldump = sqldump+"-- --------------------------------------------------------\n\n";
 if(verbose):
  VerbosePrintOut("-- "+__program_name__+" SQL Dumper");
  VerbosePrintOut("-- version "+__version__+"");
  VerbosePrintOut("-- "+__project_url__+"");
  VerbosePrintOut("--");
  VerbosePrintOut("-- Generation Time: "+time.strftime("%B %d, %Y at %I:%M %p", time.localtime())+"");
  VerbosePrintOut("-- SQLite Server version: "+sqlite3.sqlite_version+"");
  VerbosePrintOut("-- PySQLite version: "+sqlite3.version+"");
  VerbosePrintOut("-- Python Version: "+str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2])+"");
  VerbosePrintOut("--");
  VerbosePrintOut("-- Database: "+sdbfile);
  VerbosePrintOut("--");
  VerbosePrintOut("-- --------------------------------------------------------");
  VerbosePrintOut(" ");
 #all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games", "PlayoffTeams"];
 all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games"];
 table_list = ['HockeyLeagues'];
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
  if(verbose):
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
    if(isinstance(result_val, basestring)):
     get_insert_stmt_val += "\""+str(result_val)+"\", ";
    if(isinstance(result_val, baseint)):
     get_insert_stmt_val += ""+str(result_val)+", ";
    if(isinstance(result_val, float)):
     get_insert_stmt_val += ""+str(result_val)+", ";
   get_insert_stmt = get_insert_stmt[:-2]+") VALUES \n";
   if(verbose):
    VerbosePrintOut(get_insert_stmt[:-2]+") VALUES ");
   get_insert_stmt_val = get_insert_stmt_val[:-2]+");";
   if(verbose):
    VerbosePrintOut(get_insert_stmt_val[:-2]+");");
   get_insert_stmt_full += str(get_insert_stmt+get_insert_stmt_val)+"\n";
  sqldump = sqldump+get_insert_stmt_full+"\n-- --------------------------------------------------------\n\n";
  if(verbose):
   VerbosePrintOut("-- --------------------------------------------------------");
   VerbosePrintOut(" ");
 CloseHockeyDatabase(sqldatacon);
 return sqldump;

def MakeHockeySQLFileFromHockeyArray(inhockeyarray, sqlfile=None, returnsql=False, verbose=True):
 if(sqlfile is None):
  return False;
 sqlfp = open(sqlfile, "w+");
 sqlstring = MakeHockeySQLFromHockeyArray(inhockeyarray, os.path.splitext("sqlfile")[0]+".db3", verbose);
 sqlfp.write(sqlstring);
 sqlfp.close();
 if(returnsql):
  return sqlstring;
 if(not returnsql):
  return True;
 return True;

def MakeHockeyArrayFromOldHockeyDatabase(sdbfile, verbose=True):
 if(os.path.exists(sdbfile) and os.path.isfile(sdbfile) and isinstance(sdbfile, basestring)):
  sqldatacon = OpenHockeyDatabase(sdbfile);
 else:
  if(sdbfile is not None and isinstance(sdbfile, (tuple, list))):
   sqldatacon = tuple(sdbfile);
  else:
   return False;
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 leaguecur = sqldatacon[1].cursor();
 if(verbose):
  VerbosePrintOut("<?xml version=\"1.0\" encoding=\"UTF-8\"?>");
  VerbosePrintOut("<hockey database=\""+EscapeXMLString(str(sdbfile), quote=True)+"\">");
 gettablecur = sqldatacon[1].cursor();
 gettable_num = gettablecur.execute("SELECT COUNT(*) FROM sqlite_master WHERE type=\"table\" and name LIKE \"%Teams\"").fetchone()[0];
 gettable = gettablecur.execute("SELECT name FROM sqlite_master WHERE type=\"table\" and name LIKE \"%Teams\"");
 mktemptablecur = sqldatacon[1].cursor();
 mktemptablecur.execute("CREATE TEMP TABLE HockeyLeagues (\n" + \
 "  id INTEGER PRIMARY KEY AUTOINCREMENT,\n" + \
 "  LeagueName TEXT NOT NULL DEFAULT '',\n" + \
 "  LeagueFullName TEXT NOT NULL DEFAULT '',\n" + \
 "  CountryName TEXT NOT NULL DEFAULT '',\n" + \
 "  FullCountryName TEXT NOT NULL DEFAULT '',\n" + \
 "  Date INTEGER NOT NULL DEFAULT 0,\n" + \
 "  PlayOffFMT TEXT NOT NULL DEFAULT '',\n" + \
 "  OrderType TEXT NOT NULL DEFAULT '',\n" + \
 "  NumberOfTeams INTEGER NOT NULL DEFAULT 0,\n" + \
 "  NumberOfConferences INTEGER NOT NULL DEFAULT 0,\n" + \
 "  NumberOfDivisions INTEGER NOT NULL DEFAULT ''\n" + \
 ");");
 for tableinfo in gettable:
  LeagueName = re.sub("Teams$", "", tableinfo[0]);
  LeagueNameInfo = GetHockeyLeaguesInfo(LeagueName);
  getconference_num = mktemptablecur.execute("SELECT COUNT(*) FROM "+LeagueName+"Conferences").fetchone()[0];
  getdivision_num = mktemptablecur.execute("SELECT COUNT(*) FROM "+LeagueName+"Divisions").fetchone()[0];
  getteam_num = mktemptablecur.execute("SELECT COUNT(*) FROM "+LeagueName+"Teams").fetchone()[0];
  getallteam_num = getteam_num;
  mktemptablecur.execute("INSERT INTO HockeyLeagues (LeagueName, LeagueFullName, CountryName, FullCountryName, Date, PlayOffFMT, OrderType, NumberOfTeams, NumberOfConferences, NumberOfDivisions) VALUES \n" + \
  "(\""+str(LeagueNameInfo['LeagueName'])+"\", \""+str(LeagueNameInfo['FullLeagueName'])+"\", \""+str(LeagueNameInfo['CountryName'])+"\", \""+str(LeagueNameInfo['FullCountryName'])+"\", "+str(LeagueNameInfo['StartDate'])+", \""+str(LeagueNameInfo['PlayOffFMT'])+"\", \""+str(LeagueNameInfo['OrderType'])+"\", "+str(getteam_num)+", "+str(getconference_num)+", "+str(getdivision_num)+")");
 gettablecur.close();
 getleague_num = leaguecur.execute("SELECT COUNT(*) FROM HockeyLeagues").fetchone()[0];
 getleague = leaguecur.execute("SELECT LeagueName, LeagueFullName, CountryName, FullCountryName, Date, PlayOffFMT, OrderType, NumberOfTeams, NumberOfConferences, NumberOfDivisions FROM HockeyLeagues");
 leaguearrayout = { 'database': str(sdbfile) };
 leaguelist = [];
 for leagueinfo in getleague:
  leaguearray = {};
  arenalist = [];
  gamelist = [];
  HockeyLeagueHasConferences = True;
  HockeyLeagueHasConferenceStr = "yes";
  if(int(leagueinfo[7])<=0):
   HockeyLeagueHasConferences = False;
   HockeyLeagueHasConferenceStr = "no";
  HockeyLeagueHasDivisions = True;
  HockeyLeagueHasDivisionStr = "yes";
  if(int(leagueinfo[8])<=0):
   HockeyLeagueHasDivisions = False;
   HockeyLeagueHasDivisionStr = "no";
  tempdict = { 'leagueinfo': { 'name': str(leagueinfo[0]), 'fullname': str(leagueinfo[1]), 'country': str(leagueinfo[2]), 'fullcountry': str(leagueinfo[3]), 'date': str(leagueinfo[4]), 'playofffmt': str(leagueinfo[5]), 'ordertype': str(leagueinfo[6]), 'conferences': str(HockeyLeagueHasConferenceStr), 'divisions': str(HockeyLeagueHasDivisionStr) }, 'quickinfo': {'conferenceinfo': {}, 'divisioninfo': {}, 'teaminfo': {} } };
  leaguearray.update( { str(leagueinfo[0]): tempdict } );
  leaguelist.append(str(leagueinfo[0]));
  if(verbose):
   VerbosePrintOut(" <league name=\""+EscapeXMLString(str(leagueinfo[0]), quote=True)+"\" fullname=\""+EscapeXMLString(str(leagueinfo[1]), quote=True)+"\" country=\""+EscapeXMLString(str(leagueinfo[2]), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(leagueinfo[3]), quote=True)+"\" date=\""+EscapeXMLString(str(leagueinfo[4]), quote=True)+"\" playofffmt=\""+EscapeXMLString(str(leagueinfo[5]), quote=True)+"\" ordertype=\""+EscapeXMLString(str(leagueinfo[6]), quote=True)+"\" conferences=\""+EscapeXMLString(str(HockeyLeagueHasConferenceStr), quote=True)+"\" divisions=\""+EscapeXMLString(str(HockeyLeagueHasDivisionStr), quote=True)+"\">");
  conferencecur = sqldatacon[1].cursor();
  getconference_num = conferencecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Conferences").fetchone()[0];
  getconference = conferencecur.execute("SELECT Conference FROM "+leagueinfo[0]+"Conferences");
  conferencelist = [];
  for conferenceinfo in getconference:
   leaguearray[str(leagueinfo[0])].update( { str(conferenceinfo[0]): { 'conferenceinfo': { 'name': str(conferenceinfo[0]), 'league': str(leagueinfo[0]) } } } );
   leaguearray[str(leagueinfo[0])]['quickinfo']['conferenceinfo'].update( { str(conferenceinfo[0]): { 'name': str(conferenceinfo[0]), 'league': str(leagueinfo[0]) } } );
   conferencelist.append(str(conferenceinfo[0]));
   if(verbose):
    VerbosePrintOut("  <conference name=\""+EscapeXMLString(str(conferenceinfo[0]), quote=True)+"\" prefix=\"\" suffix=\"Conference\">");
   divisioncur = sqldatacon[1].cursor();
   getdivision_num = divisioncur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Divisions WHERE Conference=\""+conferenceinfo[0]+"\"").fetchone()[0];
   getdivision = divisioncur.execute("SELECT Division FROM "+leagueinfo[0]+"Divisions WHERE Conference=\""+conferenceinfo[0]+"\"");
   divisionlist = [];
   for divisioninfo in getdivision:
    leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update( { str(divisioninfo[0]): { 'divisioninfo': { 'name': str(divisioninfo[0]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]) } } } );
    leaguearray[str(leagueinfo[0])]['quickinfo']['divisioninfo'].update( { str(divisioninfo[0]): { 'name': str(divisioninfo[0]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]) } } );
    divisionlist.append(str(divisioninfo[0]));
    if(verbose):
     VerbosePrintOut("   <division name=\""+EscapeXMLString(str(divisioninfo[0]), quote=True)+"\" prefix=\"\" suffix=\"Division\">");
    teamcur = sqldatacon[1].cursor();
    getteam_num = teamcur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Teams WHERE Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"").fetchone()[0];
    getteam = teamcur.execute("SELECT CityName, AreaName, TeamName, ArenaName, TeamPrefix FROM "+leagueinfo[0]+"Teams WHERE Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"");
    teamlist = [];
    for teaminfo in getteam:
     TeamAreaInfo = GetAreaInfoFromUSCA(teaminfo[1]);
     fullteamname = GetFullTeamName(str(teaminfo[2]), str(teaminfo[4]), "");
     leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(divisioninfo[0])].update( { str(teaminfo[2]): { 'teaminfo': { 'city': str(teaminfo[0]), 'area': str(TeamAreaInfo['AreaName']), 'fullarea': str(TeamAreaInfo['FullAreaName']), 'country': str(TeamAreaInfo['CountryName']), 'fullcountry': str(TeamAreaInfo['FullCountryName']), 'name': str(teaminfo[2]), 'fullname': fullteamname, 'arena': str(teaminfo[3]), 'prefix': str(teaminfo[4]), 'suffix': "", 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0]) } } } );
     leaguearray[str(leagueinfo[0])]['quickinfo']['teaminfo'].update( { str(teaminfo[2]): { 'name': str(teaminfo[2]), 'fullname': fullteamname, 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0]) } } );
     teamlist.append(str(teaminfo[2]));
     if(verbose):
      VerbosePrintOut("    <team city=\""+EscapeXMLString(str(teaminfo[0]), quote=True)+"\" area=\""+EscapeXMLString(str(TeamAreaInfo['AreaName']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(TeamAreaInfo['FullAreaName']), quote=True)+"\" country=\""+EscapeXMLString(str(TeamAreaInfo['CountryName']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(TeamAreaInfo['FullCountryName']), quote=True)+"\" name=\""+EscapeXMLString(str(teaminfo[2]), quote=True)+"\" arena=\""+EscapeXMLString(str(teaminfo[3]), quote=True)+"\" prefix=\""+EscapeXMLString(str(teaminfo[4]), quote=True)+"\" suffix=\"\" />");
    teamcur.close();
    leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(divisioninfo[0])].update( { 'teamlist': teamlist } );
    if(verbose):
     VerbosePrintOut("   </division>");
   divisioncur.close();
   leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update( { 'divisionlist': divisionlist } );
   if(verbose):
    VerbosePrintOut("  </conference>");
  conferencecur.close();
  leaguearray[str(leagueinfo[0])].update( { 'conferencelist': conferencelist } );
  arenacur = sqldatacon[1].cursor();
  getteam_num = arenacur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Arenas WHERE id>"+str(getallteam_num)).fetchone()[0];
  getarena = arenacur.execute("SELECT CityName, AreaName, ArenaName FROM "+leagueinfo[0]+"Arenas WHERE id>"+str(getallteam_num));
  if(getteam_num>0):
   if(verbose):
    VerbosePrintOut("  <arenas>");
   for arenainfo in getarena:
    ArenaAreaInfo = GetAreaInfoFromUSCA(arenainfo[1]);
    arenalist.append( { 'city': str(arenainfo[0]), 'area': str(ArenaAreaInfo['AreaName']), 'fullarea': str(ArenaAreaInfo['FullAreaName']), 'country': str(ArenaAreaInfo['CountryName']), 'fullcountry': str(ArenaAreaInfo['FullCountryName']), 'name': str(arenainfo[2]) } );
    if(verbose):
     VerbosePrintOut("   <arena city=\""+EscapeXMLString(str(arenainfo[0]), quote=True)+"\" area=\""+EscapeXMLString(str(ArenaAreaInfo['AreaName']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(ArenaAreaInfo['FullAreaName']), quote=True)+"\" country=\""+EscapeXMLString(str(ArenaAreaInfo['CountryName']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(ArenaAreaInfo['FullCountryName']), quote=True)+"\" name=\""+EscapeXMLString(str(arenainfo[2]), quote=True)+"\" />");
   if(verbose):
    VerbosePrintOut("  </arenas>");
  leaguearray[str(leagueinfo[0])].update( { "arenas": arenalist } );
  gamecur = sqldatacon[1].cursor();
  getgame_num = gamecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Games").fetchone()[0];
  getgame = gamecur.execute("SELECT Date, HomeTeam, AwayTeam, TeamScorePeriods, ShotsOnGoal, AtArena, IsPlayOffGame FROM "+leagueinfo[0]+"Games");
  if(getgame_num>0):
   if(verbose):
    VerbosePrintOut("  <games>");
   for gameinfo in getgame:
    GetNumPeriods = len(gameinfo[3].split(","));
    EmptyScore = ",0:0" * (GetNumPeriods - 1);
    EmptyScore = "0:0"+EmptyScore;
    AtArena = gameinfo[5];
    if(GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[1]), "FullArenaName", "str")==AtArena):
     AtArena = "0";
    if(GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[2]), "FullArenaName", "str")==AtArena):
     AtArena = "1";
    gamelist.append( { 'date': str(gameinfo[0]), 'hometeam': str(gameinfo[1]), 'awayteam': str(gameinfo[2]), 'goals': str(gameinfo[3]), 'sogs': str(gameinfo[4]), 'ppgs': str(EmptyScore), 'shgs': str(EmptyScore), 'penalties': str(EmptyScore), 'pims': str(EmptyScore), 'hits': str(EmptyScore), 'takeaways': str(EmptyScore), 'faceoffwins': str(EmptyScore), 'atarena': str(AtArena), 'isplayoffgame': str(gameinfo[6]) } );
    if(verbose):
     VerbosePrintOut("   <game date=\""+EscapeXMLString(str(gameinfo[0]), quote=True)+"\" hometeam=\""+EscapeXMLString(str(gameinfo[1]), quote=True)+"\" awayteam=\""+EscapeXMLString(str(gameinfo[2]), quote=True)+"\" goals=\""+EscapeXMLString(str(gameinfo[3]), quote=True)+"\" sogs=\""+EscapeXMLString(str(gameinfo[4]), quote=True)+"\" ppgs=\""+EscapeXMLString(str(EmptyScore), quote=True)+"\" shgs=\""+EscapeXMLString(str(EmptyScore), quote=True)+"\" penalties=\""+EscapeXMLString(str(EmptyScore), quote=True)+"\" pims=\""+EscapeXMLString(str(EmptyScore), quote=True)+"\" hits=\""+EscapeXMLString(str(EmptyScore), quote=True)+"\" takeaways=\""+EscapeXMLString(str(EmptyScore), quote=True)+"\" faceoffwins=\""+EscapeXMLString(str(EmptyScore), quote=True)+"\" atarena=\""+EscapeXMLString(str(AtArena), quote=True)+"\" isplayoffgame=\""+EscapeXMLString(str(gameinfo[6]), quote=True)+"\" />");
   if(verbose):
    VerbosePrintOut("  </games>");
  leaguearray[str(leagueinfo[0])].update( { "games": gamelist } );
  leaguearrayout.update(leaguearray);
  if(verbose):
   VerbosePrintOut(" </league>");
 leaguearrayout.update( { 'leaguelist': leaguelist } );
 if(verbose):
  VerbosePrintOut("</hockey>");
 leaguecur.close();
 CloseHockeyDatabase(sqldatacon);
 if(not CheckHockeyArray(leaguearrayout)):
  return False;
 return leaguearrayout;

def MakeHockeySQLiteArrayFromHockeyDatabase(sdbfile, verbose=True):
 if(os.path.exists(sdbfile) and os.path.isfile(sdbfile) and isinstance(sdbfile, basestring)):
  if(not CheckHockeySQLiteDatabase(sdbfile)[0]):
   return False;
  sqldatacon = OpenHockeyDatabase(sdbfile);
 else:
  if(sdbfile is not None and isinstance(sdbfile, (tuple, list))):
   sqldatacon = tuple(sdbfile);
  else:
   return False;
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 #all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games", "PlayoffTeams"];
 all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games"];
 table_list = ['HockeyLeagues'];
 getleague_num_tmp = sqldatacon[0].execute("SELECT COUNT(*) FROM HockeyLeagues").fetchone()[0];
 getleague_tmp = sqldatacon[0].execute("SELECT LeagueName FROM HockeyLeagues");
 sqlitedict = { 'database': str(sdbfile) };
 for leagueinfo_tmp in getleague_tmp:
  for cur_tab in all_table_list:
   table_list.append(leagueinfo_tmp[0]+cur_tab);
 if(verbose):
  VerbosePrintOut("-- "+__program_name__+" SQL Dumper");
  VerbosePrintOut("-- version "+__version__+"");
  VerbosePrintOut("-- "+__project_url__+"");
  VerbosePrintOut("--");
  VerbosePrintOut("-- Generation Time: "+time.strftime("%B %d, %Y at %I:%M %p", time.localtime())+"");
  VerbosePrintOut("-- SQLite Server version: "+sqlite3.sqlite_version+"");
  VerbosePrintOut("-- PySQLite version: "+sqlite3.version+"");
  VerbosePrintOut("-- Python Version: "+str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2])+"");
  VerbosePrintOut("--");
  VerbosePrintOut("-- Database: "+sdbfile);
  VerbosePrintOut("--");
  VerbosePrintOut("-- --------------------------------------------------------");
 for get_cur_tab in table_list:
  if(verbose):
   VerbosePrintOut(" ");
   VerbosePrintOut("--");
   VerbosePrintOut("-- Table structure for table "+str(get_cur_tab)+"");
   VerbosePrintOut("--");
   VerbosePrintOut(" ");
   VerbosePrintOut("DROP TABLE IF EXISTS "+get_cur_tab+"\n");
   VerbosePrintOut("CREATE TEMP TABLE "+get_cur_tab+" (");
  gettableinfo = sqldatacon[0].execute("PRAGMA table_xinfo("+get_cur_tab+");").fetchall();
  sqlitedict.update( { get_cur_tab: { } } );
  collist = [];
  sqlrowlist = [];
  for tableinfo in gettableinfo:
   autoincrement = 0;
   if(tableinfo[1]=="id" and tableinfo[5]==1):
    autoincrement = 1;
   sqlitedict[get_cur_tab].update( { tableinfo[1]: { 'info': {'id': tableinfo[0], 'Name': tableinfo[1], 'Type': tableinfo[2], 'NotNull': tableinfo[3], 'DefualtValue': tableinfo[4], 'PrimaryKey': tableinfo[5], 'AutoIncrement': autoincrement, 'Hidden': tableinfo[6] } } } );
   sqlrowline = tableinfo[1]+" "+tableinfo[2];
   if(tableinfo[3]==1):
    sqlrowline = sqlrowline+" NOT NULL";
   if(tableinfo[4] is not None):
    sqlrowline = sqlrowline+" "+tableinfo[4];
   if(tableinfo[5]==1):
    sqlrowline = sqlrowline+" PRIMARY KEY";
   if(autoincrement==1):
    sqlrowline = sqlrowline+" AUTOINCREMENT";
   sqlrowlist.append(sqlrowline);
   collist.append(tableinfo[1]);
   gettabledata = sqldatacon[0].execute("SELECT "+', '.join(collist)+" FROM "+get_cur_tab);
   subcollist = [];
   rkeylist = [];
   rvaluelist = [];
   for tabledata in gettabledata:
    subcolarray = {};
    collen = len(tabledata);
    colleni = 0;
    while(colleni < collen):
     rkeylist.append(collist[colleni]);
     tabledataalt = tabledata[colleni];
     if(isinstance(tabledata[colleni], basestring)):
      tabledataalt = "\""+tabledata[colleni]+"\"";
     rvaluelist.append(str(tabledata[colleni]));
     subcolarray.update({collist[colleni]: tabledata[colleni]});
     colleni = colleni + 1;
    subcollist.append(subcolarray);
   sqlitedict[get_cur_tab].update( { 'values': subcollist } );
  if(verbose):
   VerbosePrintOut(str(',\n'.join(sqlrowlist))+"\n);\n");
   VerbosePrintOut(" ");
   VerbosePrintOut("--");
   VerbosePrintOut("-- Dumping data for table "+str(get_cur_tab)+"");
   VerbosePrintOut("--");
   VerbosePrintOut(" ");
   if(len(rvaluelist)>0):
    VerbosePrintOut("INSERT INTO "+str(get_cur_tab)+" ("+str(', '.join(rkeylist))+") VALUES");
    VerbosePrintOut("("+str(', '.join(rvaluelist))+");\n");
    VerbosePrintOut("-- --------------------------------------------------------");
  sqlitedict[get_cur_tab].update( { 'rows': collist } );
 sqldatacon[1].close();
 return sqlitedict;

def MakeHockeyArrayFromHockeySQLiteArray(inhockeyarray, verbose=True):
 if(not CheckHockeySQLiteArray(inhockeyarray)):
  return False;
 leaguearrayout = { 'database': str(inhockeyarray['database']) };
 leaguelist = [];
 for leagueinfo in inhockeyarray['HockeyLeagues']['values']:
  leaguearray = {};
  arenalist = [];
  gamelist = [];
  HockeyLeagueHasConferences = True;
  HockeyLeagueHasConferenceStr = "yes";
  if(int(leagueinfo['NumberOfConferences'])<=0):
   HockeyLeagueHasConferences = False;
   HockeyLeagueHasConferenceStr = "no";
  HockeyLeagueHasDivisions = True;
  HockeyLeagueHasDivisionStr = "yes";
  if(int(leagueinfo['NumberOfDivisions'])<=0):
   HockeyLeagueHasDivisions = False;
   HockeyLeagueHasDivisionStr = "no";
  tempdict = { 'leagueinfo': { 'name': str(leagueinfo['LeagueName']), 'fullname': str(leagueinfo['LeagueFullName']), 'country': str(leagueinfo['CountryName']), 'fullcountry': str(leagueinfo['FullCountryName']), 'date': str(leagueinfo['Date']), 'playofffmt': str(leagueinfo['PlayOffFMT']), 'ordertype': str(leagueinfo['OrderType']), 'conferences': str(HockeyLeagueHasConferenceStr), 'divisions': str(HockeyLeagueHasDivisionStr) }, 'quickinfo': {'conferenceinfo': {}, 'divisioninfo': {}, 'teaminfo': {} } };
  leaguearray.update( { str(leagueinfo['LeagueName']): tempdict } );
  leaguelist.append(str(leagueinfo['LeagueName']));
  if(verbose):
   VerbosePrintOut(" <league name=\""+EscapeXMLString(str(leagueinfo['LeagueName']), quote=True)+"\" fullname=\""+EscapeXMLString(str(leagueinfo['LeagueFullName']), quote=True)+"\" country=\""+EscapeXMLString(str(leagueinfo['CountryName']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(leagueinfo['FullCountryName']), quote=True)+"\" date=\""+EscapeXMLString(str(leagueinfo['Date']), quote=True)+"\" playofffmt=\""+EscapeXMLString(str(leagueinfo['PlayOffFMT']), quote=True)+"\" ordertype=\""+EscapeXMLString(str(leagueinfo['OrderType']), quote=True)+"\" conferences=\""+EscapeXMLString(str(HockeyLeagueHasConferenceStr), quote=True)+"\" divisions=\""+EscapeXMLString(str(HockeyLeagueHasDivisionStr), quote=True)+"\">");
  conferencelist = [];
  conarrayname = leagueinfo['LeagueName']+"Conferences";
  for conferenceinfo in inhockeyarray[conarrayname]['values']:
   leaguearray[str(leagueinfo['LeagueName'])].update( { str(conferenceinfo['Conference']): { 'conferenceinfo': { 'name': str(conferenceinfo['Conference']), 'prefix': str(conferenceinfo['ConferencePrefix']), 'suffix': str(conferenceinfo['ConferenceSuffix']), 'fullname': str(conferenceinfo['FullName']), 'league': str(leagueinfo['LeagueName']) } } } );
   leaguearray[str(leagueinfo['LeagueName'])]['quickinfo']['conferenceinfo'].update( { str(conferenceinfo['Conference']): { 'name': str(conferenceinfo['Conference']), 'fullname': str(conferenceinfo['FullName']), 'league': str(leagueinfo['LeagueName']) } } );
   conferencelist.append(str(conferenceinfo['Conference']));
   if(verbose):
    VerbosePrintOut("  <conference name=\""+str(conferenceinfo['Conference'])+"\" prefix=\""+EscapeXMLString(str(conferenceinfo['ConferencePrefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(conferenceinfo['ConferenceSuffix']), quote=True)+"\">");
   divisionlist = [];
   divarrayname = leagueinfo['LeagueName']+"Divisions";
   for divisioninfo in inhockeyarray[divarrayname]['values']:
    leaguearray[str(leagueinfo['LeagueName'])][str(conferenceinfo['Conference'])].update( { str(divisioninfo['Division']): { 'divisioninfo': { 'name': str(divisioninfo['Division']), 'prefix': str(divisioninfo['DivisionPrefix']), 'suffix': str(divisioninfo['DivisionSuffix']), 'fullname': str(divisioninfo['FullName']), 'league': str(leagueinfo['LeagueName']), 'conference': str(conferenceinfo['Conference']) } } } );
    leaguearray[str(leagueinfo['LeagueName'])]['quickinfo']['divisioninfo'].update( { str(divisioninfo['Division']): { 'name': str(divisioninfo['Division']), 'fullname': str(divisioninfo['FullName']), 'league': str(leagueinfo['LeagueName']), 'conference': str(conferenceinfo['Conference']) } } );
    divisionlist.append(str(divisioninfo['Division']));
    if(verbose):
     VerbosePrintOut("   <division name=\""+EscapeXMLString(str(divisioninfo['Division']), quote=True)+"\" prefix=\""+EscapeXMLString(str(divisioninfo['DivisionPrefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(divisioninfo['DivisionSuffix']), quote=True)+"\">");
    teamlist = [];
    teamarrayname = leagueinfo['LeagueName']+"Teams";
    for teaminfo in inhockeyarray[teamarrayname]['values']:
     fullteamname = GetFullTeamName(str(teaminfo['TeamName']), str(teaminfo['TeamPrefix']), str(teaminfo['TeamSuffix']));
     leaguearray[str(leagueinfo['LeagueName'])][str(conferenceinfo['Conference'])][str(divisioninfo['Division'])].update( { str(teaminfo['TeamName']): { 'teaminfo': { 'city': str(teaminfo['CityName']), 'area': str(teaminfo['AreaName']), 'fullarea': str(teaminfo['FullAreaName']), 'country': str(teaminfo['CountryName']), 'fullcountry': str(teaminfo['FullCountryName']), 'name': str(teaminfo['TeamName']), 'fullname': fullteamname, 'arena': str(teaminfo['ArenaName']), 'prefix': str(teaminfo['TeamPrefix']), 'suffix': str(teaminfo['TeamSuffix']), 'league': str(leagueinfo['LeagueName']), 'conference': str(conferenceinfo['Conference']), 'division': str(divisioninfo['Division']) } } } );
     leaguearray[str(leagueinfo['LeagueName'])]['quickinfo']['teaminfo'].update( { str(teaminfo['TeamName']): { 'name': str(teaminfo['TeamName']), 'fullname': fullteamname, 'league': str(leagueinfo['LeagueName']), 'conference': str(conferenceinfo['Conference']), 'division': str(divisioninfo['Division']) } } );
     teamlist.append(str(teaminfo['TeamName']));
     if(verbose):
      VerbosePrintOut("    <team city=\""+EscapeXMLString(str(teaminfo['CityName']), quote=True)+"\" area=\""+EscapeXMLString(str(teaminfo['AreaName']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(teaminfo['FullAreaName']), quote=True)+"\" country=\""+EscapeXMLString(str(teaminfo['CountryName']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(teaminfo['FullCountryName']), quote=True)+"\" name=\""+EscapeXMLString(str(teaminfo['TeamName']), quote=True)+"\" arena=\""+EscapeXMLString(str(teaminfo['ArenaName']), quote=True)+"\" prefix=\""+EscapeXMLString(str(teaminfo['TeamPrefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(teaminfo['TeamSuffix']), quote=True)+"\" />");
    leaguearray[str(leagueinfo['LeagueName'])][str(conferenceinfo['Conference'])][str(divisioninfo['Division'])].update( { 'teamlist': teamlist } );
    if(verbose):
     VerbosePrintOut("   </division>");
   leaguearray[str(leagueinfo['LeagueName'])][str(conferenceinfo['Conference'])].update( { 'divisionlist': divisionlist } );
   if(verbose):
    VerbosePrintOut("  </conference>");
  leaguearray[str(leagueinfo['LeagueName'])].update( { 'conferencelist': conferencelist } );
  araarrayname = leagueinfo['LeagueName']+"Arenas";
  getteam_num = len(inhockeyarray[teamarrayname]['values']);
  if(getteam_num>0):
   for arenainfo in inhockeyarray[teamarrayname]['values']:
    if(verbose):
     VerbosePrintOut("   <arena city=\""+EscapeXMLString(str(arenainfo['CityName']), quote=True)+"\" area=\""+EscapeXMLString(str(arenainfo['AreaName']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(arenainfo['FullAreaName']), quote=True)+"\" country=\""+EscapeXMLString(str(arenainfo['CountryName']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(arenainfo['FullCountryName']), quote=True)+"\" name=\""+EscapeXMLString(str(arenainfo['ArenaName']), quote=True)+"\" />");
    arenalist.append( { 'city': str(arenainfo['CityName']), 'area': str(arenainfo['AreaName']), 'fullarea': str(arenainfo['FullAreaName']), 'country': str(arenainfo['CountryName']), 'fullcountry': str(arenainfo['FullCountryName']), 'name': str(arenainfo['ArenaName']) } );
    if(verbose):
     VerbosePrintOut("   <arena city=\""+EscapeXMLString(str(arenainfo['CityName']), quote=True)+"\" area=\""+EscapeXMLString(str(arenainfo['AreaName']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(arenainfo['FullAreaName']), quote=True)+"\" country=\""+EscapeXMLString(str(arenainfo['CountryName']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(arenainfo['FullCountryName']), quote=True)+"\" name=\""+EscapeXMLString(str(arenainfo['ArenaName']), quote=True)+"\" />");
   if(verbose):
    VerbosePrintOut("  </arenas>");
  leaguearray[str(leagueinfo['LeagueName'])].update( { "arenas": arenalist } );
  gamearrayname = leagueinfo['LeagueName']+"Games";
  getgame_num = len(inhockeyarray[gamearrayname]['values']);
  if(getgame_num>0):
   if(verbose):
    VerbosePrintOut("  <games>");
   for gameinfo in inhockeyarray[gamearrayname]['values']:
    gamelist.append( { 'date': str(gameinfo['Date']), 'hometeam': str(gameinfo['HomeTeam']), 'awayteam': str(gameinfo['AwayTeam']), 'goals': str(gameinfo['TeamScorePeriods']), 'sogs': str(gameinfo['ShotsOnGoal']), 'ppgs': str(gameinfo['PowerPlays']), 'shgs': str(gameinfo['ShortHanded']), 'penalties': str(gameinfo['Penalties']), 'pims': str(gameinfo['PenaltyMinutes']), 'hits': str(gameinfo['HitsPerPeriod']), 'takeaways': str(gameinfo['TakeAways']), 'faceoffwins': str(gameinfo['FaceoffWins']), 'atarena': str(gameinfo['AtArena']), 'isplayoffgame': str(gameinfo['IsPlayOffGame']) } );
    if(verbose):
     VerbosePrintOut("   <game date=\""+EscapeXMLString(str(gameinfo['Date']), quote=True)+"\" hometeam=\""+EscapeXMLString(str(gameinfo['HomeTeam']), quote=True)+"\" awayteam=\""+EscapeXMLString(str(gameinfo['AwayTeam']), quote=True)+"\" goals=\""+EscapeXMLString(str(gameinfo['TeamScorePeriods']), quote=True)+"\" sogs=\""+EscapeXMLString(str(gameinfo['ShotsOnGoal']), quote=True)+"\" ppgs=\""+EscapeXMLString(str(gameinfo['PowerPlays']), quote=True)+"\" shgs=\""+EscapeXMLString(str(gameinfo['ShortHanded']), quote=True)+"\" penalties=\""+EscapeXMLString(str(gameinfo['Penalties']), quote=True)+"\" pims=\""+EscapeXMLString(str(gameinfo['PenaltyMinutes']), quote=True)+"\" hits=\""+EscapeXMLString(str(gameinfo['HitsPerPeriod']), quote=True)+"\" takeaways=\""+EscapeXMLString(str(gameinfo['TakeAways']), quote=True)+"\" faceoffwins=\""+EscapeXMLString(str(gameinfo['FaceoffWins']), quote=True)+"\" atarena=\""+EscapeXMLString(str(gameinfo['AtArena']), quote=True)+"\" isplayoffgame=\""+EscapeXMLString(str(gameinfo['IsPlayOffGame']), quote=True)+"\" />");
   if(verbose):
    VerbosePrintOut("  </games>");
  leaguearray[str(leagueinfo['LeagueName'])].update( { "games": gamelist } );
  leaguearrayout.update(leaguearray);
  if(verbose):
   VerbosePrintOut(" </league>");
 leaguearrayout.update( { 'leaguelist': leaguelist } );
 if(verbose):
  VerbosePrintOut("</hockey>");
 if(not CheckHockeyArray(leaguearrayout)):
  return False;
 return leaguearrayout;

def MakeHockeySQLFromHockeySQLiteArray(inhockeyarray, sdbfile=":memory:", verbose=True):
 if(not CheckHockeySQLiteArray(inhockeyarray)):
  return False;
 if(sdbfile is None or sdbfile==":memory:"):
  sdbfile = inhockeyarray['database'];
 #all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games", "PlayoffTeams"];
 all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games"];
 table_list = ['HockeyLeagues'];
 for leagueinfo_tmp in inhockeyarray['HockeyLeagues']['values']:
  for cur_tab in all_table_list:
   table_list.append(leagueinfo_tmp['LeagueName']+cur_tab);
 sqldump = "-- "+__program_name__+" SQL Dumper\n";
 sqldump = sqldump+"-- version "+__version__+"\n";
 sqldump = sqldump+"-- "+__project_url__+"\n";
 sqldump = sqldump+"--\n";
 sqldump = sqldump+"-- Generation Time: "+time.strftime("%B %d, %Y at %I:%M %p", time.localtime())+"\n";
 sqldump = sqldump+"-- SQLite Server version: "+sqlite3.sqlite_version+"\n";
 sqldump = sqldump+"-- PySQLite version: "+sqlite3.version+"\n";
 sqldump = sqldump+"-- Python Version: "+str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2])+"\n";
 sqldump = sqldump+"--\n";
 sqldump = sqldump+"-- Database: "+sdbfile+"\n";
 sqldump = sqldump+"--\n\n";
 sqldump = sqldump+"-- --------------------------------------------------------\n\n";
 if(verbose):
  VerbosePrintOut("-- "+__program_name__+" SQL Dumper");
  VerbosePrintOut("-- version "+__version__+"");
  VerbosePrintOut("-- "+__project_url__+"");
  VerbosePrintOut("--");
  VerbosePrintOut("-- Generation Time: "+time.strftime("%B %d, %Y at %I:%M %p", time.localtime())+"");
  VerbosePrintOut("-- SQLite Server version: "+sqlite3.sqlite_version+"");
  VerbosePrintOut("-- PySQLite version: "+sqlite3.version+"");
  VerbosePrintOut("-- Python Version: "+str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2])+"");
  VerbosePrintOut("--");
  VerbosePrintOut("-- Database: "+sdbfile);
  VerbosePrintOut("--");
  VerbosePrintOut("-- --------------------------------------------------------");
  VerbosePrintOut(" ");
 for get_cur_tab in table_list:
  sqldump = sqldump+"--\n";
  sqldump = sqldump+"-- Table structure for table "+str(get_cur_tab)+"\n";
  sqldump = sqldump+"--\n\n";
  if(verbose):
   VerbosePrintOut(" ");
   VerbosePrintOut("--");
   VerbosePrintOut("-- Table structure for table "+str(get_cur_tab)+"");
   VerbosePrintOut("--");
   VerbosePrintOut(" ");
  sqldump = sqldump+"DROP TABLE IF EXISTS "+get_cur_tab+"\n\n";
  if(verbose):
   VerbosePrintOut("DROP TABLE IF EXISTS "+get_cur_tab+"\n");
  sqldump = sqldump+"CREATE TEMP TABLE "+get_cur_tab+" (\n";
  if(verbose):
   VerbosePrintOut("CREATE TEMP TABLE "+get_cur_tab+" (");
  rowlen = len(inhockeyarray[get_cur_tab]['rows']);
  rowi = 0;
  sqlrowlist = [];
  for rowinfo in inhockeyarray[get_cur_tab]['rows']:
   sqlrowline = inhockeyarray[get_cur_tab][rowinfo]['info']['Name']+" "+inhockeyarray[get_cur_tab][rowinfo]['info']['Type'];
   if(inhockeyarray[get_cur_tab][rowinfo]['info']['NotNull']==1):
    sqlrowline = sqlrowline+" NOT NULL";
   if(inhockeyarray[get_cur_tab][rowinfo]['info']['DefualtValue'] is not None):
    sqlrowline = sqlrowline+" "+inhockeyarray[get_cur_tab][rowinfo]['info']['DefualtValue'];
   if(inhockeyarray[get_cur_tab][rowinfo]['info']['PrimaryKey']==1):
    sqlrowline = sqlrowline+" PRIMARY KEY";
   if(inhockeyarray[get_cur_tab][rowinfo]['info']['AutoIncrement']==1):
    sqlrowline = sqlrowline+" AUTOINCREMENT";
   sqlrowlist.append(sqlrowline);
  sqldump = sqldump+str(',\n'.join(sqlrowlist))+"\n);\n\n";
  sqldump = sqldump+"--\n";
  sqldump = sqldump+"-- Dumping data for table "+str(get_cur_tab)+"\n";
  sqldump = sqldump+"--\n\n";
  if(verbose):
   VerbosePrintOut(str(',\n'.join(sqlrowlist))+"\n);\n");
   VerbosePrintOut(" ");
   VerbosePrintOut("--");
   VerbosePrintOut("-- Dumping data for table "+str(get_cur_tab)+"");
   VerbosePrintOut("--");
   VerbosePrintOut(" ");
  for rowvalues in inhockeyarray[get_cur_tab]['values']:
   rkeylist = [];
   rvaluelist = [];
   for rkey, rvalue in rowvalues.items():
    rkeylist.append(rkey);
    if(isinstance(rvalue, basestring)):
     rvalue = "\""+rvalue+"\"";
    rvaluelist.append(str(rvalue));
   sqldump = sqldump+"INSERT INTO "+str(get_cur_tab)+" ("+str(', '.join(rkeylist))+") VALUES\n";
   sqldump = sqldump+"("+str(', '.join(rvaluelist))+");\n";
   if(verbose):
    VerbosePrintOut("INSERT INTO "+str(get_cur_tab)+" ("+str(', '.join(rkeylist))+") VALUES");
    VerbosePrintOut("("+str(', '.join(rvaluelist))+");");
  sqldump = sqldump+"\n-- --------------------------------------------------------\n\n";
  if(verbose):
   VerbosePrintOut("-- --------------------------------------------------------");
   VerbosePrintOut(" ");
 return sqldump;

def MakeHockeySQLFileHockeySQLiteArray(inhockeyarray, sqlfile=None, returnsql=False, verbose=True):
 if(sqlfile is None):
  return False;
 sqlfp = open(sqlfile, "w+");
 sqlstring = MakeHockeySQLFromHockeySQLiteArray(inhockeyarray, os.path.splitext("sqlfile")[0]+".db3", verbose);
 sqlfp.write(sqlstring);
 sqlfp.close();
 if(returnsql):
  return sqlstring;
 if(not returnsql):
  return True;
 return True;
 