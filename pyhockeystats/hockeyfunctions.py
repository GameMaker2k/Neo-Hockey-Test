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

    $FileInfo: hockeyfunctions.py - Last Update: 10/17/2024 Ver. 0.9.6 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals, generators, with_statement, nested_scopes

import ast
import binascii
import marshal
import os
import platform
import re
import sqlite3
import sys
import xml.dom.minidom
import time
from io import open

from .hockeydatabase import *
from .hockeydwnload import *
from .versioninfo import (__author__, __copyright__, __credits__, __email__,
                          __license__, __license_string__, __maintainer__,
                          __program_alt_name__, __program_name__, __project__,
                          __project_release_url__, __project_url__,
                          __revision__, __revision_id__, __status__,
                          __version__, __version_alt__, __version_date__,
                          __version_date_alt__, __version_date_info__,
                          __version_date_plusrc__, __version_info__,
                          version_date, version_info)
from .xmldtd import *
from .sgmldtd import *

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

from base64 import b64encode
# Import core modules
from ftplib import FTP, FTP_TLS

# JSON handling: prefer ujson or simplejson if available, fallback to json

try:
    import ujson as json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        import json

testyaml = False
try:
    import oyaml as yaml
    testyaml = True
except ImportError:
    try:
        import yaml
        testyaml = True
    except ImportError:
        testyaml = False

# Paramiko (SSH module) handling
testparamiko = False
try:
    import paramiko
    testparamiko = True
except ImportError:
    testparamiko = False

# Define FileNotFoundError for Python 2
try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

try:
    import xml.etree.cElementTree as cElementTree  # Fallback to cElementTree
except ImportError:
    import xml.etree.ElementTree as cElementTree  # Final fallback to ElementTree

# urlparse and urllib fallback handling (Python 2/3 differences)
try:
    from urlparse import urlparse, urlunparse
except ImportError:
    from urllib.parse import urlparse, urlunparse

# pickle handling: Python 2/3 differences
try:
    import cPickle as pickle  # Use faster cPickle in Python 2
except ImportError:
    import pickle  # Fallback to pickle in Python 3

# Import necessary modules with compatibility for Python 2 and 3
try:
    from html.parser import HTMLParser  # Python 3
except ImportError:
    from HTMLParser import HTMLParser  # Python 2

try:
    from urllib.request import urlopen  # Python 3
except ImportError:
    from urllib2 import urlopen  # Python 2

try:
    from io import StringIO  # Python 3
except ImportError:
    from StringIO import StringIO  # Python 2

# Pickle default protocol handling
# Use DEFAULT_PROTOCOL or fallback to 2
pickledp = getattr(pickle, 'DEFAULT_PROTOCOL', 2)

# User-Agent string for HTTP/HTTPS requests
useragent_string = "Mozilla/5.0 (compatible; {proname}/{prover}; +{prourl})".format(
    proname=__project__, prover=__version_alt__, prourl=__project_url__)

# Conditional platform information for user-agent string
if platform.python_implementation():
    useragent_string_alt = "Mozilla/5.0 ({osver}; {archtype}; +{prourl}) {pyimp}/{pyver} (KHTML, like Gecko) {proname}/{prover}".format(
        osver=platform.system() + " " + platform.release(),
        archtype=platform.machine(),
        prourl=__project_url__,
        pyimp=platform.python_implementation(),
        pyver=platform.python_version(),
        proname=__project__,
        prover=__version_alt__
    )
else:
    useragent_string_alt = "Mozilla/5.0 ({osver}; {archtype}; +{prourl}) Python/{pyver} (KHTML, like Gecko) {proname}/{prover}".format(
        osver=platform.system() + " " + platform.release(),
        archtype=platform.machine(),
        prourl=__project_url__,
        pyver=platform.python_version(),
        proname=__project__,
        prover=__version_alt__
    )

# Compatibility for basestring (Python 2) and str (Python 3)
try:
    basestring
except NameError:
    basestring = str  # In Python 3, there's no 'basestring', only 'str'

# Compatibility for long type (Python 2) and int type (Python 3)
baseint = []
try:
    baseint.append(long)  # Python 2
    baseint.insert(0, int)
except NameError:
    baseint.append(int)  # Python 3 (only 'int')
baseint = tuple(baseint)  # Combine as tuple for later use

teststringio = 0  # Default to no import success
try:
    # Python 3's io module for StringIO and BytesIO
    from io import BytesIO, StringIO
    teststringio = 3
except ImportError:
    if sys.version_info[0] < 3:
        try:
            # Python 2: Try importing from cStringIO first (faster)
            from cStringIO import StringIO
            from cStringIO import StringIO as BytesIO
            teststringio = 1
        except ImportError:
            try:
                # Fallback to Python 2's StringIO module
                from StringIO import StringIO
                from StringIO import StringIO as BytesIO
                teststringio = 2
            except ImportError:
                teststringio = 0
    else:
        teststringio = 0  # Fallback if nothing works


class ZlibFile:
    def __init__(self, file_path=None, fileobj=None, mode='rb', level=9, wbits=15, encoding=None, errors=None, newline=None):
        if file_path is None and fileobj is None:
            raise ValueError("Either file_path or fileobj must be provided")
        if file_path is not None and fileobj is not None:
            raise ValueError(
                "Only one of file_path or fileobj should be provided")

        self.file_path = file_path
        self.fileobj = fileobj
        self.mode = mode
        self.level = level
        self.wbits = wbits
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self._compressed_data = b''
        self._decompressed_data = b''
        self._position = 0
        self._text_mode = 't' in mode

        # Force binary mode for internal handling
        internal_mode = mode.replace('t', 'b')

        if 'w' in mode or 'a' in mode or 'x' in mode:
            self.file = open(
                file_path, internal_mode) if file_path else fileobj
            self._compressor = zlib.compressobj(level, zlib.DEFLATED, wbits)
        elif 'r' in mode:
            if file_path:
                if os.path.exists(file_path):
                    self.file = open(file_path, internal_mode)
                    self._load_file()
                else:
                    raise FileNotFoundError(
                        "No such file: '{}'".format(file_path))
            elif fileobj:
                self.file = fileobj
                self._load_file()
        else:
            raise ValueError("Mode should be 'rb' or 'wb'")

    def _load_file(self):
        self.file.seek(0, 0)
        self._compressed_data = self.file.read()
        if not self._compressed_data.startswith((b'\x78\x01', b'\x78\x5E', b'\x78\x9C', b'\x78\xDA')):
            raise ValueError("Invalid zlib file header")
        self._decompressed_data = zlib.decompress(
            self._compressed_data, self.wbits)
        if self._text_mode:
            self._decompressed_data = self._decompressed_data.decode(
                self.encoding or 'utf-8', self.errors or 'strict')

    def write(self, data):
        if self._text_mode:
            data = data.encode(self.encoding or 'utf-8',
                               self.errors or 'strict')
        compressed_data = self._compressor.compress(
            data) + self._compressor.flush(zlib.Z_SYNC_FLUSH)
        self.file.write(compressed_data)

    def read(self, size=-1):
        if size == -1:
            size = len(self._decompressed_data) - self._position
        data = self._decompressed_data[self._position:self._position + size]
        self._position += size
        return data

    def seek(self, offset, whence=0):
        if whence == 0:  # absolute file positioning
            self._position = offset
        elif whence == 1:  # seek relative to the current position
            self._position += offset
        elif whence == 2:  # seek relative to the file's end
            self._position = len(self._decompressed_data) + offset
        else:
            raise ValueError("Invalid value for whence")

        # Ensure the position is within bounds
        self._position = max(
            0, min(self._position, len(self._decompressed_data)))

    def tell(self):
        return self._position

    def flush(self):
        self.file.flush()

    def fileno(self):
        if hasattr(self.file, 'fileno'):
            return self.file.fileno()
        raise OSError("The underlying file object does not support fileno()")

    def isatty(self):
        if hasattr(self.file, 'isatty'):
            return self.file.isatty()
        return False

    def truncate(self, size=None):
        if hasattr(self.file, 'truncate'):
            return self.file.truncate(size)
        raise OSError("The underlying file object does not support truncate()")

    def close(self):
        if 'w' in self.mode or 'a' in self.mode or 'x' in self.mode:
            self.file.write(self._compressor.flush(zlib.Z_FINISH))
        if self.file_path:
            self.file.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


class GzipFile:
    def __init__(self, file_path=None, fileobj=None, mode='rb', compresslevel=9, encoding=None, errors=None, newline=None):
        if file_path is None and fileobj is None:
            raise ValueError("Either file_path or fileobj must be provided")
        if file_path is not None and fileobj is not None:
            raise ValueError(
                "Only one of file_path or fileobj should be provided")

        self.file_path = file_path
        self.fileobj = fileobj
        self.mode = mode
        self.compresslevel = compresslevel
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self._compressed_data = b''
        self._decompressed_data = b''
        self._position = 0
        self._text_mode = 't' in mode

        # Force binary mode for internal handling
        internal_mode = mode.replace('t', 'b')

        if 'w' in mode or 'a' in mode or 'x' in mode:
            self.file = gzip.open(file_path, internal_mode, compresslevel=compresslevel) if file_path else gzip.GzipFile(
                fileobj=fileobj, mode=internal_mode, compresslevel=compresslevel)
            self._compressor = gzip.GzipFile(
                fileobj=self.file, mode=internal_mode, compresslevel=compresslevel)
        elif 'r' in mode:
            if file_path:
                if os.path.exists(file_path):
                    self.file = gzip.open(file_path, internal_mode)
                    self._load_file()
                else:
                    raise FileNotFoundError(
                        "No such file: '{}'".format(file_path))
            elif fileobj:
                self.file = gzip.GzipFile(fileobj=fileobj, mode=internal_mode)
                self._load_file()
        else:
            raise ValueError("Mode should be 'rb' or 'wb'")

    def _load_file(self):
        self.file.seek(0, 0)
        self._compressed_data = self.file.read()
        if not self._compressed_data.startswith(b'\x1f\x8b'):
            raise ValueError("Invalid gzip file header")
        self._decompressed_data = gzip.decompress(self._compressed_data)
        if self._text_mode:
            self._decompressed_data = self._decompressed_data.decode(
                self.encoding or 'utf-8', self.errors or 'strict')

    def write(self, data):
        if self._text_mode:
            data = data.encode(self.encoding or 'utf-8',
                               self.errors or 'strict')
        compressed_data = self._compressor.compress(data)
        self.file.write(compressed_data)
        self.file.flush()

    def read(self, size=-1):
        if size == -1:
            size = len(self._decompressed_data) - self._position
        data = self._decompressed_data[self._position:self._position + size]
        self._position += size
        return data

    def seek(self, offset, whence=0):
        if whence == 0:  # absolute file positioning
            self._position = offset
        elif whence == 1:  # seek relative to the current position
            self._position += offset
        elif whence == 2:  # seek relative to the file's end
            self._position = len(self._decompressed_data) + offset
        else:
            raise ValueError("Invalid value for whence")

        # Ensure the position is within bounds
        self._position = max(
            0, min(self._position, len(self._decompressed_data)))

    def tell(self):
        return self._position

    def flush(self):
        self.file.flush()

    def fileno(self):
        if hasattr(self.file, 'fileno'):
            return self.file.fileno()
        raise OSError("The underlying file object does not support fileno()")

    def isatty(self):
        if hasattr(self.file, 'isatty'):
            return self.file.isatty()
        return False

    def truncate(self, size=None):
        if hasattr(self.file, 'truncate'):
            return self.file.truncate(size)
        raise OSError("The underlying file object does not support truncate()")

    def close(self):
        if 'w' in self.mode or 'a' in self.mode or 'x' in self.mode:
            self.file.write(self._compressor.flush())
        if self.file_path:
            self.file.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


'''
class BloscFile:
 def __init__(self, file_path=None, fileobj=None, mode='rb', level=9, encoding=None, errors=None, newline=None):
  if file_path is None and fileobj is None:
   raise ValueError("Either file_path or fileobj must be provided")
  if file_path is not None and fileobj is not None:
   raise ValueError("Only one of file_path or fileobj should be provided")

  self.file_path = file_path
  self.fileobj = fileobj
  self.mode = mode
  self.level = level
  self.encoding = encoding
  self.errors = errors
  self.newline = newline
  self._compressed_data = b''
  self._decompressed_data = b''
  self._position = 0
  self._text_mode = 't' in mode

  # Force binary mode for internal handling
  internal_mode = mode.replace('t', 'b')

  if 'w' in mode or 'a' in mode or 'x' in mode:
   self.file = open(file_path, internal_mode) if file_path else fileobj
   self._compressor = blosc.Blosc(level)
  elif 'r' in mode:
   if file_path:
    if os.path.exists(file_path):
     self.file = open(file_path, internal_mode)
     self._load_file()
    else:
     raise FileNotFoundError("No such file: '{}'".format(file_path))
   elif fileobj:
    self.file = fileobj
    self._load_file()
  else:
   raise ValueError("Mode should be 'rb' or 'wb'")

 def _load_file(self):
  self.file.seek(0, 0)
  self._compressed_data = self.file.read()
  if not self._compressed_data:
   raise ValueError("Invalid blosc file header")
  self._decompressed_data = blosc.decompress(self._compressed_data)
  if self._text_mode:
   self._decompressed_data = self._decompressed_data.decode(self.encoding or 'utf-8', self.errors or 'strict')

 def write(self, data):
  if self._text_mode:
   data = data.encode(self.encoding or 'utf-8', self.errors or 'strict')
  compressed_data = blosc.compress(data, cname='blosclz', clevel=self.level)
  self.file.write(compressed_data)
  self.file.flush()

 def read(self, size=-1):
  if size == -1:
   size = len(self._decompressed_data) - self._position
  data = self._decompressed_data[self._position:self._position + size]
  self._position += size
  return data

 def seek(self, offset, whence=0):
  if whence == 0:  # absolute file positioning
   self._position = offset
  elif whence == 1:  # seek relative to the current position
   self._position += offset
  elif whence == 2:  # seek relative to the file's end
   self._position = len(self._decompressed_data) + offset
  else:
   raise ValueError("Invalid value for whence")

  # Ensure the position is within bounds
  self._position = max(0, min(self._position, len(self._decompressed_data)))

 def tell(self):
  return self._position

 def flush(self):
  self.file.flush()

 def fileno(self):
  if hasattr(self.file, 'fileno'):
   return self.file.fileno()
  raise OSError("The underlying file object does not support fileno()")

 def isatty(self):
  if hasattr(self.file, 'isatty'):
   return self.file.isatty()
  return False

 def truncate(self, size=None):
  if hasattr(self.file, 'truncate'):
   return self.file.truncate(size)
  raise OSError("The underlying file object does not support truncate()")

 def close(self):
  if 'w' in self.mode or 'a' in self.mode or 'x' in self.mode:
   self.file.write(blosc.compress(self._compressor.flush(), cname='blosclz', clevel=self.level))
  if self.file_path:
   self.file.close()

 def __enter__(self):
  return self

 def __exit__(self, exc_type, exc_value, traceback):
  self.close()

class BrotliFile:
 def __init__(self, file_path=None, fileobj=None, mode='rb', level=11, encoding=None, errors=None, newline=None):
  if file_path is None and fileobj is None:
   raise ValueError("Either file_path or fileobj must be provided")
  if file_path is not None and fileobj is not None:
   raise ValueError("Only one of file_path or fileobj should be provided")

  self.file_path = file_path
  self.fileobj = fileobj
  self.mode = mode
  self.level = level
  self.encoding = encoding
  self.errors = errors
  self.newline = newline
  self._compressed_data = b''
  self._decompressed_data = b''
  self._position = 0
  self._text_mode = 't' in mode

  # Force binary mode for internal handling
  internal_mode = mode.replace('t', 'b')

  if 'w' in mode or 'a' in mode or 'x' in mode:
   self.file = open(file_path, internal_mode) if file_path else fileobj
   self._compressor = brotli.Compressor(quality=self.level)
  elif 'r' in mode:
   if file_path:
    if os.path.exists(file_path):
     self.file = open(file_path, internal_mode)
     self._load_file()
    else:
     raise FileNotFoundError("No such file: '{}'".format(file_path))
   elif fileobj:
    self.file = fileobj
    self._load_file()
  else:
   raise ValueError("Mode should be 'rb' or 'wb'")

 def _load_file(self):
  self.file.seek(0, 0)
  self._compressed_data = self.file.read()
  if not self._compressed_data:
   raise ValueError("Invalid brotli file header")
  self._decompressed_data = brotli.decompress(self._compressed_data)
  if self._text_mode:
   self._decompressed_data = self._decompressed_data.decode(self.encoding or 'utf-8', self.errors or 'strict')

 def write(self, data):
  if self._text_mode:
   data = data.encode(self.encoding or 'utf-8', self.errors or 'strict')
  compressed_data = self._compressor.process(data)
  self.file.write(compressed_data)
  self.file.flush()

 def read(self, size=-1):
  if size == -1:
   size = len(self._decompressed_data) - self._position
  data = self._decompressed_data[self._position:self._position + size]
  self._position += size
  return data

 def seek(self, offset, whence=0):
  if whence == 0:  # absolute file positioning
   self._position = offset
  elif whence == 1:  # seek relative to the current position
   self._position += offset
  elif whence == 2:  # seek relative to the file's end
   self._position = len(self._decompressed_data) + offset
  else:
   raise ValueError("Invalid value for whence")

  # Ensure the position is within bounds
  self._position = max(0, min(self._position, len(self._decompressed_data)))

 def tell(self):
  return self._position

 def flush(self):
  self.file.flush()

 def fileno(self):
  if hasattr(self.file, 'fileno'):
   return self.file.fileno()
  raise OSError("The underlying file object does not support fileno()")

 def isatty(self):
  if hasattr(self.file, 'isatty'):
   return self.file.isatty()
  return False

 def truncate(self, size=None):
  if hasattr(self.file, 'truncate'):
   return self.file.truncate(size)
  raise OSError("The underlying file object does not support truncate()")

 def close(self):
  if 'w' in self.mode or 'a' in self.mode or 'x' in self.mode:
   self.file.write(self._compressor.finish())
  if self.file_path:
   self.file.close()

 def __enter__(self):
  return self

 def __exit__(self, exc_type, exc_value, traceback):
  self.close()
'''


# Updated helper function to read SGML data from file, URL, or string
def ReadSGMLData(insgmlfile, sgmlisfile=True, encoding="UTF-8", headers=None, cookie_jar=None):
    sgml_data = None
    
    if sgmlisfile:
        # insgmlfile is a file path or URL
        if re.match('^(http|https|ftp|ftps|sftp)://', insgmlfile):
            # It's a URL
            try:
                insgmlfile = UncompressFileURL(insgmlfile)
                sgml_data = insgmlfile.read()
                if isinstance(sgml_data, bytes):
                    sgml_data = sgml_data.decode(encoding)
            except Exception as e:
                print("Error reading SGML data from URL:", e)
                return False
        else:
            # It's a local file
            if os.path.exists(insgmlfile) and os.path.isfile(insgmlfile):
                try:
                    insgmlfile = UncompressFile(insgmlfile, mode="rt", encoding=encoding)
                    sgml_data = insgmlfile.read()
                except Exception as e:
                    print("Error reading SGML data from file:", e)
                    return False
            else:
                print("File does not exist or is not a file:", insgmlfile)
                return False
    else:
        # insgmlfile is a string containing SGML data
        chckcompression = CheckCompressionTypeFromString(insgmlfile)
        if not chckcompression:
            sgml_data = insgmlfile
        else:
            try:
                insgmlsfile = BytesIO(insgmlfile.encode(encoding))
            except TypeError:
                insgmlsfile = BytesIO(insgmlfile)
            insgmlfile = UncompressFile(insgmlsfile)
            sgml_data = insgmlfile.read()

        if isinstance(sgml_data, bytes):
            try:
                sgml_data = sgml_data.decode(encoding)
            except Exception as e:
                print("Error decoding SGML data string:", e)
                return False
        elif sys.version_info[0] < 3 and isinstance(sgml_data, str):
            try:
                sgml_data = sgml_data.decode(encoding)
            except Exception as e:
                print("Error decoding SGML data string:", e)
                return False

    return sgml_data


# Helper function to convert SGML attribute values to Python types
def ConvertSGMLValuesForPython(value):
    if value == 'None':
        return None
    elif value.isdigit():
        return int(value)
    else:
        return value

class HockeySGMLParser(HTMLParser):
    def __init__(self):
        if sys.version_info[0] < 3:
            HTMLParser.__init__(self)
        else:
            super(HockeySGMLParser, self).__init__()

        self.leaguearrayout = {}
        self.leaguelist = []
        self.current_league = None
        self.current_conference = None
        self.current_division = None
        self.current_team = None
        self.in_hockey = False
        self.in_league = False
        self.in_conference = False
        self.in_division = False
        self.in_team = False
        self.in_arenas = False
        self.in_arena = False
        self.in_games = False
        self.in_game = False
        self.database = None

    def handle_decl(self, decl):
        pass  # Ignore DTD declarations

    def handle_pi(self, data):
        # Ignore XML declarations (processing instructions)
        if data.startswith("xml"):
            pass  # Ignore <?xml version="1.0" encoding="UTF-8"?>
        else:
            super(HockeySGMLParser, self).handle_pi(data)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.process_tag(tag, attrs)

    def handle_startendtag(self, tag, attrs):
        attrs = dict(attrs)
        self.process_tag(tag, attrs, is_empty=True)

    def process_tag(self, tag, attrs, is_empty=False):
        if tag == 'hockey':
            self.in_hockey = True
            self.database = attrs.get('database', defaultsdbfile)
            self.leaguearrayout['database'] = self.database
        elif tag == 'league' and self.in_hockey:
            self.in_league = True
            self.current_league = attrs.get('name')
            league_info = {
                'leagueinfo': {
                    'name': attrs.get('name', ''),
                    'fullname': attrs.get('fullname', ''),
                    'country': attrs.get('country', ''),
                    'fullcountry': attrs.get('fullcountry', ''),
                    'date': attrs.get('date', ''),
                    'playofffmt': attrs.get('playofffmt', ''),
                    'ordertype': attrs.get('ordertype', ''),
                    'conferences': attrs.get('conferences', ''),
                    'divisions': attrs.get('divisions', ''),
                },
                'quickinfo': {
                    'conferenceinfo': {},
                    'divisioninfo': {},
                    'teaminfo': {},
                },
                'conferencelist': [],
                'arenas': [],
                'games': [],
            }
            self.leaguearrayout[self.current_league] = league_info
            self.leaguelist.append(self.current_league)
        elif tag == 'conference' and self.in_league:
            self.in_conference = True
            self.current_conference = attrs.get('name')
            conference_info = {
                'conferenceinfo': {
                    'name': attrs.get('name', ''),
                    'prefix': attrs.get('prefix', ''),
                    'suffix': attrs.get('suffix', ''),
                    'fullname': GetFullTeamName(attrs.get('name', ''), attrs.get('prefix', ''), attrs.get('suffix', '')),
                    'league': self.current_league,
                },
            }
            self.leaguearrayout[self.current_league][self.current_conference] = conference_info
            self.leaguearrayout[self.current_league]['quickinfo']['conferenceinfo'][self.current_conference] = {
                'name': attrs.get('name', ''),
                'fullname': conference_info['conferenceinfo']['fullname'],
                'league': self.current_league,
            }
            self.leaguearrayout[self.current_league]['conferencelist'].append(self.current_conference)
            self.leaguearrayout[self.current_league][self.current_conference]['divisionlist'] = []
        elif tag == 'division' and self.in_conference:
            self.in_division = True
            self.current_division = attrs.get('name')
            division_info = {
                'divisioninfo': {
                    'name': attrs.get('name', ''),
                    'prefix': attrs.get('prefix', ''),
                    'suffix': attrs.get('suffix', ''),
                    'fullname': GetFullTeamName(attrs.get('name', ''), attrs.get('prefix', ''), attrs.get('suffix', '')),
                    'league': self.current_league,
                    'conference': self.current_conference,
                },
            }
            self.leaguearrayout[self.current_league][self.current_conference][self.current_division] = division_info
            self.leaguearrayout[self.current_league]['quickinfo']['divisioninfo'][self.current_division] = {
                'name': attrs.get('name', ''),
                'fullname': division_info['divisioninfo']['fullname'],
                'league': self.current_league,
                'conference': self.current_conference,
            }
            self.leaguearrayout[self.current_league][self.current_conference]['divisionlist'].append(self.current_division)
            self.leaguearrayout[self.current_league][self.current_conference][self.current_division]['teamlist'] = []
        elif tag == 'team' and self.in_division:
            team_name = attrs.get('name')
            full_team_name = GetFullTeamName(team_name, attrs.get('prefix', ''), attrs.get('suffix', ''))
            team_info = {
                'teaminfo': {
                    'city': attrs.get('city', ''),
                    'area': attrs.get('area', ''),
                    'fullarea': attrs.get('fullarea', ''),
                    'country': attrs.get('country', ''),
                    'fullcountry': attrs.get('fullcountry', ''),
                    'name': team_name,
                    'fullname': full_team_name,
                    'arena': attrs.get('arena', ''),
                    'prefix': attrs.get('prefix', ''),
                    'suffix': attrs.get('suffix', ''),
                    'league': self.current_league,
                    'conference': self.current_conference,
                    'division': self.current_division,
                    'affiliates': attrs.get('affiliates', ''),
                },
            }
            self.leaguearrayout[self.current_league][self.current_conference][self.current_division][team_name] = team_info
            self.leaguearrayout[self.current_league]['quickinfo']['teaminfo'][team_name] = {
                'name': team_name,
                'fullname': full_team_name,
                'league': self.current_league,
                'conference': self.current_conference,
                'division': self.current_division,
            }
            self.leaguearrayout[self.current_league][self.current_conference][self.current_division]['teamlist'].append(team_name)
        elif tag == 'arenas' and self.in_league:
            self.in_arenas = True
        elif tag == 'arena' and self.in_arenas:
            arena_info = {
                'city': attrs.get('city', ''),
                'area': attrs.get('area', ''),
                'fullarea': attrs.get('fullarea', ''),
                'country': attrs.get('country', ''),
                'fullcountry': attrs.get('fullcountry', ''),
                'name': attrs.get('name', ''),
            }
            self.leaguearrayout[self.current_league]['arenas'].append(arena_info)
        elif tag == 'games' and self.in_league:
            self.in_games = True
        elif tag == 'game' and self.in_games:
            game_info = {
                'date': attrs.get('date', ''),
                'time': attrs.get('time', ''),
                'hometeam': attrs.get('hometeam', ''),
                'awayteam': attrs.get('awayteam', ''),
                'goals': attrs.get('goals', ''),
                'sogs': attrs.get('sogs', ''),
                'ppgs': attrs.get('ppgs', ''),
                'shgs': attrs.get('shgs', ''),
                'penalties': attrs.get('penalties', ''),
                'pims': attrs.get('pims', ''),
                'hits': attrs.get('hits', ''),
                'takeaways': attrs.get('takeaways', ''),
                'faceoffwins': attrs.get('faceoffwins', ''),
                'atarena': attrs.get('atarena', ''),
                'isplayoffgame': attrs.get('isplayoffgame', ''),
            }
            self.leaguearrayout[self.current_league]['games'].append(game_info)

    def handle_endtag(self, tag):
        if tag == 'hockey':
            self.in_hockey = False
        elif tag == 'league':
            self.in_league = False
            self.current_league = None
        elif tag == 'conference':
            self.in_conference = False
            self.current_conference = None
        elif tag == 'division':
            self.in_division = False
            self.current_division = None
        elif tag == 'team':
            self.in_team = False
        elif tag == 'arenas':
            self.in_arenas = False
        elif tag == 'arena':
            self.in_arena = False
        elif tag == 'games':
            self.in_games = False
        elif tag == 'game':
            self.in_game = False

    def handle_data(self, data):
        pass  # No character data to process


class HockeySGMLChecker(HTMLParser):
    def __init__(self):
        try:
            super(HockeySGMLChecker, self).__init__()
        except TypeError:
            HTMLParser.__init__(self)  # Python 2

        self.is_valid = True  # Flag to indicate if the SGML is valid
        self.current_tags = []  # Stack to keep track of open tags
        self.required_attributes = {
            'hockey': ['database'],
            'league': ['name', 'fullname', 'country', 'fullcountry', 'date', 'playofffmt', 'ordertype', 'conferences', 'divisions'],
            'conference': ['name', 'prefix', 'suffix'],
            'division': ['name', 'prefix', 'suffix'],
            'team': ['city', 'area', 'fullarea', 'country', 'fullcountry', 'name', 'arena', 'affiliates', 'prefix', 'suffix'],
            'arena': ['city', 'area', 'fullarea', 'country', 'fullcountry', 'name'],
            'game': ['date', 'time', 'hometeam', 'awayteam', 'goals', 'sogs', 'ppgs', 'shgs', 'penalties', 'pims', 'hits', 'takeaways', 'faceoffwins', 'atarena', 'isplayoffgame']
        }
        self.allowed_container_tags = {
            'hockey': ['league'],
            'league': ['conference', 'arenas', 'games'],
            'conference': ['division'],
            'division': ['team'],
            'arenas': ['arena'],
            'games': ['game']
        }
        self.leaguelist = []
        self.current_league = None

    def handle_decl(self, decl):
        pass  # Ignore DTD declarations

    def handle_pi(self, data):
        # Ignore XML declarations (processing instructions)
        if data.startswith("xml"):
            pass  # Ignore <?xml version="1.0" encoding="UTF-8"?>
        else:
            super(HockeySGMLChecker, self).handle_pi(data)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.process_tag(tag, attrs)

    def handle_startendtag(self, tag, attrs):
        attrs = dict(attrs)
        self.process_tag(tag, attrs, is_empty=True)

    def process_tag(self, tag, attrs, is_empty=False):
        # Handle self-closing or empty tags
        if tag in ['arena', 'team', 'game']:
            return

        self.current_tags.append(tag)
        if not self.is_valid:
            return

        if tag in self.required_attributes:
            if not CheckKeyInArray(self.required_attributes[tag], attrs):
                print("Tag <{}> missing required attributes.".format(tag))
                self.is_valid = False
                return

            if tag == 'hockey':
                pass  # No additional checks
            elif tag == 'league':
                league_name = attrs.get('name')
                if league_name in self.leaguelist:
                    print("Duplicate league name:", league_name)
                    self.is_valid = False
                    return
                self.leaguelist.append(league_name)
                self.current_league = league_name
            elif tag == 'team':
                pass  # Additional team-specific validations can be added here

        elif tag in self.allowed_container_tags:
            # Check if the current context allows this container tag
            if len(self.current_tags) < 2:
                parent_tag = None
            else:
                parent_tag = self.current_tags[-2]

            allowed_children = self.allowed_container_tags.get(parent_tag, [])
            if tag not in allowed_children:
                print("Tag <{}> not allowed under <{}>.".format(tag, parent_tag))
                self.is_valid = False
                return
            # No required attributes for container tags
            pass

    def handle_endtag(self, tag):
        if not self.current_tags:
            print("Mismatched closing tag:", tag)
            self.is_valid = False
            return

        expected_tag = self.current_tags.pop()
        if tag != expected_tag:
            print("Tag mismatch: expected </{}>, got </{}>".format(expected_tag, tag))
            self.is_valid = False

    def handle_data(self, data):
        pass  # No character data to process


