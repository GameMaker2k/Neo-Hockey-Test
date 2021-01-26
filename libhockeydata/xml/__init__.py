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

    $FileInfo: __init__.py - Last Update: 1/15/2021 Ver. 0.5.0 RC 1 - Author: cooldude2k $
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
 hockeyaltdtd = pkg_resources.resource_filename(__name__, "hockeydatabase.dtd");
 hockeyaltxsl = pkg_resources.resource_filename(__name__, "hockeydatabase.xsl");
 hockeyaltxsd = pkg_resources.resource_filename(__name__, "hockeydatabase.xsd");
 hockeyaltrng = pkg_resources.resource_filename(__name__, "hockeydatabase.rng");
 hockeyaltrnc = pkg_resources.resource_filename(__name__, "hockeydatabase.rnc");
 hockeyxmlpath = os.path.dirname(hockeydtd);

if(not pkgres):
 hockeydtd = os.path.dirname(__file__)+os.sep+"hockeydata.dtd";
 hockeyxsl = os.path.dirname(__file__)+os.sep+"hockeydata.xsl";
 hockeyxsd = os.path.dirname(__file__)+os.sep+"hockeydata.xsd";
 hockeyrng = os.path.dirname(__file__)+os.sep+"hockeydata.rng";
 hockeyrnc = os.path.dirname(__file__)+os.sep+"hockeydata.rnc";
 hockeyaltdtd = os.path.dirname(__file__)+os.sep+"hockeydatabase.dtd";
 hockeyaltxsl = os.path.dirname(__file__)+os.sep+"hockeydatabase.xsl";
 hockeyaltxsd = os.path.dirname(__file__)+os.sep+"hockeydatabase.xsd";
 hockeyaltrng = os.path.dirname(__file__)+os.sep+"hockeydatabase.rng";
 hockeyaltrnc = os.path.dirname(__file__)+os.sep+"hockeydatabase.rnc";
 hockeyxmlpath = os.path.dirname(hockeydtd);
