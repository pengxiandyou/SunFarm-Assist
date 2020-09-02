#! /usr/bin/env python  
#! -*- coding:utf-8 -*-  
#====#====#====#====  
#!@Author : px
#!@time   : 2020/8/23 19:40
#!@File   : tail.py
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
# 得到新的挖宝计划
def get_new_plan(plan,type):
    if type not in [1,2]:return []
    new_plan=[]
    # 傻逼了，用插入不就逆序了吗，不过不改了
    for key in reversed(sorted(plan.keys())):
        #print(key)
        for case in  plan.get(key)[2*(type-1):2*type]:#数学方式区分葡萄和高级
            for num in range(case[-1]):
                new_plan.append((key,case[0]))
    #print(len(new_plan),new_plan)
    return new_plan
# 挖宝
def do_dig_trea(level=0,plan=constant.dig_trea_plan,is_buy=False,my_coin=0):
    # 藏宝图数量
    # 普通
    # 高级

    # 根据等级获取计划了藏宝图的数量
    # 再根据是否购买和拥有的金钱调整藏宝图数量
    # 2000*50
    #{'msg': 'success', 'putong': {'id': 585909, 'char_id': '', 'game_user_id': '', 'type': 2, 'category': 0, 'goods_id': , 'num': 80, 'create_time': 1595383426000, 'update_time': 1598265403000, 'islock': 0, 'name': '普通藏宝图', 'fruit_gold_coin': None, 'yield_increase_rate': None, 'time_decrease': None, 'make': None}, 'gaoji': {'id': 616009, 'char_id': 'B7EAC5D6F39858798FFB46F527ECE758', 'game_user_id': 'ddefaccaf5d413e25ae4f5016784de69', 'type': 2, 'category': 0, 'goods_id': 40000002, 'num': 4, 'create_time': 1598075999000, 'update_time': 1598262549000, 'islock': 0, 'name': '高级藏宝图', 'fruit_gold_coin': None, 'yield_increase_rate': None, 'time_decrease': None, 'make': None}}
    respone=utils.get(url=constant.get_map_num_url)
    print(respone)
    common_num=respone.get('putong').get('num')
    high_num = respone.get('gaoji').get('num')

    # 总共只能50次 展示还不能获取已挖次数
    count_num =50
    print("拥有",common_num,high_num)

    can_id=level//10+1
    if can_id>5:can_id=5
    print(can_id)
    pass
    need_common_num=0
    need_high_num=0
    for key in plan.keys():
        if key<=can_id:
            #1:[('common1',0),('common2',0),('high1',0),('high2',0)]
            need_common_num+=sum([x[-1] for x in plan.get(key)[:2]])
            need_high_num+=sum([x[-1] for x in plan.get(key)[2:]])
    # 其实在这里就可一逆序，但后来才发现plan要变，才有这段 其实也可以把can_id传get_new_plan，在里面截取
    # 将不符合等级的计划去掉
    for i in range(5-can_id):
        plan.popitem()#会从后面开始
    print(plan)
    print('需要',need_common_num, need_high_num)
    if need_common_num>common_num:
        if is_buy:
            # 只能买普通
            need_num=need_common_num-common_num
            need_coin=need_num*constant.common_map_price
            if need_coin>my_coin:
                need_coin=my_coin//constant.common_map_price*constant.common_map_price
                need_num=need_coin//constant.common_map_price
            if need_num>0:
                respone=utils.get(url=constant.buy_prop_url.format(constant.treasure_map_id,need_num))
            need_common_num=need_num+common_num
        else:
            need_common_num=common_num
    if need_high_num>high_num:
        need_high_num=high_num
    print('需要', need_common_num, need_high_num)
    if need_common_num>0:
        new_plan=get_new_plan(plan=plan,type=1)
        #print(new_plan)
        for case in new_plan:
            respone=utils.get(url=constant.dig_trea_url.format(case[0],case[-1]))
            print(respone)
        pass
    if need_high_num>0:
        new_plan=get_new_plan(plan=plan,type=2)
        respone = utils.get(url=constant.dig_trea_url.format(case[0], case[-1]))
        print(respone)
        pass
    pass
# 发言
def speak(data=None):
    if data==None:
        data={'msg':'未指定发言','uto':''}
    #print(data.get('uto'))
    if data.get('msg')==None:
        data.setdefault('msg','未指定发言')
    if data.get('uto')==None:
        data.setdefault('uto','')

    respone=utils.post(url=constant.head_url + '/zlpt_qhome_consumer/chatting/send', data=data,is_json=False)
    print(respone)
