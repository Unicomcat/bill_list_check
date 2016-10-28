__author__ = 'Unicomcat'
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'data-dev.sqlite')



class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'data.sqlite')

config = "sqlite:///" + os.path.join(basedir, 'data.sqlite')
cg_txt = os.path.join(basedir,'cg.txt')