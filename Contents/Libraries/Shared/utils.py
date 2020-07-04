import re, importlib, sys, os, importlib
from os.path import *

def import_ext_module(mod_path, mod_name):
  module_file = os.path.isfile(os.path.realpath(os.path.join(mod_path + mod_name)))
  if module_file == True:
    module_path = os.path.realpath(os.path.join(mod_path))
    sys.path.append(module_path)
    my_mod = importlib.import_module(mod_name[:(len(mod_name)-3)])
    return my_mod
  else:
    return False

def filebot_is(prefs_is):
  if prefs_is == True:
    import_mod = import_ext_module('../../../Scanners/Common/', 'filebotid.py')
    if import_mod != False:
      return import_mod
    else:
      import_mod = import_ext_module('../../../Scanners/Common/', 'filebot.py')
      if import_mod != False:
        return import_mod
      else:
        return False
  else:
    return False

def xstr(s):
    if s is None:
      return ''
    return str(s)

def find_id(regexp_str, search_str):
  id_ids = re.search(regexp_str, search_str, re.IGNORECASE)
  if id_ids is not None:
    id_is = id_ids.group(0)
    return id_is
  else:
    return None
