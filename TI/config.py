'''
# @Author       : Chr_
# @Date         : 2021-11-07 02:46:49
# @LastEditors  : Chr_
# @LastEditTime : 2021-11-07 16:35:48
# @Description  : 
'''

# 提取阈值
LOWERB = (66, 134, 95)
UPPERB = (104, 255, 174)

# 过滤小色块
MIN_W = 10
MIN_H = 50

# 过滤大色块
MAX_W = 640//10
MAX_H = 480//3

RECT_COLOR = (0, 0, 255)

HOST = '192.168.0.85'
WHICH = '4'