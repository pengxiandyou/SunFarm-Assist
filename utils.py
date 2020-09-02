#! /usr/bin/env python  
#! -*- coding:utf-8 -*-  
#====#====#====#====  
#!@Author : px
#!@time   : 2020/8/21 20:48
#!@File   : utils.py
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

import time
import requests
import json
# cookie好像是假的，不一样还可以C3C270AC06CE8807E8BF73B9648E4AD5
def set_header():
    header={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
        'Cookie':'JSESSIONID=E242CCF49BD344BFDF5663A205768496; YOMO_LB_COOKIE_Id=YOMOSID_c23a816e-85ad-4e28-a3d1-ce7b91fc1655; login_return_url=http://qqhome.cn/zlpt_qhome_consumer/SunFarm/index.html'
    }
    return header
def get(url, headers=None,data=None,is_json=True):
    if headers is None:
        headers = set_header()
    respones=requests.get(url=url, headers=headers,data=data)
    if is_json:
        return respones.json()
    else:
        return respones

def post(url, headers=None,data=None,is_json=True):
    if headers is None:
        headers = set_header()
    respones=requests.post(url=url, headers=headers,data=data)
    if is_json:
        return respones.json()
    else:
        return respones
def get_wday():
    return time.localtime()[6]+1
def get_time(num=0):
    return time.localtime()[num]
def json_dump(file,data=None):
    try:
        with open(file,'w')as f:
            json.dump(data,f)
            f.close()
    except IOError:
        print('dump失败')
def json_load(file):
    try:
        with open(file)as f:
            data= json.load(f)
            f.close()
    except IOError:
        print('load失败')
    return data
if __name__ == '__main__':
    print(get_wday())
    pass