# coding=utf-8
# __author__='wujide'

import urllib2
import urllib


# post
def getInvestInfo():
    url = 'https://app.91yaowang.com/app/webservice/v2/rightGive/getInvestInfo'
    loginToken = "48C81C935857F2A446107410EB1497FFBE5AA09B5DB3D5B9863A55828916D7F07E50D5D89D16356532F0C5FA85A4E5ED4C6BCC570CA76D0B2F130894163F2799"
    # todo: 添加从info/loginToken 中读取loginToken 的代码
    values = {"loginToken": loginToken}
    data = urllib.urlencode(values)
    req = urllib2.Request(url)
    response = urllib2.urlopen(req, data)
    print response.read()

if __name__ == "__main__":
    getInvestInfo()
