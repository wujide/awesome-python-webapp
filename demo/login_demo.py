# coding=utf-8
# __author__='wujide'

import urllib
import urllib2

with open(r'../info/user_pwd', 'r') as f:
    lines_strip = f.readline().split()
    phoneNum = lines_strip[0].split('=')[1]
    loginpwd = lines_strip[1].split('=')[1]
    print "phoneNum, loginpwd:", phoneNum, loginpwd

url = 'https://app.91yaowang.com/app/webservice/v2/member/login'
values = {"phoneNum": phoneNum, "loginpwd": loginpwd}
data = urllib.urlencode(values)
req = urllib2.Request(url)
response = urllib2.urlopen(req, data)
print response.read()