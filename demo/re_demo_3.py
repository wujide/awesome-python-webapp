# coding=utf-8
# __author__='Administrator'
import re


reg = r'&captcha=(\d{4})&captCode=(.*?)&isRegisted=(\d)'
reg = r'phoneNum=13800138048&captcha=(.*?)&captCode=(.*?)&isRegisted=(\d)'
result = '[http-bio-8380-exec-10]-2017-09-26 21:39:23,741  INFO VerifCodeServiceImpl:72 - phoneNum=13800138048&captcha=6130&captCode=57fd2f48c9a345708d0f6d1e876ad27d&isRegisted=1'
data = re.findall(reg, result)
print "data:", data[0][0]

