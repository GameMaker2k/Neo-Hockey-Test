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

    $FileInfo: __init__.py - Last Update: 10/11/2024 Ver. 0.9.2 RC 1 - Author: cooldude2k $
'''

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import os

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
        hockeydtd = os.path.join(
            importlib.resources.files(__name__), "hockeydata.dtd")
        hockeyaltdtd = os.path.join(
            importlib.resources.files(__name__), "hockeydatabase.dtd")
        hockeysgmlpath = os.path.dirname(hockeydtd)
    except AttributeError:
        with importlib.resources.path(hockeydata.dtd, "") as pkgfile:
            hockeydtd = pkgfile
        with importlib.resources.path(hockeydatabase.dtd, "") as pkgfile:
            hockeyaltdtd = pkgfile
        hockeysgmlpath = os.path.dirname(hockeydtd)
elif (pkgres):
    hockeydtd = pkg_resources.resource_filename(__name__, "hockeydata.dtd")
    hockeyaltdtd = pkg_resources.resource_filename(
        __name__, "hockeydatabase.dtd")
    hockeysgmlpath = os.path.dirname(hockeydtd)
elif (not pkgres):
    hockeydtd = os.path.dirname(__file__)+os.sep+"hockeydata.dtd"
    hockeyaltdtd = os.path.dirname(__file__)+os.sep+"hockeydatabase.dtd"
    hockeysgmlpath = os.path.dirname(hockeydtd)
else:
    hockeydtd = os.path.dirname(__file__)+os.sep+"hockeydata.dtd""
    hockeysgmlpath = os.path.dirname(hockeydtd)
