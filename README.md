# TheMovieDB.ID
This agent is based on the original **TheMovieDB** plugin. For the improvement of the code, thanks go to [Reyter](https://github.com/ReyterAK).

The main differences from the original version:
- Added the ability to use the movie ID or TV show instead of the name or in addition to it.
- Added the ability to use ID from [FileBot Xattr Metadata](https://github.com/filebot/plex-agents), for support, installation of this plugin is required.

## Examples
[Avatar](https://www.themoviedb.org/movie/19995-avatar) ID - 19995
It does not matter what the name of the file is, if tmdb-ID is specified in the filepath, then the information will be bound to the ID.

* `\tmdb-19995\1.mkv` = `Avatar (2009)`                                   
* `\we\like\what\tmdb-19995\we\do\Total Recall (1990).m2ts` = `Avatar (2009)`
* `\Scarface (1983) tmdb-19995.mp4` = `Avatar (2009)`                     
Note: standard plex scanners ignore the BDMV folder, so if you store movies in the BDAV/BDMV folder structure, you will have to use a third-party scanner, for example [FileBot Xattr Metadata](https://github.com/filebot/plex-agents) *(this scanner can only work with xattr metadata)*.
