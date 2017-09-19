# coding=utf-8
# __author__='wujide'

import urllib2
import urllib
from flask import json


def getInvestInfo():
    url = 'https://app.91yaowang.com/app/webservice/v2/rightGive/getInvestInfo'
    loginToken = loginToken_get()
    values = {"loginToken": loginToken}
    data = urllib.urlencode(values)
    req = urllib2.Request(url)
    response = urllib2.urlopen(req, data)
    print response.read()

try:
    import cPickle as pickle
except ImportError:
    import pickle


def loginToken_get():
    with open(r"../data/loginToken", 'r') as f:
        values = f.read()
        print "type(values):", type(values)
        data = json.dumps(values)
        print data
        d = eval(json.loads(data))
        # d = eval(pickle.load(f))
        print "type(d):", type(d)
        print d['data']['loginToken']
        return d['data']['loginToken']


if __name__ == "__main__":
    getInvestInfo()
    # loginToken_get()