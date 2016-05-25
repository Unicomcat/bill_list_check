__author__ = 'Unicomcat'
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from database import CG, BILLLIST
from config import config
Base = declarative_base()
engin = create_engine(config)
