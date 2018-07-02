# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 09:19:32 2018
《当》动力火车
当山峰没有棱角的时候
当河水不再流
当时间停住日夜不分
当天地万物化为虚有
...
当太阳不再上升的时候
当地球不再转动
当春夏秋冬不再变换
当花草树木全部凋残

练习七:全球天气未来3天
1.使用多选其一，完成天气的提醒
2.一定要多ci使用到for循环,偶尔用一次while循环
3.初步学会使用debug，知道里面的设置断点，下一步执行，下一个断点执行。
4.《闪屏的制作》进入我们天气程序的时候，有一个温馨图形的提示。使用循环实现，
  要知道是什么意思，照抄网上代码不行。

    

@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)

for a in range(5,30,3):
    time=data['list'][a]['dt_txt']
    a1=data['list'][a]['main']['temp']#重庆的温度
    a2=data['list'][a]['weather'][0]['description']#天气情况  
   
    if a2=='多云':
        print("重庆{}的温度：{},天气为：{}, 建议：出去游玩，穿秋衣".format(time,a1,a2))
    elif a2=='晴,少云' :
        print("重庆{}的温度：{},天气为：{}, 建议：可以穿秋装，多喝水，注意防晒".format(time,a1,a2))
    elif a2=='晴':
        print("重庆{}的温度：{},天气为：{}, 建议：出去游玩,可以减少衣物，注意补水".format(time,a1,a2))
    elif a2=='中雨':
        print("重庆{}的温度：{},天气为：{}, 建议：出门记得带伞".format(time,a1,a2))
    elif a2=='小雨':
        print("重庆{}的温度：{},天气为：{}, 建议：不适合出去游玩,记得带伞".format(time,a1,a2))
    
ls=['天','气','预','报']
for i in ls:
    if i=='天':
        print('*'*5,i,'*'*5)
    elif i=='气':
        print('*'*5,i,'*'*5)
    elif i=='预':
        print('*'*5,i,'*'*5)
    elif i=='报':
        print('*'*5,i,'*'*5)























