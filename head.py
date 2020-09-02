#! /usr/bin/env python  
#! -*- coding:utf-8 -*-  
#====#====#====#====  
#!@Author : px
#!@time   : 2020/8/22 14:44
#!@File   : head.py
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
import re
# 打印签到情况
def print_sign_week_situation(data):
    for week in data:
        name=week.get('name')
        coin=week.get('gold_coin')
        random_seed=week.get('random_seed')
        map_massege = ''
        map=week.get('map')
        if map:
            for key in map.keys():
                map_massege+=key+'*'+str(map.get(key))+','
            map_massege=map_massege[0:-1]
        checkIn=week.get('checkIn')
        massege=((str(coin)+'金币,') if coin else '')+(('随机种子*'+str(random_seed)+',') if random_seed else '')+((map_massege) if map_massege else '')+','+('已签到' if checkIn==1 else '未签到')
        print(f'({name}){massege}')
    pass
def print_sign_today_situation(note):
    print(note)
    pass
def print_sign_total_situation(data):
    today_count=data.get('dayCount')
    received=data.get('received')
    day_7='连续签到7天礼包：阳光礼包(小)'+('领取' if today_count<=7 else '已领取')
    day_15 = '连续签到15天礼包：阳光礼包(中)' + ('领取' if today_count <= 15 else '已领取')
    day_25 = '连续签到25天礼包：阳光礼包(大)' + ('领取' if today_count <= 25 else '已领取')
    print(f'签到总天:{today_count}天，\n{day_7}\n{day_15}\n{day_25}')
    pass
# 周签到情况
#{'msg': 'success', 'data': [{'id': 1, 'name': '星期一', 'gold_coin': 500, 'yuanbao': 0, 'random_seed': 1, 'chemical_fertilizer': None, 'dog_food': None, 'onekey_card': None, 'map': {}, 'checkIn': 1}, {'id': 2, 'name': '星期二', 'gold_coin': 200, 'yuanbao': 0, 'random_seed': None, 'chemical_fertilizer': '{10000001:1}', 'dog_food': None, 'onekey_card': None, 'map': {'增产化肥': 1}, 'checkIn': 1}, {'id': 3, 'name': '星期三', 'gold_coin': 500, 'yuanbao': 0, 'random_seed': 2, 'chemical_fertilizer': None, 'dog_food': None, 'onekey_card': None, 'map': {}, 'checkIn': 1}, {'id': 4, 'name': '星期四', 'gold_coin': 0, 'yuanbao': 0, 'random_seed': None, 'chemical_fertilizer': None, 'dog_food': None, 'onekey_card': '{30000001:1}', 'map': {'一键卡(1天)': 1}, 'checkIn': 1}, {'id': 5, 'name': '星期五', 'gold_coin': 200, 'yuanbao': 0, 'random_seed': None, 'chemical_fertilizer': '{10000002:1}', 'dog_food': None, 'onekey_card': '', 'map': {'快速化肥': 1}, 'checkIn': 1}, {'id': 6, 'name': '星期六', 'gold_coin': 200, 'yuanbao': 0, 'random_seed': None, 'chemical_fertilizer': None, 'dog_food': '{20000011:2}', 'onekey_card': None, 'map': {'狗粮': 2}, 'checkIn': 1}, {'id': 7, 'name': '星期日', 'gold_coin': 200, 'yuanbao': 0, 'random_seed': None, 'chemical_fertilizer': '{10000003:1}', 'dog_food': None, 'onekey_card': None, 'map': {'急速化肥': 1}, 'checkIn': -1}]}
def sign_week_situation(is_print=None):
    respone=utils.get(url=constant.sign_week_situation_url)
    print(respone)
    if is_print:
        print_sign_week_situation(data=respone.get('data'))
    return respone
