from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Union
from schemas import Playlist
from models import Playlist as ModelPlaylist
from database import get_db

playlists_router = APIRouter()

@playlists_router.get("/playlists", response_model=List[Playlist])
def read_playlists(db: Session = Depends(get_db)):
    """
    Retorna uma lista de todos os playlists cadastrados.

    """
    playlists = db.query(ModelPlaylist).all()
    return [Playlist.from_orm(playlist) for playlist in playlists]

@playlists_router.get("/playlists/{playlist_id}", response_model=Playlist)
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
    return Playlist.from_orm(db_playlist)

@playlists_router.post("/playlists", response_model=Playlist)
def create_playlist(playlist: Playlist, db: Session = Depends(get_db)):
    """
    Cria um novo playlist com os dados fornecidos.

    Args:
        playlist: Dados do playlist a ser criado.

    Returns:
        Playlist: playlist criado.
    """ 
    db_playlist = ModelPlaylist(**playlist.dict(exclude={"id"})) 
    db.add(db_playlist)
    db.commit()
    db.refresh(db_playlist)
    return Playlist.from_orm(db_playlist)

@playlists_router.put("/playlists/{playlist_id}", response_model=Playlist)
def update_playlist(playlist_id: int, playlist: Playlist, db: Session = Depends(get_db)):
    """
    Atualiza os dados de um playlist existente.

    Args:
        playlist_id: O ID do playlist a ser atualizado.
        playlist: Os novos dados do playlist.

    Raises:
        HTTPException: 404 - Playlist não encontrado.

    Returns:
        Playlist: O playlist atualizado.
    """
    db_playlist = db.query(ModelPlaylist).filter(ModelPlaylist.id == playlist_id).first()
    if db_playlist is None:
        raise HTTPException(status_code=404, detail="Playlist não encontrado")

    for key, value in playlist.dict(exclude_unset=True).items():
        setattr(db_playlist, key, value)

    db.commit()
    db.refresh(db_playlist)
    return Playlist.from_orm(db_playlist)

@playlists_router.delete("/playlists/{playlist_id}", response_model=Playlist)
def delete_playlist(playlist_id: int, db: Session = Depends(get_db)):
    """
    Exclui um playlist.

    Args:
        playlist_id: O ID do playlist a ser excluído.

    Raises:
        HTTPException: 404 - Playlist não encontrado.

    Returns:
        Playlist: O playlist excluído.
    """
    db_playlist = db.query(ModelPlaylist).filter(ModelPlaylist.id == playlist_id).first()
    if db_playlist is None:
        raise HTTPException(status_code=404, detail="Playlist não encontrado")

    playlist_deletado = Playlist.from_orm(db_playlist)

    db.delete(db_playlist)
    db.commit()
    return playlist_deletado
