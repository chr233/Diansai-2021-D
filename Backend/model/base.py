'''
# @Author       : Chr_
# @Date         : 2021-11-06 19:20:46
# @LastEditors  : Chr_
# @LastEditTime : 2021-11-06 20:22:40
# @Description  : 
'''

from typing import Optional
from pydantic import BaseModel


class CommonResponse(BaseModel):
    code: int = 200
    msg: str = 'ok'
    data: Optional[dict] = None
