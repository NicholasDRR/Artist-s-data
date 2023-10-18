from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse, FileResponse
from typing import Union

from app.spotify.artist_data import get_artist_data
from app.parameters import KEYS_TO_EXCLUDE
from app.file_maker import CreateFile

router = APIRouter(
    prefix="/spotify",
    tags=[
        "spotify"
    ]
)



    
@router.get('/')
def spotify_artist_data(artist_name: str, keys_to_exclude: str = KEYS_TO_EXCLUDE,  artist_country: Union[str, None] = 'BR'):
    """
    Consome a API do Spotify e busca o ***artista*** informado no parâmetro *artist_name* \n
    Retorna os dados tratados de acordo com o que for informado no parâmetro *keys_to_exclude* \n
    O parâmetro *artist_country* é opcional e tem como padrão o valor *BR* mas ao ser utilizado aumenta a precisão da API
    """
    
    keys_to_exclude = keys_to_exclude.replace(' ', '').split(',')
    
    artist_data = get_artist_data(artist_name, keys_to_exclude,  artist_country)
    
    if not artist_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Invalid Country!"})
    
    return JSONResponse(content=artist_data)