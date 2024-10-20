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

    $FileInfo: hockeyshortcuts.py - Last Update: 10/17/2024 Ver. 0.9.6 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals, generators, with_statement, nested_scopes

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
    input_file_key = 'infile'
    format_mappings = {
        'xml': ('inxmlfile', MakeHockeyArrayFromHockeyXML),
        'xmlalt': ('inxmlfile', MakeHockeyArrayFromHockeyXMLAlt),
        'sgml': ('insgmlfile', MakeHockeyArrayFromHockeySGML),
        'json': ('injsonfile', MakeHockeyArrayFromHockeyJSON),
        'yaml': ('inyamlfile', MakeHockeyArrayFromHockeyYAML),
        'pickle': ('inpicklefile', MakeHockeyArrayFromHockeyPickle),
        'marshal': ('inmarshalfile', MakeHockeyArrayFromHockeyPickle),
        'database': ('insdbfile', MakeHockeyArrayFromHockeyDatabase),
        'olddatabase': ('insdbfile', MakeHockeyArrayFromOldHockeyDatabase),
        'sql': ('insqlfile', MakeHockeyArrayFromHockeySQL),
        'array': ('inhockeyarray', MakeHockeyArrayFromHockeySQLiteArray)
    }

    if informat in format_mappings:
        file_key, function = format_mappings[informat]
        if file_key and input_file_key in funcargs:
            funcargs[file_key] = funcargs.pop(input_file_key)
        return function(**funcargs)
    return False

def MakeHockeyArrayFromHockeyDataByList(informat="xml", *funcargs):
    format_mappings = {
        'xml': MakeHockeyArrayFromHockeyXML,
        'xmlalt': MakeHockeyArrayFromHockeyXMLAlt,
        'sgml': MakeHockeyArrayFromHockeySGML,
        'json': MakeHockeyArrayFromHockeyJSON,
        'yaml': MakeHockeyArrayFromHockeyYAML,
        'pickle': MakeHockeyArrayFromHockeyPickle,
        'marshal': MakeHockeyArrayFromHockeyPickle,
        'database': MakeHockeyArrayFromHockeyDatabase,
        'olddatabase': MakeHockeyArrayFromOldHockeyDatabase,
        'sql': MakeHockeyArrayFromHockeySQL,
        'array': MakeHockeyArrayFromHockeySQLiteArray
    }
    return format_mappings.get(informat.lower(), lambda *args: False)(*funcargs)

def MakeHockeyArrayFromHockeyData(funcargs):
    if isinstance(funcargs, (tuple, list)):
        return MakeHockeyArrayFromHockeyDataByList(*funcargs)
    elif isinstance(funcargs, dict):
        return MakeHockeyArrayFromHockeyDataByDict(**funcargs)
    return False

def MakeHockeyDataFromHockeyArrayByDict(outformat="xml", **funcargs):
    outformat = outformat.lower()
    format_mappings = {
        'xml': MakeHockeyXMLFromHockeyArray,
        'xmlalt': MakeHockeyXMLAltFromHockeyArray,
        'sgml': MakeHockeySGMLFromHockeyArray,
        'json': MakeHockeyJSONFromHockeyArray,
        'yaml': MakeHockeyYAMLFromHockeyArray,
        'pickle': MakeHockeyPickleFromHockeyArray,
        'marshal': MakeHockeyMarshalFromHockeyArray,
        'database': MakeHockeyDatabaseFromHockeyArray,
        'py': MakeHockeyPythonFromHockeyArray,
        'pyalt': MakeHockeyPythonAltFromHockeyArray,
        'pyoop': MakeHockeyPythonOOPFromHockeyArray,
        'pyoopalt': MakeHockeyPythonOOPAltFromHockeyArray,
        'sql': MakeHockeySQLFromHockeyArray,
        'array': MakeHockeySQLiteArrayFromHockeyArray
    }
    return format_mappings.get(outformat, lambda **kwargs: False)(**funcargs)

def MakeHockeyDataFromHockeyArrayByList(outformat="xml", *funcargs):
    format_mappings = {
        'xml': MakeHockeyXMLFromHockeyArray,
        'xmlalt': MakeHockeyXMLAltFromHockeyArray,
        'sgml': MakeHockeySGMLFromHockeyArray,
        'json': MakeHockeyJSONFromHockeyArray,
        'yaml': MakeHockeyYAMLFromHockeyArray,
        'pickle': MakeHockeyPickleFromHockeyArray,
        'marshal': MakeHockeyMarshalFromHockeyArray,
        'database': MakeHockeyDatabaseFromHockeyArray,
        'py': MakeHockeyPythonFromHockeyArray,
        'pyalt': MakeHockeyPythonAltFromHockeyArray,
        'pyoop': MakeHockeyPythonOOPFromHockeyArray,
        'pyoopalt': MakeHockeyPythonOOPAltFromHockeyArray,
        'sql': MakeHockeySQLFromHockeyArray,
        'array': MakeHockeySQLiteArrayFromHockeyArray
    }
    return format_mappings.get(outformat.lower(), lambda *args: False)(*funcargs)

