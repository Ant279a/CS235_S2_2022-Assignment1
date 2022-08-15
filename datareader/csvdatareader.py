import os
import csv
import ast
from Album import Album
from Artist import Artist
from Track import Track
from Genre import Genre


class TrackCSVReader:

    def __init__(self, albums_csv_file: str, tracks_csv_file: str):
        if os.path.exists(f"./{albums_csv_file}"):
            self.albums_csv_file = albums_csv_file
        else:
            self.__albums_csv_file = None
        if os.path.exists(f"./{tracks_csv_file}"):
            self.tracks_csv_file = tracks_csv_file
        else:
            self.__tracks_csv_file = None

        self.__dataset_of_tracks = []
        # Set of unique artists
        self.__dataset_of_artists = set()
        # Set of unique albums
        self.__dataset_of_albums = set()
        # Set of unique genres
        self.__dataset_of_genres = set()

    @property
    def dataset_of_tracks(self) -> list:
        return self.__dataset_of_tracks

    @property
    def dataset_of_albums(self) -> set:
        return self.__dataset_of_albums

    @property
    def dataset_of_artists(self) -> set:
        return self.__dataset_of_artists

    @property
    def dataset_of_genres(self) -> set:
        return self.__dataset_of_genres

    def read_csv_files(self):
        # Reading albums csv file
        with open("./{tracks_csv_file}.csv", encoding = 'ISO-8859-1') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                # Setting variables to create Album object
                album_id = int(row['album_id'])
                title = row['album_title']

                # Creating album object
                current_album = Album(album_id, title)

                # Setting fields of Album object
                try:
                    current_album.album_url = row['album_url']
                    current_album.album_type = row['album_type']
                    current_album.release_year = int(row['album_year_released'])
                except:
                    pass

                # Adding album to dataset_of_albums checking it's unique
                if current_album not in self.__dataset_of_albums:
                    self.__dataset_of_albums.add(current_album)

        # Reading tracks csv file
        with open("./{tracks_csv_file}.csv", encoding = 'ISO-8859-1') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:

                # Setting variables to create Artist object
                artist_id = int(row['artist_id'])
                full_name = row['artist_name']

                # Creating artist object
                current_artist = Artist(artist_id, full_name)

                # Adding artist to dataset_of_artists checking if it's unique
                if current_artist not in self.__dataset_of_artists:
                    self.__dataset_of_artists.add(current_artist)
                
                # Setting up loop to catch empty genres field
                try:
                    genres_column = ast.literal_eval(row['track_genres'])
                    current_genres_list = []

                    # Looping through lists in genres column
                    for i in genres_column:
                        genre_id = int(row['genre_id'])
                        genre_name = row['genre_title']

                        # Creating genre object
                        current_genre = Genre(genre_id, genre_name)

                        # Adding genre to current_genres_list checking if it's unique
                        if current_genre not in current_genres_list:
                            current_genres_list.append(current_genre)
                        
                        # Adding genre to dataset_of_genres checking if it's unique
                        if current_genre not in self.__dataset_of_genres:
                            self.__dataset_of_genres.add(current_genre)
                except SyntaxError:
                    pass

                # Creating variables for Track object
                track_id = int(row['track_id'])
                title = row['track_title']

                # Creating current Track object
                current_track = Track(track_id, title)

                # Setting fields of Track object
                try:
                    current_track.track_url = row['track_url']
                    current.track_duration = int(row['track_duration'])
                    current.track_album = Album(int(row['album_id']), row['album_title'])
                    current.track_artist = current_artist
                    current.track_genres = current_genres_list
                except ValueError:
                    pass
                
                # Adding track to dataset_of_tracks checking if it's unique
                if current_track not in self.__dataset_of_tracks:
                    self.__dataset_of_tracks.append(current_track)
                
            


                    
