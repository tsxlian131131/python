# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:48:02 2018
题目十二：使用re爬取天气信息
1.天气描述，天气温度，天气气压

@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
description=re.compile('"description":"(.*?)"').findall(data)
temp=re.compile('"temp":(.*?)"').findall(data)
pressure=re.compile('"pressure":(.*?)"').findall(data)
for i in range(8):
    print("天气描述是:{},天气温度是:{},天气气压是:{}".format(description[i],temp[i],pressure[i]))