# 获得可买种子列表
def get_list_of_can_buy_seed(result_type='all')->list:
    respone = utils.get(url=constant.list_seed_url.format(1, 1))
    #print(respone)
    list = respone.get('data').get('list')
    #print(list)
    for i in range(2, respone.get('data').get('countPage') + 1):
        list += utils.get(url=constant.list_seed_url.format(1, i)).get('data').get('list')
    #print(len(list), list)
    respone = utils.get(url=constant.list_seed_url.format(2, 1))
    list += respone.get('data').get('list')
    for i in range(2, respone.get('data').get('countPage') + 1):
        list += utils.get(url=constant.list_seed_url.format(2, i)).get('data').get('list')
    #print(len(list), list)
    if result_type=='simple':
        return [{'id': ele.get('id'), 'name': ele.get('name')} for ele in list]
    if result_type=='more':
        return [{'id': ele.get('id'), 'name': ele.get('name'),'season':ele.get('season'),
                 'seed_gold_coin':ele.get('seed_gold_coin'),'fruit_gold_coin':ele.get('fruit_gold_coin'),
                 'single_season_yield':ele.get('single_season_yield')} for ele in list]
    if result_type=='much':
        return [{'id': ele.get('id'),'level':ele.get('level'),'name': ele.get('name'), 'season': ele.get('season'),
                 'access_way':ele.get('access_way'),'type':ele.get('type'),
                 'seed_gold_coin': ele.get('seed_gold_coin'), 'fruit_gold_coin': ele.get('fruit_gold_coin'),
                 'single_season_yield': ele.get('single_season_yield'),'single_season_exp':ele.get('single_season_exp'),
                 'germination_duration':ele.get('germination_duration'),'leaflet_duration':ele.get('leaflet_duration'),
                 'largeleaf_duration':ele.get('largeleaf_duration'),'initialmaturity_duration':ele.get('initialmaturity_duration'),
                 'mature_duration':ele.get('mature_duration')} for ele in list]
    return list
# 仓库种子列表
def get_list_of_warehouse_seed(result_type='all')->list:
    respone=utils.get(url=constant.warehouse_package_seed_all_url.format(1)).get('data')
    print(respone)
    seed_list=respone.get('list')
    seed_count=respone.get('count')
    page_count=respone.get('countPage')
    for i in range(2,page_count+1):
        seed_list+=utils.get(url=constant.warehouse_package_seed_all_url.format(i)).get('data').get('list')

    if result_type == 'simple':
        return [{'id':ele.get('goods_id'),'num':ele.get('num'),'name':ele.get('name')} for ele in seed_list]

    return seed_list
    pass
# 将[{'id':id}]转换为{id:{'id':id}}
def list_to_dict(list)->dict:
    dict={}
    for ele in list:
        dict[ele.get('id')]=ele
    return dict
# 根据计划购买种子
def buy_seed_by_plan(plan=None,coin=0,mycoin=0):
    pass
# 得到某一种子在仓库的数量
def get_num_of_seed(id=None)->list:
    if id is None:
        return [[None, 0]]
    return get_num_of_seeds([id])
# 得到一组种子在仓库的数量
def get_num_of_seeds(seeds=None)->list:
    seed_dict = list_to_dict(get_list_of_warehouse_seed(result_type='simple'))
    if seeds is None:
        return [[e,seed_dict.get(e).get('num')] for e in seed_dict.keys()]
    seed_num_list=[]
    for seed in seeds:
        seed_num_list.append([seed,seed_dict.get(seed, {}).get('num',0)])
    return seed_num_list
# 种子信息信息整合
# 一个种子
# [{}]
def get_seed_message_r_list()->list:
    get_seeds_message_r_list()
    pass
# {id:{}}
def get_seed_message_r_dict()->list:
    get_seeds_message_r_dict()
    pass

# 一组种子
# [{}]
def get_seeds_message_r_list()->list:
    pass
# {id:{}}
def get_seeds_message_r_dict()->list:
    pass
if __name__ == '__main__':
    is_run=True
    if is_run:
        if  utils.get_time(2)%10==0:
            do_dig_trea(level=40,plan={1:[('common1',5),('common2',5),('high1',0),('high2',0)],
                   2:[('common1',5),('common2',5),('high1',0),('high2',0)],
                   3:[('common1',5),('common2',5),('high1',0),('high2',0)],
                   4:[('common1',10),('common2',10),('high1',0),('high2',0)],
                   5:[('common1',0),('common2',0),('high1',0),('high2',0)]},is_buy=False)# false则不需要输入金钱
        else:
            do_dig_trea(level=40,plan={1:[('common1',0),('common2',0),('high1',0),('high2',0)],
                   2:[('common1',0),('common2',0),('high1',0),('high2',0)],
                   3:[('common1',0),('common2',0),('high1',0),('high2',0)],
                   4:[('common1',1),('common2',1),('high1',0),('high2',0)],
                   5:[('common1',0),('common2',0),('high1',0),('high2',0)]},is_buy=False)# 每天任务
    speak(data={'msg':'233'})
    #print(get_list_of_can_buy_seed(result_type='simple'))
    # result=get_list_of_warehouse_seed(result_type='simple')
    # print(result, len(result))
