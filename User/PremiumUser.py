from PlayList.PlayList import PlayList
from Searcher.Searcher import Searcher


class PremiumUser:
    def __init__(self, user_name,playlists={}):
        self.playlists = playlists
        self.user_name = user_name
        self.searcher = Searcher
    def add_playlist(self, playlist: PlayList):
        if playlist.name in self.playlists.keys():
            raise PlayListExistsException("this playlist's name is taken")
        else:
            self.playlists[playlist.name] = playlist


class PlayListExistsException(Exception):
    pass


class RestrictedUser(Exception):
    pass