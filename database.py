
from sqlalchemy import Column, String, Integer, DateTime, create_engine,exists
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import cg_txt
engine = create_engine('sqlite:///test.sqlite', echo=True)
Base = declarative_base()


class BillType:
    SCDR = 0x01
    SGWCDR = 0x02
    PGWCDR = 0x04
    egwcdr = 0x08


class HUAWEI(Base):
    __tablename__ = 'HUAWEI'
    id = Column(Integer, primary_key=True)
    CG_NAME = Column(String(10), unique=True)
    ACCESS_IP = Column(String(20))
    DISK_IP = Column(String(20))
    DISK_IP1 = Column(String(20))
    DISK_IP2 = Column(String(20))
    BILL_TYPE = Column(Integer)
    ACCESS_USERNAME = Column(String(4))
    OMU_PASSWORD = Column(String(20))
    CGU_PASSWORD = Column(String(20))
    BILL_PATH = Column(String(30))

    def __repr__(self):
        '''return "<Huawei(CG_NAME='%s', ACCESS_IP='%s', DISK_IP1='%s', DISK_IP2='%s', BILL_TYPE='%s',\
        ACCESS_USERNAME='%s', OMU_PASSWORD='%s', CGU_PASSWORD='%s', BILL_PATH='%s')>" %(self.CG_NAME, self.ACCESS_IP,self.DISK_IP1,\
                                                                      self.DISK_IP2,self.BILL_TYPE,self.ACCESS_USERNAME,\
                                                                      self.OMU_PASSWORD,self.CGU_PASSWORD,self.BILL_PATH)'''
        return self.CG_NAME.ljust(15, ' ') + '\t' + str(self.BILL_TYPE).ljust(15, ' ') + '\t' + self.ACCESS_IP.ljust(\
            15, ' ') + '\t' + self.DISK_IP.ljust(15, ' ') +self.DISK_IP1.ljust(15, ' ') + '\t' + self.DISK_IP2.ljust(15, ' ') + '\t' + self.\
            ACCESS_USERNAME.ljust(15, ' ') + '\t' + self.OMU_PASSWORD.ljust(15, ' ') + '\t' + self.CGU_PASSWORD.ljust(\
            15, ' ')+ '\t' + self.BILL_PATH.ljust(15, ' ') + '\n'


class NOKIA(Base):
    __tablename__ = 'NOKIA'
    id = Column(Integer, primary_key=True)
    CG_NAME = Column(String(10), unique=True)
    ACCESS_IP1 = Column(String(20))
    ACCESS_IP2 = Column(String(20))
    BILL_TYPE = Column(Integer)
    ACCESS_USERNAME = Column(String(4))
    PASSWORD = Column(String(20))
    BILL_PATH = Column(String(30))

    def __repr__(self):
        return self.CG_NAME.ljust(15, ' ') + '\t' + str(self.BILL_TYPE).ljust(15, ' ') + '\t' + self.ACCESS_IP1.ljust(\
            20, ' ') + '\t' + self.ACCESS_IP2.ljust(15, ' ') + '\t' + self.ACCESS_USERNAME.ljust(15, ' ') + '\t' +\
               self.PASSWORD.ljust(15,' ') + '\t' + self.BILL_PATH.ljust(15,' ') + '\n'


class ZTE(Base):
    __tablename__ = 'ZTE'
    id = Column(Integer, primary_key=True)
    CG_NAME = Column(String(10), unique=True)
    ACCESS_IP1 = Column(String(20))
    ACCESS_IP2 = Column(String(20))
    BILL_TYPE = Column(Integer)
    ACCESS_USERNAME = Column(String(4))
    PASSWORD = Column(String(20))
    BILL_PATH = Column(String(30))

    def __repr__(self):
        return self.CG_NAME.ljust(15, ' ') + '\t' + str(self.BILL_TYPE).ljust(15, ' ') + '\t' + self.ACCESS_IP1.ljust(\
            20, ' ') + '\t' + self.ACCESS_IP2.ljust(15, ' ') + '\t' + self.ACCESS_USERNAME.ljust(15, ' ') + '\t' + \
               self.PASSWORD.ljust(15, ' ') + '\t' + self.BILL_PATH.ljust(15, ' ') + '\n'