# 签到天数
def sign_total_situation(is_print=None):
    respone=utils.get(url=constant.sign_sum_url)
    print(respone)
    if is_print:
        print_sign_total_situation(data=respone)
    today_count=respone.get('dayCount')
    print('today_count',today_count)
    # 此处有bug ，如果漏签 可能出问题，因为不知道网站检测连续还是总数，比较垃圾网站，源代码里可见东西太多了
    day_count_list=[7,15,25]
    if today_count in day_count_list:# 8 9 10
        respone_t=utils.get(url=constant.receive_continuous_sign_gift.format(8+day_count_list.index(today_count)))
    return respone
# 签到
# {'note': '您今天已签到过了，请明天再来'}
def sign(is_print=None):
    respone = utils.get(url=constant.sign_url.format(utils.get_wday()))
    print(respone)
    if is_print:
        print_sign_today_situation(note=respone.get('note'))
    return respone
    pass
#活动
#################
'''
我已经40级了 8月和9月不太一样
一个月的活动猜出共有4个（大概率）
1. 收获数量 30000（几乎可以确定）
2. 阳光集市 1-30（有点怀疑）14-22 
3. 寻宝 （没遇到几次的感觉）22-27',' 大概是和好友互动发消息的类似于互发情话，看亲密度（遇到过一次和通过源代码看到一次）

源代码基于8写的，9月有变
1. 不变，但号有变
2. 2-6 集市抽奖
3. 7-13 收获果实开红包
4. 14-20 寻宝
'''

# 92登录 88-100 89-1000 90-10000 91-30000
activity_1_situation_url=constant.activity_1_situation_url
activity_1_fruit_count_url=constant.activity_1_fruit_count_url
activity_1_exchange_url=constant.activity_1_exchange_url

# 活动
# 收获
def do_activity_1():
    fruit_count=utils.get(url=activity_1_fruit_count_url).get('data').get('single_fruitsnum')
    print('fruit_count',fruit_count)
    situation=[]
    message=[]
    #[92,88,89,90,91]可能需要通过源代码获取或者通过数学把月份和数字对应起来
    #8[92,88,89,90,91]
    #9[97,93,94,95,96]
    id_list=[52,48,49,50,51]
    m=utils.get_time(1)
    for e,n in zip([id+m*5 for id in id_list],[0,100,1000,10000,30000]):
        single_situation=utils.get(url=activity_1_situation_url.format(e))
        situation.append(single_situation)
        message.append(f'{e},需要{n}个果实，'+('已领取' if single_situation.get('msg')==0 else '领取'))
        if single_situation.get('msg')==1 and fruit_count>=n:
            respone=utils.get(url=activity_1_exchange_url.format(e))
            msg=respone.get('msg')
            print(respone)
            message[-1]=f'{e},需要{n}个果实，已领取'

    print(situation,message)
    pass


def do_activity_2(type=1):
    #需要集市相关代码
    if type==1:#排名
        pass
    if type==2:#抽奖
        pass
    pass

# 寻宝
def do_activity_3(my_coin,times,coin):
    # 是否执行看设置，要几次，钱够吗，非5次
    # 暂时没写大奖自选代码
    print(my_coin,times,coin)
    can_times=50-utils.get(url=constant.treasure_hunt_times_url).get('drawTime')
    print(can_times)
    if can_times<=50:
        if  times>0 and coin>1000 and my_coin>1000:
            t_coin=my_coin
            if coin>t_coin:
                coin=t_coin
            if times>can_times:
                times=can_times
            need_coin=(times%5)*10000+times//5*45000
            print('need_coin',need_coin)
            if need_coin<=coin:
                coin=need_coin
            times=(coin%45000)//10000+coin//45000*5
            print('times',times)
            times_5=times//5
            times_1=times-times_5*5
            print(times_1,'和',times_5)
            if times_5>0:
                for i in range(times_5):
                    response = utils.get(url=constant.treasure_hunt_5_url)
                    print(response)
            if times_1>0:
                for i in range(times_1):
                    response = utils.get(url=constant.treasure_hunt_1_url)
                    print(response)
            pass

    pass

