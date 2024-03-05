from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy as sqla
import pandas as pd


engine = create_engine('sqlite:///test.db', echo=True)

Base = declarative_base()

class Filme(Base):
    __tablename__ = 'filme'
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    ano_lancamento = Column(Integer)
    pontuacao = Column(Integer)

