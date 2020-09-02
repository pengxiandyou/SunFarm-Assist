#! /usr/bin/env python  
#! -*- coding:utf-8 -*-  
#====#====#====#====  
#!@Author : px
#!@time   : 2020/8/31 22:03
#!@File   : test3.py
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
import tail
import utils
import os.path
import constant
import re
import head
def tt(t):
    t[0]=50
if __name__ == '__main__':
    # seed_list = tail.get_list_of_can_buy_seed(result_type='more')
    # seed_list_dict = tail.list_to_dict(seed_list)
    # print(seed_list_dict)
    # data=utils.json_load('market_id.json')
    # print(data)
    # utils.json_dump('233.json',data=data)
    id=[52,48,49,50,51]
    print([i+9*5 for i in id])
    print(utils.get_time(1))
    print(os.path.isfile('day.json'))
    t=[1,5,3]
    print(t)
    tt(t)
    print(t)
    print(len(constant.plant_plan))
    t1=[[1,2],[2,3]]
    t1[0][-1]=4
    print(len(t1))
    # data=utils.get(url=constant.head_url + '/zlpt_qhome_consumer/tfygmc/order/ygmcAddorderlist')
    # print(data)
    # it=re.finditer('\(\d+/\d+\)',data.get('condition'))
    # for e in it:
    #     print(e.group())

    str1='(42/50)'
    str2='(485136/200000)'
    print(str1[1:-1],str2[1:-1])
    a,b=str1[1:-1].split('/')
    print(int(a)-int(b))
    head.do_sun_market()
    head.add_order()
    # l=tail.get_list_of_warehouse_seed()
    # d=tail.list_to_dict(list=l)
    # print(d)
    # dd=[[d.get(e).get('id'),d.get(e).get('num')] for e in d.keys()]
    # print(dd)
    # seed_list=None
    # print(tail.get_num_of_seeds(seed_list))
    # print(tail.get_num_of_seed(233))
    # #print([(33,1),(1,-1)].index((3,-1)))
    # a=4
    # try:
    #     print(a)
    #     i=[(33,1),(1,-1)].index((3,-1))
    #     print(a*a)
    # except ValueError:
    #     i=-1
    #     print(a+i)
    # print(i)
    d=[[627077, 33], [627018, 1], [626965, 1], [626106, 1], [626105, 1], [625288, 1], [620195, 1], [620194, 1], [620088, 1], [620084, 1], [619420, 1], [619408, 1], [619404, 2], [619201, 1]]
    plan=[(627077, 33),(3,-1)]
    pass