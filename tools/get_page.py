# coding=utf-8
# __author__='wujide'
import urllib2


class GetPage:
    def __init__(self, url, para_name, pageIndex):
        self.total_url = url + "?" + str(para_name) + "=" + str(pageIndex)

    def getpage(self):
        request = urllib2.Request(self.total_url)
        response = urllib2.urlopen(request)
        print response.read().decode('gbk')
        return response.read().decode('gbk')

url = 'http://mm.taobao.com/json/request_top_list.htm'
gt = GetPage(url, 'page', 1)
gt.getpage()
