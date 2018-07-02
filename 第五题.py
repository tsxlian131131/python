# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:39:54 2018
函数：
变量(生命周期)
全局变量，局部变量(函数内)
练习五:实现练习四，
1.使用函数写出来。定义函数，输出每一天6:00,12:00,18:00的天气信息
2.打印折线图,使用字符串的*号操作
10----------
5-----
@author: Administrator
"""
a=3

def msg():#定义一个函数  def 函数名(): 代码
    b=4
    des='晴天'
    week='星期六'
    print('今天温度是：{}'.format(b))
    print('今天天气是：{}'.format(des))
    print('今天{}'.format(week))
print(b)
msg()
msg()
msg()

def msg(b,des,week):
    print('今天温度是：{}'.format(b))
    print('今天天气是：{}'.format(des))
    print('今天{}'.format(week))
msg(28,'晴','星期四')
msg(30,'多云','星期五')
msg(21,'小雨','星期六')
































print(a)