class HockeySQLiteSGMLParser(HTMLParser):
    def __init__(self):
        if sys.version_info[0] < 3:
            HTMLParser.__init__(self)
        else:
            super(HockeySQLiteSGMLParser, self).__init__()

        self.leaguearrayout = {}
        self.current_table = None
        self.in_hockeydb = False
        self.in_table = False
        self.in_column = False
        self.in_data = False
        self.in_row = False
        self.in_rowdata = False
        self.in_rows = False
        self.database = None

    def handle_decl(self, decl):
        # Ignore DTD declarations
        pass
    
    def handle_pi(self, data):
        # Ignore XML declarations (processing instructions)
        if data.startswith("xml"):
            pass  # Ignore <?xml version="1.0" encoding="UTF-8"?>
        else:
            super(HockeySQLiteSGMLParser, self).handle_pi(data)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.process_tag(tag, attrs)

    def handle_startendtag(self, tag, attrs):
        attrs = dict(attrs)
        self.process_tag(tag, attrs, is_empty=True)

    def process_tag(self, tag, attrs, is_empty=False):
        if tag == 'hockeydb':
            self.in_hockeydb = True
            self.database = attrs.get('database', defaultsdbfile)
            self.leaguearrayout['database'] = self.database
        elif tag == 'table' and self.in_hockeydb:
            self.in_table = True
            self.current_table = attrs.get('name')
            self.leaguearrayout[self.current_table] = {'rows': [], 'values': []}
        elif tag == 'column' and self.in_table:
            self.in_column = True
        elif tag == 'rowinfo' and self.in_column:
            rowinfo_name = attrs.get('name')
            default_value = attrs.get('defaultvalue')
            default_value = ConvertSGMLValuesForPython(default_value)
            column_info = {
                'info': {
                    'id': int(attrs.get('id', '0')),
                    'Name': attrs.get('name', ''),
                    'Type': attrs.get('type', ''),
                    'NotNull': int(attrs.get('notnull', '0')),
                    'DefualtValue': default_value,
                    'PrimaryKey': int(attrs.get('primarykey', '0')),
                    'AutoIncrement': int(attrs.get('autoincrement', '0')),
                    'Hidden': int(attrs.get('hidden', '0')),
                }
            }
            self.leaguearrayout[self.current_table][rowinfo_name] = column_info
        elif tag == 'data' and self.in_table:
            self.in_data = True
        elif tag == 'row' and self.in_data:
            self.in_row = True
            self.leaguearrayout[self.current_table]['values'].append({})
        elif tag == 'rowdata' and self.in_row:
            rowdata_name = attrs.get('name', '')
            rowdata_value = ConvertSGMLValuesForPython(attrs.get('value', ''))
            self.leaguearrayout[self.current_table]['values'][-1][rowdata_name] = rowdata_value
        elif tag == 'rows' and self.in_table:
            self.in_rows = True
        elif tag == 'rowlist' and self.in_rows:
            rowlist_name = attrs.get('name', '')
            self.leaguearrayout[self.current_table]['rows'].append(rowlist_name)

    def handle_endtag(self, tag):
        if tag == 'hockeydb':
            self.in_hockeydb = False
        elif tag == 'table':
            self.in_table = False
            self.current_table = None
        elif tag == 'column':
            self.in_column = False
        elif tag == 'data':
            self.in_data = False
        elif tag == 'row':
            self.in_row = False
        elif tag == 'rowdata':
            self.in_rowdata = False
        elif tag == 'rows':
            self.in_rows = False

    def handle_data(self, data):
        pass  # No character data to process in this structure


class HockeySQLiteSGMLChecker(HTMLParser):
    def __init__(self):
        try:
            super(HockeySQLiteSGMLChecker, self).__init__()
        except TypeError:
            HTMLParser.__init__(self)  # Python 2

        self.is_valid = True  # Flag to indicate if the SGML is valid
        self.current_tags = []  # Stack to keep track of open tags
        self.required_attributes = {
            'hockeydb': ['database'],
            'table': ['name'],
            'rowinfo': ['id', 'name', 'type', 'notnull', 'defaultvalue', 'primarykey', 'autoincrement', 'hidden'],
            'row': ['id'],
            'rowdata': ['name', 'value'],
            'rowlist': ['name']
        }
        self.allowed_container_tags = {
            'hockeydb': ['table'],
            'table': ['column', 'data', 'rows'],
            'column': ['rowinfo'],
            'data': ['row'],
            'row': ['rowdata'],
            'rows': ['rowlist']
        }
        self.leaguelist = []
        self.tablelist = []
        self.current_table = None
        self.in_table = False
        self.in_row = False

    def handle_decl(self, decl):
        pass  # Ignore DTD declarations

    def handle_pi(self, data):
        # Ignore XML declarations (processing instructions)
        if data.startswith("xml"):
            pass  # Ignore <?xml version="1.0" encoding="UTF-8"?>
        else:
            super(HockeySQLiteSGMLChecker, self).handle_pi(data)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.process_tag(tag, attrs)

    def handle_startendtag(self, tag, attrs):
        attrs = dict(attrs)
        self.process_tag(tag, attrs, is_empty=True)

    def process_tag(self, tag, attrs, is_empty=False):
        # Handle self-closing or empty tags
        if tag in ['rowlist', 'rowdata', 'rowinfo']:
            return

        self.current_tags.append(tag)
        if not self.is_valid:
            return

        if tag in self.required_attributes:
            if not CheckKeyInArray(self.required_attributes[tag], attrs):
                print("Tag <{}> missing required attributes.".format(tag))
                self.is_valid = False
                return

            if tag == 'hockeydb':
                pass  # No additional checks
            elif tag == 'table':
                table_name = attrs.get('name')
                if table_name in self.tablelist:
                    print("Duplicate table name:", table_name)
                    self.is_valid = False
                    return
                self.tablelist.append(table_name)
                self.current_table = table_name
            elif tag == 'rowdata':
                if self.current_table == "HockeyLeagues" and attrs.get('name') == "LeagueName":
                    league_name = attrs.get('value')
                    if league_name in self.leaguelist:
                        print("Duplicate league name:", league_name)
                        self.is_valid = False
                        return
                    self.leaguelist.append(league_name)
            elif tag == 'row':
                pass  # Additional row-specific validations can be added here

        elif tag in self.allowed_container_tags:
            # Check if the current context allows this container tag
            if len(self.current_tags) < 2:
                parent_tag = None
            else:
                parent_tag = self.current_tags[-2]

            allowed_children = self.allowed_container_tags.get(parent_tag, [])
            if tag not in allowed_children:
                print("Tag <{}> not allowed under <{}>.".format(tag, parent_tag))
                self.is_valid = False
                return
            # No required attributes for container tags
            pass

    def handle_endtag(self, tag):
        if not self.current_tags:
            print("Mismatched closing tag:", tag)
            self.is_valid = False
            return

        expected_tag = self.current_tags.pop()
        if tag != expected_tag:
            print("Tag mismatch: expected </{}>, got </{}>".format(expected_tag, tag))
            self.is_valid = False

    def handle_data(self, data):
        pass  # No character data to process


def CheckCompressionType(infile, closefp=True):
    if (not hasattr(infile, "read")):
        filefp = open(infile, "rb")
    else:
        filefp = infile
    filefp.seek(0, 0)
    prefp = filefp.read(2)
    filetype = False
    if (prefp == binascii.unhexlify("1f8b")):
        filetype = "gzip"
    if (prefp == binascii.unhexlify("7801")):
        filetype = "zlib"
    if (prefp == binascii.unhexlify("785e")):
        filetype = "zlib"
    if (prefp == binascii.unhexlify("789c")):
        filetype = "zlib"
    if (prefp == binascii.unhexlify("78da")):
        filetype = "zlib"
    filefp.seek(0, 0)
    prefp = filefp.read(3)
    if (prefp == binascii.unhexlify("425a68")):
        filetype = "bzip2"
    if (prefp == binascii.unhexlify("5d0000")):
        filetype = "lzma"
    filefp.seek(0, 0)
    prefp = filefp.read(4)
    if (prefp == binascii.unhexlify("28b52ffd")):
        filetype = "zstd"
    filefp.seek(0, 0)
    prefp = filefp.read(4)
    if (prefp == binascii.unhexlify("04224d18")):
        filetype = "lz4"
    filefp.seek(0, 0)
    prefp = filefp.read(6)
    if (prefp == binascii.unhexlify("fd377a585a00")):
        filetype = "lzma"
    filefp.seek(0, 0)
    prefp = filefp.read(7)
    if (prefp == binascii.unhexlify("fd377a585a0000")):
        filetype = "lzma"
    filefp.seek(0, 0)
    prefp = filefp.read(9)
    if (prefp == binascii.unhexlify("894c5a4f000d0a1a0a")):
        filetype = "lzo"
    filefp.seek(0, 0)
    if (closefp):
        filefp.close()
    return filetype


def CheckCompressionTypeFromString(instring, encoding="UTF-8", closefp=True):
    try:
        instringsfile = BytesIO(instring)
    except TypeError:
        instringsfile = BytesIO(instring.encode(encoding))
    return CheckCompressionType(instringsfile, closefp)


def UncompressFile(infile, mode="rt", encoding="UTF-8"):
    compresscheck = CheckCompressionType(infile, False)
    if (sys.version_info[0] == 2 and compresscheck):
        if (mode == "rt"):
            mode = "r"
        if (mode == "wt"):
            mode = "w"
    if (compresscheck == "gzip"):
        try:
            import gzip
        except ImportError:
            return False
        try:
            filefp = gzip.open(infile, mode, encoding=encoding)
        except (ValueError, TypeError) as e:
            filefp = gzip.open(infile, mode)
    if (compresscheck == "bzip2"):
        try:
            import bz2
        except ImportError:
            return False
        try:
            filefp = bz2.open(infile, mode, encoding=encoding)
        except (ValueError, TypeError) as e:
            filefp = bz2.open(infile, mode)
    if (compresscheck == "zstd"):
        try:
            import zstandard
        except ImportError:
            return False
        try:
            filefp = zstandard.open(infile, mode, encoding=encoding)
        except (ValueError, TypeError) as e:
            filefp = zstandard.open(infile, mode)
    if (compresscheck == "lz4"):
        try:
            import lz4.frame
        except ImportError:
            return False
        try:
            filefp = lz4.frame.open(infile, mode, encoding=encoding)
        except (ValueError, TypeError) as e:
            filefp = lz4.frame.open(infile, mode)
    if (compresscheck == "lzo" or compresscheck == "lzop"):
        try:
            import lzo
        except ImportError:
            return False
        try:
            filefp = lzo.open(infile, mode, encoding=encoding)
        except (ValueError, TypeError) as e:
            filefp = lzo.open(infile, mode)
    if (compresscheck == "lzma"):
        try:
            import lzma
        except ImportError:
            return False
        try:
            filefp = lzma.open(infile, mode, encoding=encoding)
        except (ValueError, TypeError) as e:
            filefp = lzma.open(infile, mode)
    if (compresscheck == "zlib"):
        try:
            filefp = ZlibFile(infile, mode, encoding=encoding)
        except (ValueError, TypeError) as e:
            filefp = ZlibFile(infile, mode)
    if (not compresscheck):
        try:
            filefp = open(infile, mode=mode, encoding=encoding)
        except (ValueError, TypeError) as e:
            filefp = open(infile, mode=mode)
    return filefp


def UncompressString(infile, encoding="UTF-8"):
    compresscheck = CheckCompressionTypeFromString(infile, encoding, False)
    if (compresscheck == "gzip"):
        try:
            import gzip
        except ImportError:
            return False
        fileuz = gzip.decompress(infile)
    if (compresscheck == "bzip2"):
        try:
            import bz2
        except ImportError:
            return False
        fileuz = bz2.decompress(infile)
    if (compresscheck == "zstd"):
        try:
            import zstandard
        except ImportError:
            return False
        fileuz = zstandard.decompress(infile)
    if (compresscheck == "lz4"):
        try:
            import lz4.frame
        except ImportError:
            return False
        fileuz = lz4.frame.decompress(infile)
    if (compresscheck == "lzo"):
        try:
            import lzo
        except ImportError:
            return False
        fileuz = lzo.decompress(infile)
    if (compresscheck == "lzma"):
        try:
            import lzma
        except ImportError:
            return False
        fileuz = lzma.decompress(infile)
    if (not compresscheck):
        fileuz = infile
    if (hasattr(fileuz, 'decode')):
        fileuz = fileuz.decode(encoding)
    return fileuz


def UncompressStringAlt(infile):
    filefp = StringIO()
    outstring = UncompressString(infile)
    filefp.write(outstring)
    filefp.seek(0, 0)
    return filefp


def UncompressFileURL(inurl, encoding="UTF-8"):
    if re.findall("^(http|https|ftp|ftps|sftp)\\:\\/\\/", inurl):
        inbfile = download_file_from_internet_string(inurl)
        inufile = BytesIO(UncompressString(inbfile).encode(encoding))
    else:
        return False
    return inufile


def CompressOpenFile(outfile, encoding="UTF-8"):
    if (outfile is None):
        return False
    fbasename = os.path.splitext(outfile)[0]
    fextname = os.path.splitext(outfile)[1]
    if (sys.version_info[0] == 2):
        mode = "w"
    else:
        mode = "wt"
    if (fextname not in outextlistwd):
        try:
            outfp = open(outfile, "wt", encoding=encoding)
        except (ValueError, TypeError) as e:
            outfp = open(outfile, "wt")
    elif (fextname == ".gz"):
        try:
            import gzip
        except ImportError:
            return False
        outfp = gzip.open(outfile, mode, 9, encoding=encoding)
    elif (fextname == ".bz2"):
        try:
            import bz2
        except ImportError:
            return False
        outfp = bz2.open(outfile, mode, 9, encoding=encoding)
    elif (fextname == ".zst"):
        try:
            import zstandard
        except ImportError:
            return False
        outfp = zstandard.open(
            outfile, mode, zstandard.ZstdCompressor(level=10), encoding=encoding)
    elif (fextname == ".xz"):
        try:
            import lzma
        except ImportError:
            return False
        outfp = lzma.open(outfile, mode, format=lzma.FORMAT_XZ,
                          preset=9, encoding=encoding)
    elif (fextname == ".lz4"):
        try:
            import lz4.frame
        except ImportError:
            return False
        outfp = lz4.frame.open(
            outfile, mode, format=lzma.FORMAT_XZ, preset=9, encoding=encoding)
    elif (fextname == ".lzo" or fextname == ".lzop"):
        try:
            import lzo
        except ImportError:
            return False
        outfp = lzo.open(outfile, mode, format=lzma.FORMAT_XZ,
                         preset=9, encoding=encoding)
    elif (fextname == ".lzma"):
        try:
            import lzma
        except ImportError:
            return False
        outfp = lzma.open(outfile, mode, format=lzma.FORMAT_ALONE,
                          preset=9, encoding=encoding)
    elif (fextname == ".zz" or fextname == ".zl" or fextname == ".zlib"):
        try:
            import pylzma
        except ImportError:
            try:
                import lzma
            except ImportError:
                return False
        outfp = ZlibFile(outfile, mode=mode, level=9)
    return outfp


def MakeFileFromString(instringfile, stringisfile, outstringfile, encoding="UTF-8", returnstring=False):
    if (stringisfile and ((os.path.exists(instringfile) and os.path.isfile(instringfile)) or re.findall("^(http|https|ftp|ftps|sftp)\\:\\/\\/", instringfile))):
        if (re.findall("^(http|https|ftp|ftps|sftp)\\:\\/\\/", instringfile)):
            stringfile = UncompressFileURL(
                instringfile)
        else:
            stringfile = UncompressFile(instringsfile)
    elif (not stringisfile):
        chckcompression = CheckCompressionTypeFromString(instringfile)
        if (not chckcompression):
            stringfile = StringIO(instringfile)
        else:
            try:
                instringsfile = BytesIO(instringfile)
            except TypeError:
                instringsfile = BytesIO(instringfile.encode(encoding))
            stringfile = UncompressFile(instringsfile)
    else:
        return False
    stringstring = stringfile.read()
    if (hasattr(stringstring, 'decode')):
        stringstring = stringstring.decode(encoding)
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outstringfile))):
        stringfp = BytesIO()
    else:
        stringfp = CompressOpenFile(outstringfile)
    try:
        stringfp.write(stringstring)
    except TypeError:
        stringfp.write(stringstring.encode(encoding))
    try:
        stringfp.flush()
        os.fsync(stringfp.fileno())
    except io.UnsupportedOperation:
        pass
    except AttributeError:
        pass
    except OSError as e:
        pass
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outstringfile))):
        stringfp.seek(0, 0)
        upload_file_to_internet_file(stringfp, outstringfile)
    stringfp.close()
    if (returnstring):
        return stringstring
    if (not returnstring):
        return True
    return True


def MakeHockeyFileFromHockeyString(instringfile, stringisfile, outstringfile, encoding="UTF-8", returnstring=False):
    return MakeFileFromString(instringfile, stringisfile, outstringfile, encoding, returnstring)


def CheckXMLFile(infile):
    xmlfp = UncompressFile(infile, "rb")
    xmlfp.seek(0, 0)
    prefp = xmlfp.read(6)
    validxmlfile = False
    if (prefp == binascii.unhexlify("3c3f786d6c20")):
        validxmlfile = True
    xmlfp.close()
    return validxmlfile

# From https://stackoverflow.com/a/16919069


def RemoveBlanks(node):
    for x in node.childNodes:
        if (x.nodeType == xml.dom.minidom.Node.TEXT_NODE):
            if (x.nodeValue):
                x.nodeValue = x.nodeValue.strip()
        elif (x.nodeType == xml.dom.minidom.Node.ELEMENT_NODE):
            RemoveBlanks(x)
    return True


def RemoveNamespaces(node):
    """Recursively remove xmlns attributes from all elements."""
    # Check if the node has the attribute 'xmlns'
    if node.hasAttribute("xmlns"):
        node.removeAttribute("xmlns")

    # Recursively remove 'xmlns' from child elements
    for child in node.childNodes:
        if child.nodeType == xml.dom.minidom.Node.ELEMENT_NODE:
            RemoveNamespaces(child)

    return True



def GetDataFromArray(data, path, default=None):
    element = data
    try:
        for key in path:
            element = element[key]
        return element
    except (KeyError, TypeError, IndexError):
        return default


def GetDataFromArrayAlt(structure, path, default=None):
    element = structure
    for key in path:
        if isinstance(element, dict) and key in element:
            element = element[key]
        elif isinstance(element, list) and isinstance(key, int) and -len(element) <= key < len(element):
            element = element[key]
        else:
            return default
    return element


def BeautifyXMLCode(inxmlfile, xmlisfile=True, indent="\t", newl="\n", encoding="UTF-8", beautify=True, remove_namespaces=True):
    if (xmlisfile and ((os.path.exists(inxmlfile) and os.path.isfile(inxmlfile)) or re.findall(r"^(http|https|ftp|ftps|sftp)\:\/\/", inxmlfile))):
        try:
            if (re.findall(r"^(http|https|ftp|ftps|sftp)\:\/\/", inxmlfile)):
                inxmlfile = UncompressFileURL(
                    inxmlfile, geturls_headers, geturls_cj)
                xmldom = xml.dom.minidom.parse(file=inxmlfile)
            else:
                xmldom = xml.dom.minidom.parse(file=UncompressFile(inxmlfile))
        except:
            return False
    elif (not xmlisfile):
        chckcompression = CheckCompressionTypeFromString(inxmlfile)
        if (not chckcompression):
            inxmlfile = StringIO(inxmlfile)
        else:
            try:
                inxmlsfile = BytesIO(inxmlfile)
            except TypeError:
                inxmlsfile = BytesIO(inxmlfile.encode("UTF-8"))
            inxmlfile = UncompressFile(inxmlsfile)
        try:
            xmldom = xml.dom.minidom.parse(file=inxmlfile)
        except:
            return False
    else:
        return False

    # Optionally remove namespaces
    if remove_namespaces:
        RemoveNamespaces(xmldom.documentElement)

    RemoveBlanks(xmldom)
    xmldom.normalize()
    
    if (beautify):
        outxmlcode = xmldom.toprettyxml(indent, newl, encoding)
    else:
        outxmlcode = xmldom.toxml(encoding)
    if (hasattr(outxmlcode, 'decode')):
        outxmlcode = outxmlcode.decode("UTF-8")
    xmldom.unlink()
    return outxmlcode


def BeautifyXMLCodeToFile(inxmlfile, outxmlfile, xmlisfile=True, indent="\t", newl="\n", encoding="UTF-8", beautify=True, remove_namespaces=True, returnxml=False):
    if (outxmlfile is None):
        return False
    fbasename = os.path.splitext(outxmlfile)[0]
    fextname = os.path.splitext(outxmlfile)[1]
    xmlfp = CompressOpenFile(outxmlfile)
    xmlstring = BeautifyXMLCode(
        inxmlfile, xmlisfile, indent, newl, encoding, beautify, remove_namespaces)
    if (fextname in outextlistwd):
        xmlstring = xmlstring
    try:
        xmlfp.write(xmlstring)
    except TypeError:
        xmlfp.write(xmlstring.encode("UTF-8"))
    try:
        xmlfp.flush()
        os.fsync(xmlfp.fileno())
    except io.UnsupportedOperation:
        pass
    except AttributeError:
        pass
    except OSError as e:
        pass
    xmlfp.close()
    if (returnxml):
        return xmlstring
    if (not returnxml):
        return True
    return True


def CheckHockeyXML(inxmlfile, xmlisfile=True, encoding="UTF-8"):
    if (xmlisfile and ((os.path.exists(inxmlfile) and os.path.isfile(inxmlfile)) or re.findall("^(http|https|ftp|ftps|sftp)\\:\\/\\/", inxmlfile))):
        try:
            if (re.findall("^(http|https|ftp|ftps|sftp)\\:\\/\\/", inxmlfile)):
                inxmlfile = UncompressFileURL(
                    inxmlfile)
                try:
                    hockeyfile = cElementTree.parse(
                        inxmlfile, parser=cElementTree.XMLParser(encoding=encoding))
                    hockeyroot = hockeyfile.getroot()
                except cElementTree.ParseError:
                    try:
                        inxmlfile.seek(0, 0)
                        hockeyroot = cElementTree.fromstring(inxmlfile.read())
                    except cElementTree.ParseError:
                        return False
            else:
                hockeyfile = cElementTree.parse(UncompressFile(
                    inxmlfile), parser=cElementTree.XMLParser(encoding=encoding))
                hockeyroot = hockeyfile.getroot()
        except cElementTree.ParseError:
            try:
                hockeyroot = cElementTree.fromstring(
                    UncompressFile(inxmlfile).read())
            except cElementTree.ParseError:
                return False
    elif (not xmlisfile):
        chckcompression = CheckCompressionTypeFromString(inxmlfile)
        if (not chckcompression):
            inxmlfile = StringIO(inxmlfile)
        else:
            try:
                inxmlsfile = BytesIO(inxmlfile)
            except TypeError:
                inxmlsfile = BytesIO(inxmlfile.encode(encoding))
            inxmlfile = UncompressFile(inxmlsfile)
        try:
            hockeyfile = cElementTree.parse(
                inxmlfile, parser=cElementTree.XMLParser(encoding=encoding))
            hockeyroot = hockeyfile.getroot()
        except cElementTree.ParseError:
            try:
                inxmlfile.seek(0, 0)
                hockeyroot = cElementTree.fromstring(inxmlfile.read())
            except cElementTree.ParseError:
                return False
    else:
        return False
    if (hockeyroot.tag == "hockey"):
        if ("database" not in hockeyroot.attrib):
            return False
        leaguelist = []
        for hockeyleague in hockeyroot:
            if (hockeyleague.tag == "league"):
                if (not CheckKeyInArray(["name", "fullname", "country", "fullcountry", "date", "playofffmt", "ordertype", "conferences", "divisions"], dict(hockeyleague.attrib))):
                    return False
                if (hockeyleague.attrib['name'] in leaguelist):
                    return False
                leaguelist.append(hockeyleague.attrib['name'])
                for hockeyconference in hockeyleague:
                    if (hockeyconference.tag == "conference"):
                        if (not CheckKeyInArray(["name", "prefix", "suffix"], dict(hockeyconference.attrib))):
                            return False
                        for hockeydivision in hockeyconference:
                            if (hockeydivision.tag == "division"):
                                if (not CheckKeyInArray(["name", "prefix", "suffix"], dict(hockeydivision.attrib))):
                                    return False
                                for hockeyteam in hockeydivision:
                                    if (hockeyteam.tag == "team"):
                                        if (not CheckKeyInArray(["city", "area", "fullarea", "country", "fullcountry", "name", "arena", "affiliates", "prefix", "suffix"], dict(hockeyteam.attrib))):
                                            return False
                                    else:
                                        return False
                            else:
                                return False
                    elif (hockeyconference.tag == "arenas"):
                        for hockeyarenas in hockeyconference:
                            if (hockeyarenas.tag == "arena"):
                                if (not CheckKeyInArray(["city", "area", "fullarea", "country", "fullcountry", "name"], dict(hockeyarenas.attrib))):
                                    return False
                            else:
                                return False
                    elif (hockeyconference.tag == "games"):
                        for hockeygames in hockeyconference:
                            if (hockeygames.tag == "game"):
                                if (not CheckKeyInArray(["date", "time", "hometeam", "awayteam", "goals", "sogs", "ppgs", "shgs", "penalties", "pims", "hits", "takeaways", "faceoffwins", "atarena", "isplayoffgame"], dict(hockeygames.attrib))):
                                    return False
                            else:
                                return False
                    else:
                        return False
    else:
        return False
    return True


def CheckHockeySGML(insgmlfile, sgmlisfile=True, encoding="UTF-8"):
    """
    Checks if the SGML data is correctly structured as hockey data.

    Parameters:
    - insgmlfile (str): The input SGML file path, URL, or data string.
    - sgmlisfile (bool): If True, 'insgmlfile' is treated as a file path or URL. If False, it's treated as SGML data string.
    - encoding (str): The encoding to use when reading files or decoding data.

    Returns:
    - bool: True if SGML data is valid, False otherwise.
    """

    # Read SGML data
    sgml_data = ReadSGMLData(insgmlfile, sgmlisfile=sgmlisfile, encoding=encoding)
    if sgml_data is False:
        print("Failed to read SGML data.")
        return False

    # Parse SGML data
    parser = HockeySGMLChecker()
    try:
        parser.feed(sgml_data)
        parser.close()
    except Exception as e:
        print("Error parsing SGML data:", e)
        return False

    return parser.is_valid


