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


@router.get("/download")
async def download_excel(artist_name: str, keys_to_exclude: str = KEYS_TO_EXCLUDE, artist_country: Union[str, None] = 'BR'):
    
    try:
        CreateFile(artist_name, keys_to_exclude, artist_country).create_file()
        
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail={"msg": f"ERROR!: {error}"})
    
    else:
    
        file_path = f"app/archives/artist.xlsx"
        
        return FileResponse(file_path, headers={"Content-Disposition": f"attachment; filename={artist_name}"})
    
    
@router.get('/')
def spotify_artist_data(artist_name: str, keys_to_exclude: str = KEYS_TO_EXCLUDE,  artist_country: Union[str, None] = 'BR'):
    
    keys_to_exclude = keys_to_exclude.replace(' ', '').split(',')
    
    artist_data = get_artist_data(artist_name, keys_to_exclude,  artist_country)
    
    if not artist_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Invalid Country!"})
    
    return JSONResponse(content=artist_data)