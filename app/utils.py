def id_format(artist_id: str) -> str:
    return artist_id.replace('spotify:artist:', '')

def url_format(url, artist_id, find_artist: bool = False, artist_country: str = None) -> str:
    
    if artist_country and not find_artist:
        return url.replace('id', artist_id).replace('country', artist_country)
    
    if find_artist and artist_country:
        return url.replace('artist_name', artist_id).replace('country', artist_country)
    
    return url.replace('id', artist_id)