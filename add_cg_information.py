__author__ = 'unicomcat'
from . import engine
from . import cg,billlist
conn = engine.connect()
insert_cg = cg.insert()


def insert_cg_fun(name, access_ip, disk_ip, access_type, bill_path1, bill_path2, password1, password2):
    cg_dict = {'name':name,
               'access_ip':access_ip,
               'disk_ip':disk_ip,
               'access_ip':access_type,
               'bill_path1':bill_path1,
               'bill_path2':bill_path2,
               'password1':password1,
               'password1':password2
               }



    r=conn.execute(insert_cg,**u)




