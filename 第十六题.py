# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 09:58:56 2018

题目十六：高考派2300数据统计
1.根据2300下载的两百多M文件，统计招生总人数
2.统计7各地域的人数各是多少
3.计算比例

@author: Administrator
"""

import urllib.request as r
import re
url='file:./全国招生.txt'
data=r.urlopen(url).read().decode('utf-8')
ls=re.compile('"plan":"(.*?)"',re.S).findall(data)
ls1=0
for m in ls:
    ls1=ls1+int(m)
print('全国招生总人数:{}'.format(ls1))
#####第一问结束


m=[]
data1=data.split('\n')
import json
for i in range(len(data1)):
    a=json.loads(data1[i])
    m.append(a)

东北=['辽宁','吉林','黑龙江']
华东=['上海','江苏','浙江','安徽','福建','江西','山东']
华北=['北京','天津','河北','山西','内蒙古']
华中=['河南','湖北','湖南']
华南=['广东','广西', '海南']
西南=['重庆','四川','贵州','云南','西藏']
西北=['陕西','甘肃','青海','宁夏','新疆']
d=[东北,华东,华北,华中,华南,西南,西北]
全国=['东北','华东','华北','华中','华南','西南','西北']
def ice(x):
    n=0
    Province=x
    for i in range(len(m)):
        b1=m[i]['status']
        if b1==1:
            b2=m[i]['data'][0]['city']
            b4=m[i]['data']
            if b2==x:
                for j in range(len(b4)):
                    b5=m[i]['data'][j]['plan']
                    b5=int(b5)
                    n=n+b5
    print('{}招生人数为{}'.format(Province,n))
for i in range(len(d)):
    print('{}地区招生情况:'.format(全国[i]))
    b=len(d[i])
    for j in range(b):
        x=d[i][j]
        ice(x)
        

        
        
        
        
        
        b3=m[i]['data'][0]['school']
