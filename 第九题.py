# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 10:52:56 2018
题目九：余票查询组项目
1.查询某种火车的余票，动车，高铁，直达，特快....
2.组长将各组员功能汇总
@author: Administrator
"""

##1.联网
import urllib.request as r#导入联网工具包，命令为r
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-07-07&leftTicketDTO.from_station=GZQ&leftTicketDTO.to_station=SHH&purpose_codes=ADULT'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
data=data['data']['result']
p='  '
title='车次{}出发站/到达站{}出发时间/到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
title=title.split(p)
for i in title:
    print(i.center(11),end='')

print()
for a in range(len(data)):
    ls=data[a].split('|')
    if ls[3].startswith('G'):
        ls1=[ls[3],[ls[6],ls[7]],[ls[8],ls[9]],ls[10],ls[32],ls[31],ls[30],ls[21],ls[23],'--',ls[28],'--',ls[29],ls[26],'--',ls[1]]
    for i in ls1:
        print(str(i).center(15).replace('[','').replace(']',''),end='')