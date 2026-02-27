from sqlalchemy import Column, Integer, String

from app.databse.db import Base


class Test(Base):

    __tablename__ = "TestTable"

    id = Column(Integer, primary_key=True)
    name = Column(Integer, primary_key=True)

    #  testing alembic
    age = Column(Integer, nullable=False)
