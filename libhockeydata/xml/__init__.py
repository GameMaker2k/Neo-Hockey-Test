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

    $FileInfo: __init__.py - Last Update: 2/26/2020 Ver. 0.3.1 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals;
import os;

try:
 import pkg_resources;
 pkgres = True;
except ImportError:
 pkgres = False;

if(pkgres):
 hockeydtd = pkg_resources.resource_filename(__name__, "hockeydata.dtd");
 hockeyxsl = pkg_resources.resource_filename(__name__, "hockeydata.xsl");
 hockeyxsd = pkg_resources.resource_filename(__name__, "hockeydata.xsd");
 hockeyrng = pkg_resources.resource_filename(__name__, "hockeydata.rng");
 hockeyrnc = pkg_resources.resource_filename(__name__, "hockeydata.rnc");
 hockeyxmlpath = os.path.dirname(hockeydtd);

if(not pkgres):
 hockeydtd = os.path.dirname(__file__)+os.sep+"hockeydata.dtd";
 hockeyxsl = os.path.dirname(__file__)+os.sep+"hockeydata.xsl";
 hockeyxsd = os.path.dirname(__file__)+os.sep+"hockeydata.xsd";
 hockeyrng = os.path.dirname(__file__)+os.sep+"hockeydata.rng";
 hockeyrnc = os.path.dirname(__file__)+os.sep+"hockeydata.rnc";
 hockeyxmlpath = os.path.dirname(hockeydtd);
