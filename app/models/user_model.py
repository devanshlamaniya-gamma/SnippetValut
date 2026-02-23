from datetime import datetime

from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, Text
from sqlalchemy.orm import relationship

from app.databse.db import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(Text, nullable=False)
    # hashed_password = Column(String , nullable=False , unique=True)
    is_verfied = Column(Boolean, nullable=False, default=False)
    created_at = Column(TIMESTAMP, nullable=True, default=datetime.now)

    snippets = relationship("Snippet", back_populates="user")
