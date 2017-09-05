# coding=utf-8
# __author__='wujide'

import urllib
import urllib2
import re


# 百度贴吧爬虫类
class BDTB:
    # 初始化，传入基地址，是否只看楼主的参数
    def __init__(self, baseUrl, seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)

    # 传入页码，获取该页帖子的代码
    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            # print response.read()
            return response
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接百度贴吧失败,错误原因", e.reason
                return None

    def getTitle(self):
        page = str(self.getPage(0))
        pattern = re.compile('<h1 class="post_title_embed.*?>(.*?)</h1>', re.S)
        result = re.search(pattern, page)
        if result:
            print result.group()  # 测试输出
            return result.group(1).strip()
        else:
            return None

baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL, 1)
bdtb.getPage(1)
bdtb.getTitle()


