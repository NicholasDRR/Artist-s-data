from fastapi import APIRouter, HTTPException, status
from fastapi.responses import FileResponse
from typing import Union

from app.parameters import KEYS_TO_EXCLUDE
from app.file_maker import CreateFile

router = APIRouter(
    prefix="/download",
    tags=[
        "download"
    ]
)


@router.get("/download")
async def download_excel(artist_name: str, artist_country: Union[str, None] = 'BR'):
    """
    Consome a API do Spotify e busca o ***artista*** informado no parâmetro *artist_name* \n
    O parâmetro *artist_country* é opcional e tem como padrão o valor *BR* mas ao ser utilizado aumenta a precisão da API \n
    Trata os dados do artista e reformula eles, transformando em um arquivo Excel ***.xlsx*** \n
    Cria um sheet com uma lista dos artistas relacionados ao seu artista com seus principais dados \n
    Cria outro sheet com cada artista relacionado e traz todos os dados tratados
    """
    
    try:
        CreateFile(artist_name, KEYS_TO_EXCLUDE, artist_country).create_file()
        
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail={"msg": f"ERROR!: {error}"})
    
    else:
    
        file_path = f"app/archives/artist.xlsx"
        
        return FileResponse(file_path, headers={"Content-Disposition": f"attachment; filename={artist_name}"})
    