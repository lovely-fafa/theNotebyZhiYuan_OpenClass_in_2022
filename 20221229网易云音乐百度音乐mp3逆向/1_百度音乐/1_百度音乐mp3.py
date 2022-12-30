#!/usr/bin/python 3.10
# -*- coding: utf-8 -*- 
#
# @Time    : 2022-12-30 11:52
# @Author  : 发发
# @QQ      : 1315337973
# @GitHub  : https://github.com/lovely-fafa
# @File    : 1_百度音乐mp3.py
# @Software: PyCharm

import hashlib
import time

import requests


def get_sign(music_id, secret="0b50b02fd0d73a9c4c8c3a781c30845f"):
    timestamp = str(time.time()).split(".")[0]
    md5 = hashlib.md5()
    md5.update(f'TSID={music_id}&appid=16073360&timestamp={timestamp}{secret}'.encode('utf-8'))
    return md5.hexdigest(), timestamp


def get_music_url_filename(music_id):
    sign, timestamp = get_sign(music_id)
    url = f'https://music.91q.com/v1/song/tracklink?sign={sign}&appid=16073360&TSID=T10046204448&timestamp={timestamp}'
    resp = requests.get(url)
    resp_json = resp.json()
    return resp_json['data']['path'], f"{resp_json['data']['title']}.mp3"


def download_music(music_id):
    music_url, filename = get_music_url_filename(music_id=music_id)
    resp = requests.get(url=music_url)
    with open(filename, mode='wb') as f:
        f.write(resp.content)


if __name__ == '__main__':
    download_music('T10046204448')
