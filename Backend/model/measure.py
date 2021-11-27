'''
# @Author       : Chr_
# @Date         : 2021-11-06 19:08:05
# @LastEditors  : Chr_
# @LastEditTime : 2021-11-08 02:16:56
# @Description  : 
'''

from pydantic import BaseModel

from enum import Enum


class WhichPi(Enum):
    pi3 = '3'
    pi4 = '4'


class InputData(BaseModel):
    """
    输入数据
    """
    which: WhichPi
    long: float
    dist: float
    ready: bool


class InputImg(BaseModel):
    """
    输入数据
    """
    which: WhichPi
    img: str
