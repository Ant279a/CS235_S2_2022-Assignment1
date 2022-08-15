

class Album:
    title: str
    artist_id: int
    album_url: str
    album_type: str
    release_year: int

    def __init__(self, album_id, title):
        try:
            if (album_id < 0 or not isinstance(type(album_id), int)):
                raise ValueError("ValueError")
            self.__album_id = album_id
            self.title = title
        except ValueError as e:
            print(e)
    
    def __repr__(self):
        return f'<Album {self.title}, album id = {self.__album_id}>'
    def __eq__(self, other):
        return self.__album_id == other.__album_id
    def __lt__(self, other):
        return self.__album_id < other.__album_id
    def __hash__(self):
        return hash(self.__album_id)
