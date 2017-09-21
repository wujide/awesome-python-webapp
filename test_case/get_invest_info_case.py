# coding=utf-8
# __author__='wujide'

from flask import json
from test_case import interface_test_class


def getInvestInfo():
    para_get()
    para_path = r"../info/getInvestInfo_case_para.txt"
    getInvestInfo_obj = interface_test_class.InterfaceTest(para_path)
    values = getInvestInfo_obj.data_get()
    response = getInvestInfo_obj.data_post(values)
    data = response.read()  # <type 'str'>
    print data
    file_save = r"../data/getInvestInfo"
    getInvestInfo_obj.data_save(file_save, data)
    getInvestInfo_obj.pass_or_fail(file_save)


def para_get():
    # get interface url: getInvestInfo
    with open(r"../info/url", 'r') as f:
        values = json.dumps(f.read())
        d = eval(json.loads(values))
        url_get_invest_info = d['url_getInvestInfo']
    # get the loginToken
    with open(r"../data/login", 'r') as f:
        values = json.dumps(f.read())
        d = eval(json.loads(values))
        loginToken = d['data']['loginToken']
    data = {"loginToken": loginToken,
            "url": url_get_invest_info}
    # print data
    # write to a file
    with open(r'../info/getInvestInfo_case_para.txt', 'wb+') as f:
        json.dump(data, f)


def pass_or_fail():
    with open(r"../data/getInvestInfo", 'r') as f:
        values = json.dumps(f.read())
        d = eval(json.loads(values))
        if d['data']['investAmt'] and d['data']['inviteNum']:
            print "getInvestInfo PASS"
        else:
            print "getInvestInfo FAIL"

if __name__ == "__main__":
    # para_get()
    getInvestInfo()
