#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2016-11-09-17-12
# Python 3.5

#!/usr/bin/env python
#coding: utf-8
import json

"""
,n,adj,v
hello,表示问候,,
fun,乐趣,供娱乐用的,开玩笑
python, 巨蟒,,
code,代码,,编码
{
    "fun": {
        "adj": "供娱乐用的",
        "v": "开玩笑",
        "n": "乐趣"
    },
    "python": {
        "adj": "",
        "v": "",
        "n": " 巨蟒"
    },
    "hello": {
        "adj": "",
        "v": "",
        "n": "表示问候"
    },
    "code": {
        "adj": "",
        "v": "编码",
        "n": "代码"
    }
}
"""

def make_dict(filename):
    with open(filename,"r") as file:
        dic  = {}
        i = 0
        for line in file:
            if i == 1:
                v = line.strip().split(",")
                dic.update({v[0]: {k[1]: v[1], k[2]: v[2], k[3]: v[3]}})
            else:
                k = line.strip().split(",")
                i = 1
        print(dic)
        return dic

def write_db (dic):
    json.dump(dic,open("mydict.json","w",encoding="utf8"),indent=4,ensure_ascii=False)

def search(word):
    j_list = []
    json_load_data = json.load(open("mydict.json","r",encoding="utf8"))
    if word in json_load_data.keys():
            for kk,vv in json_load_data.get(word).items():
                if vv:
                    j_list.append(vv)
            return j_list
    else:
        print("word not exsits")
        return None

if __name__ == "__main__":
    dic = make_dict('mydict.csv')
    write_db(dic)
    while True:
        word = input("enter search word:")
        result = search(word)
        if result:
            print(result)
            continue
        else:
            break