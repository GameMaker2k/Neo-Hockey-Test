#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2015-2024 Game Maker 2k - https://github.com/GameMaker2k
    Copyright 2015-2024 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: hockeyshortcuts.py - Last Update: 10/11/2024 Ver. 0.9.2 RC 1 - Author: cooldude2k $
'''

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import os
import re
import sqlite3
import sys
import time

# Python 2 handling: Reload sys and set UTF-8 encoding if applicable
try:
    reload(sys)  # Only relevant for Python 2
    if hasattr(sys, "setdefaultencoding"):
        sys.setdefaultencoding('UTF-8')
except (NameError, AttributeError):
    pass

# Python 3 handling: Ensure stdout and stderr use UTF-8 encoding
if hasattr(sys.stdout, "detach"):
    import io
    sys.stdout = io.TextIOWrapper(
        sys.stdout.detach(), encoding='UTF-8', errors='replace')
if hasattr(sys.stderr, "detach"):
    import io
    sys.stderr = io.TextIOWrapper(
        sys.stderr.detach(), encoding='UTF-8', errors='replace')
from .hockeyoopfuncs import *
from .versioninfo import (__author__, __copyright__, __credits__, __email__,
                          __license__, __license_string__, __maintainer__,
                          __program_alt_name__, __program_name__, __project__,
                          __project_release_url__, __project_url__,
                          __revision__, __revision_id__, __status__,
                          __version__, __version_alt__, __version_date__,
                          __version_date_alt__, __version_date_info__,
                          __version_date_plusrc__, __version_info__,
                          version_date, version_info)

try:
    basestring
except NameError:
    basestring = str

baseint = []
try:
    baseint.append(long)
    baseint.insert(0, int)
except NameError:
    baseint.append(int)
baseint = tuple(baseint)

pickledef = None
try:
    pickledef = pickle.DEFAULT_PROTOCOL
except AttributeError:
    pickledef = 2


def MakeHockeyArrayFromHockeyDataByDict(informat="xml", **funcargs):
    informat = informat.lower()
    if (informat == "xml"):
        if ("infile" in funcargs and "inxmlfile" not in funcargs):
            funcargs['inxmlfile'] = funcargs['infile']
            del funcargs['infile']
        return MakeHockeyArrayFromHockeyXML(**funcargs)
    elif (informat == "json"):
        if ("infile" in funcargs and "injsonfile" not in funcargs):
            funcargs['injsonfile'] = funcargs['infile']
            del funcargs['infile']
        return MakeHockeyArrayFromHockeyJSON(**funcargs)
    elif (informat == "pickle"):
        if ("infile" in funcargs and "inpicklefile" not in funcargs):
            funcargs['inpicklefile'] = funcargs['infile']
            del funcargs['infile']
        return MakeHockeyArrayFromHockeyPickle(**funcargs)
    elif (informat == "marshal"):
        if ("infile" in funcargs and "inmarshalfile" not in funcargs):
            funcargs['inmarshalfile'] = funcargs['infile']
            del funcargs['infile']
        return MakeHockeyArrayFromHockeyPickle(**funcargs)
    elif (informat == "database"):
        if ("infile" in funcargs and "insdbfile" not in funcargs):
            funcargs['insdbfile'] = funcargs['infile']
            del funcargs['infile']
        return MakeHockeyArrayFromHockeyDatabase(**funcargs)
    elif (informat == "olddatabase"):
        if ("infile" in funcargs and "insdbfile" not in funcargs):
            funcargs['insdbfile'] = funcargs['infile']
            del funcargs['infile']
        return MakeHockeyArrayFromOldHockeyDatabase(**funcargs)
    elif (informat == "sql"):
        if ("infile" in funcargs and "insqlfile" not in funcargs):
            funcargs['insqlfile'] = funcargs['infile']
            del funcargs['infile']
        return MakeHockeyArrayFromHockeySQL(**funcargs)
    elif (informat == "array"):
        return MakeHockeyArrayFromHockeySQLiteArray(**funcargs)
    else:
        return False
    return False


def MakeHockeyArrayFromHockeyDataByList(informat="xml", *funcargs):
    informat = informat.lower()
    if (informat == "xml"):
        return MakeHockeyArrayFromHockeyXML(*funcargs)
    elif (informat == "json"):
        return MakeHockeyArrayFromHockeyJSON(*funcargs)
    elif (informat == "pickle"):
        return MakeHockeyArrayFromHockeyPickle(*funcargs)
    elif (informat == "marshal"):
        return MakeHockeyArrayFromHockeyPickle(*funcargs)
    elif (informat == "database"):
        return MakeHockeyArrayFromHockeyDatabase(*funcargs)
    elif (informat == "olddatabase"):
        return MakeHockeyArrayFromOldHockeyDatabase(*funcargs)
    elif (informat == "sql"):
        return MakeHockeyArrayFromHockeySQL(*funcargs)
    elif (informat == "array"):
        return MakeHockeyArrayFromHockeySQLiteArray(*funcargs)
    else:
        return False
    return False


def MakeHockeyArrayFromHockeyData(funcargs):
    if (funcargs is not None and isinstance(funcargs, (tuple, list))):
        return MakeHockeyArrayFromHockeyDataByList(*funcargs)
    elif (funcargs is not None and isinstance(funcargs, (dict))):
        return MakeHockeyArrayFromHockeyDataByDict(**funcargs)
    else:
        return False
    return False


def MakeHockeyDataFromHockeyArrayByDict(outformat="xml", **funcargs):
    outformat = outformat.lower()
    if (outformat == "xml"):
        return MakeHockeyXMLFromHockeyArray(**funcargs)
    elif (outformat == "xmlalt"):
        return MakeHockeyXMLAltFromHockeyArray(**funcargs)
    elif (outformat == "sgml"):
        return MakeHockeySGMLFromHockeyArray(**funcargs)
    elif (outformat == "json"):
        return MakeHockeyJSONFromHockeyArray(**funcargs)
    elif (outformat == "pickle"):
        return MakeHockeyPickleFromHockeyArray(**funcargs)
    elif (outformat == "marshal"):
        return MakeHockeyMarshalFromHockeyArray(**funcargs)
    elif (outformat == "database"):
        return MakeHockeyDatabaseFromHockeyArray(**funcargs)
    elif (outformat == "py"):
        return MakeHockeyPythonFromHockeyArray(**funcargs)
    elif (outformat == "pyalt"):
        return MakeHockeyPythonAltFromHockeyArray(**funcargs)
    elif (outformat == "pyoop"):
        return MakeHockeyPythonOOPFromHockeyArray(**funcargs)
    elif (outformat == "pyoopalt"):
        return MakeHockeyPythonOOPAltFromHockeyArray(**funcargs)
    elif (outformat == "sql"):
        return MakeHockeySQLFromHockeyArray(**funcargs)
    elif (outformat == "array"):
        return MakeHockeySQLiteArrayFromHockeyArray(**funcargs)
    else:
        return False
    return False


def MakeHockeyDataFromHockeyArrayByList(outformat="xml", *funcargs):
    outformat = outformat.lower()
    if (outformat == "xml"):
        return MakeHockeyXMLFromHockeyArray(*funcargs)
    elif (outformat == "xmlalt"):
        return MakeHockeyXMLAltFromHockeyArray(*funcargs)
    elif (outformat == "sgml"):
        return MakeHockeySGMLFromHockeyArray(*funcargs)
    elif (outformat == "json"):
        return MakeHockeyJSONFromHockeyArray(*funcargs)
    elif (outformat == "pickle"):
        return MakeHockeyPickleFromHockeyArray(*funcargs)
    elif (outformat == "marshal"):
        return MakeHockeyMarshalFromHockeyArray(*funcargs)
    elif (outformat == "database"):
        return MakeHockeyDatabaseFromHockeyArray(*funcargs)
    elif (outformat == "py"):
        return MakeHockeyPythonFromHockeyArray(*funcargs)
    elif (outformat == "pyalt"):
        return MakeHockeyPythonAltFromHockeyArray(*funcargs)
    elif (outformat == "pyoop"):
        return MakeHockeyPythonOOPFromHockeyArray(*funcargs)
    elif (outformat == "pyoopalt"):
        return MakeHockeyPythonOOPAltFromHockeyArray(*funcargs)
    elif (outformat == "sql"):
        return MakeHockeySQLFromHockeyArray(*funcargs)
    elif (outformat == "array"):
        return MakeHockeySQLiteArrayFromHockeyArray(*funcargs)
    else:
        return False
    return False


def MakeHockeyDataFromHockeyArray(funcargs):
    if (funcargs is not None and isinstance(funcargs, (tuple, list))):
        return MakeHockeyDataFromHockeyArrayByList(*funcargs)
    elif (funcargs is not None and isinstance(funcargs, (dict))):
        return MakeHockeyDataFromHockeyArrayByDict(**funcargs)
    else:
        return False
    return False


def MakeHockeyDataFileFromHockeyArrayByDict(outformat="xml", **funcargs):
    outformat = outformat.lower()
    if (outformat == "xml"):
        if ("outfile" in funcargs and "outxmlfile" not in funcargs):
            funcargs['outxmlfile'] = funcargs['outfile']
            del funcargs['outfile']
        return MakeHockeyXMLFileFromHockeyArray(**funcargs)
    elif (outformat == "xmlalt"):
        if ("outfile" in funcargs and "outxmlfile" not in funcargs):
            funcargs['outxmlfile'] = funcargs['outfile']
            del funcargs['outfile']
        return MakeHockeyXMLAltFileFromHockeyArray(**funcargs)
    elif (outformat == "sgml"):
        if ("outfile" in funcargs and "outxmlfile" not in funcargs):
            funcargs['outxmlfile'] = funcargs['outfile']
            del funcargs['outfile']
        return MakeHockeySGMLFileFromHockeyArray(**funcargs)
    elif (outformat == "json"):
        if ("outfile" in funcargs and "outjsonfile" not in funcargs):
            funcargs['outjsonfile'] = funcargs['outfile']
            del funcargs['outfile']
        return MakeHockeyJSONFileFromHockeyArray(**funcargs)
    elif (outformat == "pickle"):
        if ("outfile" in funcargs and "outpicklefile" not in funcargs):
            funcargs['outpicklefile'] = funcargs['outfile']
            del funcargs['outfile']
        return MakeHockeyPickleFileFromHockeyArray(**funcargs)
    elif (outformat == "marshal"):
        if ("outfile" in funcargs and "outmarshalfile" not in funcargs):
            funcargs['outmarshalfile'] = funcargs['outfile']
            del funcargs['outfile']
        return MakeHockeyMarshalFileFromHockeyArray(**funcargs)
    elif (outformat == "py"):
        if ("outfile" in funcargs and "outpyfile" not in funcargs):
            funcargs['outpyfile'] = funcargs['outfile']
            del funcargs['outfile']
        return MakeHockeyPythonFileFromHockeyArray(**funcargs)
    elif (outformat == "pyalt"):
        if ("outfile" in funcargs and "outpyfile" not in funcargs):
            funcargs['outpyfile'] = funcargs['outfile']
            del funcargs['outfile']
        return MakeHockeyPythonAltFileFromHockeyArray(**funcargs)
    elif (outformat == "pyoop"):
        if ("outfile" in funcargs and "outpyfile" not in funcargs):
            funcargs['outpyfile'] = funcargs['outfile']
            del funcargs['outfile']
        return MakeHockeyPythonOOPFileFromHockeyArray(**funcargs)
    elif (outformat == "pyoopalt"):
        if ("outfile" in funcargs and "outpyfile" not in funcargs):
            funcargs['outpyfile'] = funcargs['outfile']
            del funcargs['outfile']
        return MakeHockeyPythonOOPAltFileFromHockeyArray(**funcargs)
    elif (outformat == "sql"):
        if ("outfile" in funcargs and "outsqlfile" not in funcargs):
            funcargs['outsqlfile'] = funcargs['outfile']
            del funcargs['outfile']
        return MakeHockeySQLFileFromHockeyArray(**funcargs)
    else:
        return False
    return False


def MakeHockeyDataFileFromHockeyArrayByList(outformat="xml", *funcargs):
    outformat = outformat.lower()
    if (outformat == "xml"):
        return MakeHockeyXMLFileFromHockeyArray(*funcargs)
    elif (outformat == "xmlalt"):
        return MakeHockeyXMLAltFileFromHockeyArray(*funcargs)
    elif (outformat == "sgml"):
        return MakeHockeySGMLFileFromHockeyArray(*funcargs)
    elif (outformat == "json"):
        return MakeHockeyJSONFileFromHockeyArray(*funcargs)
    elif (outformat == "pickle"):
        return MakeHockeyPickleFileFromHockeyArray(*funcargs)
    elif (outformat == "marshal"):
        return MakeHockeyMarshalFileFromHockeyArray(*funcargs)
    elif (outformat == "py"):
        return MakeHockeyPythonFileFromHockeyArray(*funcargs)
    elif (outformat == "pyalt"):
        return MakeHockeyPythonAltFileFromHockeyArray(*funcargs)
    elif (outformat == "pyoop"):
        return MakeHockeyPythonOOPFileFromHockeyArray(*funcargs)
    elif (outformat == "pyoopalt"):
        return MakeHockeyPythonOOPAltFileFromHockeyArray(*funcargs)
    elif (outformat == "sql"):
        return MakeHockeySQLFileFromHockeyArray(*funcargs)
    else:
        return False
    return False


def MakeHockeyDataFileFromHockeyArray(funcargs):
    if (funcargs is not None and isinstance(funcargs, (tuple, list))):
        return MakeHockeyDataFileFromHockeyArrayByList(*funcargs)
    elif (funcargs is not None and isinstance(funcargs, (dict))):
        return MakeHockeyDataFileFromHockeyArrayByDict(**funcargs)
    else:
        return False
    return False


def MakeHockeySQLiteArrayFromHockeySQLiteDataByDict(informat="xml", **funcargs):
    informat = informat.lower()
    if (informat == "xml"):
        if ("infile" in funcargs and "inxmlfile" not in funcargs):
            funcargs['inxmlfile'] = funcargs['infile']
            del funcargs['infile']
        return MakeHockeySQLiteArrayFromHockeySQLiteXML(**funcargs)
    elif (informat == "json"):
        if ("infile" in funcargs and "injsonfile" not in funcargs):
            funcargs['injsonfile'] = funcargs['infile']
            del funcargs['infile']
        return MakeHockeySQLiteArrayFromHockeySQLiteJSON(**funcargs)
    elif (informat == "pickle"):
        if ("infile" in funcargs and "inpicklefile" not in funcargs):
            funcargs['inpicklefile'] = funcargs['infile']
            del funcargs['infile']
        return MakeHockeySQLiteArrayFromHockeySQLitePickle(**funcargs)
    elif (informat == "marshal"):
        if ("infile" in funcargs and "inmarshalfile" not in funcargs):
            funcargs['inmarshalfile'] = funcargs['infile']
            del funcargs['infile']
        return MakeHockeySQLiteArrayFromHockeySQLitePickle(**funcargs)
    elif (informat == "database"):
        if ("infile" in funcargs and "insdbfile" not in funcargs):
            funcargs['insdbfile'] = funcargs['infile']
            del funcargs['infile']
        return MakeHockeySQLiteArrayFromHockeyDatabase(**funcargs)
    elif (informat == "olddatabase"):
        if ("infile" in funcargs and "insdbfile" not in funcargs):
            funcargs['insdbfile'] = funcargs['infile']
            del funcargs['infile']
        return MakeHockeySQLiteArrayFromOldHockeyDatabase(**funcargs)
    elif (informat == "sql"):
        if ("infile" in funcargs and "insqlfile" not in funcargs):
            funcargs['insqlfile'] = funcargs['infile']
            del funcargs['infile']
        return MakeHockeySQLiteArrayFromHockeySQL(**funcargs)
    elif (informat == "array"):
        return MakeHockeySQLiteArrayFromHockeyArray(**funcargs)
    else:
        return False
    return False


def MakeHockeySQLiteArrayFromHockeySQLiteDataByList(informat="xml", *funcargs):
    informat = informat.lower()
    if (informat == "xml"):
        return MakeHockeySQLiteArrayFromHockeySQLiteXML(*funcargs)
    elif (informat == "json"):
        return MakeHockeySQLiteArrayFromHockeySQLiteJSON(*funcargs)
    elif (informat == "pickle"):
        return MakeHockeySQLiteArrayFromHockeySQLitePickle(*funcargs)
    elif (informat == "marshal"):
        return MakeHockeySQLiteArrayFromHockeySQLitePickle(*funcargs)
    elif (informat == "database"):
        return MakeHockeySQLiteArrayFromHockeyDatabase(*funcargs)
    elif (informat == "olddatabase"):
        return MakeHockeySQLiteArrayFromOldHockeyDatabase(*funcargs)
    elif (informat == "sql"):
        return MakeHockeySQLiteArrayFromHockeySQL(*funcargs)
    elif (informat == "array"):
        return MakeHockeySQLiteArrayFromHockeyArray(*funcargs)
    else:
        return False
    return False


def MakeHockeySQLiteArrayFromHockeySQLiteData(funcargs):
    if (funcargs is not None and isinstance(funcargs, (tuple, list))):
        return MakeHockeySQLiteArrayFromHockeySQLiteDataByList(*funcargs)
    elif (funcargs is not None and isinstance(funcargs, (dict))):
        return MakeHockeySQLiteArrayFromHockeySQLiteDataByDict(**funcargs)
    else:
        return False
    return False


def MakeHockeySQLiteDataFromHockeySQLiteArrayByDict(outformat="xml", **funcargs):
    outformat = outformat.lower()
    if (outformat == "xml"):
        return MakeHockeySQLiteXMLFromHockeySQLiteArray(**funcargs)
    elif (outformat == "xmlalt"):
        return MakeHockeySQLiteXMLAltFromHockeySQLiteArray(**funcargs)
    elif (outformat == "sgml"):
        return MakeHockeySQLiteSGMLFromHockeySQLiteArray(**funcargs)
    elif (outformat == "json"):
        return MakeHockeySQLiteJSONFromHockeySQLiteArray(**funcargs)
    elif (outformat == "pickle"):
        return MakeHockeySQLitePickleFromHockeySQLiteArray(**funcargs)
    elif (outformat == "marshal"):
        return MakeHockeySQLiteMarshalFromHockeySQLiteArray(**funcargs)
    elif (outformat == "database"):
        return MakeHockeyDatabaseFromHockeySQLiteArray(**funcargs)
    elif (outformat == "py"):
        return MakeHockeyPythonFromHockeySQLiteArray(**funcargs)
    elif (outformat == "pyalt"):
        return MakeHockeyPythonAltFromHockeySQLiteArray(**funcargs)
    elif (outformat == "pyoop"):
        return MakeHockeyPythonOOPFromHockeySQLiteArray(**funcargs)
    elif (outformat == "pyoopalt"):
        return MakeHockeyPythonOOPAltFromHockeySQLiteArray(**funcargs)
    elif (outformat == "sql"):
        return MakeHockeySQLFromHockeySQLiteArray(**funcargs)
    elif (outformat == "array"):
        return MakeHockeyArrayFromHockeySQLiteArray(**funcargs)
    else:
        return False
    return False


def MakeHockeySQLiteDataFromHockeySQLiteArrayByList(outformat="xml", *funcargs):
    outformat = outformat.lower()
    if (outformat == "xml"):
        return MakeHockeySQLiteXMLFromHockeySQLiteArray(*funcargs)
    elif (outformat == "xmlalt"):
        return MakeHockeySQLiteXMLAltFromHockeySQLiteArray(*funcargs)
    elif (outformat == "sgml"):
        return MakeHockeySQLiteSGMLFromHockeySQLiteArray(*funcargs)
    elif (outformat == "json"):
        return MakeHockeySQLiteJSONFromHockeySQLiteArray(*funcargs)
    elif (outformat == "pickle"):
        return MakeHockeySQLitePickleFromHockeySQLiteArray(*funcargs)
    elif (outformat == "marshal"):
        return MakeHockeySQLiteMarshalFromHockeySQLiteArray(*funcargs)
    elif (outformat == "database"):
        return MakeHockeyDatabaseFromHockeySQLiteArray(*funcargs)
    elif (outformat == "py"):
        return MakeHockeyPythonFromHockeySQLiteArray(*funcargs)
    elif (outformat == "pyalt"):
        return MakeHockeyPythonAltFromHockeySQLiteArray(*funcargs)
    elif (outformat == "pyoop"):
        return MakeHockeyPythonOOPFromHockeySQLiteArray(*funcargs)
    elif (outformat == "pyoopalt"):
        return MakeHockeyPythonOOPAltFromHockeySQLiteArray(*funcargs)
    elif (outformat == "sql"):
        return MakeHockeySQLFromHockeySQLiteArray(*funcargs)
    elif (outformat == "array"):
        return MakeHockeyArrayFromHockeySQLiteArray(*funcargs)
    else:
        return False
    return False


def MakeHockeySQLiteDataFromHockeySQLiteArray(funcargs):
    if (funcargs is not None and isinstance(funcargs, (tuple, list))):
        return MakeHockeySQLiteDataFromHockeySQLiteArrayByList(*funcargs)
    elif (funcargs is not None and isinstance(funcargs, (dict))):
        return MakeHockeySQLiteDataFromHockeySQLiteArrayByDict(**funcargs)
    else:
        return False
    return False


def MakeHockeySQLiteDataFileFromHockeySQLiteArrayByDict(outformat="xml", **funcargs):
    outformat = outformat.lower()
    if (outformat == "xml"):
        return MakeHockeySQLiteXMLFileFromHockeySQLiteArray(**funcargs)
    elif (outformat == "xmlalt"):
        return MakeHockeySQLiteXMLAltFileFromHockeySQLiteArray(**funcargs)
    elif (outformat == "sgml"):
        return MakeHockeySQLiteSGMLFileFromHockeySQLiteArray(**funcargs)
    elif (outformat == "json"):
        return MakeHockeySQLiteJSONFileFromHockeySQLiteArray(**funcargs)
    elif (outformat == "pickle"):
        return MakeHockeySQLitePickleFileFromHockeySQLiteArray(**funcargs)
    elif (outformat == "marshal"):
        return MakeHockeySQLiteMarshalFileFromHockeySQLiteArray(**funcargs)
    elif (outformat == "py"):
        return MakeHockeyPythonFileFromHockeySQLiteArray(**funcargs)
    elif (outformat == "pyalt"):
        return MakeHockeyPythonAltFileFromHockeySQLiteArray(**funcargs)
    elif (outformat == "pyoop"):
        return MakeHockeyPythonOOPFileFromHockeySQLiteArray(**funcargs)
    elif (outformat == "pyoopalt"):
        return MakeHockeyPythonOOPAltFileFromHockeySQLiteArray(**funcargs)
    elif (outformat == "sql"):
        return MakeHockeySQLFileFromHockeySQLiteArray(**funcargs)
    else:
        return False
    return False


def MakeHockeySQLiteDataFileFromHockeySQLiteArrayByList(outformat="xml", *funcargs):
    outformat = outformat.lower()
    if (outformat == "xml"):
        return MakeHockeySQLiteXMLFileFromHockeySQLiteArray(*funcargs)
    elif (outformat == "xmlalt"):
        return MakeHockeySQLiteXMLAltFileFromHockeySQLiteArray(*funcargs)
    elif (outformat == "sgml"):
        return MakeHockeySQLiteSGMLFileFromHockeySQLiteArray(*funcargs)
    elif (outformat == "json"):
        return MakeHockeySQLiteJSONFileFromHockeySQLiteArray(*funcargs)
    elif (outformat == "pickle"):
        return MakeHockeySQLitePickleFileFromHockeySQLiteArray(*funcargs)
    elif (outformat == "marshal"):
        return MakeHockeySQLiteMarshalFileFromHockeySQLiteArray(*funcargs)
    elif (outformat == "py"):
        return MakeHockeyPythonFileFromHockeySQLiteArray(*funcargs)
    elif (outformat == "pyalt"):
        return MakeHockeyPythonAltFileFromHockeySQLiteArray(*funcargs)
    elif (outformat == "pyoop"):
        return MakeHockeyPythonOOPFileFromHockeySQLiteArray(*funcargs)
    elif (outformat == "pyoopalt"):
        return MakeHockeyPythonOOPAltFileFromHockeySQLiteArray(*funcargs)
    elif (outformat == "sql"):
        return MakeHockeySQLFileFromHockeySQLiteArray(*funcargs)
    else:
        return False
    return False


def MakeHockeySQLiteDataFileFromHockeySQLiteArray(funcargs):
    if (funcargs is not None and isinstance(funcargs, (tuple, list))):
        return MakeHockeySQLiteDataFileFromHockeySQLiteArrayByList(*funcargs)
    elif (funcargs is not None and isinstance(funcargs, (dict))):
        return MakeHockeySQLiteDataFileFromHockeySQLiteArrayByDict(**funcargs)
    else:
        return False
    return False


def MakeHockeyDataFromHockeyData(infuncargs, outfuncargs):
    if (infuncargs is not None and isinstance(infuncargs, (tuple, list))):
        inhockeyarray = MakeHockeyArrayFromHockeyDataByList(*infuncargs)
    elif (infuncargs is not None and isinstance(infuncargs, (dict))):
        inhockeyarray = MakeHockeyArrayFromHockeyDataByDict(**infuncargs)
    else:
        return False
    if (outfuncargs is not None and isinstance(outfuncargs, (tuple, list))):
        if (len(outfuncargs) > 1):
            outfuncargs[1] = inhockeyarray
        else:
            outfuncargs.append(inhockeyarray)
        return MakeHockeyDataFromHockeyArrayByList(*outfuncargs)
    elif (outfuncargs is not None and isinstance(outfuncargs, (dict))):
        outfuncargs.update({'inhockeyarray': inhockeyarray})
        return MakeHockeyDataFromHockeyArrayByDict(**outfuncargs)
    else:
        return False
    return False


def MakeHockeyDataFileFromHockeyData(infuncargs, outfuncargs):
    if (infuncargs is not None and isinstance(infuncargs, (tuple, list))):
        inhockeyarray = MakeHockeyArrayFromHockeyDataByList(*infuncargs)
    elif (infuncargs is not None and isinstance(infuncargs, (dict))):
        inhockeyarray = MakeHockeyArrayFromHockeyDataByDict(**infuncargs)
    else:
        return False
    if (outfuncargs is not None and isinstance(outfuncargs, (tuple, list))):
        if (len(outfuncargs) > 1):
            outfuncargs[1] = inhockeyarray
        else:
            outfuncargs.append(inhockeyarray)
        return MakeHockeyDataFileFromHockeyArrayByList(*outfuncargs)
    elif (outfuncargs is not None and isinstance(outfuncargs, (dict))):
        outfuncargs.update({'inhockeyarray': inhockeyarray})
        return MakeHockeyDataFileFromHockeyArrayByDict(**outfuncargs)
    else:
        return False
    return False


def MakeHockeyDataFromHockeySQLiteData(infuncargs, outfuncargs):
    if (infuncargs is not None and isinstance(infuncargs, (tuple, list))):
        inhockeyarray = MakeHockeySQLiteArrayFromHockeySQLiteDataByList(
            *infuncargs)
    elif (infuncargs is not None and isinstance(infuncargs, (dict))):
        inhockeyarray = MakeHockeySQLiteArrayFromHockeySQLiteDataByDict(
            **infuncargs)
    else:
        return False
    inhockeyarray = MakeHockeyArrayFromHockeySQLiteArray(
        inhockeyarray, False, False)
    if (outfuncargs is not None and isinstance(outfuncargs, (tuple, list))):
        if (len(outfuncargs) > 1):
            outfuncargs[1] = inhockeyarray
        else:
            outfuncargs.append(inhockeyarray)
        return MakeHockeyDataFromHockeyArrayByList(*outfuncargs)
    elif (outfuncargs is not None and isinstance(outfuncargs, (dict))):
        outfuncargs.update({'inhockeyarray': inhockeyarray})
        return MakeHockeyDataFromHockeyArrayByDict(**outfuncargs)
    else:
        return False
    return False


def MakeHockeyDataFileFromHockeySQLiteData(infuncargs, outfuncargs):
    if (infuncargs is not None and isinstance(infuncargs, (tuple, list))):
        inhockeyarray = MakeHockeySQLiteArrayFromHockeySQLiteDataByList(
            *infuncargs)
    elif (infuncargs is not None and isinstance(infuncargs, (dict))):
        inhockeyarray = MakeHockeySQLiteArrayFromHockeySQLiteDataByDict(
            **infuncargs)
    else:
        return False
    inhockeyarray = MakeHockeyArrayFromHockeySQLiteArray(
        inhockeyarray, False, False)
    if (outfuncargs is not None and isinstance(outfuncargs, (tuple, list))):
        if (len(outfuncargs) > 1):
            outfuncargs[1] = inhockeyarray
        else:
            outfuncargs.append(inhockeyarray)
        return MakeHockeyDataFileFromHockeyArrayByList(*outfuncargs)
    elif (outfuncargs is not None and isinstance(outfuncargs, (dict))):
        outfuncargs.update({'inhockeyarray': inhockeyarray})
        return MakeHockeyDataFileFromHockeyArrayByDict(**outfuncargs)
    else:
        return False
    return False


def MakeHockeySQLiteDataFromHockeySQLiteData(infuncargs, outfuncargs):
    if (infuncargs is not None and isinstance(infuncargs, (tuple, list))):
        inhockeyarray = MakeHockeySQLiteArrayFromHockeySQLiteDataByList(
            *infuncargs)
    elif (infuncargs is not None and isinstance(infuncargs, (dict))):
        inhockeyarray = MakeHockeySQLiteArrayFromHockeySQLiteDataByDict(
            **infuncargs)
    else:
        return False
    if (outfuncargs is not None and isinstance(outfuncargs, (tuple, list))):
        if (len(outfuncargs) > 1):
            outfuncargs[1] = inhockeyarray
        else:
            outfuncargs.append(inhockeyarray)
        return MakeHockeySQLiteDataFromHockeySQLiteArrayByList(*outfuncargs)
    elif (outfuncargs is not None and isinstance(outfuncargs, (dict))):
        outfuncargs.update({'inhockeyarray': inhockeyarray})
        return MakeHockeySQLiteDataFromHockeySQLiteArrayByDict(**outfuncargs)
    else:
        return False
    return False


def MakeHockeySQLiteDataFileFromHockeySQLiteData(infuncargs, outfuncargs):
    if (infuncargs is not None and isinstance(infuncargs, (tuple, list))):
        inhockeyarray = MakeHockeySQLiteArrayFromHockeySQLiteDataByList(
            *infuncargs)
    elif (infuncargs is not None and isinstance(infuncargs, (dict))):
        inhockeyarray = MakeHockeySQLiteArrayFromHockeySQLiteDataByDict(
            **infuncargs)
    else:
        return False
    if (outfuncargs is not None and isinstance(outfuncargs, (tuple, list))):
        if (len(outfuncargs) > 1):
            outfuncargs[1] = inhockeyarray
        else:
            outfuncargs.append(inhockeyarray)
        return MakeHockeySQLiteDataFileFromHockeySQLiteArrayByList(*outfuncargs)
    elif (outfuncargs is not None and isinstance(outfuncargs, (dict))):
        outfuncargs.update({'inhockeyarray': inhockeyarray})
        return MakeHockeySQLiteDataFileFromHockeySQLiteArrayByDict(**outfuncargs)
    else:
        return False
    return False


def MakeHockeySQLiteDataFromHockeyData(infuncargs, outfuncargs):
    if (infuncargs is not None and isinstance(infuncargs, (tuple, list))):
        inhockeyarray = MakeHockeyArrayFromHockeyDataByList(*infuncargs)
    elif (infuncargs is not None and isinstance(infuncargs, (dict))):
        inhockeyarray = MakeHockeyArrayFromHockeyDataByDict(**infuncargs)
    else:
        return False
    inhockeyarray = MakeHockeySQLiteArrayFromHockeyArray(
        inhockeyarray, False, False)
    if (outfuncargs is not None and isinstance(outfuncargs, (tuple, list))):
        if (len(outfuncargs) > 1):
            outfuncargs[1] = inhockeyarray
        else:
            outfuncargs.append(inhockeyarray)
        return MakeHockeySQLiteDataFromHockeySQLiteArrayByList(*outfuncargs)
    elif (outfuncargs is not None and isinstance(outfuncargs, (dict))):
        outfuncargs.update({'inhockeyarray': inhockeyarray})
        return MakeHockeySQLiteDataFromHockeySQLiteArrayByDict(**outfuncargs)
    else:
        return False
    return False


def MakeHockeySQLiteDataFileFromHockeyData(infuncargs, outfuncargs):
    if (infuncargs is not None and isinstance(infuncargs, (tuple, list))):
        inhockeyarray = MakeHockeyArrayFromHockeyDataByList(*infuncargs)
    elif (infuncargs is not None and isinstance(infuncargs, (dict))):
        inhockeyarray = MakeHockeyArrayFromHockeyDataByDict(**infuncargs)
    else:
        return False
    inhockeyarray = MakeHockeySQLiteArrayFromHockeyArray(
        inhockeyarray, False, False)
    if (outfuncargs is not None and isinstance(outfuncargs, (tuple, list))):
        if (len(outfuncargs) > 1):
            outfuncargs[1] = inhockeyarray
        else:
            outfuncargs.append(inhockeyarray)
        return MakeHockeySQLiteDataFileFromHockeySQLiteArrayByList(*outfuncargs)
    elif (outfuncargs is not None and isinstance(outfuncargs, (dict))):
        outfuncargs.update({'inhockeyarray': inhockeyarray})
        return MakeHockeySQLiteDataFileFromHockeySQLiteArrayByDict(**outfuncargs)
    else:
        return False
    return False
