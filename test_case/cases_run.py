# coding=utf-8
# __author__='Administrator'

from login_case import login
from get_invest_info_case import getInvestInfo
from buy_product_case import buyProduct
from pig_amount_to_base_amount import pigAmountToBaseAmount
from hytx_personal import personal
from hytx_level import level
from test_case import lcds_investcount
from test_case.lcds_simple_info import lcds_simpleinfo

login()
# 0 元白拿获取投资值和邀请值
getInvestInfo()
# buy product
buyProduct()
# 购买摇宝
pigAmountToBaseAmount()
# 会员体系 - 会员页信息
personal()
# 会员体系 - 用户等级
level()
# 理财大使：基础信息
lcds_simpleinfo
# 理财大使：好友在投，一级好友人数
lcds_investcount
