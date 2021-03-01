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

    $FileInfo: hockeyfunctions.py - Last Update: 1/15/2021 Ver. 0.5.0 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals;
import sqlite3, sys, os, re, time, pickle, marshal, platform, binascii, xml.dom.minidom;
from ftplib import FTP, FTP_TLS;
from base64 import b64encode;
from copy import copy, deepcopy;

try:
 import simplejson as json;
except ImportError:
 import json;

testparamiko = False;
try:
 import paramiko;
 testparamiko = True;
except ImportError:
 testparamiko = False;

testlxml = False;
try:
 from lxml import etree as cElementTree;
 testlxml = True;
except ImportError:
 try:
  import xml.etree.cElementTree as cElementTree;
  testlxml = False;
 except ImportError:
  import xml.etree.ElementTree as cElementTree;
  testlxml = False;

try:
 from urlparse import urlparse, urlunparse;
except ImportError:
 from urllib.parse import urlparse, urlunparse;

from .hockeydatabase import *;
from .hockeydwnload import *;
from .versioninfo import __author__, __copyright__, __credits__, __email__, __license__, __license_string__, __maintainer__, __program_name__, __program_alt_name__, __project__, __project_url__, __project_release_url__, __version__, __version_alt__, __version_date__, __version_date_alt__, __version_info__, __version_date_info__, __version_date__, __revision__, __revision_id__, __version_date_plusrc__, __status__, version_date, version_info;

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
 baseint.append(long);
 baseint.insert(0, int);
except NameError:
 baseint.append(int);
baseint = tuple(baseint);

teststringio = 0;
try:
 from io import BytesIO;
 from io import StringIO;
 teststringio = 3;
except ImportError:
 try:
  from cStringIO import StringIO as BytesIO;
  from cStringIO import StringIO;
  teststringio = 1;
 except ImportError:
  try:
   from StringIO import StringIO as BytesIO;
   from StringIO import StringIO;
   teststringio = 2;
  except ImportError:
   teststringio = 0;

def CheckCompressionType(infile, closefp=True):
 if(not hasattr(infile, "read")):
  filefp = open(infile, "rb");
 else:
  filefp = infile;
 filefp.seek(0, 0);
 prefp = filefp.read(2);
 filetype = False;
 if(prefp==binascii.unhexlify("1f8b")):
  filetype = "gzip";
 filefp.seek(0, 0);
 prefp = filefp.read(3);
 if(prefp==binascii.unhexlify("425a68")):
  filetype = "bzip2";
 filefp.seek(0, 0);
 prefp = filefp.read(7);
 if(prefp==binascii.unhexlify("fd377a585a0000")):
  filetype = "lzma";
 filefp.seek(0, 0);
 if(closefp):
  filefp.close();
 return filetype;

def UncompressFile(infile, mode="rb"):
 compresscheck = CheckCompressionType(infile, False);
 if(compresscheck=="gzip"):
  try:
   import gzip;
  except ImportError:
   return False;
  filefp = gzip.open(infile, mode);
 if(compresscheck=="bzip2"):
  try:
   import bz2;
  except ImportError:
   return False;
  filefp = bz2.open(infile, mode);
 if(compresscheck=="lzma"):
  try:
   import lzma;
  except ImportError:
   return False;
  filefp = lzma.open(infile, mode);
 if(not compresscheck):
  filefp = open(infile, mode);
 return filefp;

def UncompressFileAlt(fp):
 if(not hasattr(fp, "read")):
  return False;
 compresscheck = CheckCompressionType(fp, False);
 if(compresscheck=="gzip"):
  try:
   import gzip;
  except ImportError:
   return False;
  outfp = gzip.GzipFile(fileobj=fp, mode="rb");
 if(compresscheck=="bzip2"):
  try:
   import bz2;
  except ImportError:
   return False;
  outfp = BytesIO();
  outfp.write(bz2.decompress(fp.read()));
 if(compresscheck=="lzma"):
  try:
   import lzma;
  except ImportError:
   return False;
  outfp = BytesIO();
  outfp.write(lzma.decompress(fp.read()));
 if(not compresscheck):
  outfp = fp;
 return outfp;

def download_file_from_ftp_file(url):
 urlparts = urlparse.urlparse(url);
 file_name = os.path.basename(urlparts.path);
 file_dir = os.path.dirname(urlparts.path);
 if(urlparts.username is not None):
  ftp_username = urlparts.username;
 else:
  ftp_username = "anonymous";
 if(urlparts.password is not None):
  ftp_password = urlparts.password;
 elif(urlparts.password is None and urlparts.username=="anonymous"):
  ftp_password = "anonymous";
 else:
  ftp_password = "";
 if(urlparts.scheme=="ftp"):
  ftp = FTP();
 elif(urlparts.scheme=="ftps"):
  ftp = FTP_TLS();
 else:
  return False;
 ftp.connect(urlparts.hostname, urlparts.port);
 ftp.login(urlparts.username, urlparts.password);
 if(urlparts.scheme=="ftps"):
  ftp.prot_p();
 ftpfile = BytesIO();
 ftp.retrbinary("RETR "+urlparts.path, ftpfile.write);
 #ftp.storbinary("STOR "+urlparts.path, ftpfile.write);
 ftp.close();
 ftpfile.seek(0, 0);
 return ftpfile;

def download_file_from_ftp_string(url):
 ftpfile = download_file_from_ftp_file(url);
 return ftpfile.read();

if(testparamiko):
 def download_file_from_sftp_file(url):
  urlparts = urlparse.urlparse(url);
  file_name = os.path.basename(urlparts.path);
  file_dir = os.path.dirname(urlparts.path);
  sftp_port = urlparts.port;
  if(urlparts.port is None):
   sftp_port = 22;
  else:
   sftp_port = urlparts.port;
  if(urlparts.username is not None):
   sftp_username = urlparts.username;
  else:
   sftp_username = "anonymous";
  if(urlparts.password is not None):
   sftp_password = urlparts.password;
  elif(urlparts.password is None and urlparts.username=="anonymous"):
   sftp_password = "anonymous";
  else:
   sftp_password = "";
  if(urlparts.scheme!="sftp"):
   return False;
  ssh = paramiko.SSHClient();
  ssh.load_system_host_keys();
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy());
  try:
   ssh.connect(urlparts.hostname, port=sftp_port, username=urlparts.username, password=urlparts.password);
  except paramiko.ssh_exception.SSHException:
   return False;
  sftp = ssh.open_sftp();
  sftpfile = BytesIO();
  sftp.getfo(urlparts.path, sftpfile);
  sftp.close();
  ssh.close();
  sftpfile.seek(0, 0);
  return sftpfile;
else:
 def download_file_from_sftp_file(url):
  return False;

if(testparamiko):
 def download_file_from_sftp_string(url):
  sftpfile = download_file_from_sftp_file(url);
  return sftpfile.read();
else:
 def download_file_from_ftp_string(url):
  return False;

def UncompressFileURL(inurl, inheaders, incookiejar):
 inheadersc = deepcopy(inheaders);
 if(re.findall("^(http|https)\:\/\/", inurl)):
  inurlcheck = urlparse(inurl);
  if(inurlcheck.username is not None or inurlcheck.password is not None):
   inurlencode = b64encode(str(inurlcheck.username+":"+inurlcheck.password).encode()).decode("UTF-8");
   inheadersc.update( { 'Authorization': "Basic "+inurlencode } );
   inurlfix = list(urlparse(inurl));
   inurlfix[1] = inurlcheck.hostname;
   inurl = urlunparse(inurlfix);
  inbfile = BytesIO(download_from_url(inurl, inheadersc, incookiejar)['Content']);
  inufile = UncompressFileAlt(inbfile);
 elif(re.findall("^(ftp|ftps)\:\/\/", inurl)):
  inbfile = BytesIO(download_file_from_ftp_string(inurl));
  inufile = UncompressFileAlt(inbfile);
 elif(re.findall("^(sftp)\:\/\/", inurl) and testparamiko):
  inbfile = BytesIO(download_file_from_sftp_string(inurl));
  inufile = UncompressFileAlt(inbfile);
 else:
  return False;
 return inufile;

def CompressFile(fp, compression="auto"):
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 if(not hasattr(fp, "read")):
  return False;
 fp.seek(0, 0);
 if(not compression or compression):
  compression = None;
 if(compression not in compressionlist and compression is None):
  compression = "auto";
 if(compression=="gzip"):
  try:
   import gzip;
  except ImportError:
   return False;
  infp = BytesIO();
  infp.write(GZipCompress(fp.read(), compresslevel=9));
 if(compression=="bzip2"):
  try:
   import bz2;
  except ImportError:
   return False;
  infp = BytesIO();
  infp.write(bz2.compress(fp.read(), compresslevel=9));
 if(compression=="lzma"):
  try:
   import lzma;
  except ImportError:
   return False;
  infp = BytesIO();
  infp.write(lzma.compress(fp.read(), format=lzma.FORMAT_ALONE, preset=9));
 if(compression=="xz"):
  try:
   import lzma;
  except ImportError:
   return False;
  infp = BytesIO();
  infp.write(lzma.compress(fp.read(), format=lzma.FORMAT_XZ, preset=9));
 if(compression=="auto" or compression is None):
  infp = fp;
 infp.seek(0, 0);
 return infp;

def CompressOpenFile(outfile):
 if(outfile is None):
  return False;
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outfile)[0];
 fextname = os.path.splitext(outfile)[1];
 if(fextname not in outextlistwd):
  outfp = open(outfile, "w+");
 elif(fextname==".gz"):
  try:
   import gzip;
  except ImportError:
   return False;
  outfp = gzip.open(outfile, "w+b", 9);
 elif(fextname==".bz2"):
  try:
   import bz2;
  except ImportError:
   return False;
  outfp = bz2.open(outfile, "w+b", 9);
 elif(fextname==".xz"):
  try:
   import lzma;
  except ImportError:
   return False;
  outfp = lzma.open(outfile, "w+b", format=lzma.FORMAT_XZ, preset=9);
 elif(fextname==".lzma"):
  try:
   import lzma;
  except ImportError:
   return False;
  outfp = lzma.open(outfile, "w+b", format=lzma.FORMAT_ALONE, preset=9);
 return outfp;

def MakeFileFromString(instringfile, stringisfile, outstringfile, returnstring=False):
 if(stringisfile and ((os.path.exists(instringfile) and os.path.isfile(instringfile)) or re.findall("^(http|https|ftp|ftps|sftp)\:\/\/", instringfile))):
  if(re.findall("^(http|https|ftp|ftps|sftp)\:\/\/", instringfile)):
   stringfile = UncompressFileURL(instringfile, geturls_headers, geturls_cj);
  else:
   instringsfile = open(instringfile, "rb");
   stringfile = UncompressFileAlt(instringsfile);
 elif(not stringisfile):
  instringsfile = BytesIO(instringfile.encode());
  stringfile = UncompressFileAlt(instringsfile);
 else:
  return False;
 stringstring = stringfile.read().decode("UTF-8");
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outstringfile)[0];
 fextname = os.path.splitext(outstringfile)[1];
 stringfp = CompressOpenFile(outstringfile);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  stringstring = stringstring.encode();
 stringfp.write(stringstring);
 stringfp.close();
 if(returnstring):
  return stringstring;
 if(not returnstring):
  return True;
 return True;

def MakeHockeyFileFromHockeyString(instringfile, stringisfile, outstringfile, returnstring=False):
 return MakeFileFromString(instringfile, stringisfile, outstringfile, returnstring);

def CheckXMLFile(infile):
 xmlfp = open(infile, "rb");
 xmlfp = UncompressFileAlt(xmlfp);
 xmlfp.seek(0, 0);
 prefp = xmlfp.read(6);
 validxmlfile = False;
 if(prefp==binascii.unhexlify("3c3f786d6c20")):
  validxmlfile = True;
 xmlfp.close();
 return validxmlfile;

# From https://stackoverflow.com/a/16919069
def RemoveBlanks(node):
 for x in node.childNodes:
  if(x.nodeType == xml.dom.minidom.Node.TEXT_NODE):
   if(x.nodeValue):
    x.nodeValue = x.nodeValue.strip();
  elif(x.nodeType == xml.dom.minidom.Node.ELEMENT_NODE):
   RemoveBlanks(x);
 return True;

def BeautifyXMLCode(inxmlfile, xmlisfile=True, indent="\t", newl="\n", encoding="UTF-8", beautify=True):
 if(xmlisfile and ((os.path.exists(inxmlfile) and os.path.isfile(inxmlfile)) or re.findall("^(http|https|ftp|ftps|sftp)\:\/\/", inxmlfile))):
  try:
   if(re.findall("^(http|https|ftp|ftps|sftp)\:\/\/", inxmlfile)):
    inxmlfile = UncompressFileURL(inxmlfile, geturls_headers, geturls_cj);
    xmldom = xml.dom.minidom.parse(file=inxmlfile);
   else:
    xmldom = xml.dom.minidom.parse(file=UncompressFile(inxmlfile));
  except: 
   return False;
 elif(not xmlisfile):
  inxmlsfile = BytesIO(inxmlfile.encode());
  inxmlfile = UncompressFileAlt(inxmlsfile);
  try:
   xmldom = xml.dom.minidom.parse(file=inxmlfile);
  except: 
   return False;
 else:
  return False;
 RemoveBlanks(xmldom);
 xmldom.normalize();
 if(beautify):
  outxmlcode = xmldom.toprettyxml(indent, newl, encoding).decode(encoding);
 else:
  outxmlcode = xmldom.toxml(encoding).decode(encoding);
 xmldom.unlink();
 return outxmlcode;

def BeautifyXMLCodeToFile(inxmlfile, outxmlfile, xmlisfile=True, indent="\t", newl="\n", encoding="UTF-8", beautify=True, returnxml=False):
 if(outxmlfile is None):
  return False;
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outxmlfile)[0];
 fextname = os.path.splitext(outxmlfile)[1];
 xmlfp = CompressOpenFile(outxmlfile);
 xmlstring = BeautifyXMLCode(inxmlfile, xmlisfile, indent, newl, encoding, beautify);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  xmlstring = xmlstring.encode();
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml):
  return xmlstring;
 if(not returnxml):
  return True;
 return True;

def CheckKeyInArray(validkeys, checkdict):
 ivalidkeys = 0;
 ilvalidkeys = len(validkeys);
 while(ivalidkeys<ilvalidkeys):
  if(validkeys[ivalidkeys] not in checkdict):
   return False;
  ivalidkeys = ivalidkeys + 1;
 return True;

