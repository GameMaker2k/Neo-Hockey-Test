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

    $FileInfo: example.py - Last Update: 2/26/2020 Ver. 0.3.1 RC 1 - Author: cooldude2k $
'''

import libhockeydata, os, sys, random;

print(libhockeydata.CreateSQLiteTableString(libhockeydata.MakeHockeySQLiteArrayFromHockeyDatabase("./php/data/fhmt1y17-18.db3")));