def MakeHockeyDataFromHockeyArray(funcargs):
    if isinstance(funcargs, (tuple, list)):
        return MakeHockeyDataFromHockeyArrayByList(*funcargs)
    elif isinstance(funcargs, dict):
        return MakeHockeyDataFromHockeyArrayByDict(**funcargs)
    return False

def MakeHockeyDataFileFromHockeyArrayByDict(outformat="xml", **funcargs):
    outformat = outformat.lower()
    file_format_mappings = {
        'xml': ('outxmlfile', MakeHockeyXMLFileFromHockeyArray),
        'xmlalt': ('outxmlfile', MakeHockeyXMLAltFileFromHockeyArray),
        'sgml': ('outsgmlfile', MakeHockeySGMLFileFromHockeyArray),
        'json': ('outjsonfile', MakeHockeyJSONFileFromHockeyArray),
        'yaml': ('outyamlfile', MakeHockeyYAMLFileFromHockeyArray),
        'pickle': ('outpicklefile', MakeHockeyPickleFileFromHockeyArray),
        'marshal': ('outmarshalfile', MakeHockeyMarshalFileFromHockeyArray),
        'py': ('outpyfile', MakeHockeyPythonFileFromHockeyArray),
        'pyalt': ('outpyfile', MakeHockeyPythonAltFileFromHockeyArray),
        'pyoop': ('outpyfile', MakeHockeyPythonOOPFileFromHockeyArray),
        'pyoopalt': ('outpyfile', MakeHockeyPythonOOPAltFileFromHockeyArray),
        'sql': ('outsqlfile', MakeHockeySQLFileFromHockeyArray)
    }

    if outformat in file_format_mappings:
        file_key, function = file_format_mappings[outformat]
        if file_key in funcargs and 'outfile' in funcargs:
            funcargs[file_key] = funcargs.pop('outfile')
        return function(**funcargs)
    return False

def MakeHockeyDataFileFromHockeyArrayByList(outformat="xml", *funcargs):
    file_format_mappings = {
        'xml': MakeHockeyXMLFileFromHockeyArray,
        'xmlalt': MakeHockeyXMLAltFileFromHockeyArray,
        'sgml': MakeHockeySGMLFileFromHockeyArray,
        'json': MakeHockeyJSONFileFromHockeyArray,
        'yaml': MakeHockeyYAMLFileFromHockeyArray,
        'pickle': MakeHockeyPickleFileFromHockeyArray,
        'marshal': MakeHockeyMarshalFileFromHockeyArray,
        'py': MakeHockeyPythonFileFromHockeyArray,
        'pyalt': MakeHockeyPythonAltFileFromHockeyArray,
        'pyoop': MakeHockeyPythonOOPFileFromHockeyArray,
        'pyoopalt': MakeHockeyPythonOOPAltFileFromHockeyArray,
        'sql': MakeHockeySQLFileFromHockeyArray
    }
    return file_format_mappings.get(outformat.lower(), lambda *args: False)(*funcargs)

def MakeHockeyDataFileFromHockeyArray(funcargs):
    if isinstance(funcargs, (tuple, list)):
        return MakeHockeyDataFileFromHockeyArrayByList(*funcargs)
    elif isinstance(funcargs, dict):
        return MakeHockeyDataFileFromHockeyArrayByDict(**funcargs)
    return False

def MakeHockeySQLiteArrayFromHockeySQLiteDataByDict(informat="xml", **funcargs):
    informat = informat.lower()
    file_format_mappings = {
        'xml': ('inxmlfile', MakeHockeySQLiteArrayFromHockeySQLiteXML),
        'xmlalt': ('inxmlfile', MakeHockeySQLiteArrayFromHockeySQLiteXMLAlt),
        'sgml': ('insgmlfile', MakeHockeySQLiteArrayFromHockeySQLiteSGML),
        'json': ('injsonfile', MakeHockeySQLiteArrayFromHockeySQLiteJSON),
        'yaml': ('inyamlfile', MakeHockeySQLiteArrayFromHockeySQLiteYAML),
        'pickle': ('inpicklefile', MakeHockeySQLiteArrayFromHockeySQLitePickle),
        'marshal': ('inmarshalfile', MakeHockeySQLiteArrayFromHockeySQLitePickle),
        'database': ('insdbfile', MakeHockeySQLiteArrayFromHockeyDatabase),
        'olddatabase': ('insdbfile', MakeHockeySQLiteArrayFromOldHockeyDatabase),
        'sql': ('insqlfile', MakeHockeySQLiteArrayFromHockeySQL),
        'array': ('inhockeyarray', MakeHockeySQLiteArrayFromHockeyArray)
    }

    if informat in file_format_mappings:
        file_key, function = file_format_mappings[informat]
        if file_key in funcargs and 'infile' in funcargs:
            funcargs[file_key] = funcargs.pop('infile')
        return function(**funcargs)
    return False

