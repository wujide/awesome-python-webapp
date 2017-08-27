# coding=utf-8
# __author__='wujide'

import urllib2
import urllib
from flask import json


def getInvestInfo():
    url = 'https://app.91yaowang.com/app/webservice/v2/rightGive/getInvestInfo'
    # loginToken = "48C81C935857F2A446107410EB1497FFBE5AA09B5DB3D5B9863A55828916D7F07E50D5D89D16356532F0C5FA85A4E5ED4C6BCC570CA76D0B2F130894163F2799"
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

