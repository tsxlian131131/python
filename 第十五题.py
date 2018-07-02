# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 08:53:44 2018

题目十五：未来三天 天气类天气对象
1.定义一个天气类Weather 静态的属性(temp,description,pre) 动态属性(msg打印当前天气属性)
2.创建3天的天气对象，并调用msg方法

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
class Weather:
    def __init__(self,time,temp,description,pressure):#########系统固定的方法
        self.time=time
        self.temp=temp
        self.description=description
        self.pressure=pressure
    def msg(self):#self 有对象
        print('时间：{},温度{},天气情况{},气压{}'.format(self.time,self.temp,self.description,self.pressure))
for i in range(1,22,2):
    time=(data['list'][i]['dt_txt'])
    temp=(data['list'][i]['main']['temp'])
    description=(data['list'][i]['weather'][0]['description'])
    pressure=(data['list'][i]['main']['pressure'])
    a=Weather(time,temp,description,pressure)
    a.msg()

























