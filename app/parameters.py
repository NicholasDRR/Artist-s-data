import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')

CLIENT_SECRET=os.getenv('CLIENT_SECRET')

FIND_ARTIST_URL = 'https://api.spotify.com/v1/search?q=artist_name&type=artist&market=country&limit=1'

ARTIST_URL = 'https://api.spotify.com/v1/artists/id'

TOP_TRACKS_URL = 'https://api.spotify.com/v1/artists/id/top-tracks?market=country'

ALBUMS_URL = 'https://api.spotify.com/v1/artists/id/albums?market=country&limit=50'

RELATED_ARTISTS_URL = 'https://api.spotify.com/v1/artists/id/related-artists'

KEYS_TO_EXCLUDE = 'id, link, images, uri, href, external_urls, external_ids, is_local, preview_url, limit, next, offset, previous, total, album_group, album_type'