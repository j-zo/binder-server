from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


book_genre_association = Table("book_genre_association", Base.metadata,
    Column("book_id", ForeignKey("book.id"), primary_key=True),
    Column("genre_id", ForeignKey("genre.id"), primary_key=True)
)


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40), unique=True, index=True, nullable=False)
    small_description = Column(String(250), unique=True, nullable=False)
    big_description = Column(String, unique=True, nullable=False)
    is_blocked = Column(Boolean, default=False)
    author_id = Column(Integer, ForeignKey("user.id"), ondelete="SET NULL")

    genres = relationship("Genre", secondary=book_genre_association, back_populates="books")
    author = relationship("User", back_populates="books")
    reviews = relationship("Review", back_populates="book")
