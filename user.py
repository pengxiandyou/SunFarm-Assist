#! /usr/bin/env python  
#! -*- coding:utf-8 -*-  
#====#====#====#====  
#!@Author : px
#!@time   : 2020/8/22 22:28
#!@File   : user.py
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
import constant
import utils
# 听说导入的话，默认就是单例，因为生成一个文件。而且这个程序不打算用多线程。
'''
{'msg': 'success', 'data': {'id': 4193, 'char_id': 'B7EAC5D6F39858798FFB46F527ECE758', 'game_user_id': 'ddefaccaf5d413e25ae4f5016784de69', 'sow_times': 2817, 'mischief_times': 1373, 'salefruit': 214180, 'steal_times': 939, 'dogbite_times': 744, 'guard_times': 1096, 'treasuremap_times': 315, 'chemical_times': 389, 'dogfood_times': 179, 'rarefruits_num': 17918, 'medal_id': 8, 'single_fruitsnum': 24511, 'double_fruitsnum': 138721, 'single_rarefruitsnum': 0, 'double_rarefruitsnum': 17918}}
{'msg': 'success', 'data': {'id': 4486, 'char_id': 'B7EAC5D6F39858798FFB46F527ECE758', 'game_user_id': 'ddefaccaf5d413e25ae4f5016784de69', 'gold_coin': 127609, 'yuanbao': 0, 'exp': 24788, 'level': 40, 'open_space': 13, 'red_space': 7, 'black_space': 0, 'gold_space': 0, 'violetgold_space': 0, 'amethyst_space': 0, 'vip_time': None, 'dog': 20000003, 'dog_time': 1598271067000, 'consecutive_checkIns': 48, 'oneKey_time': 1598007705000, 'specimen_num': 201, 'harvestedfruit': 138692, 'nickname': 'Je t＇aime', 'steal': None, 'drought': None, 'rough': None, 'wormy': None}}
'''
class User:
    # B7EAC5D6F39858798FFB46F527ECE758
    char_id=None
    # ddefaccaf5d413e25ae4f5016784de69
    game_user_id=None
    # 钱
    gold_coin=None
    # 经验
    exp=None
    # 等级
    level=None
    ##############
    # 土地
    # 普通土地
    open_space=None
    # 红土地
    red_space=None
    # 黑土地
    black_space=None
    # 金土地
    gold_space=None
    # 紫金土地
    violetgold_space=None
    # 紫晶土地
    amethyst_space=None
    ##################
    # 狗
    dog=None
    dog_name={20000001:'田园犬',20000002:'苏格兰牧羊犬',20000003:'斑点狗'}
    # 狗粮到期时间
    dog_time=None
    # 连续登录
    consecutive_checkIns=None
    # 一键
    oneKey_time=None
    # 已制标本数量
    specimen_num=None
    # 收获的水果数量
    harvestedfruit=None
    # 昵称
    nickname=None
    # 播种次数
    sow_times=None
    # 恶作剧次数？
    mischief_times=None
    # 售卖果实数量
    salefruit=None
    # 偷窃次数
    steal_times=None
    # 狗咬次数 不清是自己狗咬 还是偷取被咬
    dogbite_times=None
    # 守卫次数
    guard_times=None
    # 挖宝次数
    treasuremap_times=None
    # 施肥次数
    chemical_times=None
    # 喂狗次数
    dogfood_times=None
    # 稀有果实
    rarefruits_num=None
    # 佩戴勋章id 共14
    medal_id=None
    medal={1:'古怪的农夫',2:'了不起的收割者',3:'破坏者',4:'果实狂热者',5:'神偷小飞侠',6:'栽培大师',7:'作物歼灭者',8:'我可能是条咸鱼',9:'小怪兽在此',10:'农场地主',11:'有米之人',12:'化肥大户',13:'招猫逗狗',14:'厉害了我的哥'}
    # 这个月当前果实数
    single_fruitsnum=None
    #
    double_fruitsnum=None
    #
    single_rarefruitsnum=None
    #
    double_rarefruitsnum=None

    #####################
    # 不清不楚
    vip_time=None
    steal=None
    drought=None
    rough=None
    wormy=None


    def __init__(self):
        information=self.__get_user_information()
        #print(information)
        self.__set_user_information(information=information)

    def __get_user_information(self):
        information1=utils.get(url=constant.user_info_other_url).get('data')
        information2=utils.get(url=constant.user_info_main_url).get('data')
        information2.update(information1)
        return information2

    def __set_user_information(self,information):
        self.char_id = information.get('char_id')
        self.game_user_id=information.get('game_user_id')
        self.gold_coin=information.get('gold_coin')
        self.exp=information.get('exp')
        self.level=information.get('level')
        self.open_space=information.get('open_space')
        self.red_space=information.get('red_space')
        self.black_space=information.get('black_space')
        self.gold_space=information.get('gold_space')
        self.violetgold_space=information.get('violetgold_space')
        self.amethyst_space=information.get('amethyst_space')
        self.dog=information.get('dog')
        self.dog_time=information.get('dog_time')
        self.consecutive_checkIns=information.get('consecutive_checkIns')
        self.oneKey_time=information.get('oneKey_time')
        self.specimen_num=information.get('specimen_num')
        self.harvestedfruit=information.get('harvestedfruit')
        self.nickname=information.get('nickname')
        self.sow_times=information.get('sow_times')
        self.mischief_times=information.get('mischief_times')
        self.salefruit=information.get('salefruit')
        self.steal_times=information.get('steal_times')
        self.dogbite_times=information.get('dogbite_times')
        self.guard_times=information.get('guard_times')
        self.treasuremap_times=information.get('treasuremap_times')
        self.chemical_times=information.get('chemical_times')
        self.dogfood_times=information.get('dogfood_times')
        self.rarefruits_num=information.get('rarefruits_num')
        self.medal_id=information.get('medal_id')
        self.single_fruitsnum=information.get('single_fruitsnum')
        self.double_fruitsnum=information.get('double_fruitsnum')
        self.single_rarefruitsnum=information.get('single_rarefruitsnum')
        self.double_rarefruitsnum=information.get('double_rarefruitsnum')
        pass
    def refresh_user_information(self):
        information = self.__get_user_information()
        self.__set_user_information(information=information)

    def toString(self):
        information=f'你的char_id是{constant.green.format(self.char_id)},game_user_id是{constant.green.format(self.game_user_id)}。\n' \
                    f'你的昵称是{constant.green.format(self.nickname)}.你佩戴的勋章是{constant.green.format(self.medal.get(self.medal_id))}。\n' \
                    f'你共连续登录{constant.green.format(self.consecutive_checkIns)}天。现在' \
                    f'等级是{constant.green.format(self.level)},经验是{constant.green.format(self.exp)}，拥有金钱{constant.green.format(self.gold_coin)}。\n' \
                    f'你拥有普通土地{constant.green.format(self.open_space)}块，红土地{constant.green.format(self.red_space)}块，' \
                    f'黑土地{constant.green.format(self.black_space)}块，金土地{constant.green.format(self.gold_space)}块，' \
                    f'紫金土地{constant.green.format(self.violetgold_space)}块，紫晶土地{constant.green.format(self.amethyst_space)}块，' \
                    f'共{constant.green.format(self.open_space+self.black_space+self.red_space+self.gold_space+self.violetgold_space+self.amethyst_space)}块土地。\n' \
                    f'你的狗狗是{constant.green.format(self.dog_name.get(self.dog))}，到期时间是{constant.green.format(self.dog_time)}，喂它次数是{constant.green.format(self.dogfood_times)}，' \
                    f'守卫次数是{constant.green.format(self.guard_times)}。你被咬次数{constant.green.format(self.dogbite_times)}。\n' \
                    f'你的一键到期时间是{constant.green.format(self.oneKey_time)}。\n' \
                    f'你目前播种{constant.green.format(self.sow_times)}次，施肥{constant.green.format(self.chemical_times)}次，' \
                    f'收获的水果数量是{constant.green.format(self.harvestedfruit)}，拥有{constant.green.format(self.rarefruits_num)}稀有果实，' \
                    f'共制{constant.green.format(self.specimen_num)}个标本,售卖果实{constant.green.format(self.salefruit)}个。\n' \
                    f'你共挖宝{constant.green.format(self.treasuremap_times)}次。\n' \
                    f'这个月你收获{constant.green.format(self.single_fruitsnum)}果实。\n'\
                    f'你恶作剧{constant.green.format(self.mischief_times)}次数(？), 偷窃{constant.green.format(self.steal_times)}次。\n' \
                    f'double_fruitsnum:{constant.green.format(self.double_fruitsnum)} ' \
                    f'single_rarefruitsnum:{constant.green.format(self.single_rarefruitsnum)}' \
                    f' double_rarefruitsnum:{constant.green.format(self.double_rarefruitsnum)}'
        return information
    ################

user=User()
if __name__ == '__main__':
    #print(User().toString())
    #print(constant.green.format('wo he ni'),250,251)
    pass