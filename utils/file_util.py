# !/usr/bin/env python
# --*-- coding:utf-8 --*--
'''
@auther : QinKeXin
@file: file_util.py
@time: 2017/12/28 9:29
@desc:
'''

import os

BASE_PATH = 'D:\\'

def save(name, data):
    name = BASE_PATH + name
    print(name)
    if os.path.exists(name):
        print('已经存在此文件！')
        return False
    file = open(name, 'w')
    file.close()
    try:
        file = open(name, 'wb+')
        file.write(data.encode('UTF-8'))
        file.close()
        return True
    except IOError:
        print('保存失败！')
        return False

def saveImage(name, data):
    name = BASE_PATH + name
    try:
        with open(name, 'wb') as f:
            f.write(data)
    except Exception:
        print('出错')
