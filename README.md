# 文件说明

## Frontend - 前端

部署在主机树莓派上即可

把`html`文件夹丢进`nginx`的`www`文件中, `nginx.conf`为`nginx`的配置文件, 反代配置在里面

## Backend - 后端

部署在主机树莓派上即可

需要安装`fastapi`和`uvicorn`模块

运行方法: `uvicorn main:app`

## TI - 图像识别程序

两只树莓派都需要安装, 一只树莓派独立运行时可以计算长度, 两只一起运行才能计算角度

需要安装`opencv`和`requests`模块

配置文件为`config.py`, 需要修改后端地址(`HOST`)和指定是哪一只树莓派(`WHICH`), 以及修改色块识别的上下阈值(`LOWERB`和`UPPERB`)

运行方法 `python3 main.py`
