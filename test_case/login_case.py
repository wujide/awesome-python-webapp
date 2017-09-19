# coding=utf-8
# __author__='wujide'
import urllib
import urllib2
import para_get
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


def login():
    # 初始化login接口参数
    login_case = para_get.ParaGet(r"../info/para_login.txt")
    # 获取参数
    values = login_case.data_get()
    # print values
    data = urllib.urlencode(values)
    req = urllib2.Request(values['url'])
    response = urllib2.urlopen(req, data)
    print "type(response):", type(response)
    dd = response.read()
    print "type(dd):", type(dd)
    print dd
    #write_to_file(dd)


'''
def write_to_file(data):
    with open(r'../data/loginToken', 'wb+') as f:
        print "data:", data
        print "type(eval(data)):", type(eval(data))
        print "eval(data):", eval(data)
        json.dump(eval(data), f)

'''

if __name__ == "__main__":
    login()
    # login_get()
    # data_get()

