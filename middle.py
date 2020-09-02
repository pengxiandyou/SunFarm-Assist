#! /usr/bin/env python  
#! -*- coding:utf-8 -*-  
#====#====#====#====  
#!@Author : px
#!@time   : 2020/8/21 20:49
#!@File   : middle.py
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
import tail
# 一键
def oneKey():
    return False
    pass

def get_land_data():
    respone = utils.get(url=constant.plant_url)
    plant = respone
    print(plant)
    data = plant.get('data')
    return data
def post_operate_note(url):
    respone = utils.post(url=url)
    return respone
def get_operate_note(url):
    respone = utils.get(url=url)
    return respone
def find_land_can_plant(landlist):
    newlist=[]
    for land in landlist:
        if land.get('state')==constant.state[2]:
            newlist.append(land)
    return newlist
    pass
def print_land(data,belong=None):
    if data:
        landlits=data.get('list')
        for land in landlits:
            time=land.get('time')
            state=land.get('state')
            drought='[浇水]' if land.get('drought')==constant.drought else ''
            rough = '[除草]' if land.get('rough') == constant.rough else ''
            wormy = '[杀虫]' if land.get('wormy') == constant.wormy else ''
            #steal= '[偷取]' if land.get('steal')==constant.steal  else ''
            message=('' if time==None else time)+state+('[收获]' if '成熟产量' in state else '')+drought+rough+wormy
            print(f'[坑{land.get("landNum"): >2}]{land.get("seedName")}({land.get("currentSeason")}/{land.get("season")}季){message}')
# 找出可种植的
def do_farm_work(data,belong=None,plan=None,onekey=oneKey()):
    if data:
        landlits = data.get('list')
        for land in landlits:
            num=land.get('landNum')
            if land.get('rough') == constant.rough:do_weed(landNum=num)
            if land.get('drought') == constant.drought: do_water(landNum=num)
            if land.get('wormy') == constant.wormy: do_insecticide(landNum=num)
            stale=land.get('state')
            if stale  in constant.state or constant.state[-1] in stale:
                if stale==constant.state[0]:do_reclamation()
                # 未考虑多季植物 直接收获翻地
                if constant.state[-1]  in  stale: do_reward(landNum=num);do_turn_the_ground(landNum=num);
                if stale==constant.state[1]:do_turn_the_ground(landNum=num)
        do_plant(data=get_land_data(),plan=plan)
    pass
# 除草
def do_weed(landNum,belong=None,onekey=oneKey()):
    if landNum:
        note=get_operate_note(constant.weed_url.format(landNum))
        print(note)
    pass
# 浇水
def do_water(landNum,belong=None,onekey=oneKey()):
    if landNum:
        note=get_operate_note(constant.water_url.format(landNum))
        print(note)
    pass
# 杀虫
def do_insecticide(landNum,belong=None,onekey=oneKey()):
    if landNum:
        note=get_operate_note(constant.insecticide_url.format(landNum))
        print(note)
    pass
# 收获
def do_reward(landNum,belong=None,onekey=oneKey()):
    if landNum:
        note = get_operate_note(constant.reward_url.format(landNum))
        print(note)
        pass
    pass
# 翻地
def do_turn_the_ground(landNum,belong=None,onekey=oneKey()):
    if landNum:
        note = get_operate_note(constant.turn_the_ground_url.format(landNum))
        print(note)
        pass
    pass
# 偷取
def do_steal(landNum,belong=None,onekey=oneKey()):
    pass
# 种草
def do_plantGrass(landNum,belong=None,onekey=oneKey()):
    pass
# 放虫
def do_insect(landNum,belong=None,onekey=oneKey()):
    pass
# 开垦
def do_reclamation(grade=None,money=None,belong='my'):
    pass
# 种植
def do_plant(data,plan=None,onekey=oneKey()):
    #钱不够导致空仓库，会报错。不想try。
    if data:
        # 3是牧草 没有牧草了
        if tail.get_num_of_seed(3)[0][-1] == 0:
            utils.post(constant.buy_seed_url.format(3, 24))
        if plan is None:
            plan = constant.plant_plan
        else:
            #暂时默认plan符合仓库里种子，因为在main里会根据仓库生成plan
            try:
                idx=plan.index(constant.plant_plan[0])
            except ValueError:
                idx=-1
            if idx==-1:
                plan.append(constant.plant_plan[0])

        landlist_can_plant=find_land_can_plant(data.get('list'))
        if landlist_can_plant:
            id,num=plan[0]
            for land in landlist_can_plant:
                if num>0:
                    num-=1
                note=get_operate_note(constant.plant_seed_in_lan_url.format(land.get('landNum'),id))
                print(note)
                if num==0:
                    del plan[0]
                    if plan:id,num=plan[0]
            plan[0]=(id,num)
            pass
    pass

if __name__ == '__main__':
    data=get_land_data()
    print_land(data)
    do_farm_work(data)
    data = get_land_data()
    print_land(data)

    pass