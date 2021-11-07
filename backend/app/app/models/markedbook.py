from sqlalchemy import Column, ForeignKey, String, Integer, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class BookStatuses:
    LIKED = "liked"
    DISLIKED = "disliked"
    BOUGHT = "bought"


class MarkedBook(Base):
    __tablename__ = "markedbooks"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), index=True)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"), index=True)
    status = Column(String, index=True, nullable=False)
    user = relationship("User", back_populates="markedbooks")
    book = relationship("Book", back_populates="markedbooks")
    __table_args__ = (UniqueConstraint(
        "user_id",
        "book_id",
        name="_unique_together_user_book"
        ),
    )
