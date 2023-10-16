import requests
from operator import itemgetter


def get_artist_data(artist_name: str, keys_to_exclude: list):

    top_tracks = requests.get(f'https://api.deezer.com/search?q={artist_name}').json()
    
    if 'error' in top_tracks:
        return None
    
    top_tracks = sorted(top_tracks['data'], key=itemgetter('rank'))
    
    artist_id = ''
    
    albums_ids = set()
    
    for items in top_tracks.copy():
        
        albums_ids.add(items['album']['id'])
        
        for item in items.copy():
            for key_exclude in keys_to_exclude:
                if item == key_exclude:
                    items.pop(item)
        
        for key_exclude in keys_to_exclude:
            for item in items['artist'].copy():
                if item == key_exclude:
                    items['artist'].pop(item)
                        
        for key_exclude in keys_to_exclude:
            for item in items['album'].copy():
                if item == key_exclude:
                    items['album'].pop(item)
                        
        
        if items['artist']['name'].upper() == artist_name.upper():
            artist_id = items['artist']['id']
            
    
    artist_data = requests.get(f'https://api.deezer.com/artist/{artist_id}').json()
    
    
    albums_list = []
    
    
    for id in albums_ids:
        albums_data = requests.get(f'https://api.deezer.com/album/{id}').json()
        albums_list.append(albums_data)
    
    
    for albums in albums_list:
    
        for item in albums.copy():
            for key_exclude in keys_to_exclude:
                if item == key_exclude:
                    albums.pop(item)
        
        
        for items in albums['contributors'].copy():
            for item in items.copy():
                for key_exclude in keys_to_exclude:
                    if item == key_exclude:
                        items.pop(item)
                        
                        
        for item in albums['artist'].copy():
            for key_exclude in keys_to_exclude:
                if item == key_exclude:
                    albums['artist'].pop(item)
        
        for items in albums['tracks']['data'].copy():
            for item in items.copy():
                for key_exclude in keys_to_exclude:
                    if item == key_exclude:
                        items.pop(item)
                        
                        
        for items in albums['tracks']['data'].copy():
            for item in items['artist'].copy():
                for key_exclude in keys_to_exclude:
                    if item == key_exclude:
                        items['artist'].pop(item)
                        
                        
        for items in albums['tracks']['data'].copy():
            for item in items['album'].copy():
                for key_exclude in keys_to_exclude:
                    if item == key_exclude:
                        items['album'].pop(item)
    
    
    
    
    formated_artist_data = {
        "artist_data": artist_data,
        "top_tracks": top_tracks,
        "top_albums": albums_list
    }
    
    
    
    return formated_artist_data