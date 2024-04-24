# dependencies.py
from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from configs.config import config
from databases.connection import SessionLocal
from models import Base as BaseModels

engine = create_engine(url=config["DATABASE_URL"], echo=False)

# Bind the engine to the Base class
BaseModels.metadata.bind = engine

# Create the tables
BaseModels.metadata.create_all(engine)


def get_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


SessionDep = Annotated[Session, Depends(get_database)]
