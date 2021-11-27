'''
# @Author       : Chr_
# @Date         : 2021-11-07 00:27:59
# @LastEditors  : Chr_
# @LastEditTime : 2021-11-08 02:27:45
# @Description  : 
'''

import cv2

from config import RECT_COLOR, UPPERB, LOWERB, MIN_H, MIN_W, MAX_H, MAX_W
from sendpic import send_data, send_img, check_status, report

from length import length_calc


def color_block_finder(img):
    '''
    色块识别 返回矩形信息
    '''
    # 转换色彩空间 HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 根据颜色阈值转换为二值化图像
    img_bin = cv2.inRange(img_hsv, LOWERB, UPPERB)

    # 寻找轮廓（只寻找最外侧的色块）
    contours, hier = cv2.findContours(
        img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    # 外接矩形区域集合
    rects = []

    # 如果最大宽度没有设定，就设定为图像的宽度

    # 遍历所有的边缘轮廓集合
    for cidx, cnt in enumerate(contours):
        # 获取联通域的外界矩形
        (x, y, w, h) = cv2.boundingRect(cnt)

        if MAX_W >= w >= MIN_W and MAX_H >= h >= MIN_H:
            # 将矩形的信息(tuple)添加到rects中
            rects.append((x, y, w, h))

    l = len(rects)

    if l == 1:
        return rects[0]

    elif l > 1:

        sizes = [w*h for _, _, w, h in rects]

        m_size = max(sizes)

        index = sizes.index(m_size)

        return rects[index]

    return None


def draw_color_block_rect(img, rect):
    '''
    绘制色块的矩形区域
    '''
    # 遍历矩形区域
    x, y, w, h = rect
    # 在画布上绘制矩形区域（红框）
    cv2.rectangle(img, pt1=(x, y), pt2=(
        x+w, y+h), color=RECT_COLOR, thickness=3)


def cap_video(cap):
    '''
    捕获视频流
    '''

    count = 0  # 检测数量

    period = 0  # 检测轮数

    enable = False

    data = []

    FREQ = cv2.getTickFrequency()

    while(True):
        succ, img = cap.read()
        count += 1
        if succ:
            h, w, _ = img.shape
            center = (w // 2, h // 2)
            # 旋转中心+旋转角度+旋转比例
            m = cv2.getRotationMatrix2D((center), -4, 1)
            # 图像名称+模型+宽高
            img = cv2.warpAffine(img, m, (w, h))
            img = img[30:-30, 30:-30]

            # 识别色块 获取矩形区域数组
            rect = color_block_finder(img)

            tick = cv2.getTickCount() / FREQ

            # 绘制色块的矩形区域

            if rect:
                draw_color_block_rect(img, rect)
                send_img(img)

                # cv2.imwrite(f'data/result-{i}.jpg', img)

                data.append((tick, rect[0]))
            else:
                print('未检出')
                # count -= 1
                continue

            # print(i)

        else:
            print("视频读取完毕或者视频路径异常")
            # break
            # count -= 1

        if enable:
            if (count >= 100):
                period += 1
                length, dist = length_calc(data)
                send_data(length, dist, False)
                data = []
                count = 0

            if(period >= 4):
                enable = False
                length, dist = length_calc(data)
                send_data(length, dist, True)
                data = []
                period = 0

        else:
            if (count >= 20):
                enable = check_status()
                if enable:
                    report()


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    try:
        cap_video(cap)

    except Exception as e:
        print(e)

    finally:
        cap.release()
