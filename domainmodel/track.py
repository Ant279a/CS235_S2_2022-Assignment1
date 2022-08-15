from Artist import Artist
from Album import Album

class Track:
    def __init__(self, track_id, title):
        if not isinstance(track_id, int) or track_id < 0:
            raise ValueError()
        self.__track_id = track_id
        if not isinstance(title, str) or title == "":
            self.title = None
        else:
            self.title = title.strip()
        self.__genres = []
        self.__artist = None
        self.__album = None
        self.__track_duration = None
        self.__track_url = None
    
    @property
    def track_id(self) -> int:
        return self.__track_id
    
    @property
    def title(self) -> str:
        return self.__title

    @property
    def album(self) -> Album:
        return self.__album
    
    @property
    def artist(self) -> Artist:
        return self.__artist
    
    @property
    def genres(self) -> list:
        return self.__genres
    
    @property
    def track_url(self) -> str:
        return self.__track_url
    
    @property
    def track_duration(self) -> int:
        return self.__track_duration
    
    @title.setter
    def title(self, new_title):
        if new_title == "" or not isinstance(new_title, str):
            self.__title = None
        else:
            self.__title = new_title.strip()
    
    @album.setter
    def album(self, new_album):
        if not isinstance(new_album, Album):
            self.__album = None
        self.__album = new_album
    
    @artist.setter
    def artist(self, new_artist):
        if not isinstance(new_artist, Artist):
            self.__artist = None
        self.__artist = new_artist
    
    @track_duration.setter
    def track_duration(self, new_track_duration):
        if not isinstance(new_track_duration, int) or new_track_duration < 0:
            raise ValueError()
        else:
            self.__track_duration = new_track_duration
    
    @track_url.setter
    def track_url(self, new_track_url):
        if new_track_url == "" or not isinstance(new_track_url, str):
            self.__track_url = None
        else:
            self.__track_url = new_track_url

    def __repr__(self):
        return f'<Track {self.__title}, track id = {self.__track_id}>'
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__track_id == other.__track_id
    def __lt__(self, other):
        return self.__track_id < other.__track_id
    def __hash__(self):
        return hash(self.__track_id)