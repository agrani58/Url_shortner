from fastapi import FastAPI
from .database import engine, Base
from .routes import links

app = FastAPI(title="URL Shortener")

Base.metadata.create_all(bind=engine)

app.include_router(links.router)
