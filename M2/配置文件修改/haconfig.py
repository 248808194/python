#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2016/12/16 0012 10:11
#file: haconfig.py
# Python 3.5

import time
import  shutil

def updateconf(file,old_line,old_dict,**kwargs):
    '''
    添加一个已经存在的backend server字段
    '''

    with open(file,"w") as oldfile:
        for k,v in kwargs.items():
            if kwargs.get(k): # v值存在
                newlist_server = list(set([old_dict.get(k)[i].strip() for i in range(len(old_dict.get(k)))]) | set(v)) # 获取kwargs 和olddict 下的server 交集
                for nline in newlist_server:
                    old_dict[k] = newlist_server
            else:
                pass # 这里因该再次判断，暂先不写
        #         del old_dict[k]
        for k,v in old_dict.items():
            old_line.append("backend "+ k )
            for i in v:
                i = i.strip()
                old_line.append("server "+ i )
        for line in old_line:
            oldfile.write(line + "\n")

def delconf(file,old_line,old_dict,**kwargs):
    '''
传入过滤掉的backend server 列表 old——line
传入 原文件的backend server 字典
 将需要删除的字典，key ，value 与old——dict匹配
 更新old_dict 后循环追加到old_line 下，将old_line 写入到文件中去，

    '''
    for k,v in kwargs.items():
        print("before",old_dict)
        if kwargs.get(k): # v值存在 # 遍历出v 值，并且在old_list 中删除掉V值
            old_list = old_dict.get(k)
            kwargs_list = (kwargs.get(k))
            for i in kwargs_list:
                i = i.split("server")[1].strip()
                print(i)
                if i in old_list:
                    old_list.remove(i)
            old_dict[k] = old_list
        else:
            del old_dict[k]
    for k,v in old_dict.items():
        old_line.append("backend "+ k)
        if old_dict.get(k):
            for i in v:
                i = i.strip()
                old_line.append("server " + i)
    with open(file,"w") as file:
        for i in old_line:
            file.write(i + "\n")

def addconf(file,old_line,old_dict,**kwargs):
    '''
增加新的backend , server
 通过传入的kwargs取更新old_line
 遍历old_line 写入到文件中去
    '''

    old_dict.update(kwargs)
    print(old_dict)
    with open(file,"w") as chfile:
        for k,v in old_dict.items():
            old_line.append("backend "  + k)
            for vv in v:
                old_line.append("server " + vv)
        for line in old_line:
            line = line.strip() + "\n"
            chfile.write(line)

def backup_conf(file):
    """
    先备份文件，将文件备份为 文件名+ 时间格式
    打开文件保持关键性参数到字典下
    example：
    {
        'www.test.com': [
            'web0110.10.0.1weight20maxconn3000',
            'web0210.10.0.2weight20maxconn3000'
        ],
        'news.test.com': [
            'web0110.10.0.1weight20maxconn3000'
        ]
    }
    backend判断逻辑：
        逐行读取文件，如果 是以backend开头，且in_backend 为False ，
        将in_backend 值置为True
        清空tmp_key_list 列表，为下一个backend server段做存储数据准备
        将backend 那一行的第二个参数设为字典的key
        将in_server 值 置为 True
     server判断逻辑
        当in_server 为True时，
        将server 的第二个参数拿出来放到tmp_key_list 列表中
        将in_backend 值置为False
    """
    bak_time = time.strftime("%Y-%m-%d-%H-%M-%S")
    shutil.copy(file,file + bak_time)

    with open(file,"r") as oldfile:
        in_backend = False
        in_server = False
        old_dict = {}
        oldline = []
        tmp_key_list = []
        for i in oldfile: # 获取老的配置文件参数
            i = i.strip()
            oldline.append(i)
        for line in oldline:
            if line.strip().startswith("backend") and in_backend == False:
                in_backend = True
                tmp_key_list = []
                old_dict[line.strip().split()[1]] = tmp_key_list
                in_server = True
                continue

            if line.strip().startswith("server") and  in_server == True:
                if line.strip().startswith("server"):
                    tmp_key_list.append(line.strip().split("server")[1].strip())
                    in_backend = False
                    continue
        oldline = [ x.strip() for x in open(file,"r") if not x.strip().startswith("backend") and  not x.strip().startswith("server") ]# 嵌套的list 表达式
        return [old_dict,oldline] #  函数返回原始backend 值，和文件原始数据列表

def main(file,*args,**kwargs):
    bak = backup_conf(file)
    old_dict = bak[0]
    old_line = bak[1]
    if args:
        if args[0] == "delconf": # 判断arg传入的第一个参数
            delconf(file, old_line, old_dict, **kwargs)
        elif args[0] == "addconf":
            addconf(file, old_line,old_dict, **kwargs)
        elif args[0] == "updateconf":
            updateconf(file,old_line,old_dict,**kwargs)
    else:
        print("参数args不能为空")

# main("test.txt","updateconf",**{"www.t111est.com":["100.1.7.90 100.1.7.9 weight 20 maxconn 5000"]})
# main("test.txt","delconf",**{"www.t111est.com":["server 100.1.7.90 100.1.7.9 weight 20 maxconn 5000"]})
# main("test.txt","addconf",**{"www.test2.com":["100.1.7.90 100.1.7.9 weight 20 maxconn 5000"]})
