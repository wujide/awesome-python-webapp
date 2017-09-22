# coding=utf-8
# __author__='Administrator'

from login_case import login
from get_invest_info_case import getInvestInfo
from buy_product_case import buyProduct
from pig_amount_to_base_amount import pigAmountToBaseAmount
from hytx_personal import personal
from hytx_level import level


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

