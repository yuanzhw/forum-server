import time
import json
from flask import make_response


def log(*args, **kwargs):
    time_format = '%H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(time_format, value)
    with open('log.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)


def response(data, status=None, header=None):
    if header is None:
        header = {'Content-type': 'application/json'}
    data = json.dumps(data)
    res = make_response(data, status, header)
    return res
