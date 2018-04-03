#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-04-13-09:19
# Python 3.5

from  socket_client import socket_client




while True:
    command_action = input(":")
    command_action = command_action.strip().split()
    action = command_action[0]
    filename = command_action[1]
    print(command_action)
    if len(command_action) == 2:
        if hasattr(socket_client(),action):
            func = getattr(socket_client(),action)
            func(filename)

    else:
        continue

