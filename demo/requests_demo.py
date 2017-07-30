# coding=utf-8
# __author__='wujide'

import requests
import json


''''
#测试百度
def baidu_func(url):
    headers = {}
    params = {}
    req = requests.post(url, headers=headers, params=params)
    print(req.text)

if __name__ == '__main__':
    url = "http://www.baidu.com"
    baidu_func(url)
'''


# login test
def login_test(url):
    data = json.dumps({'phoneNum': 13800138000, 'loginpwd': '123456abcd'})
    req = requests.post(url, data)
    print req.json

if __name__ == '__main__':
    url = "https://app.91yaowang.com/app/webservice/v2/member/login"
    login_test(url)