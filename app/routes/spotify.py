from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse, FileResponse
from typing import Union

from app.spotify.artist_data import get_artist_data
from app.parameters import KEYS_TO_EXCLUDE

router = APIRouter(
    prefix="/spotify",
    tags=[
        "spotify"
    ]
)


@router.get("/download")
async def download_excel():
    
    file_path = f"app/archives/model.xlsx"
    
    return FileResponse(file_path, headers={"Content-Disposition": f"attachment; filename=fds"})
    
    
@router.get('/')
def spotify_artist_data(artist_name: str, keys_to_exclude: str = KEYS_TO_EXCLUDE,  artist_country: Union[str, None] = 'BR'):
    
    keys_to_exclude = keys_to_exclude.replace(' ', '').split(',')
    
    artist_data = get_artist_data(artist_name, keys_to_exclude,  artist_country)
    
    if not artist_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Invalid Country!"})
    
    return JSONResponse(content=artist_data)