def CheckHockeyXML(inxmlfile, xmlisfile=True):
 if(xmlisfile and ((os.path.exists(inxmlfile) and os.path.isfile(inxmlfile)) or re.findall("^(http|https|ftp|ftps|sftp)\:\/\/", inxmlfile))):
  try:
   if(re.findall("^(http|https|ftp|ftps|sftp)\:\/\/", inxmlfile)):
    inxmlfile = UncompressFileURL(inxmlfile, geturls_headers, geturls_cj);
    try:
     hockeyfile = cElementTree.ElementTree(file=inxmlfile);
    except cElementTree.ParseError: 
     return False;
   else:
    hockeyfile = cElementTree.ElementTree(file=UncompressFile(inxmlfile));
  except cElementTree.ParseError: 
   return False;
 elif(not xmlisfile):
  inxmlsfile = BytesIO(inxmlfile.encode());
  inxmlfile = UncompressFileAlt(inxmlsfile);
  try:
   hockeyfile = cElementTree.ElementTree(file=inxmlsfile);
  except cElementTree.ParseError: 
   return False;
 else:
  return False;
 hockeyroot = hockeyfile.getroot();
 if(hockeyroot.tag=="hockey"):
  if("database" not in hockeyroot.attrib):
   return False;
  leaguelist = [];
  for hockeyleague in hockeyroot:
   if(hockeyleague.tag=="league"):
    if(not CheckKeyInArray(["name", "fullname", "country", "fullcountry", "date", "playofffmt", "ordertype", "conferences", "divisions"], dict(hockeyleague.attrib))):
     return False;
    if(hockeyleague.attrib['name'] in leaguelist):
     return False;
    leaguelist.append(hockeyleague.attrib['name']);
    for hockeyconference in hockeyleague:
     if(hockeyconference.tag=="conference"):
      if(not CheckKeyInArray(["name", "prefix", "suffix"], dict(hockeyconference.attrib))):
       return False;
      for hockeydivision in hockeyconference:
       if(hockeydivision.tag=="division"):
        if(not CheckKeyInArray(["name", "prefix", "suffix"], dict(hockeydivision.attrib))):
         return False;
        for hockeyteam in hockeydivision:
         if(hockeyteam.tag=="team"):
          if(not CheckKeyInArray(["city", "area", "fullarea", "country", "fullcountry", "name", "arena", "affiliates", "prefix", "suffix"], dict(hockeyteam.attrib))):
           return False;
         else:
          return False;
       else:
        return False;
     elif(hockeyconference.tag=="arenas"):
      for hockeyarenas in hockeyconference:
       if(hockeyarenas.tag=="arena"):
        if(not CheckKeyInArray(["city", "area", "fullarea", "country", "fullcountry", "name"], dict(hockeyarenas.attrib))):
         return False;
       else:
        return False;
     elif(hockeyconference.tag=="games"):
      for hockeygames in hockeyconference:
       if(hockeygames.tag=="game"):
        if(not CheckKeyInArray(["date", "time", "hometeam", "awayteam", "goals", "sogs", "ppgs", "shgs", "penalties", "pims", "hits", "takeaways", "faceoffwins", "atarena", "isplayoffgame"], dict(hockeygames.attrib))):
         return False;
       else:
        return False;
     else:
      return False;
 else:
  return False;
 return True;

def CheckHockeySQLiteXML(inxmlfile, xmlisfile=True):
 if(xmlisfile and ((os.path.exists(inxmlfile) and os.path.isfile(inxmlfile)) or re.findall("^(http|https|ftp|ftps|sftp)\:\/\/", inxmlfile))):
  try:
   if(re.findall("^(http|https|ftp|ftps|sftp)\:\/\/", inxmlfile)):
    inxmlfile = UncompressFileURL(inxmlfile, geturls_headers, geturls_cj);
    try:
     hockeyfile = cElementTree.ElementTree(file=inxmlfile);
    except cElementTree.ParseError: 
     return False;
   else:
    hockeyfile = cElementTree.ElementTree(file=UncompressFile(inxmlfile));
  except cElementTree.ParseError: 
   return False;
 elif(not xmlisfile):
  inxmlsfile = BytesIO(inxmlfile.encode());
  inxmlfile = UncompressFileAlt(inxmlsfile);
  try:
   hockeyfile = cElementTree.ElementTree(file=inxmlsfile);
  except cElementTree.ParseError: 
   return False;
 else:
  return False;
 hockeyroot = hockeyfile.getroot();
 leaguelist = [];
 tablelist = [];
 if(hockeyroot.tag=="hockeydb"):
  if("database" not in hockeyroot.attrib):
   return False;
  for hockeytable in hockeyroot:
   if(hockeytable.tag=="table"):
    if(not CheckKeyInArray(["name"], dict(hockeytable.attrib))):
     return False;
    tablelist.append(hockeytable.attrib['name']);
    for hockeycolumn in hockeytable:
     if(hockeycolumn.tag=="column"):
      for hockeyrowinfo in hockeycolumn:
       if(hockeyrowinfo.tag=="rowinfo"):
        if(not CheckKeyInArray(["id", "name", "type", "notnull", "defaultvalue", "primarykey", "autoincrement", "hidden"], dict(hockeyrowinfo.attrib))):
         return False;
       else:
        return False;
     elif(hockeycolumn.tag=="data"):
      for hockeydata in hockeycolumn:
       if(hockeydata.tag=="row"):
        if(not CheckKeyInArray(["id"], dict(hockeydata.attrib))):
         return False;
        for rowdata in hockeydata:
         if(rowdata.tag=="rowdata"):
          if(not CheckKeyInArray(["name", "value"], dict(rowdata.attrib))):
           return False;
          if(hockeytable.attrib['name']=="HockeyLeagues" and rowdata.attrib['name']=="LeagueName"):
           if(rowdata.attrib['value'] in leaguelist):
            return False;
           leaguelist.append(rowdata.attrib['value']);
         else:
          return False;
       else:
        return False;
     elif(hockeycolumn.tag=="rows"):
      for hockeyrows in hockeycolumn:
       if(hockeyrows.tag=="rowlist"):
        if(not CheckKeyInArray(["name"], dict(hockeyrows.attrib))):
         return False;
       else:
        return False;
     else:
      return False;
 else:
  return False;
 #all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games", "PlayoffTeams"];
 all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games"];
 table_list = ['HockeyLeagues'];
 for leagueinfo_tmp in leaguelist:
  for cur_tab in all_table_list:
   table_list.append(leagueinfo_tmp+cur_tab);
 for get_cur_tab in table_list:
  if get_cur_tab not in tablelist:
   return False;
 return True;

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

def MakeHockeyJSONFromHockeyArray(inhockeyarray, jsonindent=1, verbose=True, jsonverbose=True):
 if(not CheckHockeyArray(inhockeyarray) and not CheckHockeySQLiteArray(inhockeyarray)):
  return False;
 jsonstring = json.dumps(inhockeyarray, indent=jsonindent);
 if(verbose and jsonverbose):
  VerbosePrintOut(jsonstring);
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 return jsonstring;

