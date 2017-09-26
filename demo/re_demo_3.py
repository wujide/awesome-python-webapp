# coding=utf-8
# __author__='Administrator'
import re


reg = r'&captcha=(\d{4})&captCode=(.*?)&isRegisted=(\d)'
result = '&captcha=6130&captCode=57fd2f48c9a345708d0f6d1e876ad27d&isRegisted=1'
data = re.match(reg, result).groups()
print "data:", data

