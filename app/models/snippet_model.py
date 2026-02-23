from sqlalchemy import TIMESTAMP, Column, ForeignKey, Index, Integer, String, Text
from sqlalchemy.orm import relationship

from app.databse.db import Base


class Snippet(Base):

    __tablename__ = "snippets"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    code = Column(Text)
    language = Column(String, nullable=False)
    owner_id = Column(ForeignKey("users.id"), nullable=False)
    created_at = Column(TIMESTAMP)

    user = relationship("User", back_populates="snippets")
