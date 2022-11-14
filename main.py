import json
import os
# -*- coding: utf-8 -*-
import sys
import uuid
import requests
import base64
import hashlib

from importlib import reload


import time

from playsound import playsound

reload(sys)

YOUDAO_URL1 = 'https://openapi.youdao.com/ocrapi'
YOUDAO_URL2 = 'https://openapi.youdao.com/ttsapi'

APP_KEY = '27f20cdcd1bde173'
APP_SECRET = 'BHol0iA5DINxS1z0h6LxReezCfFhfxwJ'


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def encryptmain(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()

def encryptreader(signStr):
    hash_algorithm = hashlib.md5()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()

def do_request1(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL1, data=data, headers=headers)

def do_request2(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL2, data=data, headers=headers)


def connect():
    f = open(r'cut.jpg', 'rb')  # 二进制方式打开图文件
    q = base64.b64encode(f.read()).decode('utf-8')  # 读取文件内容，转换为base64编码
    f.close()

    data = {}
    data['detectType'] = '10012'
    data['imageType'] = '1'
    data['langType'] = 'ru'
    data['img'] = q
    data['docType'] = 'json'
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    sign = encryptmain(signStr)
    data['appKey'] = APP_KEY
    data['salt'] = salt
    data['sign'] = sign

    response = do_request1(data)
    print(json.loads(response.content.decode())['Result']['regions'][0]['lines'])
    ewen=json.loads(response.content.decode())['Result']['regions'][0]['lines'][0]['text'];
    print(json.loads(response.content.decode())['Result']['regions'][0]['lines'][0]['text'])
    return ewen;

def reader(q):
    data = {}
    data['langType'] = 'ru'
    salt = str(uuid.uuid1())
    signStr = APP_KEY + q + salt + APP_SECRET

    sign = encryptreader(signStr)
    data['appKey'] = APP_KEY
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign

    response = do_request2(data)
    contentType = response.headers['Content-Type']
    if contentType == "audio/mp3":
        millis = int(round(time.time() * 1000))
        filePath = os.getcwd() + "\\mp3\\" + str(millis) + ".mp3"
        print(filePath)
        fo = open(filePath, 'wb')
        fo.write(response.content)
        fo.close()
        playsound(filePath)
    else:
        print(response.content)


def mm():
    ewen=connect();
    reader(ewen);