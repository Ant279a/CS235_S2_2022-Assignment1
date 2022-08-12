
class Genre:

    name: str
    __genre_id: int
    

    def __init__(self, genre_id, genre_name):
        try:
            if (genre_id < 0 or not instanceof(genre_id, int)):
                raise ValueError("ValueError")
            self.__genre_id = genre_id
            self.__genre_name = genre_name
        except ValueError as e:
            print(e)
    
    def __repr__(self):
        return f'<Genre {self.__genre_name}, genre id = {self.__genre_id}>'
    def __eq__(self, other):
        return self.__genre_id == other.__genre_id
    def __lt__(self, other):
        return self.__genre_id < other.__genre_id
    def __hash__(self):
        return hash(self.__genre_id)
    
    