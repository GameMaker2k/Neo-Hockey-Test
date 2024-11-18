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

    $FileInfo: __init__.py - Last Update: 10/17/2024 Ver. 0.9.6 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals, generators, with_statement, nested_scopes

import os
from io import open

implib = False
pkgres = False
try:
    import pkg_resources
    pkgres = True
except ImportError:
    pkgres = False
    try:
        import importlib.resources
        implib = True
    except ImportError:
        implib = False

if (implib):
    try:
        hockeysgmldtd = os.path.join(
            importlib.resources.files(__name__), "hockeydata.dtd")
        hockeyaltsgmldtd = os.path.join(
            importlib.resources.files(__name__), "hockeydatabase.dtd")
        hockeysgmlpath = os.path.dirname(hockeysgmldtd)
    except AttributeError:
        with importlib.resources.path(hockeydata.dtd, "") as pkgfile:
            hockeysgmldtd = pkgfile
        with importlib.resources.path(hockeydatabase.dtd, "") as pkgfile:
            hockeyaltsgmldtd = pkgfile
        hockeysgmlpath = os.path.dirname(hockeysgmldtd)
elif (pkgres):
    hockeysgmldtd = pkg_resources.resource_filename(__name__, "hockeydata.dtd")
    hockeyaltsgmldtd = pkg_resources.resource_filename(
        __name__, "hockeydatabase.dtd")
    hockeysgmlpath = os.path.dirname(hockeysgmldtd)
elif (not pkgres):
    hockeysgmldtd = os.path.dirname(__file__)+os.sep+"hockeydata.dtd"
    hockeyaltsgmldtd = os.path.dirname(__file__)+os.sep+"hockeydatabase.dtd"
    hockeysgmlpath = os.path.dirname(hockeysgmldtd)
else:
    hockeysgmldtd = os.path.dirname(__file__)+os.sep+"hockeydata.dtd"
    hockeysgmlpath = os.path.dirname(hockeysgmldtd)

hockeyfp = open(hockeysgmldtd, "r", encoding="UTF-8")
hockeysgmldtdstring = hockeyfp.read()
hockeyfp.close()

hockeyaltfp = open(hockeyaltsgmldtd, "r", encoding="UTF-8")
hockeyaltsgmldtdstring = hockeyaltfp.read()
hockeyaltfp.close()
