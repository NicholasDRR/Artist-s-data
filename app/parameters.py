import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')

CLIENT_SECRET=os.getenv('CLIENT_SECRET')

ARTIST_ID = '2kCcBybjl3SAtIcwdWpUe3'

ARTIST_URL = 'https://api.spotify.com/v1/artists/id'

TOP_TRACKS_URL = 'https://api.spotify.com/v1/artists/id/top-tracks?market=UA'

ALBUMS_URL = 'https://api.spotify.com/v1/artists/2kCcBybjl3SAtIcwdWpUe3/albums?market=UA&limit=50'

RELATED_ARTISTS_URL = 'https://api.spotify.com/v1/artists/id/related-artists'