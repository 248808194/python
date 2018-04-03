#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao
#create_date:2017-02-05-13:26
# Python 3.5

def person(name,age,sex,job):
    def walk(p):
        print('person %s is walking...'%p['name'])
    date = {
        'name':name,
        'age':age,
        'sex':sex,
        'job':job,
        'walk':walk
    }
    return date


def dog(name,dog_type):

    def bark(d):
        print('dog %s: wang wang wang...'%d['name'])

    date = {
        'name':name,
        'dog_type':dog_type,
        'bark':bark
    }

    return date


d1 = dog("李闯","京巴")
p1 = person("孙海涛",36,"F","运维")

d1['bark'](d1)

p1['walk'](p1)