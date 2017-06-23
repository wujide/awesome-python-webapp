# coding=utf-8
# __author__='wujide'

import re

# match 匹配
reg = r'^\d{3}\-\d{3,8}'
tel = '021-12345'
if re.match(reg, tel):
    print 'It\'s matched !'
else:
    print "No"

# split 切分
s = 'a, b   c;; d'
print re.split(r'[\s\,\;]+', s)


# group 分组
reg_1 = r'(\d{3})-(\d{3,8})$'
txt = '123-456789'
m = re.match(reg_1, txt)
print m.group(0)
print m.group(1)
print m.group(2)

# 先编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print re_telephone.match('012-34567').groups()

