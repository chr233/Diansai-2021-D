'''
# @Author       : Chr_
# @Date         : 2021-11-05 13:35:59
# @LastEditors  : Chr_
# @LastEditTime : 2021-11-08 02:15:15
# @Description  : 
'''
from PIL import Image
from base64 import b64encode

Storage = {
    '3': {
        'img': '',
        'long': 0,
        'dist': 0,
        'ready': True
    },
    '4': {
        'img': '',
        'long': 0,
        'dist': 0,
        'ready': True
    },
    'data': {
        'img': '',
        'enable': False,
        'recvA':False,
        'recvB':False
    }
}


def load_demo():
    path = r'img/demo.png'
    with open(path, 'rb') as f:
        file_content = f.read()
        base64_bytes = b64encode(file_content)
        base64_string = base64_bytes.decode('utf-8')
        data = f'data:image/png;base64,{base64_string}'
    Storage['3']['img'] = data
    Storage['4']['img'] = data
    Storage['data']['img'] = data
