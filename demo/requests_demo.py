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

with open(r'../info/user_pwd', 'r') as f:
    lines = f.readline()
    lines_strip = lines.split()
    phoneNum = lines_strip[0].split('=')[1]
    loginpwd = lines_strip[1].split('=')[1]

with open(r'../info/url', 'r') as f_url:
    lines = f_url.readline()
    print lines
    lines_strip = lines.split('=')
    url_login = lines_strip[1]


# login test
def login_test(url):
    # data = json.dumps({'phoneNum': phoneNum, 'loginpwd': loginpwd})
    data = 'phoneNum='+ phoneNum +'&'+ 'loginpwd='+ loginpwd
    print "data", data
    req = requests.post(url, data, verify=False)
    print req.json
    print "req:", req
    print "req.status:", req.response

if __name__ == '__main__':
    url = url_login
    login_test(url)