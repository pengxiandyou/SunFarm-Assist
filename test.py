#! /usr/bin/env python  
#! -*- coding:utf-8 -*-  
#====#====#====#====  
#!@Author : px
#!@time   : 2020/8/22 10:26
#!@File   : test.py
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
import middle
list=[{'landNum': 1, 'landId': 2, 'seedId': None, 'seedName': None, 'time': None, 'state': '可种植', 'drought': None, 'rough': None, 'wormy': None, 'steal': None, 'image': None, 'currentSeason': None, 'season': None, 'harvestTime': None}, {'landNum': 2, 'landId': 2, 'seedId': 326, 'seedName': '梨', 'time': '10小时8分46秒', 'state': '成熟', 'drought': None, 'rough': None, 'wormy': None, 'steal': None, 'image': None, 'currentSeason': 3, 'season': 4, 'harvestTime': '10小时8分46秒'}, {'landNum': 3, 'landId': 2, 'seedId': 320, 'seedName': '金针菇', 'time': '11小时43分47秒', 'state': '成熟', 'drought': None, 'rough': None, 'wormy': None, 'steal': None, 'image': None, 'currentSeason': 3, 'season': 4, 'harvestTime': '11小时43分47秒'}, {'landNum': 4, 'landId': 2, 'seedId': None, 'seedName': None, 'time': None, 'state': '可种植', 'drought': None, 'rough': None, 'wormy': None, 'steal': None, 'image': None, 'currentSeason': None, 'season': None, 'harvestTime': None}, {'landNum': 5, 'landId': 2, 'seedId': 365, 'seedName': '枇杷', 'time': '16小时23分48秒', 'state': '成熟', 'drought': None, 'rough': None, 'wormy': None, 'steal': None, 'image': None, 'currentSeason': 4, 'season': 4, 'harvestTime': '16小时23分48秒'}, {'landNum': 6, 'landId': 2, 'seedId': 370, 'seedName': '樱桃', 'time': '1小时52分48秒', 'state': '成熟', 'drought': 0, 'rough': 0, 'wormy': 0, 'steal': None, 'image': None, 'currentSeason': 1, 'season': 4, 'harvestTime': '1小时52分48秒'}, {'landNum': 7, 'landId': 2, 'seedId': 254, 'seedName': '风信子', 'time': '7小时23分51秒', 'state': '成熟', 'drought': None, 'rough': None, 'wormy': None, 'steal': None, 'image': None, 'currentSeason': 2, 'season': 2, 'harvestTime': '7小时23分51秒'}, {'landNum': 8, 'landId': 1, 'seedId': 253, 'seedName': '甘蔗', 'time': '7小时13分53秒', 'state': '成熟', 'drought': None, 'rough': None, 'wormy': None, 'steal': None, 'image': None, 'currentSeason': 2, 'season': 2, 'harvestTime': '7小时13分53秒'}, {'landNum': 9, 'landId': 1, 'seedId': 374, 'seedName': '李子', 'time': '3小时30分56秒', 'state': '成熟', 'drought': None, 'rough': None, 'wormy': None, 'steal': None, 'image': None, 'currentSeason': 3, 'season': 4, 'harvestTime': '3小时30分56秒'}, {'landNum': 10, 'landId': 1, 'seedId': 368, 'seedName': '君子兰', 'time': '10小时8分56秒', 'state': '成熟', 'drought': None, 'rough': None, 'wormy': None, 'steal': None, 'image': None, 'currentSeason': 2, 'season': 4, 'harvestTime': '10小时8分56秒'}, {'landNum': 11, 'landId': 1, 'seedId': 476, 'seedName': '雪人', 'time': '8小时28分57秒', 'state': '成熟', 'drought': None, 'rough': None, 'wormy': None, 'steal': None, 'image': None, 'currentSeason': 2, 'season': 5, 'harvestTime': '8小时28分57秒'}, {'landNum': 12, 'landId': 1, 'seedId': 374, 'seedName': '李子', 'time': '5小时52分50秒', 'state': '成熟', 'drought': 0, 'rough': 0, 'wormy': 0, 'steal': None, 'image': None, 'currentSeason': 1, 'season': 4, 'harvestTime': '5小时52分50秒'}, {'landNum': 13, 'landId': 1, 'seedId': 328, 'seedName': '仙人掌', 'time': '10小时4分', 'state': '成熟', 'drought': None, 'rough': None, 'wormy': None, 'steal': None, 'image': None, 'currentSeason': 2, 'season': 4, 'harvestTime': '10小时4分'}, {'landNum': 14, 'landId': 1, 'seedId': 366, 'seedName': '兰花', 'time': '10小时19分2秒', 'state': '成熟', 'drought': None, 'rough': None, 'wormy': None, 'steal': None, 'image': None, 'currentSeason': 2, 'season': 4, 'harvestTime': '10小时19分2秒'}, {'landNum': 15, 'landId': 1, 'seedId': 326, 'seedName': '梨', 'time': '10小时9分3秒', 'state': '成熟', 'drought': None, 'rough': None, 'wormy': None, 'steal': None, 'image': None, 'currentSeason': 2, 'season': 4, 'harvestTime': '10小时9分3秒'}, {'landNum': 16, 'landId': 1, 'seedId': 329, 'seedName': '月季花', 'time': '10小时14分5秒', 'state': '成熟', 'drought': None, 'rough': None, 'wormy': None, 'steal': None, 'image': None, 'currentSeason': 2, 'season': 4, 'harvestTime': '10小时14分5秒'}, {'landNum': 17, 'landId': 1, 'seedId': 308, 'seedName': '无花果', 'time': '10小时19分6秒', 'state': '成熟', 'drought': None, 'rough': None, 'wormy': None, 'steal': None, 'image': None, 'currentSeason': 2, 'season': 3, 'harvestTime': '10小时19分6秒'}, {'landNum': 18, 'landId': 1, 'seedId': 309, 'seedName': '马蹄莲', 'time': '11小时44分9秒', 'state': '成熟', 'drought': None, 'rough': None, 'wormy': None, 'steal': None, 'image': None, 'currentSeason': 2, 'season': 3, 'harvestTime': '11小时44分9秒'}, {'landNum': 19, 'landId': 1, 'seedId': None, 'seedName': None, 'time': None, 'state': '可种植', 'drought': None, 'rough': None, 'wormy': None, 'steal': None, 'image': None, 'currentSeason': None, 'season': None, 'harvestTime': None}, {'landNum': 20, 'landId': 1, 'seedId': 305, 'seedName': '薰衣草', 'time': '10小时4分11秒', 'state': '成熟', 'drought': None, 'rough': None, 'wormy': None, 'steal': None, 'image': None, 'currentSeason': 2, 'season': 3, 'harvestTime': '10小时4分11秒'}, {'landNum': 21, 'landId': 0, 'seedId': None, 'seedName': None, 'time': None, 'state': '可开垦', 'drought': None, 'rough': None, 'wormy': None, 'steal': None, 'image': None, 'currentSeason': None, 'season': None, 'harvestTime': None}, {'landNum': 22, 'landId': 0, 'seedId': None, 'seedName': None, 'time': None, 'state': '可开垦', 'drought': None, 'rough': None, 'wormy': None, 'steal': None, 'image': None, 'currentSeason': None, 'season': None, 'harvestTime': None}, {'landNum': 23, 'landId': 0, 'seedId': None, 'seedName': None, 'time': None, 'state': '可开垦', 'drought': None, 'rough': None, 'wormy': None, 'steal': None, 'image': None, 'currentSeason': None, 'season': None, 'harvestTime': None}, {'landNum': 24, 'landId': 0, 'seedId': None, 'seedName': None, 'time': None, 'state': '可开垦', 'drought': None, 'rough': None, 'wormy': None, 'steal': None, 'image': None, 'currentSeason': None, 'season': None, 'harvestTime': None}]
def find(list):
    newlist=[]
    return newlist
