import secrets
import string
from sqlalchemy.orm import Session
from . import models, schemas


def generate_short_code(length=8):
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def create_link(db: Session, link: schemas.LinkCreate):
    short_code = generate_short_code()  # generates a random code
    db_link = models.Link(original_url=link.original_url, short_code=short_code)
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link


def get_url(db: Session, short_code: str):
    link = db.query(models.Link).filter(models.Link.short_code == short_code).first()
    if link:
        return link.original_url
    return None
