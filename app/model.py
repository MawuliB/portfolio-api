from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSON
from config import Base


class User(Base):
    __tablename__ = "user"

    name = Column(String)
    email = Column(String, primary_key=True)
    username = Column(String)
    socials = Column(JSON)
    data = Column(JSON)
