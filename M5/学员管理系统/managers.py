#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-05-19-13:19
# Python 3.5

from core.tech import  Tech
from core.stu import Stu

def main():
    username = input("username:")
    password = input("password:")

    if Tech().login(username,password):
        Tech().msg()
    else:
        if Stu().login(username,password):
            print('is sutdent')
        else:
            print('username or password not missmatch')









if __name__ == '__main__':
    main()

