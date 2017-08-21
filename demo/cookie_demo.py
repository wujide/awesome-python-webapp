# coding=utf-8
# __author__='wujide'
import cookielib
import urllib2

url = 'https://www.baidu.com'
filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
handle = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handle)
response = opener.open(url)
cookie.save(ignore_discard=True, ignore_expires=True)
for item in cookie:
    print "Name = " + item.name
    print "value = " + item.value




