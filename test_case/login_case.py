# coding=utf-8
# __author__='wujide'

import urllib
import urllib2

with open(r'../info/user_pwd', 'r') as f:
    lines_strip = f.readline().split()
    phoneNum = lines_strip[0].split('=')[1]
    loginpwd = lines_strip[1].split('=')[1]
    print "phoneNum, loginpwd:", phoneNum, loginpwd


# post
def login():
    url = 'https://app.91yaowang.com/app/webservice/v2/member/login'
    values = {"phoneNum": phoneNum, "loginpwd": loginpwd}
    data = urllib.urlencode(values)
    req = urllib2.Request(url)
    response = urllib2.urlopen(req, data)
    # todo: 添加把loginToken 读取并写入info/loginToken 的代码
    print response.read()


# get方法，貌似不允许
def login_get():
    url_1 = "https://app.91yaowang.com/app/webservice/v2/member/login"
    values_get = {"phoneNum": "13800138015", "loginpwd": loginpwd}
    data_get = urllib.urlencode(values_get)
    url_get = url_1 + "?" + data_get
    print url_get
    req_get = urllib2.Request(url_get)
    response_get = urllib2.urlopen(req_get)
    print response_get.read()


if __name__ == "__main__":
    login()
    # login_get()
