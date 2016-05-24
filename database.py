__author__ = 'Unicomcat'
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from . import Base


class Acess_Type:
    FTP = 1
    SSH = 2


class bill_type:
    SCDR = 0x01
    SGWCDR = 0x02
    PGWCDR = 0x04
#define CG class include CG information


class CG(Base):
    __tablename__ = 'cg'
    id = Column(Integer, primary_key= True)
    name = Column(String(20),unique = True)
    access_ip = Column(String(20))
    disk_ip = Column(String(20), default='NULL')
    access_type = Column(Integer)
    bill_tpye = Column(Integer)


class BILL_LIST(Base):
    __tablename__ = 'bill_list'
    id = Column(Integer)


