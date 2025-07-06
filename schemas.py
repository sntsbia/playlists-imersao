from pydantic import BaseModel
from typing import List


class Playlist(BaseModel):
    name: str
    category: str
    details: str
    class Config:
        from_attributes = True

Playlists = List[Playlist]