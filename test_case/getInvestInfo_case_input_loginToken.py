# coding=utf-8
# __author__='wujide'



import para_get

def getInvestInfo():
    # 初始化login接口参数
    getInvestInfo = para_get.ParaGet(r"../info/getInvestInfo_case_para.txt")
    # 获取参数
    values = getInvestInfo.data_get()
    # print values
    data = urllib.urlencode(values)
    req = urllib2.Request(values['url'])
    response = urllib2.urlopen(req, data)
    print "type(response):", type(response)
    dd = response.read()
    print "type(dd):", type(dd)
    print dd
    #write_to_file(dd)

if __name__ == "__main__":
    getInvestInfo()