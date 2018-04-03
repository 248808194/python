#!/usr/bin/env python
# Author: Zhoutao
#create_date:2016/12/9 0009 14:34
#file: model_subprocess.py
# Python 3.5


# import subprocess
# child = subprocess.Popen("ping 202.96.209.5 -t",shell= True)
# child.wait()

# import subprocess
# obj = subprocess.Popen("mkdir t3", shell=True,cwd="." )

import subprocess

obj = subprocess.Popen(["ipython"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True) # 打开ipython 在其中输入 内容
abc = input("enter ")
obj.stdin.write(abc+"\n")
obj.stdin.write(abc)
obj.stdin.close() # 关闭stdin

cmd_out = obj.stdout.read()
obj.stdout.close()
cmd_error = obj.stderr.read()
obj.stderr.close()
print(cmd_out)
print(cmd_error)