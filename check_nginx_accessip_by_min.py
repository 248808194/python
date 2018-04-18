'''
14.215.160.24|16/Apr/2018:22:04:40 +0800|"GET /index_files/TB2iyMccXokyKJjy1zbXXXZfVXa_!!276530134.jpg HTTP/1.1
14.215.160.24|16/Apr/2018:22:05:40 +0800|"GET /index_files/TB2iyMccXokyKJjy1zbXXXZfVXa_!!276530134.jpg HTTP/1.1
利用时间和ip地址去做键值对。

'''
import re

with open('500.log', 'r') as f1:
    alllines = f1.readlines()

tmpdist = {}
for k, v in enumerate(alllines): #其实这里可以不用enumerate 
    time = re.search(r'\d{2}\/\w+\/\d{4}:\d{2}', v).group() #过滤出时间 精确到分钟
    ip = re.search(r'(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})', v).group() #过滤出IP地址
    if time not in tmpdist.keys(): 
        tmpdist[time] = [{ip: 1}]
        continue
    else:
        for i in tmpdist[time]:  # 循环时间的那个列表
            if ip in i.keys():  # ip 在子列表中存在
                i[ip] += 1  # ip的值 +1
            else:  # 如果不存在，新建一个字典
                tmpdist[time].append({ip: 1})
print(tmpdist)

#{'16/Apr/2018:22': [{'14.215.160.24': 27}], '16/Apr/2018:23': [{'14.215.160.24': 29}]}
#
