import os
from time import sleep

def check_agent(plugis_path, home_path):
  sleep(1)
# ############## Fanart.tv plugin
  # filepath = "%s\\Fanart-TV.bundle\\Contents\\Code\\%s" % (plugis_path, '__init__.py')
  # init_file = os.path.isfile(os.path.realpath(os.path.join(filepath)))
  # if init_file:
    # init_file = open(filepath,"r")
    # init_list = init_file.readlines()
    # try:
      # index_num = init_list.index("		'com.plexapp.agents.themoviedb'\n")
    # except:
      # index_num = None
    # init_file.close()
    # if index_num is not None:
      # init_list[index_num] = "		'com.plexapp.agents.themoviedb', 'com.plexapp.agents.themoviedb.id'\n"
      # index_num = init_list.index("		'com.plexapp.agents.themoviedb'\n")
      # init_list[index_num] = "		'com.plexapp.agents.themoviedb', 'com.plexapp.agents.themoviedb.id'\n"
      # index_num = init_list.index("		elif media.primary_agent == 'com.plexapp.agents.themoviedb':\n")
      # init_list[index_num] = "		elif media.primary_agent == 'com.plexapp.agents.themoviedb' or media.primary_agent == 'com.plexapp.agents.themoviedb.id':\n"   
      # init_file = open(filepath,"w")
      # for i in init_list:
         # init_file.write(i)
      # init_file.close()
# ############## MoviePosterDB plugin
  # filepath = "%s\\MoviePosterDB.bundle\\Contents\\Code\\%s" % (plugis_path, '__init__.py')
  # init_file = os.path.isfile(os.path.realpath(os.path.join(filepath)))
  # if init_file:
    # init_file = open(filepath,"r")
    # init_list = init_file.readlines()
    # try:
      # index_num = init_list.index("	contributes_to = ['com.plexapp.agents.imdb']\n")
    # except:
      # index_num = None
    # init_file.close()
    # if index_num is not None:
      # init_list[index_num] = "	contributes_to = ['com.plexapp.agents.imdb', 'com.plexapp.agents.themoviedb.id']\n"
      # init_file = open(filepath,"w")
      # for i in init_list:
         # init_file.write(i)
      # init_file.close()
# ############## Plex Movie plugin
  # filepath = "%s\\PlexMovie.bundle\\Contents\\Code\\%s" % (plugis_path, '__init__.py')
  # init_file = os.path.isfile(os.path.realpath(os.path.join(filepath)))
  # if init_file:
    # init_file = open(filepath,"r")
    # init_list = init_file.readlines()
    # try:
      # index_num = init_list.index("  contributes_to = ['com.plexapp.agents.themoviedb']\n")
    # except:
      # index_num = None
    # init_file.close()
    # if index_num is not None:
      # init_list[index_num] = "  contributes_to = ['com.plexapp.agents.themoviedb', 'com.plexapp.agents.themoviedb.id']\n"
      # index_num = init_list.index("      tmdb_search = re.search(r'^(com.plexapp.agents.themoviedb://)([\d]+)\?.+', theGuid)\n")
      # init_list[index_num] = "      tmdb_search = re.search(r'^(com.plexapp.agents.themoviedb.id://|com.plexapp.agents.themoviedb://)([\d]+)\?.+', theGuid)\n"
      # index_num = init_list.index("    tmdb_search = re.search(r'^(com.plexapp.agents.themoviedb://)([\d]+)\?.+', metadata.guid)\n")
      # init_list[index_num] = "    tmdb_search = re.search(r'^(com.plexapp.agents.themoviedb.id://|com.plexapp.agents.themoviedb://)([\d]+)\?.+', metadata.guid)\n"      
      # init_file = open(filepath,"w")
      # for i in init_list:
         # init_file.write(i)
      # init_file.close()
# ################ OpenSubtitles plugin
  # filepath = "%s\\OpenSubtitles.bundle\\Contents\\Code\\%s" % (plugis_path, '__init__.py')
  # init_file = os.path.isfile(os.path.realpath(os.path.join(filepath)))
  # if init_file:
    # init_file = open(filepath,"r")
    # init_list = init_file.readlines()
    # try:
      # index_num = init_list.index("  contributes_to = ['com.plexapp.agents.imdb']\n")
    # except:
      # index_num = None
    # init_file.close()
    # if index_num is not None:
      # init_list[index_num] = "  contributes_to = ['com.plexapp.agents.imdb', 'com.plexapp.agents.themoviedb.id']\n"
      # init_file = open(filepath,"w")
      # for i in init_list:
         # init_file.write(i)
      # init_file.close()
# ############## PlexThemeMusic plugin
  # filepath = "%s\\PlexThemeMusic.bundle\\Contents\\Code\\%s" % (plugis_path, '__init__.py')
  # init_file = os.path.isfile(os.path.realpath(os.path.join(filepath)))
  # if init_file:
    # init_file = open(filepath,"r")
    # init_list = init_file.readlines()
    # try:
      # index_num = init_list.index("    'com.plexapp.agents.themoviedb'\n")
    # except:
      # index_num = None
    # init_file.close()
    # if index_num is not None:
      # init_list[index_num] = "    'com.plexapp.agents.themoviedb', 'com.plexapp.agents.themoviedb.id'\n"
      # index_num = init_list.index("    elif media.primary_agent == 'com.plexapp.agents.themoviedb':\n")
      # init_list[index_num] = "    elif media.primary_agent == 'com.plexapp.agents.themoviedb' or media.primary_agent == 'com.plexapp.agents.themoviedb.id':"
      # init_file = open(filepath,"w")
      # for i in init_list:
         # init_file.write(i)
      # init_file.close()
############## TMDBTrailer plugin
  filepath = '%s\\Plug-ins\\TMDBTrailer.bundle\\Contents\\Code\\%s' % (home_path, '__init__.py')
  init_file = os.path.isfile(os.path.realpath(os.path.join(os.path.normpath(filepath))))
  if init_file:
    init_file = open(filepath,"r")
    init_list = init_file.readlines()
    try:
      index_num = init_list.index("		'com.plexapp.agents.themoviedb'\n")
    except:
      index_num = None
    init_file.close()
    if index_num is not None:
      init_list[index_num] = "		'com.plexapp.agents.themoviedb', 'com.plexapp.agents.themoviedb.id'\n"
      init_file = open(filepath,"w")
      for i in init_list:
         init_file.write(i)
      init_file.close()
