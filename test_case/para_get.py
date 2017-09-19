# coding=utf-8
# __author__='wujide'
from flask import json


class ParaGet:
    def __init__(self, file_path):
        self.file_path = file_path

    def data_get(self):
        with open(self.file_path, 'rb') as f:
            values = json.dumps(f.read())  # type(values): <type 'str'>
            data = eval(json.loads(values))  # type(data): <type 'dict'>
            return data
