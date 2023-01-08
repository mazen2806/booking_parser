from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.db import models

DB_URL = 'postgresql://postgres:mysecretpassword@localhost:5432/postgres'


def save_properties(data, city):
    hotels = []
    for value in data:
        h = models.HotelEntity(
            name=value.name,
            score=value.score,
            city=city,
            stars_count=value.stars_count
        )
        hotels.append(h)

    engine = get_engine()
    with Session(engine) as session:
        session.add_all(hotels)
        session.commit()


def get_engine():
    engine = create_engine(DB_URL, echo=True, future=True)
    return engine
