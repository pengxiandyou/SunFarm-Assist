#! /usr/bin/env python  
#! -*- coding:utf-8 -*-  
#====#====#====#====  
#!@Author : px
#!@time   : 2020/8/24 22:07
#!@File   : test1.py
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
mp=[{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'},
{'msg': '您今天已经挖了50次了，不能进行挖宝哦~，明天再来吧'}
]
import constant
import utils
import json
from user import user
import pickle
import requests
import head
import tail
if __name__ == '__main__':
    # print(len(mp))
    # #{'msg': 'success', 'data': {'list': [{'id': 1, 'level': 0, 'name': '白萝卜', 'season': 1, 'access_way': 0, 'type': 0, 'seed_gold_coin': 45, 'seed_yuanbao': 0, 'fruit_gold_coin': 4, 'fruit_yuanbao': 0, 'single_season_yield': 25, 'single_season_exp': 8, 'germination_duration': 120, 'leaflet_duration': 300, 'largeleaf_duration': 480, 'initialmaturity_duration': 600, 'mature_duration': 900, 'gold_proceed': 5, 'exp_proceed': 1, 'daily_purchase': 5000, 'pictorial_type1': 0, 'pictorial_type2': 0, 'pictorial_type3': '蔬菜Ⅲ', 'image': '101'}, {'id': 2, 'level': 0, 'name': '胡萝卜', 'season': 1, 'access_way': 0, 'type': 0, 'seed_gold_coin': 50, 'seed_yuanbao': 0, 'fruit_gold_coin': 5, 'fruit_yuanbao': 0, 'single_season_yield': 27, 'single_season_exp': 10, 'germination_duration': 120, 'leaflet_duration': 300, 'largeleaf_duration': 480, 'initialmaturity_duration': 900, 'mature_duration': 1200, 'gold_proceed': 0, 'exp_proceed': 0, 'daily_purchase': 5000, 'pictorial_type1': 0, 'pictorial_type2': 0, 'pictorial_type3': '蔬菜Ⅲ', 'image': '101'}, {'id': 3, 'level': 0, 'name': '牧草', 'season': 1, 'access_way': 0, 'type': 0, 'seed_gold_coin': 67, 'seed_yuanbao': 0, 'fruit_gold_coin': 3, 'fruit_yuanbao': 0, 'single_season_yield': 30, 'single_season_exp': 6, 'germination_duration': 60, 'leaflet_duration': 240, 'largeleaf_duration': 300, 'initialmaturity_duration': 600, 'mature_duration': 600, 'gold_proceed': 0, 'exp_proceed': 0, 'daily_purchase': 5000, 'pictorial_type1': 0, 'pictorial_type2': 3, 'pictorial_type3': '其他', 'image': '101'}, {'id': 8, 'level': 1, 'name': '大白菜', 'season': 1, 'access_way': 0, 'type': 0, 'seed_gold_coin': 269, 'seed_yuanbao': 0, 'fruit_gold_coin': 16, 'fruit_yuanbao': 0, 'single_season_yield': 34, 'single_season_exp': 19, 'germination_duration': 600, 'leaflet_duration': 1200, 'largeleaf_duration': 1800, 'initialmaturity_duration': 3600, 'mature_duration': 3600, 'gold_proceed': 0, 'exp_proceed': 0, 'daily_purchase': 5000, 'pictorial_type1': 0, 'pictorial_type2': 0, 'pictorial_type3': '蔬菜Ⅰ', 'image': '101'}, {'id': 9, 'level': 1, 'name': '大葱', 'season': 1, 'access_way': 1, 'type': 0, 'seed_gold_coin': 269, 'seed_yuanbao': 0, 'fruit_gold_coin': 17, 'fruit_yuanbao': 0, 'single_season_yield': 32, 'single_season_exp': 19, 'germination_duration': 600, 'leaflet_duration': 1200, 'largeleaf_duration': 1800, 'initialmaturity_duration': 3600, 'mature_duration': 3600, 'gold_proceed': 0, 'exp_proceed': 0, 'daily_purchase': 5000, 'pictorial_type1': 1, 'pictorial_type2': 2, 'pictorial_type3': '清爽蓝绿', 'image': '101'}, {'id': 10, 'level': 1, 'name': '大蒜', 'season': 1, 'access_way': 0, 'type': 0, 'seed_gold_coin': 267, 'seed_yuanbao': 0, 'fruit_gold_coin': 20, 'fruit_yuanbao': 0, 'single_season_yield': 27, 'single_season_exp': 19, 'germination_duration': 600, 'leaflet_duration': 1200, 'largeleaf_duration': 1800, 'initialmaturity_duration': 3600, 'mature_duration': 3600, 'gold_proceed': 0, 'exp_proceed': 0, 'daily_purchase': 5000, 'pictorial_type1': 0, 'pictorial_type2': 0, 'pictorial_type3': '蔬菜Ⅲ', 'image': '101'}, {'id': 13, 'level': 3, 'name': '水稻', 'season': 1, 'access_way': 0, 'type': 0, 'seed_gold_coin': 266, 'seed_yuanbao': 0, 'fruit_gold_coin': 22, 'fruit_yuanbao': 0, 'single_season_yield': 25, 'single_season_exp': 20, 'germination_duration': 600, 'leaflet_duration': 1200, 'largeleaf_duration': 1800, 'initialmaturity_duration': 3600, 'mature_duration': 3600, 'gold_proceed': 0, 'exp_proceed': 0, 'daily_purchase': 5000, 'pictorial_type1': 0, 'pictorial_type2': 0, 'pictorial_type3': '蔬菜Ⅲ', 'image': '101'}, {'id': 14, 'level': 3, 'name': '小麦', 'season': 1, 'access_way': 0, 'type': 0, 'seed_gold_coin': 267, 'seed_yuanbao': 0, 'fruit_gold_coin': 23, 'fruit_yuanbao': 0, 'single_season_yield': 24, 'single_season_exp': 20, 'germination_duration': 600, 'leaflet_duration': 1200, 'largeleaf_duration': 1800, 'initialmaturity_duration': 3600, 'mature_duration': 3600, 'gold_proceed': 0, 'exp_proceed': 0, 'daily_purchase': 5000, 'pictorial_type1': 0, 'pictorial_type2': 0, 'pictorial_type3': '蔬菜Ⅲ', 'image': '101'}, {'id': 16, 'level': 5, 'name': '玉米', 'season': 1, 'access_way': 0, 'type': 0, 'seed_gold_coin': 357, 'seed_yuanbao': 0, 'fruit_gold_coin': 25, 'fruit_yuanbao': 0, 'single_season_yield': 30, 'single_season_exp': 26, 'germination_duration': 900, 'leaflet_duration': 1500, 'largeleaf_duration': 2400, 'initialmaturity_duration': 3600, 'mature_duration': 6000, 'gold_proceed': 0, 'exp_proceed': 0, 'daily_purchase': 5000, 'pictorial_type1': 0, 'pictorial_type2': 0, 'pictorial_type3': '蔬菜Ⅲ', 'image': '101'}, {'id': 17, 'level': 5, 'name': '鲜姜', 'season': 1, 'access_way': 1, 'type': 0, 'seed_gold_coin': 320, 'seed_yuanbao': 0, 'fruit_gold_coin': 28, 'fruit_yuanbao': 0, 'single_season_yield': 24, 'single_season_exp': 23, 'germination_duration': 600, 'leaflet_duration': 1200, 'largeleaf_duration': 1800, 'initialmaturity_duration': 3600, 'mature_duration': 5400, 'gold_proceed': 0, 'exp_proceed': 0, 'daily_purchase': 5000, 'pictorial_type1': 1, 'pictorial_type2': 3, 'pictorial_type3': '其他', 'image': '101'}], 'count': 103, 'pageIndex': 1, 'pageSize': 10, 'countPage': 11}}
    # respone=utils.get(url=constant.list_seed_url.format(1,1))
    # print(respone)
    # list=respone.get('data').get('list')
    # print(list)
    # for i in range(2,respone.get('data').get('countPage')+1):
    #     list+=utils.get(url=constant.list_seed_url.format(1,i)).get('data').get('list')
    # print(len(list), list)
    # respone = utils.get(url=constant.list_seed_url.format(2, 1))
    # list += respone.get('data').get('list')
    # for i in range(2,respone.get('data').get('countPage')+1):
    #     list+=utils.get(url=constant.list_seed_url.format(2,i)).get('data').get('list')
    # print(len(list), list)
    # with open('seed.json','w') as f:
    #     s=json.dump(list,f)
    # print(s)
    # with open('user','wb') as f:
    #     pickle.dump(user.user,f)
    # with open('user','rb') as f:
    #     use=pickle.load(f)
    #     use.toString()
    #     print(user.User,type(use))
    # print(use.toString())
    # #print(user.user.toString())
    # print(22)
    #print([7, 15, 25].index(15))
    #print(utils.post(url=constant.buy_seed_url.format(3,10)))
    #print(utils.get(url=constant.head_url+'/zlpt_qhome_consumer/tfquser/'))
    #发言
    #print(utils.post(url=constant.head_url+'/zlpt_qhome_consumer/chatting/send',data={'msg':'我是夜猫子3号，晚上好','uto':''},headers=utils.set_header(),is_json=False))
    #祈福信息
    #print(utils.get(url=constant.head_url+'/zlpt_qhome_consumer/ygmc/spin/getSpinInfo?size=100'))#?page=1&size=10
    #print(len({'spinNum': 2, 'orderNum': 2, 'list': [{'id': 14286, 'char_id': '6C58B5AF4F00F1E72F43646F72DC7FB5', 'game_user_id': '82F80E7C794F85DED81BE32653811484', 'text': "<font color='#9932cc'>(๑• . •๑)</font>获得了七夕礼包,获得了金币10000,快速化肥*2,高级藏宝图*1", 'create_time': 1598320610000, 'nickname': '肥猫'}, {'id': 14285, 'char_id': '07B76A666B88AD11444D3BAA50D50946', 'game_user_id': 'EE55E2E0FE72D1BFE5463B7D298D5722', 'text': "<font color='#9932cc'>思念是一场花瓣雨，浪漫是一场太阳雨。</font>获得了金币28282", 'create_time': 1598320574000, 'nickname': '那年'}, {'id': 14284, 'char_id': 'C74C77A0A523A676A09D1ADC00A5E3A4', 'game_user_id': '7153E1F1959A8CEE679A2BE7BDC011BA', 'text': "<font color='#9932cc'>在天愿为比翼鸟，在地愿为连理枝！</font>获得了金币777", 'create_time': 1598319253000, 'nickname': '庅'}, {'id': 14283, 'char_id': 'BA52DAA7646266D40B000C573318FB96', 'game_user_id': '964F62B554FF885811ECD1517CEAB33D', 'text': "<font color='#9932cc'>美</font>获得了金币10163", 'create_time': 1598317258000, 'nickname': '暮裳'}, {'id': 14282, 'char_id': 'BA52DAA7646266D40B000C573318FB96', 'game_user_id': '964F62B554FF885811ECD1517CEAB33D', 'text': "<font color='#9932cc'>美</font>获得了七夕种子包,获得了枇杷种子*1", 'create_time': 1598317250000, 'nickname': '暮裳'}, {'id': 14281, 'char_id': 'BA52DAA7646266D40B000C573318FB96', 'game_user_id': '964F62B554FF885811ECD1517CEAB33D', 'text': "<font color='#9932cc'>美</font>获得了金币29109", 'create_time': 1598317241000, 'nickname': '暮裳'}, {'id': 14280, 'char_id': '07B76A666B88AD11444D3BAA50D50946', 'game_user_id': '85C8C36DFFF6614CCA08B5BA030A8FEC', 'text': "<font color='#9932cc'>织云弄巧，飞星传恨，银汉昭昭暗渡。金凤玉露一相逢，便胜却人间无数。</font>获得了七夕化肥包(小),获得了急速化肥*1", 'create_time': 1598317067000, 'nickname': '那年'}, {'id': 14279, 'char_id': '07B76A666B88AD11444D3BAA50D50946', 'game_user_id': '85C8C36DFFF6614CCA08B5BA030A8FEC', 'text': "<font color='#9932cc'>织云弄巧，飞星传恨，银汉昭昭暗渡。金凤玉露一相逢，便胜却人间无数。</font>获得了七夕化肥包(大),获得了急速化肥*2", 'create_time': 1598317063000, 'nickname': '那年'}, {'id': 14278, 'char_id': 'FB27007E0D2CD7115E8ADE99EAD05950', 'game_user_id': '5E09E16EA0C2F0150DD8C66948D93911', 'text': "<font color='#9932cc'>思念是一场花瓣雨，浪漫是一场太阳雨。</font>获得了金币271", 'create_time': 1598315339000, 'nickname': '霜至'}, {'id': 14277, 'char_id': 'F239EB9B7133C0FD3906CA617948EAD8', 'game_user_id': '94102CEFD5F7F3CC8A3F1D50A4238AAA', 'text': "<font color='#9932cc'>爱是牛郎织女痴情的等待，漫长的轮回，忠贞的相守。</font>获得了金币16660", 'create_time': 1598315276000, 'nickname': '飞鸽衔黄叶'}, {'id': 14276, 'char_id': 'F239EB9B7133C0FD3906CA617948EAD8', 'game_user_id': '94102CEFD5F7F3CC8A3F1D50A4238AAA', 'text': "<font color='#9932cc'>在天愿为比翼鸟，在地愿为连理枝！</font>获得了七夕化肥包(小),获得了急速化肥*1", 'create_time': 1598315245000, 'nickname': '飞鸽衔黄叶'}, {'id': 14275, 'char_id': '85C8C36DFFF6614CCA08B5BA030A8FEC', 'game_user_id': '8162C7154316DFFA5C1C2A8AC0B271A6', 'text': "<font color='#9932cc'>在天愿为比翼鸟，在地愿为连理枝！</font>获得了七夕化肥包(小),获得了急速化肥*1", 'create_time': 1598314471000, 'nickname': '盖天帝'}, {'id': 14274, 'char_id': 'B904B367C4C5C564BD3861A25A079FF2', 'game_user_id': '15C63A084F36062DA175A63BF6069CE1', 'text': "<font color='#9932cc'>不是最好的时光里有你在，而是你在，我才有了最好的时光。</font>获得了七夕化肥包(小),获得了高级化肥*1", 'create_time': 1598313673000, 'nickname': '幸福的猪'}, {'id': 14273, 'char_id': 'B904B367C4C5C564BD3861A25A079FF2', 'game_user_id': '15C63A084F36062DA175A63BF6069CE1', 'text': "<font color='#9932cc'>在天愿为比翼鸟，在地愿为连理枝！</font>获得了七夕礼包,获得了金币10000,快速化肥*2,高级藏宝图*1", 'create_time': 1598313662000, 'nickname': '幸福的猪'}, {'id': 14272, 'char_id': '90045422A1F2A9C31B4213C2104DA972', 'game_user_id': '363AB489AFE7F20BA2C34D7A9114B415', 'text': "<font color='#9932cc'>不是最好的时光里有你在，而是你在，我才有了最好的时光。</font>获得了七夕挖宝包,获得了高级藏宝图*1", 'create_time': 1598312878000, 'nickname': '12312333'}, {'id': 14271, 'char_id': '90045422A1F2A9C31B4213C2104DA972', 'game_user_id': '363AB489AFE7F20BA2C34D7A9114B415', 'text': "<font color='#9932cc'>不是最好的时光里有你在，而是你在，我才有了最好的时光。</font>获得了流萤礼包,获得了金币10000,快速化肥*2,一键卡(1天)*1", 'create_time': 1598312869000, 'nickname': '12312333'}, {'id': 14270, 'char_id': '90045422A1F2A9C31B4213C2104DA972', 'game_user_id': '363AB489AFE7F20BA2C34D7A9114B415', 'text': "<font color='#9932cc'>不是最好的时光里有你在，而是你在，我才有了最好的时光。</font>获得了七夕种子包,获得了六出花种子*1", 'create_time': 1598312844000, 'nickname': '12312333'}, {'id': 14269, 'char_id': '4DB6D3FEC781367EDAFB6ACBAA1F95BC', 'game_user_id': '07AFAD35243BF5622F9F9D65C3DD7F67', 'text': "<font color='#9932cc'>我愿做你的小尾巴，你走到哪我就随到哪。</font>获得了金币323", 'create_time': 1598311992000, 'nickname': '無'}, {'id': 14268, 'char_id': '4DB6D3FEC781367EDAFB6ACBAA1F95BC', 'game_user_id': '07AFAD35243BF5622F9F9D65C3DD7F67', 'text': "<font color='#9932cc'>我愿做你的小尾巴，你走到哪我就随到哪。</font>获得了金币22089", 'create_time': 1598311989000, 'nickname': '無'}, {'id': 14267, 'char_id': '4DB6D3FEC781367EDAFB6ACBAA1F95BC', 'game_user_id': '07AFAD35243BF5622F9F9D65C3DD7F67', 'text': "<font color='#9932cc'>我愿做你的小尾巴，你走到哪我就随到哪。</font>获得了金币952", 'create_time': 1598311984000, 'nickname': '無'}, {'id': 14266, 'char_id': '4DB6D3FEC781367EDAFB6ACBAA1F95BC', 'game_user_id': '07AFAD35243BF5622F9F9D65C3DD7F67', 'text': "<font color='#9932cc'>我愿做你的小尾巴，你走到哪我就随到哪。</font>获得了七夕种子包,获得了蓝铃花种子*1", 'create_time': 1598311980000, 'nickname': '無'}, {'id': 14265, 'char_id': '4DB6D3FEC781367EDAFB6ACBAA1F95BC', 'game_user_id': '07AFAD35243BF5622F9F9D65C3DD7F67', 'text': "<font color='#9932cc'>我愿做你的小尾巴，你走到哪我就随到哪。</font>获得了七夕种子包,获得了冬瓜种子*1", 'create_time': 1598311977000, 'nickname': '無'}, {'id': 14264, 'char_id': '07AFAD35243BF5622F9F9D65C3DD7F67', 'game_user_id': '4DB6D3FEC781367EDAFB6ACBAA1F95BC', 'text': "<font color='#9932cc'>思念是一场花瓣雨，浪漫是一场太阳雨。</font>获得了七夕礼包,获得了金币10000,快速化肥*2,高级藏宝图*1", 'create_time': 1598311814000, 'nickname': '舞'}, {'id': 14263, 'char_id': '07AFAD35243BF5622F9F9D65C3DD7F67', 'game_user_id': '4DB6D3FEC781367EDAFB6ACBAA1F95BC', 'text': "<font color='#9932cc'>思念是一场花瓣雨，浪漫是一场太阳雨。</font>获得了七夕种子包,获得了哈密瓜种子*1", 'create_time': 1598311811000, 'nickname': '舞'}, {'id': 14262, 'char_id': '07AFAD35243BF5622F9F9D65C3DD7F67', 'game_user_id': '4DB6D3FEC781367EDAFB6ACBAA1F95BC', 'text': "<font color='#9932cc'>思念是一场花瓣雨，浪漫是一场太阳雨。</font>获得了七夕种子包,获得了大山樱种子*1", 'create_time': 1598311805000, 'nickname': '舞'}, {'id': 14261, 'char_id': '07AFAD35243BF5622F9F9D65C3DD7F67', 'game_user_id': '4DB6D3FEC781367EDAFB6ACBAA1F95BC', 'text': "<font color='#9932cc'>思念是一场花瓣雨，浪漫是一场太阳雨。</font>获得了七夕挖宝包,获得了普通藏宝图*1", 'create_time': 1598311802000, 'nickname': '舞'}, {'id': 14260, 'char_id': '07AFAD35243BF5622F9F9D65C3DD7F67', 'game_user_id': '4DB6D3FEC781367EDAFB6ACBAA1F95BC', 'text': "<font color='#9932cc'>思念是一场花瓣雨，浪漫是一场太阳雨。</font>获得了金币563", 'create_time': 1598311793000, 'nickname': '舞'}, {'id': 14259, 'char_id': 'EFE8710713C9304D89ABEB874C4FFC55', 'game_user_id': '4E0FE59180ECA5ADA2F555F503E3F67B', 'text': "<font color='#9932cc'>织云弄巧，飞星传恨，银汉昭昭暗渡。金凤玉露一相逢，便胜却人间无数。</font>获得了七夕化肥包(小),获得了快速化肥*1", 'create_time': 1598311668000, 'nickname': '染柒柒'}, {'id': 14258, 'char_id': 'EFE8710713C9304D89ABEB874C4FFC55', 'game_user_id': '4E0FE59180ECA5ADA2F555F503E3F67B', 'text': "<font color='#9932cc'>爱是牛郎织女痴情的等待，漫长的轮回，忠贞的相守。</font>获得了七夕化肥包(小),获得了快速化肥*1", 'create_time': 1598311661000, 'nickname': '染柒柒'}, {'id': 14257, 'char_id': '363AB489AFE7F20BA2C34D7A9114B415', 'game_user_id': '90045422A1F2A9C31B4213C2104DA972', 'text': "<font color='#9932cc'>织云弄巧，飞星传恨，银汉昭昭暗渡。金凤玉露一相逢，便胜却人间无数。</font>获得了金币850", 'create_time': 1598310542000, 'nickname': '油渍净'}, {'id': 14256, 'char_id': '363AB489AFE7F20BA2C34D7A9114B415', 'game_user_id': '90045422A1F2A9C31B4213C2104DA972', 'text': "<font color='#9932cc'>织云弄巧，飞星传恨，银汉昭昭暗渡。金凤玉露一相逢，便胜却人间无数。</font>获得了金币18445", 'create_time': 1598310526000, 'nickname': '油渍净'}, {'id': 14255, 'char_id': 'B5DF83EE87A5389648CAC5DE758DCB16', 'game_user_id': '27640AF4350FE6D8B003E1929C7C6D8E', 'text': "<font color='#9932cc'>无</font>获得了七夕挖宝包,获得了普通藏宝图*1", 'create_time': 1598310144000, 'nickname': '周友堂'}, {'id': 14254, 'char_id': 'B5DF83EE87A5389648CAC5DE758DCB16', 'game_user_id': '543D316BE74FA9B0BD70217BE929B02C', 'text': "<font color='#9932cc'>无</font>获得了金币28022", 'create_time': 1598310075000, 'nickname': '周友堂'}, {'id': 14253, 'char_id': 'EFE8710713C9304D89ABEB874C4FFC55', 'game_user_id': '4E0FE59180ECA5ADA2F555F503E3F67B', 'text': "<font color='#9932cc'>织云弄巧，飞星传恨，银汉昭昭暗渡。金凤玉露一相逢，便胜却人间无数。</font>获得了七夕种子包,获得了彩灯果种子*1", 'create_time': 1598309700000, 'nickname': '染柒柒'}, {'id': 14252, 'char_id': '07B76A666B88AD11444D3BAA50D50946', 'game_user_id': '85C8C36DFFF6614CCA08B5BA030A8FEC', 'text': "<font color='#9932cc'>好希望陪着你一直到老，让你做我手心里的宝。</font>获得了七夕化肥包(小),获得了高级化肥*1", 'create_time': 1598309588000, 'nickname': '那年'}, {'id': 14251, 'char_id': '07B76A666B88AD11444D3BAA50D50946', 'game_user_id': '85C8C36DFFF6614CCA08B5BA030A8FEC', 'text': "<font color='#9932cc'>好希望陪着你一直到老，让你做我手心里的宝。</font>获得了金币311", 'create_time': 1598309584000, 'nickname': '那年'}, {'id': 14250, 'char_id': '07B76A666B88AD11444D3BAA50D50946', 'game_user_id': '85C8C36DFFF6614CCA08B5BA030A8FEC', 'text': "<font color='#9932cc'>好希望陪着你一直到老，让你做我手心里的宝。</font>获得了金币430", 'create_time': 1598309578000, 'nickname': '那年'}, {'id': 14249, 'char_id': '85C8C36DFFF6614CCA08B5BA030A8FEC', 'game_user_id': 'B45029086B49780242B01E3226AEE320', 'text': "<font color='#9932cc'>在天愿为比翼鸟，在地愿为连理枝！</font>获得了七夕化肥包(小),获得了快速化肥*1", 'create_time': 1598308796000, 'nickname': '盖天帝'}, {'id': 14248, 'char_id': '85C8C36DFFF6614CCA08B5BA030A8FEC', 'game_user_id': 'EE55E2E0FE72D1BFE5463B7D298D5722', 'text': "<font color='#9932cc'>不是最好的时光里有你在，而是你在，我才有了最好的时光。</font>获得了七夕挖宝包,获得了高级藏宝图*1", 'create_time': 1598304236000, 'nickname': '盖天帝'}, {'id': 14247, 'char_id': 'BDA86A54554EE1C08C40998F4ABD96D9', 'game_user_id': '17430B2EF7D812C0D3888FBE6CB780B9', 'text': "<font color='#9932cc'>好希望陪着你一直到老，让你做我手心里的宝。</font>获得了七夕化肥包(小),获得了急速化肥*1", 'create_time': 1598302193000, 'nickname': '缘'}, {'id': 14246, 'char_id': 'B7EAC5D6F39858798FFB46F527ECE758', 'game_user_id': 'CCAD69C2262CC29CDB8084EC76053BAE', 'text': "<font color='#9932cc'>在天愿为比翼鸟，在地愿为连理枝！</font>获得了七夕种子包,获得了豆角种子*1", 'create_time': 1598294004000, 'nickname': 'Je t＇aime'}, {'id': 14245, 'char_id': 'B7EAC5D6F39858798FFB46F527ECE758', 'game_user_id': 'CCAD69C2262CC29CDB8084EC76053BAE', 'text': "<font color='#9932cc'>在天愿为比翼鸟，在地愿为连理枝！</font>获得了七夕种子包,获得了桔梗花种子*1", 'create_time': 1598293996000, 'nickname': 'Je t＇aime'}, {'id': 14244, 'char_id': '1C480D9EDECAB99F870F5348BD8EFB4E', 'game_user_id': 'E5382897DFB984ADAA4E76FAFBDD7CC3', 'text': "<font color='#9932cc'>不是最好的时光里有你在，而是你在，我才有了最好的时光。</font>获得了七夕种子包,获得了樱桃种子*1", 'create_time': 1598292577000, 'nickname': '醉翁之意不在酒'}, {'id': 14243, 'char_id': '1C480D9EDECAB99F870F5348BD8EFB4E', 'game_user_id': 'E5382897DFB984ADAA4E76FAFBDD7CC3', 'text': "<font color='#9932cc'>不是最好的时光里有你在，而是你在，我才有了最好的时光。</font>获得了七夕化肥包(小),获得了急速化肥*1", 'create_time': 1598292573000, 'nickname': '醉翁之意不在酒'}, {'id': 14242, 'char_id': 'D110892934CAC0D8B739AF6FCF39C96C', 'game_user_id': '69C5F7638DA2BA8E7F84BE6DAE7CD621', 'text': "<font color='#9932cc'>织云弄巧，飞星传恨，银汉昭昭暗渡。金凤玉露一相逢，便胜却人间无数。</font>获得了金币9140", 'create_time': 1598289125000, 'nickname': '星★叶'}, {'id': 14241, 'char_id': 'D110892934CAC0D8B739AF6FCF39C96C', 'game_user_id': '69C5F7638DA2BA8E7F84BE6DAE7CD621', 'text': "<font color='#9932cc'>思念是一场花瓣雨，浪漫是一场太阳雨。</font>获得了流萤礼包,获得了金币10000,快速化肥*2,一键卡(1天)*1", 'create_time': 1598289117000, 'nickname': '星★叶'}, {'id': 14240, 'char_id': 'D110892934CAC0D8B739AF6FCF39C96C', 'game_user_id': '69C5F7638DA2BA8E7F84BE6DAE7CD621', 'text': "<font color='#9932cc'>织云弄巧，飞星传恨，银汉昭昭暗渡。金凤玉露一相逢，便胜却人间无数。</font>获得了七夕礼包,获得了金币10000,快速化肥*2,高级藏宝图*1", 'create_time': 1598289112000, 'nickname': '星★叶'}, {'id': 14239, 'char_id': 'F8C137DB264B3E7BC1F7630EEEB7B0C8', 'game_user_id': 'D43E9B3B8700165B5E3376CA3C7165D2', 'text': "<font color='#9932cc'>织云弄巧，飞星传恨，银汉昭昭暗渡。金凤玉露一相逢，便胜却人间无数。</font>获得了七夕化肥包(小),获得了快速化肥*1", 'create_time': 1598287335000, 'nickname': '黄药师'}, {'id': 14238, 'char_id': '85C8C36DFFF6614CCA08B5BA030A8FEC', 'game_user_id': '13EBE3EDFE2636747DBA62810696F15F', 'text': "<font color='#9932cc'>在天愿为比翼鸟，在地愿为连理枝！</font>获得了金币637", 'create_time': 1598286907000, 'nickname': '盖天帝'}, {'id': 14237, 'char_id': '64D7D6B0618EF13E2091217DCF3E247D', 'game_user_id': 'D28FEB4AA23FAD26BD3A4ED7A7056777', 'text': "<font color='#9932cc'>织云弄巧，飞星传恨，银汉昭昭暗渡。金凤玉露一相逢，便胜却人间无数。</font>获得了七夕种子包,获得了杨桃种子*1", 'create_time': 1598286222000, 'nickname': '萤火流光'}, {'id': 14236, 'char_id': '64D7D6B0618EF13E2091217DCF3E247D', 'game_user_id': 'D28FEB4AA23FAD26BD3A4ED7A7056777', 'text': "<font color='#9932cc'>织云弄巧，飞星传恨，银汉昭昭暗渡。金凤玉露一相逢，便胜却人间无数。</font>获得了金币923", 'create_time': 1598286220000, 'nickname': '萤火流光'}, {'id': 14235, 'char_id': '64D7D6B0618EF13E2091217DCF3E247D', 'game_user_id': 'D28FEB4AA23FAD26BD3A4ED7A7056777', 'text': "<font color='#9932cc'>织云弄巧，飞星传恨，银汉昭昭暗渡。金凤玉露一相逢，便胜却人间无数。</font>获得了金币825", 'create_time': 1598286218000, 'nickname': '萤火流光'}, {'id': 14234, 'char_id': '64D7D6B0618EF13E2091217DCF3E247D', 'game_user_id': 'D28FEB4AA23FAD26BD3A4ED7A7056777', 'text': "<font color='#9932cc'>织云弄巧，飞星传恨，银汉昭昭暗渡。金凤玉露一相逢，便胜却人间无数。</font>获得了金币949", 'create_time': 1598286215000, 'nickname': '萤火流光'}, {'id': 14233, 'char_id': '64D7D6B0618EF13E2091217DCF3E247D', 'game_user_id': 'D28FEB4AA23FAD26BD3A4ED7A7056777', 'text': "<font color='#9932cc'>织云弄巧，飞星传恨，银汉昭昭暗渡。金凤玉露一相逢，便胜却人间无数。</font>获得了七夕挖宝包,获得了高级藏宝图*1", 'create_time': 1598286210000, 'nickname': '萤火流光'}, {'id': 14232, 'char_id': '07B76A666B88AD11444D3BAA50D50946', 'game_user_id': 'EFE8710713C9304D89ABEB874C4FFC55', 'text': "<font color='#9932cc'>思念是一场花瓣雨，浪漫是一场太阳雨。</font>获得了七夕礼包,获得了金币10000,快速化肥*2,高级藏宝图*1", 'create_time': 1598286077000, 'nickname': '那年'}, {'id': 14231, 'char_id': '07B76A666B88AD11444D3BAA50D50946', 'game_user_id': 'EFE8710713C9304D89ABEB874C4FFC55', 'text': "<font color='#9932cc'>思念是一场花瓣雨，浪漫是一场太阳雨。</font>获得了金币23740", 'create_time': 1598286067000, 'nickname': '那年'}, {'id': 14230, 'char_id': '07B76A666B88AD11444D3BAA50D50946', 'game_user_id': 'EFE8710713C9304D89ABEB874C4FFC55', 'text': "<font color='#9932cc'>思念是一场花瓣雨，浪漫是一场太阳雨。</font>获得了金币5549", 'create_time': 1598286051000, 'nickname': '那年'}, {'id': 14229, 'char_id': '07B76A666B88AD11444D3BAA50D50946', 'game_user_id': 'EFE8710713C9304D89ABEB874C4FFC55', 'text': "<font color='#9932cc'>思念是一场花瓣雨，浪漫是一场太阳雨。</font>获得了金币306", 'create_time': 1598286037000, 'nickname': '那年'}, {'id': 14228, 'char_id': 'D110892934CAC0D8B739AF6FCF39C96C', 'game_user_id': '69C5F7638DA2BA8E7F84BE6DAE7CD621', 'text': "<font color='#9932cc'>在天愿为比翼鸟，在地愿为连理枝！</font>获得了七夕种子包,获得了彩灯果种子*1", 'create_time': 1598285691000, 'nickname': '星★叶'}, {'id': 14227, 'char_id': 'D110892934CAC0D8B739AF6FCF39C96C', 'game_user_id': '69C5F7638DA2BA8E7F84BE6DAE7CD621', 'text': "<font color='#9932cc'>不是最好的时光里有你在，而是你在，我才有了最好的时光。</font>获得了金币734", 'create_time': 1598285684000, 'nickname': '星★叶'}, {'id': 14226, 'char_id': '33566EF72AB799002A4A4FB266D67F21', 'game_user_id': 'C1019A3C6908EF7D87601C2E18E28C6A', 'text': "<font color='#9932cc'>思念是一场花瓣雨，浪漫是一场太阳雨。</font>获得了金币986", 'create_time': 1598285586000, 'nickname': '℡☞℡夜℡雨℡阁℡☜℡'}, {'id': 14225, 'char_id': '33566EF72AB799002A4A4FB266D67F21', 'game_user_id': 'C1019A3C6908EF7D87601C2E18E28C6A', 'text': "<font color='#9932cc'>在天愿为比翼鸟，在地愿为连理枝！</font>获得了七夕挖宝包,获得了高级藏宝图*1", 'create_time': 1598285576000, 'nickname': '℡☞℡夜℡雨℡阁℡☜℡'}, {'id': 14224, 'char_id': 'B3113248FD53EF923E40FCF23838C7A3', 'game_user_id': '75CD4711F486BB0E8EFAEF3BAF5EF81D', 'text': "<font color='#9932cc'>在天愿为比翼鸟，在地愿为连理枝！</font>获得了金币397", 'create_time': 1597978540000, 'nickname': '小鹿'}, {'id': 14223, 'char_id': '54B165E93410FB7027012F4F215A5517', 'game_user_id': '8AC04A10906726F9127F690DB8061047', 'text': "<font color='#9932cc'>七夕的情，最真，因为有永恒的爱恋牵系。</font>获得了流萤礼包,获得了金币10000,快速化肥*2,一键卡(1天)*1", 'create_time': 1597806144000, 'nickname': '一给我里giaogiao'}]}.get('list')))
    # 小号 friendUid=CCAD69C2262CC29CDB8084EC76053BAE=char_id
    # 表白
    # print(utils.get(url=constant.head_url+'/zlpt_qhome_consumer/ygmc/spin/confession?friendUid={}&note={}'.format('CCAD69C2262CC29CDB8084EC76053BAE','测试')))
    # l=[1,2,3,4,5,6,7,8,9]
    # times=27+8+1
    # print(times%len(l))
    # ll=[22222]
    # print(times % len(ll))
    # type 0包裹种子1仓库2包裹道具 category -1全部0普通1稀有 make -1几乎都是1已制标2未制标0可制标
    #print(utils.get(url=constant.warehouse_package_seed_all_url.format(1)))
    #499
    #market_list=head.get_market_list(result_type='simple')
    # with open('market.json','w') as f:
    #     json.dump(market_list,f)
    #print(market_list,'\n' ,len(market_list))
    # with open('market_id.json','w') as f:# 没有则添加
    #     json.dump({499:{"id": 499,'order_id_list':{170330:0,170336:0},
    #                617:{"id": 617,'order_id_list':},
    #                1548:{"id": 1548,'order_id_list':},
    #                1632:{"id": 1632,'order_id_list':}},f)
    # with open('market_order_id.json', 'w') as f:
    #     json.dump({170330:{'num':0,'requirementMapList':{},'gold_coin':0,'sum_gold_coin':0},#309{id:309,name:"马蹄莲",need:27,have:0,season:3,'seed_gold_coin':9293,'fruit_gold_coin':285,"single_season_yield": 30,’sell‘:30*3*285-9293},{}
    #                170336:{'num':0,'requirementMapList':{},'gold_coin':0,'sum_gold_coin':0}},f)
    market_list = head.get_market_list(result_type='simple')
    print(market_list)
    seed_list=tail.get_list_of_can_buy_seed(result_type='more')
    seed_list_dict=tail.list_to_dict(seed_list)
    with open('market_id.json') as f:
        market_id=json.load(f)
    print("market_id",market_id)

    with open('market_order_id.json') as f:
        market_order_id=json.load(f)

    print('market_order_id',market_order_id)

    with open('market_gen_time.json') as f:
        market_gen_time=json.load(f)
    print('market_gen_time',market_gen_time)

    for ele in market_list:
        # 判断是否在时间字典里，以及是否是新订单
        id=ele.get('id')
        str_id=str(id)
        generateorder_time=ele.get('generateorder_time')
        if market_gen_time.get(str_id)==generateorder_time:#说明已经记录过了，不是新订单，不管
            continue
        market_gen_time[str_id]=generateorder_time#没有则添加，有则修改

        # 是否是删除的订单
        order_id = ele.get('order_id')
        if order_id==0:continue

        str_order_id = str(order_id)
        # 开始相关数据处理
        # 统计order_id
        if str_id not in market_id.keys():
            market_id[str_id]={'id':id,'order_id_list':{}}
        order_id_list=market_id.get(str_id).get('order_id_list')
        if str_order_id not in order_id_list.keys():
            order_id_list[str_order_id]=1
        else:
            order_id_list[str_order_id]+=1
        # 统计关于每一个order_id
        if str_order_id not in market_order_id.keys():
            market_order_id[str_order_id]={'num':0,'requirementMapList':{},'gold_coin':0,'sum_gold_coin':0}
        market_order_id[str_order_id]['num']+=1
        market_order_id[str_order_id]['gold_coin']=ele.get('gold_coin')
        market_order_id[str_order_id]['sum_gold_coin']+=ele.get('gold_coin')
        print(ele.get('requirementMapList'))
        for e in ele.get('requirementMapList'):
            seed_id=e.get("果实id")
            #print(seed_id)
            seed_name=e.get("果实名称")
            need=e.get("所需数量")
            have=e.get("库存")
            season=seed_list_dict.get(seed_id).get('season')
            seed_gold_coin=seed_list_dict.get(seed_id).get('seed_gold_coin')
            fruit_gold_coin=seed_list_dict.get(seed_id).get('fruit_gold_coin')
            single_season_yield=seed_list_dict.get(seed_id).get('single_season_yield')
            sell=single_season_yield*season*fruit_gold_coin-seed_gold_coin
            if str(seed_id) not in market_order_id.get(str_order_id).get('requirementMapList').keys():
                market_order_id[str_order_id]['requirementMapList'][seed_id]={'id':seed_id,'name':seed_name,
                                                                              'need':need,
                                                                              'have':have,'season':season,
                                                                              'seed_gold_coin':seed_gold_coin,
                                                                              'fruit_gold_coin':fruit_gold_coin,
                                                                              'single_season_yield':single_season_yield,
                                                                              'sell':sell}
            else:
                temp=market_order_id[str_order_id]['requirementMapList'][seed_id]
                temp['need']+=need
                temp['have']=have
                temp['sell']+=sell
    with open('market_id.json','w') as f:
        json.dump(market_id,f)
    print("market_id",market_id)
    with open('market_order_id.json','w') as f:
        json.dump(market_order_id,f)
    print('market_order_id',market_order_id)
    with open('market_gen_time.json','w') as f:
        json.dump(market_gen_time,f)
    print('market_gen_time',market_gen_time)
    f.close()
    pass