def CheckHockeySQLiteXML(inxmlfile, xmlisfile=True, encoding="UTF-8"):
    if (xmlisfile and ((os.path.exists(inxmlfile) and os.path.isfile(inxmlfile)) or re.findall("^(http|https|ftp|ftps|sftp)\\:\\/\\/", inxmlfile))):
        try:
            if (re.findall("^(http|https|ftp|ftps|sftp)\\:\\/\\/", inxmlfile)):
                inxmlfile = UncompressFileURL(
                    inxmlfile)
                try:
                    hockeyfile = cElementTree.parse(
                        inxmlfile, parser=cElementTree.XMLParser(encoding=encoding))
                    hockeyroot = hockeyfile.getroot()
                except cElementTree.ParseError:
                    try:
                        inxmlfile.seek(0, 0)
                        hockeyroot = cElementTree.fromstring(inxmlfile.read())
                    except cElementTree.ParseError:
                        return False
            else:
                hockeyfile = cElementTree.parse(UncompressFile(
                    inxmlfile), parser=cElementTree.XMLParser(encoding=encoding))
                hockeyroot = hockeyfile.getroot()
        except cElementTree.ParseError:
            try:
                hockeyroot = cElementTree.fromstring(
                    UncompressFile(inxmlfile).read())
            except cElementTree.ParseError:
                return False
    elif (not xmlisfile):
        chckcompression = CheckCompressionTypeFromString(inxmlfile)
        if (not chckcompression):
            inxmlfile = StringIO(inxmlfile)
        else:
            try:
                inxmlsfile = BytesIO(inxmlfile)
            except TypeError:
                inxmlsfile = BytesIO(inxmlfile.encode(encoding))
            inxmlfile = UncompressFile(inxmlsfile)
        try:
            hockeyfile = cElementTree.parse(
                inxmlfile, parser=cElementTree.XMLParser(encoding=encoding))
            hockeyroot = hockeyfile.getroot()
        except cElementTree.ParseError:
            try:
                inxmlfile.seek(0, 0)
                hockeyroot = cElementTree.fromstring(inxmlfile.read())
            except cElementTree.ParseError:
                return False
    else:
        return False
    leaguelist = []
    tablelist = []
    if (hockeyroot.tag == "hockeydb"):
        if ("database" not in hockeyroot.attrib):
            return False
        for hockeytable in hockeyroot:
            if (hockeytable.tag == "table"):
                if (not CheckKeyInArray(["name"], dict(hockeytable.attrib))):
                    return False
                tablelist.append(hockeytable.attrib['name'])
                for hockeycolumn in hockeytable:
                    if (hockeycolumn.tag == "column"):
                        for hockeyrowinfo in hockeycolumn:
                            if (hockeyrowinfo.tag == "rowinfo"):
                                if (not CheckKeyInArray(["id", "name", "type", "notnull", "defaultvalue", "primarykey", "autoincrement", "hidden"], dict(hockeyrowinfo.attrib))):
                                    return False
                            else:
                                return False
                    elif (hockeycolumn.tag == "data"):
                        for hockeydata in hockeycolumn:
                            if (hockeydata.tag == "row"):
                                if (not CheckKeyInArray(["id"], dict(hockeydata.attrib))):
                                    return False
                                for rowdata in hockeydata:
                                    if (rowdata.tag == "rowdata"):
                                        if (not CheckKeyInArray(["name", "value"], dict(rowdata.attrib))):
                                            return False
                                        if (hockeytable.attrib['name'] == "HockeyLeagues" and rowdata.attrib['name'] == "LeagueName"):
                                            if (rowdata.attrib['value'] in leaguelist):
                                                return False
                                            leaguelist.append(
                                                rowdata.attrib['value'])
                                    else:
                                        return False
                            else:
                                return False
                    elif (hockeycolumn.tag == "rows"):
                        for hockeyrows in hockeycolumn:
                            if (hockeyrows.tag == "rowlist"):
                                if (not CheckKeyInArray(["name"], dict(hockeyrows.attrib))):
                                    return False
                            else:
                                return False
                    else:
                        return False
    else:
        return False
    # all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games", "PlayoffTeams"]
    all_table_list = ["Conferences", "Divisions",
                      "Arenas", "Teams", "Stats", "GameStats", "Games"]
    table_list = ['HockeyLeagues']
    for leagueinfo_tmp in leaguelist:
        for cur_tab in all_table_list:
            table_list.append(leagueinfo_tmp+cur_tab)
    for get_cur_tab in table_list:
        if get_cur_tab not in tablelist:
            return False
    return True


def CheckHockeySQLiteSGML(insgmlfile, sgmlisfile=True, encoding="UTF-8"):
    """
    Checks if the SGML data is correctly structured as hockey SQLite data.

    Parameters:
    - insgmlfile (str): The input SGML file path, URL, or data string.
    - sgmlisfile (bool): If True, 'insgmlfile' is treated as a file path or URL. If False, it's treated as SGML data string.
    - encoding (str): The encoding to use when reading files or decoding data.

    Returns:
    - bool: True if SGML data is valid, False otherwise.
    """

    # Read SGML data
    sgml_data = ReadSGMLData(insgmlfile, sgmlisfile=sgmlisfile, encoding=encoding)
    if sgml_data is False:
        print("Failed to read SGML data.")
        return False

    # Parse SGML data
    parser = HockeySQLiteSGMLChecker()
    try:
        parser.feed(sgml_data)
        parser.close()
    except Exception as e:
        print("Error parsing SGML data:", e)
        return False

    # After parsing, check that all expected tables are present
    if parser.is_valid:
        # Expected tables
        all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games"]
        expected_tables = ['HockeyLeagues']
        for league_name in parser.leaguelist:
            for tablename in all_table_list:
                expected_tables.append(league_name + tablename)
        for expected_table in expected_tables:
            if expected_table not in parser.tablelist:
                print("Missing expected table:", expected_table)
                parser.is_valid = False
                break

    return parser.is_valid


def CopyHockeyDatabase(insdbfile, outsdbfile, returninsdbfile=True, returnoutsdbfile=True):
    if (not CheckHockeySQLiteDatabase(insdbfile)[0]):
        return False
    if (insdbfile is None):
        insqldatacon = OpenHockeyDatabase(":memory:")
    if (insdbfile is not None and isinstance(insdbfile, basestring)):
        insqldatacon = OpenHockeyDatabase(insdbfile)
    if (insdbfile is not None and isinstance(insdbfile, (tuple, list))):
        insqldatacon = tuple(insdbfile)
    if (outsdbfile is None):
        outsqldatacon = MakeHockeyDatabase(":memory:")
    if (outsdbfile is not None and isinstance(outsdbfile, basestring)):
        outsqldatacon = MakeHockeyDatabase(outsdbfile)
    if (outsdbfile is not None and isinstance(outsdbfile, (tuple, list))):
        outsqldatacon = tuple(outsdbfile)
    if (not isinstance(insqldatacon, (tuple, list)) and not insqldatacon):
        return False
    if (not isinstance(outsqldatacon, (tuple, list)) and not outsqldatacon):
        return False
    insqldatacon[1].backup(outsqldatacon)
    if (returninsdbfile and returnoutsdbfile):
        return [insqldatacon, outsqldatacon]
    elif (returninsdbfile and not returnoutsdbfile):
        CloseHockeyDatabase(outsqldatacon)
        return [insqldatacon]
    elif (not returninsdbfile and returnoutsdbfile):
        CloseHockeyDatabase(insqldatacon)
        return [outsqldatacon]
    elif (not returninsdbfile and not returnoutsdbfile):
        CloseHockeyDatabase(insqldatacon)
        CloseHockeyDatabase(outsqldatacon)
        return None
    else:
        return False
    return False


def DumpHockeyDatabase(insdbfile, returninsdbfile=True):
    if (not CheckHockeySQLiteDatabase(insdbfile)[0]):
        return False
    if (insdbfile is None):
        insqldatacon = OpenHockeyDatabase(":memory:")
    if (insdbfile is not None and isinstance(insdbfile, basestring)):
        insqldatacon = OpenHockeyDatabase(insdbfile)
    if (insdbfile is not None and isinstance(insdbfile, (tuple, list))):
        insqldatacon = tuple(insdbfile)
    if (not isinstance(insqldatacon, (tuple, list)) and not insqldatacon):
        return False
    dbdumplist = []
    for line in insqldatacon[1].iterdump():
        dbdumplist.append(line+"\n")
    sqloutstring = ''.join(dbdumplist)
    if (returninsdbfile):
        return [sqloutstring, insqldatacon]
    elif (not returninsdbfile):
        CloseHockeyDatabase(insqldatacon)
        return [sqloutstring]
    else:
        return False
    return False


def DumpHockeyDatabaseToSQLFile(insdbfile, outsqlfile, encoding="UTF-8", returninsdbfile=True):
    if (not CheckHockeySQLiteDatabase(insdbfile)[0]):
        return False
    if (insdbfile is None):
        insqldatacon = OpenHockeyDatabase(":memory:")
    if (insdbfile is not None and isinstance(insdbfile, basestring)):
        insqldatacon = OpenHockeyDatabase(insdbfile)
    if (insdbfile is not None and isinstance(insdbfile, (tuple, list))):
        insqldatacon = tuple(insdbfile)
    if (not isinstance(insqldatacon, (tuple, list)) and not insqldatacon):
        return False
    with CompressOpenFile(outsqlfile) as f:
        for line in insqldatacon[1].iterdump():
            try:
                f.write('%s\n' % line)
            except TypeError:
                f.write('%s\n' % line.encode(encoding))
        try:
            f.flush()
            os.fsync(f.fileno())
        except io.UnsupportedOperation:
            pass
        except AttributeError:
            pass
        except OSError as e:
            pass
    if (returninsdbfile):
        return [insqldatacon]
    elif (not returninsdbfile):
        CloseHockeyDatabase(insqldatacon)
        return None
    else:
        return False
    return False


def RestoreHockeyDatabaseFromSQL(insqlstring, outsdbfile, returnoutsdbfile=True):
    if (outsdbfile is None):
        insqldatacon = MakeHockeyDatabase(":memory:")
    if (outsdbfile is not None and isinstance(outsdbfile, basestring)):
        insqldatacon = MakeHockeyDatabase(outsdbfile)
    if (outsdbfile is not None and isinstance(outsdbfile, (tuple, list))):
        insqldatacon = tuple(outsdbfile)
    if (not isinstance(insqldatacon, (tuple, list)) and not insqldatacon):
        return False
    insqldatacon[0].execute('BEGIN TRANSACTION')
    insqldatacon[1].executescript(insqlstring)
    insqldatacon[1].commit()
    if (returnoutsdbfile):
        return [insqldatacon]
    elif (not returnoutsdbfile):
        CloseHockeyDatabase(insqldatacon)
        return None
    else:
        return False
    return False


def RestoreHockeyDatabaseFromSQLFile(insqlfile, outsdbfile, encoding="UTF-8", returnoutsdbfile=True):
    if (outsdbfile is None):
        insqldatacon = MakeHockeyDatabase(":memory:")
    if (outsdbfile is not None and isinstance(outsdbfile, basestring)):
        insqldatacon = MakeHockeyDatabase(outsdbfile)
    if (outsdbfile is not None and isinstance(outsdbfile, (tuple, list))):
        insqldatacon = tuple(outsdbfile)
    if (not isinstance(insqldatacon, (tuple, list)) and not insqldatacon):
        return False
    with UncompressFile(insqlfile) as f:
        sqlinput = f.read()
        if (hasattr(sqlinput, 'decode')):
            sqlinput = sqlinput.decode(encoding)
    insqldatacon[0].execute('BEGIN TRANSACTION')
    insqldatacon[1].executescript(sqlinput)
    insqldatacon[1].commit()
    if (returnoutsdbfile):
        return [insqldatacon]
    elif (not returnoutsdbfile):
        CloseHockeyDatabase(insqldatacon)
        return None
    else:
        return False
    return False


def DumpHockeyArrayToFile(inhockeyarray, outarrayfile, returnarray=False, encoding="UTF-8", verbose=False, verbosetype="array"):
    if (not CheckHockeyArray(inhockeyarray) and not CheckHockeySQLiteArray(inhockeyarray)):
        return False
    if (outarrayfile is None):
        return False
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outarrayfile))):
        arrayfp = BytesIO()
    else:
        arrayfp = CompressOpenFile(outarrayfile)
    print(inhockeyarray, file=arrayfp)
    try:
        arrayfp.flush()
        os.fsync(arrayfp.fileno())
    except io.UnsupportedOperation:
        pass
    except AttributeError:
        pass
    except OSError as e:
        pass
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outarrayfile))):
        arrayfp.seek(0, 0)
        upload_file_to_internet_file(arrayfp, outjsonfile)
    arrayfp.close()
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose):
        VerbosePrintOut(hockeyarray)
    if (returnarray):
        return inhockeyarray
    if (not returnarray):
        return True
    return True


def DumpHockeyArrayToString(inhockeyarray, encoding="UTF-8", verbose=False, verbosetype="array"):
    if (not CheckHockeyArray(inhockeyarray) and not CheckHockeySQLiteArray(inhockeyarray)):
        return False
    arrayfp = StringIO()
    print(inhockeyarray, file=arrayfp)
    arrayfp.seek(0, 0)
    outstr = arrayfp.read()
    arrayfp.close()
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose):
        VerbosePrintOut(hockeyarray)
    return outstr


def RestoreHockeyArrayFromFile(inarrayfile, arrayisfile=True, encoding="UTF-8", verbose=False, verbosetype="array"):
    if (arrayisfile and ((os.path.exists(inarrayfile) and os.path.isfile(inarrayfile)) or re.findall("^(http|https|ftp|ftps|sftp)\\:\\/\\/", inarrayfile))):
        if (re.findall("^(http|https|ftp|ftps|sftp)\\:\\/\\/", inarrayfile)):
            inarrayfile = UncompressFileURL(
                inarrayfile)
            hockeyarray = ast.literal_eval(arrayfp.read())
        else:
            arrayfp = UncompressFile(inarrayfile)
            hockeyarray = ast.literal_eval(arrayfp.read())
            arrayfp.close()
    elif (not arrayisfile):
        arrayfp = BytesIO(inarrayfile.encode(encoding))
        arrayfp = UncompressFile(arrayfp)
        hockeyarray = ast.literal_eval(arrayfp.read())
        arrayfp.close()
    else:
        return False
    if (not CheckHockeyArray(hockeyarray) and not CheckHockeySQLiteArray(hockeyarray)):
        return False
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            hockeyarray, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            hockeyarray, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            hockeyarray, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            hockeyarray, verbose=False))
    elif (verbose):
        VerbosePrintOut(hockeyarray)
    return hockeyarray



def RestoreHockeyArrayFromFile(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        # Safely evaluate the content and return the array
    ast.literal_eval(content)
    return ast.literal_eval(content)


def MakeHockeyJSONFromHockeyArray(inhockeyarray, jsonindent=1, beautify=True, sortkeys=False, verbose=False, verbosetype="array"):
    if (not CheckHockeyArray(inhockeyarray) and not CheckHockeySQLiteArray(inhockeyarray)):
        return False
    if (beautify):
        jsonstring = json.dumps(
            inhockeyarray, sort_keys=sortkeys, indent=jsonindent)
    else:
        jsonstring = json.dumps(
            inhockeyarray, sort_keys=sortkeys, separators=(', ', ': '))
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(jsonstring)
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose):
        VerbosePrintOut(inhockeyarray)
    return jsonstring


def MakeHockeyJSONFromHockeySQLiteArray(inhockeyarray, jsonindent=1, beautify=True, sortkeys=False, verbose=False, verbosetype="array"):
    jsonstring = MakeHockeyJSONFromHockeyArray(
        inhockeyarray, jsonindent, beautify, sortkeys, verbose, verbosetype)
    return jsonstring


def MakeHockeyJSONFileFromHockeyArray(inhockeyarray, outjsonfile=None, returnjson=False, jsonindent=1, beautify=True, sortkeys=False, encoding="UTF-8", verbose=False, verbosetype="array"):
    if (outjsonfile is None):
        return False
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outjsonfile))):
        jsonfp = BytesIO()
    else:
        jsonfp = CompressOpenFile(outjsonfile)
    jsonstring = MakeHockeyJSONFromHockeyArray(
        inhockeyarray, jsonindent, beautify, sortkeys, verbose, verbosetype)
    try:
        jsonfp.write(jsonstring)
    except TypeError:
        jsonfp.write(jsonstring.encode(encoding))
    try:
        jsonfp.flush()
        os.fsync(jsonfp.fileno())
    except io.UnsupportedOperation:
        pass
    except AttributeError:
        pass
    except OSError as e:
        pass
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outjsonfile))):
        jsonfp.seek(0, 0)
        upload_file_to_internet_file(jsonfp, outjsonfile)
    jsonfp.close()
    if (returnjson):
        return jsonstring
    if (not returnjson):
        return True
    return True


def MakeHockeyJSONFileFromHockeySQLiteArray(inhockeyarray, outjsonfile=None, returnjson=False, jsonindent=1, beautify=True, sortkeys=False, verbose=False, verbosetype="array"):
    jsonstring = MakeHockeyJSONFileFromHockeyArray(
        inhockeyarray, outjsonfile, returnjson, jsonindent, beautify, sortkeys, verbose, verbosetype)
    return jsonstring


def MakeHockeyArrayFromHockeyJSON(injsonfile, jsonisfile=True, verbose=False, verbosetype="array"):
    if (jsonisfile and ((os.path.exists(injsonfile) and os.path.isfile(injsonfile)) or re.findall("^(http|https|ftp|ftps|sftp)\\:\\/\\/", injsonfile))):
        if (re.findall("^(http|https|ftp|ftps|sftp)\\:\\/\\/", injsonfile)):
            injsonfile = UncompressFileURL(
                injsonfile)
            try:
                hockeyarray = json.load(injsonfile)
            except json.JSONDecodeError:
                return False
        else:
            jsonfp = UncompressFile(injsonfile)
            hockeyarray = json.load(jsonfp)
            jsonfp.close()
    elif (not jsonisfile):
        chckcompression = CheckCompressionTypeFromString(injsonfile)
        if (not chckcompression):
            jsonfp = StringIO(injsonfile)
        else:
            try:
                injsonsfile = BytesIO(injsonfile)
            except TypeError:
                injsonsfile = BytesIO(injsonfile.encode(encoding))
            jsonfp = UncompressFile(injsonsfile)
        hockeyarray = json.load(jsonfp)
        jsonfp.close()
    else:
        return False
    if (not CheckHockeyArray(hockeyarray) and not CheckHockeySQLiteArray(hockeyarray)):
        return False
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            hockeyarray, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            hockeyarray, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            hockeyarray, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            hockeyarray, verbose=False))
    elif (verbose):
        VerbosePrintOut(hockeyarray)
    return hockeyarray

def MakeHockeySQLiteArrayFromHockeyJSON(injsonfile, jsonisfile=True, verbose=False, verbosetype="array"):
 hockeyarray = MakeHockeyArrayFromHockeyJSON(injsonfile, jsonisfile, verbose, verbosetype)
 return hockeyarray


def MakeHockeyYAMLFromHockeyArray(inhockeyarray, yamlindent=1, beautify=True, sortkeys=False, verbose=False, verbosetype="array"):
    if testyaml:
        # Using YAML if available
        if not CheckHockeyArray(inhockeyarray) and not CheckHockeySQLiteArray(inhockeyarray):
            return False
        if beautify:
            yamlstring = yaml.dump(inhockeyarray, sort_keys=sortkeys, indent=yamlindent)
        else:
            yamlstring = yaml.dump(inhockeyarray, sort_keys=sortkeys, default_flow_style=False)
        if verbose and verbosetype == "json":
            VerbosePrintOut(MakeHockeJSONFromHockeyArray(inhockeyarray, verbose=False))
        elif verbose and verbosetype == "yaml":
            VerbosePrintOut(yamlstring)
        elif verbose and verbosetype == "xml":
            VerbosePrintOut(MakeHockeyXMLFromHockeyArray(inhockeyarray, verbose=False))
        elif verbose and verbosetype == "sgml":
            VerbosePrintOut(MakeHockeySGMLFromHockeyArray(inhockeyarray, verbose=False))
        elif verbose:
            VerbosePrintOut(inhockeyarray)
        return yamlstring
    else:
        # Fallback to JSON functions
        return MakeHockeyJSONFromHockeyArray(inhockeyarray, jsonindent=yamlindent, beautify=beautify, sortkeys=sortkeys, verbose=verbose, verbosetype=verbosetype)


def MakeHockeyYAMLFileFromHockeyArray(inhockeyarray, outyamlfile=None, returnyaml=False, yamlindent=1, beautify=True, sortkeys=False, encoding="UTF-8", verbose=False, verbosetype="array"):
    if testyaml:
        if (outyamlfile is None):
            return False
        if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outyamlfile))):
            yamlfp = BytesIO()
        else:
            yamlfp = CompressOpenFile(outyamlfile)
        yamlstring = MakeHockeyYAMLFromHockeyArray(
            inhockeyarray, yamlindent, beautify, sortkeys, verbose, verbosetype)
        try:
            yamlfp.write(yamlstring)
        except TypeError:
            yamlfp.write(yamlstring.encode(encoding))
        try:
            yamlfp.flush()
            os.fsync(yamlfp.fileno())
        except io.UnsupportedOperation:
            pass
        except AttributeError:
            pass
        except OSError as e:
            pass
        if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outyamlfile))):
            yamlfp.seek(0, 0)
            upload_file_to_internet_file(yamlfp, outyamlfile)
        yamlfp.close()
        if (returnyaml):
            return yamlstring
        if (not returnyaml):
            return True
        return True
    else:
        # Fallback to JSON file function
        return MakeHockeyJSONFileFromHockeyArray(inhockeyarray, outyamlfile, returnjson=returnyaml, jsonindent=yamlindent, beautify=beautify, sortkeys=sortkeys, encoding=encoding, verbose=verbose, verbosetype=verbosetype)


def MakeHockeyArrayFromHockeyYAML(inyamlfile, yamlisfile=True, verbose=False, verbosetype="array"):
    if testyaml:
        if yamlisfile and (os.path.isfile(inyamlfile) or re.findall("^(http|https|ftp|ftps|sftp)\\:\\/\\/", inyamlfile)):
            if re.findall("^(http|https|ftp|ftps|sftp)\\:\\/\\/", inyamlfile):
                inyamlfile = UncompressFileURL(inyamlfile)
                with inyamlfile as yamlfp:
                    try:
                        hockeyarray = yaml.load(yamlfp, Loader=yaml.SafeLoader)
                    except yaml.YAMLError:
                        return False
            else:
                with UncompressFile(inyamlfile) as yamlfp:
                    hockeyarray = yaml.load(yamlfp, Loader=yaml.SafeLoader)
        else:
            if not yamlisfile:
                chckcompression = CheckCompressionTypeFromString(inyamlfile)
                if not chckcompression:
                    yamlfp = StringIO(inyamlfile)
                else:
                    try:
                        inyamlsfile = BytesIO(inyamlfile.encode("utf-8"))
                    except TypeError:
                        inyamlsfile = BytesIO(inyamlfile)
                    yamlfp = UncompressFile(inyamlsfile)
                hockeyarray = yaml.load(yamlfp, Loader=yaml.SafeLoader)
            else:
                return False
        if not CheckHockeyArray(hockeyarray) and not CheckHockeySQLiteArray(hockeyarray):
            return False
        if verbose:
            if verbose and verbosetype == "json":
                VerbosePrintOut(MakeHockeJSONFromHockeyArray(hockeyarray, verbose=False))
            elif verbose and verbosetype == "yaml":
                VerbosePrintOut(MakeHockeYAMLFromHockeyArray(hockeyarray, verbose=False))
            elif verbosetype == "xml":
                VerbosePrintOut(MakeHockeyXMLFromHockeyArray(hockeyarray, verbose=False))
            elif verbosetype == "sgml":
                VerbosePrintOut(MakeHockeySGMLFromHockeyArray(hockeyarray, verbose=False))
            else:
                VerbosePrintOut(hockeyarray)
        return hockeyarray
    else:
        # Fallback to JSON loading
        return MakeHockeyArrayFromHockeyJSON(inyamlfile, jsonisfile=yamlisfile, verbose=verbose, verbosetype=verbosetype)


def MakeHockeySQLiteArrayFromHockeyYAML(inyamlfile, yamlisfile=True, verbose=False, verbosetype="array"):
    hockeyarray = MakeHockeyArrayFromHockeyYAML(inyamlfile, yamlisfile, verbose, verbosetype)
    return hockeyarray


def MakeHockeyPickleFromHockeyArray(inhockeyarray, protocol=pickledp, verbose=False, verbosetype="array"):
    if (not CheckHockeyArray(inhockeyarray) and not CheckHockeySQLiteArray(inhockeyarray)):
        return False
    if (protocol is None):
        picklestring = pickle.dumps(inhockeyarray, fix_imports=True)
    else:
        picklestring = pickle.dumps(
            inhockeyarray, protocol=protocol, fix_imports=True)
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose):
        VerbosePrintOut(inhockeyarray)
    return picklestring


def MakeHockeyPickleFileFromHockeyArray(inhockeyarray, outpicklefile=None, returnpickle=False, protocol=pickledp, encoding="UTF-8", verbose=False, verbosetype="array"):
    if (outpicklefile is None):
        return False
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outpicklefile))):
        picklefp = BytesIO()
    else:
        picklefp = CompressOpenFile(outpicklefile)
    picklestring = MakeHockeyPickleFromHockeyArray(
        inhockeyarray, protocol, verbose, verbosetype)
    try:
        picklefp.write(picklestring)
    except TypeError:
        picklefp.write(picklestring.encode(encoding))
    try:
        picklefp.flush()
        os.fsync(picklefp.fileno())
    except io.UnsupportedOperation:
        pass
    except AttributeError:
        pass
    except OSError as e:
        pass
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outpicklefile))):
        picklefp.seek(0, 0)
        upload_file_to_internet_file(picklefp, outpicklefile)
        picklefp.close()
    picklefp.close()
    if (returnpickle):
        return picklestring
    if (not returnpickle):
        return True
    return True


def MakeHockeyArrayFromHockeyPickle(inpicklefile, pickleisfile=True, encoding="UTF-8", verbose=False, verbosetype="array"):
    if (pickleisfile and ((os.path.exists(inpicklefile) and os.path.isfile(inpicklefile)) or re.findall("^(http|https|ftp|ftps|sftp)\\:\\/\\/", inpicklefile))):
        if (re.findall("^(http|https|ftp|ftps|sftp)\\:\\/\\/", inpicklefile)):
            inpicklefile = UncompressFileURL(
                inpicklefile)
            hockeyarray = pickle.load(inpicklefile)
        else:
            picklefp = UncompressFile(inpicklefile)
            hockeyarray = pickle.load(picklefp, fix_imports=True)
            picklefp.close()
    elif (not pickleisfile):
        picklefp = BytesIO(inpicklefile.encode(encoding))
        picklefp = UncompressFile(picklefp)
        hockeyarray = pickle.load(picklefp, fix_imports=True)
        picklefp.close()
    else:
        return False
    if (not CheckHockeyArray(hockeyarray) and not CheckHockeySQLiteArray(hockeyarray)):
        return False
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            hockeyarray, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            hockeyarray, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            hockeyarray, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            hockeyarray, verbose=False))
    elif (verbose):
        VerbosePrintOut(hockeyarray)
    return hockeyarray


def MakeHockeyMarshalFromHockeyArray(inhockeyarray, version=marshal.version, verbose=False, verbosetype="array"):
    if (not CheckHockeyArray(inhockeyarray) and not CheckHockeySQLiteArray(inhockeyarray)):
        return False
    marshalstring = marshal.dumps(inhockeyarray, version)
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose):
        VerbosePrintOut(inhockeyarray)
    return marshalstring


def MakeHockeyMarshalFileFromHockeyArray(inhockeyarray, outmarshalfile=None, returnmarshal=False, version=marshal.version, encoding="UTF-8", verbose=False, verbosetype="array"):
    if (outmarshalfile is None):
        return False
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outmarshalfile))):
        marshalfp = BytesIO()
    else:
        marshalfp = CompressOpenFile(outmarshalfile)
    marshalstring = MakeHockeyMarshalFromHockeyArray(
        inhockeyarray, version, verbose, verbosetype)
    try:
        marshalfp.write(marshalstring)
    except TypeError:
        marshalfp.write(marshalstring.encode(encoding))
    try:
        marshalfp.flush()
        os.fsync(marshalfp.fileno())
    except io.UnsupportedOperation:
        pass
    except AttributeError:
        pass
    except OSError as e:
        pass
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outmarshalfile))):
        marshalfp.seek(0, 0)
        upload_file_to_internet_file(marshalfp, outmarshalfile)
        marshalfp.close()
    marshalfp.close()
    if (returnmarshal):
        return marshalstring
    if (not returnmarshal):
        return True
    return True


def MakeHockeyArrayFromHockeyMarshal(inmarshalfile, marshalisfile=True, encoding="UTF-8", verbose=False, verbosetype="array"):
    if (marshalisfile and ((os.path.exists(inmarshalfile) and os.path.isfile(inmarshalfile)) or re.findall("^(http|https|ftp|ftps|sftp)\\:\\/\\/", inmarshalfile))):
        if (re.findall("^(http|https|ftp|ftps|sftp)\\:\\/\\/", inmarshalfile)):
            inmarshalfile = UncompressFileURL(
                inmarshalfile)
            hockeyarray = marshal.load(inmarshalfile)
        else:
            marshalfp = UncompressFile(inmarshalfile)
            hockeyarray = marshal.load(marshalfp)
            marshalfp.close()
    elif (not marshalisfile):
        marshalfp = BytesIO(inmarshalfile.encode(encoding))
        marshalfp = UncompressFile(marshalfp)
        hockeyarray = marshal.load(marshalfp)
        marshalfp.close()
    else:
        return False
    if (not CheckHockeyArray(hockeyarray) and not CheckHockeySQLiteArray(hockeyarray)):
        return False
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            hockeyarray, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            hockeyarray, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            hockeyarray, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            hockeyarray, verbose=False))
    elif (verbose):
        VerbosePrintOut(hockeyarray)
    return hockeyarray


def MakeHockeyShelveFromHockeyArray(inhockeyarray, version=pickledp, verbose=False, verbosetype="array"):
    if (not CheckHockeyArray(inhockeyarray) and not CheckHockeySQLiteArray(inhockeyarray)):
        return False
    outshelvefile = BytesIO()
    with shelve.open(outshelvefile, protocol=version) as shelf_file:
        for key, value in inhockeyarray.items():
            shelf_file[key] = value
    outshelvefile.seek(0, 0)
    shelvestring = outshelvefile.read()
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose):
        VerbosePrintOut(inhockeyarray)
    return shelvestring


def MakeHockeyShelveFileFromHockeyArray(inhockeyarray, outshelvefile=None, returnshelve=False, version=pickledp, verbose=False, verbosetype="array"):
    if (outshelvefile is None):
        return False
    with shelve.open(outshelvefile, protocol=version) as shelf_file:
        for key, value in inhockeyarray.items():
            shelf_file[key] = value
    if (returnshelve):
        shelvestring = MakeHockeyShelveFromHockeyArray(
            inhockeyarray, version, verbose, verbosetype)
        return shelvestring
    if (not returnshelve):
        return True
    return True


