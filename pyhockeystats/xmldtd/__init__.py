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

# Define the required file names
file_names = [
    "hockeydatabase.dsdl", "hockeydatabase.dtd", "hockeydata.dsdl",
    "hockeydata.dtd", "hockeydata.rnc", "hockeydata.rng", "hockeydata.trex",
    "hockeydata.xsd", "hockeydata.xsl", "hockeydatabase.rnc", "hockeydatabase.rng",
    "hockeydatabase.trex", "hockeydatabase.xsd", "hockeydatabase.xsl"
]

# Helper function to assign file paths based on the method available
def get_file_paths(base_function, use_pkg_resources=False):
    if use_pkg_resources:
        return {name: base_function(__name__, name) for name in file_names}
    else:
        return {name: os.path.join(base_function(__name__), name) for name in file_names}

if implib:
    try:
        # Use importlib.resources.files() for modern resource handling
        file_paths = get_file_paths(importlib.resources.files)
    except AttributeError:
        # Fallback for older versions using importlib.resources.path()
        file_paths = {}
        for name in file_names:
            with importlib.resources.path(__name__, name) as pkgfile:
                file_paths[name] = pkgfile
elif pkgres:
    # Use pkg_resources for resource handling
    file_paths = get_file_paths(pkg_resources.resource_filename, use_pkg_resources=True)
else:
    # Fallback if neither importlib.resources nor pkg_resources are available
    base_path = os.path.dirname(__file__)
    file_paths = {name: os.path.join(base_path, name) for name in file_names}

# Now that we have the file paths, let's open and read the relevant files

hockeyfp = open(file_paths["hockeydata.dtd"], "r", encoding="UTF-8")
hockeysgmldtdstring = hockeyfp.read()
hockeyfp.close()

hockeyaltfp = open(file_paths["hockeydatabase.dtd"], "r", encoding="UTF-8")
hockeyaltsgmldtdstring = hockeyaltfp.read()
hockeyaltfp.close()

# You can now use `hockeyxmldtdstring` and `hockeyaltxmldtdstring` 
# in further processing as needed.
