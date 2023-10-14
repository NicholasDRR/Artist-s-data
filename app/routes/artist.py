from fastapi import APIRouter
from fastapi.responses import JSONResponse

from spotify.artist_data import formarted_artist_data

router = APIRouter(
    prefix="/artist",
)


@router.get('/')
def spotify_artist_data():
    return JSONResponse(content=formarted_artist_data)