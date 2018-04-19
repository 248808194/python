'''
14.215.160.24|16/Apr/2018:22:04:40 +0800|"GET /index_files/TB2iyMccXokyKJjy1zbXXXZfVXa_!!276530134.jpg HTTP/1.1
14.215.160.24|16/Apr/2018:22:05:40 +0800|"GET /index_files/TB2iyMccXokyKJjy1zbXXXZfVXa_!!276530134.jpg HTTP/1.1
'''

#method 1
from collections import Counter  # counter 简单的计数器
from pprint import pprint


def get_data(f_handle):
    ''' from a file handle get data '''
    log_dict = {}
    for i in f_handle:
        x = i.split()
        print(x[3])
        date_key = x[3][1:-3]
        print(date_key)
        if date_key not in log_dict:
            log_dict[date_key] = []
        else:
            log_dict[date_key].append(x[0])

    print('log_doct',log_dict)
    return log_dict


def count_log(xx_log, n=10):
    '''from log cut count ip '''
    x = []
    for i, j in xx_log.items():
        x.append([i, Counter(j).most_common(n)])
    return x


if __name__ == '__main__':
    filex = open('500.log')
    pprint(count_log(get_data(filex)))

#method 2 
import re

with open('500.log', 'r') as f1:
    alllines = f1.readlines()
iplist = []
tmpdist = {}
for k, v in enumerate(alllines):
    time = re.search(r'\d{2}\/\w+\/\d{4}:\d{2}:\d{2}', v).group()
    time = re.sub('[/:]','-',time)
    ip = re.search(r'(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})', v).group()
    if time not in tmpdist.keys(): #r如果time 不在列表中,tmpdist中新建一个k，v
        tmpdist[time] = [{ip: 1}]
    else: #否则证明time 的key 已经存在的。
        for kk,vv in enumerate(tmpdist[time]):  # 循环时间的那个列表
            for  k,v in vv.items():  #{'14.215.160.24': 27}
                if ip == k:  # ip 在子列表中存在
                    tmpdist[time][kk][ip] += 1  # ip的值 +1
                else:# 如果ip不存在，新建一个子字
                    if ip not in iplist:
                        tmpdist[time].append({ip:1})
        iplist.append(ip)
print(tmpdist)
#最终输出结果：
    # {'16-Apr-2018-22-04': [{'14.215.160.24': 13}], '16-Apr-2018-22-05': [{'14.215.160.25': 15}]}
#
