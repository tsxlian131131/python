# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 15:53:24 2018
第八题：保存淘宝数据(小组项目)
1.每个组员爬取100页数据(同一种商品)，条件是北京，上海，广州，成都...
2.保存的商品信息有(同第六题),并且是以为csv格式保存
3.单个组员求出当前城市的商品的众数(最多的价格)
4.小组文件合并，求出商品的平均价格
@author: Administrator
"""

f=open('./shenzhen.csv','w')
f.write('店铺名,商品名,价格,销量,地址\n')
for i in range(0,100):
    import urllib.request as r
    url2='https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=t%E6%81%A4%E7%94%B7&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&loc=%E6%B7%B1%E5%9C%B3&s={}&ajax=true'
    a=44*i
    url=url2.format(a)
    data=r.urlopen(url).read().decode('utf-8')
    import json
    data=json.loads(data)
    l=len(data['mods']['itemlist']['data']['auctions'])
    for a in range(0,l):
        nick=data['mods']['itemlist']['data']['auctions'][a]['nick']#店铺名
        raw_title=data['mods']['itemlist']['data']['auctions'][a]['raw_title']#商品名
        view_price=data['mods']['itemlist']['data']['auctions'][a]['view_price']#价格
        view_sales=data['mods']['itemlist']['data']['auctions'][a]['view_sales']#销量
        item_loc=data['mods']['itemlist']['data']['auctions'][a]['item_loc']#地址
        f.write('{},{},{},{},{}\n'.format(nick,raw_title,view_price,view_sales,item_loc))
    print('第{}页已获取数据'.format(i+1))
f.close()
print('关键词为“t恤男”深圳地区前100页数据获取完成！')
