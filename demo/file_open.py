# coding=utf-8
# __author__='Administrator'


with open(r'../info/user_pwd', 'r') as f:
    lines = f.readline()
    print lines
    lines_strip = lines.split()
    print lines_strip
    phoneNum = lines_strip[0].split('=')[1]
    loginpwd = lines_strip[1].split('=')[1]
    print phoneNum, loginpwd


with open(r'../info/url', 'r') as f_url:
    lines = f_url.readline()
    print lines
    lines_strip = lines.split('=')
    url = lines_strip[1]
    print url

