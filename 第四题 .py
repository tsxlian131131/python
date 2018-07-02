# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 17:19:35 2018

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 10:48:22 2018
全球未来5天气预报
2018-06-21 03:00:00    按照3小时一次预报
2018-06-21 06:00:00
2018-06-21 09:00:00------当前时间
2018-06-21 12:00:00
2018-06-25 21:00:00

第四题：求出重庆未来5天天气
1.打印每天的6:00,12:00,18:00的天气(城市,温度，情况，气压，最高温度，最低温度)
2.同上写出[英文版的]
3.根据天气的情况，给出建议：例如，今天下雨，提示带伞。今天温度高，穿衬衫...三个件以上
4.根据温度打印出问题折线图
    28——————————————————————————————
    30——————————————————————————————————
    10——————————————————
5.打印出其他10个城市的天气，计算出天气排名，按着大到小的顺序。

@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)

def msg(a):
    time=data['list'][a]['dt_txt']
    a1=data['list'][a]['main']['temp']#重庆的温度
    a2=data['list'][a]['weather'][0]['description']#天气情况
    a3=data['list'][a]['main']['temp_max']#最高温度
    a4=data['list'][a]['main']['temp_min']#最低温度
    a5=data['list'][a]['main']['pressure']#气压
    print("重庆{}的温度{},天气情况{},最高温度{},最低温度{},气压为{}"
          .format(time,a1,a2,a3,a4,a5))
    if a1<20:
        print("多穿衣服")
    else :
        print("可以穿秋装，多喝水，注意防晒")
    if a2=='多云':
        print("出去游玩")
    if a2=='小雨':
        print("出门记得带伞")
    if a2=='大雨':
        print("不适合出去游玩")
msg(0)
msg(2)
msg(6)
msg(8)
msg(10)
msg(14)
msg(16)
msg(18)
msg(22)
msg(24)
msg(26)
msg(30)
msg(32)
msg(34)
