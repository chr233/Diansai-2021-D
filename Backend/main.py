'''
# @Author       : Chr_
# @Date         : 2021-11-04 20:30:06
# @LastEditors  : Chr_
# @LastEditTime : 2021-11-08 01:34:12
# @Description  : 
'''

import uvicorn
from fastapi import FastAPI

from router import root, measure, display

from memdb import load_demo

app = FastAPI()

app.include_router(display.router)
app.include_router(measure.router)
app.include_router(root.router)

load_demo()

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
