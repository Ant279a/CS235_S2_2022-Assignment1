class Artist:
    def __init__(self, artist_id: int, full_name: str):
        if artist_id < 0 or not instanceof(artist_id, int):
            raise ValueError("Artist id must be a positive integer") 
        self.__artist_id: int = artist_id
        self.__full_name = None

    @property
    def artist_id(self) -> int:
        return self.__artist_id

    @property
    def full_name(self) -> str:
        return self.__full_name

    @full_name.setter
    def full_name(self, new_full_name):
        if new_full_name == "" or not instanceof(new_full_name, str):
            self.__full_name = None
        else:
            self.__full_name = new_full_name

    def __repr__(self):
        # we use access via the property here
        return f"<Artist {self.full_name}, artist id = {self.artist_id}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.artist_id == other.artist_id

    def __lt__(self, other):
        return self.artist_id < other.artist

    def __hash__(self):
        return hash(self.artist_id)
