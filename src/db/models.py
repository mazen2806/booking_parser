import uuid

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()


class HotelEntity(Base):
    __tablename__ = 'property_short_info'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=lambda: uuid.uuid4().hex)
    name = Column(String(100), nullable=False)
    city = Column(String(50), nullable=False)
    score = Column(Float(5, 2), nullable=False)
    stars_count = Column(Integer, nullable=True)
    details_url = Column(String(500), nullable=True)
