from sqlalchemy import CheckConstraint, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    score = Column(Integer, CheckConstraint("0 <= score >= 5"), nullable=False)
    comment = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("user.id"), ondelete="CASCADE")
    book_id = Column(Integer, ForeignKey("book.id"), ondelete="CASCADE")

    author = relationship("User", back_populates="reviews")
    book = relationship("Book", back_populates="reviews")