def MakeHockeyArrayFromHockeyShelve(inshelvefile, shelveisfile=True, version=pickledp, encoding="UTF-8", verbose=False, verbosetype="array"):
    if (shelveisfile):
        with shelve.open(inshelvefile, protocol=version) as shelf_file:
            hockeyarray = dict(shelf_file)
    else:
        try:
            inshelvefile = BytesIO(inshelvefile)
        except TypeError:
            inshelvefile = BytesIO(inshelvefile.encode(encoding))
        with shelve.open(inshelvefile, protocol=version) as shelf_file:
            hockeyarray = dict(shelf_file)
    if (not CheckHockeyArray(hockeyarray) and not CheckHockeySQLiteArray(hockeyarray)):
        return False
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            hockeyarray, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            hockeyarray, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            hockeyarray, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            hockeyarray, verbose=False))
    elif (verbose):
        VerbosePrintOut(hockeyarray)
    return hockeyarray


def MakeHockeyXMLFromHockeyArray(inhockeyarray, beautify=True, encoding="UTF-8", includedtd=True, verbose=False, verbosetype="array"):
    if (not CheckHockeyArray(inhockeyarray)):
        return False
    xmlstring = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    if(includedtd):
        xmlstring = xmlstring+"\n"+hockeyxmldtdstring;
    if "database" in inhockeyarray.keys():
        xmlstring = xmlstring+"<hockey database=\"" + \
            EscapeXMLString(
                str(inhockeyarray['database']), quote=True)+"\">\n"
    if "database" not in inhockeyarray.keys():
        xmlstring = xmlstring+"<hockey database=\"" + \
            EscapeXMLString(str(defaultsdbfile))+"\">\n"
    for hlkey in inhockeyarray['leaguelist']:
        xmlstring = xmlstring+" <league name=\""+EscapeXMLString(str(hlkey), quote=True)+"\" fullname=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['fullname']), quote=True)+"\" country=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['fullcountry']), quote=True)+"\" date=\""+EscapeXMLString(str(
            inhockeyarray[hlkey]['leagueinfo']['date']), quote=True)+"\" playofffmt=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['playofffmt']), quote=True)+"\" ordertype=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['ordertype']), quote=True)+"\" conferences=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['conferences']), quote=True)+"\" divisions=\""+EscapeXMLString(str(inhockeyarray[hlkey]['leagueinfo']['divisions']), quote=True)+"\">\n"
        conferencecount = 0
        conferenceend = len(inhockeyarray[hlkey]['conferencelist'])
        for hckey in inhockeyarray[hlkey]['conferencelist']:
            xmlstring = xmlstring+"  <conference name=\""+EscapeXMLString(str(hckey), quote=True)+"\" prefix=\""+EscapeXMLString(str(
                inhockeyarray[hlkey][hckey]['conferenceinfo']['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey]['conferenceinfo']['suffix']), quote=True)+"\">\n"
            for hdkey in inhockeyarray[hlkey][hckey]['divisionlist']:
                xmlstring = xmlstring+"   <division name=\""+EscapeXMLString(str(hdkey), quote=True)+"\" prefix=\""+EscapeXMLString(str(
                    inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix']), quote=True)+"\">\n"
                for htkey in inhockeyarray[hlkey][hckey][hdkey]['teamlist']:
                    xmlstring = xmlstring+"    <team city=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']), quote=True)+"\" area=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(
                        inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(htkey), quote=True)+"\" arena=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']), quote=True)+"\" prefix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']), quote=True)+"\" suffix=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']), quote=True)+"\" affiliates=\""+EscapeXMLString(str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['affiliates']), quote=True)+"\" />\n"
                xmlstring = xmlstring+"   </division>\n"
            xmlstring = xmlstring+"  </conference>\n"
            conferencecount = conferencecount + 1
        if (conferencecount >= conferenceend):
            hasarenas = False
            if (len(inhockeyarray[hlkey]['arenas']) > 0):
                hasarenas = True
                xmlstring = xmlstring+"  <arenas>\n"
            for hakey in inhockeyarray[hlkey]['arenas']:
                if (hakey):
                    hasarenas = True
                    xmlstring = xmlstring+"   <arena city=\""+EscapeXMLString(str(hakey['city']), quote=True)+"\" area=\""+EscapeXMLString(str(hakey['area']), quote=True)+"\" fullarea=\""+EscapeXMLString(str(
                        hakey['fullarea']), quote=True)+"\" country=\""+EscapeXMLString(str(hakey['country']), quote=True)+"\" fullcountry=\""+EscapeXMLString(str(hakey['fullcountry']), quote=True)+"\" name=\""+EscapeXMLString(str(hakey['name']), quote=True)+"\" />\n"
            if (hasarenas):
                xmlstring = xmlstring+"  </arenas>\n"
            hasgames = False
            if (len(inhockeyarray[hlkey]['games']) > 0):
                hasgames = True
                xmlstring = xmlstring+"  <games>\n"
            for hgkey in inhockeyarray[hlkey]['games']:
                if (hgkey):
                    hasgames = True
                    xmlstring = xmlstring+"   <game date=\""+EscapeXMLString(str(hgkey['date']), quote=True)+"\" time=\""+EscapeXMLString(str(hgkey['time']), quote=True)+"\" hometeam=\""+EscapeXMLString(str(hgkey['hometeam']), quote=True)+"\" awayteam=\""+EscapeXMLString(str(hgkey['awayteam']), quote=True)+"\" goals=\""+EscapeXMLString(str(hgkey['goals']), quote=True)+"\" sogs=\""+EscapeXMLString(str(hgkey['sogs']), quote=True)+"\" ppgs=\""+EscapeXMLString(str(hgkey['ppgs']), quote=True)+"\" shgs=\""+EscapeXMLString(str(
                        hgkey['shgs']), quote=True)+"\" penalties=\""+EscapeXMLString(str(hgkey['penalties']), quote=True)+"\" pims=\""+EscapeXMLString(str(hgkey['pims']), quote=True)+"\" hits=\""+EscapeXMLString(str(hgkey['hits']), quote=True)+"\" takeaways=\""+EscapeXMLString(str(hgkey['takeaways']), quote=True)+"\" faceoffwins=\""+EscapeXMLString(str(hgkey['faceoffwins']), quote=True)+"\" atarena=\""+EscapeXMLString(str(hgkey['atarena']), quote=True)+"\" isplayoffgame=\""+EscapeXMLString(str(hgkey['isplayoffgame']), quote=True)+"\" />\n"
            if (hasgames):
                xmlstring = xmlstring+"  </games>\n"
        xmlstring = xmlstring+" </league>\n"
    xmlstring = xmlstring+"</hockey>\n"
    xmlstring = BeautifyXMLCode(xmlstring, False, " ", "\n", encoding, beautify)
    if (not CheckHockeyXML(xmlstring, False)):
        return False
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(xmlstring)
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose):
        VerbosePrintOut(inhockeyarray)
    return xmlstring


def MakeHockeyXMLFileFromHockeyArray(inhockeyarray, outxmlfile=None, returnxml=False, beautify=True, encoding="UTF-8", includedtd=True, verbose=False, verbosetype="array"):
    if (outxmlfile is None):
        return False
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outxmlfile))):
        xmlfp = BytesIO()
    else:
        xmlfp = CompressOpenFile(outxmlfile)
    xmlstring = MakeHockeyXMLFromHockeyArray(inhockeyarray, beautify, encoding, includedtd, verbose, verbosetype)
    try:
        xmlfp.write(xmlstring)
    except TypeError:
        xmlfp.write(xmlstring.encode(encoding))
    try:
        xmlfp.flush()
        os.fsync(xmlfp.fileno())
    except io.UnsupportedOperation:
        pass
    except AttributeError:
        pass
    except OSError as e:
        pass
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outxmlfile))):
        xmlfp.seek(0, 0)
        upload_file_to_internet_file(xmlfp, outxmlfile)
        xmlfp.close()
    xmlfp.close()
    if (returnxml):
        return xmlstring
    if (not returnxml):
        return True
    return True


def MakeHockeySGMLFromHockeyArray(inhockeyarray, beautify=True, encoding="UTF-8", includedtd=True, verbose=False, verbosetype="array"):
    if not CheckHockeyArray(inhockeyarray):
        return False
    sgmlstring = ""
    database_value = inhockeyarray.get('database', defaultsdbfile)
    if(includedtd):
        sgmlstring = sgmlstring+hockeysgmldtdstring;
    sgmlstring += "<hockey database=\"" + EscapeSGMLString(str(database_value), quote=True) + "\">\n"

    for hlkey in inhockeyarray['leaguelist']:
        league_info = inhockeyarray[hlkey]['leagueinfo']
        sgmlstring += " <league name=\"" + EscapeSGMLString(str(hlkey)) + "\" fullname=\"" + EscapeSGMLString(str(league_info['fullname'])) + "\" country=\"" + EscapeSGMLString(str(league_info['country'])) + "\" fullcountry=\"" + EscapeSGMLString(str(league_info['fullcountry'])) + "\" date=\"" + EscapeSGMLString(str(league_info['date'])) + "\" playofffmt=\"" + EscapeSGMLString(str(league_info['playofffmt'])) + "\" ordertype=\"" + EscapeSGMLString(str(league_info['ordertype'])) + "\" conferences=\"" + EscapeSGMLString(str(league_info['conferences'])) + "\" divisions=\"" + EscapeSGMLString(str(league_info['divisions'])) + "\">\n"

        for hckey in inhockeyarray[hlkey]['conferencelist']:
            conference_info = inhockeyarray[hlkey][hckey]['conferenceinfo']
            sgmlstring += "  <conference name=\"" + EscapeSGMLString(str(hckey)) + "\" prefix=\"" + EscapeSGMLString(str(conference_info['prefix'])) + "\" suffix=\"" + EscapeSGMLString(str(conference_info['suffix'])) + "\">\n"

            for hdkey in inhockeyarray[hlkey][hckey]['divisionlist']:
                division_info = inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']
                sgmlstring += "   <division name=\"" + EscapeSGMLString(str(hdkey)) + "\" prefix=\"" + EscapeSGMLString(str(division_info['prefix'])) + "\" suffix=\"" + EscapeSGMLString(str(division_info['suffix'])) + "\">\n"

                for htkey in inhockeyarray[hlkey][hckey][hdkey]['teamlist']:
                    teaminfo = inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']
                    sgmlstring += ("    <team city=\"" + EscapeSGMLString(str(teaminfo['city'])) +
                                   "\" area=\"" + EscapeSGMLString(str(teaminfo['area'])) +
                                   "\" fullarea=\"" + EscapeSGMLString(str(teaminfo['fullarea'])) +
                                   "\" country=\"" + EscapeSGMLString(str(teaminfo['country'])) +
                                   "\" fullcountry=\"" + EscapeSGMLString(str(teaminfo['fullcountry'])) +
                                   "\" name=\"" + EscapeSGMLString(str(htkey)) +
                                   "\" arena=\"" + EscapeSGMLString(str(teaminfo['arena'])) +
                                   "\" prefix=\"" + EscapeSGMLString(str(teaminfo['prefix'])) +
                                   "\" suffix=\"" + EscapeSGMLString(str(teaminfo['suffix'])) +
                                   "\" affiliates=\"" + EscapeSGMLString(str(teaminfo['affiliates'])) + "\">\n")
                sgmlstring += "   </division>\n"
            sgmlstring += "  </conference>\n"

        if 'arenas' in inhockeyarray[hlkey] and len(inhockeyarray[hlkey]['arenas']) > 0:
            sgmlstring += "  <arenas>\n"
            for hakey in inhockeyarray[hlkey]['arenas']:
                if hakey:
                    sgmlstring += ("   <arena city=\"" + EscapeSGMLString(str(hakey['city'])) +
                                   "\" area=\"" + EscapeSGMLString(str(hakey['area'])) +
                                   "\" fullarea=\"" + EscapeSGMLString(str(hakey['fullarea'])) +
                                   "\" country=\"" + EscapeSGMLString(str(hakey['country'])) +
                                   "\" fullcountry=\"" + EscapeSGMLString(str(hakey['fullcountry'])) +
                                   "\" name=\"" + EscapeSGMLString(str(hakey['name'])) + "\">\n")
            sgmlstring += "  </arenas>\n"

        if 'games' in inhockeyarray[hlkey] and len(inhockeyarray[hlkey]['games']) > 0:
            sgmlstring += "  <games>\n"
            for hgkey in inhockeyarray[hlkey]['games']:
                if hgkey:
                    sgmlstring += ("   <game date=\"" + EscapeSGMLString(str(hgkey['date'])) +
                                   "\" time=\"" + EscapeSGMLString(str(hgkey['time'])) +
                                   "\" hometeam=\"" + EscapeSGMLString(str(hgkey['hometeam'])) +
                                   "\" awayteam=\"" + EscapeSGMLString(str(hgkey['awayteam'])) +
                                   "\" goals=\"" + EscapeSGMLString(str(hgkey['goals'])) +
                                   "\" sogs=\"" + EscapeSGMLString(str(hgkey['sogs'])) +
                                   "\" ppgs=\"" + EscapeSGMLString(str(hgkey['ppgs'])) +
                                   "\" shgs=\"" + EscapeSGMLString(str(hgkey['shgs'])) +
                                   "\" penalties=\"" + EscapeSGMLString(str(hgkey['penalties'])) +
                                   "\" pims=\"" + EscapeSGMLString(str(hgkey['pims'])) +
                                   "\" hits=\"" + EscapeSGMLString(str(hgkey['hits'])) +
                                   "\" takeaways=\"" + EscapeSGMLString(str(hgkey['takeaways'])) +
                                   "\" faceoffwins=\"" + EscapeSGMLString(str(hgkey['faceoffwins'])) +
                                   "\" atarena=\"" + EscapeSGMLString(str(hgkey['atarena'])) +
                                   "\" isplayoffgame=\"" + EscapeSGMLString(str(hgkey['isplayoffgame'])) + "\">\n")
            sgmlstring += "  </games>\n"

        sgmlstring += " </league>\n"
    sgmlstring += "</hockey>\n"

    if (not CheckHockeySGML(sgmlstring, False)):
        return False

    if verbose:
        if verbosetype=="json":
            VerbosePrintOut(MakeHockeyJSONFromHockeyArray(inhockeyarray, verbose=False))
        elif verbosetype=="yaml":
            VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(inhockeyarray, verbose=False))
        elif verbosetype=="xml":
            VerbosePrintOut(MakeHockeyXMLFromHockeyArray(inhockeyarray, verbose=False))
        elif verbosetype=="sgmml":
            VerbosePrintOut(sgmlstring)
        else:
            VerbosePrintOut(inhockeyarray)

    return sgmlstring


def MakeHockeySGMLFileFromHockeyArray(inhockeyarray, outsgmlfile=None, returnsgml=False, beautify=True, encoding="UTF-8", includedtd=True, verbose=False, verbosetype="array"):
    if (outsgmlfile is None):
        return False
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outsgmlfile))):
        sgmlfp = BytesIO()
    else:
        sgmlfp = CompressOpenFile(outsgmlfile)
    sgmlstring = MakeHockeySGMLFromHockeyArray(inhockeyarray, beautify, encoding, includedtd, verbose, verbosetype)
    try:
        sgmlfp.write(sgmlstring)
    except TypeError:
        sgmlfp.write(sgmlstring.encode(encoding))
    try:
        sgmlfp.flush()
        os.fsync(sgmlfp.fileno())
    except io.UnsupportedOperation:
        pass
    except AttributeError:
        pass
    except OSError as e:
        pass
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outsgmlfile))):
        sgmlfp.seek(0, 0)
        upload_file_to_internet_file(sgmlfp, outsgmlfile)
        sgmlfp.close()
    sgmlfp.close()
    if (returnsgml):
        return sgmlstring
    if (not returnsgml):
        return True
    return True


def MakeHockeyXMLAltFromHockeyArray(inhockeyarray, beautify=True, encoding="UTF-8", includedtd=True, verbose=False, verbosetype="array"):
    if (not CheckHockeyArray(inhockeyarray)):
        return False
    if "database" in inhockeyarray.keys():
        xmlstring_hockey = cElementTree.Element(
            "hockey", {'database': str(inhockeyarray['database'])})
    if "database" not in inhockeyarray.keys():
        xmlstring_hockey = cElementTree.Element(
            "hockey", {'database': str(defaultsdbfile)})
    for hlkey in inhockeyarray['leaguelist']:
        xmlstring_league = cElementTree.SubElement(xmlstring_hockey, "league", {'name': str(hlkey), 'fullname': str(inhockeyarray[hlkey]['leagueinfo']['fullname']), 'country': str(inhockeyarray[hlkey]['leagueinfo']['country']), 'fullcountry': str(inhockeyarray[hlkey]['leagueinfo']['fullcountry']), 'date': str(
            inhockeyarray[hlkey]['leagueinfo']['date']), 'playofffmt': str(inhockeyarray[hlkey]['leagueinfo']['playofffmt']), 'ordertype': str(inhockeyarray[hlkey]['leagueinfo']['ordertype']), 'conferences': str(inhockeyarray[hlkey]['leagueinfo']['conferences']), 'divisions': str(inhockeyarray[hlkey]['leagueinfo']['divisions'])})
        conferencecount = 0
        conferenceend = len(inhockeyarray[hlkey]['conferencelist'])
        for hckey in inhockeyarray[hlkey]['conferencelist']:
            xmlstring_conference = cElementTree.SubElement(xmlstring_league, "conference", {'name': str(hckey), 'prefix': str(
                inhockeyarray[hlkey][hckey]['conferenceinfo']['prefix']), 'suffix': str(inhockeyarray[hlkey][hckey]['conferenceinfo']['suffix'])})
            for hdkey in inhockeyarray[hlkey][hckey]['divisionlist']:
                xmlstring_division = cElementTree.SubElement(xmlstring_conference, "division", {'name': str(hdkey), 'prefix': str(
                    inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix']), 'suffix': str(inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix'])})
                for htkey in inhockeyarray[hlkey][hckey][hdkey]['teamlist']:
                    xmlstring_team = cElementTree.SubElement(xmlstring_division, "team", {'city': str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']), 'area': str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']), 'fullarea': str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']), 'country': str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']), 'fullcountry': str(
                        inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']), 'name': str(htkey), 'arena': str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']), 'prefix': str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']), 'suffix': str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']), 'affiliates': str(inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['affiliates'])})
            conferencecount = conferencecount + 1
        if (conferencecount >= conferenceend):
            hasarenas = False
            if (len(inhockeyarray[hlkey]['arenas']) > 0):
                hasarenas = True
                xmlstring_arenas = cElementTree.SubElement(
                    xmlstring_league, "arenas")
            for hakey in inhockeyarray[hlkey]['arenas']:
                if (hakey):
                    hasarenas = True
                    xmlstring_arena = cElementTree.SubElement(xmlstring_arenas, "arena", {'city': str(hakey['city']), 'area': str(hakey['area']), 'fullarea': str(
                        hakey['fullarea']), 'country': str(hakey['country']), 'fullcountry': str(hakey['fullcountry']), 'name': str(htkey)})
            hasgames = False
            if (len(inhockeyarray[hlkey]['games']) > 0):
                hasgames = True
                xmlstring_games = cElementTree.SubElement(
                    xmlstring_league, "games")
            for hgkey in inhockeyarray[hlkey]['games']:
                if (hgkey):
                    hasgames = True
                    xmlstring_game = cElementTree.SubElement(xmlstring_games, "game", {'date': str(hgkey['date']), 'time': str(hgkey['time']), 'hometeam': str(hgkey['hometeam']), 'awayteam': str(hgkey['awayteam']), 'goals': str(hgkey['goals']), 'sogs': str(hgkey['sogs']), 'ppgs': str(hgkey['ppgs']), 'shgs': str(
                        hgkey['shgs']), 'penalties': str(hgkey['penalties']), 'pims': str(hgkey['pims']), 'hits': str(hgkey['hits']), 'takeaways': str(hgkey['takeaways']), 'faceoffwins': str(hgkey['faceoffwins']), 'atarena': str(hgkey['atarena']), 'isplayoffgame': str(hgkey['isplayoffgame'])})
    '''xmlstring = cElementTree.tostring(xmlstring_hockey, encoding, "xml", True, "xml", True)'''
    try:
        xmlstring = cElementTree.tostring(
                xmlstring_hockey, encoding=encoding, method="xml", xml_declaration=True)
    except TypeError:
        xmlstring = cElementTree.tostring(
                xmlstring_hockey, encoding=encoding, method="xml")
    if (hasattr(xmlstring, 'decode')):
        xmlstring = xmlstring.decode(encoding)

    # Insert the DTD after the XML declaration, before the root element
    if includedtd:
        xml_declaration = '<?xml version="1.0" encoding="{}"?>\n'.format(encoding)
        xmlstring = xml_declaration + hockeyxmldtdstring + "\n" + xmlstring[len(xml_declaration):]

    xmlstring = BeautifyXMLCode(xmlstring, False, " ", "\n", encoding, beautify)
    if (hasattr(xmlstring, 'decode')):
        xmlstring = xmlstring.decode(encoding)
    if (not CheckHockeyXML(xmlstring, False)):
        return False
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(xmlstring)
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose):
        VerbosePrintOut(inhockeyarray)
    return xmlstring


def MakeHockeyXMLAltFileFromHockeyArray(inhockeyarray, outxmlfile=None, returnxml=False, beautify=True, encoding="UTF-8", includedtd=True, verbose=False, verbosetype="array"):
    if (outxmlfile is None):
        return False
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outxmlfile))):
        xmlfp = BytesIO()
    else:
        xmlfp = CompressOpenFile(outxmlfile)
    xmlstring = MakeHockeyXMLAltFromHockeyArray(
        inhockeyarray, beautify, encoding, includedtd, verbose, verbosetype)
    try:
        xmlfp.write(xmlstring)
    except TypeError:
        xmlfp.write(xmlstring.encode(encoding))
    try:
        xmlfp.flush()
        os.fsync(xmlfp.fileno())
    except io.UnsupportedOperation:
        pass
    except AttributeError:
        pass
    except OSError as e:
        pass
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outxmlfile))):
        xmlfp.seek(0, 0)
        upload_file_to_internet_file(xmlfp, outxmlfile)
        xmlfp.close()
    xmlfp.close()
    if (returnxml):
        return xmlstring
    if (not returnxml):
        return True
    return True


def MakeHockeyArrayFromHockeyXML(inxmlfile, xmlisfile=True, encoding="UTF-8", verbose=False, verbosetype="array"):
    if (not CheckHockeyXML(inxmlfile, xmlisfile)):
        return False
    if (xmlisfile and ((os.path.exists(inxmlfile) and os.path.isfile(inxmlfile)) or re.findall("^(http|https|ftp|ftps|sftp)\\:\\/\\/", inxmlfile))):
        try:
            if (re.findall("^(http|https|ftp|ftps|sftp)\\:\\/\\/", inxmlfile)):
                inxmlfile = UncompressFileURL(
                    inxmlfile)
                try:
                    hockeyfile = cElementTree.parse(
                        inxmlfile, parser=cElementTree.XMLParser(encoding=encoding))
                    hockeyroot = hockeyfile.getroot()
                except cElementTree.ParseError:
                    try:
                        inxmlfile.seek(0, 0)
                        hockeyroot = cElementTree.fromstring(inxmlfile.read())
                    except cElementTree.ParseError:
                        return False
            else:
                hockeyfile = cElementTree.parse(UncompressFile(
                    inxmlfile), parser=cElementTree.XMLParser(encoding=encoding))
                hockeyroot = hockeyfile.getroot()
        except cElementTree.ParseError:
            try:
                hockeyroot = cElementTree.fromstring(
                    UncompressFile(inxmlfile).read())
            except cElementTree.ParseError:
                return False
    elif (not xmlisfile):
        chckcompression = CheckCompressionTypeFromString(inxmlfile)
        if (not chckcompression):
            inxmlfile = StringIO(inxmlfile)
        else:
            try:
                inxmlsfile = BytesIO(inxmlfile)
            except TypeError:
                inxmlsfile = BytesIO(inxmlfile.encode(encoding))
            inxmlfile = UncompressFile(inxmlsfile)
        try:
            hockeyfile = cElementTree.parse(
                inxmlfile, parser=cElementTree.XMLParser(encoding=encoding))
            hockeyroot = hockeyfile.getroot()
        except cElementTree.ParseError:
            try:
                inxmlfile.seek(0, 0)
                hockeyroot = cElementTree.fromstring(inxmlfile.read())
            except cElementTree.ParseError:
                return False
    else:
        return False
    leaguearrayout = {'database': str(hockeyroot.attrib['database'])}
    leaguelist = []
    for getleague in hockeyroot:
        leaguearray = {}
        arenalist = []
        gamelist = []
        if (getleague.tag == "league"):
            tempdict = {'leagueinfo': {'name': str(getleague.attrib['name']), 'fullname': str(getleague.attrib['fullname']), 'country': str(getleague.attrib['country']), 'fullcountry': str(getleague.attrib['fullcountry']), 'date': str(getleague.attrib['date']), 'playofffmt': str(
                getleague.attrib['playofffmt']), 'ordertype': str(getleague.attrib['ordertype']), 'conferences': str(getleague.attrib['conferences']), 'divisions': str(getleague.attrib['divisions'])}, 'quickinfo': {'conferenceinfo': {}, 'divisioninfo': {}, 'teaminfo': {}}}
            leaguearray.update({str(getleague.attrib['name']): tempdict})
            leaguelist.append(str(getleague.attrib['name']))
        if (getleague.tag == "league"):
            conferencelist = []
            for getconference in getleague:
                if (getconference.tag == "conference"):
                    ConferenceFullName = GetFullTeamName(str(getconference.attrib['name']), str(
                        getconference.attrib['prefix']), str(getconference.attrib['suffix']))
                    leaguearray[str(getleague.attrib['name'])].update({str(getconference.attrib['name']): {'conferenceinfo': {'name': str(getconference.attrib['name']), 'prefix': str(
                        getconference.attrib['prefix']), 'suffix': str(getconference.attrib['suffix']), 'fullname': str(ConferenceFullName), 'league': str(getleague.attrib['name'])}}})
                    leaguearray[str(getleague.attrib['name'])]['quickinfo']['conferenceinfo'].update({str(getconference.attrib['name']): {
                        'name': str(getconference.attrib['name']), 'fullname': str(ConferenceFullName), 'league': str(getleague.attrib['name'])}})
                    conferencelist.append(str(getconference.attrib['name']))
                divisiondict = {}
                divisionlist = []
                if (getconference.tag == "conference"):
                    for getdivision in getconference:
                        DivisionFullName = GetFullTeamName(str(getdivision.attrib['name']), str(
                            getdivision.attrib['prefix']), str(getdivision.attrib['suffix']))
                        leaguearray[str(getleague.attrib['name'])][str(getconference.attrib['name'])].update({str(getdivision.attrib['name']): {'divisioninfo': {'name': str(getdivision.attrib['name']), 'prefix': str(
                            getdivision.attrib['prefix']), 'suffix': str(getdivision.attrib['suffix']), 'fullname': str(DivisionFullName), 'league': str(getleague.attrib['name']), 'conference': str(getconference.attrib['name'])}}})
                        leaguearray[str(getleague.attrib['name'])]['quickinfo']['divisioninfo'].update({str(getdivision.attrib['name']): {'name': str(
                            getdivision.attrib['name']), 'fullname': str(DivisionFullName), 'league': str(getleague.attrib['name']), 'conference': str(getconference.attrib['name'])}})
                        divisionlist.append(str(getdivision.attrib['name']))
                        teamdist = {}
                        teamlist = []
                        if (getdivision.tag == "division"):
                            for getteam in getdivision:
                                if (getteam.tag == "team"):
                                    fullteamname = GetFullTeamName(str(getteam.attrib['name']), str(
                                        getteam.attrib['prefix']), str(getteam.attrib['suffix']))
                                    leaguearray[str(getleague.attrib['name'])][str(getconference.attrib['name'])][str(getdivision.attrib['name'])].update({str(getteam.attrib['name']): {'teaminfo': {'city': str(getteam.attrib['city']), 'area': str(getteam.attrib['area']), 'fullarea': str(getteam.attrib['fullarea']), 'country': str(getteam.attrib['country']), 'fullcountry': str(getteam.attrib['fullcountry']), 'name': str(
                                        getteam.attrib['name']), 'fullname': fullteamname, 'arena': str(getteam.attrib['arena']), 'prefix': str(getteam.attrib['prefix']), 'suffix': str(getteam.attrib['suffix']), 'league': str(getleague.attrib['name']), 'conference': str(getconference.attrib['name']), 'division': str(getdivision.attrib['name']), 'affiliates': str(getteam.attrib['affiliates'])}}})
                                    leaguearray[str(getleague.attrib['name'])]['quickinfo']['teaminfo'].update({str(getteam.attrib['name']): {'name': str(getteam.attrib['name']), 'fullname': fullteamname, 'league': str(
                                        getleague.attrib['name']), 'conference': str(getconference.attrib['name']), 'division': str(getdivision.attrib['name'])}})
                                    teamlist.append(
                                        str(getteam.attrib['name']))
                            leaguearray[str(getleague.attrib['name'])][str(getconference.attrib['name'])][str(
                                getdivision.attrib['name'])].update({'teamlist': teamlist})
                    leaguearray[str(getleague.attrib['name'])][str(
                        getconference.attrib['name'])].update({'divisionlist': divisionlist})
                if (getconference.tag == "arenas"):
                    for getarenas in getconference:
                        arenalist.append({'city': str(getarenas.attrib['city']), 'area': str(getarenas.attrib['area']), 'fullarea': str(getarenas.attrib['fullarea']), 'country': str(
                            getarenas.attrib['country']), 'fullcountry': str(getarenas.attrib['fullcountry']), 'name': str(getarenas.attrib['name'])})
                leaguearray[str(getleague.attrib['name'])].update(
                    {"arenas": arenalist})
                if (getconference.tag == "games"):
                    for getgame in getconference:
                        gamelist.append({'date': str(getgame.attrib['date']), 'time': str(getgame.attrib['time']), 'hometeam': str(getgame.attrib['hometeam']), 'awayteam': str(getgame.attrib['awayteam']), 'goals': str(getgame.attrib['goals']), 'sogs': str(getgame.attrib['sogs']), 'ppgs': str(getgame.attrib['ppgs']), 'shgs': str(
                            getgame.attrib['shgs']), 'penalties': str(getgame.attrib['penalties']), 'pims': str(getgame.attrib['pims']), 'hits': str(getgame.attrib['hits']), 'takeaways': str(getgame.attrib['takeaways']), 'faceoffwins': str(getgame.attrib['faceoffwins']), 'atarena': str(getgame.attrib['atarena']), 'isplayoffgame': str(getgame.attrib['isplayoffgame'])})
                leaguearray[str(getleague.attrib['name'])
                            ].update({"games": gamelist})
            leaguearray[str(getleague.attrib['name'])].update(
                {'conferencelist': conferencelist})
            leaguearrayout.update(leaguearray)
    leaguearrayout.update({'leaguelist': leaguelist})
    if (not CheckHockeyArray(leaguearrayout)):
        return False
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose):
        VerbosePrintOut(leaguearrayout)
    return leaguearrayout


