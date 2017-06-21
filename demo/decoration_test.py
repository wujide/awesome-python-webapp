# coding=utf-8
# __author__='wujide'

import time


def log(func):
    def wrapper(*args, **kwargs):
        print "call %s():" % func.__name__
        return func(*args, **kwargs)
    return wrapper()


@log
def now():
    print "now:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

now

