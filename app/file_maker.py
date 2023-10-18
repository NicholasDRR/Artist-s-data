import pandas as pd

from app.spotify.artist_data import get_artist_data


class CreateFile:
    
    def __init__(self, artist_name: str, keys_to_exclude: set, artist_country: str):
        self.artist_name = artist_name
        self.keys_to_exclude = keys_to_exclude
        self.artist_country = artist_country
    
    
    def format_data(self):

        artist_data = get_artist_data(self.artist_name, self.keys_to_exclude, self.artist_country)

        artist_list_lines = [['Name', 'Genres','Followers','Album','Tracks','Artists','Popularity','Duration'],]
                
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
            
            artist_list_lines.append(line)
            
        related_artist_list_lines = []
        related_artists_list = []
            
        for artist in artist_data['artists related']['artists']:
            
            line = []
            
            line.append(artist['name'])
            related_artists_list.append(artist['name'])
            line.append(', '.join(artist['genres']))
            line.append(artist['followers']['total'])
            line.append(artist['popularity'])
            line.append(artist['type'])
            
            related_artist_list_lines.append(line)
        

        related_artist_list_lines.sort(key=lambda x: x[3])
        related_artist_list_lines.insert(0, ['Name', 'Genres','Followers','Popularity','Type'])

        return artist_list_lines, related_artist_list_lines, related_artists_list
    
    
    def create_file(self):


        writer = pd.ExcelWriter("app/archives/artist.xlsx")

        artist_list_lines, related_artist_list_lines, related_artists_list = self.format_data()

        df = pd.DataFrame(artist_list_lines)
        df2 = pd.DataFrame(related_artist_list_lines)

        df.columns = df.iloc[0]
        df = df[1:]

        df2.columns = df2.iloc[0]
        df2 = df2[1:]



        df.to_excel(writer, index=False, sheet_name=f'Principal Artist')
        df2.to_excel(writer, index=False, sheet_name=f'Related artists')


        for artist in related_artists_list:
            
            self.artist_name = artist
            
            artist_list_lines, related_artist_list_lines, related_artists_list = self.format_data()
            
            df3 = pd.DataFrame(artist_list_lines)
            
            df3.columns = df3.iloc[0]
            df3 = df3[1:]

            
            df3.to_excel(writer, index=False, sheet_name=f'{artist}')
            


        writer.save()