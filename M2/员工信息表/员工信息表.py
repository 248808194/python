#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2016-12-21-13:36
# Python 3.5
import commons

def write_back(file,old_dict):
    '''
    先写入第一行列名
    遍历循环子字典写入到文件中去
    '''
    with open(file, "w") as f:
        v_keys = ['id','name', 'age', 'phone', 'dep', 'year']
        f.write(','.join(v_keys) + '\n')
        for i, v in old_dict.items():
            tmplist = [i]
            for ii in v_keys:
                if ii == 'id':
                    continue
                tmplist.append(v.get(ii))
            f.write(','.join(tmplist) + '\n')


def select(old_dict,inp_str):
    '''
    判断1：在select 和 from 之间 的字符串放在一个列表中，如果大于1 逐个去匹配，如果小于 1 判断是否为 * 号，如果不为* 也放在列表中 par_list =  [ "name","age" ]
    判断1-2：有没有where 如果有 将where 后面的字符串分别放入到一个列表中，Example: wherepar_list = [ age, ">","22" ]
    如果没有where 直接通过par_list 查出数据
    如果有where 将 wherepar_list 中的参数拿出来查出数据
    函数结束最后将零时列表，字典等清空.
    '''
    select_part_list = inp_str.strip().split()[1].strip().split(",") # 将语句select参数拿出来组成列表，并且循环便利该列表
    where_part_list = inp_str.strip().split("where")[1].strip().split()  # 将语句ｗｈｅｒｅ之后的参数拿出来组成一个列表
    print(where_part_list)
    condition_dict = {">":"dayu","<":"xiaoyu","=":"dengyu","like":"like"} # 定义一个where 条件组成的字典
    for i in condition_dict.keys(): # 遍历循环字典的key
        if where_part_list[1] == i: # 获取ｋｅｙ　以便通过反射执行函数
            print(where_part_list[1])
            func_str = condition_dict.get(where_part_list[1]) # 获取condition_dict value
            func = getattr(commons,func_str) #通过反射去执行commons下的各个函数
            func(old_dict,select_part_list,where_part_list)


def update(old_dict,inp_str,file):
    '''
    将set后的字段拿出来，其实tuple　list　都一样
    将ｗｈｅｒｅ后面的字段拿出来
    遍历循环整个＿ｄｉｃｔ　子字段
    将子，字典中的tuple(key,value)　和　wherelist 做比较，如果相同，则更新old_dict 中某个值 example 'dep'

    :param old_dct:
    :param inp_str:
    :return:
    '''
    setlist  = tuple(inp_str.strip().split("set")[1].split()[0].strip().split('=')) # ('dep', '"it"')
    wherelist = tuple(inp_str.strip().split("where")[1].strip().strip().split("=")) # ('name ', ' "zhoutao"')

    for i in old_dict.values():
        for ii in i.items(): # tuple 和　tuple 做比较
            if wherelist == ii:
                i[setlist[0]] = setlist[1]

    write_back(file,old_dict)

def insert(old_dict,inp_str,file):
    '''
    先统计出id 将最大的ID拿出来＋１，为插入的ｉｄ做准备
    INSERT INTO table SET name = zhoutao,age = 22,phone = 111111,dep = IT,year = 2014-10-20
    将ｉｎｓｅｒｔ　组合成字典insert_dict = {'name':'zhoutao','age':'22','dep':'it','phone':'18964381759','year':'20140123'}
    检查ｉｎｓｅｒｔ　中的ｐｈｏｎｅ是否存在与old_dict 有则报告已经存在
    没有，将insert_dict 插入　ＩＤ　组合成一个新字典，更新到old_dict下去
    将ｏｌｄ_dict 更新到文件中去			先统计出id 将最大的ID拿出来＋１，为插入的ｉｄ做准备
    INSERT INTO table SET name = zhoutao,age = 22,phone = 111111,dep = IT,year = 2014-10-20
    将ｉｎｓｅｒｔ　组合成字典insert_dict = {'name':'zhoutao','age':'22','dep':'it','phone':'18964381759','year':'20140123'}
    检查ｉｎｓｅｒｔ　中的ｐｈｏｎｅ是否存在与old_dict 有则报告已经存在
    没有，将insert_dict 插入　ＩＤ　组合成一个新字典，更新到old_dict下去
    将ｏｌｄ_dict 更新到文件中去
    '''
    insert_id = str(max([ int(x) for x in old_dict.keys() ]) + 1)
    get_dict = dict([tuple(x.strip().split(' = ')) for x in inp_str.strip().split('SET')[1].strip().split(',') if x.split()])
    value_phone = [ x.get('phone') for x in old_dict.values() ]
    if get_dict.get("phone") in value_phone:
        print("phone is exists")
    else:
        old_dict.update({insert_id:get_dict})
        write_back(file,old_dict)





def deltel(old_dict,inp_str,file):
    '''
    获取到删除的ｉｄ，如果ｉｄ　存在则删除，如果不存在，则打印ｉｄ不存在
    :param old_dict:
    :param inp_str:
    :return:
    '''
    getid = inp_str.split('=')[1]
    print(getid)
    if getid in [ x for x in old_dict.keys() ]:
        del old_dict[getid]
    else:
        print('id not found')

    write_back(file,old_dict)
        


def get_dict(file):
    with open("info.txt", "r", encoding="utf8") as f:
        b = 0
        old_dict = {}
        for i in f:
            chr_dict = {}
            i = i.strip().split(",")
            if b == 1:
                chr_dict['name']= i[1]
                chr_dict['age']= i[2]
                chr_dict['phone']= i[3]
                chr_dict['dep']= i[4]
                chr_dict['year']= i[5]
                old_dict.update({i[0]: chr_dict})  # 这个bug 需要修改一下，应该是循环便利文件才对
            else:
                i.remove("id")  # 过滤掉 id这个参数
                for ii in i:
                    chr_dict[ii] = None
                    b = 1
        return  old_dict
# get_dict("info.txt")


def main(file):
    while True:
        old_dict = get_dict(file)
        inp_str = input("请输入增删改查语句:")
        if inp_str.startswith("select"):
            select(old_dict,inp_str)
        elif inp_str.startswith("update"):
            update(old_dict,inp_str,file)
        elif inp_str.startswith("insert"):
            insert(old_dict,inp_str,file)
        elif inp_str.startswith("delete"):
            deltel(old_dict,inp_str,file)
        else:
            print("syntax error (%s) not support"%inp_str)
if __name__ == "__main__":
    main('info.txt')






