# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 09:10:48 2018
K12（小学到高中12年的简称）--
高考--高考派(统计全中国大学招生情况，例如北京大学(3000)在北京招多少人？在重庆？在全国？)
全中国有多少所大学？
全中国有多少个城市？
在某个城市文科招的人数？理科招生的人数？
====
全国大学招生人数排行：例如
郑州大学 8000
桂林大学 6000
.....
西藏藏医学院：5
=
家长帮班级项目：
注意点：同一时间，访问量过大，可能会导致本次项目无法进行，因为北京那边服务器奔溃。导致全国都无法访问。
导致对方程序员加班。所以我们整个班级，需要有一套策略，要拿到所有数据但不会导致奔溃。
策略例如：
======
题目十四：家长帮大数据爬虫项目
1.根据all_school.txt获取全中国学校网址编号：1304，生成一个2300列表
2.根据http://www.gaokaopai.com/daxue-zhaosheng-学校编号.html 获取全国城市的编号 例如北京：11
3.班级团队(需要下载142600(2300*31*2)次)：
    中国划分区域-分组(城市)
    区域分组员
    如何下载策略-分时间下载
    执行人物2300-分配到自己的任务一般是2300
    保存数据---组长全部合并--班长统计
4.待定


@author: Administrator
"""
import urllib.request as r
url='file:./all_school.txt'
data=r.urlopen(url).read().decode('utf-8')
print(data)#打开文件
import re

ls=re.compile('jianjie-(.*?).html',re.S).findall(data)
ls1=re.compile('(.*?)http').findall(data)
for i in range(len(ls)):
    data1=ls[i]
    data2=ls1[i]
    print("编号:{}".format(data1))
url='http://www.gaokaopai.com/daxue-0-0-0-0-0-0-0.html '
data='id=2948&type=2&city=50&state=1'.encode()
req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
d=r.urlopen(req).read().decode('utf-8','ignore')
e=re.compile('<span><a href="http://www.gaokaopai.com/daxue-(.*?)-0-0-0-0-0-0.html">').findall(d) 
f=re.compile('<span><a href="http://www.gaokaopai.com/daxue-..-0-0-0-0-0-0.html">(.*?)</a></span>').findall(d)
for i in range(len(e)):
    print('{}-{}'.format(f[i],e[i]))

f=open('./江苏理科.txt','w',encoding='utf-8')
for n in range(len(ls)):
    url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
    data='id={}&type=2&city=33&state=1'.format(ls[n])
    data1=data.encode()
    req=r.Request(url,data=data1,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    a=r.urlopen(req).read().decode('utf-8','ignore')
    if a.startswith('{'):
        print("成功{}".format(n))
    else:
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
        data='id={}&type=2&city=33&state=1'.format(ls[n])
        data1=data.encode()
        req=r.Request(url,data=data1,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        a=r.urlopen(req).read().decode('utf-8','ignore')
        print("错误更改成功")
    f.write(a+"\n")
f.close()

#打开数据进行分析
import urllib.request as r
url='file:./江苏理科12.txt'
data=r.urlopen(url).read().decode('utf-8')
list=data.split()
h=[]##数据列表
import json
for i in range(2300):
    a2=json.loads(list[i])  
    h.append(a2)
    

#华东
#江苏
area={'黑龙江':'东北','吉林':'东北','辽宁':'东北'}
areaplan={'东北':0}
areaplan['东北']=areaplan['东北']+8
###########通过下面定义多个变量赋值，计算出中国地区的人数
a=0
b=0
c=0
if '东北'==plan:
   a=a+1 
import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With': 'XMLHttpRequest'}
req=r.Request(url,headers=headers,data='id=477&type=2&city=23&state=1'.encode())
data=r.urlopen(req).read().decode('utf-8','ignore')
import json

data=json.loads(data)

for i in range(142600):
    if data['status']==1:
        ls=data['data']
    for school in ls:
        city=school['city']
        print(area[city])
        print(int(school['plan']))
        areaplan[area[city]]=areaplan[area[city]]+int(school['plan'])

m=[]
import urllib.request as r
url='file:./全国招生计划表0206C正确.txt'
data=r.urlopen(url).read().decode('utf-8')
data=data.split('\n')#data=data.split('\n')
import json
for i in range(len(data)):
    a=json.loads(data[i])
    m.append(a)

东北=['辽宁','吉林','黑龙江']
华东=['上海','江苏','浙江','安徽','福建','江西','山东']
华北=['北京','天津','河北','山西','内蒙古']
华中=['河南','湖北','湖南']
华南=['广东','广西', '海南']
西南=['重庆','四川','贵州','云南','西藏']
西北=['陕西','甘肃','青海','宁夏','新疆']
all=[东北,华东,华北,华中,华南,西南,西北]
area=['东北','华东','华北','华中','华南','西南','西北']
for l in range(len(all)):
    b=len(all[l])
    v=0
    for j in range(b):
        x=all[l][j]
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
        v=v+n
        print('{}招生人数为{}'.format(Province,n))
    print('{}地区招生总人数:{}\n'.format(area[l],v))






