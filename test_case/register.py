# coding=utf-8
# __author__='wujide'
from tools.server_log_get import server_log_get
from tools.getVerifCodeNew_get import verifCode_get
from tools.captcha_get import captcha_get
from interface_test_class import InterfaceTest


def register():
    # use regression to get captcha（图形码）
    captcha_get(13800138048)
    # connect server, and read the catalina.out
    server_log_get(13800138048)
    # register interface

    # para_get()
    para_path = r"../info/buyProduct_para.txt"
    obj = InterfaceTest(para_path)
    obj.para_get(para_path=para_path, iterface_url='url_buyProduct')
    values = obj.data_get()
    response = obj.data_post(values)
    data = response.read()  # <type 'str'>
    file_save = r"../data/buyProduct"
    obj.data_save(file_save, data)
    obj.pass_or_fail(file_save)
    return data


if __name__ == '__main__':
    print buyProduct()


