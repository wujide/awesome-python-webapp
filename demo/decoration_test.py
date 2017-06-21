# coding=utf-8
# __author__='wujide'

import time, functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print "call %s():" % func.__name__
        return func(*args, **kwargs)
    return wrapper


@log
def now():
    print "now:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

now()



def log_1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print "%s %s():" % (text, func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log_1("run")
def now_1():
    print "now_1:", time.strftime("%Y%m%d", time.localtime())

now_1()



def log_2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print "\nbegin call:"
        print "call %s():" % func.__name__
        data = func(*args, **kwargs)
        print "end call:"
        return data
    return wrapper


@log_2
def now_2():
    print "now_2:", time.strftime("%Y-%m-%d", time.localtime())

now_2()