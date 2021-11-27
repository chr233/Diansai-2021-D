'''
# @Author       : Chr_
# @Date         : 2021-11-05 12:58:50
# @LastEditors  : Chr_
# @LastEditTime : 2021-11-08 02:28:17
# @Description  : 
'''

from fastapi import APIRouter
from model.display import EnableResponse

from model.measure import InputData, InputImg
from model.base import CommonResponse

from memdb import Storage

router = APIRouter(prefix='/api',
                   tags=['树莓派通信'],
                   dependencies=[],
                   responses={404: {'detail': 'page not found'}},)


@router.post('/data', response_model=CommonResponse)
async def receive_data(data: InputData):
    key = data.which.value

    if data.long != 0:
        Storage[key]['long'] = data.long
    Storage[key]['dist'] = data.dist
    Storage[key]['ready'] = data.ready

    return {"code": 200, "msg": "ok"}


@router.post('/img', response_model=CommonResponse)
async def receive_img(data: InputImg):
    key = data.which.value

    Storage[key]['img'] = data.img

    return {"code": 200, "msg": "ok"}


@router.get('/status', response_model=EnableResponse)
async def get_status():
    enable = Storage['data']['enable']

    return {"enable": enable}


@router.post('/report/3', response_model=CommonResponse)
async def report3():
    Storage['data']['recvA'] = True
    
    if Storage['data']['recvA'] and Storage['data']['recvB'] :
        Storage['data']['enable'] = False

    return {"code": 200, "msg": "ok"}


@router.post('/report/4', response_model=CommonResponse)
async def report4():
    Storage['data']['recvB'] = True

    if Storage['data']['recvA'] and Storage['data']['recvB'] :
        Storage['data']['enable'] = False

    return {"code": 200, "msg": "ok"}