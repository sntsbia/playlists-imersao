from fastapi import FastAPI
from database import engine, Base
from routers.playlists import playlists_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Playlists", 
    description="""
        Esta API fornece endpoints para gerenciar playlists.  
        
        Permite realizar diferentes operações na entidade.
    """, 
    version="1.0.0",
)

app.include_router(playlists_router, tags=["playlists"])