#表白
def do_activity_4(people_list=None, confession_statement_list=None):
    ##需要集市相关代码
    if confession_statement_list is None:
        confession_statement_list = ['在天愿为比翼鸟，在地愿为连理枝！'
                                        ,'不是最好的时光里有你在，而是你在，我才有了最好的时光。'
                                        ,'好希望陪着你一直到老，让你做我手心里的宝。'
                                        ,'花儿那么美，天空那么蓝，风儿那么凉爽，这一切都是因为，在我身边，一直有你陪伴。'
                                        ,'我愿做你的小尾巴，你走到哪我就随到哪。'
                                        ,'织云弄巧，飞星传恨，银汉昭昭暗渡。金凤玉露一相逢，便胜却人间无数。'
                                        ,'爱是牛郎织女痴情的等待，漫长的轮回，忠贞的相守。'
                                        ,'七夕的情，最真，因为有永恒的爱恋牵系。'
                                        ,'假如真的有鹊桥。我要跟你走到桥的尽头。'
                                        ,'思念是一场花瓣雨，浪漫是一场太阳雨。']
    if people_list is None:#注意修改为自己的好友
        people_list = ['CCAD69C2262CC29CDB8084EC76053BAE']
    situation=utils.get(url=constant.head_url + '/zlpt_qhome_consumer/ygmc/spin/getSpinInfo?page=1&size=10')  # ?page=1&size=10
    # 完成集市次数
    num_of_market=situation.get('orderNum')
    # 拥有纸鹤数量
    num_of_papercrane=num_of_market
    # 使用
    times_of_use_papercrane=situation.get('spinNum')
    times =num_of_papercrane-times_of_use_papercrane
    print('进入了4',times,num_of_market,times_of_use_papercrane)
    if num_of_market>0 and times>0:
        for i in range(times):
            respone=utils.get(url=constant.activity_4_vindicate_url.format(people_list[i%len(people_list)],confession_statement_list[i%len(confession_statement_list)]))
            print(respone)
            pass

    pass

# 开红包
def do_activity_open_redbag():
    pass

def do_activity(activity_3_times=constant.activity3_treasure_hunt_times,my_coin=0,coin=45000*10,people_list=None,confession_statement_list=None,is_run_list=None):
    if is_run_list==None:
        is_run_list=[True,True,False,True]
    while len(is_run_list)<4:
        is_run_list.append(False)
    print(is_run_list)
    if is_run_list[0]:
        do_activity_1()
    # 关于时间的获取，以后会根据源代码或数学关系来控制
    time_day=utils.get_time(2)
    time_m=utils.get_time(1)
    if time_m==8:
        if is_run_list[1] and 14<=time_day<=22:
            do_activity_2(type=1)#集市排名类型 未实现
        if is_run_list[2] and 22<=time_day<=27:
            print('ac3')#寻宝
            do_activity_3(times=activity_3_times,coin=coin,my_coin=my_coin)
        if is_run_list[3] and 25<=time_day:
            # 表白
            do_activity_4(people_list=people_list,confession_statement_list=confession_statement_list)
    if time_m==9:
        if is_run_list[1] and 2 <= time_day <= 6:
            do_activity_2(type=2)  # 集市抽奖类型
        if is_run_list[2] and 7<=time_day<=13:
            do_activity_open_redbag()
        if is_run_list[3] and 14<=time_day<=20:
            do_activity_3(times=activity_3_times, coin=coin, my_coin=my_coin)
#################
# 阳光事务
# 挖宝默认挖
# 使用化肥
def use_3_times_fertilizer():
    #我不打算实现，我不需要
    pass

# 偷好友10次果实
def steal_10_times_friend_fruit(coin=None):
    # 涉及好友列表或者动态里的偷菜和捣乱
    # 暂不打算实现，我都不偷
    if coin is None:
        coin=0
    if  coin>=10000:
        #相关逻辑
        pass
    pass

# 捣乱
def make_trouble_10_times():
    # 涉及好友列表或者动态里的偷菜和捣乱
    # 我的计划是从动态里挑出近两天的人和好友（有多余次数时）
    pass

