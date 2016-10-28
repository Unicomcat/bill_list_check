# -*- coding: utf-8 -*-
__author__ = 'unicomcat'
from CG import CG
from database import BillType
from database import database
import time
from database import HUAWEI
#conn = engine.connect()
#insert_cg = cg.insert()
#insert_billlist = billlist.insert()
#def check_ip_address(CG):

database_my = database()
database_my.load_cg_detail()
bill_date = int(time.strftime('%Y%m%d', time.localtime(time.time()-24*60*60)))

for huawei_cg in database_my.session.query(HUAWEI).all():
    print huawei_cg.CG_NAME
    disk_ip = CG.test_disk_ip(huawei_cg.ACCESS_IP,huawei_cg.ACCESS_USERNAME,huawei_cg.OMU_PASSWORD,huawei_cg.CGU_PASSWORD,huawei_cg.DISK_IP1,huawei_cg.DISK_IP2)
    database.session.query(HUAWEI).filter(HUAWEI.id==huawei_cg.id).update({HUAWEI.DISK_IP: disk_ip})
    print disk_ip
    database.session.commit()
    CG_haha = CG(cg_name=huawei_cg.CG_NAME, access_ip=huawei_cg.ACCESS_IP, disk_ip=huawei_cg.DISK_IP,
              access_type='ssh', bill_path1=huawei_cg.BILL_PATH, bill_path2='',
              password1=huawei_cg.OMU_PASSWORD, password2=huawei_cg.CGU_PASSWORD, access_username=huawei_cg.ACCESS_USERNAME,
              bill_type=huawei_cg.BILL_TYPE, bill_date=str(bill_date), cg_type='ATCA')
    CG_haha.get_bill_information()
    CG_haha.write_bill_summary_txt()



#raw_input('press anykey to exit\n')





