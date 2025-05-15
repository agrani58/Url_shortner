from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import get_db
from ..crud import create_link, get_url

router = APIRouter(prefix="/links")


@router.post("/", response_model=schemas.Link)
def create_link(link: schemas.LinkCreate, db: Session = Depends(get_db)):
    return crud.create_link(db=db, link=link)


@router.get("/{short_code}")
def redirect(short_code: str, db: Session = Depends(get_db)):
    if url := crud.get_url(db, short_code):
        return {"url": url}
    raise HTTPException(status_code=404)