def MakeHockeySQLiteArrayFromHockeySQLiteDataByList(informat="xml", *funcargs):
    format_mappings = {
        'xml': MakeHockeySQLiteArrayFromHockeySQLiteXML,
        'xmlalt': MakeHockeySQLiteArrayFromHockeySQLiteXMLAlt,
        'sgml': MakeHockeySQLiteArrayFromHockeySQLiteSGML,
        'json': MakeHockeySQLiteArrayFromHockeySQLiteJSON,
        'yaml': MakeHockeySQLiteArrayFromHockeySQLiteYAML,
        'pickle': MakeHockeySQLiteArrayFromHockeySQLitePickle,
        'marshal': MakeHockeySQLiteArrayFromHockeySQLitePickle,
        'database': MakeHockeySQLiteArrayFromHockeyDatabase,
        'olddatabase': MakeHockeySQLiteArrayFromOldHockeyDatabase,
        'sql': MakeHockeySQLiteArrayFromHockeySQL,
        'array': MakeHockeySQLiteArrayFromHockeyArray
    }
    return format_mappings.get(informat.lower(), lambda *args: False)(*funcargs)

def MakeHockeySQLiteArrayFromHockeySQLiteData(funcargs):
    if isinstance(funcargs, (tuple, list)):
        return MakeHockeySQLiteArrayFromHockeySQLiteDataByList(*funcargs)
    elif isinstance(funcargs, dict):
        return MakeHockeySQLiteArrayFromHockeySQLiteDataByDict(**funcargs)
    return False

def MakeHockeySQLiteDataFileFromHockeySQLiteArrayByDict(outformat="xml", **funcargs):
    outformat = outformat.lower()
    file_format_mappings = {
        'xml': ('outxmlfile', MakeHockeySQLiteXMLFileFromHockeySQLiteArray),
        'xmlalt': ('outxmlfile', MakeHockeySQLiteXMLAltFileFromHockeySQLiteArray),
        'sgml': ('outsgmlfile', MakeHockeySQLiteSGMLFileFromHockeySQLiteArray),
        'json': ('outjsonfile', MakeHockeySQLiteJSONFileFromHockeySQLiteArray),
        'yaml': ('outyamlfile', MakeHockeySQLiteYAMLFileFromHockeySQLiteArray),
        'pickle': ('outpicklefile', MakeHockeySQLitePickleFileFromHockeySQLiteArray),
        'marshal': ('outmarshalfile', MakeHockeySQLiteMarshalFileFromHockeySQLiteArray),
        'py': ('outpyfile', MakeHockeyPythonFileFromHockeySQLiteArray),
        'pyalt': ('outpyfile', MakeHockeyPythonAltFileFromHockeySQLiteArray),
        'pyoop': ('outpyfile', MakeHockeyPythonOOPFileFromHockeySQLiteArray),
        'pyoopalt': ('outpyfile', MakeHockeyPythonOOPAltFileFromHockeySQLiteArray),
        'sql': ('outsqlfile', MakeHockeySQLFileFromHockeySQLiteArray)
    }

    if outformat in file_format_mappings:
        file_key, function = file_format_mappings[outformat]
        if file_key in funcargs and 'outfile' in funcargs:
            funcargs[file_key] = funcargs.pop('outfile')
        return function(**funcargs)
    return False

def MakeHockeySQLiteDataFileFromHockeySQLiteArrayByList(outformat="xml", *funcargs):
    file_format_mappings = {
        'xml': MakeHockeySQLiteXMLFileFromHockeySQLiteArray,
        'xmlalt': MakeHockeySQLiteXMLAltFileFromHockeySQLiteArray,
        'sgml': MakeHockeySQLiteSGMLFileFromHockeySQLiteArray,
        'json': MakeHockeySQLiteJSONFileFromHockeySQLiteArray,
        'yaml': MakeHockeySQLiteYAMLFileFromHockeySQLiteArray,
        'pickle': MakeHockeySQLitePickleFileFromHockeySQLiteArray,
        'marshal': MakeHockeySQLiteMarshalFileFromHockeySQLiteArray,
        'py': MakeHockeyPythonFileFromHockeySQLiteArray,
        'pyalt': MakeHockeyPythonAltFileFromHockeySQLiteArray,
        'pyoop': MakeHockeyPythonOOPFileFromHockeySQLiteArray,
        'pyoopalt': MakeHockeyPythonOOPAltFileFromHockeySQLiteArray,
        'sql': MakeHockeySQLFileFromHockeySQLiteArray
    }
    return file_format_mappings.get(outformat.lower(), lambda *args: False)(*funcargs)

def MakeHockeySQLiteDataFileFromHockeySQLiteArray(funcargs):
    if isinstance(funcargs, (tuple, list)):
        return MakeHockeySQLiteDataFileFromHockeySQLiteArrayByList(*funcargs)
    elif isinstance(funcargs, dict):
        return MakeHockeySQLiteDataFileFromHockeySQLiteArrayByDict(**funcargs)
    return False