class BILL_SUMMARY(Base):
    __tablename__ = 'BILL_SUMMARY'
    id = Column(Integer, primary_key=True)
    DATE = Column(String(10))
    BEGIN_FILE_NAME = Column(String(20))
    LAST_FILE_NAME = Column(String(20))
    FILE_SIZE = Column(Integer)
    BILL_NUM = Column(String(4))
    BILL_TYPE = Column(String(20))
    CG_NAME = Column(String(10))
    def __repr__(self):
        return "<BILL_SUMMARY (DATE='%s'>" %(self.DATE)


#bill_summary2 = BILL_SUMMARY(DATE='20160522')

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

class database():
#define every bill file's information
    session = Session()
#    def __init__(self):
#        self.print_database_cg('all')

    def add_CG1(self):
        print "this is the first time boot this program,so you should provide base CG information"
        CG_kind = raw_input("first select CG kind 1.HUAWEI 2.ZTE 3.NOKIA")
        CG_NAME = raw_input("please input CG_NAME")
        print CG_NAME
        BILL_TYPE = raw_input("please input BILL_TYPE SCDR = 0x01,SGWCDR = 0x02,PGWCDR = 0x04,egwcdr = 0x08")
        print BILL_TYPE
        if CG_kind == '1':
            ACCESS_IP = raw_input("please input ACCESS_IP")
            print ACCESS_IP
            DISK_IP1 = raw_input("please input DISK_IP1")
            print DISK_IP1
            DISK_IP2 = raw_input("please input DISK_IP2")
            print DISK_IP2
            ACCESS_USERNAME = raw_input("please input ACCESS_USERNAME")
            print ACCESS_USERNAME
            OMU_PASSWORD = raw_input("please input OMU_PASSWORD")
            print OMU_PASSWORD
            CGU_PASSWORD = raw_input("please input CGU_PASSWORD")
            print CGU_PASSWORD
            BILL_PATH = raw_input("please input BILL_PATH")
            print BILL_PATH
            return HUAWEI(CG_NAME=CG_NAME,ACCESS_IP=ACCESS_IP,DISK_IP1=DISK_IP1,DISK_IP2=DISK_IP2,BILL_TYPE=BILL_TYPE,\
                          ACCESS_USERNAME=ACCESS_USERNAME,OMU_PASSWORD=OMU_PASSWORD,CGU_PASSWORD=CGU_PASSWORD,\
                          BILL_PATH=BILL_PATH)
        elif CG_kind == '2' or CG_kind == '3':
            ACCESS_IP1 = raw_input("please input ACCESS_IP1")
            print ACCESS_IP1
            ACCESS_IP2 = raw_input("please input ACCESS_IP2")
            print ACCESS_IP2
            ACCESS_USERNAME = raw_input("please input ACCESS_USERNAME")
            print ACCESS_USERNAME
            PASSWORD = raw_input("please input PASSWORD")
            print PASSWORD
            BILL_PATH = raw_input("BILL_PATH")
            print BILL_PATH
            if CG_kind == '2':
                return ZTE(CG_NAME=CG_NAME, ACCESS_IP1=ACCESS_IP1, ACCESS_IP2=ACCESS_IP2,BILL_TYPE=BILL_TYPE,\
                           ACCESS_USERNAME=ACCESS_USERNAME, PASSWORD=PASSWORD,BILL_PATH=BILL_PATH)
            elif CG_kind == '3':
                return NOKIA(CG_NAME=CG_NAME, ACCESS_IP1=ACCESS_IP1, ACCESS_IP2=ACCESS_IP2,BILL_TYPE=BILL_TYPE,\
                           ACCESS_USERNAME=ACCESS_USERNAME, PASSWORD=PASSWORD,BILL_PATH=BILL_PATH)
            else:
                print "error"
        else:
            print "error"

    def add_CG(self, temp_detail):
        exist_huawei = self.session.query(HUAWEI).filter_by(CG_NAME=temp_detail[1]).all()
        exist_nokia = self.session.query(NOKIA).filter_by(CG_NAME=temp_detail[1]).all()
        exist_zte = self.session.query(ZTE).filter_by(CG_NAME=temp_detail[1]).all()
        if temp_detail[0]=='1'and not exist_huawei:
            cg_instance = HUAWEI(CG_NAME=temp_detail[1],BILL_TYPE=temp_detail[2],ACCESS_IP=temp_detail[3],DISK_IP1=\
                temp_detail[4],DISK_IP2=temp_detail[5],ACCESS_USERNAME=temp_detail[6],OMU_PASSWORD=temp_detail[7],CGU_PASSWORD\
                =temp_detail[8],BILL_PATH=temp_detail[9])
            self.session.add(cg_instance)
            self.session.commit()
        elif temp_detail[0]=='3' and not exist_nokia :
            cg_instance = NOKIA(CG_NAME=temp_detail[1], ACCESS_IP1=temp_detail[3], ACCESS_IP2=temp_detail[4],BILL_TYPE=\
                temp_detail[2],ACCESS_USERNAME=temp_detail[5], PASSWORD=temp_detail[6],BILL_PATH=temp_detail[7])
            self.session.add(cg_instance)
            self.session.commit()
        elif temp_detail[0]=='2' and not exist_zte :
            cg_instance = ZTE (CG_NAME=temp_detail[1], ACCESS_IP1=temp_detail[3], ACCESS_IP2=temp_detail[4],BILL_TYPE=\
                temp_detail[2],ACCESS_USERNAME=temp_detail[5], PASSWORD=temp_detail[6],BILL_PATH=temp_detail[7])
            self.session.add(cg_instance)
            self.session.commit()
        else:
            print temp_detail[1]+' is already exist!!'

    def delete_cg(self, cg_name):
        exist_huawei = self.session.query(HUAWEI).filter_by(CG_NAME=cg_name).first()
        exist_nokia = self.session.query(NOKIA).filter_by(CG_NAME=cg_name).first()
        exist_zte = self.session.query(ZTE).filter_by(CG_NAME=cg_name).first()
        if exist_huawei:
            try:
                self.session.query(HUAWEI).filter(HUAWEI.CG_NAME == cg_name).delete()
                self.session.commit()
            except:
                print "delete failed"
        elif exist_zte:
            try:
                self.session.query(ZTE).filter(ZTE.CG_NAME == cg_name).delete()
                self.session.commit()
            except:
                print "delete failed"
        elif exist_nokia:
            try:
                self.session.query(NOKIA).filter(NOKIA.CG_NAME == cg_name).delete()
                self.session.commit()
            except:
                print "delete failed "
        else:
            print "delete_cg delete failed may be this cg does not exist"

    def mod_cg(self, cg_name):
        cg_huawei = self.session.query(HUAWEI).filter_by(CG_NAME=cg_name).first()
        cg_zte = self.session.query(ZTE).filter_by(CG_NAME=cg_name).first()
        cg_nokia = self.session.query(NOKIA).filter_by(CG_NAME=cg_name).first()
        cg_list = [cg_huawei, cg_zte, cg_nokia]
        for item in cg_list:
            if item != None:
                print item
                if cg_huawei:
                    new_data = raw_input(
                        "please in put data as follow.\n  CG_type|CG_NAME|BILL_TYPE|ACCESS_IP|DISK_IP1|DISK_IP2|ACCESS_USERNAME|OMU_PASSWORD|CGU_PASSWORD|BILL_PATH")
                    try:
                        self.session.query(HUAWEI).filter(HUAWEI.CG_NAME == cg_name).delete()
                        self.session.commit()
                    except:
                        print "delete failed"
                    new_data_list = new_data.split('|')
                    try:
                        self.add_CG(new_data_list)
                        print self.session.query(HUAWEI).filter(HUAWEI.CG_NAME == cg_name).first()
                    except:
                        print "failed your input is something wrong"
                elif cg_zte:
                    new_data = raw_input(
                        "please in put data as follow.\n  CG_type|CG_NAME|BILL_TYPE|ACCESS_IP1|ACCESS_IP2|DISK_IP2|ACCESS_USERNAME|PASSWORD|BILL_PATH")
                    try:
                        self.session.query(ZTE).filter(ZTE.CG_NAME == cg_name).delete()
                        self.session.commit()
                    except:
                        print "delete failed"
                    new_data_list = new_data.split('|')
                    try:
                        self.add_CG(new_data_list)
                        print self.session.query(ZTE).filter(ZTE.CG_NAME == cg_name).first()
                    except:
                        print "failed your input is something wrong"
                elif cg_nokia:
                    new_data = raw_input(
                        "please in put data as follow.\n  CG_type|CG_NAME|BILL_TYPE|ACCESS_IP1|ACCESS_IP2|DISK_IP2|ACCESS_USERNAME|PASSWORD|BILL_PATH")
                    try:
                        self.session.query(NOKIA).filter(NOKIA.CG_NAME == cg_name).delete()
                        self.session.commit()
                    except:
                        print "delete failed"
                    new_data_list = new_data.split('|')
                    self.add_CG(new_data_list)
                    try:
                        self.add_CG(new_data_list)
                        print self.session.query(NOKIA).filter(NOKIA.CG_NAME == cg_name).first()
                    except:
                        print "failed your input is something wrong"
                else:
                    print "so are you kidding me?"
            else:
                pass

    def print_database_cg(self, cmd):
        if cmd == 'all':
            print 'CG_NAME'.ljust(15, ' ') + '\t' + 'BILL_TYPE'.ljust(15, ' ') + '\t' + 'ACCESS_IP'.ljust(\
                15, ' ') + '\t' + 'DISK_IP1'.ljust(15, ' ') + '\t' + 'DISK_IP2'.ljust(15, ' ') + '\t' + 'ACCESS_USERNAME'.\
                ljust(15, ' ') + '\t' + 'OMU_PASSWORD'.ljust(15, ' ') + '\t' + 'CGU_PASSWORD'.ljust(15, ' ')+ '\t' + \
                'BILL_PATH'.ljust(15, ' ') + '\n'
            for member in self.session.query(HUAWEI).all():
                print member
            print 'CG_NAME'.ljust(15, ' ') + '\t' + 'BILL_TYPE'.ljust(15, ' ') + '\t' + 'ACCESS_IP1'.ljust( \
                20, ' ') + '\t' + 'ACCESS_IP2'.ljust(15, ' ') + '\t' + 'ACCESS_USERNAME'.ljust(15, ' ') + '\t' + \
            'PASSWORD'.ljust(15, ' ') + '\t' + 'BILL_PATH'.ljust(15, ' ') + '\n'
            for member in self.session.query(NOKIA).all():
                print member
            for member in self.session.query(ZTE).all():
                print member
        elif cmd == 'ls':
            print self.session.query(HUAWEI.CG_NAME).all()
            print self.session.query(NOKIA.CG_NAME).all()
            print self.session.query(ZTE.CG_NAME).all()
        else:
            print "print_database_cg\n"

    def load_cg_detail(self):
        with open(cg_txt, 'r') as cg_detail:
            for member in cg_detail.read().split('\n'):
                # print member
                temp_detail = []
                for member_detail in member.split('|'):
                    temp_detail.append(member_detail)
                # print temp_detail
                if temp_detail != ['']:
                    try:
                        self.add_CG(temp_detail)
                    except:
                        print "add CG failed. this line is error\n" + member

    #while raw_input("finsh add? yes or no\n")=='no':
    #    CG = add_CG()
    #    print CG
    #    session.add(CG)
    #session.commit()
    #CG_detail = open('CG.txt', 'r')
    #for member in CG_detail.read().split('\n'):
    #    #print member
    #    temp_detail=[]
    #    for member_detail in member.split('|'):
    #        temp_detail.append(member_detail)
    #    #print temp_detail
    #    if temp_detail !=['']:
    #        try:
    #            add_CG(temp_detail)
    #        except:
    #            print "add CG failed. this line is error\n" + member
    #print_database_cg('all')
    #print_database_cg('ls')
    #print_database_cg('mod')
    #delete_cg('CG88')
    #mod_cg('CG11')


    def list_cg_detail(self):
        print self.session.query(HUAWEI).all()





