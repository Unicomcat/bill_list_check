#coding:utf-8
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, DateTime
#from database import CG, BILLLIST
from config import config
#Base = declarative_base()
engine = create_engine(config)
metadata = MetaData()
# 定义表
cg = Table('cg', metadata,
        Column('id', Integer, primary_key= True),
        Column('name', String(20),unique = True),
        Column('access_ip', String(40)),
        Column('disk_ip', String(40),default='NULL'),
        Column('access_type', Integer),
        Column('bill_tpye', Integer),
        Column('bill_path1', String(40)),
        Column('bill_path2', String(40)),
        Column('password1',String(20)),
        Column('password2',String(20))
    )

billlist = Table('billlist', metadata,
        Column('id', Integer, primary_key=True),
        Column('name',String(20),unique = True),
        Column('bill_tpye', String(10)),
        Column('first_bill', String(30)),
        Column('last_bill', String(30)),
        Column('total_num', Integer),
        Column('total_size', Integer),
        Column('data_time', DateTime)
    )
# 创建数据表，如果数据表存在，则忽视
metadata.create_all(engine)
# 获取数据库连接







