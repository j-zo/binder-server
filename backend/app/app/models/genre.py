from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40), unique=True, index=True, nullable=False)
    description = Column(String, unique=True, nullable=False)
    books = relationship("Book", secondary=book_genre_association, back_populates="genres")
