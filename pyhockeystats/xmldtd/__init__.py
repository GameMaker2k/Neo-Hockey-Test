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

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

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
        hockeyxmldtd = os.path.join(
            importlib.resources.files(__name__), "hockeydata.dtd")
        hockeyxmlxslt = os.path.join(
            importlib.resources.files(__name__), "hockeydata.xslt")
        hockeyxmlxsl = os.path.join(
            importlib.resources.files(__name__), "hockeydata.xsl")
        hockeyxmlxsd = os.path.join(
            importlib.resources.files(__name__), "hockeydata.xsd")
        hockeyxmlrng = os.path.join(
            importlib.resources.files(__name__), "hockeydata.rng")
        hockeyxmlrnc = os.path.join(
            importlib.resources.files(__name__), "hockeydata.rnc")
        hockeyxmlaltdtd = os.path.join(
            importlib.resources.files(__name__), "hockeydatabase.dtd")
        hockeyxmlaltxslt = os.path.join(
            importlib.resources.files(__name__), "hockeydatabase.xslt")
        hockeyxmlaltxsl = os.path.join(
            importlib.resources.files(__name__), "hockeydatabase.xsl")
        hockeyxmlaltxsd = os.path.join(
            importlib.resources.files(__name__), "hockeydatabase.xsd")
        hockeyxmlaltrng = os.path.join(
            importlib.resources.files(__name__), "hockeydatabase.rng")
        hockeyxmlaltrnc = os.path.join(
            importlib.resources.files(__name__), "hockeydatabase.rnc")
    except AttributeError:
        with importlib.resources.path("hockeyxmldata.dtd", "") as pkgfile:
            hockeyxmldtd = pkgfile
        with importlib.resources.path("hockeyxmldata.xslt", "") as pkgfile:
            hockeyxmlxslt = pkgfile
        with importlib.resources.path("hockeyxmldata.xsl", "") as pkgfile:
            hockeyxmlxsl = pkgfile
        with importlib.resources.path("hockeyxmldata.xsd", "") as pkgfile:
            hockeyxmlxsd = pkgfile
        with importlib.resources.path("hockeyxmldata.rng", "") as pkgfile:
            hockeyxmlrng = pkgfile
        with importlib.resources.path("hockeyxmldata.rnc", "") as pkgfile:
            hockeyxmlrnc = pkgfile
        with importlib.resources.path("hockeyxmldatabase.dtd", "") as pkgfile:
            hockeyxmlaltdtd = pkgfile
        with importlib.resources.path("hockeyxmldatabase.xslt", "") as pkgfile:
            hockeyxmlaltxslt = pkgfile
        with importlib.resources.path("hockeyxmldatabase.xsl", "") as pkgfile:
            hockeyxmlaltxsl = pkgfile
        with importlib.resources.path("hockeyxmldatabase.xsd", "") as pkgfile:
            hockeyxmlaltxsd = pkgfile
        with importlib.resources.path("hockeyxmldatabase.rng", "") as pkgfile:
            hockeyxmlaltrng = pkgfile
        with importlib.resources.path("hockeyxmldatabase.rnc", "") as pkgfile:
            hockeyxmlaltrnc = pkgfile
elif (pkgres):
    hockeyxmldtd = pkg_resources.resource_filename(__name__, "hockeydata.dtd")
    hockeyxmlxslt = pkg_resources.resource_filename(__name__, "hockeydata.xslt")
    hockeyxmlxsl = pkg_resources.resource_filename(__name__, "hockeydata.xsl")
    hockeyxmlxsd = pkg_resources.resource_filename(__name__, "hockeydata.xsd")
    hockeyxmlrng = pkg_resources.resource_filename(__name__, "hockeydata.rng")
    hockeyxmlrnc = pkg_resources.resource_filename(__name__, "hockeydata.rnc")
    hockeyxmlaltdtd = pkg_resources.resource_filename(
        __name__, "hockeydatabase.dtd")
    hockeyxmlaltxslt = pkg_resources.resource_filename(
        __name__, "hockeydatabase.xslt")
    hockeyxmlaltxsl = pkg_resources.resource_filename(
        __name__, "hockeydatabase.xsl")
    hockeyxmlaltxsd = pkg_resources.resource_filename(
        __name__, "hockeydatabase.xsd")
    hockeyxmlaltrng = pkg_resources.resource_filename(
        __name__, "hockeydatabase.rng")
    hockeyxmlaltrnc = pkg_resources.resource_filename(
        __name__, "hockeydatabase.rnc")
    hockeyxmlxmlpath = os.path.dirname(hockeyxmldtd)
