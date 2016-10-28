#!/usr/bin/python  
# -*- coding: utf-8 -*-
import ftplib
import os
import socket

HOST = '132.151.148.4'
DIRN = 'R6'
USERNAME = 'administrator'
PASSWORD = 'igwb'


def main():
    try:
        f = ftplib.FTP(HOST,USERNAME,PASSWORD)
    except (socket.error, socket.gaierror):
        print 'ERROR:cannot reach " %s"' % HOST
        return
    print '***Connected to host "%s"' % HOST

    try:
        haha = f.nlst()
        print haha
    except ftplib.error_perm:
        print 'ERROR: cannot login anonymously'
        f.quit()
        return

if __name__ == '__main__':
    main()
