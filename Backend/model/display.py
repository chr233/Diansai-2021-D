'''
# @Author       : Chr_
# @Date         : 2021-11-05 08:02:37
# @LastEditors  : Chr_
# @LastEditTime : 2021-11-08 01:33:08
# @Description  : 
'''

from pydantic import BaseModel


class ImgResponse(BaseModel):
    imgA: str = ''
    imgB: str = ''


class DataResponse(BaseModel):
    long: str = '0.0'
    angle: str = '0.0'
    readyA:bool = False
    readyB:bool = False


class EnableResponse(BaseModel):
    enable: bool = False
