from sqlalchemy import create_engine, Column, Integer, String, MetaData, ForeignKey

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import sqlalchemy as sqla
import pandas as pd
import os


local_path = os.getcwd()

archive = 'demo.db'
engine = create_engine(f'sqlite:///{os.path.join(local_path,archive)}')
engine.begin()

Session = sessionmaker(bind=engine)
Base = declarative_base()
metadata = MetaData()


def remove_table(table, metadata = metadata, engine = engine):
    metadata.reflect(engine)
    tables_disponiveis = metadata.tables
    if table in tables_disponiveis:
        tables_disponiveis[table].drop(engine)