# coding=utf-8
# __author__='wujide'

import requests


def send_request(url):
    r = requests.get(url, verify=False)
    return r.status_code


def visit_baidu(url='https://www.baidu.com'):
    return send_request(url)

if __name__ == "__main__":
    url = 'https://www.baidu.com'
    print visit_baidu(url)