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

# findall
reg_2 = r"\(?0\d{2,3}[) -]?\d{7,8}"
txt_2 = '(021)88776543 010-55667890 02584533622 057184720483 837922740'
tel_find = re.findall(reg_2, txt_2)
if tel_find:
    print "tel_find:", tel_find
else:
    print "nothing find"


email = 'test@test.com test.test@test.com _123@123.com 3434@123.456.cn 456@456.me '
reg_3 = r'\w+[\w.]*@[\w.]+\.\w+ '
email_find = re.findall(reg_3, email)
if email_find:
    print "email_find:", email_find
else:
    print "no email found"


# 先编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print re_telephone.match('012-34567').groups()
