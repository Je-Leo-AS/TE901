from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy as sqla
import pandas as pd
import os


local_path = os.getcwd()

archive = 'test.db'
engine = create_engine(f'sqlite:///{os.path.join(local_path,archive)}', echo=True)

Base = declarative_base()
