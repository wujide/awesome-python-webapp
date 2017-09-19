# coding=utf-8
# __author__='wujide'
import urllib
import urllib2

from flask import json


class InterfaceTest:
    def __init__(self, file_path):
        self.file_path = file_path

    def data_get(self):
        with open(self.file_path, 'rb') as f:
            values = json.dumps(f.read())  # type(values): <type 'str'>
            data = eval(json.loads(values))  # type(data): <type 'dict'>
            return data

    @staticmethod
    def data_post(values):
        data = urllib.urlencode(values)
        req = urllib2.Request(values['url'])
        response = urllib2.urlopen(req, data)
        return response
