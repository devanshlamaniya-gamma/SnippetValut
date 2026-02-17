from sqlalchemy import Column , Integer , String , Boolean , TIMESTAMP
from app.databse.db import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer , primary_key=True)
    name = Column(String , nullable=False)
    password = Column(String , nullable=False)
    hashed_password = Column(String , nullable=False , unique=True)
    is_verfied = Column(Boolean , nullable=False)
    created_at = Column(TIMESTAMP , nullable=True)