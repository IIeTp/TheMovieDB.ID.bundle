import re, importlib, sys, os, importlib
from os.path import *

def plexpathbin(module):
  return (os.path.split(os.path.split(module.__file__)[0])[0])

def plexporiginpluginspath(plexpathh):
  list_dir = [d for d in os.listdir(plexpathh + "\Resources") if os.path.isdir(os.path.join(plexpathh + "\Resources", d))]
  index = 0
  for item in list_dir:
    plugins_path = find_id(r'(Plug-ins-)(.+)', item)
    if plugins_path:
      return(plugins_path)
      break
    index = index + 1
  return None

def module_add_syspath(mod_path, mod_name):
  module_file = os.path.isfile(os.path.realpath(os.path.join(mod_path + mod_name)))
  if module_file == True:
    module_path = os.path.realpath(os.path.join(mod_path))
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
