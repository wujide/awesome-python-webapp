# coding=utf-8
# __author__='wujide'
import urllib
import urllib2
from flask import json
import interface_test_class

'''
with open(r'../info/user_pwd', 'r') as f:
    lines_strip = f.readline().split()
    phoneNum = lines_strip[0].split('=')[1]
    loginpwd = lines_strip[1].split('=')[1]
    print "phoneNum, loginpwd:", phoneNum, loginpwd
'''


def login():
    # 初始化login 实例
    login_obj = interface_test_class.InterfaceTest(r"../info/login_case_para.txt")
    # 获取参数
    values = login_obj.data_get()  # <type 'dict'>
    response = login_obj.data_post(values)
    data = response.read()  # <type 'str'>
    print data
    file_save = r'../data/login'
    login_obj.data_save(file_save, data)
    login_obj.pass_or_fail(file_save)


def pass_or_fail():
    with open(r"../data/login", 'r') as f:
        values = json.dumps(f.read())
        d = eval(json.loads(values))
        if d['data']['loginToken']:
            print "login PASS"
        else:
            print "login FAIL"

if __name__ == "__main__":
    login()
