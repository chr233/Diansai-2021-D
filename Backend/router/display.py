'''
# @Author       : Chr_
# @Date         : 2021-11-05 07:51:56
# @LastEditors  : Chr_
# @LastEditTime : 2021-11-08 02:29:17
# @Description  :
'''

import math
from math import atan, pi
from os import fwalk
from fastapi import APIRouter

from memdb import Storage
from model.base import CommonResponse

from model.display import ImgResponse, DataResponse, EnableResponse

router = APIRouter(prefix='/api',
                   tags=['显示终端'],
                   dependencies=[],
                   responses={404: {'detail': 'page not found'}},)


@router.get('/img', response_model=ImgResponse)
async def img():
    imgA = Storage['3']['img']
    imgB = Storage['4']['img']

    return {"imgA": imgA, "imgB": imgB}


@router.get('/data', response_model=DataResponse)
async def long():

    if Storage['4']['long'] != 0:
        klong = '4'
    else:
        klong = '3'

    l = Storage[klong]['long']

    if l == 0:
        long = '测量中'
    else:
        long = str(l)[:5] + 'm'

    x1 = Storage['4']['dist']
    x2 = Storage['3']['dist']

    if x2 == 0:
        angle = '测量中'
    else:
        ang = abs(atan((x1/x2)))
        ang = (ang/math.pi)*180
        angle = str(ang)[:5] + '°'

    readyA = Storage['3']['ready']
    readyB = Storage['4']['ready']

    return {'long': long, 'angle': angle,
            'readyA': readyA, 'readyB': readyB}


@router.get('/status/on', response_model=CommonResponse)
async def set_status():

    for key in ['3', '4']:
        Storage[key]['img'] = Storage['data']['img']
        Storage[key]['long'] = 0
        Storage[key]['dist'] = 0
        Storage[key]['ready'] = False

    Storage['data']['enable'] = True

    Storage['data']['recvA'] = False
    Storage['data']['recvB'] = False

    return {"code": 200, "msg": "ok"}
