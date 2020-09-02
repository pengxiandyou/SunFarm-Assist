#! /usr/bin/env python  
#! -*- coding:utf-8 -*-  
#====#====#====#====  
#!@Author : px
#!@time   : 2020/8/25 11:42
#!@File   : test2.py
#!License : (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
#====#====#====#====
"""
             ┏┓      ┏┓
            ┏┛┻━━━━━━┛┻┓
            ┃          ┃
            ┃  ┳┛  ┗┳  ┃
            ┃     ┻    ┃
            ┗━┓      ┏━┛
              ┃      ┗━━━┓
              ┃  神兽保佑 ┣┓
              ┃  永无BUG！┏┛
              ┗┓┓┏━━━━┳┓┏┛
               ┃┫┫    ┃┫┫
               ┗┻┛    ┗┻┛
"""
# $
import utils
import constant
import json
if __name__ == '__main__':
    respone=utils.get(url=constant.list_seed_url.format(1,1))
    print(respone)
    list=respone.get('data').get('list')
    print(list)
    for i in range(2,respone.get('data').get('countPage')+1):
        list+=utils.get(url=constant.list_seed_url.format(1,i)).get('data').get('list')
    print(len(list), list)
    respone = utils.get(url=constant.list_seed_url.format(2, 1))
    list += respone.get('data').get('list')
    for i in range(2,respone.get('data').get('countPage')+1):
        list+=utils.get(url=constant.list_seed_url.format(2,i)).get('data').get('list')
    print(len(list), list)
    with open('seed.json','w') as f:
        json.dump(list,f)
    with open('seed.json') as f:
        s=json.load(f)
    print(len(s))
    pass