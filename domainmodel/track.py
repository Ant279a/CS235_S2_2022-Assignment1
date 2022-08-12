from domainmodel.artist import Artist


class Track:

    album = None
    artist = None
    genres = []
    track_duration = None
    track_url = None

    def __init__(self, track_id, title):
        if (not instanceof(track_id, int)):
            raise TypeError()
        else:
            self.__track_id = track_id
            self.title = title
    




    def add_genre(self, genre):
        self.genres.append(genre)

    def __repr__(self):
        return f'<Track {self.title}, track id = {self.__track_id}>'
    def __eq__(self, other):
        return self.__track_id == other.__track_id
    def __lt__(self, other):
        return self.__track_id < other.__track_id
    def __hash__(self):
        return hash(self.__track_id)
    

    

    


