'''
# @Author       : Chr_
# @Date         : 2021-11-07 03:39:43
# @LastEditors  : Chr_
# @LastEditTime : 2021-11-08 02:21:52
# @Description  : 
'''

import requests
from base64 import b64encode

import cv2

from config import HOST, WHICH

ImgAPI = f'http://{HOST}/api/img'
DataAPI = f'http://{HOST}/api/data'
StatusAPI = f'http://{HOST}/api/status'
ReportAPI = f'http://{HOST}/api/report/{WHICH}'

Session = requests.session()


def send_img(img):
    try:
        _, img_enc = cv2.imencode('.jpg', img)
        b64_str = b64encode(img_enc).decode('utf-8')
        b64_img = f'data:image/jpg;base64,{b64_str}'
        data = {'which': WHICH, 'img': b64_img}
        resp = Session.post(ImgAPI, json=data)
    except Exception as e:
        print(e)


def send_data(long, dist, ready: bool = False):
    try:
        data = {'which': WHICH, 'long': long, 'dist': dist, "ready": ready}
        resp = Session.post(DataAPI, json=data)

    except Exception as e:
        print(e)


def check_status() -> bool:
    try:
        resp = Session.get(StatusAPI)

        jp = resp.json()

        return jp['enable']

    except Exception as e:
        print(e)
        return False
    
def report():
    try:
        resp = Session.post(ReportAPI)

    except Exception as e:
        print(e)
