#!/usr/bin/python 3.10
# -*- coding: utf-8 -*- 
#
# @Time    : 2023-01-02 22:44
# @Author  : 发发
# @QQ      : 1315337973
# @GitHub  : https://github.com/lovely-fafa
# @File    : 1_请求m3u8.py
# @Software: PyCharm

import hashlib
import time
import random

import requests


def get_signature(params):
    up_data_str = '&'.join([f'{i}={str(params[i])}' for i in
                            ['cid', 'expiretime', 'nonce', 'page', 'playerid', 'type', 'uuid']])
    sha1 = hashlib.sha1()
    sha1.update(up_data_str.encode('utf-8'))
    return sha1.hexdigest()


def get_player_id():
    return f"{str(timestamp).replace('.', '')[:13][-7:]}{random.randint(10000000, 99999999)}"


def get_m3u8(params):
    params['playerid'] = get_player_id()
    signature = get_signature(params)
    params['signature'] = signature

    print(params)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Referer': 'https://www.1905.com/'
    }
    resp = requests.get(url='https://profile.m1905.com/mvod/getVideoinfo.php',
                        params=params,
                        headers=headers)
    print(resp.text)


if __name__ == '__main__':
    timestamp = time.time()
    params = {
        'cid': "441891",
        'expiretime': str(timestamp).split('.')[0],
        'nonce': str(timestamp).split('.')[0],
        'page': "https://www.1905.com/vod/play/441891.shtml?fr=vodhome_jsxftj_1",
        'type': "hls",
        'uuid': "1d59ab4d-ac7d-451f-8c1c-203ee2e20de0",
        'callback': 'fnCallback0'
    }
    print(get_m3u8(params=params))