def MakeHockeyArrayFromHockeySGML(insgmlfile, sgmlisfile=True, encoding="UTF-8", verbose=False, verbosetype="array"):
    """
    Parses SGML data and converts it into a hockey array (nested dictionary).
    """
    if (not CheckHockeySGML(insgmlfile, sgmlisfile)):
        return False
    # Read SGML data
    sgml_data = ReadSGMLData(insgmlfile, sgmlisfile=sgmlisfile, encoding=encoding)
    if sgml_data is False:
        return False

    # Parse SGML data
    parser = HockeySGMLParser()
    try:
        parser.feed(sgml_data)
        parser.close()
    except Exception as e:
        return False

    leaguearrayout = parser.leaguearrayout
    leaguearrayout['leaguelist'] = parser.leaguelist

    # Check if the resulting array is valid
    if not CheckHockeyArray(leaguearrayout):
        return False

    # Verbose output
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose):
        VerbosePrintOut(leaguearrayout)

    return leaguearrayout


def MakeHockeyArrayFromHockeyXMLAlt(inxmlfile, xmlisfile=True, encoding="UTF-8", verbose=False, verbosetype="array"):
 return MakeHockeyArrayFromHockeySGML(inxmlfile, xmlisfile, encoding, verbose, verbosetype)


def MakeHockeyDatabaseFromHockeyArray(inhockeyarray, outsdbfile=None, returndb=False, verbose=False, verbosetype="array"):
    if (not CheckHockeyArray(inhockeyarray)):
        return False
    if (outsdbfile is None and "database" in inhockeyarray.keys()):
        sqldatacon = MakeHockeyDatabase(inhockeyarray['database'])
    if (outsdbfile is None and "database" not in inhockeyarray.keys()):
        sqldatacon = MakeHockeyDatabase(":memory:")
    if (outsdbfile is not None and isinstance(outsdbfile, basestring)):
        sqldatacon = MakeHockeyDatabase(outsdbfile)
    if (outsdbfile is not None and isinstance(outsdbfile, (tuple, list))):
        sqldatacon = tuple(outsdbfile)
        outsdbfile = GetHockeyDatabaseFileName(sqldatacon)
    if (not CheckHockeySQLiteDatabaseConnection(sqldatacon)):
        return False
    leaguecount = 0
    for hlkey in inhockeyarray['leaguelist']:
        sqldatacon[0].execute('BEGIN TRANSACTION')
        if (leaguecount == 0):
            MakeHockeyLeagueTable(sqldatacon)
        MakeHockeyTeamTable(sqldatacon, hlkey)
        MakeHockeyConferenceTable(sqldatacon, hlkey)
        MakeHockeyGameTable(sqldatacon, hlkey)
        MakeHockeyDivisionTable(sqldatacon, hlkey)
        HockeyLeagueHasConferences = True
        if (inhockeyarray[hlkey]['leagueinfo']['conferences'].lower() == "no"):
            HockeyLeagueHasConferences = False
        HockeyLeagueHasDivisions = True
        if (inhockeyarray[hlkey]['leagueinfo']['divisions'].lower() == "no"):
            HockeyLeagueHasDivisions = False
        MakeHockeyLeague(sqldatacon, hlkey, inhockeyarray[hlkey]['leagueinfo']['fullname'], inhockeyarray[hlkey]['leagueinfo']['country'], inhockeyarray[hlkey]['leagueinfo']
                         ['fullcountry'], inhockeyarray[hlkey]['leagueinfo']['date'], inhockeyarray[hlkey]['leagueinfo']['playofffmt'], inhockeyarray[hlkey]['leagueinfo']['ordertype'])
        leaguecount = leaguecount + 1
        conferencecount = 0
        conferenceend = len(inhockeyarray[hlkey]['conferencelist'])
        for hckey in inhockeyarray[hlkey]['conferencelist']:
            MakeHockeyConference(sqldatacon, hlkey, hckey, inhockeyarray[hlkey][hckey]['conferenceinfo'][
                                 'prefix'], inhockeyarray[hlkey][hckey]['conferenceinfo']['suffix'], HockeyLeagueHasConferences)
            for hdkey in inhockeyarray[hlkey][hckey]['divisionlist']:
                MakeHockeyDivision(sqldatacon, hlkey, hdkey, hckey, inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix'],
                                   inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix'], HockeyLeagueHasConferences, HockeyLeagueHasDivisions)
                for htkey in inhockeyarray[hlkey][hckey][hdkey]['teamlist']:
                    MakeHockeyTeam(sqldatacon, hlkey, str(inhockeyarray[hlkey]['leagueinfo']['date']), inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea'], htkey, inhockeyarray[
                                   hlkey][hckey]['conferenceinfo']['name'], inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['name'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix'], inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['affiliates'], HockeyLeagueHasConferences, HockeyLeagueHasDivisions)
            conferencecount = conferencecount + 1
        if (conferencecount >= conferenceend):
            hasarenas = False
            if (len(inhockeyarray[hlkey]['arenas']) > 0):
                hasarenas = True
            for hakey in inhockeyarray[hlkey]['arenas']:
                if (hakey):
                    hasarenas = True
                    MakeHockeyArena(sqldatacon, hlkey, hakey['city'], hakey['area'],
                                    hakey['country'], hakey['fullcountry'], hakey['fullarea'], hakey['name'])
            hasgames = False
            if (len(inhockeyarray[hlkey]['games']) > 0):
                hasgames = True
            for hgkey in inhockeyarray[hlkey]['games']:
                if (hgkey):
                    hasgames = True
                    MakeHockeyGame(sqldatacon, hlkey, hgkey['date'], hgkey['time'], hgkey['hometeam'], hgkey['awayteam'], hgkey['goals'], hgkey['sogs'], hgkey['ppgs'],
                                   hgkey['shgs'], hgkey['penalties'], hgkey['pims'], hgkey['hits'], hgkey['takeaways'], hgkey['faceoffwins'], hgkey['atarena'], hgkey['isplayoffgame'])
        sqldatacon[1].commit()
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose):
        VerbosePrintOut(inhockeyarray)
    if (not returndb):
        CloseHockeyDatabase(sqldatacon)
    if (returndb):
        return sqldatacon
    if (not returndb):
        return True
    return True


def MakeHockeyPythonFromHockeyArray(inhockeyarray, verbose=False, verbosetype="array"):
    if (not CheckHockeyArray(inhockeyarray)):
        return False
    pyfilename = __package__
    if (pyfilename == "__main__"):
        pyfilename = os.path.splitext(os.path.basename(__file__))[0]
    pystring = ("#!/usr/bin/env python\n" \
           "# -*- coding: utf-8 -*-\n\n" \
           "from __future__ import absolute_import, division, print_function, unicode_literals, generators, with_statement, nested_scopes\n" \
           "import " + pyfilename + ", sys, logging\n\n" \
           "# Python 2 handling: Reload sys and set UTF-8 encoding if applicable\n" \
           "try:\n" \
           "    reload(sys)  # Only relevant for Python 2\n" \
           "    if hasattr(sys, 'setdefaultencoding'):\n" \
           "        sys.setdefaultencoding('UTF-8')\n" \
           "except (NameError, AttributeError):\n" \
           "    pass\n\n" \
           "# Python 3 handling: Ensure stdout and stderr use UTF-8 encoding\n" \
           "if hasattr(sys.stdout, 'detach'):\n" \
           "    import io\n" \
           "    sys.stdout = io.TextIOWrapper(\n" \
           "        sys.stdout.detach(), encoding='UTF-8', errors='replace')\n" \
           "if hasattr(sys.stderr, 'detach'):\n" \
           "    import io\n" \
           "    sys.stderr = io.TextIOWrapper(\n" \
           "        sys.stderr.detach(), encoding='UTF-8', errors='replace')\n\n" \
           "logging.basicConfig(format=\"%(message)s\", stream=sys.stdout, level=logging.INFO)\n\n" \
           + "sqldatacon = " + pyfilename \
           + ".MakeHockeyDatabase(\"" + inhockeyarray['database'] + "\")\n")
    pystring = pystring+pyfilename+".MakeHockeyLeagueTable(sqldatacon)\n"
    for hlkey in inhockeyarray['leaguelist']:
        HockeyLeagueHasConferences = True
        if (inhockeyarray[hlkey]['leagueinfo']['conferences'].lower() == "no"):
            HockeyLeagueHasConferences = False
        HockeyLeagueHasDivisions = True
        if (inhockeyarray[hlkey]['leagueinfo']['divisions'].lower() == "no"):
            HockeyLeagueHasDivisions = False
        pystring = pystring+pyfilename+".MakeHockeyTeamTable(sqldatacon, \""+hlkey+"\")\n"+pyfilename+".MakeHockeyConferenceTable(sqldatacon, \""+hlkey+"\")\n"+pyfilename+".MakeHockeyGameTable(sqldatacon, \""+hlkey+"\")\n"+pyfilename+".MakeHockeyDivisionTable(sqldatacon, \""+hlkey+"\")\n"+pyfilename+".MakeHockeyLeague(sqldatacon, \""+hlkey+"\", \"" + \
            inhockeyarray[hlkey]['leagueinfo']['fullname']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['country']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullcountry']+"\", \"" + \
            inhockeyarray[hlkey]['leagueinfo']['date']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['playofffmt'] + \
            "\", \""+inhockeyarray[hlkey]['leagueinfo']['ordertype']+"\")\n"
        conferencecount = 0
        conferenceend = len(inhockeyarray[hlkey]['conferencelist'])
        for hckey in inhockeyarray[hlkey]['conferencelist']:
            pystring = pystring+pyfilename+".MakeHockeyConference(sqldatacon, \""+hlkey+"\", \""+hckey+"\", \""+inhockeyarray[hlkey][hckey]['conferenceinfo'][
                'prefix']+"\", \""+inhockeyarray[hlkey][hckey]['conferenceinfo']['suffix']+"\", "+str(HockeyLeagueHasConferences)+")\n"
            for hdkey in inhockeyarray[hlkey][hckey]['divisionlist']:
                pystring = pystring+pyfilename+".MakeHockeyDivision(sqldatacon, \""+hlkey+"\", \""+hdkey+"\", \""+hckey+"\", \""+inhockeyarray[hlkey][hckey][hdkey]['divisioninfo'][
                    'prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+")\n"
                for htkey in inhockeyarray[hlkey][hckey][hdkey]['teamlist']:
                    pystring = pystring+pyfilename+".MakeHockeyTeam(sqldatacon, \""+hlkey+"\", \""+str(inhockeyarray[hlkey]['leagueinfo']['date'])+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']+"\", \""+inhockeyarray[hlkey][hckey][
                        hdkey][htkey]['teaminfo']['fullarea']+"\", \""+htkey+"\", \""+hckey+"\", \""+hdkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['affiliates']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+")\n"
            conferencecount = conferencecount + 1
        if (conferencecount >= conferenceend):
            hasarenas = False
            if (len(inhockeyarray[hlkey]['arenas']) > 0):
                hasarenas = True
            for hakey in inhockeyarray[hlkey]['arenas']:
                if (hakey):
                    hasarenas = True
                    pystring = pystring+pyfilename+".MakeHockeyArena(sqldatacon, \""+hlkey+"\", \""+hakey['city']+"\", \""+hakey['area']+"\", \""+hakey[
                        'country']+"\", \""+hakey['fullcountry']+"\", \""+hakey['fullarea']+"\", \""+hakey['name']+"\")\n"
            hasgames = False
            if (len(inhockeyarray[hlkey]['games']) > 0):
                hasgames = True
            for hgkey in inhockeyarray[hlkey]['games']:
                if (hgkey):
                    hasgames = True
                    pystring = pystring+pyfilename+".MakeHockeyGame(sqldatacon, \""+hlkey+"\", "+hgkey['date']+", "+hgkey['time']+", \""+hgkey['hometeam']+"\", \""+hgkey['awayteam']+"\", \""+hgkey['goals']+"\", \""+hgkey['sogs']+"\", \""+hgkey[
                        'ppgs']+"\", \""+hgkey['shgs']+"\", \""+hgkey['penalties']+"\", \""+hgkey['pims']+"\", \""+hgkey['hits']+"\", \""+hgkey['takeaways']+"\", \""+hgkey['faceoffwins']+"\", \""+hgkey['atarena']+"\", \""+hgkey['isplayoffgame']+"\")\n"
    pystring = pystring+"\n"
    pystring = pystring+pyfilename+".CloseHockeyDatabase(sqldatacon)\n"
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose):
        VerbosePrintOut(inhockeyarray)
    return pystring


def MakeHockeyPythonFileFromHockeyArray(inhockeyarray, outpyfile=None, returnpy=False, encoding="UTF-8", verbose=False, verbosetype="array"):
    if (outpyfile is None):
        return False
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outpyfile))):
        pyfp = BytesIO()
    else:
        pyfp = CompressOpenFile(outpyfile)
    pystring = MakeHockeyPythonFromHockeyArray(inhockeyarray, verbose, verbosetype)
    try:
        pyfp.write(pystring)
    except TypeError:
        pyfp.write(pystring.encode(encoding))
    try:
        pyfp.flush()
        os.fsync(pyfp.fileno())
    except io.UnsupportedOperation:
        pass
    except AttributeError:
        pass
    except OSError as e:
        pass
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outpyfile))):
        pyfp.seek(0, 0)
        upload_file_to_internet_file(pyfp, outpyfile)
        pyfp.close()
    pyfp.close()
    if (fextname not in outextlistwd):
        os.chmod(outpyfile, 0o755)
    if (returnpy):
        return pystring
    if (not returnpy):
        return True
    return True


def MakeHockeyPythonAltFromHockeyArray(inhockeyarray, verbose=False, verbosetype="array", verbosepy=True):
    if (not CheckHockeyArray(inhockeyarray)):
        return False
    pyfilename = __package__
    if (pyfilename == "__main__"):
        pyfilename = os.path.splitext(os.path.basename(__file__))[0]
    pystring = ("#!/usr/bin/env python\n" \
           "# -*- coding: utf-8 -*-\n\n" \
           "from __future__ import absolute_import, division, print_function, unicode_literals, generators, with_statement, nested_scopes\n" \
           "import " + pyfilename + ", sys, logging\n\n" \
           "# Python 2 handling: Reload sys and set UTF-8 encoding if applicable\n" \
           "try:\n" \
           "    reload(sys)  # Only relevant for Python 2\n" \
           "    if hasattr(sys, 'setdefaultencoding'):\n" \
           "        sys.setdefaultencoding('UTF-8')\n" \
           "except (NameError, AttributeError):\n" \
           "    pass\n\n" \
           "# Python 3 handling: Ensure stdout and stderr use UTF-8 encoding\n" \
           "if hasattr(sys.stdout, 'detach'):\n" \
           "    import io\n" \
           "    sys.stdout = io.TextIOWrapper(\n" \
           "        sys.stdout.detach(), encoding='UTF-8', errors='replace')\n" \
           "if hasattr(sys.stderr, 'detach'):\n" \
           "    import io\n" \
           "    sys.stderr = io.TextIOWrapper(\n" \
           "        sys.stderr.detach(), encoding='UTF-8', errors='replace')\n\n" \
           "logging.basicConfig(format=\"%(message)s\", stream=sys.stdout, level=logging.INFO)\n\n" \
           + "hockeyarray = " + pyfilename \
           + ".CreateHockeyArray(\""+inhockeyarray['database']+"\")\n")
    for hlkey in inhockeyarray['leaguelist']:
        HockeyLeagueHasConferences = True
        if (inhockeyarray[hlkey]['leagueinfo']['conferences'].lower() == "no"):
            HockeyLeagueHasConferences = False
        HockeyLeagueHasDivisions = True
        if (inhockeyarray[hlkey]['leagueinfo']['divisions'].lower() == "no"):
            HockeyLeagueHasDivisions = False
        pystring = pystring+pyfilename+".AddHockeyLeagueToArray(hockeyarray, \""+hlkey+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullname']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['country']+"\", \""+inhockeyarray[hlkey]['leagueinfo'][
            'fullcountry']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['date']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['playofffmt']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['ordertype']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+")\n"
        conferencecount = 0
        conferenceend = len(inhockeyarray[hlkey]['conferencelist'])
        for hckey in inhockeyarray[hlkey]['conferencelist']:
            pystring = pystring+pyfilename + \
                ".AddHockeyConferenceToArray(hockeyarray, \"" + \
                hlkey+"\", \""+hckey+"\")\n"
            for hdkey in inhockeyarray[hlkey][hckey]['divisionlist']:
                pystring = pystring+pyfilename+".AddHockeyDivisionToArray(hockeyarray, \""+hlkey+"\", \""+hdkey+"\", \""+hckey+"\", \"" + \
                    inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['prefix']+"\", \"" + \
                    inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix']+"\")\n"
                for htkey in inhockeyarray[hlkey][hckey][hdkey]['teamlist']:
                    pystring = pystring+pyfilename+".AddHockeyTeamToArray(hockeyarray, \""+hlkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']+"\", \""+inhockeyarray[
                        hlkey][hckey][hdkey][htkey]['teaminfo']['fullarea']+"\", \""+htkey+"\", \""+hckey+"\", \""+hdkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['affiliates']+"\")\n"
            conferencecount = conferencecount + 1
        if (conferencecount >= conferenceend):
            hasarenas = False
            if (len(inhockeyarray[hlkey]['arenas']) > 0):
                hasarenas = True
            for hakey in inhockeyarray[hlkey]['arenas']:
                if (hakey):
                    hasarenas = True
                    pystring = pystring+pyfilename + \
                        ".AddHockeyArenaToArray(hockeyarray, \""+hlkey+"\", \""+hakey['city']+"\", \""+hakey['area']+"\", \"" + \
                        hakey['country']+"\", \""+hakey['fullcountry']+"\", \"" + \
                        hakey['fullarea']+"\", \""+hakey['name']+"\")\n"
            hasgames = False
            if (len(inhockeyarray[hlkey]['games']) > 0):
                hasgames = True
            for hgkey in inhockeyarray[hlkey]['games']:
                if (hgkey):
                    hasgames = True
                    pystring = pystring+pyfilename+".AddHockeyGameToArray(hockeyarray, \""+hlkey+"\", "+hgkey['date']+", "+hgkey['time']+", \""+hgkey['hometeam']+"\", \""+hgkey['awayteam']+"\", \""+hgkey['goals']+"\", \""+hgkey['sogs']+"\", \""+hgkey[
                        'ppgs']+"\", \""+hgkey['shgs']+"\", \""+hgkey['penalties']+"\", \""+hgkey['pims']+"\", \""+hgkey['hits']+"\", \""+hgkey['takeaways']+"\", \""+hgkey['faceoffwins']+"\", \""+hgkey['atarena']+"\", \""+hgkey['isplayoffgame']+"\")\n"
    pystring = pystring+"\n"
    if (verbosepy):
        pyverbose = "True"
    elif (not verbosepy):
        pyverbose = "False"
    else:
        pyverbose = "False"
    pystring = pystring+pyfilename + \
        ".MakeHockeyDatabaseFromHockeyArray(hockeyarray, None, False, "+str(
            pyverbose)+", \""+str(verbosetype)+"\")\n"
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose):
        VerbosePrintOut(inhockeyarray)
    return pystring


def MakeHockeyPythonAltFileFromHockeyArray(inhockeyarray, outpyfile=None, returnpy=False, encoding="UTF-8", verbose=False, verbosetype="array", verbosepy=True):
    if (outpyfile is None):
        return False
    pyfp = CompressOpenFile(outpyfile)
    pystring = MakeHockeyPythonAltFromHockeyArray(
        inhockeyarray, verbose, verbosetype, verbosepy)
    try:
        pyfp.write(pystring)
    except TypeError:
        pyfp.write(pystring.encode(encoding))
    try:
        pyfp.flush()
        os.fsync(pyfp.fileno())
    except io.UnsupportedOperation:
        pass
    except AttributeError:
        pass
    except OSError as e:
        pass
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outpyfile))):
        pyfp.seek(0, 0)
        upload_file_to_internet_file(pyfp, outpyfile)
        pyfp.close()
    pyfp.close()
    if (fextname not in outextlistwd):
        os.chmod(outpyfile, 0o755)
    if (returnpy):
        return pystring
    if (not returnpy):
        return True
    return True


def MakeHockeyPythonOOPFromHockeyArray(inhockeyarray, verbose=False, verbosetype="array"):
    if (not CheckHockeyArray(inhockeyarray)):
        return False
    pyfilename = __package__
    if (pyfilename == "__main__"):
        pyfilename = os.path.splitext(os.path.basename(__file__))[0]
    pystring = ("#!/usr/bin/env python\n" \
           "# -*- coding: utf-8 -*-\n\n" \
           "from __future__ import absolute_import, division, print_function, unicode_literals, generators, with_statement, nested_scopes\n" \
           "import " + pyfilename + ", sys, logging\n\n" \
           "# Python 2 handling: Reload sys and set UTF-8 encoding if applicable\n" \
           "try:\n" \
           "    reload(sys)  # Only relevant for Python 2\n" \
           "    if hasattr(sys, 'setdefaultencoding'):\n" \
           "        sys.setdefaultencoding('UTF-8')\n" \
           "except (NameError, AttributeError):\n" \
           "    pass\n\n" \
           "# Python 3 handling: Ensure stdout and stderr use UTF-8 encoding\n" \
           "if hasattr(sys.stdout, 'detach'):\n" \
           "    import io\n" \
           "    sys.stdout = io.TextIOWrapper(\n" \
           "        sys.stdout.detach(), encoding='UTF-8', errors='replace')\n" \
           "if hasattr(sys.stderr, 'detach'):\n" \
           "    import io\n" \
           "    sys.stderr = io.TextIOWrapper(\n" \
           "        sys.stderr.detach(), encoding='UTF-8', errors='replace')\n\n" \
           "logging.basicConfig(format=\"%(message)s\", stream=sys.stdout, level=logging.INFO)\n\n" \
           + "sqldatacon = " + pyfilename \
           + ".MakeHockeyData(\""+inhockeyarray['database']+"\")\n")
    for hlkey in inhockeyarray['leaguelist']:
        HockeyLeagueHasConferences = True
        if (inhockeyarray[hlkey]['leagueinfo']['conferences'].lower() == "no"):
            HockeyLeagueHasConferences = False
        HockeyLeagueHasDivisions = True
        if (inhockeyarray[hlkey]['leagueinfo']['divisions'].lower() == "no"):
            HockeyLeagueHasDivisions = False
        pystring = pystring+"sqldatacon.MakeHockeyTeamTable(\""+hlkey+"\")\n"+"sqldatacon.MakeHockeyConferenceTable(\""+hlkey+"\")\n"+"sqldatacon.MakeHockeyGameTable(\""+hlkey+"\")\n"+"sqldatacon.MakeHockeyDivisionTable(\""+hlkey+"\")\n"+"sqldatacon.AddHockeyLeague(\""+hlkey+"\", \"" + \
            inhockeyarray[hlkey]['leagueinfo']['fullname']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['country']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullcountry']+"\", \"" + \
            inhockeyarray[hlkey]['leagueinfo']['date']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['playofffmt'] + \
            "\", \""+inhockeyarray[hlkey]['leagueinfo']['ordertype']+"\")\n"
        conferencecount = 0
        conferenceend = len(inhockeyarray[hlkey]['conferencelist'])
        for hckey in inhockeyarray[hlkey]['conferencelist']:
            pystring = pystring+"sqldatacon.AddHockeyConference(\""+hlkey+"\", \""+hckey+"\", \""+inhockeyarray[hlkey][hckey]['conferenceinfo'][
                'prefix']+"\", \""+inhockeyarray[hlkey][hckey]['conferenceinfo']['suffix']+"\", "+str(HockeyLeagueHasConferences)+")\n"
            for hdkey in inhockeyarray[hlkey][hckey]['divisionlist']:
                pystring = pystring+"sqldatacon.AddHockeyDivision(\""+hlkey+"\", \""+hdkey+"\", \""+hckey+"\", \""+inhockeyarray[hlkey][hckey][hdkey]['divisioninfo'][
                    'prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+")\n"
                for htkey in inhockeyarray[hlkey][hckey][hdkey]['teamlist']:
                    pystring = pystring+"sqldatacon.AddHockeyTeam(\""+hlkey+"\", \""+str(inhockeyarray[hlkey]['leagueinfo']['date'])+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']+"\", \""+inhockeyarray[hlkey][hckey][
                        hdkey][htkey]['teaminfo']['fullarea']+"\", \""+htkey+"\", \""+hckey+"\", \""+hdkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['affiliates']+"\", "+str(HockeyLeagueHasConferences)+", "+str(HockeyLeagueHasDivisions)+")\n"
            conferencecount = conferencecount + 1
        if (conferencecount >= conferenceend):
            hasarenas = False
            if (len(inhockeyarray[hlkey]['arenas']) > 0):
                hasarenas = True
            for hakey in inhockeyarray[hlkey]['arenas']:
                if (hakey):
                    hasarenas = True
                    pystring = pystring+"sqldatacon.AddHockeyArena(\""+hlkey+"\", \""+hakey['city']+"\", \""+hakey['area'] + \
                        "\", \""+hakey['country']+"\", \""+hakey['fullcountry'] + \
                        "\", \""+hakey['fullarea'] + \
                        "\", \""+hakey['name']+"\")\n"
            hasgames = False
            if (len(inhockeyarray[hlkey]['games']) > 0):
                hasgames = True
            for hgkey in inhockeyarray[hlkey]['games']:
                if (hgkey):
                    hasgames = True
                    pystring = pystring+"sqldatacon.AddHockeyGame(\""+hlkey+"\", "+hgkey['date']+", "+hgkey['time']+", \""+hgkey['hometeam']+"\", \""+hgkey['awayteam']+"\", \""+hgkey['goals']+"\", \""+hgkey['sogs']+"\", \""+hgkey['ppgs'] + \
                        "\", \""+hgkey['shgs']+"\", \""+hgkey['penalties']+"\", \""+hgkey['pims']+"\", \""+hgkey['hits']+"\", \"" + \
                        hgkey['takeaways']+"\", \""+hgkey['faceoffwins']+"\", \"" + \
                        hgkey['atarena']+"\", \"" + \
                        hgkey['isplayoffgame']+"\")\n"
    pystring = pystring+"\n"
    pystring = pystring+"sqldatacon.CloseHockeyDatabase(sqldatacon)\n"
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose):
        VerbosePrintOut(inhockeyarray)
    return pystring


def MakeHockeyPythonOOPFileFromHockeyArray(inhockeyarray, outpyfile=None, returnpy=False, encoding="UTF-8", verbose=False, verbosetype="array"):
    if (outpyfile is None):
        return False
    pyfp = CompressOpenFile(outpyfile)
    pystring = MakeHockeyPythonOOPFromHockeyArray(inhockeyarray, verbose, verbosetype)
    ()
    try:
        pyfp.write(pystring)
    except TypeError:
        pyfp.write(pystring.encode(encoding))
    try:
        pyfp.flush()
        os.fsync(pyfp.fileno())
    except io.UnsupportedOperation:
        pass
    except AttributeError:
        pass
    except OSError as e:
        pass
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outpyfile))):
        pyfp.seek(0, 0)
        upload_file_to_internet_file(pyfp, outpyfile)
        pyfp.close()
    pyfp.close()
    if (fextname not in outextlistwd):
        os.chmod(outpyfile, 0o755)
    if (returnpy):
        return pystring
    if (not returnpy):
        return True
    return True


