from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Union
import schemas
from models import Playlist as ModelPlaylist
from database import get_db

playlists_router = APIRouter()

@playlists_router.get("/playlists", response_model=List[schemas.Playlist])
def read_playlists(db: Session = Depends(get_db)):
    """
    Retorna uma lista de todos os playlists cadastrados.

    """
    playlists = db.query(ModelPlaylist).all()
    return playlists

@playlists_router.get("/playlists/{playlist_id}", response_model=schemas.Playlist)
def read_playlist(playlist_id: int, db: Session = Depends(get_db)):
    """
    Retorna os detalhes de um playlist específico com base no ID fornecido.

    Args:
        playlist_id: O ID do playlist.

    Raises:
        HTTPException: Se o playlist não for encontrado.
    """
    db_playlist = db.query(ModelPlaylist).filter(ModelPlaylist.id == playlist_id).first()
    if db_playlist is None:
        raise HTTPException(status_code=404, detail="Playlist não encontrado")
    return db_playlist

@playlists_router.post("/playlists", response_model=schemas.Playlist, status_code=201)
def create_playlist(playlist: schemas.PlaylistCreate, db: Session = Depends(get_db)):
    """
    Cria um novo playlist com os dados fornecidos.

    Args:
        playlist: Dados do playlist a ser criado.

    Returns:
        schemas.Playlist: playlist criado.
    """ 
    db_playlist = ModelPlaylist(**playlist.dict()) 
    db.add(db_playlist)
    db.commit()
    db.refresh(db_playlist)
    return db_playlist

@playlists_router.put("/playlists/{playlist_id}", response_model=schemas.Playlist)
def update_playlist(playlist_id: int, playlist: schemas.PlaylistUpdate, db: Session = Depends(get_db)):
    """
    Atualiza os dados de um playlist existente.

    Args:
        playlist_id: O ID do playlist a ser atualizado.
        playlist: Os novos dados (parciais ou completos) do playlist.

    Raises:
        HTTPException: 404 - Playlist não encontrado.

    Returns:
        schemas.Playlist: O playlist atualizado.
    """
    db_playlist = db.query(ModelPlaylist).filter(ModelPlaylist.id == playlist_id).first()
    if db_playlist is None:
        raise HTTPException(status_code=404, detail="Playlist não encontrado")

    for key, value in playlist.dict(exclude_unset=True, exclude_none=True).items():
        setattr(db_playlist, key, value)

    db.commit()
    db.refresh(db_playlist)
    return db_playlist

@playlists_router.delete("/playlists/{playlist_id}", status_code=204)
def delete_playlist(playlist_id: int, db: Session = Depends(get_db)):
    """
    Exclui um playlist.

    Args:
        playlist_id: O ID do playlist a ser excluído.

    Raises:
        HTTPException: 404 - Playlist não encontrado.

    Returns:
        None
    """
    db_playlist = db.query(ModelPlaylist).filter(ModelPlaylist.id == playlist_id).first()
    if db_playlist is None:
        raise HTTPException(status_code=404, detail="Playlist não encontrado")

    db.delete(db_playlist)
    db.commit()
    return
