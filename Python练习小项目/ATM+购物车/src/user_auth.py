# -*- coding: utf-8 -*-
# @Time : 2020/7/3 11:30
# @Author : tchua
# @Email : tchuaxiaohua@163.com
# @File : user_auth.py
# @Software: PyCharm

"""
用户登录注册
"""

import os
import json
import datetime
from conf import settings
from lib import common

user_loger = common.get_logger("user")
# 查询用户接口
def user_select(username):
    user_file = os.path.join(settings.USER_DIR, f'{username}.json')
    if os.path.exists(user_file):
        with open(user_file,'r',encoding='utf-8') as f:
            user_info = json.load(f)
            return user_info
    # else:
    #     return f"用户{username}不存在"

# 用户数据保存接口
def user_save(user_dic):
    username = user_dic.get("user")
    user_file = os.path.join(settings.USER_DIR, f'{username}.json')
    # 用户信息落库
    with open(user_file,'w',encoding='utf-8') as f:
        json.dump(user_dic,f,ensure_ascii=False)

# 用户注册接口
def user_regist(username,passwd):
    # 填充模板字段
    settings.USER_DIC['user'] = username
    settings.USER_DIC['passwd'] = passwd
    # 保存数据
    user_save(settings.USER_DIC)
    msg = f"用户{username}注册成功！"
    user_loger.info(msg)
    return True,msg

# 用户登录接口
def user_login(username,passwd):
    user_dic = user_select(username)
    if user_dic:
        if user_dic["status"] == 1:
            return False,'用户已锁定,请联系管理员解除！'
        else:
            passwd = common.md5_pwd(username,passwd)
            if passwd == user_dic['passwd']:
                msg = f'用户{username}登录成功！'
                user_loger.info(msg)
                return True,'用户登录成功！'
            else:
                msg = f'用户{username}密码错误！'
                user_loger.error(msg)
                return False,'密码错误'
    msg = f'用户{username}不存在'
    user_loger.info(msg)
    return False,'用户不存在'

# 用户余额查询接口
def user_balance(username):
    user_dic = user_select(username)
    return user_dic['deflimit']

# 提现接口
def user_withdraw(username,balance):
    user_dic = user_select(username)
    if user_dic['deflimit'] >= int(balance):
        user_dic['deflimit'] -= int(balance)
        draw_mony =  int(balance) - int(balance) * 0.05
        # 记录流水
        msg = f'{datetime.datetime.now()}- 用户{username}提现￥{balance}成功,实际到账{draw_mony}'
        user_dic['flow'].append(msg)
        user_loger.info(f'用户{username}提现￥{balance}成功,实际到账{draw_mony}')
        # 保存数据
        user_save(user_dic)
        return True,msg
    else:
        return False,'余额不足'

# 转账接口
def user_transfer(username,login_user,balance):
    user_dic = user_select(login_user)
    to_user_dic = user_select(username)
    if not to_user_dic:
        return False,f"{username}不存在"
    if user_dic["deflimit"] >= int(balance):
        user_dic["deflimit"] -= int(balance)
        to_user_dic['deflimit'] += int(balance)

        #流水记录
        to_user_msg = f"{datetime.datetime.now()} - 收到{login_user}转账￥{balance}成功"
        to_user_dic['flow'].append(to_user_msg)
        user_msg = f"{datetime.datetime.now()} - 转账给用户{username}￥{balance}成功"
        user_dic['flow'].append(user_msg)
        # 保存数据
        user_save(user_dic)
        user_save(to_user_dic)
        msg = f"用户{login_user}转账给用户{username},￥{balance}成功"
        user_loger.info(msg)
        return True,f"用户{login_user}转账给用户{username},￥{balance}成功"

# 还款接口
def user_repayment(username,repaymoney):
    user_dic = user_select(username)
    user_dic['deflimit'] += int(repaymoney)
    msg = f'{datetime.datetime.now()} - 还款成功,余额为￥{user_dic["deflimit"]}'
    user_dic['flow'].append(msg)
    user_save(user_dic)
    user_loger.info('还款成功,余额为￥{0}'.format(user_dic['deflimit']))
    return True,'还款成功,余额为￥{0}'.format(user_dic['deflimit'])

# 流水查询接口
def user_view_flow(username):
    user_dic = user_select(username)
    return user_dic['flow']