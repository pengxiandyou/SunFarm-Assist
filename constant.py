#! /usr/bin/env python  
#! -*- coding:utf-8 -*-  
#====#====#====#====  
#!@Author : px
#!@time   : 2020/8/18 21:50
#!@File   : constant.py
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
# 常量

User_Agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
head_url='http://qqhome.cn'
# 用户信息
user_info_other_url=head_url+'/zlpt_qhome_consumer/tfygmc/userOther'
user_info_main_url=head_url+'/zlpt_qhome_consumer/tfygmc/user'
##################
# 签到
# 每周签到情况
sign_week_situation_url=head_url+'/zlpt_qhome_consumer/tfygmc/gift/checkinGift'
# 签到 id 周几 1 2 3 4 5 6 7
sign_url=head_url+'/zlpt_qhome_consumer/ygmc/checkIn?giftId={}'
# 签到天数
sign_sum_url=head_url+'/zlpt_qhome_consumer/tfygmc/gift/dayCount'
# 领取连续签到的礼包 8 9 10-->7 15 25
receive_continuous_sign_gift=head_url+'/zlpt_qhome_consumer/ygmc/giftPackage?giftId={}'
# 点击种植获得页面 id为第几块田 lanNum
click_plant_url=head_url+'/zlpt_qhome_consumer/SunFarm/plant.html?id={}&make=-1&category=-1&pageIndex=1'

#######################
# 种的植物 即田
plant_url=head_url+'/zlpt_qhome_consumer/tfygmc/land/myplanting/1'
# 农活操作
operate=head_url+'/zlpt_qhome_consumer/ygmc/operate/'
operate_chuhai=operate+'chuhai'+'?land_num={}'

#浇水
water_url=operate_chuhai+'&type=drought'
# 除草
weed_url=operate_chuhai+'&type=rough'
# 杀虫
insecticide_url=operate_chuhai+'&type=wormy'
# 收获
reward_url=operate+'gain?land_num={}'
# 翻地
turn_the_ground_url=operate+'turnFloor?land_num={}'
# 种植
plant_seed_in_lan_url=operate+'sow?land_num={}&seed_id={}'
##########################
# 商店
# post种子购买 id->seed_id num
buy_seed_url=head_url+'/zlpt_qhome_consumer/ygmc/shop/buy?id={}&num={}'
# 种子列表 type 1普通 2稀有
# 道具列表把seed改为prop
# {type} {pageIndex}
list_seed_url=head_url+'/zlpt_qhome_consumer/tfygmc/shop/seed/{}/{}'
# get道具购买 id num
# 普通藏宝图 id=40000001
buy_prop_url=head_url+'/zlpt_qhome_consumer/ygmc/shop/buyProp?id={}&num={}'
############################
#每一块田的状态和需要的处理

# 第几块土地 x0
landNum=[x for x in range(0,25)]
# 土壤类型 普通 红 黑 金 紫金 紫晶
landId=[None,1,2,3,4,5,6]
# 种子编号
seedId=0
# 种子名字
seedName='?'
# 成熟时间
time='?小时？分钟？秒'
# 状态
state=['可开垦','可翻地','可种植','成熟','成熟产量']
# 浇水
drought=1
# 除草
rough=1
# 杀虫
wormy=1
# 偷取
steal=1
# 土地图片(?，大概率不是，应该是植物图片)
image=[]
# 当前季 表示有1，2，3，4 不会使用
currentSeason=[None,1,2,3,4]
# 总共季 表示有1，2，3，4 不会使用
season=[None,1,2,3,4]
# 表面意思收获时间
harvestTime='?小时？分钟？秒'
#######################
# 几乎无关
count=24
pageIndex=1
pageSize=24
countPage=1
###################

# 种植计划
plant_plan=[(3,-1)]
seed_buy_plan=[(3,10)]



####################
# 活动相关
# 寻宝
activity3_treasure_hunt_times=50
treasure_hunt_5_url=head_url+'/zlpt_qhome_consumer/tfygmc/xunbao/drawFive'
treasure_hunt_1_url=head_url+'/zlpt_qhome_consumer/tfygmc/xunbao/drawOne'
treasure_hunt_times_url=head_url+'/zlpt_qhome_consumer/tfygmc/xunbao/getPrize'

# 收获
activity_1_situation_url=head_url+'/zlpt_qhome_consumer/tfygmc/newusergift/receivable/{}'
activity_1_fruit_count_url=user_info_other_url
activity_1_exchange_url=head_url+'/zlpt_qhome_consumer/tfygmc/newusergift/reward/{}'
# 表白
activity_4_situation_url=head_url+'/zlpt_qhome_consumer/ygmc/spin/getSpinInfo?page=1&size=10'
activity_4_all_situation_url=head_url+'/zlpt_qhome_consumer/ygmc/spin/getSpinInfo?size={}'#尽可能大
activity_4_vindicate_url=head_url+'/zlpt_qhome_consumer/ygmc/spin/confession?friendUid={}&&note={}'
# 集市比拼

###################
# 阳光事务

######################
# 阳光集市
get_market_situation_url=head_url+'/zlpt_qhome_consumer/tfygmc/order/myOrder'
#post id
# 提交订单
submit_order_url=head_url+'/zlpt_qhome_consumer/tfygmc/order/submitOrder/{}'
# 删除订单
delete_order_url=head_url+'/zlpt_qhome_consumer/tfygmc/order/deleteOrder/{}'
# 增加订单情况
add_market_situation_url=head_url+'/zlpt_qhome_consumer/tfygmc/order/ygmcAddorderlist'
# post
# 增加订单
add_market_list_url=head_url+'/zlpt_qhome_consumer/tfygmc/order/addQYgmcUserOrderlist'
######################
# 挖宝 id 1.天圣雪山(0级开放) 2.幽暗森林(10级开放) 3.沼泽湿地(20级开放) 4.无尽荒漠(30级开放) 5.神秘孤岛(30级开放)
# 5 最好挖 high1
dig_trea_plan={1:[('common1',5),('common2',5),('high1',0),('high2',0)],
               2:[('common1',5),('common2',5),('high1',0),('high2',0)],
               3:[('common1',5),('common2',5),('high1',0),('high2',0)],
               4:[('common1',10),('common2',10),('high1',0),('high2',0)],
               5:[('common1',0),('common2',0),('high1',0),('high2',0)]}
# 获得藏宝图数量
get_map_num_url=head_url+'/zlpt_qhome_consumer/tfygmc/bag/getCangBaoTu'
# 普通藏宝图jiage
common_map_price=2000
# 普通藏宝图id
treasure_map_id=40000001
# 挖宝url {地图id}{哪一个 如 common1}
dig_trea_url=head_url+'/zlpt_qhome_consumer/tfygmc/treasuremap/wabao/{}/{}'
########################################################

# 仓库
# type 0包裹种子1仓库2包裹道具 category -1全部0普通1稀有 make -1几乎都是1已制标2未制标0可制标
warehouse_url=head_url+'/zlpt_qhome_consumer/tfygmc/bag/{}/{}/{}/{}'
# 全部种子 pageIndex=1
warehouse_package_seed_all_url=head_url+'/zlpt_qhome_consumer/tfygmc/bag/0/-1/-1/{}'
green='\033[1;32m{}\033[0m'

if __name__ == '__main__':
    pass