elif (not pkgres):
    hockeyxmldtd = os.path.dirname(__file__)+os.sep+"hockeydata.dtd"
    hockeyxmlxslt = os.path.dirname(__file__)+os.sep+"hockeydata.xslt"
    hockeyxmlxsl = os.path.dirname(__file__)+os.sep+"hockeydata.xsl"
    hockeyxmlxsd = os.path.dirname(__file__)+os.sep+"hockeydata.xsd"
    hockeyxmlrng = os.path.dirname(__file__)+os.sep+"hockeydata.rng"
    hockeyxmlrnc = os.path.dirname(__file__)+os.sep+"hockeydata.rnc"
    hockeyxmlaltdtd = os.path.dirname(__file__)+os.sep+"hockeydatabase.dtd"
    hockeyxmlaltxslt = os.path.dirname(__file__)+os.sep+"hockeydatabase.xslt"
    hockeyxmlaltxsl = os.path.dirname(__file__)+os.sep+"hockeydatabase.xsl"
    hockeyxmlaltxsd = os.path.dirname(__file__)+os.sep+"hockeydatabase.xsd"
    hockeyxmlaltrng = os.path.dirname(__file__)+os.sep+"hockeydatabase.rng"
    hockeyxmlaltrnc = os.path.dirname(__file__)+os.sep+"hockeydatabase.rnc"
    hockeyxmlxmlpath = os.path.dirname(hockeyxmldtd)
else:
    hockeyxmldtd = os.path.dirname(__file__)+os.sep+"hockeydata.dtd"
    hockeyxmlxslt = os.path.dirname(__file__)+os.sep+"hockeydata.xslt"
    hockeyxmlxsl = os.path.dirname(__file__)+os.sep+"hockeydata.xsl"
    hockeyxmlxsd = os.path.dirname(__file__)+os.sep+"hockeydata.xsd"
    hockeyxmlrng = os.path.dirname(__file__)+os.sep+"hockeydata.rng"
    hockeyxmlrnc = os.path.dirname(__file__)+os.sep+"hockeydata.rnc"
    hockeyxmlaltdtd = os.path.dirname(__file__)+os.sep+"hockeydatabase.dtd"
    hockeyxmlaltxsly = os.path.dirname(__file__)+os.sep+"hockeydatabase.xslt"
    hockeyxmlaltxsl = os.path.dirname(__file__)+os.sep+"hockeydatabase.xsl"
    hockeyxmlaltxsd = os.path.dirname(__file__)+os.sep+"hockeydatabase.xsd"
    hockeyxmlaltrng = os.path.dirname(__file__)+os.sep+"hockeydatabase.rng"
    hockeyxmlaltrnc = os.path.dirname(__file__)+os.sep+"hockeydatabase.rnc"
    hockeyxmlxmlpath = os.path.dirname(hockeyxmldtd)

hockeyfp = open(hockeyxmldtd, "r", encoding="UTF-8")
hockeyxmldtdstring = hockeyfp.read()
hockeyfp.close()

hockeyaltfp = open(hockeyxmlaltdtd, "r", encoding="UTF-8")
hockeyaltxmldtdstring = hockeyaltfp.read()
hockeyaltfp.close()