def MakeHockeyJSONFileFromHockeyArray(inhockeyarray, outjsonfile=None, returnjson=False, jsonindent=1, verbose=True, jsonverbose=True):
 if(outjsonfile is None):
  return False;
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outjsonfile)[0];
 fextname = os.path.splitext(outjsonfile)[1];
 jsonfp = CompressOpenFile(outjsonfile);
 jsonstring = MakeHockeyJSONFromHockeyArray(inhockeyarray, jsonindent, verbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  jsonstring = jsonstring.encode();
 jsonfp.write(jsonstring);
 jsonfp.close();
 if(returnjson):
  return jsonstring;
 if(not returnjson):
  return True;
 return True;

def MakeHockeyArrayFromHockeyJSON(injsonfile, jsonisfile=True, verbose=True, jsonverbose=True):
 if(jsonisfile and ((os.path.exists(injsonfile) and os.path.isfile(injsonfile)) or re.findall("^(http|https|ftp|ftps|sftp)\:\/\/", injsonfile))):
  if(re.findall("^(http|https|ftp|ftps|sftp)\:\/\/", injsonfile)):
   injsonfile = UncompressFileURL(injsonfile, geturls_headers, geturls_cj);
   try:
    hockeyarray = json.load(injsonfile);
   except json.JSONDecodeError:
    return False;
  else:
   jsonfp = UncompressFile(injsonfile);
   hockeyarray = json.load(jsonfp);
   jsonfp.close();
 elif(not jsonisfile):
   jsonfp = BytesIO(injsonfile.encode());
   jsonfp = UncompressFileAlt(jsonfp);
   hockeyarray = json.load(jsonfp);
   jsonfp.close();
 else:
  return False;
 if(not CheckHockeyArray(hockeyarray) and not CheckHockeySQLiteArray(hockeyarray)):
  return False;
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(hockeyarray, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(hockeyarray, verbose=False, jsonverbose=True));
 return hockeyarray;

def MakeHockeyPickleFromHockeyArray(inhockeyarray, verbose=True, jsonverbose=True):
 if(not CheckHockeyArray(inhockeyarray) and not CheckHockeySQLiteArray(inhockeyarray)):
  return False;
 picklestring = pickle.dumps(inhockeyarray);
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 return picklestring;

def MakeHockeyPickleFileFromHockeyArray(inhockeyarray, outpicklefile=None, returnpickle=False, verbose=True, jsonverbose=True):
 if(outpicklefile is None):
  return False;
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outpicklefile)[0];
 fextname = os.path.splitext(outpicklefile)[1];
 picklefp = CompressOpenFile(outpicklefile);
 picklestring = MakeHockeyPickleFromHockeyArray(inhockeyarray, verbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  picklestring = picklestring.encode();
 picklefp.write(picklestring);
 picklefp.close();
 if(returnpickle):
  return picklestring;
 if(not returnpickle):
  return True;
 return True;

def MakeHockeyArrayFromHockeyPickle(inpicklefile, pickleisfile=True, verbose=True, jsonverbose=True):
 if(pickleisfile and ((os.path.exists(inpicklefile) and os.path.isfile(inpicklefile)) or re.findall("^(http|https|ftp|ftps|sftp)\:\/\/", inpicklefile))):
  if(re.findall("^(http|https|ftp|ftps|sftp)\:\/\/", inpicklefile)):
   inpicklefile = UncompressFileURL(inpicklefile, geturls_headers, geturls_cj);
   hockeyarray = pickle.load(urllib2.urlopen(urllib2.Request(inpicklefile, None, geturls_headers)));
  else:
   picklefp = UncompressFile(inpicklefile);
   hockeyarray = pickle.load(picklefp);
   picklefp.close();
 elif(not pickleisfile):
  picklefp = BytesIO(inpicklefile.encode());
  picklefp = UncompressFileAlt(picklefp);
  hockeyarray = json.load(picklefp);
  picklefp.close();
 else:
  return False;
 if(not CheckHockeyArray(hockeyarray) and not CheckHockeySQLiteArray(hockeyarray)):
  return False;
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(hockeyarray, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(hockeyarray, verbose=False, jsonverbose=True));
 return hockeyarray;

def MakeHockeyMarshalFromHockeyArray(inhockeyarray, verbose=True, jsonverbose=True):
 if(not CheckHockeyArray(inhockeyarray) and not CheckHockeySQLiteArray(inhockeyarray)):
  return False;
 marshalstring = marshal.dumps(inhockeyarray);
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 return marshalstring;

def MakeHockeyMarshalFileFromHockeyArray(inhockeyarray, outmarshalfile=None, returnmarshal=False, verbose=True, jsonverbose=True):
 if(outmarshalfile is None):
  return False;
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outmarshalfile)[0];
 fextname = os.path.splitext(outmarshalfile)[1];
 marshalfp = CompressOpenFile(outmarshalfile);
 marshalstring = MakeHockeyMarshalFromHockeyArray(inhockeyarray, verbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  marshalstring = marshalstring.encode();
 marshalfp.write(marshalstring);
 marshalfp.close();
 if(returnmarshal):
  return marshalstring;
 if(not returnmarshal):
  return True;
 return True;

def MakeHockeyArrayFromHockeyMarshal(inmarshalfile, marshalisfile=True, verbose=True, jsonverbose=True):
 if(marshalisfile and ((os.path.exists(inmarshalfile) and os.path.isfile(inmarshalfile)) or re.findall("^(http|https|ftp|ftps|sftp)\:\/\/", inmarshalfile))):
  if(re.findall("^(http|https|ftp|ftps|sftp)\:\/\/", inmarshalfile)):
   inmarshalfile = UncompressFileURL(inmarshalfile, geturls_headers, geturls_cj);
   hockeyarray = marshal.load(urllib2.urlopen(urllib2.Request(inmarshalfile, None, geturls_headers)));
  else:
   marshalfp = UncompressFile(inmarshalfile);
   hockeyarray = marshal.load(marshalfp);
   marshalfp.close();
 elif(not marshalisfile):
  marshalfp = BytesIO(inmarshalfile.encode());
  marshalfp = UncompressFileAlt(marshalfp);
  hockeyarray = json.load(marshalfp);
  marshalfp.close();
 else:
  return False;
 if(not CheckHockeyArray(hockeyarray) and not CheckHockeySQLiteArray(hockeyarray)):
  return False;
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(hockeyarray, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(hockeyarray, verbose=False, jsonverbose=True));
 return hockeyarray;

def MakeHockeyXMLFromHockeyArray(inhockeyarray, beautify=True, verbose=True, jsonverbose=True):
 if(not CheckHockeyArray(inhockeyarray)):
  return False;
 inchockeyarray = deepcopy(inhockeyarray);
 xmlstring = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
 if "database" in inchockeyarray.keys():
  xmlstring = xmlstring+"<hockey database=\""+EscapeXMLString(str(inchockeyarray['database']), quote=True)+"\">\n";
 if "database" not in inchockeyarray.keys():
  xmlstring = xmlstring+"<hockey database=\""+EscapeXMLString(str(defaultsdbfile))+"\">\n";
 for hlkey in inchockeyarray['leaguelist']:
  xmlstring = xmlstring+" <league name=\""+EscapeXMLString(str(hlkey), quote=True)+"\" fullname=\""+EscapeXMLString(str(inchockeyarray[hlkey]['leagueinfo']['fullname']), quote=True)+"\" country=\""+EscapeXMLString(str(inchockeyarray[hlkey]['leagueinfo']['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(inchockeyarray[hlkey]['leagueinfo']['fullcountry']), quote=True)+"\" date=\""+EscapeXMLString(str(inchockeyarray[hlkey]['leagueinfo']['date']), quote=True)+"\" playofffmt=\""+EscapeXMLString(str(inchockeyarray[hlkey]['leagueinfo']['playofffmt']), quote=True)+"\" ordertype=\""+EscapeXMLString(str(inchockeyarray[hlkey]['leagueinfo']['ordertype']), quote=True)+"\" conferences=\""+EscapeXMLString(str(inchockeyarray[hlkey]['leagueinfo']['conferences']), quote=True)+"\" divisions=\""+EscapeXMLString(str(inchockeyarray[hlkey]['leagueinfo']['divisions']), quote=True)+"\">\n";
  conferencecount = 0;
  conferenceend = len(inchockeyarray[hlkey]['conferencelist']);
  for hckey in inchockeyarray[hlkey]['conferencelist']:
   xmlstring = xmlstring+"  <conference name=\""+EscapeXMLString(str(hckey), quote=True)+"\" prefix=\""+EscapeXMLString(str(inchockeyarray[hlkey][hckey]['conferenceinfo']['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(inchockeyarray[hlkey][hckey]['conferenceinfo']['suffix']), quote=True)+"\">\n";
   for hdkey in inchockeyarray[hlkey][hckey]['divisionlist']:
    xmlstring = xmlstring+"   <division name=\""+EscapeXMLString(str(hdkey), quote=True)+"\" prefix=\""+EscapeXMLString(str(inchockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(inchockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix']), quote=True)+"\">\n";
    for htkey in inchockeyarray[hlkey][hckey][hdkey]['teamlist']:
     xmlstring = xmlstring+"    <team city=\""+EscapeXMLString(str(inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']), quote=True)+"\" area=\""+EscapeXMLString(str(inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(htkey), quote=True)+"\" arena=\""+EscapeXMLString(str(inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']), quote=True)+"\" prefix=\""+EscapeXMLString(str(inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']), quote=True)+"\" affiliates=\""+EscapeXMLString(str(inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['affiliates']), quote=True)+"\" />\n";
    xmlstring = xmlstring+"   </division>\n";
   xmlstring = xmlstring+"  </conference>\n";
   conferencecount = conferencecount + 1;
  if(conferencecount>=conferenceend):
   hasarenas = False;
   if(len(inchockeyarray[hlkey]['arenas'])>0):
    hasarenas = True;
    xmlstring = xmlstring+"  <arenas>\n";
   for hakey in inchockeyarray[hlkey]['arenas']:
    if(hakey):
     hasarenas = True;
     xmlstring = xmlstring+"   <arena city=\""+EscapeXMLString(str(hakey['city']), quote=True)+"\" area=\""+EscapeXMLString(str(hakey['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(hakey['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(hakey['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(hakey['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(hakey['name']), quote=True)+"\" />\n";
   if(hasarenas):
    xmlstring = xmlstring+"  </arenas>\n";
   hasgames = False;
   if(len(inchockeyarray[hlkey]['games'])>0):
    hasgames = True;
    xmlstring = xmlstring+"  <games>\n";
   for hgkey in inchockeyarray[hlkey]['games']:
    if(hgkey):
     hasgames = True;
     xmlstring = xmlstring+"   <game date=\""+EscapeXMLString(str(hgkey['date']), quote=True)+"\" hometeam=\""+EscapeXMLString(str(hgkey['hometeam']), quote=True)+"\" awayteam=\""+EscapeXMLString(str(hgkey['awayteam']), quote=True)+"\" goals=\""+EscapeXMLString(str(hgkey['goals']), quote=True)+"\" sogs=\""+EscapeXMLString(str(hgkey['sogs']), quote=True)+"\" ppgs=\""+EscapeXMLString(str(hgkey['ppgs']), quote=True)+"\" shgs=\""+EscapeXMLString(str(hgkey['shgs']), quote=True)+"\" penalties=\""+EscapeXMLString(str(hgkey['penalties']), quote=True)+"\" pims=\""+EscapeXMLString(str(hgkey['pims']), quote=True)+"\" hits=\""+EscapeXMLString(str(hgkey['hits']), quote=True)+"\" takeaways=\""+EscapeXMLString(str(hgkey['takeaways']), quote=True)+"\" faceoffwins=\""+EscapeXMLString(str(hgkey['faceoffwins']), quote=True)+"\" atarena=\""+EscapeXMLString(str(hgkey['atarena']), quote=True)+"\" isplayoffgame=\""+EscapeXMLString(str(hgkey['isplayoffgame']), quote=True)+"\" />\n";
   if(hasgames):
    xmlstring = xmlstring+"  </games>\n";
  xmlstring = xmlstring+" </league>\n";
 xmlstring = xmlstring+"</hockey>\n";
 xmlstring = BeautifyXMLCode(xmlstring, False, " ", "\n", "UTF-8", beautify);
 if(not CheckHockeyXML(xmlstring, False)):
  return False;
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(xmlstring);
 return xmlstring;

def MakeHockeyXMLFileFromHockeyArray(inhockeyarray, outxmlfile=None, returnxml=False, beautify=True, verbose=True, jsonverbose=True):
 if(outxmlfile is None):
  return False;
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outxmlfile)[0];
 fextname = os.path.splitext(outxmlfile)[1];
 xmlfp = CompressOpenFile(outxmlfile);
 xmlstring = MakeHockeyXMLFromHockeyArray(inhockeyarray, beautify, verbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  xmlstring = xmlstring.encode();
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml):
  return xmlstring;
 if(not returnxml):
  return True;
 return True;

def MakeHockeyXMLAltFromHockeyArray(inhockeyarray, beautify=True, verbose=True, jsonverbose=True):
 if(not CheckHockeyArray(inhockeyarray)):
  return False;
 inchockeyarray = deepcopy(inhockeyarray);
 if "database" in inchockeyarray.keys():
  xmlstring_hockey = cElementTree.Element("hockey", { 'database': str(inchockeyarray['database']) } );
 if "database" not in inchockeyarray.keys():
  xmlstring_hockey = cElementTree.Element("hockey", { 'database': str(defaultsdbfile) } );
 for hlkey in inchockeyarray['leaguelist']:
  xmlstring_league = cElementTree.SubElement(xmlstring_hockey, "league", { 'name': str(hlkey), 'fullname': str(inchockeyarray[hlkey]['leagueinfo']['fullname']), 'country': str(inchockeyarray[hlkey]['leagueinfo']['country']), 'fullcountry': str(inchockeyarray[hlkey]['leagueinfo']['fullcountry']), 'date': str(inchockeyarray[hlkey]['leagueinfo']['date']), 'playofffmt': str(inchockeyarray[hlkey]['leagueinfo']['playofffmt']), 'ordertype': str(inchockeyarray[hlkey]['leagueinfo']['ordertype']), 'conferences': str(inchockeyarray[hlkey]['leagueinfo']['conferences']), 'divisions': str(inchockeyarray[hlkey]['leagueinfo']['divisions']) } );
  conferencecount = 0;
  conferenceend = len(inchockeyarray[hlkey]['conferencelist']);
  for hckey in inchockeyarray[hlkey]['conferencelist']:
   xmlstring_conference = cElementTree.SubElement(xmlstring_league, "conference", { 'name': str(hckey), 'prefix': str(inchockeyarray[hlkey][hckey]['conferenceinfo']['prefix']), 'suffix': str(inchockeyarray[hlkey][hckey]['conferenceinfo']['suffix']) } );
   for hdkey in inchockeyarray[hlkey][hckey]['divisionlist']:
    xmlstring_division = cElementTree.SubElement(xmlstring_conference, "division", { 'name': str(hdkey), 'prefix': str(inchockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix']), 'suffix': str(inchockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix']) } );
    for htkey in inchockeyarray[hlkey][hckey][hdkey]['teamlist']:
     xmlstring_team = cElementTree.SubElement(xmlstring_division, "team", { 'city': str(inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']), 'area': str(inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']), 'fullarea': str(inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']), 'country': str(inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']), 'fullcountry': str(inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']), 'name': str(htkey), 'arena': str(inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']), 'prefix': str(inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']), 'suffix': str(inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']), 'affiliates': str(inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['affiliates']) } );
   conferencecount = conferencecount + 1;
  if(conferencecount>=conferenceend):
   hasarenas = False;
   if(len(inchockeyarray[hlkey]['arenas'])>0):
    hasarenas = True;
    xmlstring_arenas = cElementTree.SubElement(xmlstring_league, "arenas");
   for hakey in inchockeyarray[hlkey]['arenas']:
    if(hakey):
     hasarenas = True;
     xmlstring_arena = cElementTree.SubElement(xmlstring_arenas, "arena", { 'city': str(hakey['city']), 'area': str(hakey['area']), 'fullarea': str(hakey['fullarea']), 'country': str(hakey['country']), 'fullcountry': str(hakey['fullcountry']), 'name': str(htkey) } );
   hasgames = False;
   if(len(inchockeyarray[hlkey]['games'])>0):
    hasgames = True;
    xmlstring_games = cElementTree.SubElement(xmlstring_league, "games");
   for hgkey in inchockeyarray[hlkey]['games']:
    if(hgkey):
     hasgames = True;
     xmlstring_game = cElementTree.SubElement(xmlstring_games, "game", { 'date': str(hgkey['date']), 'hometeam': str(hgkey['hometeam']), 'awayteam': str(hgkey['awayteam']), 'goals': str(hgkey['goals']), 'sogs': str(hgkey['sogs']), 'ppgs': str(ppgs), 'shgs': str(hgkey['shgs']), 'penalties': str(hgkey['penalties']), 'pims': str(hgkey['pims']), 'hits': str(hgkey['hits']), 'takeaways': str(hgkey['takeaways']), 'faceoffwins': str(hgkey['faceoffwins']), 'atarena': str(hgkey['atarena']), 'isplayoffgame': str(hgkey['isplayoffgame']) } );
 '''xmlstring = cElementTree.tostring(xmlstring_hockey, "UTF-8", "xml", True, "xml", True).decode("UTF-8");'''
 if(testlxml):
  xmlstring = cElementTree.tostring(xmlstring_hockey, encoding="UTF-8", method="xml", xml_declaration=True, pretty_print=True).decode("UTF-8");
 else:
  try:
   xmlstring = cElementTree.tostring(xmlstring_hockey, encoding="UTF-8", method="xml", xml_declaration=True).decode("UTF-8");
  except TypeError:
   xmlstring = cElementTree.tostring(xmlstring_hockey, encoding="UTF-8", method="xml").decode("UTF-8");
 xmlstring = BeautifyXMLCode(xmlstring, False, " ", "\n", "UTF-8", beautify);
 if(not CheckHockeyXML(xmlstring, False)):
  return False;
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(xmlstring);
 return xmlstring;

def MakeHockeyXMLAltFileFromHockeyArray(inhockeyarray, outxmlfile=None, returnxml=False, beautify=True, verbose=True, jsonverbose=True):
 if(outxmlfile is None):
  return False;
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outxmlfile)[0];
 fextname = os.path.splitext(outxmlfile)[1];
 xmlfp = CompressOpenFile(outxmlfile);
 xmlstring = MakeHockeyXMLAltFromHockeyArray(inhockeyarray, beautify, verbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  xmlstring = xmlstring.encode();
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml):
  return xmlstring;
 if(not returnxml):
  return True;
 return True;

def MakeHockeyArrayFromHockeyXML(inxmlfile, xmlisfile=True, verbose=True, jsonverbose=True):
 if(not CheckHockeyXML(inxmlfile, xmlisfile)):
  return False;
 if(xmlisfile and ((os.path.exists(inxmlfile) and os.path.isfile(inxmlfile)) or re.findall("^(http|https|ftp|ftps|sftp)\:\/\/", inxmlfile))):
  try:
   if(re.findall("^(http|https|ftp|ftps|sftp)\:\/\/", inxmlfile)):
    inxmlfile = UncompressFileURL(inxmlfile, geturls_headers, geturls_cj);
    try:
     hockeyfile = cElementTree.ElementTree(file=inxmlfile);
    except cElementTree.ParseError: 
     return False;
   else:
    hockeyfile = cElementTree.ElementTree(file=UncompressFile(inxmlfile));
  except cElementTree.ParseError: 
   return False;
 elif(not xmlisfile):
  inxmlsfile = BytesIO(inxmlfile.encode());
  inxmlfile = UncompressFileAlt(inxmlsfile);
  try:
   hockeyfile = cElementTree.ElementTree(file=inxmlsfile);
  except cElementTree.ParseError: 
   return False;
 else:
  return False;
 gethockey = hockeyfile.getroot();
 leaguearrayout = { 'database': str(gethockey.attrib['database']) };
 leaguelist = [];
 for getleague in gethockey:
  leaguearray = {};
  arenalist = [];
  gamelist = [];
  if(getleague.tag=="league"):
   tempdict = { 'leagueinfo': { 'name': str(getleague.attrib['name']), 'fullname': str(getleague.attrib['fullname']), 'country': str(getleague.attrib['country']), 'fullcountry': str(getleague.attrib['fullcountry']), 'date': str(getleague.attrib['date']), 'playofffmt': str(getleague.attrib['playofffmt']), 'ordertype': str(getleague.attrib['ordertype']), 'conferences': str(getleague.attrib['conferences']), 'divisions': str(getleague.attrib['divisions']) }, 'quickinfo': {'conferenceinfo': {}, 'divisioninfo': {}, 'teaminfo': {} } };
   leaguearray.update( { str(getleague.attrib['name']): tempdict } );
   leaguelist.append(str(getleague.attrib['name']));
  if(getleague.tag == "league"):
   conferencelist = [];
   for getconference in getleague:
    if(getconference.tag == "conference"):
     ConferenceFullName = GetFullTeamName(str(getconference.attrib['name']), str(getconference.attrib['prefix']), str(getconference.attrib['suffix']));
     leaguearray[str(getleague.attrib['name'])].update( { str(getconference.attrib['name']): { 'conferenceinfo': { 'name': str(getconference.attrib['name']), 'prefix': str(getconference.attrib['prefix']), 'suffix': str(getconference.attrib['suffix']), 'fullname': str(ConferenceFullName), 'league': str(getleague.attrib['name']) } } } );
     leaguearray[str(getleague.attrib['name'])]['quickinfo']['conferenceinfo'].update( { str(getconference.attrib['name']): { 'name': str(getconference.attrib['name']), 'fullname': str(ConferenceFullName), 'league': str(getleague.attrib['name']) } } );
     conferencelist.append(str(getconference.attrib['name']));
    divisiondict = {};
    divisionlist = [];
    if(getconference.tag == "conference"):
     for getdivision in getconference:
      DivisionFullName = GetFullTeamName(str(getdivision.attrib['name']), str(getdivision.attrib['prefix']), str(getdivision.attrib['suffix']));
      leaguearray[str(getleague.attrib['name'])][str(getconference.attrib['name'])].update( { str(getdivision.attrib['name']): { 'divisioninfo': { 'name': str(getdivision.attrib['name']), 'prefix': str(getdivision.attrib['prefix']), 'suffix': str(getdivision.attrib['suffix']), 'fullname': str(DivisionFullName), 'league': str(getleague.attrib['name']), 'conference': str(getconference.attrib['name']) } } } );
      leaguearray[str(getleague.attrib['name'])]['quickinfo']['divisioninfo'].update( { str(getdivision.attrib['name']): { 'name': str(getdivision.attrib['name']), 'fullname': str(DivisionFullName), 'league': str(getleague.attrib['name']), 'conference': str(getconference.attrib['name']) } } );
      divisionlist.append(str(getdivision.attrib['name']));
      teamdist = {};
      teamlist = [];
      if(getdivision.tag == "division"):
       for getteam in getdivision:
        if(getteam.tag == "team"):
         fullteamname = GetFullTeamName(str(getteam.attrib['name']), str(getteam.attrib['prefix']), str(getteam.attrib['suffix']));
         leaguearray[str(getleague.attrib['name'])][str(getconference.attrib['name'])][str(getdivision.attrib['name'])].update( { str(getteam.attrib['name']): { 'teaminfo': { 'city': str(getteam.attrib['city']), 'area': str(getteam.attrib['area']), 'fullarea': str(getteam.attrib['fullarea']), 'country': str(getteam.attrib['country']), 'fullcountry': str(getteam.attrib['fullcountry']), 'name': str(getteam.attrib['name']), 'fullname': fullteamname, 'arena': str(getteam.attrib['arena']), 'prefix': str(getteam.attrib['prefix']), 'suffix': str(getteam.attrib['suffix']), 'league': str(getleague.attrib['name']), 'conference': str(getconference.attrib['name']), 'division': str(getdivision.attrib['name']), 'affiliates': str(getteam.attrib['affiliates']) } } } );
         leaguearray[str(getleague.attrib['name'])]['quickinfo']['teaminfo'].update( { str(getteam.attrib['name']): { 'name': str(getteam.attrib['name']), 'fullname': fullteamname, 'league': str(getleague.attrib['name']), 'conference': str(getconference.attrib['name']), 'division': str(getdivision.attrib['name']) } } );
         teamlist.append(str(getteam.attrib['name']));
       leaguearray[str(getleague.attrib['name'])][str(getconference.attrib['name'])][str(getdivision.attrib['name'])].update( { 'teamlist': teamlist } );
     leaguearray[str(getleague.attrib['name'])][str(getconference.attrib['name'])].update( { 'divisionlist': divisionlist } );
    if(getconference.tag == "arenas"):
     for getarenas in getconference:
      arenalist.append( { 'city': str(getarenas.attrib['city']), 'area': str(getarenas.attrib['area']), 'fullarea': str(getarenas.attrib['fullarea']), 'country': str(getarenas.attrib['country']), 'fullcountry': str(getarenas.attrib['fullcountry']), 'name': str(getarenas.attrib['name']) } );
    leaguearray[str(getleague.attrib['name'])].update( { "arenas": arenalist } );
    if(getconference.tag == "games"):
     for getgame in getconference:
      gamelist.append( { 'date': str(getgame.attrib['date']), 'time': str(getgame.attrib['time']), 'hometeam': str(getgame.attrib['hometeam']), 'awayteam': str(getgame.attrib['awayteam']), 'goals': str(getgame.attrib['goals']), 'sogs': str(getgame.attrib['sogs']), 'ppgs': str(getgame.attrib['ppgs']), 'shgs': str(getgame.attrib['shgs']), 'penalties': str(getgame.attrib['penalties']), 'pims': str(getgame.attrib['pims']), 'hits': str(getgame.attrib['hits']), 'takeaways': str(getgame.attrib['takeaways']), 'faceoffwins': str(getgame.attrib['faceoffwins']), 'atarena': str(getgame.attrib['atarena']), 'isplayoffgame': str(getgame.attrib['isplayoffgame']) } );
    leaguearray[str(getleague.attrib['name'])].update( { "games": gamelist } );
   leaguearray[str(getleague.attrib['name'])].update( { 'conferencelist': conferencelist } );
   leaguearrayout.update(leaguearray);
 leaguearrayout.update( { 'leaguelist': leaguelist } );
 if(not CheckHockeyArray(leaguearrayout)):
  return False;
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(leaguearrayout, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(leaguearrayout, verbose=False, jsonverbose=True));
 return leaguearrayout;

def MakeHockeyDatabaseFromHockeyArray(inhockeyarray, outsdbfile=None, returndb=False, verbose=True, jsonverbose=True):
 if(not CheckHockeyArray(inhockeyarray)):
  return False;
 inchockeyarray = deepcopy(inhockeyarray);
 if(outsdbfile is None and "database" in inchockeyarray.keys()):
  sqldatacon = MakeHockeyDatabase(inchockeyarray['database']);
 if(outsdbfile is None and "database" not in inchockeyarray.keys()):
  sqldatacon = MakeHockeyDatabase(":memory:");
 if(outsdbfile is not None and isinstance(outsdbfile, basestring)):
  sqldatacon = MakeHockeyDatabase(outsdbfile);
 if(outsdbfile is not None and isinstance(outsdbfile, (tuple, list))):
  sqldatacon = tuple(outsdbfile);
  outsdbfile = ":memory:";
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 leaguecount = 0;
 for hlkey in inchockeyarray['leaguelist']:
  if(leaguecount==0):
   MakeHockeyLeagueTable(sqldatacon);
  MakeHockeyTeamTable(sqldatacon, hlkey);
  MakeHockeyConferenceTable(sqldatacon, hlkey);
  MakeHockeyGameTable(sqldatacon, hlkey);
  MakeHockeyDivisionTable(sqldatacon, hlkey);
  HockeyLeagueHasConferences = True;
  if(inchockeyarray[hlkey]['leagueinfo']['conferences'].lower()=="no"):
   HockeyLeagueHasConferences = False;
  HockeyLeagueHasDivisions = True;
  if(inchockeyarray[hlkey]['leagueinfo']['divisions'].lower()=="no"):
   HockeyLeagueHasDivisions = False;
  MakeHockeyLeague(sqldatacon, hlkey, inchockeyarray[hlkey]['leagueinfo']['fullname'], inchockeyarray[hlkey]['leagueinfo']['country'], inchockeyarray[hlkey]['leagueinfo']['fullcountry'], inchockeyarray[hlkey]['leagueinfo']['date'], inchockeyarray[hlkey]['leagueinfo']['playofffmt'], inchockeyarray[hlkey]['leagueinfo']['ordertype']);
  leaguecount = leaguecount + 1;
  conferencecount = 0;
  conferenceend = len(inchockeyarray[hlkey]['conferencelist']);
  for hckey in inchockeyarray[hlkey]['conferencelist']:
   MakeHockeyConference(sqldatacon, hlkey, hckey, inchockeyarray[hlkey][hckey]['conferenceinfo']['prefix'], inchockeyarray[hlkey][hckey]['conferenceinfo']['suffix'], HockeyLeagueHasConferences);
   for hdkey in inchockeyarray[hlkey][hckey]['divisionlist']:
    MakeHockeyDivision(sqldatacon, hlkey, hdkey, hckey, inchockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix'], inchockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix'], HockeyLeagueHasConferences, HockeyLeagueHasDivisions);
    for htkey in inchockeyarray[hlkey][hckey][hdkey]['teamlist']:
     MakeHockeyTeam(sqldatacon, hlkey, str(inchockeyarray[hlkey]['leagueinfo']['date']), inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city'], inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area'], inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country'], inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry'], inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea'], htkey, inchockeyarray[hlkey][hckey]['conferenceinfo']['name'], inchockeyarray[hlkey][hckey][hdkey]['divisioninfo']['name'], inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena'], inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix'], inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix'], inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['affiliates'], HockeyLeagueHasConferences, HockeyLeagueHasDivisions);
   conferencecount = conferencecount + 1;
  if(conferencecount>=conferenceend):
   hasarenas = False;
   if(len(inchockeyarray[hlkey]['arenas'])>0):
    hasarenas = True;
   for hakey in inchockeyarray[hlkey]['arenas']:
    if(hakey):
     hasarenas = True;
     MakeHockeyArena(sqldatacon, hlkey, hakey['city'], hakey['area'], hakey['country'], hakey['fullcountry'], hakey['fullarea'], hakey['name']);
   hasgames = False;
   if(len(inchockeyarray[hlkey]['games'])>0):
    hasgames = True;
   for hgkey in inchockeyarray[hlkey]['games']:
    if(hgkey):
     hasgames = True;
     MakeHockeyGame(sqldatacon, hlkey, hgkey['date'], hgkey['time'], hgkey['hometeam'], hgkey['awayteam'], hgkey['goals'], hgkey['sogs'], hgkey['ppgs'], hgkey['shgs'], hgkey['penalties'], hgkey['pims'], hgkey['hits'], hgkey['takeaways'], hgkey['faceoffwins'], hgkey['atarena'], hgkey['isplayoffgame']);
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 if(not returndb):
  CloseHockeyDatabase(sqldatacon);
 if(returndb):
  return sqldatacon;
 if(not returndb):
  return True;
 return True;

def MakeHockeyPythonFromHockeyArray(inhockeyarray, verbose=True, jsonverbose=True):
 if(not CheckHockeyArray(inhockeyarray)):
  return False;
 inchockeyarray = deepcopy(inhockeyarray);
 pyfilename = __package__;
 if(pyfilename=="__main__"):
  pyfilename = os.path.splitext(os.path.basename(__file__))[0];
 pystring = "#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nfrom __future__ import absolute_import, division, print_function, unicode_literals;\nimport "+pyfilename+";\n\n";
 pystring = pystring+"sqldatacon = "+pyfilename+".MakeHockeyDatabase(\""+inchockeyarray['database']+"\");\n";
 pystring = pystring+pyfilename+".MakeHockeyLeagueTable(sqldatacon);\n";
 for hlkey in inchockeyarray['leaguelist']:
  HockeyLeagueHasConferences = True;
  if(inchockeyarray[hlkey]['leagueinfo']['conferences'].lower()=="no"):
   HockeyLeagueHasConferences = False;
  HockeyLeagueHasDivisions = True;
  if(inchockeyarray[hlkey]['leagueinfo']['divisions'].lower()=="no"):
   HockeyLeagueHasDivisions = False;
  pystring = pystring+pyfilename+".MakeHockeyTeamTable(sqldatacon, \""+hlkey+"\");\n"+pyfilename+".MakeHockeyConferenceTable(sqldatacon, \""+hlkey+"\");\n"+pyfilename+".MakeHockeyGameTable(sqldatacon, \""+hlkey+"\");\n"+pyfilename+".MakeHockeyDivisionTable(sqldatacon, \""+hlkey+"\");\n"+pyfilename+".MakeHockeyLeague(sqldatacon, \""+hlkey+"\", \""+inchockeyarray[hlkey]['leagueinfo']['fullname']+"\", \""+inchockeyarray[hlkey]['leagueinfo']['country']+"\", \""+inchockeyarray[hlkey]['leagueinfo']['fullcountry']+"\", \""+inchockeyarray[hlkey]['leagueinfo']['date']+"\", \""+inchockeyarray[hlkey]['leagueinfo']['playofffmt']+"\", \""+inchockeyarray[hlkey]['leagueinfo']['ordertype']+"\");\n";
  conferencecount = 0;
  conferenceend = len(inchockeyarray[hlkey]['conferencelist']);
  for hckey in inchockeyarray[hlkey]['conferencelist']:
   pystring = pystring+pyfilename+".MakeHockeyConference(sqldatacon, \""+hlkey+"\", \""+hckey+"\", \""+inchockeyarray[hlkey][hckey]['conferenceinfo']['prefix']+"\", \""+inchockeyarray[hlkey][hckey]['conferenceinfo']['suffix']+"\", "+str(HockeyLeagueHasConferences)+");\n";
   for hdkey in inchockeyarray[hlkey][hckey]['divisionlist']:
    pystring = pystring+pyfilename+".MakeHockeyDivision(sqldatacon, \""+hlkey+"\", \""+hdkey+"\", \""+hckey+"\", \""+inchockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix']+"\", \""+inchockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");\n";
    for htkey in inchockeyarray[hlkey][hckey][hdkey]['teamlist']:
     pystring = pystring+pyfilename+".MakeHockeyTeam(sqldatacon, \""+hlkey+"\", \""+str(inchockeyarray[hlkey]['leagueinfo']['date'])+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']+"\", \""+htkey+"\", \""+hckey+"\", \""+hdkey+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['affiliates']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");\n";
   conferencecount = conferencecount + 1;
  if(conferencecount>=conferenceend):
   hasarenas = False;
   if(len(inchockeyarray[hlkey]['arenas'])>0):
    hasarenas = True;
   for hakey in inchockeyarray[hlkey]['arenas']:
    if(hakey):
     hasarenas = True;
     pystring = pystring+pyfilename+".MakeHockeyArena(sqldatacon, \""+hlkey+"\", \""+hakey['city']+"\", \""+hakey['area']+"\", \""+hakey['country']+"\", \""+hakey['fullcountry']+"\", \""+hakey['fullarea']+"\", \""+hakey['name']+"\");\n";
   hasgames = False;
   if(len(inchockeyarray[hlkey]['games'])>0):
    hasgames = True;
   for hgkey in inchockeyarray[hlkey]['games']:
    if(hgkey):
     hasgames = True;
     pystring = pystring+pyfilename+".MakeHockeyGame(sqldatacon, \""+hlkey+"\", "+hgkey['date']+", "+hgkey['time']+", \""+hgkey['hometeam']+"\", \""+hgkey['awayteam']+"\", \""+hgkey['goals']+"\", \""+hgkey['sogs']+"\", \""+hgkey['ppgs']+"\", \""+hgkey['shgs']+"\", \""+hgkey['penalties']+"\", \""+hgkey['pims']+"\", \""+hgkey['hits']+"\", \""+hgkey['takeaways']+"\", \""+hgkey['faceoffwins']+"\", \""+hgkey['atarena']+"\", \""+hgkey['isplayoffgame']+"\");\n";
 pystring = pystring+"\n";
 pystring = pystring+pyfilename+".CloseHockeyDatabase(sqldatacon);\n";
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 return pystring;

def MakeHockeyPythonFileFromHockeyArray(inhockeyarray, outpyfile=None, returnpy=False, verbose=True, jsonverbose=True):
 if(outpyfile is None):
  return False;
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outpyfile)[0];
 fextname = os.path.splitext(outpyfile)[1];
 pyfp = CompressOpenFile(outpyfile);
 pystring = MakeHockeyPythonFromHockeyArray(inhockeyarray, verbose);
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

def MakeHockeyPythonAltFromHockeyArray(inhockeyarray, verbose=True, jsonverbose=True, verbosepy=True):
 if(not CheckHockeyArray(inhockeyarray)):
  return False;
 inchockeyarray = deepcopy(inhockeyarray);
 pyfilename = __package__;
 if(pyfilename=="__main__"):
  pyfilename = os.path.splitext(os.path.basename(__file__))[0];
 pystring = "#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nfrom __future__ import absolute_import, division, print_function, unicode_literals;\nimport "+pyfilename+";\n\n";
 pystring = pystring+"hockeyarray = "+pyfilename+".CreateHockeyArray(\""+inchockeyarray['database']+"\");\n";
 for hlkey in inchockeyarray['leaguelist']:
  HockeyLeagueHasConferences = True;
  if(inchockeyarray[hlkey]['leagueinfo']['conferences'].lower()=="no"):
   HockeyLeagueHasConferences = False;
  HockeyLeagueHasDivisions = True;
  if(inchockeyarray[hlkey]['leagueinfo']['divisions'].lower()=="no"):
   HockeyLeagueHasDivisions = False;
  pystring = pystring+"hockeyarray = "+pyfilename+".AddHockeyLeagueToArray(hockeyarray, \""+hlkey+"\", \""+inchockeyarray[hlkey]['leagueinfo']['fullname']+"\", \""+inchockeyarray[hlkey]['leagueinfo']['country']+"\", \""+inchockeyarray[hlkey]['leagueinfo']['fullcountry']+"\", \""+inchockeyarray[hlkey]['leagueinfo']['date']+"\", \""+inchockeyarray[hlkey]['leagueinfo']['playofffmt']+"\", \""+inchockeyarray[hlkey]['leagueinfo']['ordertype']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");\n";
  conferencecount = 0;
  conferenceend = len(inchockeyarray[hlkey]['conferencelist']);
  for hckey in inchockeyarray[hlkey]['conferencelist']:
   pystring = pystring+"hockeyarray = "+pyfilename+".AddHockeyConferenceToArray(hockeyarray, \""+hlkey+"\", \""+hckey+"\");\n";
   for hdkey in inchockeyarray[hlkey][hckey]['divisionlist']:
    pystring = pystring+"hockeyarray = "+pyfilename+".AddHockeyDivisionToArray(hockeyarray, \""+hlkey+"\", \""+hdkey+"\", \""+hckey+"\", \""+inchockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix']+"\", \""+inchockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix']+"\");\n";
    for htkey in inchockeyarray[hlkey][hckey][hdkey]['teamlist']:
     pystring = pystring+"hockeyarray = "+pyfilename+".AddHockeyTeamToArray(hockeyarray, \""+hlkey+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']+"\", \""+htkey+"\", \""+hckey+"\", \""+hdkey+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['affiliates']+"\");\n";
   conferencecount = conferencecount + 1;
  if(conferencecount>=conferenceend):
   hasarenas = False;
   if(len(inchockeyarray[hlkey]['arenas'])>0):
    hasarenas = True;
   for hakey in inchockeyarray[hlkey]['arenas']:
    if(hakey):
     hasarenas = True;
     pystring = pystring+"hockeyarray = "+pyfilename+".AddHockeyArenaToArray(hockeyarray, \""+hlkey+"\", \""+hakey['city']+"\", \""+hakey['area']+"\", \""+hakey['country']+"\", \""+hakey['fullcountry']+"\", \""+hakey['fullarea']+"\", \""+hakey['name']+"\");\n";
   hasgames = False;
   if(len(inchockeyarray[hlkey]['games'])>0):
    hasgames = True;
   for hgkey in inchockeyarray[hlkey]['games']:
    if(hgkey):
     hasgames = True;
     pystring = pystring+"hockeyarray = "+pyfilename+".AddHockeyGameToArray(hockeyarray, \""+hlkey+"\", "+hgkey['date']+", "+hgkey['time']+", \""+hgkey['hometeam']+"\", \""+hgkey['awayteam']+"\", \""+hgkey['goals']+"\", \""+hgkey['sogs']+"\", \""+hgkey['ppgs']+"\", \""+hgkey['shgs']+"\", \""+hgkey['penalties']+"\", \""+hgkey['pims']+"\", \""+hgkey['hits']+"\", \""+hgkey['takeaways']+"\", \""+hgkey['faceoffwins']+"\", \""+hgkey['atarena']+"\", \""+hgkey['isplayoffgame']+"\");\n";
 pystring = pystring+"\n";
 if(verbosepy):
  pyverbose = "True";
 elif(not verbosepy):
  pyverbose = "False";
 else:
  pyverbose = "False";
 pystring = pystring+pyfilename+".MakeHockeyDatabaseFromHockeyArray(hockeyarray, None, False, "+str(pyverbose)+", "+str(jsonverbose)+");\n";
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 return pystring;

def MakeHockeyPythonAltFileFromHockeyArray(inhockeyarray, outpyfile=None, returnpy=False, verbose=True, jsonverbose=True, verbosepy=True):
 if(outpyfile is None):
  return False;
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outpyfile)[0];
 fextname = os.path.splitext(outpyfile)[1];
 pyfp = CompressOpenFile(outpyfile);
 pystring = MakeHockeyPythonAltFromHockeyArray(inhockeyarray, verbose, verbosepy);
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