# 出售果实活动10000金币
def sell_fruit_for_10000_gold():
    # 不打算实现
    pass

# 买5种种子
def buy_5_seeds(plan=None, coin=67 * 5):
    if plan is None:
        plan = [(3, 5)]
    tail.buy_seed_by_plan(plan=plan,coin=coin)
    pass

# 添加狗粮
def add_dog_food():
    pass

# 阳光事务
def do_sun_affair():
    # 空函数，需要自己实现
    use_3_times_fertilizer()
    # 空函数，需要自己实现
    steal_10_times_friend_fruit()

    make_trouble_10_times()
    # 空函数，需要自己实现
    sell_fruit_for_10000_gold()
    # 不想执行，我又不搞心愿树。每天大概80点就行了
    #buy_5_seeds()
    add_dog_food()
    pass
# 阳光事务领取和开启
def receive_and_turnOn():
    pass
##############
# 阳光集市
def get_market_list(result_type='all')->list:
    respone=utils.get(url=constant.get_market_situation_url)
    # [{'id': 499, 'char_id': 'B7EAC5D6F39858798FFB46F527ECE758', 'game_user_id': 'ddefaccaf5d413e25ae4f5016784de69', 'order_num': 1, 'create_time': 1576421224000, 'status': 1, 'order_id': 170318, 'generateorder_time': 1598369064000, 'countdown': None, 'requirementMapList': [{'所需数量': 41, '是否可求助': '否', '果实id': 325, '果实名称': '猕猴桃', '库存': 544}, {'所需数量': 23, '是否可求助': '否', '果实id': 265, '果实名称': '栀子花', '库存': 496}, {'所需数量': 26, '是否可求助': '是', '果实id': 1277, '果实名称': '芦笋', '库存': 4}, {'所需数量': 22, '是否可求助': '否', '果实id': 269, '果实名称': '丝瓜', '库存': 168}], 'gold_coin': 37012, 'npc_image': 5, 'npc': '【斯科特的小店】我的天呐，如今的世道还能相信别人吗，你能给我这个吗'}, {'id': 617, 'char_id': 'B7EAC5D6F39858798FFB46F527ECE758', 'game_user_id': 'ddefaccaf5d413e25ae4f5016784de69', 'order_num': 1, 'create_time': 1578956730000, 'status': 1, 'order_id': 170319, 'generateorder_time': 1598369068000, 'countdown': None, 'requirementMapList': [{'所需数量': 37, '是否可求助': '是', '果实id': 1275, '果实名称': '秋葵', '库存': 18}, {'所需数量': 46, '是否可求助': '是', '果实id': 1277, '果实名称': '芦笋', '库存': 4}, {'所需数量': 39, '是否可求助': '否', '果实id': 142, '果实名称': '月桂花', '库存': 692}], 'gold_coin': 17129, 'npc_image': 9, 'npc': '【贾尔斯的锤子】嘿，前面的游客买的什么好东西，我也要来一份'}, {'id': 1548, 'char_id': 'B7EAC5D6F39858798FFB46F527ECE758', 'game_user_id': 'ddefaccaf5d413e25ae4f5016784de69', 'order_num': 1, 'create_time': 1595081358000, 'status': 1, 'order_id': 170306, 'generateorder_time': 1598368171000, 'countdown': None, 'requirementMapList': [{'所需数量': 20, '是否可求助': '否', '果实id': 1010, '果实名称': '四季豆', '库存': 21}, {'所需数量': 50, '是否可求助': '否', '果实id': 262, '果实名称': '橙子', '库存': 356}, {'所需数量': 50, '是否可求助': '否', '果实id': 8, '果实名称': '大白菜', '库存': 315}, {'所需数量': 48, '是否可求助': '否', '果实id': 268, '果实名称': '葡萄', '库存': 668}], 'gold_coin': 18735, 'npc_image': 10, 'npc': '【奥德丽的农场】做明星，要是不红就得死，要是红了，就是生不如死啊！'}, {'id': 1632, 'char_id': 'B7EAC5D6F39858798FFB46F527ECE758', 'game_user_id': 'ddefaccaf5d413e25ae4f5016784de69', 'order_num': 1, 'create_time': 1598349503000, 'status': 1, 'order_id': 170320, 'generateorder_time': 1598369077000, 'countdown': None, 'requirementMapList': [{'所需数量': 49, '是否可求助': '否', '果实id': 1013, '果实名称': '芥蓝', '库存': 1331}, {'所需数量': 40, '是否可求助': '是', '果实id': 222, '果实名称': '黄豆', '库存': 16}], 'gold_coin': 7947, 'npc_image': 14, 'npc': '【温格丝】今天要去参加舞会，看我的衣服漂亮么？'}]
    #print(respone.get('data'))
    #print(len(respone.get('data')))
    if result_type=='simple':
        return [{'id':ele.get('id'),'order_id':ele.get('order_id'),'generateorder_time':ele.get('generateorder_time'),
                 'requirementMapList':ele.get('requirementMapList'),'gold_coin':ele.get('gold_coin')} for ele in respone.get('data') if ele.get('status')==1]
    return respone.get('data')
    pass


