import os
prefs = False
meta_path = '../../../Plug-in Support/Metadata Combination/com.plexapp.agents.themoviedb.id/'
meta_file = "Movies.xml"
meta_full_path = meta_path + meta_file

def is_file(file_path, file_name):
  ref_file = os.path.isfile(os.path.realpath(os.path.join(file_path + file_name)))
  if ref_file == True:
    return True
  else:
    return False

def check_metapref(Prefs):
  if is_file(meta_path, meta_file) == False:
    if not os.path.exists(meta_path):
        os.makedirs(meta_path)
    new_file = open(meta_full_path,"w")
    new_data = ["<?xml version='1.0' encoding='utf8'?>\n", '<combine class="Movie">\n', '  <sources>\n', '    <agent>com.plexapp.agents.themoviedb.id</agent>\n', '  </sources>\n', '</combine>\n']
    for i in new_data:
       new_file.write(i)
    new_file.close()

  meta_prefs = open(meta_full_path,"r")
  meta_list = meta_prefs.readlines()
  agent_num = meta_list.index("    <agent>com.plexapp.agents.themoviedb.id</agent>\n")
  meta_prefs.close()
  if Prefs['tmdb_trailer'] == True and meta_list.count("    <agent>com.plexapp.agents.tmdbtrailer</agent>\n") > 0:
    pass
  elif Prefs['tmdb_trailer'] == True and meta_list.count("    <agent>com.plexapp.agents.tmdbtrailer</agent>\n") == 0:
    meta_list.insert(agent_num + 1, "    <agent>com.plexapp.agents.tmdbtrailer</agent>\n")
    meta_prefs = open(meta_full_path,"w")
    for i in meta_list:
       meta_prefs.write(i)
    meta_prefs.close()
  elif Prefs['tmdb_trailer'] == False and meta_list.count("    <agent>com.plexapp.agents.tmdbtrailer</agent>\n") > 0:
    meta_list.remove("    <agent>com.plexapp.agents.tmdbtrailer</agent>\n")
    meta_prefs = open(meta_full_path,"w")
    for i in meta_list:
       meta_prefs.write(i)
    meta_prefs.close()

  if Prefs['fanart'] == True and meta_list.count("    <agent>com.plexapp.agents.fanarttv</agent>\n") > 0:
    pass
  elif Prefs['fanart'] == True and meta_list.count("    <agent>com.plexapp.agents.fanarttv</agent>\n") == 0:
    meta_list.insert(agent_num + 1, "    <agent>com.plexapp.agents.fanarttv</agent>\n")
    meta_prefs = open(meta_full_path,"w")
    for i in meta_list:
       meta_prefs.write(i)
    meta_prefs.close()
  elif Prefs['fanart'] == False and meta_list.count("    <agent>com.plexapp.agents.fanarttv</agent>\n") > 0:
    meta_list.remove("    <agent>com.plexapp.agents.fanarttv</agent>\n")
    meta_prefs = open(meta_full_path,"w")
    for i in meta_list:
       meta_prefs.write(i)
    meta_prefs.close()