def MakeHockeyPythonOOPFromHockeyArray(inhockeyarray, verbose=True, jsonverbose=True):
 if(not CheckHockeyArray(inhockeyarray)):
  return False;
 inchockeyarray = deepcopy(inhockeyarray);
 pyfilename = __package__;
 if(pyfilename=="__main__"):
  pyfilename = os.path.splitext(os.path.basename(__file__))[0];
 pystring = "#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nfrom __future__ import absolute_import, division, print_function, unicode_literals;\nimport "+pyfilename+";\n\n";
 pystring = pystring+"sqldatacon = "+pyfilename+".MakeHockeyClass(\""+inchockeyarray['database']+"\");\n";
 pystring = pystring+"sqldatacon.MakeHockeyLeagueTable(sqldatacon);\n";
 for hlkey in inchockeyarray['leaguelist']:
  HockeyLeagueHasConferences = True;
  if(inchockeyarray[hlkey]['leagueinfo']['conferences'].lower()=="no"):
   HockeyLeagueHasConferences = False;
  HockeyLeagueHasDivisions = True;
  if(inchockeyarray[hlkey]['leagueinfo']['divisions'].lower()=="no"):
   HockeyLeagueHasDivisions = False;
  pystring = pystring+"sqldatacon.MakeHockeyTeamTable(sqldatacon, \""+hlkey+"\");\n"+"sqldatacon.MakeHockeyConferenceTable(sqldatacon, \""+hlkey+"\");\n"+"sqldatacon.MakeHockeyGameTable(sqldatacon, \""+hlkey+"\");\n"+"sqldatacon.MakeHockeyDivisionTable(sqldatacon, \""+hlkey+"\");\n"+"sqldatacon.AddHockeyLeague(sqldatacon, \""+hlkey+"\", \""+inchockeyarray[hlkey]['leagueinfo']['fullname']+"\", \""+inchockeyarray[hlkey]['leagueinfo']['country']+"\", \""+inchockeyarray[hlkey]['leagueinfo']['fullcountry']+"\", \""+inchockeyarray[hlkey]['leagueinfo']['date']+"\", \""+inchockeyarray[hlkey]['leagueinfo']['playofffmt']+"\", \""+inchockeyarray[hlkey]['leagueinfo']['ordertype']+"\");\n";
  conferencecount = 0;
  conferenceend = len(inchockeyarray[hlkey]['conferencelist']);
  for hckey in inchockeyarray[hlkey]['conferencelist']:
   pystring = pystring+"sqldatacon.AddHockeyConference(sqldatacon, \""+hlkey+"\", \""+hckey+"\", \""+inchockeyarray[hlkey][hckey]['conferenceinfo']['prefix']+"\", \""+inchockeyarray[hlkey][hckey]['conferenceinfo']['suffix']+"\", "+str(HockeyLeagueHasConferences)+");\n";
   for hdkey in inchockeyarray[hlkey][hckey]['divisionlist']:
    pystring = pystring+"sqldatacon.AddHockeyDivision(sqldatacon, \""+hlkey+"\", \""+hdkey+"\", \""+hckey+"\", \""+inchockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix']+"\", \""+inchockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");\n";
    for htkey in inchockeyarray[hlkey][hckey][hdkey]['teamlist']:
     pystring = pystring+"sqldatacon.AddHockeyTeam(sqldatacon, \""+hlkey+"\", \""+str(inchockeyarray[hlkey]['leagueinfo']['date'])+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']+"\", \""+htkey+"\", \""+hckey+"\", \""+hdkey+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['affiliates']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");\n";
   conferencecount = conferencecount + 1;
  if(conferencecount>=conferenceend):
   hasarenas = False;
   if(len(inchockeyarray[hlkey]['arenas'])>0):
    hasarenas = True;
   for hakey in inchockeyarray[hlkey]['arenas']:
    if(hakey):
     hasarenas = True;
     pystring = pystring+"sqldatacon.AddHockeyArena(sqldatacon, \""+hlkey+"\", \""+hakey['city']+"\", \""+hakey['area']+"\", \""+hakey['country']+"\", \""+hakey['fullcountry']+"\", \""+hakey['fullarea']+"\", \""+hakey['name']+"\");\n";
   hasgames = False;
   if(len(inchockeyarray[hlkey]['games'])>0):
    hasgames = True;
   for hgkey in inchockeyarray[hlkey]['games']:
    if(hgkey):
     hasgames = True;
     pystring = pystring+"sqldatacon.AddHockeyGame(sqldatacon, \""+hlkey+"\", "+hgkey['date']+", "+hgkey['time']+", \""+hgkey['hometeam']+"\", \""+hgkey['awayteam']+"\", \""+hgkey['goals']+"\", \""+hgkey['sogs']+"\", \""+hgkey['ppgs']+"\", \""+hgkey['shgs']+"\", \""+hgkey['penalties']+"\", \""+hgkey['pims']+"\", \""+hgkey['hits']+"\", \""+hgkey['takeaways']+"\", \""+hgkey['faceoffwins']+"\", \""+hgkey['atarena']+"\", \""+hgkey['isplayoffgame']+"\");\n";
 pystring = pystring+"\n";
 pystring = pystring+"sqldatacon.CloseHockeyDatabase(sqldatacon);\n";
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 return pystring;

