#!/usr/bin/python 3.10
# -*- coding: utf-8 -*- 
#
# @Time    : 2022-12-29 17:30
# @Author  : 发发
# @QQ      : 1315337973
# @GitHub  : https://github.com/lovely-fafa
# @File    : 1_python实现.py
# @Software: PyCharm


import requests
import js2py


def get_params(music_id):
    js_content = open(r'./0_逆向过程文件/2_js.js', encoding='utf-8', mode='r').read()
    context = js2py.EvalJs()
    context.execute(js_content)
    res = context.getData(music_id).to_dict()
    params = {'params': res['encText'], 'encSecKey': res['encSecKey']}

    return params


def get_lrc(music_id):
    url = 'https://music.163.com/weapi/song/lyric?csrf_token='
    resp = requests.post(url=url, params=get_params(music_id=music_id))
    lrc_text = resp.json()['lrc']['lyric']
    return lrc_text


if __name__ == '__main__':
    lrc = get_lrc(music_id='2008225969')
    print(lrc)

