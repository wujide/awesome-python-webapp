# coding=utf-8
# __author__='wujide'
import os
import urllib
import urllib2
import cPickle
from flask import json, jsonify

with open(r'../info/user_pwd', 'r') as f:
    lines_strip = f.readline().split()
    phoneNum = lines_strip[0].split('=')[1]
    loginpwd = lines_strip[1].split('=')[1]
    print "phoneNum, loginpwd:", phoneNum, loginpwd

try:
    import cPickle as pickle
except ImportError:
    import pickle


def data_get():
    with open(r"../info/user_pwd_dict.txt", 'rb') as f:
        d = f.read()
        data = json.loads(json.dumps(d))
        print type(data)
        print data
        return data



# post
def login():
    url = 'https://app.91yaowang.com/app/webservice/v2/member/login'
    values = {"phoneNum": phoneNum, "loginpwd": loginpwd}
    data = urllib.urlencode(values)
    req = urllib2.Request(url)
    response = urllib2.urlopen(req, data)
    print response.read()
    # 序列化并保存到文件中
    date_return = json.load(response)
    write_to_file(date_return)
    # print date_return
    # print type(date_return)
    loginToken = date_return['data']['loginToken']
    # print "loginToken = ", loginToken
    # d = dict(loginToken=loginToken)


def write_to_file(data):
    with open(r'../data/loginToken', 'w+') as f:
        pickle.dump(data, f)


if __name__ == "__main__":
    login()
    # login_get()
    # data_get()
