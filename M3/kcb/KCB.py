#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-14-13:50
# Python 3.5


import os,sys,time,datetime,pickle,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core import main
# print(main)
from kcb.core.schools import School




if __name__ == '__main__':
    main.run()