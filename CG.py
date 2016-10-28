# -*- coding: utf-8 -*-
__author__ = 'unicomcat'
import paramiko
import time
from database import BillType,BILL_SUMMARY
from database import database
import re
import sys

reload(sys)

sys.setdefaultencoding( "utf-8" )
class CG(object):
    '''
    cg_name = ''              #cg_name = 'CG12'
    access_ip = ''            #access_ip = '192.40.1.10'
    access_username = ''      #access_username = root
    access_type = ''          #access_type = 'ssh'
    disk_ip = ''              #disk_ip = '172.16.128.8'
    bill_type = ''            #bill_type = 'pgwcdr/sgwcdr/scdr'
    bill_path1 = ''           #bill_path = '/var/igwb/backsve/'
    bill_path2 = ''
    password1 = ''
    password2 = ''
    port = ''
    bill_date=''
    cg_type = ''
    pgw_bill_information = {
        'file_num': '',
        'begin_file': '',
        'end_file': '',
        'total_size': ''
    }
    sgw_bill_information = {
        'file_num': '',
        'begin_file': '',
        'end_file': '',
        'total_size': ''
    }
    scdr_bill_information = {
        'file_num': '',
        'begin_file': '',
        'end_file': '',
        'total_size': ''
    }
    bill_summary = {'pgw':pgw_bill_information,'sgw':sgw_bill_information,'scdr':scdr_bill_information}
'''
    def __init__(self, **kwargs):
        self.cg_name = kwargs['cg_name']
        self.access_ip = kwargs['access_ip']
        self.access_username = kwargs['access_username']
        self.disk_ip = kwargs['disk_ip']
        self.access_type = kwargs['access_type']
        self.bill_type = kwargs['bill_type']
        self.bill_path1 = kwargs['bill_path1']
        self.bill_path2 = kwargs['bill_path2']
        self.password1 = kwargs['password1']
        self.password2 = kwargs['password2']
        self.bill_date = kwargs['bill_date']
        self.cg_type = kwargs['cg_type']
        self.pgw_bill_information = {
        'file_num': '/',
        'begin_file': '/',
        'end_file': '/',
        'total_size': '/'
         }
        self.sgw_bill_information = {
        'file_num': '/',
        'begin_file': '/',
        'end_file': '/',
        'total_size': '/'
        }
        self.scdr_bill_information = {
        'file_num': '/',
        'begin_file': '/',
        'end_file': '/',
        'total_size': '/'
        }
        self.bill_summary = {'pgwcdr':self.pgw_bill_information,'sgwcdr':self.sgw_bill_information,'scdr':self.scdr_bill_information}

    @classmethod
    def test_disk_ip(cls, access_ip, access_username, omu_password, cgu_password,disk_ip1,disk_ip2):
        port = 22
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(access_ip, port, access_username, omu_password)
        execshell = ssh.invoke_shell()
        for disk_ip in [disk_ip1,disk_ip2]:
            execshell.send('ssh ' + disk_ip + '\n')
            resp = execshell.recv(1024)
            if '(yes/no)? ' in resp:
                execshell.send('yes \n')
            buff = ''
            while not buff.endswith('password: '):
                resp = execshell.recv(1024)
                buff += resp
            print buff
            execshell.send(cgu_password + '\n')
            buff = ''
            while not buff.endswith('# '):
                resp = execshell.recv(1024)
                buff += resp
            print buff
            execshell.send('df -h | grep igwb \n')
            buff = ''
            answer=''
            while not buff.endswith('# '):
                resp = execshell.recv(1024)
                buff += resp
                answer = re.findall('/var/igwb', buff)
            if answer == ['/var/igwb']:
                return disk_ip
            else:
                execshell.send('exit \n')
                buff = ''
                answer = ''
                while not buff.endswith('# '):
                    resp = execshell.recv(1024)
                    buff += resp
                continue
            return "error in check disk ip !"






    def test_connect_cg(self):
        if self.access_type == 'ssh':
            self.port = 22
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.access_ip, self.port, self.access_username, self.password1)
            execshell = ssh.invoke_shell()
            if self.password2 == '':
                print 'nokia/zte'
            else:
                execshell.send('ssh ' + self.disk_ip + '\n')
                buff = ''
                while not buff.endswith('password: '):
                    resp = execshell.recv(9999)
                    buff += resp
                execshell.send(self.password2+'\n')
                print execshell.recv(9999)
                print 'huawei'
        elif self.access_type == 'ftp':
            self.port = 21
        else:
            pass

    def get_bill_information(self):
        if self.access_type == 'ssh':
            self.port = 22
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.access_ip, self.port, self.access_username, self.password1)
            execshell = ssh.invoke_shell()
            if self.password2 == '':
                if self.cg_type == 'Nokia':
                    bill_path = self.bill_path1+'BAK_' + self.bill_date
                    stdin, stdout, stderr = ssh.exec_command('find '+bill_path+' -type f |wc -l')
                    for line in stdout:
                        self.pgw_bill_information['file_num']=line.strip('\n')
                    #print self.pgw_bill_information
                    stdin, stdout, stderr = ssh.exec_command('cd ' + bill_path +';ls -tr')
                    file_name = []
                    for line in stdout:
                        file_name.append(line.strip('\n'))
                    #print file_name[0], file_name[-1]
                    self.pgw_bill_information['begin_file'] = file_name[0]
                    self.pgw_bill_information['end_file'] = file_name[-1]
                    stdin, stdout, stderr = ssh.exec_command('cd ' + bill_path +';du -sh -b')
                    for line in stdout:
                        self.pgw_bill_information['total_size']=line.strip('\t.\n')
                    print self.pgw_bill_information
                    ssh.close()
            else:
                execshell.send('ssh ' + self.disk_ip + '\n')
                buff = ''
                while not buff.endswith('password: '):
                    resp = execshell.recv(1024)
                    buff += resp
                print buff
                execshell.send(self.password2+'\n')
                buff = ''
                while not buff.endswith('# '):
                    resp = execshell.recv(1024)
                    buff += resp
                print buff
                bill_kind = {}
                bill_path_arry=[]
                if self.bill_type == BillType.SGWCDR|BillType.PGWCDR:
                    bill_path_arry.append(self.bill_path1 + 'R9/first/' + 'sgwcdr/' + self.bill_date)
                    bill_path_arry.append(self.bill_path1 + 'R9/first/' + 'pgwcdr/' + self.bill_date)
                elif self.bill_type == BillType.SGWCDR|BillType.PGWCDR|BillType.SCDR:
                    bill_path_arry.append(self.bill_path1 + 'R9/first/' + 'sgwcdr/' + self.bill_date)
                    bill_path_arry.append(self.bill_path1 + 'R9/first/' + 'pgwcdr/' + self.bill_date)
                    bill_path_arry.append(self.bill_path1 + 'R6/first/' + 'scdr/' + self.bill_date)
                elif self.bill_type == BillType.SCDR:
                    bill_path_arry.append(self.bill_path1 + 'R6/first/' + 'scdr/' + self.bill_date)
                else:
                    print 'now that is not support!'
                for bill_path in bill_path_arry:
                    if 'sgw' in bill_path:
                        bill_kind = self.bill_summary['sgwcdr']
                    elif 'pgw' in bill_path:
                        bill_kind = self.bill_summary['pgwcdr']
                    elif 'scdr' in bill_path:
                        bill_kind = self.bill_summary['scdr']

                    execshell.send('ls -t '+bill_path+'| head -1 \n')
                    buff = ''
                    answer = ''
                    while not answer:
                        resp = execshell.recv(1024)
                        buff += resp
                        answer = re.findall('gzR\d+.+.dat', buff)
                    print answer[0]
                    bill_kind['end_file'] = answer[0]

                    execshell.send('ls -tr '+bill_path+'| head -1 \n')
                    buff = ''
                    answer = ''
                    while not answer:
                        resp = execshell.recv(1024)
                        buff += resp
                        answer = re.findall('gzR\d+.+.dat', buff)
                    print answer[0]
                    bill_kind['begin_file'] = answer[0]

                    execshell.send('du -sh -b '+bill_path+'\n')
                    buff = ''
                    answer = ''
                    while not answer:
                        resp = execshell.recv(1024)
                        buff += resp
                        answer = re.findall('\\r\\n\d+\\t', buff)

                    print answer[0].strip('\r\n').strip('\t')
                    bill_kind['total_size'] = answer[0].strip('\r\n').strip('\t')

                    execshell.send('find '+bill_path+' -type f |wc -l\n')
                    buff = ''
                    answer = ''
                    while not answer:
                        resp = execshell.recv(1024)
                        buff += resp
                        answer = re.findall('\\r\\n\d+\\r\\n', buff)

                    print answer[0].strip('\r\n').strip('\r\n')
                    bill_kind['file_num'] = answer[0].strip('\r\n').strip('\r\n')

                    print self.bill_summary

                ssh.close()
        elif self.access_type == 'ftp':
            self.port = 21
        else:
            pass

    def write_bill_summary_txt(self):
        bill_txt = open(self.bill_date+'.txt','a')
        for bill_detail in self.bill_summary:
            '''
            bill_txt.write(unicode(self.cg_name,'utf-8').ljust(20, ' ')+'\t'+self.bill_date.ljust(20,' ')+'\n')
            bill_txt.write((unicode(bill_detail,'utf-8')+u'话单数').ljust(20, ' ')+'\t'+
                self.bill_summary[bill_detail]['file_num'].ljust(20, ' ')+'\n')
            bill_txt.write(u'文件大小（Byte）'.ljust(20,' ')+'\t'+self.bill_summary[bill_detail]['total_size'].ljust(20,' ')+'\n')
            bill_txt.write(u'第一个文件'.ljust(20,' ')+'\t'+self.bill_summary[bill_detail]['begin_file'].ljust(20,' ')+'\n')
            bill_txt.write(u'最后一个文件'.ljust(20,' ')+'\t'+self.bill_summary[bill_detail]['end_file'].ljust(20,' ')+'\n\n')

            '''
            bill_txt.write(self.cg_name.ljust(20, ' ') + '\t' + self.bill_date.ljust(20, ' ') + '\n')
            bill_txt.write((unicode(bill_detail, 'utf-8') + u'话单数').ljust(20, ' ') + '\t' +
                           self.bill_summary[bill_detail]['file_num'].ljust(20, ' ') + '\n')
            bill_txt.write(u'文件大小（Byte）'.ljust(20, ' ') + '\t' + self.bill_summary[bill_detail]['total_size'].ljust(20,
                                                                                                                    ' ') + '\n')
            bill_txt.write(
                u'第一个文件'.ljust(20, ' ') + '\t' + self.bill_summary[bill_detail]['begin_file'].ljust(20, ' ') + '\n')
            bill_txt.write(
                u'最后一个文件'.ljust(20, ' ') + '\t' + self.bill_summary[bill_detail]['end_file'].ljust(20, ' ') + '\n\n')

            bill_instance = BILL_SUMMARY(DATE=self.bill_date,
                                         BEGIN_FILE_NAME=self.bill_summary[bill_detail]['begin_file'],
                                         LAST_FILE_NAME=self.bill_summary[bill_detail]['end_file'],
                                         FILE_SIZE=self.bill_summary[bill_detail]['total_size'],
                                         BILL_NUM = self.bill_summary[bill_detail]['file_num'],
                                         BILL_TYPE = self.bill_type,
                                         CG_NAME = self.cg_name
                                         )
            database.session.add(bill_instance)
            database.session.commit()


        bill_txt.close()