def MakeHockeyPythonOOPAltFromHockeyArray(inhockeyarray, verbose=False, verbosetype="array", verbosepy=True):
    if (not CheckHockeyArray(inhockeyarray)):
        return False
    pyfilename = __package__
    if (pyfilename == "__main__"):
        pyfilename = os.path.splitext(os.path.basename(__file__))[0]
    pystring = ("#!/usr/bin/env python\n" \
           "# -*- coding: utf-8 -*-\n\n" \
           "from __future__ import absolute_import, division, print_function, unicode_literals, generators, with_statement, nested_scopes\n" \
           "import " + pyfilename + ", sys, logging\n\n" \
           "# Python 2 handling: Reload sys and set UTF-8 encoding if applicable\n" \
           "try:\n" \
           "    reload(sys)  # Only relevant for Python 2\n" \
           "    if hasattr(sys, 'setdefaultencoding'):\n" \
           "        sys.setdefaultencoding('UTF-8')\n" \
           "except (NameError, AttributeError):\n" \
           "    pass\n\n" \
           "# Python 3 handling: Ensure stdout and stderr use UTF-8 encoding\n" \
           "if hasattr(sys.stdout, 'detach'):\n" \
           "    import io\n" \
           "    sys.stdout = io.TextIOWrapper(\n" \
           "        sys.stdout.detach(), encoding='UTF-8', errors='replace')\n" \
           "if hasattr(sys.stderr, 'detach'):\n" \
           "    import io\n" \
           "    sys.stderr = io.TextIOWrapper(\n" \
           "        sys.stderr.detach(), encoding='UTF-8', errors='replace')\n\n" \
           "logging.basicConfig(format=\"%(message)s\", stream=sys.stdout, level=logging.INFO)\n\n" \
           + "hockeyarray = " + pyfilename \
           + ".MakeHockeyArray(\""+inhockeyarray['database']+"\")\n")
    for hlkey in inhockeyarray['leaguelist']:
        HockeyLeagueHasConferences = True
        if (inhockeyarray[hlkey]['leagueinfo']['conferences'].lower() == "no"):
            HockeyLeagueHasConferences = False
        HockeyLeagueHasDivisions = True
        if (inhockeyarray[hlkey]['leagueinfo']['divisions'].lower() == "no"):
            HockeyLeagueHasDivisions = False
        pystring = pystring+"hockeyarray.AddHockeyLeague(\""+hlkey+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullname']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['country']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['fullcountry'] + \
            "\", \""+inhockeyarray[hlkey]['leagueinfo']['date']+"\", \""+inhockeyarray[hlkey]['leagueinfo']['playofffmt']+"\", \"" + \
            inhockeyarray[hlkey]['leagueinfo']['ordertype']+"\", " + \
            str(HockeyLeagueHasConferences)+", " + \
            str(HockeyLeagueHasDivisions)+")\n"
        conferencecount = 0
        conferenceend = len(inhockeyarray[hlkey]['conferencelist'])
        for hckey in inhockeyarray[hlkey]['conferencelist']:
            pystring = pystring+"hockeyarray.AddHockeyConference(\""+hlkey+"\", \""+hckey+"\", \""+inhockeyarray[
                hlkey][hckey]['conferenceinfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey]['conferenceinfo']['suffix']+"\")\n"
            for hdkey in inhockeyarray[hlkey][hckey]['divisionlist']:
                pystring = pystring+"hockeyarray.AddHockeyDivision(\""+hlkey+"\", \""+hdkey+"\", \""+hckey+"\", \""+inhockeyarray[
                    hlkey][hckey][hdkey]['divisioninfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey]['divisioninfo']['suffix']+"\")\n"
                for htkey in inhockeyarray[hlkey][hckey][hdkey]['teamlist']:
                    pystring = pystring+"hockeyarray.AddHockeyTeam(\""+hlkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['city']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['area']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['country']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['fullcountry']+"\", \""+inhockeyarray[hlkey][
                        hckey][hdkey][htkey]['teaminfo']['fullarea']+"\", \""+htkey+"\", \""+hckey+"\", \""+hdkey+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['arena']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['prefix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['suffix']+"\", \""+inhockeyarray[hlkey][hckey][hdkey][htkey]['teaminfo']['affiliates']+"\")\n"
            conferencecount = conferencecount + 1
        if (conferencecount >= conferenceend):
            hasarenas = False
            if (len(inhockeyarray[hlkey]['arenas']) > 0):
                hasarenas = True
            for hakey in inhockeyarray[hlkey]['arenas']:
                if (hakey):
                    hasarenas = True
                    pystring = pystring+"hockeyarray.AddHockeyArena(\""+hlkey+"\", \""+hakey['city']+"\", \""+hakey['area']+"\", \""+hakey[
                        'country']+"\", \""+hakey['fullcountry']+"\", \""+hakey['fullarea']+"\", \""+hakey['name']+"\")\n"
            hasgames = False
            if (len(inhockeyarray[hlkey]['games']) > 0):
                hasgames = True
            for hgkey in inhockeyarray[hlkey]['games']:
                if (hgkey):
                    hasgames = True
                    pystring = pystring+"hockeyarray.AddHockeyGame(\""+hlkey+"\", "+hgkey['date']+", "+hgkey['time']+", \""+hgkey['hometeam']+"\", \""+hgkey['awayteam']+"\", \""+hgkey['goals']+"\", \""+hgkey['sogs']+"\", \""+hgkey[
                        'ppgs']+"\", \""+hgkey['shgs']+"\", \""+hgkey['penalties']+"\", \""+hgkey['pims']+"\", \""+hgkey['hits']+"\", \""+hgkey['takeaways']+"\", \""+hgkey['faceoffwins']+"\", \""+hgkey['atarena']+"\", \""+hgkey['isplayoffgame']+"\")\n"
    pystring = pystring+"\n"
    if (verbosepy):
        pyverbose = "True"
    elif (not verbosepy):
        pyverbose = "False"
    else:
        pyverbose = "False"
    pystring = pystring + \
        "hockeyarray.MakeHockeyDatabase(None, False, " + \
        str(pyverbose)+", \""+str(verbosetype)+"\")\n"
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose):
        VerbosePrintOut(inhockeyarray)
    return pystring


def MakeHockeyPythonOOPAltFileFromHockeyArray(inhockeyarray, outpyfile=None, returnpy=False, encoding="UTF-8", verbose=False, verbosetype="array", verbosepy=True):
    if (outpyfile is None):
        return False
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outpyfile))):
        pyfp = BytesIO()
    else:
        pyfp = CompressOpenFile(outpyfile)
    pystring = MakeHockeyPythonOOPAltFromHockeyArray(
        inhockeyarray, verbose, verbosetype, verbosepy)
    try:
        pyfp.write(pystring)
    except TypeError:
        pyfp.write(pystring.encode(encoding))
    try:
        pyfp.flush()
        os.fsync(pyfp.fileno())
    except io.UnsupportedOperation:
        pass
    except AttributeError:
        pass
    except OSError as e:
        pass
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outpyfile))):
        pyfp.seek(0, 0)
        upload_file_to_internet_file(pyfp, outpyfile)
        pyfp.close()
    pyfp.close()
    if (fextname not in outextlistwd):
        os.chmod(outpyfile, 0o755)
    if (returnpy):
        return pystring
    if (not returnpy):
        return True
    return True


def MakeHockeyArrayFromHockeyDatabase(insdbfile, verbose=False, verbosetype="array"):
    if (isinstance(insdbfile, basestring) and (os.path.exists(insdbfile) and os.path.isfile(insdbfile))):
        if (not CheckHockeySQLiteDatabase(insdbfile)[0]):
            return False
        sqldatacon = OpenHockeyDatabase(insdbfile)
    else:
        if (insdbfile is not None and isinstance(insdbfile, (tuple, list))):
            sqldatacon = tuple(insdbfile)
            insdbfile = GetHockeyDatabaseFileName(sqldatacon)
        else:
            return False
    if (not CheckHockeySQLiteDatabaseConnection(sqldatacon)):
        return False
    leaguecur = sqldatacon[1].cursor()
    getleague_num = leaguecur.execute(
        "SELECT COUNT(*) FROM HockeyLeagues").fetchone()[0]
    getleague = leaguecur.execute(
        "SELECT LeagueName, LeagueFullName, CountryName, FullCountryName, Date, PlayOffFMT, OrderType, NumberOfConferences, NumberOfDivisions FROM HockeyLeagues")
    leaguearrayout = {'database': str(insdbfile)}
    leaguelist = []
    for leagueinfo in getleague:
        leaguearray = {}
        arenalist = []
        gamelist = []
        HockeyLeagueHasConferences = True
        HockeyLeagueHasConferenceStr = "yes"
        if (int(leagueinfo[7]) <= 0):
            HockeyLeagueHasConferences = False
            HockeyLeagueHasConferenceStr = "no"
        HockeyLeagueHasDivisions = True
        HockeyLeagueHasDivisionStr = "yes"
        if (int(leagueinfo[8]) <= 0):
            HockeyLeagueHasDivisions = False
            HockeyLeagueHasDivisionStr = "no"
        tempdict = {'leagueinfo': {'name': str(leagueinfo[0]), 'fullname': str(leagueinfo[1]), 'country': str(leagueinfo[2]), 'fullcountry': str(leagueinfo[3]), 'date': str(leagueinfo[4]), 'playofffmt': str(
            leagueinfo[5]), 'ordertype': str(leagueinfo[6]), 'conferences': str(HockeyLeagueHasConferenceStr), 'divisions': str(HockeyLeagueHasDivisionStr)}, 'quickinfo': {'conferenceinfo': {}, 'divisioninfo': {}, 'teaminfo': {}}}
        leaguearray.update({str(leagueinfo[0]): tempdict})
        leaguelist.append(str(leagueinfo[0]))
        conferencecur = sqldatacon[1].cursor()
        getconference_num = conferencecur.execute(
            "SELECT COUNT(*) FROM "+leagueinfo[0]+"Conferences WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\"").fetchone()[0]
        getconference = conferencecur.execute("SELECT Conference, ConferencePrefix, ConferenceSuffix, FullName FROM " +
                                              leagueinfo[0]+"Conferences WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\"")
        conferencelist = []
        for conferenceinfo in getconference:
            leaguearray[str(leagueinfo[0])].update({str(conferenceinfo[0]): {'conferenceinfo': {'name': str(conferenceinfo[0]), 'prefix': str(
                conferenceinfo[1]), 'suffix': str(conferenceinfo[2]), 'fullname': str(conferenceinfo[3]), 'league': str(leagueinfo[0])}}})
            leaguearray[str(leagueinfo[0])]['quickinfo']['conferenceinfo'].update({str(conferenceinfo[0]): {
                'name': str(conferenceinfo[0]), 'fullname': str(conferenceinfo[3]), 'league': str(leagueinfo[0])}})
            conferencelist.append(str(conferenceinfo[0]))
            divisioncur = sqldatacon[1].cursor()
            getdivision_num = divisioncur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Divisions WHERE LeagueName=\"" +
                                                  leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\"").fetchone()[0]
            getdivision = divisioncur.execute("SELECT Division, DivisionPrefix, DivisionSuffix, FullName FROM " +
                                              leagueinfo[0]+"Divisions WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\"")
            divisionlist = []
            for divisioninfo in getdivision:
                leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update({str(divisioninfo[0]): {'divisioninfo': {'name': str(divisioninfo[0]), 'prefix': str(
                    divisioninfo[1]), 'suffix': str(divisioninfo[2]), 'fullname': str(divisioninfo[3]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0])}}})
                leaguearray[str(leagueinfo[0])]['quickinfo']['divisioninfo'].update({str(divisioninfo[0]): {'name': str(
                    divisioninfo[0]), 'fullname': str(divisioninfo[3]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0])}})
                divisionlist.append(str(divisioninfo[0]))
                teamcur = sqldatacon[1].cursor()
                getteam_num = teamcur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Teams WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\"" +
                                              leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"").fetchone()[0]
                getteam = teamcur.execute("SELECT CityName, AreaName, FullAreaName, CountryName, FullCountryName, TeamName, ArenaName, TeamPrefix, TeamSuffix, Affiliates FROM " +
                                          leagueinfo[0]+"Teams WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"")
                teamlist = []
                for teaminfo in getteam:
                    fullteamname = GetFullTeamName(
                        str(teaminfo[5]), str(teaminfo[7]), str(teaminfo[8]))
                    leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(divisioninfo[0])].update({str(teaminfo[5]): {'teaminfo': {'city': str(teaminfo[0]), 'area': str(teaminfo[1]), 'fullarea': str(teaminfo[2]), 'country': str(teaminfo[3]), 'fullcountry': str(teaminfo[4]), 'name': str(
                        teaminfo[5]), 'fullname': fullteamname, 'arena': str(teaminfo[6]), 'prefix': str(teaminfo[7]), 'suffix': str(teaminfo[8]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0]), 'affiliates': str(teaminfo[9])}}})
                    leaguearray[str(leagueinfo[0])]['quickinfo']['teaminfo'].update({str(teaminfo[5]): {'name': str(
                        teaminfo[5]), 'fullname': fullteamname, 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0])}})
                    teamlist.append(str(teaminfo[5]))
                teamcur.close()
                leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(
                    divisioninfo[0])].update({'teamlist': teamlist})
            divisioncur.close()
            leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update(
                {'divisionlist': divisionlist})
        conferencecur.close()
        leaguearray[str(leagueinfo[0])].update(
            {'conferencelist': conferencelist})
        arenacur = sqldatacon[1].cursor()
        getteam_num = arenacur.execute(
            "SELECT COUNT(*) FROM "+leagueinfo[0]+"Arenas WHERE TeamID=0").fetchone()[0]
        getarena = arenacur.execute(
            "SELECT CityName, AreaName, FullAreaName, CountryName, FullCountryName, ArenaName FROM "+leagueinfo[0]+"Arenas WHERE TeamID=0")
        if (getteam_num > 0):
            for arenainfo in getarena:
                arenalist.append({'city': str(arenainfo[0]), 'area': str(arenainfo[1]), 'fullarea': str(
                    arenainfo[2]), 'country': str(arenainfo[3]), 'fullcountry': str(arenainfo[4]), 'name': str(arenainfo[5])})
        leaguearray[str(leagueinfo[0])].update({"arenas": arenalist})
        gamecur = sqldatacon[1].cursor()
        getgame_num = gamecur.execute(
            "SELECT COUNT(*) FROM "+leagueinfo[0]+"Games").fetchone()[0]
        getgame = gamecur.execute(
            "SELECT Date, Time, HomeTeam, AwayTeam, TeamScorePeriods, ShotsOnGoal, PowerPlays, ShortHanded, Penalties, PenaltyMinutes, HitsPerPeriod, TakeAways, FaceoffWins, AtArena, IsPlayOffGame FROM "+leagueinfo[0]+"Games")
        if (getgame_num > 0):
            for gameinfo in getgame:
                AtArena = gameinfo[13]
                if (GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[2]), "FullArenaName", "str") == AtArena):
                    AtArena = "0"
                if (GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[3]), "FullArenaName", "str") == AtArena):
                    AtArena = "1"
                gamelist.append({'date': str(gameinfo[0]), 'time': str(gameinfo[1]), 'hometeam': str(gameinfo[2]), 'awayteam': str(gameinfo[3]), 'goals': str(gameinfo[4]), 'sogs': str(gameinfo[5]), 'ppgs': str(gameinfo[6]), 'shgs': str(
                    gameinfo[7]), 'penalties': str(gameinfo[8]), 'pims': str(gameinfo[9]), 'hits': str(gameinfo[10]), 'takeaways': str(gameinfo[11]), 'faceoffwins': str(gameinfo[12]), 'atarena': str(AtArena), 'isplayoffgame': str(gameinfo[14])})
        leaguearray[str(leagueinfo[0])].update({"games": gamelist})
        leaguearrayout.update(leaguearray)
    leaguearrayout.update({'leaguelist': leaguelist})
    leaguecur.close()
    sqldatacon[1].close()
    if (not CheckHockeyArray(leaguearrayout)):
        return False
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose):
        VerbosePrintOut(leaguearrayout)
    return leaguearrayout


def MakeHockeyArrayFromHockeySQL(insqlfile, insdbfile=None, sqlisfile=True, encoding="UTF-8", verbose=False, verbosetype="array"):
    if (sqlisfile and (os.path.exists(insqlfile) and os.path.isfile(insqlfile))):
        sqlfp = UncompressFile(insqlfile)
        sqlstring = sqlfp.read()
        sqlfp.close()
    elif (not sqlisfile):
        sqlfp = BytesIO(insqlfile)
        sqlfp = UncompressFile(sqlfp)
        sqlstring = sqlfp.read()
        sqlfp.close()
    else:
        return False
    if (insdbfile is None and len(re.findall("Database\\:([\\w\\W]+)", insqlfile)) >= 1):
        insdbfile = re.findall("Database\\:([\\w\\W]+)", insqlfile)[0].strip()
    if (insdbfile is None and len(re.findall("Database\\:([\\w\\W]+)", insqlfile)) < 1):
        file_wo_extension, file_extension = os.path.splitext(insqlfile)
        insdbfile = file_wo_extension+".db3"
    sqldatacon = MakeHockeyDatabase(":memory:")
    if (CheckHockeySQLiteDatabaseConnection(sqldatacon)):
     sqldatacon[0].execute('BEGIN TRANSACTION')
    elif (not CheckHockeySQLiteDatabaseConnection(sqldatacon)):
        return False
    try:
        sqldatacon[0].executescript(sqlstring)
    except ValueError:
        sqldatacon[0].executescript(sqlstring.decode(encoding))
    sqldatacon[1].commit()
    leaguecur = sqldatacon[1].cursor()
    getleague_num = leaguecur.execute(
        "SELECT COUNT(*) FROM HockeyLeagues").fetchone()[0]
    getleague = leaguecur.execute(
        "SELECT LeagueName, LeagueFullName, CountryName, FullCountryName, Date, PlayOffFMT, OrderType, NumberOfConferences, NumberOfDivisions FROM HockeyLeagues")
    leaguearrayout = {'database': str(insdbfile)}
    leaguelist = []
    for leagueinfo in getleague:
        leaguearray = {}
        arenalist = []
        gamelist = []
        HockeyLeagueHasConferences = True
        HockeyLeagueHasConferenceStr = "yes"
        if (int(leagueinfo[7]) <= 0):
            HockeyLeagueHasConferences = False
            HockeyLeagueHasConferenceStr = "no"
        HockeyLeagueHasDivisions = True
        HockeyLeagueHasDivisionStr = "yes"
        if (int(leagueinfo[8]) <= 0):
            HockeyLeagueHasDivisions = False
            HockeyLeagueHasDivisionStr = "no"
        tempdict = {'leagueinfo': {'name': str(leagueinfo[0]), 'fullname': str(leagueinfo[1]), 'country': str(leagueinfo[2]), 'fullcountry': str(leagueinfo[3]), 'date': str(leagueinfo[4]), 'playofffmt': str(
            leagueinfo[5]), 'ordertype': str(leagueinfo[6]), 'conferences': str(HockeyLeagueHasConferenceStr), 'divisions': str(HockeyLeagueHasDivisionStr)}, 'quickinfo': {'conferenceinfo': {}, 'divisioninfo': {}, 'teaminfo': {}}}
        leaguearray.update({str(leagueinfo[0]): tempdict})
        leaguelist.append(str(leagueinfo[0]))
        conferencecur = sqldatacon[1].cursor()
        getconference_num = conferencecur.execute(
            "SELECT COUNT(*) FROM "+leagueinfo[0]+"Conferences WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\"").fetchone()[0]
        getconference = conferencecur.execute("SELECT Conference, ConferencePrefix, ConferenceSuffix, FullName FROM " +
                                              leagueinfo[0]+"Conferences WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\"")
        conferencelist = []
        for conferenceinfo in getconference:
            leaguearray[str(leagueinfo[0])].update({str(conferenceinfo[0]): {'conferenceinfo': {'name': str(conferenceinfo[0]), 'prefix': str(
                conferenceinfo[1]), 'suffix': str(conferenceinfo[2]), 'fullname': str(conferenceinfo[3]), 'league': str(leagueinfo[0])}}})
            leaguearray[str(leagueinfo[0])]['quickinfo']['conferenceinfo'].update({str(conferenceinfo[0]): {
                'name': str(conferenceinfo[0]), 'fullname': str(conferenceinfo[3]), 'league': str(leagueinfo[0])}})
            conferencelist.append(str(conferenceinfo[0]))
            divisioncur = sqldatacon[1].cursor()
            getdivision_num = divisioncur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Divisions WHERE LeagueName=\"" +
                                                  leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\"").fetchone()[0]
            getdivision = divisioncur.execute("SELECT Division, DivisionPrefix, DivisionSuffix, FullName FROM " +
                                              leagueinfo[0]+"Divisions WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\"")
            divisionlist = []
            for divisioninfo in getdivision:
                leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update({str(divisioninfo[0]): {'divisioninfo': {'name': str(divisioninfo[0]), 'prefix': str(
                    divisioninfo[1]), 'suffix': str(divisioninfo[2]), 'fullname': str(divisioninfo[3]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0])}}})
                leaguearray[str(leagueinfo[0])]['quickinfo']['divisioninfo'].update({str(divisioninfo[0]): {'name': str(
                    divisioninfo[0]), 'fullname': str(divisioninfo[3]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0])}})
                divisionlist.append(str(divisioninfo[0]))
                teamcur = sqldatacon[1].cursor()
                getteam_num = teamcur.execute("SELECT COUNT(*) FROM "+leagueinfo[0]+"Teams WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\"" +
                                              leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"").fetchone()[0]
                getteam = teamcur.execute("SELECT CityName, AreaName, FullAreaName, CountryName, FullCountryName, TeamName, ArenaName, TeamPrefix, TeamSuffix, Affiliates FROM " +
                                          leagueinfo[0]+"Teams WHERE LeagueName=\""+leagueinfo[0]+"\" AND LeagueFullName=\""+leagueinfo[1]+"\" AND Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"")
                teamlist = []
                for teaminfo in getteam:
                    fullteamname = GetFullTeamName(
                        str(teaminfo[5]), str(teaminfo[7]), str(teaminfo[8]))
                    leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(divisioninfo[0])].update({str(teaminfo[5]): {'teaminfo': {'city': str(teaminfo[0]), 'area': str(teaminfo[1]), 'fullarea': str(teaminfo[2]), 'country': str(teaminfo[3]), 'fullcountry': str(teaminfo[4]), 'name': str(
                        teaminfo[5]), 'fullname': fullteamname, 'arena': str(teaminfo[6]), 'prefix': str(teaminfo[7]), 'suffix': str(teaminfo[8]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0]), 'affiliates': str(teaminfo[9])}}})
                    leaguearray[str(leagueinfo[0])]['quickinfo']['teaminfo'].update({str(teaminfo[5]): {'name': str(
                        teaminfo[5]), 'fullname': fullteamname, 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0])}})
                    teamlist.append(str(teaminfo[5]))
                teamcur.close()
                leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(
                    divisioninfo[0])].update({'teamlist': teamlist})
            divisioncur.close()
            leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update(
                {'divisionlist': divisionlist})
        conferencecur.close()
        leaguearray[str(leagueinfo[0])].update(
            {'conferencelist': conferencelist})
        arenacur = sqldatacon[1].cursor()
        getteam_num = arenacur.execute(
            "SELECT COUNT(*) FROM "+leagueinfo[0]+"Arenas WHERE TeamID=0").fetchone()[0]
        getarena = arenacur.execute(
            "SELECT CityName, AreaName, FullAreaName, CountryName, FullCountryName, ArenaName FROM "+leagueinfo[0]+"Arenas WHERE TeamID=0")
        if (getteam_num > 0):
            for arenainfo in getarena:
                arenalist.append({'city': str(arenainfo[0]), 'area': str(arenainfo[1]), 'fullarea': str(
                    arenainfo[2]), 'country': str(arenainfo[3]), 'fullcountry': str(arenainfo[4]), 'name': str(arenainfo[5])})
        leaguearray[str(leagueinfo[0])].update({"arenas": arenalist})
        gamecur = sqldatacon[1].cursor()
        getgame_num = gamecur.execute(
            "SELECT COUNT(*) FROM "+leagueinfo[0]+"Games").fetchone()[0]
        getgame = gamecur.execute(
            "SELECT Date, Time, HomeTeam, AwayTeam, TeamScorePeriods, ShotsOnGoal, PowerPlays, ShortHanded, Penalties, PenaltyMinutes, HitsPerPeriod, TakeAways, FaceoffWins, AtArena, IsPlayOffGame FROM "+leagueinfo[0]+"Games")
        if (getgame_num > 0):
            for gameinfo in getgame:
                AtArena = gameinfo[13]
                if (GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[2]), "FullArenaName", "str") == AtArena):
                    AtArena = "0"
                if (GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[3]), "FullArenaName", "str") == AtArena):
                    AtArena = "1"
                gamelist.append({'date': str(gameinfo[0]), 'time': str(gameinfo[1]), 'hometeam': str(gameinfo[2]), 'awayteam': str(gameinfo[3]), 'goals': str(gameinfo[4]), 'sogs': str(gameinfo[5]), 'ppgs': str(gameinfo[6]), 'shgs': str(
                    gameinfo[7]), 'penalties': str(gameinfo[8]), 'pims': str(gameinfo[9]), 'hits': str(gameinfo[10]), 'takeaways': str(gameinfo[11]), 'faceoffwins': str(gameinfo[12]), 'atarena': str(AtArena), 'isplayoffgame': str(gameinfo[14])})
        leaguearray[str(leagueinfo[0])].update({"games": gamelist})
        leaguearrayout.update(leaguearray)
    leaguearrayout.update({'leaguelist': leaguelist})
    leaguecur.close()
    sqldatacon[1].close()
    if (not CheckHockeyArray(leaguearrayout)):
        return False
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose):
        VerbosePrintOut(leaguearrayout)
    return leaguearrayout


def MakeHockeySQLFromHockeyArray(inhockeyarray, insdbfile=":memory:", verbose=False, verbosetype="array"):
    if (not CheckHockeyArray(inhockeyarray)):
        return False
    if (insdbfile is None):
        insdbfile = GetHockeyDatabaseFileName(sqldatacon)
    sqldatacon = MakeHockeyDatabaseFromHockeyArray(
        inhockeyarray, ":memory:", True, False, False)
    if (not CheckHockeySQLiteDatabaseConnection(sqldatacon)):
        return False
    sqldump = "-- "+__program_name__+" SQL Dumper\n"
    sqldump = sqldump+"-- version "+__version__+"\n"
    sqldump = sqldump+"-- "+__project_url__+"\n"
    sqldump = sqldump+"--\n"
    sqldump = sqldump+"-- Generation Time: " + \
        time.strftime("%B %d, %Y at %I:%M %p", time.localtime())+"\n"
    sqldump = sqldump+"-- SQLite Server version: "+sqlite3.sqlite_version+"\n"
    sqldump = sqldump+"-- PySQLite version: "+sqlite3.version+"\n"
    sqldump = sqldump+"-- Python Version: " + \
        str(sys.version_info[0])+"."+str(sys.version_info[1]
                                         )+"."+str(sys.version_info[2])+"\n"
    sqldump = sqldump+"--\n"
    sqldump = sqldump+"-- Database: "+insdbfile+"\n"
    sqldump = sqldump+"--\n\n"
    sqldump = sqldump+"-- --------------------------------------------------------\n\n"
    # all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games", "PlayoffTeams"]
    all_table_list = ["Conferences", "Divisions",
                      "Arenas", "Teams", "Stats", "GameStats", "Games"]
    table_list = ['HockeyLeagues']
    getleague_tmp = sqldatacon[0].execute(
        "SELECT LeagueName FROM HockeyLeagues")
    for leagueinfo_tmp in getleague_tmp:
        for cur_tab in all_table_list:
            table_list.append(leagueinfo_tmp[0]+cur_tab)
    for get_cur_tab in table_list:
        tresult = sqldatacon[0].execute("SELECT * FROM "+get_cur_tab)
        tmbcor = sqldatacon[1].cursor()
        tabresult = tmbcor.execute(
            "SELECT * FROM sqlite_master WHERE type=\"table\" and tbl_name=\""+get_cur_tab+"\";").fetchone()[4]
        tabresultcol = list(map(lambda x: x[0], sqldatacon[0].description))
        tresult_list = []
        sqldump = sqldump+"--\n"
        sqldump = sqldump+"-- Table structure for table "+str(get_cur_tab)+"\n"
        sqldump = sqldump+"--\n\n"
        sqldump = sqldump+"DROP TABLE IF EXISTS "+get_cur_tab+";\n\n"+tabresult+";\n\n"
        sqldump = sqldump+"--\n"
        sqldump = sqldump+"-- Dumping data for table "+str(get_cur_tab)+"\n"
        sqldump = sqldump+"--\n\n"
        get_insert_stmt_full = ""
        for tresult_tmp in tresult:
            get_insert_stmt = "INSERT INTO "+str(get_cur_tab)+" ("
            get_insert_stmt_val = "("
            for result_cal_val in tabresultcol:
                get_insert_stmt += str(result_cal_val)+", "
            for result_val in tresult_tmp:
                if (isinstance(result_val, basestring)):
                    get_insert_stmt_val += "\""+str(result_val)+"\", "
                if (isinstance(result_val, baseint)):
                    get_insert_stmt_val += ""+str(result_val)+", "
                if (isinstance(result_val, float)):
                    get_insert_stmt_val += ""+str(result_val)+", "
            get_insert_stmt = get_insert_stmt[:-2]+") VALUES \n"
            get_insert_stmt_val = get_insert_stmt_val[:-2]+");"
            get_insert_stmt_full += str(get_insert_stmt +
                                        get_insert_stmt_val)+"\n"
        sqldump = sqldump+get_insert_stmt_full + \
            "\n-- --------------------------------------------------------\n\n"
    CloseHockeyDatabase(sqldatacon)
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose):
        VerbosePrintOut(leaguearrayout)
    return sqldump


