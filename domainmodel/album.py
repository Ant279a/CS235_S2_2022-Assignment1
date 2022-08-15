class Album:
    def __init__(self, album_id, title):
        if not isinstance(album_id, int) or album_id < 0:
            raise ValueError()
        self.__album_id = album_id
        if not isinstance(title, str) or title == "":
            self.title = None
        else:
            self.title = title.strip()
        self.album_url = None
        self.album_type = None
        self.release_year = None
    
    @property
    def album_id(self) -> int:
        return self.__album_id
    
    @property
    def title(self) -> str:
        return self.__title
    
    @property
    def album_url(self) -> str:
        return self.__album_url
    
    @property
    def album_type(self) -> str:
        return self.__album_type
    
    @property
    def release_year(self) -> int:
        return self.__release_year

    @title.setter
    def title(self, new_title):
        if new_title == "" or not isinstance(new_title, str):
            self.__title = None
        else:
            self.__title = new_title.strip()
    
    @album_url.setter
    def album_url(self, new_album_url):
        if new_album_url == "" or not isinstance(new_album_url, str):
            self.__album_url = None
        else:
            self.__album_url = new_album_url
    
    @album_type.setter
    def album_type(self, new_album_type):
        if new_album_type == "" or not isinstance(new_album_type, str):
            self.__album_type = None
        else:
            self.__album_type = new_album_type
    
    @release_year.setter
    def release_year(self, new_release_year):
        if new_release_year == "" or not isinstance(new_release_year, int):
            self.__release_year = None
        else:
            self.__release_year = new_release_year
    
    def __repr__(self):
        return f'<Album {self.title}, album id = {self.__album_id}>'
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.album_id == other.__album_id
    def __lt__(self, other):
        return self.__album_id < other.__album_id
    def __hash__(self):
        return hash(self.__album_id)