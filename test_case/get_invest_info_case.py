# coding=utf-8
# __author__='wujide'

from flask import json

from test_case import interface_test_class


def getInvestInfo():
    para_get()
    para_path = r"../info/getInvestInfo_case_para.txt"
    getInvestInfo = interface_test_class.InterfaceTest(para_path)
    values = getInvestInfo.data_get()
    response = getInvestInfo.data_post(values)
    dd = response.read()  # <type 'str'>
    print dd


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
    print data
    # write to a file
    with open(r'../info/getInvestInfo_case_para.txt', 'wb+') as f:
        json.dump(data, f)


if __name__ == "__main__":
    # para_get()
    getInvestInfo()
