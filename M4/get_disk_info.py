#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-04-10-17:05
# Python 3.5
import os,sys,subprocess,re
from subprocess import  Popen

disk = 0
def get_DiskInfo():
    p = Popen('fdisk -l',shell= True)
    stdout,stderr = p.communicate()
    diskdata = stdout
    disk_initial_size = 0
    re_disk_type = re.compile(r'Disk /dev/[shd]{1}.*:\s+[\d.\s\w]*,\s+([\d]+).*')
    disk_size_bytes = re_disk_type.findall(diskdata.decode('UTF-8'))
    for size in disk_size_bytes:
        disk_initial_size += int(size)
        disk_size_total_bytes = '%.2f'  % (float(disk_initial_size)/1000/1000/1000)
        disk_size_total_G = disk_size_total_bytes + 'G'
        disk = disk_size_total_G
    return disk

if __name__ == '__main__':
    disk = get_DiskInfo()
    print(disk)