# coding=utf-8
# __author__='wujide'

import urllib2
import urllib


# post
def getInvestInfo():
    url = 'https://app.91yaowang.com/app/webservice/v2/rightGive/getInvestInfo'
    logintoken = '48C81C935857F2A446107410EB1497FF67E90CDF5D6054AE0234265BC4239D8E44D7F53564EFB55B8B67554A74E31D90D35AA60D717365C64BD79B1D60049DA4'
    # todo: 添加从info/loginToken 中读取loginToken 的代码
    values = {"logintoken": logintoken}
    data = urllib.urlencode(values)
    req = urllib2.Request(url)
    response = urllib2.urlopen(req, data)
    print response.read()

if __name__ == "__main__":
    getInvestInfo()
