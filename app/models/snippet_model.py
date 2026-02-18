from sqlalchemy import Column , String , Text , Integer , TIMESTAMP , Index , ForeignKey
from app.databse.db import Base
from sqlalchemy.orm import relationship


class Snippet(Base):

    __tablename__ = "snippets"

    id = Column(Integer , primary_key=True)
    title = Column(String  , nullable=False)
    code = Column(Text , nullable=False)
    owner_id = Column(ForeignKey("users.id") , nullable=False)
    created_at = Column(TIMESTAMP)


    user = relationship("User", back_populates="snippets") 