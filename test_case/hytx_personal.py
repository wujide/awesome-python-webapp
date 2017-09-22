# coding=utf-8
# __author__='wujide'
from flask import json
from interface_test_class import InterfaceTest


def personal():
    para_path = r"../info/hytx_personal_case_para.txt"
    getInvestInfo_obj = InterfaceTest(para_path)
    getInvestInfo_obj.para_get(para_path=para_path, iterface_url='url_hytx_personal')
    values = getInvestInfo_obj.data_get()
    response = getInvestInfo_obj.data_post(values)
    data = response.read()  # <type 'str'>
    file_save = r"../data/hytx_personal"
    getInvestInfo_obj.data_save(file_save, data)
    getInvestInfo_obj.pass_or_fail(file_save)
    return data


if __name__ == '__main__':
    print personal()
