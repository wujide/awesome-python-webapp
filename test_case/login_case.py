# coding=utf-8
# __author__='wujide'
import ast
import os
import urllib
import urllib2
import cPickle
from flask import json, jsonify
'''
with open(r'../info/user_pwd', 'r') as f:
    lines_strip = f.readline().split()
    phoneNum = lines_strip[0].split('=')[1]
    loginpwd = lines_strip[1].split('=')[1]
    print "phoneNum, loginpwd:", phoneNum, loginpwd
'''
try:
    import cPickle as pickle
except ImportError:
    import pickle


def data_get():
    with open(r"../info/user_pwd_dict.txt", 'rb') as f:
        d = f.read()
        data = json.dumps(d)
        # print "type(data):", type(data)
        values = eval(json.loads(data))
        # print values['user']
        print "type(values):", type(values)
        return values


def login():
    values = data_get()
    # print values
    data = urllib.urlencode(values)
    req = urllib2.Request(values['url'])
    response = urllib2.urlopen(req, data)
    print "type(response):", type(response)
    dd = response.read()
    print "type(dd):", type(dd)
    print dd
    # 序列化并保存到文件中
    dt = urllib.urlencode(eval(dd))
    # date_return = json.dump(response)
    write_to_file(dt)
    # print date_return
    # print type(date_return)
    #loginToken = date_return['data']['loginToken']
    #print "loginToken = ", loginToken
    # d = dict(loginToken=loginToken)


def write_to_file(data):
    with open(r'../data/loginToken', 'wb+') as f:
        print data
        pickle.dump(data, f)


if __name__ == "__main__":
    login()
    # login_get()
    # data_get()

