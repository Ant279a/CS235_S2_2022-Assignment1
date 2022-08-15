class Genre:
    def __init__(self, genre_id, genre_name):
        if (not isinstance(genre_id, int) or genre_id < 0):
            raise ValueError()
        self.__genre_id = genre_id
        if (not isinstance(genre_name, str) or genre_name == ""):
            self.name = None
        else:
            self.name = genre_name.strip()
    
    @property
    def genre_id(self) -> int:
        return self.__genre_id
    
    @property
    def name(self) -> str:
        return self.__genre_name
    
    @name.setter
    def name(self, new_genre_name):
        if new_genre_name == "" or not isinstance(new_genre_name, str):
            self.__genre_name = None
        else:
            self.__genre_name = new_genre_name.strip()
    
    def __repr__(self):
        return f'<Genre {self.__genre_name}, genre id = {self.__genre_id}>'
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.genre_id == other.__genre_id
    def __lt__(self, other):
        return self.__genre_id < other.__genre_id
    def __hash__(self):
        return hash(self.__genre_id)