def MakeHockeyPythonOOPFileFromHockeyArray(inhockeyarray, outpyfile=None, returnpy=False, verbose=True, jsonverbose=True):
 if(outpyfile is None):
  return False;
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outpyfile)[0];
 fextname = os.path.splitext(outpyfile)[1];
 pyfp = CompressOpenFile(outpyfile);
 pystring = MakeHockeyPythonOOPFromHockeyArray(inhockeyarray, verbose);
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

def MakeHockeyPythonOOPAltFromHockeyArray(inhockeyarray, verbose=True, jsonverbose=True, verbosepy=True):
 if(not CheckHockeyArray(inhockeyarray)):
  return False;
 inchockeyarray = deepcopy(inhockeyarray);
 pyfilename = __package__;
 if(pyfilename=="__main__"):
  pyfilename = os.path.splitext(os.path.basename(__file__))[0];
 pystring = "#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nfrom __future__ import absolute_import, division, print_function, unicode_literals;\nimport "+pyfilename+";\n\n";
 pystring = pystring+"hockeyarray = "+pyfilename+".MakeHockeyArray(\""+inchockeyarray['database']+"\");\n";
 for hlkey in inchockeyarray['leaguelist']:
  HockeyLeagueHasConferences = True;
  if(inchockeyarray[hlkey]['leagueinfo']['conferences'].lower()=="no"):
   HockeyLeagueHasConferences = False;
  HockeyLeagueHasDivisions = True;
  if(inchockeyarray[hlkey]['leagueinfo']['divisions'].lower()=="no"):
   HockeyLeagueHasDivisions = False;
  pystring = pystring+"hockeyarray = hockeyarray.AddHockeyLeague(\""+hlkey+"\", \""+inchockeyarray[hlkey]['leagueinfo']['fullname']+"\", \""+inchockeyarray[hlkey]['leagueinfo']['country']+"\", \""+inchockeyarray[hlkey]['leagueinfo']['fullcountry']+"\", \""+inchockeyarray[hlkey]['leagueinfo']['date']+"\", \""+inchockeyarray[hlkey]['leagueinfo']['playofffmt']+"\", \""+inchockeyarray[hlkey]['leagueinfo']['ordertype']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+");\n";
  conferencecount = 0;
  conferenceend = len(inchockeyarray[hlkey]['conferencelist']);
  for hckey in inchockeyarray[hlkey]['conferencelist']:
   pystring = pystring+"hockeyarray = hockeyarray.AddHockeyConference(\""+hlkey+"\", \""+hckey+"\", \""+inchockeyarray[hlkey][hckey]['conferenceinfo']['prefix']+"\", \""+inchockeyarray[hlkey][hckey]['conferenceinfo']['suffix']+"\");\n";
   for hdkey in inchockeyarray[hlkey][hckey]['divisionlist']:
    pystring = pystring+"hockeyarray = hockeyarray.AddHockeyDivision(\""+hlkey+"\", \""+hdkey+"\", \""+hckey+"\", \""+inchockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix']+"\", \""+inchockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix']+"\");\n";
    for htkey in inchockeyarray[hlkey][hckey][hdkey]['teamlist']:
     pystring = pystring+"hockeyarray = hockeyarray.AddHockeyTeam(\""+hlkey+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']+"\", \""+htkey+"\", \""+hckey+"\", \""+hdkey+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']+"\", \""+inchockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['affiliates']+"\");\n";
   conferencecount = conferencecount + 1;
  if(conferencecount>=conferenceend):
   hasarenas = False;
   if(len(inchockeyarray[hlkey]['arenas'])>0):
    hasarenas = True;
   for hakey in inchockeyarray[hlkey]['arenas']:
    if(hakey):
     hasarenas = True;
     pystring = pystring+"hockeyarray = hockeyarray.AddHockeyArena(\""+hlkey+"\", \""+hakey['city']+"\", \""+hakey['area']+"\", \""+hakey['country']+"\", \""+hakey['fullcountry']+"\", \""+hakey['fullarea']+"\", \""+hakey['name']+"\");\n";
   hasgames = False;
   if(len(inchockeyarray[hlkey]['games'])>0):
    hasgames = True;
   for hgkey in inchockeyarray[hlkey]['games']:
    if(hgkey):
     hasgames = True;
     pystring = pystring+"hockeyarray = hockeyarray.AddHockeyGame(\""+hlkey+"\", "+hgkey['date']+", "+hgkey['time']+", \""+hgkey['hometeam']+"\", \""+hgkey['awayteam']+"\", \""+hgkey['goals']+"\", \""+hgkey['sogs']+"\", \""+hgkey['ppgs']+"\", \""+hgkey['shgs']+"\", \""+hgkey['penalties']+"\", \""+hgkey['pims']+"\", \""+hgkey['hits']+"\", \""+hgkey['takeaways']+"\", \""+hgkey['faceoffwins']+"\", \""+hgkey['atarena']+"\", \""+hgkey['isplayoffgame']+"\");\n";
 pystring = pystring+"\n";
 if(verbosepy):
  pyverbose = "True";
 elif(not verbosepy):
  pyverbose = "False";
 else:
  pyverbose = "False";
 pystring = pystring+"hockeyarray.MakeHockeyDatabase(None, False, False, "+str(pyverbose)+", "+str(jsonverbose)+");\n";
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 return pystring;

def MakeHockeyPythonOOPAltFileFromHockeyArray(inhockeyarray, outpyfile=None, returnpy=False, verbose=True, jsonverbose=True, verbosepy=True):
 if(outpyfile is None):
  return False;
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outpyfile)[0];
 fextname = os.path.splitext(outpyfile)[1];
 pyfp = CompressOpenFile(outpyfile);
 pystring = MakeHockeyPythonOOPAltFromHockeyArray(inhockeyarray, verbose, verbosepy);
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

def MakeHockeyArrayFromHockeyDatabase(insdbfile, verbose=True, jsonverbose=True):
 if(isinstance(insdbfile, basestring) and (os.path.exists(insdbfile) and os.path.isfile(insdbfile))):
  if(not CheckHockeySQLiteDatabase(insdbfile)[0]):
   return False;
  sqldatacon = OpenHockeyDatabase(insdbfile);
 else:
  if(insdbfile is not None and isinstance(insdbfile, (tuple, list))):
   sqldatacon = tuple(insdbfile);
   insdbfile = ":memory:";
  else:
   return False;
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 leaguecur = sqldatacon[1].cursor();
 getleague_num = leaguecur.execute("SELECT COUNT(*) FROM HockeyLeagues").fetchone()[0];
 getleague = leaguecur.execute("SELECT LeagueName, LeagueFullName, CountryName, FullCountryName, Date, PlayOffFMT, OrderType, NumberOfConferences, NumberOfDivisions FROM HockeyLeagues");
 leaguearrayout = { 'database': str(insdbfile) };
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
  conferencecur = sqldatacon[1].cursor();
  getconference_num = conferencecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Conferences WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\"").fetchone()[0];
  getconference = conferencecur.execute("SELECT Conference, ConferencePrefix, ConferenceSuffix, FullName FROM "+leagueinfo[0]+"Conferences WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\"");
  conferencelist = [];
  for conferenceinfo in getconference:
   leaguearray[str(leagueinfo[0])].update( { str(conferenceinfo[0]): { 'conferenceinfo': { 'name': str(conferenceinfo[0]), 'prefix': str(conferenceinfo[1]), 'suffix': str(conferenceinfo[2]), 'fullname': str(conferenceinfo[3]), 'league': str(leagueinfo[0]) } } } );
   leaguearray[str(leagueinfo[0])]['quickinfo']['conferenceinfo'].update( { str(conferenceinfo[0]): { 'name': str(conferenceinfo[0]), 'fullname': str(conferenceinfo[3]), 'league': str(leagueinfo[0]) } } );
   conferencelist.append(str(conferenceinfo[0]));
   divisioncur = sqldatacon[1].cursor();
   getdivision_num = divisioncur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Divisions WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\"").fetchone()[0];
   getdivision = divisioncur.execute("SELECT Division, DivisionPrefix, DivisionSuffix, FullName FROM "+leagueinfo[0]+"Divisions WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\"");
   divisionlist = [];
   for divisioninfo in getdivision:
    leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update( { str(divisioninfo[0]): { 'divisioninfo': { 'name': str(divisioninfo[0]), 'prefix': str(divisioninfo[1]), 'suffix': str(divisioninfo[2]), 'fullname': str(divisioninfo[3]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]) } } } );
    leaguearray[str(leagueinfo[0])]['quickinfo']['divisioninfo'].update( { str(divisioninfo[0]): { 'name': str(divisioninfo[0]), 'fullname': str(divisioninfo[3]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]) } } );
    divisionlist.append(str(divisioninfo[0]));
    teamcur = sqldatacon[1].cursor();
    getteam_num = teamcur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Teams WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"").fetchone()[0];
    getteam = teamcur.execute("SELECT CityName, AreaName, FullAreaName, CountryName, FullCountryName, TeamName, ArenaName, TeamPrefix, TeamSuffix, Affiliates FROM "+leagueinfo[0]+"Teams WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"");
    teamlist = [];
    for teaminfo in getteam:
     fullteamname = GetFullTeamName(str(teaminfo[5]), str(teaminfo[7]), str(teaminfo[8]));
     leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(divisioninfo[0])].update( { str(teaminfo[5]): { 'teaminfo': { 'city': str(teaminfo[0]), 'area': str(teaminfo[1]), 'fullarea': str(teaminfo[2]), 'country': str(teaminfo[3]), 'fullcountry': str(teaminfo[4]), 'name': str(teaminfo[5]), 'fullname': fullteamname, 'arena': str(teaminfo[6]), 'prefix': str(teaminfo[7]), 'suffix': str(teaminfo[8]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0]), 'affiliates': str(teaminfo[9]) } } } );
     leaguearray[str(leagueinfo[0])]['quickinfo']['teaminfo'].update( { str(teaminfo[5]): { 'name': str(teaminfo[5]), 'fullname': fullteamname, 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0]) } } );
     teamlist.append(str(teaminfo[5]));
    teamcur.close();
    leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(divisioninfo[0])].update( { 'teamlist': teamlist } );
   divisioncur.close();
   leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update( { 'divisionlist': divisionlist } );
  conferencecur.close();
  leaguearray[str(leagueinfo[0])].update( { 'conferencelist': conferencelist } );
  arenacur = sqldatacon[1].cursor();
  getteam_num = arenacur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Arenas WHERE TeamID=0").fetchone()[0];
  getarena = arenacur.execute("SELECT CityName, AreaName, FullAreaName, CountryName, FullCountryName, ArenaName FROM "+leagueinfo[0]+"Arenas WHERE TeamID=0");
  if(getteam_num>0):
   for arenainfo in getarena:
    arenalist.append( { 'city': str(arenainfo[0]), 'area': str(arenainfo[1]), 'fullarea': str(arenainfo[2]), 'country': str(arenainfo[3]), 'fullcountry': str(arenainfo[4]), 'name': str(arenainfo[5]) } );
  leaguearray[str(leagueinfo[0])].update( { "arenas": arenalist } );
  gamecur = sqldatacon[1].cursor();
  getgame_num = gamecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Games").fetchone()[0];
  getgame = gamecur.execute("SELECT Date, Time, HomeTeam, AwayTeam, TeamScorePeriods, ShotsOnGoal, PowerPlays, ShortHanded, Penalties, PenaltyMinutes, HitsPerPeriod, TakeAways, FaceoffWins, AtArena, IsPlayOffGame FROM "+leagueinfo[0]+"Games");
  if(getgame_num>0):
   for gameinfo in getgame:
    AtArena = gameinfo[13];
    if(GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[2]), "FullArenaName", "str")==AtArena):
     AtArena = "0";
    if(GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[3]), "FullArenaName", "str")==AtArena):
     AtArena = "1";
    gamelist.append( { 'date': str(gameinfo[0]), 'time': str(gameinfo[1]), 'hometeam': str(gameinfo[2]), 'awayteam': str(gameinfo[3]), 'goals': str(gameinfo[4]), 'sogs': str(gameinfo[5]), 'ppgs': str(gameinfo[6]), 'shgs': str(gameinfo[7]), 'penalties': str(gameinfo[8]), 'pims': str(gameinfo[9]), 'hits': str(gameinfo[10]), 'takeaways': str(gameinfo[11]), 'faceoffwins': str(gameinfo[12]), 'atarena': str(AtArena), 'isplayoffgame': str(gameinfo[14]) } );
  leaguearray[str(leagueinfo[0])].update( { "games": gamelist } );
  leaguearrayout.update(leaguearray);
 leaguearrayout.update( { 'leaguelist': leaguelist } );
 leaguecur.close();
 sqldatacon[1].close();
 if(not CheckHockeyArray(leaguearrayout)):
  return False;
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(leaguearrayout, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(leaguearrayout, verbose=False, jsonverbose=True));
 return leaguearrayout;

