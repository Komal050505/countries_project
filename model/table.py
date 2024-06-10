from sqlalchemy import Column, String, Integer, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Countries(Base):
    __tablename__ = "countries"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(50))
    capital = Column("capital", String(100))
    population = Column("population", String(100))

