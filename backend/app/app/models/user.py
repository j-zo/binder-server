from sqlalchemy import Boolean, Column, Date, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(40), unique=True, index=True, nullable=False)
    email = Column(String(40), unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    birthday = Column(Date, nullable=False, index=True)
    about = Column(String(250))
    is_author = Column(Boolean, index=True, default=False)
    books = relationship("Book", back_populates="author")
    reviews = relationship("Review", back_populates="author")
    markedbooks = relationship("MarkedBook", back_populates="user")