def MakeHockeyArrayFromHockeySQL(insqlfile, insdbfile=None, sqlisfile=True, verbose=True, jsonverbose=True):
 if(sqlisfile and (os.path.exists(insqlfile) and os.path.isfile(insqlfile))):
  sqlfp = UncompressFile(insqlfile);
  sqlstring = sqlfp.read();
  sqlfp.close();
 elif(not sqlisfile):
  sqlfp = BytesIO(insqlfile);
  sqlfp = UncompressFileAlt(sqlfp);
  sqlstring = sqlfp.read();
  sqlfp.close();
 else:
  return False;
 if(insdbfile is None and len(re.findall(r"Database\:([\w\W]+)", insqlfile))>=1):
  insdbfile = re.findall(r"Database\:([\w\W]+)", insqlfile)[0].strip();
 if(insdbfile is None and len(re.findall(r"Database\:([\w\W]+)", insqlfile))<1):
  file_wo_extension, file_extension = os.path.splitext(insqlfile);
  insdbfile = file_wo_extension+".db3";
 sqldatacon = MakeHockeyDatabase(":memory:");
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 try:
  sqldatacon[0].executescript(sqlstring);
 except ValueError:
  sqldatacon[0].executescript(sqlstring.decode("UTF-8"));
 leaguecur = sqldatacon[1].cursor();
 getleague_num = leaguecur.execute("SELECT COUNT(*) FROM HockeyLeagues").fetchone()[0];
 getleague = leaguecur.execute("SELECT LeagueName, LeagueFullName, CountryName, FullCountryName, Date, PlayOffFMT, OrderType, NumberOfConferences, NumberOfDivisions FROM HockeyLeagues");
 leaguearrayout = { 'database': str(insdbfile) };
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
  conferencecur = sqldatacon[1].cursor();
  getconference_num = conferencecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Conferences WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\"").fetchone()[0];
  getconference = conferencecur.execute("SELECT Conference, ConferencePrefix, ConferenceSuffix, FullName FROM "+leagueinfo[0]+"Conferences WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\"");
  conferencelist = [];
  for conferenceinfo in getconference:
   leaguearray[str(leagueinfo[0])].update( { str(conferenceinfo[0]): { 'conferenceinfo': { 'name': str(conferenceinfo[0]), 'prefix': str(conferenceinfo[1]), 'suffix': str(conferenceinfo[2]), 'fullname': str(conferenceinfo[3]), 'league': str(leagueinfo[0]) } } } );
   leaguearray[str(leagueinfo[0])]['quickinfo']['conferenceinfo'].update( { str(conferenceinfo[0]): { 'name': str(conferenceinfo[0]), 'fullname': str(conferenceinfo[3]), 'league': str(leagueinfo[0]) } } );
   conferencelist.append(str(conferenceinfo[0]));
   divisioncur = sqldatacon[1].cursor();
   getdivision_num = divisioncur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Divisions WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\"").fetchone()[0];
   getdivision = divisioncur.execute("SELECT Division, DivisionPrefix, DivisionSuffix, FullName FROM "+leagueinfo[0]+"Divisions WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\"");
   divisionlist = [];
   for divisioninfo in getdivision:
    leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update( { str(divisioninfo[0]): { 'divisioninfo': { 'name': str(divisioninfo[0]), 'prefix': str(divisioninfo[1]), 'suffix': str(divisioninfo[2]), 'fullname': str(divisioninfo[3]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]) } } } );
    leaguearray[str(leagueinfo[0])]['quickinfo']['divisioninfo'].update( { str(divisioninfo[0]): { 'name': str(divisioninfo[0]), 'fullname': str(divisioninfo[3]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]) } } );
    divisionlist.append(str(divisioninfo[0]));
    teamcur = sqldatacon[1].cursor();
    getteam_num = teamcur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Teams WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"").fetchone()[0];
    getteam = teamcur.execute("SELECT CityName, AreaName, FullAreaName, CountryName, FullCountryName, TeamName, ArenaName, TeamPrefix, TeamSuffix, Affiliates FROM "+leagueinfo[0]+"Teams WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"");
    teamlist = [];
    for teaminfo in getteam:
     fullteamname = GetFullTeamName(str(teaminfo[5]), str(teaminfo[7]), str(teaminfo[8]));
     leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(divisioninfo[0])].update( { str(teaminfo[5]): { 'teaminfo': { 'city': str(teaminfo[0]), 'area': str(teaminfo[1]), 'fullarea': str(teaminfo[2]), 'country': str(teaminfo[3]), 'fullcountry': str(teaminfo[4]), 'name': str(teaminfo[5]), 'fullname': fullteamname, 'arena': str(teaminfo[6]), 'prefix': str(teaminfo[7]), 'suffix': str(teaminfo[8]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0]), 'affiliates': str(teaminfo[9]) } } } );
     leaguearray[str(leagueinfo[0])]['quickinfo']['teaminfo'].update( { str(teaminfo[5]): { 'name': str(teaminfo[5]), 'fullname': fullteamname, 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0]) } } );
     teamlist.append(str(teaminfo[5]));
    teamcur.close();
    leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(divisioninfo[0])].update( { 'teamlist': teamlist } );
   divisioncur.close();
   leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update( { 'divisionlist': divisionlist } );
  conferencecur.close();
  leaguearray[str(leagueinfo[0])].update( { 'conferencelist': conferencelist } );
  arenacur = sqldatacon[1].cursor();
  getteam_num = arenacur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Arenas WHERE TeamID=0").fetchone()[0];
  getarena = arenacur.execute("SELECT CityName, AreaName, FullAreaName, CountryName, FullCountryName, ArenaName FROM "+leagueinfo[0]+"Arenas WHERE TeamID=0");
  if(getteam_num>0):
   for arenainfo in getarena:
    arenalist.append( { 'city': str(arenainfo[0]), 'area': str(arenainfo[1]), 'fullarea': str(arenainfo[2]), 'country': str(arenainfo[3]), 'fullcountry': str(arenainfo[4]), 'name': str(arenainfo[5]) } );
  leaguearray[str(leagueinfo[0])].update( { "arenas": arenalist } );
  gamecur = sqldatacon[1].cursor();
  getgame_num = gamecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Games").fetchone()[0];
  getgame = gamecur.execute("SELECT Date, Time, HomeTeam, AwayTeam, TeamScorePeriods, ShotsOnGoal, PowerPlays, ShortHanded, Penalties, PenaltyMinutes, HitsPerPeriod, TakeAways, FaceoffWins, AtArena, IsPlayOffGame FROM "+leagueinfo[0]+"Games");
  if(getgame_num>0):
   for gameinfo in getgame:
    AtArena = gameinfo[13];
    if(GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[2]), "FullArenaName", "str")==AtArena):
     AtArena = "0";
    if(GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[3]), "FullArenaName", "str")==AtArena):
     AtArena = "1";
    gamelist.append( { 'date': str(gameinfo[0]), 'time': str(gameinfo[1]), 'hometeam': str(gameinfo[2]), 'awayteam': str(gameinfo[3]), 'goals': str(gameinfo[4]), 'sogs': str(gameinfo[5]), 'ppgs': str(gameinfo[6]), 'shgs': str(gameinfo[7]), 'penalties': str(gameinfo[8]), 'pims': str(gameinfo[9]), 'hits': str(gameinfo[10]), 'takeaways': str(gameinfo[11]), 'faceoffwins': str(gameinfo[12]), 'atarena': str(AtArena), 'isplayoffgame': str(gameinfo[14]) } );
  leaguearray[str(leagueinfo[0])].update( { "games": gamelist } );
  leaguearrayout.update(leaguearray);
 leaguearrayout.update( { 'leaguelist': leaguelist } );
 leaguecur.close();
 sqldatacon[1].close();
 if(not CheckHockeyArray(leaguearrayout)):
  return False;
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(leaguearrayout, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(leaguearrayout, verbose=False, jsonverbose=True));
 return leaguearrayout;

def MakeHockeySQLFromHockeyArray(inhockeyarray, insdbfile=":memory:", verbose=True, jsonverbose=True):
 if(not CheckHockeyArray(inhockeyarray)):
  return False;
 if(insdbfile is None):
  insdbfile = ":memory:";
 sqldatacon = MakeHockeyDatabaseFromHockeyArray(inhockeyarray, ":memory:", True, False, False);
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
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
 sqldump = sqldump+"-- Database: "+insdbfile+"\n";
 sqldump = sqldump+"--\n\n";
 sqldump = sqldump+"-- --------------------------------------------------------\n\n";
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
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 return sqldump;