def MakeHockeySQLFileFromHockeyArray(inhockeyarray, outsqlfile=None, returnsql=False, encoding="UTF-8", verbose=False, verbosetype="array"):
    if (outsqlfile is None):
        return False
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outsqlfile))):
        sqlfp = BytesIO()
    else:
        sqlfp = CompressOpenFile(outsqlfile)
    sqlstring = MakeHockeySQLFromHockeyArray(
        inhockeyarray, os.path.splitext(outsqlfile)[0]+".db3", verbose, verbosetype)
    try:
        sqlfp.write(sqlstring)
    except TypeError:
        sqlfp.write(sqlstring.encode(encoding))
    try:
        sqlfp.flush()
        os.fsync(sqlfp.fileno())
    except io.UnsupportedOperation:
        pass
    except AttributeError:
        pass
    except OSError as e:
        pass
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outsqlfile))):
        sqlfp.seek(0, 0)
        upload_file_to_internet_file(sqlfp, outsqlfile)
        sqlfp.close()
    sqlfp.close()
    if (returnsql):
        return sqlstring
    if (not returnsql):
        return True
    return True


def MakeHockeySQLFromHockeyDatabase(insdbfile, verbose=False, verbosetype="array"):
    if (os.path.exists(insdbfile) and os.path.isfile(insdbfile) and isinstance(insdbfile, basestring)):
        sqldatacon = OpenHockeyDatabase(insdbfile)
    else:
        if (insdbfile is not None and isinstance(insdbfile, (tuple, list))):
            sqldatacon = tuple(insdbfile)
            insdbfile = GetHockeyDatabaseFileName(sqldatacon)
        else:
            return False
    if (not hasattr(sqldatacon[0], "execute")):
        return False
    if (not hasattr(sqldatacon[1], "execute")):
        return False
    sqldump = "-- "+__program_name__+" SQL Dumper\n"
    sqldump = sqldump+"-- version "+__version__+"\n"
    sqldump = sqldump+"-- "+__project_url__+"\n"
    sqldump = sqldump+"--\n"
    sqldump = sqldump+"-- Generation Time: " + \
        time.strftime("%B %d, %Y at %I:%M %p", time.localtime())+"\n"
    sqldump = sqldump+"-- SQLite Server version: "+sqlite3.sqlite_version+"\n"
    sqldump = sqldump+"-- PySQLite version: "+sqlite3.version+"\n"
    sqldump = sqldump+"-- Python Version: " + \
        str(sys.version_info[0])+"."+str(sys.version_info[1]
                                         )+"."+str(sys.version_info[2])+"\n\n"
    sqldump = sqldump+"--\n"
    sqldump = sqldump+"-- Database: "+insdbfile+"\n"
    sqldump = sqldump+"--\n\n"
    sqldump = sqldump+"-- --------------------------------------------------------\n\n"
    # all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games", "PlayoffTeams"]
    all_table_list = ["Conferences", "Divisions",
                      "Arenas", "Teams", "Stats", "GameStats", "Games"]
    table_list = ['HockeyLeagues']
    getleague_num_tmp = sqldatacon[0].execute(
        "SELECT COUNT(*) FROM HockeyLeagues").fetchone()[0]
    getleague_tmp = sqldatacon[0].execute(
        "SELECT LeagueName FROM HockeyLeagues")
    for leagueinfo_tmp in getleague_tmp:
        for cur_tab in all_table_list:
            table_list.append(leagueinfo_tmp[0]+cur_tab)
    for get_cur_tab in table_list:
        tresult = sqldatacon[0].execute("SELECT * FROM "+get_cur_tab)
        tmbcor = sqldatacon[1].cursor()
        tabresult = tmbcor.execute(
            "SELECT * FROM sqlite_master WHERE type=\"table\" and tbl_name=\""+get_cur_tab+"\";").fetchone()[4]
        tabresultcol = list(map(lambda x: x[0], sqldatacon[0].description))
        tresult_list = []
        sqldump = sqldump+"--\n"
        sqldump = sqldump+"-- Table structure for table "+str(get_cur_tab)+"\n"
        sqldump = sqldump+"--\n\n"
        sqldump = sqldump+"DROP TABLE IF EXISTS "+get_cur_tab+";\n\n"+tabresult+";\n\n"
        sqldump = sqldump+"--\n"
        sqldump = sqldump+"-- Dumping data for table "+str(get_cur_tab)+"\n"
        sqldump = sqldump+"--\n\n"
        get_insert_stmt_full = ""
        for tresult_tmp in tresult:
            get_insert_stmt = "INSERT INTO "+str(get_cur_tab)+" ("
            get_insert_stmt_val = "("
            for result_cal_val in tabresultcol:
                get_insert_stmt += str(result_cal_val)+", "
            for result_val in tresult_tmp:
                if (isinstance(result_val, basestring)):
                    get_insert_stmt_val += "\""+str(result_val)+"\", "
                if (isinstance(result_val, baseint)):
                    get_insert_stmt_val += ""+str(result_val)+", "
                if (isinstance(result_val, float)):
                    get_insert_stmt_val += ""+str(result_val)+", "
            get_insert_stmt = get_insert_stmt[:-2]+") VALUES \n"
            get_insert_stmt_val = get_insert_stmt_val[:-2]+");"
            get_insert_stmt_full += str(get_insert_stmt +
                                        get_insert_stmt_val)+"\n"
        sqldump = sqldump+get_insert_stmt_full + \
            "\n-- --------------------------------------------------------\n\n"
    CloseHockeyDatabase(sqldatacon)
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(MakeHockeyArrayFromHockeyDatabase(
            insdbfile, verbose=False), verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(MakeHockeyArrayFromHockeyDatabase(
            insdbfile, verbose=False), verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(MakeHockeyArrayFromHockeyDatabase(
            insdbfile, verbose=False), verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(MakeHockeyArrayFromHockeyDatabase(
            insdbfile, verbose=False), verbose=False))
    elif (verbose):
        VerbosePrintOut(MakeHockeyArrayFromHockeyDatabase(
            insdbfile, verbose=False))
    return sqldump


def MakeHockeySQLFileFromHockeyDatabase(insdbfile, outsqlfile=None, returnsql=False, encoding="UTF-8", verbose=False, verbosetype="array"):
    if (not os.path.exists(insdbfile) or not os.path.isfile(insdbfile)):
        return False
    if (outsqlfile is None):
        file_wo_extension, file_extension = os.path.splitext(insdbfile)
        outsqlfile = file_wo_extension+".sql"
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outsqlfile))):
        sqlfp = BytesIO()
    else:
        sqlfp = CompressOpenFile(outsqlfile)
    sqlstring = MakeHockeySQLFromHockeyDatabase(
        insdbfile, verbose, verbosetype)
    try:
        sqlfp.write(sqlstring)
    except TypeError:
        sqlfp.write(sqlstring.encode(encoding))
    try:
        sqlfp.flush()
        os.fsync(sqlfp.fileno())
    except io.UnsupportedOperation:
        pass
    except AttributeError:
        pass
    except OSError as e:
        pass
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outsqlfile))):
        sqlfp.seek(0, 0)
        upload_file_to_internet_file(sqlfp, outsqlfile)
        sqlfp.close()
    sqlfp.close()
    if (returnsql):
        return sqlstring
    if (not returnsql):
        return True
    return True


def MakeHockeyArrayFromOldHockeyDatabase(insdbfile, verbose=False, verbosetype="array"):
    if (isinstance(insdbfile, basestring) and (os.path.exists(insdbfile) and os.path.isfile(insdbfile))):
        sqldatacon = OpenHockeyDatabase(insdbfile)
    else:
        if (insdbfile is not None and isinstance(insdbfile, (tuple, list))):
            sqldatacon = tuple(insdbfile)
            insdbfile = GetHockeyDatabaseFileName(sqldatacon)
        else:
            return False
    if (not CheckHockeySQLiteDatabaseConnection(sqldatacon)):
        return False
    leaguecur = sqldatacon[1].cursor()
    gettablecur = sqldatacon[1].cursor()
    gettable_num = gettablecur.execute(
        "SELECT COUNT(*) FROM sqlite_master WHERE type=\"table\" and name LIKE \"%Teams\"").fetchone()[0]
    gettable = gettablecur.execute(
        "SELECT name FROM sqlite_master WHERE type=\"table\" and name LIKE \"%Teams\"")
    mktemptablecur = sqldatacon[1].cursor()
    mktemptablecur.execute("CREATE TEMP TABLE HockeyLeagues (\n" +
                           "  id INTEGER PRIMARY KEY AUTOINCREMENT,\n" +
                           "  LeagueName TEXT NOT NULL DEFAULT '',\n" +
                           "  LeagueFullName TEXT NOT NULL DEFAULT '',\n" +
                           "  CountryName TEXT NOT NULL DEFAULT '',\n" +
                           "  FullCountryName TEXT NOT NULL DEFAULT '',\n" +
                           "  Date INTEGER NOT NULL DEFAULT 0,\n" +
                           "  PlayOffFMT TEXT NOT NULL DEFAULT '',\n" +
                           "  OrderType TEXT NOT NULL DEFAULT '',\n" +
                           "  NumberOfTeams INTEGER NOT NULL DEFAULT 0,\n" +
                           "  NumberOfConferences INTEGER NOT NULL DEFAULT 0,\n" +
                           "  NumberOfDivisions INTEGER NOT NULL DEFAULT ''\n" +
                           ");")
    for tableinfo in gettable:
        LeagueName = re.sub("Teams$", "", tableinfo[0])
        LeagueNameInfo = GetHockeyLeaguesInfo(LeagueName)
        getconference_num = mktemptablecur.execute(
            "SELECT COUNT(*) FROM "+LeagueName+"Conferences").fetchone()[0]
        getdivision_num = mktemptablecur.execute(
            "SELECT COUNT(*) FROM "+LeagueName+"Divisions").fetchone()[0]
        getteam_num = mktemptablecur.execute(
            "SELECT COUNT(*) FROM "+LeagueName+"Teams").fetchone()[0]
        getallteam_num = getteam_num
        mktemptablecur.execute("INSERT INTO HockeyLeagues (LeagueName, LeagueFullName, CountryName, FullCountryName, Date, PlayOffFMT, OrderType, NumberOfTeams, NumberOfConferences, NumberOfDivisions) VALUES \n" +
                               "(\""+str(LeagueNameInfo['LeagueName'])+"\", \""+str(LeagueNameInfo['FullLeagueName'])+"\", \""+str(LeagueNameInfo['CountryName'])+"\", \""+str(LeagueNameInfo['FullCountryName'])+"\", "+str(LeagueNameInfo['StartDate'])+", \""+str(LeagueNameInfo['PlayOffFMT'])+"\", \""+str(LeagueNameInfo['OrderType'])+"\", "+str(getteam_num)+", "+str(getconference_num)+", "+str(getdivision_num)+")")
    gettablecur.close()
    getleague_num = leaguecur.execute(
        "SELECT COUNT(*) FROM HockeyLeagues").fetchone()[0]
    getleague = leaguecur.execute(
        "SELECT LeagueName, LeagueFullName, CountryName, FullCountryName, Date, PlayOffFMT, OrderType, NumberOfTeams, NumberOfConferences, NumberOfDivisions FROM HockeyLeagues")
    leaguearrayout = {'database': str(insdbfile)}
    leaguelist = []
    for leagueinfo in getleague:
        leaguearray = {}
        arenalist = []
        gamelist = []
        HockeyLeagueHasConferences = True
        HockeyLeagueHasConferenceStr = "yes"
        if (int(leagueinfo[7]) <= 0):
            HockeyLeagueHasConferences = False
            HockeyLeagueHasConferenceStr = "no"
        HockeyLeagueHasDivisions = True
        HockeyLeagueHasDivisionStr = "yes"
        if (int(leagueinfo[8]) <= 0):
            HockeyLeagueHasDivisions = False
            HockeyLeagueHasDivisionStr = "no"
        tempdict = {'leagueinfo': {'name': str(leagueinfo[0]), 'fullname': str(leagueinfo[1]), 'country': str(leagueinfo[2]), 'fullcountry': str(leagueinfo[3]), 'date': str(leagueinfo[4]), 'playofffmt': str(
            leagueinfo[5]), 'ordertype': str(leagueinfo[6]), 'conferences': str(HockeyLeagueHasConferenceStr), 'divisions': str(HockeyLeagueHasDivisionStr)}, 'quickinfo': {'conferenceinfo': {}, 'divisioninfo': {}, 'teaminfo': {}}}
        leaguearray.update({str(leagueinfo[0]): tempdict})
        leaguelist.append(str(leagueinfo[0]))
        conferencecur = sqldatacon[1].cursor()
        getconference_num = conferencecur.execute(
            "SELECT COUNT(*) FROM "+leagueinfo[0]+"Conferences").fetchone()[0]
        getconference = conferencecur.execute(
            "SELECT Conference FROM "+leagueinfo[0]+"Conferences")
        conferencelist = []
        for conferenceinfo in getconference:
            leaguearray[str(leagueinfo[0])].update({str(conferenceinfo[0]): {'conferenceinfo': {
                'name': str(conferenceinfo[0]), 'league': str(leagueinfo[0])}}})
            leaguearray[str(leagueinfo[0])]['quickinfo']['conferenceinfo'].update(
                {str(conferenceinfo[0]): {'name': str(conferenceinfo[0]), 'league': str(leagueinfo[0])}})
            conferencelist.append(str(conferenceinfo[0]))
            divisioncur = sqldatacon[1].cursor()
            getdivision_num = divisioncur.execute(
                "SELECT COUNT(*) FROM "+leagueinfo[0]+"Divisions WHERE Conference=\""+conferenceinfo[0]+"\"").fetchone()[0]
            getdivision = divisioncur.execute(
                "SELECT Division FROM "+leagueinfo[0]+"Divisions WHERE Conference=\""+conferenceinfo[0]+"\"")
            divisionlist = []
            for divisioninfo in getdivision:
                leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update({str(divisioninfo[0]): {'divisioninfo': {
                    'name': str(divisioninfo[0]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0])}}})
                leaguearray[str(leagueinfo[0])]['quickinfo']['divisioninfo'].update({str(divisioninfo[0]): {
                    'name': str(divisioninfo[0]), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0])}})
                divisionlist.append(str(divisioninfo[0]))
                teamcur = sqldatacon[1].cursor()
                getteam_num = teamcur.execute(
                    "SELECT COUNT(*) FROM "+leagueinfo[0]+"Teams WHERE Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"").fetchone()[0]
                getteam = teamcur.execute("SELECT CityName, AreaName, TeamName, ArenaName, TeamPrefix, Affiliates FROM " +
                                          leagueinfo[0]+"Teams WHERE Conference=\""+conferenceinfo[0]+"\" AND Division=\""+divisioninfo[0]+"\"")
                teamlist = []
                for teaminfo in getteam:
                    TeamAreaInfo = GetAreaInfoFromUSCA(teaminfo[1])
                    fullteamname = GetFullTeamName(
                        str(teaminfo[2]), str(teaminfo[4]), "")
                    leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(divisioninfo[0])].update({str(teaminfo[2]): {'teaminfo': {'city': str(teaminfo[0]), 'area': str(TeamAreaInfo['AreaName']), 'fullarea': str(TeamAreaInfo['FullAreaName']), 'country': str(TeamAreaInfo['CountryName']), 'fullcountry': str(
                        TeamAreaInfo['FullCountryName']), 'name': str(teaminfo[2]), 'fullname': fullteamname, 'arena': str(teaminfo[3]), 'prefix': str(teaminfo[4]), 'suffix': "", 'affiliates': str(teaminfo[5].strip()), 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0])}}})
                    leaguearray[str(leagueinfo[0])]['quickinfo']['teaminfo'].update({str(teaminfo[2]): {'name': str(
                        teaminfo[2]), 'fullname': fullteamname, 'league': str(leagueinfo[0]), 'conference': str(conferenceinfo[0]), 'division': str(divisioninfo[0])}})
                    teamlist.append(str(teaminfo[2]))
                teamcur.close()
                leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])][str(
                    divisioninfo[0])].update({'teamlist': teamlist})
            divisioncur.close()
            leaguearray[str(leagueinfo[0])][str(conferenceinfo[0])].update(
                {'divisionlist': divisionlist})
        conferencecur.close()
        leaguearray[str(leagueinfo[0])].update(
            {'conferencelist': conferencelist})
        arenacur = sqldatacon[1].cursor()
        getteam_num = arenacur.execute(
            "SELECT COUNT(*) FROM "+leagueinfo[0]+"Arenas WHERE id>"+str(getallteam_num)).fetchone()[0]
        getarena = arenacur.execute(
            "SELECT CityName, AreaName, ArenaName FROM "+leagueinfo[0]+"Arenas WHERE id>"+str(getallteam_num))
        if (getteam_num > 0):
            for arenainfo in getarena:
                ArenaAreaInfo = GetAreaInfoFromUSCA(arenainfo[1])
                arenalist.append({'city': str(arenainfo[0]), 'area': str(ArenaAreaInfo['AreaName']), 'fullarea': str(ArenaAreaInfo['FullAreaName']), 'country': str(
                    ArenaAreaInfo['CountryName']), 'fullcountry': str(ArenaAreaInfo['FullCountryName']), 'name': str(arenainfo[2])})
        leaguearray[str(leagueinfo[0])].update({"arenas": arenalist})
        gamecur = sqldatacon[1].cursor()
        getgame_num = gamecur.execute(
            "SELECT COUNT(*) FROM "+leagueinfo[0]+"Games").fetchone()[0]
        getgame = gamecur.execute(
            "SELECT Date, HomeTeam, AwayTeam, TeamScorePeriods, ShotsOnGoal, AtArena, IsPlayOffGame FROM "+leagueinfo[0]+"Games")
        if (getgame_num > 0):
            for gameinfo in getgame:
                GetNumPeriods = len(gameinfo[3].split(","))
                EmptyScore = ",0:0" * (GetNumPeriods - 1)
                EmptyScore = "0:0"+EmptyScore
                AtArena = gameinfo[5]
                if (GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[1]), "FullArenaName", "str") == AtArena):
                    AtArena = "0"
                if (GetTeamData(sqldatacon, leagueinfo[0], GetTeam2Num(sqldatacon, leagueinfo[0], gameinfo[2]), "FullArenaName", "str") == AtArena):
                    AtArena = "1"
                gamelist.append({'date': str(gameinfo[0]), 'time': "0000", 'hometeam': str(gameinfo[1]), 'awayteam': str(gameinfo[2]), 'goals': str(gameinfo[3]), 'sogs': str(gameinfo[4]), 'ppgs': str(EmptyScore), 'shgs': str(
                    EmptyScore), 'penalties': str(EmptyScore), 'pims': str(EmptyScore), 'hits': str(EmptyScore), 'takeaways': str(EmptyScore), 'faceoffwins': str(EmptyScore), 'atarena': str(AtArena), 'isplayoffgame': str(gameinfo[6])})
        leaguearray[str(leagueinfo[0])].update({"games": gamelist})
        leaguearrayout.update(leaguearray)
    leaguearrayout.update({'leaguelist': leaguelist})
    leaguecur.close()
    CloseHockeyDatabase(sqldatacon)
    if (not CheckHockeyArray(leaguearrayout)):
        return False
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose):
        VerbosePrintOut(leaguearrayout)
    return leaguearrayout


def MakeHockeySQLiteArrayFromHockeyDatabase(insdbfile, verbose=False, verbosetype="array"):
    if (isinstance(insdbfile, basestring) and (os.path.exists(insdbfile) and os.path.isfile(insdbfile))):
        if (not CheckHockeySQLiteDatabase(insdbfile)[0]):
            return False
        sqldatacon = OpenHockeyDatabase(insdbfile)
    else:
        if (insdbfile is not None and isinstance(insdbfile, (tuple, list))):
            sqldatacon = tuple(insdbfile)
            insdbfile = GetHockeyDatabaseFileName(sqldatacon)
        else:
            return False
    if (not CheckHockeySQLiteDatabaseConnection(sqldatacon)):
        return False
    # all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games", "PlayoffTeams"]
    all_table_list = ["Conferences", "Divisions",
                      "Arenas", "Teams", "Stats", "GameStats", "Games"]
    table_list = ['HockeyLeagues']
    getleague_num_tmp = sqldatacon[0].execute(
        "SELECT COUNT(*) FROM HockeyLeagues").fetchone()[0]
    getleague_tmp = sqldatacon[0].execute(
        "SELECT LeagueName FROM HockeyLeagues")
    leaguearrayout = {'database': str(insdbfile)}
    for leagueinfo_tmp in getleague_tmp:
        for cur_tab in all_table_list:
            table_list.append(leagueinfo_tmp[0]+cur_tab)
    for get_cur_tab in table_list:
        gettableinfo = sqldatacon[0].execute(
            "PRAGMA table_xinfo("+get_cur_tab+");").fetchall()
        leaguearrayout.update({get_cur_tab: {}})
        collist = []
        sqlrowlist = []
        for tableinfo in gettableinfo:
            autoincrement = 0
            if (tableinfo[1] == "id" and tableinfo[5] == 1):
                autoincrement = 1
            leaguearrayout[get_cur_tab].update({tableinfo[1]: {'info': {'id': tableinfo[0], 'Name': tableinfo[1], 'Type': tableinfo[2], 'NotNull': tableinfo[3],
                                               'DefualtValue': tableinfo[4], 'PrimaryKey': tableinfo[5], 'AutoIncrement': autoincrement, 'Hidden': tableinfo[6]}}})
            sqlrowline = tableinfo[1]+" "+tableinfo[2]
            if (tableinfo[3] == 1):
                sqlrowline = sqlrowline+" NOT NULL"
            if (tableinfo[4] is not None):
                sqlrowline = sqlrowline+" "+tableinfo[4]
            if (tableinfo[5] == 1):
                sqlrowline = sqlrowline+" PRIMARY KEY"
            if (autoincrement == 1):
                sqlrowline = sqlrowline+" AUTOINCREMENT"
            sqlrowlist.append(sqlrowline)
            collist.append(tableinfo[1])
            gettabledata = sqldatacon[0].execute(
                "SELECT "+', '.join(collist)+" FROM "+get_cur_tab)
            subcollist = []
            rkeylist = []
            rvaluelist = []
            for tabledata in gettabledata:
                subcolarray = {}
                collen = len(tabledata)
                colleni = 0
                while (colleni < collen):
                    rkeylist.append(collist[colleni])
                    tabledataalt = tabledata[colleni]
                    if (isinstance(tabledata[colleni], basestring)):
                        tabledataalt = "\""+tabledata[colleni]+"\""
                    rvaluelist.append(str(tabledata[colleni]))
                    subcolarray.update({collist[colleni]: tabledata[colleni]})
                    colleni = colleni + 1
                subcollist.append(subcolarray)
            leaguearrayout[get_cur_tab].update({'values': subcollist})
        leaguearrayout[get_cur_tab].update({'rows': collist})
    sqldatacon[1].close()
    if (not CheckHockeySQLiteArray(leaguearrayout)):
        return False
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose):
        VerbosePrintOut(leaguearrayout)
    return leaguearrayout


def MakeHockeySQLiteXMLFromHockeySQLiteArray(inhockeyarray, beautify=True, encoding="UTF-8", includedtd=True, verbose=False, verbosetype="array"):
    if (not CheckHockeySQLiteArray(inhockeyarray)):
        return False
    xmlstring = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    if(includedtd):
        xmlstring = xmlstring+"\n"+hockeyaltxmldtdstring;
    if "database" in inhockeyarray.keys():
        xmlstring = xmlstring+"<hockeydb database=\"" + \
            EscapeXMLString(
                str(inhockeyarray['database']), quote=True)+"\">\n"
    if "database" not in inhockeyarray.keys():
        xmlstring = xmlstring+"<hockeydb database=\"" + \
            EscapeXMLString(str(defaultsdbfile), quote=True)+"\">\n"
    # all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games", "PlayoffTeams"]
    all_table_list = ["Conferences", "Divisions",
                      "Arenas", "Teams", "Stats", "GameStats", "Games"]
    table_list = ['HockeyLeagues']
    for leagueinfo_tmp in inhockeyarray['HockeyLeagues']['values']:
        for cur_tab in all_table_list:
            table_list.append(leagueinfo_tmp['LeagueName']+cur_tab)
    for get_cur_tab in table_list:
        xmlstring = xmlstring+" <table name=\"" + \
            EscapeXMLString(str(get_cur_tab), quote=True)+"\">\n"
        rowlen = len(inhockeyarray[get_cur_tab]['rows'])
        rowi = 0
        sqlrowlist = []
        xmlstring = xmlstring+"  <column>\n"
        for rowinfo in inhockeyarray[get_cur_tab]['rows']:
            xmlstring = xmlstring+"   <rowinfo id=\""+EscapeXMLString(str(inhockeyarray[get_cur_tab][rowinfo]['info']['id']), quote=True)+"\" name=\""+EscapeXMLString(str(inhockeyarray[get_cur_tab][rowinfo]['info']['Name']), quote=True)+"\" type=\""+EscapeXMLString(str(inhockeyarray[get_cur_tab][rowinfo]['info']['Type']), quote=True)+"\" notnull=\""+EscapeXMLString(str(inhockeyarray[get_cur_tab][rowinfo]['info']['NotNull']), quote=True)+"\" defaultvalue=\""+EscapeXMLString(
                ConvertPythonValuesForXML(str(inhockeyarray[get_cur_tab][rowinfo]['info']['DefualtValue'])), quote=True)+"\" primarykey=\""+EscapeXMLString(str(inhockeyarray[get_cur_tab][rowinfo]['info']['PrimaryKey']), quote=True)+"\" autoincrement=\""+EscapeXMLString(str(inhockeyarray[get_cur_tab][rowinfo]['info']['AutoIncrement']), quote=True)+"\" hidden=\""+EscapeXMLString(str(inhockeyarray[get_cur_tab][rowinfo]['info']['Hidden']), quote=True)+"\" />\n"
        xmlstring = xmlstring+"  </column>\n"
        if (len(inhockeyarray[get_cur_tab]['values']) > 0):
            xmlstring = xmlstring+"  <data>\n"
        rowid = 0
        for rowvalues in inhockeyarray[get_cur_tab]['values']:
            xmlstring = xmlstring+"   <row id=\"" + \
                EscapeXMLString(str(rowid), quote=True)+"\">\n"
            rowid = rowid + 1
            for rkey, rvalue in rowvalues.items():
                xmlstring = xmlstring+"    <rowdata name=\"" + \
                    EscapeXMLString(str(rkey), quote=True)+"\" value=\"" + \
                    EscapeXMLString(str(rvalue), quote=True)+"\" />\n"
            xmlstring = xmlstring+"   </row>\n"
        if (len(inhockeyarray[get_cur_tab]['values']) > 0):
            xmlstring = xmlstring+"  </data>\n"
        else:
            xmlstring = xmlstring+"  <data />\n"
        xmlstring = xmlstring+"  <rows>\n"
        for rowinfo in inhockeyarray[get_cur_tab]['rows']:
            xmlstring = xmlstring+"   <rowlist name=\"" + \
                EscapeXMLString(str(rowinfo), quote=True)+"\" />\n"
        xmlstring = xmlstring+"  </rows>\n"
        xmlstring = xmlstring+" </table>\n"
    xmlstring = xmlstring+"</hockeydb>\n"
    xmlstring = BeautifyXMLCode(xmlstring, False, " ", "\n", encoding, beautify)
    if (not CheckHockeySQLiteXML(xmlstring, False)):
        return False
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose):
        VerbosePrintOut(inhockeyarray)
    return xmlstring


def MakeHockeySQLiteXMLFileFromHockeySQLiteArray(inhockeyarray, outxmlfile=None, returnxml=False, beautify=True, encoding="UTF-8", includedtd=True, verbose=False, verbosetype="array"):
    if (outxmlfile is None):
        return False
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outxmlfile))):
        xmlfp = BytesIO()
    else:
        xmlfp = CompressOpenFile(outxmlfile)
    xmlstring = MakeHockeySQLiteXMLFromHockeySQLiteArray(
        inhockeyarray, beautify, encoding, includedtd, verbose, verbosetype)
    try:
        xmlfp.write(xmlstring)
    except TypeError:
        xmlfp.write(xmlstring.encode(encoding))
    try:
        xmlfp.flush()
        os.fsync(xmlfp.fileno())
    except io.UnsupportedOperation:
        pass
    except AttributeError:
        pass
    except OSError as e:
        pass
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outxmlfile))):
        xmlfp.seek(0, 0)
        upload_file_to_internet_file(xmlfp, outxmlfile)
        xmlfp.close()
    xmlfp.close()
    if (returnxml):
        return xmlstring
    if (not returnxml):
        return True
    return True


