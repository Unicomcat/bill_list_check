# -*- coding: utf-8 -*-
__author__ = 'unicomcat'
from CG import CG
from database import BillType
from database import database
import time
from database import HUAWEI,NOKIA,ZTE
#conn = engine.connect()
#insert_cg = cg.insert()
#insert_billlist = billlist.insert()
#def check_ip_address(CG):

database_my = database()
database_my.load_cg_detail()
#bill_date = time.strftime('%Y%m%d', time.localtime(time.time()-24*60*60*2))

for i in range(1,8):
    bill_date = time.strftime('%Y%m%d', time.localtime(time.time() - 24 * 60 * 60 * i))
    for huawei_cg in database_my.session.query(HUAWEI).all():
        print huawei_cg.CG_NAME
        disk_ip = CG.test_disk_ip(huawei_cg.ACCESS_IP,huawei_cg.ACCESS_USERNAME,huawei_cg.OMU_PASSWORD,huawei_cg.CGU_PASSWORD,huawei_cg.DISK_IP1,huawei_cg.DISK_IP2)
        database.session.query(HUAWEI).filter(HUAWEI.id==huawei_cg.id).update({HUAWEI.DISK_IP: disk_ip})
        print disk_ip
        database.session.commit()
        CG_haha = CG(cg_name=huawei_cg.CG_NAME, \
                     access_ip=huawei_cg.ACCESS_IP, \
                     disk_ip=huawei_cg.DISK_IP,
                     access_type='ssh', \
                     bill_path1=huawei_cg.BILL_PATH,\
                     bill_path2='',
                     password1=huawei_cg.OMU_PASSWORD, \
                     password2=huawei_cg.CGU_PASSWORD,\
                     access_username=huawei_cg.ACCESS_USERNAME,
                     bill_type=huawei_cg.BILL_TYPE,\
                     bill_date=bill_date, \
                     cg_type='ATCA')
        CG_haha.get_bill_information()
        CG_haha.write_bill_summary_txt()

    for nokia_cg in database_my.session.query(NOKIA).all():
        CG_haha = CG(cg_name=nokia_cg.CG_NAME,\
                     access_ip=nokia_cg.ACCESS_IP1,\
                     access_type='ssh',\
                     bill_type='',\
                     bill_date=bill_date,\
                     access_username=nokia_cg.ACCESS_USERNAME,\
                     bill_path1=nokia_cg.BILL_PATH,\
                     password1=nokia_cg.PASSWORD,\
                     cg_type='Nokia',\
                     disk_ip='',\
                     bill_path2='',\
                     password2='')
        CG_haha.get_bill_information()
        CG_haha.write_bill_summary_txt()

    for zte_cg in database_my.session.query(ZTE).all():
        CG_haha = CG(cg_name=zte_cg.CG_NAME,\
                     access_ip=zte_cg.ACCESS_IP1,\
                     access_type='ssh',\
                     bill_type='',\
                     bill_date=bill_date,\
                     access_username=zte_cg.ACCESS_USERNAME,\
                     bill_path1=zte_cg.BILL_PATH,\
                     password1=zte_cg.PASSWORD,\
                     cg_type='Nokia',\
                     disk_ip='',\
                     bill_path2='',\
                     password2='')
        CG_haha.get_bill_information()
        CG_haha.write_bill_summary_txt()


#raw_input('press anykey to exit\n')