def x(l):
    l.pop(0)
    l.insert(0,66)

if __name__ == '__main__':

    l=[2,3,5,6,4]
    print(l)
    x(l)
    print(l)
    ll=[(22,33),(55,88)]
    a,b=ll[0]
    print(a)
    print(b)
    a=555
    b=666
    del ll[0]
    print(ll)
    ll[0]=(a,b)
    a, b = ll[0]
    print(a)
    print(b)
    print(ll)
    print(''==None)
    d={1:1,2:2,3:3}
    d1={1:2,4:4,5:5}
    print(d.update(d1))
    print(d)
    A=None
    B=None
    C=None
    D=None
    lo=[A,B,C,D]
    for ind,key in zip(range(len(lo)),d):
        lo[ind]=d.get(key)
    print(lo)
    print(A,B,C,D)
    #print(utils.get(url=constant.treasure_hunt_times_url))
    print('{}//{}'.format(22,33))
    print(d.keys())
    print([(1, 0), (2, 00), (3, 0), (4, 0)][2:])
    print([[1, 0], [2, 0], [3, 0], [4, 0]][0:3])
    print([[1, 0], [2, 0], [3, 0], [4, 0]][0:2])
    print([[1, 0], [2, 0], [3, 0], [4, 0]][2:4])
    print([(1, 0), (2, 00), (3, 0), (4, 0)][0:2])
    print([(1, 0), (2, 00), (3, 0), (4, 0)][2:4])
    print(sum([x[1] for x in [('common1', 5), ('common2', 7), ('high1', 0), ('high2', 0)][:2]]))
    #print(utils.get(url=constant.buy_prop_url.format(constant.treasure_map_id,1)))
    ww=(('#',5))
    www=('*',1)
    wwww=('_',3)
    print([ww*5,www*5,wwww*0])

    #print(utils.get(url=constant.dig_trea_url.format(2,'common1')))
    print((22,330) in [(22,330),(44,55),(55,66)])
    pass