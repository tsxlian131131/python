# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 15:52:44 2018
练习六：获取淘宝数据并且展示(只要第一页的商品48个)
1.每一行显示4个商品信息(商品名，价格，付款，店铺名,地址，)
2.列出12排商品
3.给商品排序，从价格高到低
4.给商品排序，按照销量排序
5.商品过滤，只要15天退款的商品，包邮的商品

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E5%A4%96%E5%A5%97&ajax=true'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
for x in range(36):
        a=data['mods']['itemlist']['data']['auctions'][x]['raw_title']
        b=data['mods']['itemlist']['data']['auctions'][x]['item_loc']
        c=data['mods']['itemlist']['data']['auctions'][x]['view_sales']
        d=data['mods']['itemlist']['data']['auctions'][x]['nick']
        e=data['mods']['itemlist']['data']['auctions'][x]['view_price']
        print('商品名为：{},地址为：{},付款人为：{},商铺名为：{},价格为：{}'.format(a,b,c,d,e))
ls=[]
print('价格由高到低')
for i in range(12):
    view_price=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    a=float(view_price)
    ls.append(a)
sorted(ls)
ls1=sorted(ls,reverse=True)
print(ls1)

ls=[]
import re
for i in range(36):
    x=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
    y=re.sub('\D','',x)
    z=int(y)
    ls.append(z)   
sorted(ls)
lls=sorted(ls,reverse=True)
print(ls)


for i in range(36):
    a1=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
    c1=data['mods']['itemlist']['data']['auctions'][i]['view_fee']
    if(c1=='0.00'):
        print('商品名称为{},包邮'.format(a1))

