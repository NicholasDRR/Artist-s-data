from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from app.deezer.artist_data import get_artist_data
from app.parameters import KEYS_TO_EXCLUDE

router = APIRouter(
    prefix="/deezer",
    tags=[
        "deezer"
    ]
)


@router.get('/')
def deezer_artist_data(artist_name: str, keys_to_exclude: str = KEYS_TO_EXCLUDE):

    keys_to_exclude = keys_to_exclude.replace(' ', '').replace('id', '').replace('name', '').split(',')
    
    artist_data = get_artist_data(artist_name, keys_to_exclude)
    
    if not artist_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"msg": "Invalid artist name"})

    return JSONResponse(content=artist_data)