def MakeHockeySQLFileFromHockeyArray(inhockeyarray, outsqlfile=None, returnsql=False, verbose=True, jsonverbose=True):
 if(outsqlfile is None):
  return False;
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outsqlfile)[0];
 fextname = os.path.splitext(outsqlfile)[1];
 sqlfp = CompressOpenFile(outsqlfile);
 sqlstring = MakeHockeySQLFromHockeyArray(inhockeyarray, os.path.splitext(outsqlfile)[0]+".db3", verbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  sqlstring = sqlstring.encode();
 sqlfp.write(sqlstring);
 sqlfp.close();
 if(returnsql):
  return sqlstring;
 if(not returnsql):
  return True;
 return True;

def MakeHockeySQLFromHockeyDatabase(insdbfile, verbose=True, jsonverbose=True):
 if(os.path.exists(insdbfile) and os.path.isfile(insdbfile) and isinstance(insdbfile, basestring)):
  sqldatacon = OpenHockeyDatabase(insdbfile);
 else:
  if(insdbfile is not None and isinstance(insdbfile, (tuple, list))):
   sqldatacon = tuple(insdbfile);
  else:
   return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
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
 sqldump = sqldump+"-- Database: "+insdbfile+"\n";
 sqldump = sqldump+"--\n\n";
 sqldump = sqldump+"-- --------------------------------------------------------\n\n";
 #all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games", "PlayoffTeams"];
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
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(MakeHockeyArrayFromHockeyDatabase(insdbfile, verbose=False, jsonverbose=True), verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(MakeHockeyArrayFromHockeyDatabase(insdbfile, verbose=False, jsonverbose=True), verbose=False, jsonverbose=True));
 return sqldump;

def MakeHockeySQLFileFromHockeyDatabase(insdbfile, outsqlfile=None, returnsql=False, verbose=True, jsonverbose=True):
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
 sqlstring = MakeHockeySQLFromHockeyDatabase(insdbfile, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  sqlstring = sqlstring.encode();
 sqlfp.write(sqlstring);
 sqlfp.close();
 if(returnsql):
  return sqlstring;
 if(not returnsql):
  return True;
 return True;

def MakeHockeyArrayFromOldHockeyDatabase(insdbfile, verbose=True, jsonverbose=True):
 if(isinstance(insdbfile, basestring) and (os.path.exists(insdbfile) and os.path.isfile(insdbfile))):
  sqldatacon = OpenHockeyDatabase(insdbfile);
 else:
  if(insdbfile is not None and isinstance(insdbfile, (tuple, list))):
   sqldatacon = tuple(insdbfile);
   insdbfile = ":memory:";
  else:
   return False;
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 leaguecur = sqldatacon[1].cursor();
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
 leaguearrayout = { 'database': str(insdbfile) };
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
  conferencecur = sqldatacon[1].cursor();
  getconference_num = conferencecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Conferences").fetchone()[0];
  getconference = conferencecur.execute("SELECT Conference FROM "+leagueinfo[0]+"Conferences");
  conferencelist = [];
  for conferenceinfo in getconference:
   leaguearray[str(leagueinfo[0])].update( { str(conferenceinfo[0]): { 'conferenceinfo': { 'name': str(conferenceinfo[0]), 'league': str(leagueinfo[0]) } } } );
   leaguearray[str(leagueinfo[0])]['quickinfo']['conferenceinfo'].update( { str(conferenceinfo[0]): { 'name': str(conferenceinfo[0]), 'league': str(leagueinfo[0]) } } );
   conferencelist.append(str(conferenceinfo[0]));
   divisioncur = sqldatacon[1].cursor();
   getdivision_num = divisioncur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Divisions WHERE Conference=\""+conferenceinfo[0]+"\"").fetchone()[0];
   getdivision = divisioncur.execute("SELECT Division FROM "+leagueinfo[0]+"Divisions WHERE Conference=\""+conferenceinfo[0]+"\"");
   divisionlist = [];
   for divisioninfo in getdivision:
    leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update( { str(divisioninfo[0]): { 'divisioninfo': { 'name': str(divisioninfo[0]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]) } } } );
    leaguearray[str(leagueinfo[0])]['quickinfo']['divisioninfo'].update( { str(divisioninfo[0]): { 'name': str(divisioninfo[0]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]) } } );
    divisionlist.append(str(divisioninfo[0]));
    teamcur = sqldatacon[1].cursor();
    getteam_num = teamcur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Teams WHERE Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"").fetchone()[0];
    getteam = teamcur.execute("SELECT CityName, AreaName, TeamName, ArenaName, TeamPrefix, Affiliates FROM "+leagueinfo[0]+"Teams WHERE Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"");
    teamlist = [];
    for teaminfo in getteam:
     TeamAreaInfo = GetAreaInfoFromUSCA(teaminfo[1]);
     fullteamname = GetFullTeamName(str(teaminfo[2]), str(teaminfo[4]), "");
     leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(divisioninfo[0])].update( { str(teaminfo[2]): { 'teaminfo': { 'city': str(teaminfo[0]), 'area': str(TeamAreaInfo['AreaName']), 'fullarea': str(TeamAreaInfo['FullAreaName']), 'country': str(TeamAreaInfo['CountryName']), 'fullcountry': str(TeamAreaInfo['FullCountryName']), 'name': str(teaminfo[2]), 'fullname': fullteamname, 'arena': str(teaminfo[3]), 'prefix': str(teaminfo[4]), 'suffix': "", 'affiliates': str(teaminfo[5].strip()), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0]) } } } );
     leaguearray[str(leagueinfo[0])]['quickinfo']['teaminfo'].update( { str(teaminfo[2]): { 'name': str(teaminfo[2]), 'fullname': fullteamname, 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0]) } } );
     teamlist.append(str(teaminfo[2]));
    teamcur.close();
    leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(divisioninfo[0])].update( { 'teamlist': teamlist } );
   divisioncur.close();
   leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update( { 'divisionlist': divisionlist } );
  conferencecur.close();
  leaguearray[str(leagueinfo[0])].update( { 'conferencelist': conferencelist } );
  arenacur = sqldatacon[1].cursor();
  getteam_num = arenacur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Arenas WHERE id>"+str(getallteam_num)).fetchone()[0];
  getarena = arenacur.execute("SELECT CityName, AreaName, ArenaName FROM "+leagueinfo[0]+"Arenas WHERE id>"+str(getallteam_num));
  if(getteam_num>0):
   for arenainfo in getarena:
    ArenaAreaInfo = GetAreaInfoFromUSCA(arenainfo[1]);
    arenalist.append( { 'city': str(arenainfo[0]), 'area': str(ArenaAreaInfo['AreaName']), 'fullarea': str(ArenaAreaInfo['FullAreaName']), 'country': str(ArenaAreaInfo['CountryName']), 'fullcountry': str(ArenaAreaInfo['FullCountryName']), 'name': str(arenainfo[2]) } );
  leaguearray[str(leagueinfo[0])].update( { "arenas": arenalist } );
  gamecur = sqldatacon[1].cursor();
  getgame_num = gamecur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Games").fetchone()[0];
  getgame = gamecur.execute("SELECT Date, HomeTeam, AwayTeam, TeamScorePeriods, ShotsOnGoal, AtArena, IsPlayOffGame FROM "+leagueinfo[0]+"Games");
  if(getgame_num>0):
   for gameinfo in getgame:
    GetNumPeriods = len(gameinfo[3].split(","));
    EmptyScore = ",0:0" * (GetNumPeriods - 1);
    EmptyScore = "0:0"+EmptyScore;
    AtArena = gameinfo[5];
    if(GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[1]), "FullArenaName", "str")==AtArena):
     AtArena = "0";
    if(GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[2]), "FullArenaName", "str")==AtArena):
     AtArena = "1";
    gamelist.append( { 'date': str(gameinfo[0]), 'time': "0000", 'hometeam': str(gameinfo[1]), 'awayteam': str(gameinfo[2]), 'goals': str(gameinfo[3]), 'sogs': str(gameinfo[4]), 'ppgs': str(EmptyScore), 'shgs': str(EmptyScore), 'penalties': str(EmptyScore), 'pims': str(EmptyScore), 'hits': str(EmptyScore), 'takeaways': str(EmptyScore), 'faceoffwins': str(EmptyScore), 'atarena': str(AtArena), 'isplayoffgame': str(gameinfo[6]) } );
  leaguearray[str(leagueinfo[0])].update( { "games": gamelist } );
  leaguearrayout.update(leaguearray);
 leaguearrayout.update( { 'leaguelist': leaguelist } );
 leaguecur.close();
 CloseHockeyDatabase(sqldatacon);
 if(not CheckHockeyArray(leaguearrayout)):
  return False;
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(leaguearrayout, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(leaguearrayout, verbose=False, jsonverbose=True));
 return leaguearrayout;

def MakeHockeySQLiteArrayFromHockeyDatabase(insdbfile, verbose=True, jsonverbose=True):
 if(isinstance(insdbfile, basestring) and (os.path.exists(insdbfile) and os.path.isfile(insdbfile))):
  if(not CheckHockeySQLiteDatabase(insdbfile)[0]):
   return False;
  sqldatacon = OpenHockeyDatabase(insdbfile);
 else:
  if(insdbfile is not None and isinstance(insdbfile, (tuple, list))):
   sqldatacon = tuple(insdbfile);
   insdbfile = ":memory:";
  else:
   return False;
 if(not isinstance(sqldatacon, (tuple, list)) and not sqldatacon):
  return False;
 if(not hasattr(sqldatacon[0], "execute")):
  return False;
 if(not hasattr(sqldatacon[1], "execute")):
  return False;
 #all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games", "PlayoffTeams"];
 all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games"];
 table_list = ['HockeyLeagues'];
 getleague_num_tmp = sqldatacon[0].execute("SELECT COUNT(*) FROM HockeyLeagues").fetchone()[0];
 getleague_tmp = sqldatacon[0].execute("SELECT LeagueName FROM HockeyLeagues");
 leaguearrayout = { 'database': str(insdbfile) };
 for leagueinfo_tmp in getleague_tmp:
  for cur_tab in all_table_list:
   table_list.append(leagueinfo_tmp[0]+cur_tab);
 for get_cur_tab in table_list:
  gettableinfo = sqldatacon[0].execute("PRAGMA table_xinfo("+get_cur_tab+");").fetchall();
  leaguearrayout.update( { get_cur_tab: { } } );
  collist = [];
  sqlrowlist = [];
  for tableinfo in gettableinfo:
   autoincrement = 0;
   if(tableinfo[1]=="id" and tableinfo[5]==1):
    autoincrement = 1;
   leaguearrayout[get_cur_tab].update( { tableinfo[1]: { 'info': {'id': tableinfo[0], 'Name': tableinfo[1], 'Type': tableinfo[2], 'NotNull': tableinfo[3], 'DefualtValue': tableinfo[4], 'PrimaryKey': tableinfo[5], 'AutoIncrement': autoincrement, 'Hidden': tableinfo[6] } } } );
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
   leaguearrayout[get_cur_tab].update( { 'values': subcollist } );
  leaguearrayout[get_cur_tab].update( { 'rows': collist } );
 sqldatacon[1].close();
 if(not CheckHockeySQLiteArray(leaguearrayout)):
  return False;
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(leaguearrayout, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(leaguearrayout, verbose=False, jsonverbose=True));
 return leaguearrayout;

def MakeHockeySQLiteXMLFromHockeySQLiteArray(inhockeyarray, beautify=True, verbose=True, jsonverbose=True):
 if(not CheckHockeySQLiteArray(inhockeyarray)):
  return False;
 inchockeyarray = deepcopy(inhockeyarray);
 xmlstring = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
 if "database" in inchockeyarray.keys():
  xmlstring = xmlstring+"<hockeydb database=\""+EscapeXMLString(str(inchockeyarray['database']), quote=True)+"\">\n";
 if "database" not in inchockeyarray.keys():
  xmlstring = xmlstring+"<hockeydb database=\""+EscapeXMLString(str(defaultsdbfile))+"\">\n";
 #all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games", "PlayoffTeams"];
 all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games"];
 table_list = ['HockeyLeagues'];
 for leagueinfo_tmp in inchockeyarray['HockeyLeagues']['values']:
  for cur_tab in all_table_list:
   table_list.append(leagueinfo_tmp['LeagueName']+cur_tab);
 for get_cur_tab in table_list:
  xmlstring = xmlstring+" <table name=\""+EscapeXMLString(str(get_cur_tab))+"\">\n";
  rowlen = len(inchockeyarray[get_cur_tab]['rows']);
  rowi = 0;
  sqlrowlist = [];
  xmlstring = xmlstring+"  <column>\n";
  for rowinfo in inchockeyarray[get_cur_tab]['rows']:
   xmlstring = xmlstring+"   <rowinfo id=\""+EscapeXMLString(str(inchockeyarray[get_cur_tab][rowinfo]['info']['id']))+"\" name=\""+EscapeXMLString(str(inchockeyarray[get_cur_tab][rowinfo]['info']['Name']))+"\" type=\""+EscapeXMLString(str(inchockeyarray[get_cur_tab][rowinfo]['info']['Type']))+"\" notnull=\""+EscapeXMLString(str(inchockeyarray[get_cur_tab][rowinfo]['info']['NotNull']))+"\" defaultvalue=\""+EscapeXMLString(ConvertPythonValuesForXML(str(inchockeyarray[get_cur_tab][rowinfo]['info']['DefualtValue'])))+"\" primarykey=\""+EscapeXMLString(str(inchockeyarray[get_cur_tab][rowinfo]['info']['PrimaryKey']))+"\" autoincrement=\""+EscapeXMLString(str(inchockeyarray[get_cur_tab][rowinfo]['info']['AutoIncrement']))+"\" hidden=\""+EscapeXMLString(str(inchockeyarray[get_cur_tab][rowinfo]['info']['Hidden']))+"\" />\n";
  xmlstring = xmlstring+"  </column>\n";
  if(len(inchockeyarray[get_cur_tab]['values'])>0):
   xmlstring = xmlstring+"  <data>\n";
  rowid = 0;
  for rowvalues in inchockeyarray[get_cur_tab]['values']:
   xmlstring = xmlstring+"   <row id=\""+EscapeXMLString(str(rowid))+"\">\n"; 
   rowid = rowid + 1;
   for rkey, rvalue in rowvalues.items():
    xmlstring = xmlstring+"    <rowdata name=\""+EscapeXMLString(str(rkey))+"\" value=\""+EscapeXMLString(str(rvalue))+"\" />\n";
   xmlstring = xmlstring+"   </row>\n"; 
  if(len(inchockeyarray[get_cur_tab]['values'])>0):
   xmlstring = xmlstring+"  </data>\n";
  else:
   xmlstring = xmlstring+"  <data />\n";
  xmlstring = xmlstring+"  <rows>\n";
  for rowinfo in inchockeyarray[get_cur_tab]['rows']:
   xmlstring = xmlstring+"   <rowlist name=\""+EscapeXMLString(str(rowinfo))+"\" />\n";   
  xmlstring = xmlstring+"  </rows>\n";
  xmlstring = xmlstring+" </table>\n";
 xmlstring = xmlstring+"</hockeydb>\n";
 xmlstring = BeautifyXMLCode(xmlstring, False, " ", "\n", "UTF-8", beautify);
 if(not CheckHockeySQLiteXML(xmlstring, False)):
  return False;
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 return xmlstring;

def MakeHockeySQLiteXMLFileFromHockeySQLiteArray(inhockeyarray, outxmlfile=None, returnxml=False, beautify=True, verbose=True, jsonverbose=True):
 if(outxmlfile is None):
  return False;
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outxmlfile)[0];
 fextname = os.path.splitext(outxmlfile)[1];
 xmlfp = CompressOpenFile(outxmlfile);
 xmlstring = MakeHockeySQLiteXMLFromHockeySQLiteArray(inhockeyarray, beautify, verbose, jsonverbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  xmlstring = xmlstring.encode();
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml):
  return xmlstring;
 if(not returnxml):
  return True;
 return True;

def MakeHockeySQLiteXMLAltFromHockeySQLiteArray(inhockeyarray, beautify=True, verbose=True, jsonverbose=True):
 if(not CheckHockeySQLiteArray(inhockeyarray)):
  return False;
 inchockeyarray = deepcopy(inhockeyarray);
 if "database" in inchockeyarray.keys():
  xmlstring_hockeydb = cElementTree.Element("hockeydb", { 'database': str(inchockeyarray['database']) } );
 if "database" not in inchockeyarray.keys():
  xmlstring_hockeydb = cElementTree.Element("hockeydb", { 'database': str(defaultsdbfile) } );
 #all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games", "PlayoffTeams"];
 all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games"];
 table_list = ['HockeyLeagues'];
 for leagueinfo_tmp in inchockeyarray['HockeyLeagues']['values']:
  for cur_tab in all_table_list:
   table_list.append(leagueinfo_tmp['LeagueName']+cur_tab);
 for get_cur_tab in table_list:
  xmlstring_table = cElementTree.SubElement(xmlstring_hockeydb, "table", { 'name': str(get_cur_tab) } );
  rowlen = len(inchockeyarray[get_cur_tab]['rows']);
  rowi = 0;
  sqlrowlist = [];
  xmlstring_column = cElementTree.SubElement(xmlstring_table, "column");
  for rowinfo in inchockeyarray[get_cur_tab]['rows']:
   xmlstring_rowinfo = cElementTree.SubElement(xmlstring_column, "rowinfo", { 'id': str(inchockeyarray[get_cur_tab][rowinfo]['info']['id']), 'name': str(inchockeyarray[get_cur_tab][rowinfo]['info']['Name']), 'type': str(inchockeyarray[get_cur_tab][rowinfo]['info']['Type']), 'notnull': str(inchockeyarray[get_cur_tab][rowinfo]['info']['NotNull']), 'defaultvalue': ConvertPythonValuesForXML(str(inchockeyarray[get_cur_tab][rowinfo]['info']['DefualtValue'])), 'primarykey': str(inchockeyarray[get_cur_tab][rowinfo]['info']['PrimaryKey']), 'autoincrement': str(inchockeyarray[get_cur_tab][rowinfo]['info']['AutoIncrement']), 'hidden': str(inchockeyarray[get_cur_tab][rowinfo]['info']['Hidden']) } );
  if(len(inchockeyarray[get_cur_tab]['values'])>0):
   xmlstring_data = cElementTree.SubElement(xmlstring_table, "data");
  rowid = 0;
  for rowvalues in inchockeyarray[get_cur_tab]['values']:
   xmlstring_row = cElementTree.SubElement(xmlstring_data, "row", { 'id': str(rowid) } );
   rowid = rowid + 1;
   for rkey, rvalue in rowvalues.items():
    xmlstring_rowdata = cElementTree.SubElement(xmlstring_row, "rowdata", { 'name': str(rkey), 'value': str(rvalue) } );
  if(len(inchockeyarray[get_cur_tab]['values'])<0):
   xmlstring_data = cElementTree.SubElement(xmlstring_table, "data");
  xmlstring_rows = cElementTree.SubElement(xmlstring_table, "rows");
  for rowinfo in inchockeyarray[get_cur_tab]['rows']:
   xmlstring_rowlist = cElementTree.SubElement(xmlstring_rows, "rowlist", { 'name': str(rowinfo) } );
 '''xmlstring = cElementTree.tostring(xmlstring_hockey, "UTF-8", "xml", True, "xml", True).decode("UTF-8");'''
 if(testlxml):
  xmlstring = cElementTree.tostring(xmlstring_hockey, encoding="UTF-8", method="xml", xml_declaration=True, pretty_print=True).decode("UTF-8");
 else:
  try:
   xmlstring = cElementTree.tostring(xmlstring_hockey, encoding="UTF-8", method="xml", xml_declaration=True).decode("UTF-8");
  except TypeError:
   xmlstring = cElementTree.tostring(xmlstring_hockey, encoding="UTF-8", method="xml").decode("UTF-8");
 xmlstring = BeautifyXMLCode(xmlstring, False, " ", "\n", "UTF-8", beautify);
 if(not CheckHockeySQLiteXML(xmlstring, False)):
  return False;
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 return xmlstring;

