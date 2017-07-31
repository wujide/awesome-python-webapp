# coding=utf-8
# __author__='wujide'

import requests


def send_request(url):
    r = requests.get(url, verify=False)
    return r.status_code


def visit_ustack():
    return send_request('https://www.baidu.com')