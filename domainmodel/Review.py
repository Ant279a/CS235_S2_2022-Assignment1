from Album import Album
from Artist import Artist
from Track import Track
import datetime

class Review:
    def __init__(self, track, review_text, rating):
        if not isinstance(track, Track):
            self.__track = None
        else:
            self.__track = track
        if not isinstance(review_text, str) or review_text == "":
            self.__review_text = "N/A"
        else:
            self.__review_text = review_text.strip()
        if not isinstance(rating, int) or rating < 0 or rating > 5:
            raise ValueError()
        self.__rating = rating
        self.__timestamp = datetime.datetime.now()

    @property
    def track(self) -> Track:
        return self.__track
    
    @property
    def review_text(self) -> str:
        return self.__review_text
    
    @property
    def rating(self) -> int:
        return self.__rating
    
    @property
    def timestamp(self) -> datetime:
        return self.__timestamp
    
    @review_text.setter
    def review_text(self, new_review_text):
        if new_review_text == "" or not isinstance(new_review_text, str):
            self.__review_text = "N/A"
        else:
            self.__review_text = new_review_text.strip()
    
    @rating.setter
    def rating(self, new_rating):
        if not isinstance(new_rating, int) or new_rating < 0 or new_rating > 5:
            raise ValueError()
        self.__rating = new_rating
    
    def __repr__(self):
        return f'<Review {self.__review_text}, rating = {self.__rating}>'
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.review_text == other.__review_text and self.rating == other.__rating and self.timestamp == other.__timestamp and self.__track == other.__track
    