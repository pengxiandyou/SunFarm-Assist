#! /usr/bin/env python  
#! -*- coding:utf-8 -*-  
#====#====#====#====  
#!@Author : px
#!@time   : 2020/8/16 22:50
#!@File   : main.py
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
'''
主要是主页面。
将主页面分成三个部分，head 、middle、 tail。
头部用于处理活动和签到，中间用于处理集市和土地，尾部用于处理商店和挖宝和发言

'''
import constant
import utils
import json
import head
import tail
from user import User
import os.path
import middle
# respones=requests.post(url=constant.buy_seed_url.format(3,10),headers=utils.set_header())
# data=respones.json()
# print(data)
def store_market_data(data):
    # 将集市数据存起来
    pass
def load_market_data()->list:
    return []
def get_plan_of_buy_seed()->list:
    # 默认服务器不会有超过等级的集市物品
    # 根据集市数据制定购买计划
    # 未使用金钱来限制计划，所以会让价格低的计划在前面，至于在那里实现，我是在计划最终生成时
    load_market_data()
    return []
def get_plan_of_plant(buy_plan=None,coin=None)->list:
    # 根据购买计划和仓库和金钱 使仓库有相应数量的物品 并根据仓库制定计划
    # 注 计划[-1]一定要有默认计划保底
    if buy_plan is None:
        buy_plan=get_plan_of_buy_seed()
    if coin is None:
        coin=User.gold_coin
    return constant.plant_plan
def get_plan_by_warehouse()->list:
    #根据仓库里有啥种啥
    #如果仓库里没有，会在种植时购买牧草，如果仓库里还没有就会报错，所以要求你有较多钱，不过50个牧草才三千多金币。
    pass
def dump_plan(plan):
    utils.json_dump('plan.json',data=plan)
def load_plan():
    return utils.json_load('plan.json')
def do_1_times():
    # 默认你钱较多 大概几十万（误）
    # 挖宝
    if utils.get_time(2) % 10 == 0:  # 每十天一次挖50次 不够就买，钱不够就能买多少买多少
        tail.do_dig_trea(level=User.level, plan={1: [('common1', 5), ('common2', 5), ('high1', 0), ('high2', 0)],
                                                 2: [('common1', 5), ('common2', 5), ('high1', 0), ('high2', 0)],
                                                 3: [('common1', 5), ('common2', 5), ('high1', 0), ('high2', 0)],
                                                 4: [('common1', 10), ('common2', 10), ('high1', 0), ('high2', 0)],
                                                 5: [('common1', 0), ('common2', 0), ('high1', 0), ('high2', 0)]},
                         is_buy=True, my_coin=User.gold_coin)  # false则不需要输入金钱
    else:
        tail.do_dig_trea(level=40, plan={1: [('common1', 0), ('common2', 0), ('high1', 0), ('high2', 0)],
                                         2: [('common1', 0), ('common2', 0), ('high1', 0), ('high2', 0)],
                                         3: [('common1', 0), ('common2', 0), ('high1', 0), ('high2', 0)],
                                         4: [('common1', 1), ('common2', 1), ('high1', 0), ('high2', 0)],
                                         5: [('common1', 0), ('common2', 0), ('high1', 0), ('high2', 0)]}, is_buy=True,
                         my_coin=User.gold_coin)  # 每天任务
    #聊天
    tail.speak(data={'msg': '233'})
    #种植方面
    if os.path.isfile('plan.json'):
        plan=utils.json_load('plan,json')
    else:
        plan=get_plan_of_plant()
    #一键还未实现
    middle.do_farm_work(middle.get_land_data(),plan=plan)
    if len(plan)==1:
        #可传入购买计划和金钱
        plan=get_plan_of_plant()
    #签到
    head.sign(is_print=True)
    head.sign_total_situation(is_print=True)
    #活动
    #activity_3_times寻宝次数，my_coin我拥有的钱，活动3——寻宝需要，people_list表白的人列表，可以传入好友列表，默认是我的小号，记得修改，confession_statement_list表白语句列表，有默认，is_run_list针对4个活动的运行否，默认寻宝不执行，可以短，缺少的都是不执行
    #和集市有关的活动在一直运行里可以多次执行或者一天结束前执行，内部未实现
    head.do_activity(activity_3_times=50,my_coin=User.gold_coin,people_list=None,confession_statement_list=None,is_run_list=None)
    #集市
    head.do_sun_market()
    head.add_order()#多次运行时，需要执行一次
    #做阳光事务
    head.do_sun_affair()
    #领取和开启
    head.receive_and_turnOn()

    #保存数据
    utils.json_dump('plan.json',data=plan)
    pass
if __name__ == '__main__':
    '''大致思路
       先执行tail.py的相关函数：挖宝、聊天，
       接着再执行middle.py相关函数：在种植方面，根据计划种植，而计划可以用集市数据生成。
       关于计划，先用集市生成的，再用仓库种子和金钱生成最终计划，将计划保存和读取。
       关于没有钱和仓库里空空如也，那是你的事，自己实现相关代码。
       循环种植等方面。
       head.py里签到不考虑到循环。
       活动要考虑部分执行和部分循环。
       集市要放到循环。

       循环尾部需要更新用户信息

       在运行结束或一天即将结束要运行阳光事务相关代码和保存数据。
    '''
    do_1_times()
    with open('day.json') as  f:
        temp_day = json.load(f)
    today = utils.get_time(2)
    pass