# coding=utf-8
# __author__='wujide'
from flask import json


class ParaGet:
    def __init__(self, file_path):
        self.file_path = file_path

    def data_get(self):
        with open(self.file_path, 'rb') as f:
            d = f.read()
            print "type(d)", type(d)
            data = json.dumps(d)
            print "type(data):", type(data)
            values = eval(json.loads(data))
            # print values['user']
            print "type(values):", type(values)
            return values