def MakeHockeySQLiteXMLAltFileFromHockeySQLiteArray(inhockeyarray, outxmlfile=None, returnxml=False, beautify=True, verbose=True, jsonverbose=True):
 if(outxmlfile is None):
  return False;
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outxmlfile)[0];
 fextname = os.path.splitext(outxmlfile)[1];
 xmlfp = CompressOpenFile(outxmlfile);
 xmlstring = MakeHockeySQLiteXMLAltFromHockeySQLiteArray(inhockeyarray, beautify, verbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  xmlstring = xmlstring.encode();
 xmlfp.write(xmlstring);
 xmlfp.close();
 if(returnxml):
  return xmlstring;
 if(not returnxml):
  return True;
 return True;

def MakeHockeySQLiteArrayFromHockeySQLiteXML(inxmlfile, xmlisfile=True, verbose=True, jsonverbose=True):
 if(not CheckHockeySQLiteXML(inxmlfile, xmlisfile)):
  return False;
 if(xmlisfile and ((os.path.exists(inxmlfile) and os.path.isfile(inxmlfile)) or re.findall("^(http|https|ftp|ftps|sftp)\:\/\/", inxmlfile))):
  try:
   if(re.findall("^(http|https|ftp|ftps|sftp)\:\/\/", inxmlfile)):
    inxmlfile = UncompressFileURL(inxmlfile, geturls_headers, geturls_cj);
   else:
    hockeyfile = cElementTree.ElementTree(file=UncompressFile(inxmlfile));
  except cElementTree.ParseError: 
   return False;
 elif(not xmlisfile):
  inxmlsfile = BytesIO(inxmlfile.encode());
  inxmlfile = UncompressFileAlt(inxmlsfile);
  try:
   hockeyfile = cElementTree.ElementTree(file=inxmlsfile);
  except cElementTree.ParseError: 
   return False;
 else:
  return False;
 gethockey = hockeyfile.getroot();
 leaguearrayout = { 'database': str(gethockey.attrib['database']) };
 for gettable in gethockey:
  leaguearrayout.update( { gettable.attrib['name']: { 'rows': [], 'values': [] } } );
  if(gettable.tag=="table"):
   columnstart = 0;
   for getcolumn in gettable:
    if(getcolumn.tag=="column"):
     columnstart = 1;
     rowinfonum = 0;
     for getcolumninfo in getcolumn:
      if(getcolumninfo.tag=="rowinfo"):
       defaultvale = getcolumninfo.attrib['defaultvalue'];
       if(defaultvale.isdigit()):
        defaultvale = int(defaultvale);
       if(defaultvale=="None"):
        defaultvale = None;
       leaguearrayout[gettable.attrib['name']].update( { getcolumninfo.attrib['name']: { 'info': {'id': int(getcolumninfo.attrib['id']), 'Name': getcolumninfo.attrib['name'], 'Type': getcolumninfo.attrib['type'], 'NotNull': int(getcolumninfo.attrib['notnull']), 'DefualtValue': ConvertXMLValuesForPython(defaultvale), 'PrimaryKey': int(getcolumninfo.attrib['primarykey']), 'AutoIncrement': int(getcolumninfo.attrib['autoincrement']), 'Hidden': int(getcolumninfo.attrib['hidden']) } } } );
       rowinfonum = rowinfonum + 1;
   datastart = 0;
   for getdata in gettable:
    if(getdata.tag=="data"):
     datastart = 1;
     rowstart = 0;
     rowdatanum = 0;
     for getrow in getdata:
      if(getrow.tag=="row"):
       rowstart = 1;
       rowdatanum = 0;
       rowdatadict = {};
       for getrowdata in getrow:
        if(getrowdata.tag=="rowdata"):
         rowdatadict.update( { getrowdata.attrib['name']: getrowdata.attrib['value'] } );
         rowdatanum = rowdatanum + 1;
       leaguearrayout[gettable.attrib['name']]['values'].append( rowdatadict );
   rowsstart = 0;
   rowscount = 0;
   for getrows in gettable:
    if(getrows.tag=="rows"):
     rowsstart = 1;
     rowscount = 0;
     for getrowlist in getcolumn:
      if(getrowlist.tag=="rowlist"):
       leaguearrayout[gettable.attrib['name']]['rows'].append(getrowlist.attrib['name']);
       rowscount = rowscount + 1;
 if(not CheckHockeySQLiteArray(leaguearrayout)):
  return False;
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(leaguearrayout, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 return leaguearrayout;

def MakeHockeyArrayFromHockeySQLiteArray(inhockeyarray, verbose=True, jsonverbose=True):
 if(not CheckHockeySQLiteArray(inhockeyarray)):
  return False;
 inchockeyarray = deepcopy(inhockeyarray);
 leaguearrayout = { 'database': str(inchockeyarray['database']) };
 leaguelist = [];
 for leagueinfo in inchockeyarray['HockeyLeagues']['values']:
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
  conferencelist = [];
  conarrayname = leagueinfo['LeagueName']+"Conferences";
  for conferenceinfo in inchockeyarray[conarrayname]['values']:
   leaguearray[str(leagueinfo['LeagueName'])].update( { str(conferenceinfo['Conference']): { 'conferenceinfo': { 'name': str(conferenceinfo['Conference']), 'prefix': str(conferenceinfo['ConferencePrefix']), 'suffix': str(conferenceinfo['ConferenceSuffix']), 'fullname': str(conferenceinfo['FullName']), 'league': str(leagueinfo['LeagueName']) } } } );
   leaguearray[str(leagueinfo['LeagueName'])]['quickinfo']['conferenceinfo'].update( { str(conferenceinfo['Conference']): { 'name': str(conferenceinfo['Conference']), 'fullname': str(conferenceinfo['FullName']), 'league': str(leagueinfo['LeagueName']) } } );
   conferencelist.append(str(conferenceinfo['Conference']));
   divisionlist = [];
   divarrayname = leagueinfo['LeagueName']+"Divisions";
   for divisioninfo in inchockeyarray[divarrayname]['values']:
    leaguearray[str(leagueinfo['LeagueName'])][str(conferenceinfo['Conference'])].update( { str(divisioninfo['Division']): { 'divisioninfo': { 'name': str(divisioninfo['Division']), 'prefix': str(divisioninfo['DivisionPrefix']), 'suffix': str(divisioninfo['DivisionSuffix']), 'fullname': str(divisioninfo['FullName']), 'league': str(leagueinfo['LeagueName']), 'conference': str(conferenceinfo['Conference']) } } } );
    leaguearray[str(leagueinfo['LeagueName'])]['quickinfo']['divisioninfo'].update( { str(divisioninfo['Division']): { 'name': str(divisioninfo['Division']), 'fullname': str(divisioninfo['FullName']), 'league': str(leagueinfo['LeagueName']), 'conference': str(conferenceinfo['Conference']) } } );
    divisionlist.append(str(divisioninfo['Division']));
    teamlist = [];
    teamarrayname = leagueinfo['LeagueName']+"Teams";
    for teaminfo in inchockeyarray[teamarrayname]['values']:
     fullteamname = GetFullTeamName(str(teaminfo['TeamName']), str(teaminfo['TeamPrefix']), str(teaminfo['TeamSuffix']));
     leaguearray[str(leagueinfo['LeagueName'])][str(conferenceinfo['Conference'])][str(divisioninfo['Division'])].update( { str(teaminfo['TeamName']): { 'teaminfo': { 'city': str(teaminfo['CityName']), 'area': str(teaminfo['AreaName']), 'fullarea': str(teaminfo['FullAreaName']), 'country': str(teaminfo['CountryName']), 'fullcountry': str(teaminfo['FullCountryName']), 'name': str(teaminfo['TeamName']), 'fullname': fullteamname, 'arena': str(teaminfo['ArenaName']), 'prefix': str(teaminfo['TeamPrefix']), 'suffix': str(teaminfo['TeamSuffix']), 'league': str(leagueinfo['LeagueName']), 'conference': str(conferenceinfo['Conference']), 'division': str(divisioninfo['Division']), 'affiliates': str(teaminfo['Affiliates']) } } } );
     leaguearray[str(leagueinfo['LeagueName'])]['quickinfo']['teaminfo'].update( { str(teaminfo['TeamName']): { 'name': str(teaminfo['TeamName']), 'fullname': fullteamname, 'league': str(leagueinfo['LeagueName']), 'conference': str(conferenceinfo['Conference']), 'division': str(divisioninfo['Division']) } } );
     teamlist.append(str(teaminfo['TeamName']));
    leaguearray[str(leagueinfo['LeagueName'])][str(conferenceinfo['Conference'])][str(divisioninfo['Division'])].update( { 'teamlist': teamlist } );
   leaguearray[str(leagueinfo['LeagueName'])][str(conferenceinfo['Conference'])].update( { 'divisionlist': divisionlist } );
  leaguearray[str(leagueinfo['LeagueName'])].update( { 'conferencelist': conferencelist } );
  araarrayname = leagueinfo['LeagueName']+"Arenas";
  getteam_num = len(inchockeyarray[teamarrayname]['values']);
  if(getteam_num>0):
   for arenainfo in inchockeyarray[teamarrayname]['values']:
    arenalist.append( { 'city': str(arenainfo['CityName']), 'area': str(arenainfo['AreaName']), 'fullarea': str(arenainfo['FullAreaName']), 'country': str(arenainfo['CountryName']), 'fullcountry': str(arenainfo['FullCountryName']), 'name': str(arenainfo['ArenaName']) } );
  leaguearray[str(leagueinfo['LeagueName'])].update( { "arenas": arenalist } );
  gamearrayname = leagueinfo['LeagueName']+"Games";
  getgame_num = len(inchockeyarray[gamearrayname]['values']);
  if(getgame_num>0):
   for gameinfo in inchockeyarray[gamearrayname]['values']:
    gamelist.append( { 'date': str(gameinfo['Date']), 'time': str(gameinfo['Time']), 'hometeam': str(gameinfo['HomeTeam']), 'awayteam': str(gameinfo['AwayTeam']), 'goals': str(gameinfo['TeamScorePeriods']), 'sogs': str(gameinfo['ShotsOnGoal']), 'ppgs': str(gameinfo['PowerPlays']), 'shgs': str(gameinfo['ShortHanded']), 'penalties': str(gameinfo['Penalties']), 'pims': str(gameinfo['PenaltyMinutes']), 'hits': str(gameinfo['HitsPerPeriod']), 'takeaways': str(gameinfo['TakeAways']), 'faceoffwins': str(gameinfo['FaceoffWins']), 'atarena': str(gameinfo['AtArena']), 'isplayoffgame': str(gameinfo['IsPlayOffGame']) } );
  leaguearray[str(leagueinfo['LeagueName'])].update( { "games": gamelist } );
  leaguearrayout.update(leaguearray);
 leaguearrayout.update( { 'leaguelist': leaguelist } );
 if(not CheckHockeyArray(leaguearrayout)):
  return False;
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(leaguearrayout, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 return leaguearrayout;

def MakeHockeySQLFromHockeySQLiteArray(inhockeyarray, insdbfile=":memory:", verbose=True, jsonverbose=True):
 if(not CheckHockeySQLiteArray(inhockeyarray)):
  return False;
 inchockeyarray = deepcopy(inhockeyarray);
 if(insdbfile is None or insdbfile==":memory:"):
  insdbfile = inchockeyarray['database'];
 #all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games", "PlayoffTeams"];
 all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games"];
 table_list = ['HockeyLeagues'];
 for leagueinfo_tmp in inchockeyarray['HockeyLeagues']['values']:
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
 sqldump = sqldump+"-- Database: "+insdbfile+"\n";
 sqldump = sqldump+"--\n\n";
 sqldump = sqldump+"-- --------------------------------------------------------\n\n";
 for get_cur_tab in table_list:
  sqldump = sqldump+"--\n";
  sqldump = sqldump+"-- Table structure for table "+str(get_cur_tab)+"\n";
  sqldump = sqldump+"--\n\n";
  sqldump = sqldump+"DROP TABLE IF EXISTS "+get_cur_tab+"\n\n";
  sqldump = sqldump+"CREATE TEMP TABLE "+get_cur_tab+" (\n";
  rowlen = len(inchockeyarray[get_cur_tab]['rows']);
  rowi = 0;
  sqlrowlist = [];
  for rowinfo in inchockeyarray[get_cur_tab]['rows']:
   sqlrowline = inchockeyarray[get_cur_tab][rowinfo]['info']['Name']+" "+inchockeyarray[get_cur_tab][rowinfo]['info']['Type'];
   if(inchockeyarray[get_cur_tab][rowinfo]['info']['NotNull']==1):
    sqlrowline = sqlrowline+" NOT NULL";
   if(inchockeyarray[get_cur_tab][rowinfo]['info']['DefualtValue'] is not None):
    sqlrowline = sqlrowline+" "+inchockeyarray[get_cur_tab][rowinfo]['info']['DefualtValue'];
   if(inchockeyarray[get_cur_tab][rowinfo]['info']['PrimaryKey']==1):
    sqlrowline = sqlrowline+" PRIMARY KEY";
   if(inchockeyarray[get_cur_tab][rowinfo]['info']['AutoIncrement']==1):
    sqlrowline = sqlrowline+" AUTOINCREMENT";
   sqlrowlist.append(sqlrowline);
  sqldump = sqldump+str(',\n'.join(sqlrowlist))+"\n);\n\n";
  sqldump = sqldump+"--\n";
  sqldump = sqldump+"-- Dumping data for table "+str(get_cur_tab)+"\n";
  sqldump = sqldump+"--\n\n";
  for rowvalues in inchockeyarray[get_cur_tab]['values']:
   rkeylist = [];
   rvaluelist = [];
   for rkey, rvalue in rowvalues.items():
    rkeylist.append(rkey);
    if(isinstance(rvalue, basestring)):
     rvalue = "\""+rvalue+"\"";
    rvaluelist.append(str(rvalue));
   sqldump = sqldump+"INSERT INTO "+str(get_cur_tab)+" ("+str(', '.join(rkeylist))+") VALUES\n";
   sqldump = sqldump+"("+str(', '.join(rvaluelist))+");\n";
  sqldump = sqldump+"\n-- --------------------------------------------------------\n\n";
 if(verbose and jsonverbose):
  VerbosePrintOut(MakeHockeyJSONFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 elif(verbose and not jsonverbose):
  VerbosePrintOut(MakeHockeyXMLFromHockeyArray(inhockeyarray, verbose=False, jsonverbose=True));
 return sqldump;

def MakeHockeySQLFileFromHockeySQLiteArray(inhockeyarray, outsqlfile=None, returnsql=False, verbose=True, jsonverbose=True):
 if(outsqlfile is None):
  return False;
 compressionlist = ['auto', 'gzip', 'bzip2', 'lzma', 'xz'];
 outextlist = ['gz', 'bz2', 'lzma', 'xz'];
 outextlistwd = ['.gz', '.bz2', '.lzma', '.xz'];
 fbasename = os.path.splitext(outsqlfile)[0];
 fextname = os.path.splitext(outsqlfile)[1];
 sqlfp = CompressOpenFile(outsqlfile);
 sqlstring = MakeHockeySQLFromHockeySQLiteArray(inhockeyarray, os.path.splitext(outsqlfile)[0]+".db3", verbose);
 if(fextname==".gz" or fextname==".bz2" or fextname==".xz" or fextname==".lzma"):
  sqlstring = sqlstring.encode();
 sqlfp.write(sqlstring);
 sqlfp.close();
 if(returnsql):
  return sqlstring;
 if(not returnsql):
  return True;
 return True;
