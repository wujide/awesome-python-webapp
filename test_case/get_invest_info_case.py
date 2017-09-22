# coding=utf-8
# __author__='wujide'

from flask import json
from interface_test_class import InterfaceTest


def getInvestInfo():
    # para_get()
    para_path = r"../info/getInvestInfo_case_para.txt"
    getInvestInfo_obj = InterfaceTest(para_path)
    getInvestInfo_obj.para_get(para_path=para_path, iterface_url='url_getInvestInfo')
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
    # get the loginToken
    with open(r"../data/login", 'r') as f:
        values = json.dumps(f.read())
        dd = eval(json.loads(values))
    with open(r"../info/getInvestInfo_case_para.txt", 'r') as f:
        values = json.dumps(f.read())
        data = eval(json.loads(values))
        data['loginToken'] = dd['data']['loginToken']
        data['url'] = d['url_getInvestInfo']
    # write to a file
    with open(r'../info/getInvestInfo_case_para.txt', 'wb+') as f:
        json.dump(data, f)

if __name__ == "__main__":
    # para_get()
    getInvestInfo()
