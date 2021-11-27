from math import pi
from typing import Tuple


def length_calc(data) -> Tuple[float, int]:
    min_x = 999
    max_x = 0
    max_x_index = -1
    min_x_index = -1

    for i in range(0, len(data)):
        t, x = data[i]
        if (x > max_x):
            max_x = x
            max_x_index = i

        if(x < min_x):
            min_x = x
            min_x_index = i

    dist = max_x - min_x

    if(max_x_index == -1 and min_x_index == -1):
        return (0,dist)

    if(max_x - min_x <= 60):
        return (0,dist)

    total_time = abs(data[max_x_index][0] - data[min_x_index][0])

    # shijian = sum1/len(t_dif_list)  # 获取最终时间
    # print(total_time)
    T = total_time*2
    l = (pow(T, 2)*9.8)/(pow(pi, 2)*4)

    if(l < 0.48):
        # print(l)
        l = 0
    if(l > 1.52):
        # print(l)
        l = 0

    return (l, dist)
