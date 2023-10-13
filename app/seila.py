import requests

from app.utils import *
from app.parameters import *
from app.access_token import *


artist_data = requests.get(url=url_format(ARTIST_URL, ARTIST_ID), headers=headers).json()

top_tracks = requests.get(url=url_format(TOP_TRACKS_URL, ARTIST_ID), headers=headers).json()

artist_albums = requests.get(url=url_format(ALBUMS_URL, ARTIST_ID), headers=headers).json()

related_artists = requests.get(url=url_format(RELATED_ARTISTS_URL, ARTIST_ID), headers=headers).json()


formarted_artist_data = {
    "name": artist_data['name'],
    "popularity": artist_data['popularity'],
    "genres": artist_data['genres'],
    "followers": artist_data['followers']['total'],
    "top_tracks": {},
    
}
