# coding=utf-8
# __author__='wujide'
import urllib
import urllib2
from flask import json
import para_get

'''
with open(r'../info/user_pwd', 'r') as f:
    lines_strip = f.readline().split()
    phoneNum = lines_strip[0].split('=')[1]
    loginpwd = lines_strip[1].split('=')[1]
    print "phoneNum, loginpwd:", phoneNum, loginpwd
'''


def login():
    # 初始化login接口参数
    login_para = para_get.ParaGet(r"../info/login_case_para.txt")
    # 获取参数
    values = login_para.data_get()  # <type 'dict'>
    print type(values), values
    data = urllib.urlencode(values)  # <type 'str'>
    print "type(data):", type(data), data
    req = urllib2.Request(values['url'])
    response = urllib2.urlopen(req, data)  # <type 'instance'>
    dd = response.read()  # <type 'str'>
    print dd
    write_to_file(dd)


def write_to_file(data):
    with open(r'../data/loginToken', 'wb+') as f:
        # print "data:", data
        # print "type(eval(data)):", type(eval(data))
        # print "eval(data):", eval(data)
        json.dump(eval(data), f)

if __name__ == "__main__":
    login()
