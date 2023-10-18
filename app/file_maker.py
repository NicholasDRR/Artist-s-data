import pandas as pd

from spotify.artist_data import get_artist_data
from parameters import KEYS_TO_EXCLUDE


artist_data = get_artist_data('derek', KEYS_TO_EXCLUDE,  'BR')

list_lines = [['Name', 'Genres','Followers','Album','Tracks','Artists','Popularity','Duration'],]

        
for artists in artist_data['top tracks']:
    
    artists_track = []
    
    line = []
    
    for artist in artists['artists']:
        artists_track.append(artist['name'])
    
    line.append(artist_data['name'])
    
    line.append(', '.join([genre for genre in artist_data['genres']]))
    
    line.append(artist_data['followers'])
    
    line.append(artists['album']['name'])
    
    line.append(artists['name'])
    
    line.append(', '.join(artists_track))
    
    line.append(artists['popularity'])
    
    line.append(artists['duration_ms'])
    
    list_lines.append(line)


df = pd.DataFrame(list_lines)

df.columns = df.iloc[0]
df = df[1:]


df.to_excel(f"archives/{artist_data['name']}.xlsx", index=False)
