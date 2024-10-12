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

    $FileInfo: __init__.py - Last Update: 10/11/2024 Ver. 0.9.0 RC 1 - Author: cooldude2k $
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
        hockeyxsl = os.path.join(
            importlib.resources.files(__name__), "hockeydata.xsl")
        hockeyxsd = os.path.join(
            importlib.resources.files(__name__), "hockeydata.xsd")
        hockeyrng = os.path.join(
            importlib.resources.files(__name__), "hockeydata.rng")
        hockeyrnc = os.path.join(
            importlib.resources.files(__name__), "hockeydata.rnc")
        hockeyaltdtd = os.path.join(
            importlib.resources.files(__name__), "hockeydatabase.dtd")
        hockeyaltxsl = os.path.join(
            importlib.resources.files(__name__), "hockeydatabase.xsl")
        hockeyaltxsd = os.path.join(
            importlib.resources.files(__name__), "hockeydatabase.xsd")
        hockeyaltrng = os.path.join(
            importlib.resources.files(__name__), "hockeydatabase.rng")
        hockeyaltrnc = os.path.join(
            importlib.resources.files(__name__), "hockeydatabase.rnc")
    except AttributeError:
        with importlib.resources.path(hockeydata.dtd, "") as pkgfile:
            hockeydtd = pkgfile
        with importlib.resources.path(hockeydata.xsl, "") as pkgfile:
            hockeyxsl = pkgfile
        with importlib.resources.path(hockeydata.xsd, "") as pkgfile:
            hockeyxsd = pkgfile
        with importlib.resources.path(hockeydata.rng, "") as pkgfile:
            hockeyrng = pkgfile
        with importlib.resources.path(hockeydata.rnc, "") as pkgfile:
            hockeyrnc = pkgfile
        with importlib.resources.path(hockeydatabase.dtd, "") as pkgfile:
            hockeyaltdtd = pkgfile
        with importlib.resources.path(hockeydatabase.xsl, "") as pkgfile:
            hockeyaltxsl = pkgfile
        with importlib.resources.path(hockeydatabase.xsd, "") as pkgfile:
            hockeyaltxsd = pkgfile
        with importlib.resources.path(hockeydatabase.rng, "") as pkgfile:
            hockeyaltrng = pkgfile
        with importlib.resources.path(hockeydatabase.rnc, "") as pkgfile:
            hockeyaltrnc = pkgfile
elif (pkgres):
    hockeydtd = pkg_resources.resource_filename(__name__, "hockeydata.dtd")
    hockeyxsl = pkg_resources.resource_filename(__name__, "hockeydata.xsl")
    hockeyxsd = pkg_resources.resource_filename(__name__, "hockeydata.xsd")
    hockeyrng = pkg_resources.resource_filename(__name__, "hockeydata.rng")
    hockeyrnc = pkg_resources.resource_filename(__name__, "hockeydata.rnc")
    hockeyaltdtd = pkg_resources.resource_filename(
        __name__, "hockeydatabase.dtd")
    hockeyaltxsl = pkg_resources.resource_filename(
        __name__, "hockeydatabase.xsl")
    hockeyaltxsd = pkg_resources.resource_filename(
        __name__, "hockeydatabase.xsd")
    hockeyaltrng = pkg_resources.resource_filename(
        __name__, "hockeydatabase.rng")
    hockeyaltrnc = pkg_resources.resource_filename(
        __name__, "hockeydatabase.rnc")
    hockeyxmlpath = os.path.dirname(hockeydtd)
elif (not pkgres):
    hockeydtd = os.path.dirname(__file__)+os.sep+"hockeydata.dtd"
    hockeyxsl = os.path.dirname(__file__)+os.sep+"hockeydata.xsl"
    hockeyxsd = os.path.dirname(__file__)+os.sep+"hockeydata.xsd"
    hockeyrng = os.path.dirname(__file__)+os.sep+"hockeydata.rng"
    hockeyrnc = os.path.dirname(__file__)+os.sep+"hockeydata.rnc"
    hockeyaltdtd = os.path.dirname(__file__)+os.sep+"hockeydatabase.dtd"
    hockeyaltxsl = os.path.dirname(__file__)+os.sep+"hockeydatabase.xsl"
    hockeyaltxsd = os.path.dirname(__file__)+os.sep+"hockeydatabase.xsd"
    hockeyaltrng = os.path.dirname(__file__)+os.sep+"hockeydatabase.rng"
    hockeyaltrnc = os.path.dirname(__file__)+os.sep+"hockeydatabase.rnc"
    hockeyxmlpath = os.path.dirname(hockeydtd)
else:
    hockeydtd = os.path.dirname(__file__)+os.sep+"hockeydata.dtd"
    hockeyxsl = os.path.dirname(__file__)+os.sep+"hockeydata.xsl"
    hockeyxsd = os.path.dirname(__file__)+os.sep+"hockeydata.xsd"
    hockeyrng = os.path.dirname(__file__)+os.sep+"hockeydata.rng"
    hockeyrnc = os.path.dirname(__file__)+os.sep+"hockeydata.rnc"
    hockeyaltdtd = os.path.dirname(__file__)+os.sep+"hockeydatabase.dtd"
    hockeyaltxsl = os.path.dirname(__file__)+os.sep+"hockeydatabase.xsl"
    hockeyaltxsd = os.path.dirname(__file__)+os.sep+"hockeydatabase.xsd"
    hockeyaltrng = os.path.dirname(__file__)+os.sep+"hockeydatabase.rng"
    hockeyaltrnc = os.path.dirname(__file__)+os.sep+"hockeydatabase.rnc"
    hockeyxmlpath = os.path.dirname(hockeydtd)
