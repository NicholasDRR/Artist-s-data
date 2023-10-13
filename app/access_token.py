import requests
import base64

from app.parameters import CLIENT_ID, CLIENT_SECRET

def get_access_token():

    client_id = CLIENT_ID
    client_secret = CLIENT_SECRET
    credentials = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

    auth_options = {
        'url': 'https://accounts.spotify.com/api/token',
        'headers': {
            'Authorization': 'Basic ' + credentials
        },
        'data': {
            'grant_type': 'client_credentials'
        }
    }

    response = requests.post(auth_options['url'], headers=auth_options['headers'], data=auth_options['data']).json()
    
    return response['access_token']


ACCESS_TOKEN = get_access_token()

headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}'
}