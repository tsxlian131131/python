# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 08:54:28 2018
题目十七：软件发布会
软件发布地址之一：http://www.91xiazai.com/Publish/index
icon图片下载：https://www.easyicon.net/12740-color_colour_icon.html
http://www.zuiben.com/lib/upload.php
-----
1.图片名称，图标，软件下载地址，源代码下载地址，应用截图
2.分享朋友圈()
3.周一 软件发布会
@author: Administrator
"""
'''爬取一百页电影数据
'''
m=[]
import urllib.request as r    
for i in range(1,101):
    url='http://dianying.2345.com/list/-------{}.html'.format(i)
    req=r.Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
    p=r.urlopen(req).read().decode('gbk','ignore')
    print('第{}页获取结束'.format(i))
    m.append(p)

'''找出每部电影唯一指代的数字代码
'''
import re
n=[]
for i in range(len(m)):
    ls=re.compile('<li media="(.*?)".*').findall(m[i])
    n.append(ls)
a=[]
for i in range(len(n)):
    for j in range(35):
        b=n[i][j]
        a.append(b)

'''通过之前的电影相关数字编码，在网站上爬取每部电影的详细数据
'''

s=[]
for k in range(len(a)):
    url='http://dianying.2345.com/detail/{}.html '.format(a[k])
    req=r.Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
    data=r.urlopen(url).read().decode('gbk')
    print('成功{}'.format(k))
    s.append(data)

'''整理出我们需要的电影数据，并保存为TXT的文本
'''
f=open('./dianying1.txt','w')
import re
for y in range(len(s)):
    name=re.compile('<h1>(.*?)</h1>',re.S).findall(s[y])
    pinfen=re.compile('<em class="emScore">(.*?)</em>',re.S).findall(s[y])
    jianjie=re.compile('<span class="sAll">(.*?)</span>',re.S).findall(s[y])
    diqu=re.compile('<a title="(.*?)" data-ajax83="ys_dy_2015_detail_diq').findall(s[y])
    zhuyan=re.compile('<a data-ajax83="ys_dy_2015_detail_zhy_." title="(.*?)" href',re.S).findall(s[y])
    shichang=re.compile('<em class="emTit">时长：</em>\n\s*<em>(.*?)</em>',re.S).findall(s[y])
    niandai=re.compile('<em class="emTit">年代：</em>\n\s*<em>(.*?)</em>',re.S).findall(s[y])
    print('{}数据已录取'.format(y))
    f.write('电影名：{},豆瓣评分:{},地区:{},年代:{},时长:{},主演:{},电影简介:{}\n'.format(name,pinfen,diqu,niandai,shichang,zhuyan,jianjie))
f.close()

'''读取之前的文本数据，并整理为用户查询时需要的格式
'''
m=[]
import urllib.request as r
url='file:./dianying.txt'
data=r.urlopen(url).read().decode('gbk')
data1=data.split('\n')
ls1=[]
ls2=[]
ls3=[]
for i in range(len(data1)):#电影名,时长，简介.
    if i%3==0:
        ls1.append(data1[i])
    if i%3==1:
        ls2.append(data1[i])
    if i%3==2:
        ls3.append(data1[i])

'''用户查询的相关代码
'''

import re
dy=re.compile("电影名：..(.*?)..,").findall(data)
p='yes'
o='no'
def ice(b):
    for i in range(len(dy)):
        a=dy[i]
        try:
            a.index(b)
            print('{}\n{}\n{}\n'.format(ls1[i],ls2[i],ls3[i]))
        except Exception as r:
            pass

b=input('请输入电影名称：') 
ice(b)
c=input('查询结束,是否继续查询：yes或者no')
while c==p:
    b=input('请输入电影名称：') 
    ice(b)
    c=input('查询结束,是否继续查询：yes或者no')
    continue 
else:
    input('输入任意退出')





















      