# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:48:02 2018
爬取百度网页数据，用http:// 而不是其他
题目十一：爬取百度网页数据
1.爬取百度搜索标题
2.爬取标题下的描述
3.搜索的标题的网站
@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='http://www.baidu.com/s?ie=utf-8&mod=1&isbd=1&isid=890cf7af000072b1&ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E7%94%B0%E9%A6%A5%E7%94%84%E5%92%8C%E6%9E%97%E4%BF%8A%E6%9D%B0&oq=%25E7%2594%25B0%25E9%25A6%25A5%25E7%2594%2584%25E5%2592%258C%25E6%259E%2597%25E4%25BF%258A%25E6%259D%25B0&rsv_pq=890cf7af000072b1&rsv_t=1af2pEB81nWG%2FXd%2FDTjY%2Fas6ARjmMvsuHZFIDNNtlZLQSciClwPKNS%2FK9iE&rqlang=cn&rsv_enter=0&prefixsug=%25E7%2594%25B0%25E9%25A6%25A5%25E7%2594%2584%25E5%2592%258C%25E6%259E%2597%25E4%25BF%258A%25E6%259D%25B0&rsp=0&bs=%E7%94%B0%E9%A6%A5%E7%94%84%E5%92%8C%E6%9E%97%E4%BF%8A%E6%9D%B0&rsv_sid=undefined&_ss=1&clist=e8c12211fbb4b34b%09307ce5de4977d530%092878738a27cb02b8%09dd554be535e781b6%098c0272c5e32b559a%098c0272c5e32b559a&hsug=&f4s=1&csor=7&_cr1=48689'
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
ls=re.compile('"title":"(.*?)"').findall(data)
la=re.compile('</span>.*</div><div').findall(data)
la1=la[2:12]
lm=re.compile('style="text-decoration:none;">(.*?)&nbsp;</a><').findall(data)
for i in range(len(ls)):    
    print("标题:{}\n描述:{}\n网址:{}\n".format(ls[i],la1[i],lm[i]))

