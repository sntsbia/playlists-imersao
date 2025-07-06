from pydantic import BaseModel
from typing import Optional

# Propriedades compartilhadas por todos os schemas de playlist
class PlaylistBase(BaseModel):
    name: str
    category: str
    details: str

# Propriedades para receber via API na criação
class PlaylistCreate(PlaylistBase):
    pass

# Propriedades para receber via API na atualização (todos os campos são opcionais)
class PlaylistUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    details: Optional[str] = None

# Propriedades para retornar ao cliente (inclui o ID)
class Playlist(PlaylistBase):
    id: int

    class Config:
        from_attributes = True