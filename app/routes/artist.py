from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.seila import top_tracks

router = APIRouter(
    prefix="/artist",
)



@router.get('/')
def spotify_artist_data():
    return JSONResponse(content=top_tracks)