from Review import Review
from Album import Album
from Artist import Artist
from Track import Track

class User:
    def __init__(self, user_id, user_name, password):
        self.__liked_tracks = []
        self.__reviews = []
        if not isinstance(user_id, int) or user_id < 0:
            raise ValueError()
        self.__user_id = user_id
        if not isinstance(user_name, str) or user_name == "":
            self.__user_name = None
        else:
            self.__user_name = (user_name.strip()).lower()
        if not isinstance(password, str) or len(password) < 7:
            self.__password = None
        else:
            self.__password = password

    @property
    def user_id(self) -> int:
        return self.__user_id
    
    @property
    def user_name(self) -> str:
        return self.__user_name
    
    @property
    def password(self) -> str:
        return self.__password
    
    @property
    def liked_tracks(self) -> list:
        return self.__liked_tracks
    
    @property
    def reviews(self) -> list:
        return self.__reviews

    def add_liked_track(self, track) -> None:
        if isinstance(track, Track) and track not in self.__liked_tracks:
            self.__liked_tracks.append(track)
    
    def add_review(self, review) -> None:
        if isinstance(review, Review) and review not in self.__reviews:
            self.__reviews.append(review)

    def remove_liked_track(self, track) -> None:
        if isinstance(track, Track) and track in self.__liked_tracks:
            self.__liked_tracks.remove(track)
    
    def remove_review(self, review) -> None:
        if isinstance(review, Review) and review in self.__reviews:
            self.__reviews.remove(review)
    
    def __repr__(self):
        return f'<User {self.__user_name}, user id = {self.__user_id}>'
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.user_id is other.__user_id
    
    def __hash__(self):
        return hash(self.__user_id)
    
    def __lt__(self, other):
        return self.__user_id < other.__user_id
    
user1 = User(123, 'Shyamli', 'pw12345')
user2 = User(345, 'asma', 'pw67890')
user3 = User(567, 'Daniel', 'pw87465')
album1 = Album(15, 'Justice')
artist1 = Artist(1, 'Tailor Swift')
track1 = Track(1, 'As it Was ')
review1 = Review(track1, 10, 3)
review2 = Review(track1, 9, 4)
user1.add_review(review1)
user1.remove_review(review2)
print(user1.reviews)
    
    