# TheMovieDB.ID
This agent is based on the original **TheMovieDB** plugin. For the improvement of the code, thanks go to [Reyter](https://github.com/ReyterAK).

The main differences from the original version:
- Added the ability to use the ID from movie or TV show, instead of the name or in addition to it.
- Added the ability to use ID from [FileBot Xattr Metadata](https://github.com/IIeTp/Filebot-Xattr-Scanners-ID), for support, installation of this plugin is required.

Added support for the following third party plugins:
- CineMaterial
- Fanart.tv
- OpenSubtitles.org
- Plex Movie

## Examples
[Avatar](https://www.themoviedb.org/movie/19995-avatar) tmdb-ID = 19995, [Avatar](https://www.imdb.com/title/tt0499549/) imdb-id = tt0499549
It does not matter what the name of the file is, if tmdb-ID is specified in the filepath, then the information will be bound to the ID.
Pattern: tmdb-00000 or tt00000

* `\tmdb-19995\1.mkv` = `Avatar (2009)`                                   
* `\we\like\what\tmdb-19995\we\do\Total Recall (1990).m2ts` = `Avatar (2009)`
* `\Scarface (1983) tmdb-19995.mp4` = `Avatar (2009)`                     
* `\Avengers. Endgame (2019) tt0499549.avi` = `Avatar (2009)`       
Note: standard plex scanners ignore the BDMV folder, so if you store movies in the BDAV/BDMV folder structure, you will have to use a third-party scanner, for example [FileBot Xattr Metadata](https://github.com/filebot/plex-agents) *(this scanner can only work with xattr metadata)*.

## Install
1. If you want to install the agent manually or if you are interested in the source code, you can download the latest copy of the agent from Github: [releases](https://github.com/IIeTp/TheMovieDB.ID.bundle/releases)
2. Move TheMovieDB.ID.bundle to the default plugins folder. [FAQ](https://support.plex.tv/articles/202915258-where-is-the-plex-media-server-data-directory-located/)            
   `%LOCALAPPDATA%\Plex Media Server\Plug-ins` for Windows Vista/7/8/10
   