def do_sun_market(seed_list_dict=None,market_id=None,market_order_id=None,market_gen_time=None,is_return=False):
    # 不求助，未实现
    # 这一段时间有点久，应该可以用多线程
    # 获取数据
    market_list = get_market_list(result_type='simple')
    if seed_list_dict==None:
        seed_list = tail.get_list_of_can_buy_seed(result_type='more')
        seed_list_dict = tail.list_to_dict(seed_list)
    # 读取文件 感觉这样写，我就可以在main里尝试使用多线程来搞
    if market_id==None:
        market_id =utils.json_load('market_id.json')
    #print("market_id", market_id)
    if market_order_id==None:
        market_order_id = utils.json_load('market_order_id.json')
    #print('market_order_id', market_order_id)
    if market_gen_time==None:
        market_gen_time = utils.json_load('market_gen_time.json')
    #print('market_gen_time', market_gen_time)
    # 数据处理
    process_id=[]
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
        process=[id,0]
        for e in ele.get('requirementMapList'):
            seed_id=e.get("果实id")
            seed_name=e.get("果实名称")
            need=e.get("所需数量")
            have=e.get("库存")
            if e.get('是否可求助')=='是':process[-1]=1
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
            #print(process)
        process_id.append(process)
    #订单处理
    #提交和删除，不求助，自己实现
    print(process_id)
    for p in process_id:
        if p[-1]==1:
            respone=utils.get(url=constant.delete_order_url.format(p[0]))
            print(respone)
        if p[-1]==0:
            respone=utils.post(url=constant.submit_order_url.format(p[0]))
            print(respone)
    #增加订单
    #单独作为一个函数
    # 数据保存
    if is_return:
        return market_id,market_order_id,market_gen_time
    utils.json_dump('market_id.json',data=market_id)
    utils.json_dump('market_order_id.json', data=market_order_id)
    utils.json_dump('market_gen_time.json', data=market_gen_time)
    #print("market_id",market_id)
def add_order():
    data=utils.get(url=constant.add_market_situation_url)
    print(data)
    it=re.finditer('\(\d+/\d+\)',data.get('condition'))
    flag=True
    for e in it:
        print(e.group())
        a,b=e.group()[1:-1].split('/')
        if int(a)-int(b)<0:flag=False
    if flag:
        reponse=utils.post(url=constant.add_market_list_url)
        print(reponse)

##################
# 获得一种好友列表[char_id]
def get_friend_list(type='my')->list:
    #完整好友
    #动态里的捣乱好友
    return []
########################
# 助人为乐
def help_friend():
    pass
if __name__ == '__main__':
    sign(is_print=True)
    sign_total_situation(is_print=True)
    sign_week_situation(is_print=True)
    do_activity(activity_3_times=50,my_coin=500000)
    do_sun_market()
    add_order()
    pass