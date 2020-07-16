# -*- coding: utf-8 -*-
# @Time : 2020/7/3 11:48
# @Author : tchua
# @Email : tchuaxiaohua@163.com
# @File : main.py
# @Software: PyCharm

from src import user_auth
from src import shopping_center
from lib import common
from conf import settings
from src import admin_func
login_user = None

def regist():
    username = input("请输入用户名:")
    passwd = input("请输入密码:")
    # 判断用户是否已存在
    if not user_auth.user_select(username):
        passwd = common.md5_pwd(username,passwd)
        user_auth.user_regist(username,passwd)
    else:
        print('用户已存在')

def login():
    while True:
        username = input("请输入用户名:")
        passwd = input("请输入密码:")
        flag,msg = user_auth.user_login(username,passwd)
        if flag:
            global login_user
            login_user = username
            print(msg)
            break
        else:
            print(msg)
            break

# 查看余额
@common.login_auth
def view_balance():
    balance = user_auth.user_balance(login_user)
    print(f"用户{login_user}余额:",balance)
# 提现
@common.login_auth
def withdraw():
    while True:
        balance = input("请输入提现金额:")
        flag,msg = user_auth.user_withdraw(login_user,balance)
        if flag:
            print(msg)
            break
        else:
            print(msg)
# 转账
@common.login_auth
def transfer():
    while True:
        to_user = input("请输入对方账户:")
        t_money = input("请输入转账金额:")
        flag,msg = user_auth.user_transfer(to_user,login_user,t_money)
        if flag:
            print(msg)
            break
        else:
            print(msg)

# 还款
@common.login_auth
def repayment():
    repay_money = input("请输入还款金额:").strip()
    if repay_money.isdigit():
        flag,msg = user_auth.user_repayment(login_user,repay_money)
        if flag:
            print(msg)
    else:
        print('金额输入错误')
# 流水查询
@common.login_auth
def view_flow():
    flow_lst = user_auth.user_view_flow(login_user)
    if flow_lst:
        for item in flow_lst:
            print(item)
    else:
        print("用户未产生流水")

# 购物
@common.login_auth
def shopping():
    print("欢迎来到信用卡购物中心")
    lst = settings.GOODS_LST
    for a,b in enumerate(settings.GOODS_LST):
        print(a, b)
    # 购物车初始化
    user_shopcar = {}
    while True:
        id = input("请选择你需要的商品编号【Q退出/C结算/Y添加购物车】:")

        if id.upper() == 'Q':
            break
        elif id.upper() == 'C':
            flag,msg = shopping_center.user_goods_bill(user_shopcar,login_user)
            if flag:
                print(msg)
                break
            else:
                print(msg)
                user_shopcar = {}
        elif id.isdigit():
            goods_name = lst[int(id)][0]
            goods_price = lst[int(id)][1]

            if goods_name in user_shopcar:
                user_shopcar[goods_name][1] += 1
            else:
                user_shopcar[goods_name] = [goods_price, 1]
# 历史订单查询
@common.login_auth
def view_order():
    user_orders = shopping_center.user_order_view(login_user)
    if user_orders:
        for k,v in user_orders.items():
            print(k,':',v)
    else:
        print("用户还没购物！")

@common.login_auth
def admin():
    # while True:
        user_dic = user_auth.user_select(login_user)
        if user_dic['adm']:
            print("欢迎进入ATM后台管理")
            print(admin_menu)
            while True:
                choice = input("输入功能编号:").strip()
                if choice.upper() == '5':
                    print("退出管理员模式")
                    break
                if choice not in admin_func_dic:
                    continue
                admin_func_dic.get(choice)()
        else:
            print(f"用户{login_user}不是管理员")



# 函数功能字典
func_dic = {
    '1': regist,
    '2': login,
    '3': view_balance,
    '4': withdraw,
    '5': transfer,
    '6': repayment,
    '7': view_flow,
    '8': shopping,
    '9': view_order,
    '10': admin
}

admin_func_dic = {
    '1': admin_func.create_user,
    '2': admin_func.del_user,
    '3': admin_func.user_lock,
    '4': admin_func.change_balabce
}
admin_menu = """
1、新建用户
2、删除用户
3、锁定
4、用户提额
5、退出
"""

menu = """
===================
1、注册
2、登录
3、查看余额
4、提现
5、转账
6、还款
7、查看流水
8、购物
9、查看历史订单
10、管理员
===================
"""
#
def run():
    print(menu)
    while True:
        choice = input("输入功能编号:").strip()
        if choice not in func_dic:
            continue
        func_dic.get(choice)()

run()