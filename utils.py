import os.path
import time
import json
from flask import make_response

def log(*args, **kwargs):
    # time.time() 返回 unix time
    # 如何把 unix time 转换为普通人类可以看懂的格式呢？
    format = '%H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    with open('gua.log.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)


def response(data, status=None, header=None):
    if header is None:
        header = {'Content-type': 'application/json'}
    data = json.dumps(data)
    res = make_response(data, status, header)
    return res
