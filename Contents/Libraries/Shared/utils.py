import re, importlib, sys, os, importlib
from os.path import *

def module_add_syspath(mod_path, mod_name):
  module_file = os.path.isfile(os.path.realpath(os.path.join(os.path.normpath(mod_path + mod_name))))
  if module_file == True:
    module_path = os.path.realpath(os.path.join(os.path.normpath(mod_path)))
    sys.path.append(module_path)
    return True
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
