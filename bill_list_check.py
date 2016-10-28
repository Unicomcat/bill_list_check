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

#bill_date = raw_input(u'输入需要统计的日期，如2016年5月23日，则输入20160523\n')
#CG12 = CG(cg_name='CG12', access_ip='192.40.1.10', disk_ip='172.16.128.8',
#          access_type='ssh', bill_path1='/var/igwb/backsave/', bill_path2='/var/igwb/backsave/R6/first/',
#          password1='cnp200@HW', password2='cnp200@HW' ,access_username='root',
#          bill_type=BillType.SCDR | BillType.PGWCDR | BillType.SGWCDR, bill_date=bill_date,cg_type='ATCA')
#Nokia_CG = CG(cg_name='Nokia_CG',access_ip='192.40.2.72',access_type='ssh', bill_type='pgwcdr',
#              bill_date=bill_date,access_username='root',bill_path1='/cdr/work/proc_raw/proc/archive/',
#              password1='siemens',cg_type='Nokia',disk_ip='',bill_path2='',password2='')
#CG13 = CG(cg_name='CG13', access_ip='192.40.1.13', disk_ip='172.16.128.24',
#          access_type='ssh', bill_path1='/var/igwb/backsave/', bill_path2='/var/igwb/backsave/R6/first/',
#          password1='cnp200@HW', password2='cnp200@HW' ,access_username='root',
#          bill_type=BillType.SCDR | BillType.PGWCDR | BillType.SGWCDR, bill_date=bill_date,cg_type='ATCA')
#
#CG11 = CG(cg_name='CG11', access_ip='132.151.148.8', disk_ip='172.16.128.8',
#          access_type='ssh', bill_path1='/var/igwb/backsave/', bill_path2='/var/igwb/backsave/R6/first/',
#          password1='huawei', password2='huawei' ,access_username='root',
#          bill_type= BillType.PGWCDR | BillType.SGWCDR, bill_date=bill_date,cg_type='ATCA')
#
#CG9 = CG(cg_name='CG9', access_ip='192.40.1.20', disk_ip='172.16.128.24',
#          access_type='ssh', bill_path1='/var/igwb/backsave/', bill_path2='/var/igwb/backsave/R6/first/',
#          password1='huawei', password2='huawei' ,access_username='root',
#          bill_type= BillType.PGWCDR | BillType.SGWCDR, bill_date=bill_date,cg_type='ATCA')
#
#CG8 = CG(cg_name='CG8', access_ip='132.151.148.27', disk_ip='172.16.128.24',
#          access_type='ssh', bill_path1='/var/igwb/backsave/', bill_path2='/var/igwb/backsave/R6/first/',
#          password1='huawei', password2='huawei' ,access_username='root',
#          bill_type=BillType.SCDR | BillType.PGWCDR | BillType.SGWCDR, bill_date=bill_date,cg_type='ATCA')
#
#CG10 = CG(cg_name='CG8', access_ip='132.151.148.27', disk_ip='172.16.128.32',
#         access_type='ssh', bill_path1='/var/igwb/backsave/', bill_path2='/var/igwb/backsave/R6/first/',
#         password1='huawei', password2='huawei' ,access_username='root',
#         bill_type=BillType.SCDR, bill_date=bill_date,cg_type='ATCA')

#CG12 = CG(cg_name='CG12', access_ip='192.40.1.10', disk_ip='172.16.128.8',
#          access_type='ssh', bill_path1='/var/igwb/backsave/', bill_path2='/var/igwb/backsave/R6/first/',
#          password1='cnp200@HW', password2='cnp200@HW' ,access_username='root',
#          bill_type=BillType.SCDR | BillType.PGWCDR | BillType.SGWCDR, bill_date=bill_date,cg_type='ATCA')
#


#Nokia_CG.get_bill_information()
#Nokia_CG.write_bill_summary_txt()
#CG13.get_bill_information()
#CG13.write_bill_summary_txt()
#CG12.get_bill_information()
#CG12.write_bill_summary_txt()
#CG11.get_bill_information()
#CG11.write_bill_summary_txt()
#CG9.get_bill_information()
#CG9.write_bill_summary_txt()
#CG8.get_bill_information()
#CG8.write_bill_summary_txt()
#CG10.get_bill_information()
#CG10.write_bill_summary_txt()

#raw_input('press anykey to exit\n')





