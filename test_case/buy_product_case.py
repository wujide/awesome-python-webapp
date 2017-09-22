# coding=utf-8
# __author__='wujide'

from flask import json
from interface_test_class import InterfaceTest


def buyProduct():
    # para_get()
    para_path = r"../info/buyProduct_case_para.txt"
    getInvestInfo_obj = InterfaceTest(para_path)
    getInvestInfo_obj.para_get(para_path=r"../info/buyProduct_case_para.txt", iterface_url='url_buyProduct')
    values = getInvestInfo_obj.data_get()
    response = getInvestInfo_obj.data_post(values)
    data = response.read()  # <type 'str'>
    print data
    file_save = r"../data/buyProduct"
    getInvestInfo_obj.data_save(file_save, data)
    getInvestInfo_obj.pass_or_fail(file_save)


if __name__ == '__main__':
    buyProduct()
