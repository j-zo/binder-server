from sqlalchemy import Boolean, CheckConstraint, Column, Date, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(40), unique=True, index=True)
    email = Column(String(40), unique=True, index=True, nullable=False)
    hashed_password = Column(String, CheckConstraint("len(password) >= 8"), nullable=False)
    birthday = Column(Date, index=True)
    about = Column(String(250))
    is_author = Column(Boolean, default=False)
    is_superuser = Column(Boolean(), default=False)
    books = relationship("Book", back_populates="author")
    reviews = relationship("Review", back_populates="author")
    markedbooks = relationship("MarkedBook", back_populates="user")
    items = relationship("Item", back_populates="owner")
