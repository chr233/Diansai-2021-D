'''
# @Author       : Chr_
# @Date         : 2021-11-05 08:28:50
# @LastEditors  : Chr_
# @LastEditTime : 2021-11-07 03:14:32
# @Description  : 
'''

from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from config import DEBUG_MODE

router = APIRouter(prefix='',
                   tags=['根'],
                   dependencies=[],
                   responses={404: {'detail': 'page not found'}},)



@router.get('/')
async def root():
    if DEBUG_MODE:
        return RedirectResponse('/docs')
    else:
        return {'message': 'Hello, World!'}