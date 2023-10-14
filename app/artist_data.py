import requests

from app.utils import *
from app.parameters import *
from app.access_token import *


artist_data = requests.get(url=url_format(ARTIST_URL, ARTIST_ID), headers=headers).json()

top_tracks = requests.get(url=url_format(TOP_TRACKS_URL, ARTIST_ID), headers=headers).json()

artist_albums = requests.get(url=url_format(ALBUMS_URL, ARTIST_ID), headers=headers).json()

related_artists = requests.get(url=url_format(RELATED_ARTISTS_URL, ARTIST_ID), headers=headers).json()

keys_to_exclude = {'id', 'images', 'uri', 'href', 'external_urls', 'external_ids', 'is_local', 
                   'preview_url', 'limit', 'next', 'offset', 'previous', 'total', 'album_group',
                   'album_type'}

#TOP TRACKS
tracks_data = []

for album in top_tracks['tracks']:
    
    album_copy = album.copy()
    
    for album_key in album_copy.copy():
        for key_exclude in keys_to_exclude:
            if album_key == key_exclude:
                album.pop(key_exclude)
                
    for album_key in album_copy['album'].copy():
        for key_exclude in keys_to_exclude:
            if album_key == key_exclude:
                album['album'].pop(key_exclude)
    
    for artists in album_copy['album']['artists'].copy():
       for artist in artists.copy():
           for key_exclude in keys_to_exclude:
                if artist == key_exclude:
                    artists.pop(key_exclude)  
       
    for artists in album_copy['artists'].copy():
        for artist in artists.copy():
            for key_exclude in keys_to_exclude:
                if artist == key_exclude:
                    artists.pop(key_exclude)  
    
    tracks_data.append(album)

    

#ALBUMS
albums_data = []

for album in artist_albums.copy():
    for key_exclude in keys_to_exclude:
        if album == key_exclude:
            artist_albums.pop(key_exclude)

for items in artist_albums['items'].copy():
    
    for item in items.copy():
        for key_exclude in keys_to_exclude:
            if item == key_exclude:
                items.pop(key_exclude)
    
    for artists in items['artists'].copy():
        for artist in artists.copy():
            for key_exclude in keys_to_exclude:
                if artist == key_exclude:
                    artists.pop(key_exclude) 
                    


#RELATED ARTISTS

for artists in related_artists['artists'].copy():
    for artist in artists.copy():
        for key_exclude in keys_to_exclude:
            if artist == key_exclude:
                    artists.pop(key_exclude) 

            


formarted_artist_data = {
    "name": artist_data['name'],
    "popularity": artist_data['popularity'],
    "genres": artist_data['genres'],
    "followers": artist_data['followers']['total'],
    "top tracks": tracks_data,
    "albums": artist_albums,
    "artists related": related_artists,
}