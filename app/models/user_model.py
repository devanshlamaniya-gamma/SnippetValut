from sqlalchemy import Column , Integer , String , Boolean , TIMESTAMP , DefaultClause
from app.databse.db import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class User(Base):

    __tablename__ = "users"

    id = Column(Integer , primary_key=True)
    name = Column(String , nullable=False)
    password = Column(String , nullable=False)
    # hashed_password = Column(String , nullable=False , unique=True)
    is_verfied = Column(Boolean , nullable=False , default=False)
    created_at = Column(TIMESTAMP , nullable=True , default=datetime.now)

    snippet = relationship("Snippet", back_populates="user_model")