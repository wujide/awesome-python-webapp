# coding=utf-8
# __author__='wujide'
import urllib2


class getPage:
    def __init__(self, siteURL, para_name, pageIndex):
        self.url = siteURL + "?" + str(para_name) + "=" + str(pageIndex)

    def getpage(self):
        url = self.url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        print response.read().decode('gbk')
        return response.read().decode('gbk')

url = 'http://mm.taobao.com/json/request_top_list.htm'
gt = getPage(url, 'page', 1)
gt.getpage()
