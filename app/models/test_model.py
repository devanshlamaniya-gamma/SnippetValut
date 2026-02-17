from sqlalchemy import Column , String , Integer
from app.databse.db import Base

class Test(Base):

    __tablename__ = "TestTable"

    id = Column(Integer,primary_key=True)
    name = Column(Integer , primary_key=True)

    # add to use and test alembic
    age = Column(Integer,nullable=False)