def MakeHockeySQLiteSGMLFromHockeySQLiteArray(inhockeyarray, beautify=True, encoding="UTF-8", includedtd=True, verbose=False, verbosetype="array"):
    if not CheckHockeySQLiteArray(inhockeyarray):
        return False
    sgmlstring = ""
    database_value = inhockeyarray.get('database', defaultsdbfile)
    if(includedtd):
        sgmlstring = sgmlstring+hockeyaltsgmldtdstring;
    sgmlstring += "<hockeydb database=\"" + EscapeSGMLString(str(database_value), quote=True) + "\">\n"
    
    # List of tables to process
    all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games"]
    table_list = ['HockeyLeagues']
    for leagueinfo_tmp in inhockeyarray['HockeyLeagues']['values']:
        table_list.extend([leagueinfo_tmp['LeagueName'] + tablename for tablename in all_table_list])
    
    for get_cur_tab in table_list:
        sgmlstring += " <table name=\"" + EscapeSGMLString(str(get_cur_tab), quote=True) + "\">\n"
        
        # Column definitions
        sgmlstring += "  <column>\n"
        for rowinfo in inhockeyarray[get_cur_tab]['rows']:
            rowdata = inhockeyarray[get_cur_tab][rowinfo]['info']
            sgmlstring += ("   <rowinfo id=\"" + EscapeSGMLString(str(rowdata['id']), quote=True) +
                           "\" name=\"" + EscapeSGMLString(str(rowdata['Name']), quote=True) +
                           "\" type=\"" + EscapeSGMLString(str(rowdata['Type']), quote=True) +
                           "\" notnull=\"" + EscapeSGMLString(str(rowdata['NotNull']), quote=True) +
                           "\" defaultvalue=\"" + EscapeSGMLString(str(rowdata['DefualtValue']), quote=True) +
                           "\" primarykey=\"" + EscapeSGMLString(str(rowdata['PrimaryKey']), quote=True) +
                           "\" autoincrement=\"" + EscapeSGMLString(str(rowdata['AutoIncrement']), quote=True) +
                           "\" hidden=\"" + EscapeSGMLString(str(rowdata['Hidden']), quote=True) + "\">\n")
        sgmlstring += "  </column>\n"
        
        # Data rows
        if len(inhockeyarray[get_cur_tab]['values']) > 0:
            sgmlstring += "  <data>\n"
            rowid = 0
            for rowvalues in inhockeyarray[get_cur_tab]['values']:
                sgmlstring += "   <row id=\"" + EscapeSGMLString(str(rowid), quote=True) + "\">\n"
                rowid += 1
                for rkey, rvalue in rowvalues.items():
                    sgmlstring += ("    <rowdata name=\"" + EscapeSGMLString(str(rkey), quote=True) +
                                   "\" value=\"" + EscapeSGMLString(str(rvalue), quote=True) + "\">\n")
                sgmlstring += "   </row>\n"
            sgmlstring += "  </data>\n"
        else:
            sgmlstring += "  <data></data>\n"
        
        # Row list
        sgmlstring += "  <rows>\n"
        for rowinfo in inhockeyarray[get_cur_tab]['rows']:
            sgmlstring += "   <rowlist name=\"" + EscapeSGMLString(str(rowinfo), quote=True) + "\">\n"
        sgmlstring += "  </rows>\n"
        sgmlstring += " </table>\n"
    
    sgmlstring += "</hockeydb>\n"

    if (not CheckHockeySQLiteSGML(sgmlstring, False)):
        return False
    
    if verbose:
        if verbosetype=="json":
            VerbosePrintOut(MakeHockeyJSONFromHockeyArray(inhockeyarray, verbose=False))
        if verbosetype=="yaml":
            VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(inhockeyarray, verbose=False))
        if verbosetype=="xml":
            VerbosePrintOut(MakeHockeyXMLFromHockeyArray(inhockeyarray, verbose=False))
        if verbosetype=="sgml":
            VerbosePrintOut(MakeHockeySGMLFromHockeyArray(inhockeyarray, verbose=False))
        else:
            VerbosePrintOut(inhockeyarray)
    
    return sgmlstring


def MakeHockeySQLiteSGMLFileFromHockeySQLiteArray(inhockeyarray, outsgmlfile=None, returnsgml=False, beautify=True, encoding="UTF-8", includedtd=True, verbose=False, verbosetype="array"):
    if (outsgmlfile is None):
        return False
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outsgmlfile))):
        sgmlfp = BytesIO()
    else:
        sgmlfp = CompressOpenFile(outsgmlfile)
    sgmlstring = MakeHockeySQLiteSGMLFromHockeySQLiteArray(
        inhockeyarray, beautify, encoding, includedtd, verbose, verbosetype)
    try:
        sgmlfp.write(sgmlstring)
    except TypeError:
        sgmlfp.write(sgmlstring.encode(encoding))
    try:
        sgmlfp.flush()
        os.fsync(sgmlfp.fileno())
    except io.UnsupportedOperation:
        pass
    except AttributeError:
        pass
    except OSError as e:
        pass
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outsgmlfile))):
        sgmlfp.seek(0, 0)
        upload_file_to_internet_file(sgmlfp, outsgmlfile)
        sgmlfp.close()
    sgmlfp.close()
    if (returnsgml):
        return sgmlstring
    if (not returnsgml):
        return True
    return True


def MakeHockeySQLiteXMLAltFromHockeySQLiteArray(inhockeyarray, beautify=True, encoding="UTF-8", includedtd=True, verbose=False, verbosetype="array"):
    if (not CheckHockeySQLiteArray(inhockeyarray)):
        return False
    if "database" in inhockeyarray.keys():
        xmlstring_hockeydb = cElementTree.Element(
            "hockeydb", {'database': str(inhockeyarray['database'])})
    if "database" not in inhockeyarray.keys():
        xmlstring_hockeydb = cElementTree.Element(
            "hockeydb", {'database': str(defaultsdbfile)})
    # all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games", "PlayoffTeams"]
    all_table_list = ["Conferences", "Divisions",
                      "Arenas", "Teams", "Stats", "GameStats", "Games"]
    table_list = ['HockeyLeagues']
    for leagueinfo_tmp in inhockeyarray['HockeyLeagues']['values']:
        for cur_tab in all_table_list:
            table_list.append(leagueinfo_tmp['LeagueName']+cur_tab)
    for get_cur_tab in table_list:
        xmlstring_table = cElementTree.SubElement(
            xmlstring_hockeydb, "table", {'name': str(get_cur_tab)})
        rowlen = len(inhockeyarray[get_cur_tab]['rows'])
        rowi = 0
        sqlrowlist = []
        xmlstring_column = cElementTree.SubElement(xmlstring_table, "column")
        for rowinfo in inhockeyarray[get_cur_tab]['rows']:
            xmlstring_rowinfo = cElementTree.SubElement(xmlstring_column, "rowinfo", {'id': str(inhockeyarray[get_cur_tab][rowinfo]['info']['id']), 'name': str(inhockeyarray[get_cur_tab][rowinfo]['info']['Name']), 'type': str(inhockeyarray[get_cur_tab][rowinfo]['info']['Type']), 'notnull': str(inhockeyarray[get_cur_tab][rowinfo]['info']['NotNull']), 'defaultvalue': ConvertPythonValuesForXML(
                str(inhockeyarray[get_cur_tab][rowinfo]['info']['DefualtValue'])), 'primarykey': str(inhockeyarray[get_cur_tab][rowinfo]['info']['PrimaryKey']), 'autoincrement': str(inhockeyarray[get_cur_tab][rowinfo]['info']['AutoIncrement']), 'hidden': str(inhockeyarray[get_cur_tab][rowinfo]['info']['Hidden'])})
        if (len(inhockeyarray[get_cur_tab]['values']) > 0):
            xmlstring_data = cElementTree.SubElement(xmlstring_table, "data")
        rowid = 0
        for rowvalues in inhockeyarray[get_cur_tab]['values']:
            xmlstring_row = cElementTree.SubElement(
                xmlstring_data, "row", {'id': str(rowid)})
            rowid = rowid + 1
            for rkey, rvalue in rowvalues.items():
                xmlstring_rowdata = cElementTree.SubElement(
                    xmlstring_row, "rowdata", {'name': str(rkey), 'value': str(rvalue)})
        if (len(inhockeyarray[get_cur_tab]['values']) < 0):
            xmlstring_data = cElementTree.SubElement(xmlstring_table, "data")
        xmlstring_rows = cElementTree.SubElement(xmlstring_table, "rows")
        for rowinfo in inhockeyarray[get_cur_tab]['rows']:
            xmlstring_rowlist = cElementTree.SubElement(
                xmlstring_rows, "rowlist", {'name': str(rowinfo)})
    '''xmlstring = cElementTree.tostring(xmlstring_hockey, encoding, "xml", True, "xml", True)'''
    try:
        xmlstring = cElementTree.tostring(
                xmlstring_hockey, encoding=encoding, method="xml", xml_declaration=True)
    except TypeError:
        xmlstring = cElementTree.tostring(
                xmlstring_hockey, encoding=encoding, method="xml")
    if (hasattr(xmlstring, 'decode')):
        xmlstring = xmlstring.decode(encoding)
    xmlstring = BeautifyXMLCode(xmlstring, False, " ", "\n", encoding, beautify)
    if (hasattr(xmlstring, 'decode')):
        xmlstring = xmlstring.decode(encoding)
    # Insert the DTD after the XML declaration, before the root element
    if includedtd:
        xml_declaration = '<?xml version="1.0" encoding="{}"?>\n'.format(encoding)
        xmlstring = xml_declaration + hockeyaltxmldtdstring + "\n" + xmlstring[len(xml_declaration):]
    if (not CheckHockeySQLiteXML(xmlstring, False)):
        return False
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose):
        VerbosePrintOut(inhockeyarray)
    return xmlstring


def MakeHockeySQLiteXMLAltFileFromHockeySQLiteArray(inhockeyarray, outxmlfile=None, returnxml=False, beautify=True, encoding="UTF-8", includedtd=True, verbose=False, verbosetype="array"):
    if (outxmlfile is None):
        return False
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outxmlfile))):
        xmlfp = BytesIO()
    else:
        xmlfp = CompressOpenFile(outxmlfile)
    xmlstring = MakeHockeySQLiteXMLAltFromHockeySQLiteArray(
        inhockeyarray, beautify, encoding, includedtd, verbose, verbosetype)
    try:
        xmlfp.write(xmlstring)
    except TypeError:
        xmlfp.write(xmlstring.encode(encoding))
    try:
        xmlfp.flush()
        os.fsync(xmlfp.fileno())
    except io.UnsupportedOperation:
        pass
    except AttributeError:
        pass
    except OSError as e:
        pass
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outxmlfile))):
        xmlfp.seek(0, 0)
        upload_file_to_internet_file(xmlfp, outxmlfile)
        xmlfp.close()
    xmlfp.close()
    if (returnxml):
        return xmlstring
    if (not returnxml):
        return True
    return True


def MakeHockeySQLiteArrayFromHockeySQLiteXML(inxmlfile, xmlisfile=True, encoding="UTF-8", verbose=False, verbosetype="array"):
    if (not CheckHockeySQLiteXML(inxmlfile, xmlisfile)):
        return False
    if (xmlisfile and ((os.path.exists(inxmlfile) and os.path.isfile(inxmlfile)) or re.findall("^(http|https|ftp|ftps|sftp)\\:\\/\\/", inxmlfile))):
        try:
            if (re.findall("^(http|https|ftp|ftps|sftp)\\:\\/\\/", inxmlfile)):
                inxmlfile = UncompressFileURL(
                    inxmlfile)
                try:
                    hockeyfile = cElementTree.parse(
                        inxmlfile, parser=cElementTree.XMLParser(encoding=encoding))
                    hockeyroot = hockeyfile.getroot()
                except cElementTree.ParseError:
                    try:
                        inxmlfile.seek(0, 0)
                        hockeyroot = cElementTree.fromstring(inxmlfile.read())
                    except cElementTree.ParseError:
                        return False
            else:
                hockeyfile = cElementTree.parse(UncompressFile(
                    inxmlfile), parser=cElementTree.XMLParser(encoding=encoding))
                hockeyroot = hockeyfile.getroot()
        except cElementTree.ParseError:
            try:
                hockeyroot = cElementTree.fromstring(
                    UncompressFile(inxmlfile).read())
            except cElementTree.ParseError:
                return False
    elif (not xmlisfile):
        chckcompression = CheckCompressionTypeFromString(inxmlfile)
        if (not chckcompression):
            inxmlfile = StringIO(inxmlfile)
        else:
            try:
                inxmlsfile = BytesIO(inxmlfile)
            except TypeError:
                inxmlsfile = BytesIO(inxmlfile.encode(encoding))
            inxmlfile = UncompressFile(inxmlsfile)
        try:
            hockeyfile = cElementTree.parse(
                inxmlfile, parser=cElementTree.XMLParser(encoding=encoding))
            hockeyroot = hockeyfile.getroot()
        except cElementTree.ParseError:
            try:
                inxmlfile.seek(0, 0)
                hockeyroot = cElementTree.fromstring(inxmlfile.read())
            except cElementTree.ParseError:
                return False
    else:
        return False
    leaguearrayout = {'database': str(hockeyroot.attrib['database'])}
    for gettable in hockeyroot:
        leaguearrayout.update(
            {gettable.attrib['name']: {'rows': [], 'values': []}})
        if (gettable.tag == "table"):
            columnstart = 0
            for getcolumn in gettable:
                if (getcolumn.tag == "column"):
                    columnstart = 1
                    rowinfonum = 0
                    for getcolumninfo in getcolumn:
                        if (getcolumninfo.tag == "rowinfo"):
                            defaultvale = getcolumninfo.attrib['defaultvalue']
                            if (defaultvale.isdigit()):
                                defaultvale = int(defaultvale)
                            if (defaultvale == "None"):
                                defaultvale = None
                            leaguearrayout[gettable.attrib['name']].update({getcolumninfo.attrib['name']: {'info': {'id': int(getcolumninfo.attrib['id']), 'Name': getcolumninfo.attrib['name'], 'Type': getcolumninfo.attrib['type'], 'NotNull': int(
                                getcolumninfo.attrib['notnull']), 'DefualtValue': ConvertXMLValuesForPython(defaultvale), 'PrimaryKey': int(getcolumninfo.attrib['primarykey']), 'AutoIncrement': int(getcolumninfo.attrib['autoincrement']), 'Hidden': int(getcolumninfo.attrib['hidden'])}}})
                            rowinfonum = rowinfonum + 1
            datastart = 0
            for getdata in gettable:
                if (getdata.tag == "data"):
                    datastart = 1
                    rowstart = 0
                    rowdatanum = 0
                    for getrow in getdata:
                        if (getrow.tag == "row"):
                            rowstart = 1
                            rowdatanum = 0
                            rowdatadict = {}
                            for getrowdata in getrow:
                                if (getrowdata.tag == "rowdata"):
                                    rowdatadict.update(
                                        {getrowdata.attrib['name']: getrowdata.attrib['value']})
                                    rowdatanum = rowdatanum + 1
                            leaguearrayout[gettable.attrib['name']
                                           ]['values'].append(rowdatadict)
            rowsstart = 0
            rowscount = 0
            for getrows in gettable:
                if (getrows.tag == "rows"):
                    rowsstart = 1
                    rowscount = 0
                    for getrowlist in getcolumn:
                        if (getrowlist.tag == "rowlist"):
                            leaguearrayout[gettable.attrib['name']]['rows'].append(
                                getrowlist.attrib['name'])
                            rowscount = rowscount + 1
    if (not CheckHockeySQLiteArray(leaguearrayout)):
        return False
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose):
        VerbosePrintOut(leaguearrayout)
    return leaguearrayout


def MakeHockeySQLiteArrayFromHockeySQLiteSGML(insgmlfile, sgmlisfile=True, encoding="UTF-8", verbose=False, verbosetype="array"):
    """
    Parses SGML data representing a hockey SQLite database and converts it into a hockey SQLite array.
    """
    if (not CheckHockeySQLiteSGML(insgmlfile, sgmlisfile)):
        return False
    # Read SGML data
    sgml_data = ReadSGMLData(insgmlfile, sgmlisfile=sgmlisfile, encoding=encoding)
    if sgml_data is False:
        return False

    # Parse SGML data
    parser = HockeySQLiteSGMLParser()
    try:
        parser.feed(sgml_data)
        parser.close()
    except Exception as e:
        return False

    leaguearrayout = parser.leaguearrayout

    # Check if the resulting array is valid
    if not CheckHockeySQLiteArray(leaguearrayout):
        return False

    # Verbose output
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose):
        VerbosePrintOut(leaguearrayout)

    return leaguearrayout


def MakeHockeySQLiteArrayFromHockeySQLiteXMLAlt(inxmlfile, xmlisfile=True, encoding="UTF-8", verbose=False, verbosetype="array"):
 return MakeHockeySQLiteArrayFromHockeySQLiteSGML(inxmlfile, xmlisfile, encoding, verbose, verbosetype)


def MakeHockeyArrayFromHockeySQLiteArray(inhockeyarray, verbose=False, verbosetype="array"):
    if (not CheckHockeySQLiteArray(inhockeyarray)):
        return False
    leaguearrayout = {'database': str(inhockeyarray['database'])}
    leaguelist = []
    for leagueinfo in inhockeyarray['HockeyLeagues']['values']:
        leaguearray = {}
        arenalist = []
        gamelist = []
        conarrayname = leagueinfo['LeagueName']+"Conferences"
        divarrayname = leagueinfo['LeagueName']+"Divisions"
        teamarrayname = leagueinfo['LeagueName']+"Teams"
        araarrayname = leagueinfo['LeagueName']+"Arenas"
        gamearrayname = leagueinfo['LeagueName']+"Games"
        HockeyLeagueHasConferences = True
        HockeyLeagueHasConferenceStr = "yes"
        if (int(leagueinfo['NumberOfConferences']) <= 0):
            HockeyLeagueHasConferences = False
            HockeyLeagueHasConferenceStr = "no"
        HockeyLeagueHasDivisions = True
        HockeyLeagueHasDivisionStr = "yes"
        if (int(leagueinfo['NumberOfDivisions']) <= 0):
            HockeyLeagueHasDivisions = False
            HockeyLeagueHasDivisionStr = "no"
        tempdict = {'leagueinfo': {'name': str(leagueinfo['LeagueName']), 'fullname': str(leagueinfo['LeagueFullName']), 'country': str(leagueinfo['CountryName']), 'fullcountry': str(leagueinfo['FullCountryName']), 'date': str(leagueinfo['Date']), 'playofffmt': str(
            leagueinfo['PlayOffFMT']), 'ordertype': str(leagueinfo['OrderType']), 'conferences': str(HockeyLeagueHasConferenceStr), 'divisions': str(HockeyLeagueHasDivisionStr)}, 'quickinfo': {'conferenceinfo': {}, 'divisioninfo': {}, 'teaminfo': {}}}
        leaguearray.update({str(leagueinfo['LeagueName']): tempdict})
        leaguelist.append(str(leagueinfo['LeagueName']))
        conferencelist = []
        for conferenceinfo in inhockeyarray[conarrayname]['values']:
            leaguearray[str(leagueinfo['LeagueName'])].update({str(conferenceinfo['Conference']): {'conferenceinfo': {'name': str(conferenceinfo['Conference']), 'prefix': str(
                conferenceinfo['ConferencePrefix']), 'suffix': str(conferenceinfo['ConferenceSuffix']), 'fullname': str(conferenceinfo['FullName']), 'league': str(leagueinfo['LeagueName'])}}})
            leaguearray[str(leagueinfo['LeagueName'])]['quickinfo']['conferenceinfo'].update({str(conferenceinfo['Conference']): {
                'name': str(conferenceinfo['Conference']), 'fullname': str(conferenceinfo['FullName']), 'league': str(leagueinfo['LeagueName'])}})
            conferencelist.append(str(conferenceinfo['Conference']))
            divisionlist = []
            for divisioninfo in inhockeyarray[divarrayname]['values']:
                leaguearray[str(leagueinfo['LeagueName'])][str(conferenceinfo['Conference'])].update({str(divisioninfo['Division']): {'divisioninfo': {'name': str(divisioninfo['Division']), 'prefix': str(
                    divisioninfo['DivisionPrefix']), 'suffix': str(divisioninfo['DivisionSuffix']), 'fullname': str(divisioninfo['FullName']), 'league': str(leagueinfo['LeagueName']), 'conference': str(conferenceinfo['Conference'])}}})
                leaguearray[str(leagueinfo['LeagueName'])]['quickinfo']['divisioninfo'].update({str(divisioninfo['Division']): {'name': str(
                    divisioninfo['Division']), 'fullname': str(divisioninfo['FullName']), 'league': str(leagueinfo['LeagueName']), 'conference': str(conferenceinfo['Conference'])}})
                divisionlist.append(str(divisioninfo['Division']))
                teamlist = []
                for teaminfo in inhockeyarray[teamarrayname]['values']:
                    fullteamname = GetFullTeamName(str(teaminfo['TeamName']), str(
                        teaminfo['TeamPrefix']), str(teaminfo['TeamSuffix']))
                    leaguearray[str(leagueinfo['LeagueName'])][str(conferenceinfo['Conference'])][str(divisioninfo['Division'])].update({str(teaminfo['TeamName']): {'teaminfo': {'city': str(teaminfo['CityName']), 'area': str(teaminfo['AreaName']), 'fullarea': str(teaminfo['FullAreaName']), 'country': str(teaminfo['CountryName']), 'fullcountry': str(teaminfo['FullCountryName']), 'name': str(
                        teaminfo['TeamName']), 'fullname': fullteamname, 'arena': str(teaminfo['ArenaName']), 'prefix': str(teaminfo['TeamPrefix']), 'suffix': str(teaminfo['TeamSuffix']), 'league': str(leagueinfo['LeagueName']), 'conference': str(conferenceinfo['Conference']), 'division': str(divisioninfo['Division']), 'affiliates': str(teaminfo['Affiliates'])}}})
                    leaguearray[str(leagueinfo['LeagueName'])]['quickinfo']['teaminfo'].update({str(teaminfo['TeamName']): {'name': str(teaminfo['TeamName']), 'fullname': fullteamname, 'league': str(
                        leagueinfo['LeagueName']), 'conference': str(conferenceinfo['Conference']), 'division': str(divisioninfo['Division'])}})
                    teamlist.append(str(teaminfo['TeamName']))
                leaguearray[str(leagueinfo['LeagueName'])][str(conferenceinfo['Conference'])][str(
                    divisioninfo['Division'])].update({'teamlist': teamlist})
            leaguearray[str(leagueinfo['LeagueName'])][str(
                conferenceinfo['Conference'])].update({'divisionlist': divisionlist})
        leaguearray[str(leagueinfo['LeagueName'])].update(
            {'conferencelist': conferencelist})
        getteam_num = len(inhockeyarray[teamarrayname]['values'])
        if (getteam_num > 0):
            for arenainfo in inhockeyarray[teamarrayname]['values']:
                arenalist.append({'city': str(arenainfo['CityName']), 'area': str(arenainfo['AreaName']), 'fullarea': str(arenainfo['FullAreaName']), 'country': str(
                    arenainfo['CountryName']), 'fullcountry': str(arenainfo['FullCountryName']), 'name': str(arenainfo['ArenaName'])})
        leaguearray[str(leagueinfo['LeagueName'])].update(
            {"arenas": arenalist})
        getgame_num = len(inhockeyarray[gamearrayname]['values'])
        if (getgame_num > 0):
            for gameinfo in inhockeyarray[gamearrayname]['values']:
                gamelist.append({'date': str(gameinfo['Date']), 'time': str(gameinfo['Time']), 'hometeam': str(gameinfo['HomeTeam']), 'awayteam': str(gameinfo['AwayTeam']), 'goals': str(gameinfo['TeamScorePeriods']), 'sogs': str(gameinfo['ShotsOnGoal']), 'ppgs': str(gameinfo['PowerPlays']), 'shgs': str(
                    gameinfo['ShortHanded']), 'penalties': str(gameinfo['Penalties']), 'pims': str(gameinfo['PenaltyMinutes']), 'hits': str(gameinfo['HitsPerPeriod']), 'takeaways': str(gameinfo['TakeAways']), 'faceoffwins': str(gameinfo['FaceoffWins']), 'atarena': str(gameinfo['AtArena']), 'isplayoffgame': str(gameinfo['IsPlayOffGame'])})
        leaguearray[str(leagueinfo['LeagueName'])].update({"games": gamelist})
        leaguearrayout.update(leaguearray)
    leaguearrayout.update({'leaguelist': leaguelist})
    if (not CheckHockeyArray(leaguearrayout)):
        return False
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            leaguearrayout, verbose=False))
    elif (verbose):
        VerbosePrintOut(leaguearrayout)
    return leaguearrayout


def MakeHockeySQLFromHockeySQLiteArray(inhockeyarray, insdbfile=":memory:", verbose=False, verbosetype="array"):
    if (not CheckHockeySQLiteArray(inhockeyarray)):
        return False
    if (insdbfile is None or insdbfile == ":memory:"):
        insdbfile = inhockeyarray['database']
    # all_table_list = ["Conferences", "Divisions", "Arenas", "Teams", "Stats", "GameStats", "Games", "PlayoffTeams"]
    all_table_list = ["Conferences", "Divisions",
                      "Arenas", "Teams", "Stats", "GameStats", "Games"]
    table_list = ['HockeyLeagues']
    for leagueinfo_tmp in inhockeyarray['HockeyLeagues']['values']:
        for cur_tab in all_table_list:
            table_list.append(leagueinfo_tmp['LeagueName']+cur_tab)
    sqldump = "-- "+__program_name__+" SQL Dumper\n"
    sqldump = sqldump+"-- version "+__version__+"\n"
    sqldump = sqldump+"-- "+__project_url__+"\n"
    sqldump = sqldump+"--\n"
    sqldump = sqldump+"-- Generation Time: " + \
        time.strftime("%B %d, %Y at %I:%M %p", time.localtime())+"\n"
    sqldump = sqldump+"-- SQLite Server version: "+sqlite3.sqlite_version+"\n"
    sqldump = sqldump+"-- PySQLite version: "+sqlite3.version+"\n"
    sqldump = sqldump+"-- Python Version: " + \
        str(sys.version_info[0])+"."+str(sys.version_info[1]
                                         )+"."+str(sys.version_info[2])+"\n"
    sqldump = sqldump+"--\n"
    sqldump = sqldump+"-- Database: "+insdbfile+"\n"
    sqldump = sqldump+"--\n\n"
    sqldump = sqldump+"-- --------------------------------------------------------\n\n"
    for get_cur_tab in table_list:
        sqldump = sqldump+"--\n"
        sqldump = sqldump+"-- Table structure for table "+str(get_cur_tab)+"\n"
        sqldump = sqldump+"--\n\n"
        sqldump = sqldump+"DROP TABLE IF EXISTS "+get_cur_tab+"\n\n"
        sqldump = sqldump+"CREATE TEMP TABLE "+get_cur_tab+" (\n"
        rowlen = len(inhockeyarray[get_cur_tab]['rows'])
        rowi = 0
        sqlrowlist = []
        for rowinfo in inhockeyarray[get_cur_tab]['rows']:
            sqlrowline = inhockeyarray[get_cur_tab][rowinfo]['info']['Name'] + \
                " "+inhockeyarray[get_cur_tab][rowinfo]['info']['Type']
            if (inhockeyarray[get_cur_tab][rowinfo]['info']['NotNull'] == 1):
                sqlrowline = sqlrowline+" NOT NULL"
            if (inhockeyarray[get_cur_tab][rowinfo]['info']['DefualtValue'] is not None):
                sqlrowline = sqlrowline+" " + \
                    inhockeyarray[get_cur_tab][rowinfo]['info']['DefualtValue']
            if (inhockeyarray[get_cur_tab][rowinfo]['info']['PrimaryKey'] == 1):
                sqlrowline = sqlrowline+" PRIMARY KEY"
            if (inhockeyarray[get_cur_tab][rowinfo]['info']['AutoIncrement'] == 1):
                sqlrowline = sqlrowline+" AUTOINCREMENT"
            sqlrowlist.append(sqlrowline)
        sqldump = sqldump+str(',\n'.join(sqlrowlist))+"\n);\n\n"
        sqldump = sqldump+"--\n"
        sqldump = sqldump+"-- Dumping data for table "+str(get_cur_tab)+"\n"
        sqldump = sqldump+"--\n\n"
        for rowvalues in inhockeyarray[get_cur_tab]['values']:
            rkeylist = []
            rvaluelist = []
            for rkey, rvalue in rowvalues.items():
                rkeylist.append(rkey)
                if (isinstance(rvalue, basestring)):
                    rvalue = "\""+rvalue+"\""
                rvaluelist.append(str(rvalue))
            sqldump = sqldump+"INSERT INTO " + \
                str(get_cur_tab)+" ("+str(', '.join(rkeylist))+") VALUES\n"
            sqldump = sqldump+"("+str(', '.join(rvaluelist))+");\n"
        sqldump = sqldump+"\n-- --------------------------------------------------------\n\n"
    if (verbose and verbosetype=="json"):
        VerbosePrintOut(MakeHockeyJSONFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="yaml"):
        VerbosePrintOut(MakeHockeyYAMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="xml"):
        VerbosePrintOut(MakeHockeyXMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose and verbosetype=="sgml"):
        VerbosePrintOut(MakeHockeySGMLFromHockeyArray(
            inhockeyarray, verbose=False))
    elif (verbose):
        VerbosePrintOut(inhockeyarray)
    return sqldump


def MakeHockeySQLFileFromHockeySQLiteArray(inhockeyarray, outsqlfile=None, returnsql=False, encoding="UTF-8", verbose=False, verbosetype="array"):
    if (outsqlfile is None):
        return False
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outsqlfile))):
        sqlfp = BytesIO()
    else:
        sqlfp = CompressOpenFile(outsqlfile)
    sqlstring = MakeHockeySQLFromHockeySQLiteArray(
        inhockeyarray, os.path.splitext(outsqlfile)[0]+".db3", verbose, verbosetype)
    try:
        sqlfp.write(sqlstring)
    except TypeError:
        sqlfp.write(sqlstring.encode(encoding))
    try:
        sqlfp.flush()
        os.fsync(sqlfp.fileno())
    except io.UnsupportedOperation:
        pass
    except AttributeError:
        pass
    except OSError as e:
        pass
    if(re.findall(r"^(ftp|ftps|sftp)\:\/\/", str(outsqlfile))):
        sqlfp.seek(0, 0)
        upload_file_to_internet_file(sqlfp, outsqlfile)
        sqlfp.close()
    sqlfp.close()
    if (returnsql):
        return sqlstring
    if (not returnsql):
        return True
    return True
