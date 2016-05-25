__author__ = 'Unicomcat'
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from . import Base


class AcessType:
    FTP = 1
    SSH = 2


class BillType:
    SCDR = 0x01
    SGWCDR = 0x02
    PGWCDR = 0x04


#define CG class include CG information
class CG(Base):
    __tablename__ = 'cg'
    id = Column(Integer, primary_key=True)
    name = Column(String(10), unique=True)
    access_ip = Column(String(20))
    disk_ip = Column(String(20), default='NULL')
    access_type = Column(Integer)
    bill_tpye = Column(Integer)


#define every bill file's information
class BILLLIST(Base):
    __tablename__ = 'billlist'
    id = Column(Integer, primary_key=True)
    name = Column(String(10))
    bill_tpye = Column(String(10))
    first = Column(String(30))
    last = Column(String(30))
    total_num = Column(Integer)
    data_time = Column(DateTime)


