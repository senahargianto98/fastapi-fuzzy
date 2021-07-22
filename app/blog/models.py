from sqlalchemy import Column, Integer, String, ForeignKey
from blog.database import Base
from sqlalchemy.orm import relationship

class Test(Base):
    __tablename__ = 'tests'

    id = Column(Integer, primary_key=True, index=True)
    a1 = Column(Integer)
    a2 = Column(Integer)
    hasil = Column(Integer)

class Fuzzy(Base):
    __tablename__ = 'fuzzy'

    id = Column(Integer, primary_key=True, index=True)
    query = Column(String)
    result = Column(String)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
