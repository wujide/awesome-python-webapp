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


class para_get:
    def __init__(self, file_path):
        self.file_path = file_path

    def data_get(self):
        pass



def data_get():
    with open(r"../info/user_pwd_dict.txt", 'rb') as f:
        d = f.read()
        print "type(d)", type(d)
        data = json.dumps(d)
        print "type(data):", type(data)
        values = eval(json.loads(data))
        # print values['user']
        print "type(values):", type(values)
        return values


def write_to_file(data):
    with open(r'../data/loginToken', 'wb+') as f:
        print "data:", data
        print "type(eval(data)):", type(eval(data))
        print "eval(data):", eval(data)
        json.dump(eval(data), f)


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
    write_to_file(dd)


if __name__ == "__main__":
    login()
    # login_get()
    # data_get()

