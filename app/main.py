from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.spotify import router as router_spotify
from app.routes.deezer import router as router_deezer

app = FastAPI()


origins = [
    "http://localhost"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router_spotify)
app.include_router(router_deezer)