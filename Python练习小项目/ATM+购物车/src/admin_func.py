#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2020/7/9 18:01
# @Author    :tchua

from src import main
from src import user_auth
from conf import settings
import os
# 创建用户
def create_user():
    main.regist()

# 删除用户
def del_user():
    username = input("请输入要删除的用户名:")
    user_dic = user_auth.user_select(username)
    if user_dic:
        user_data = os.path.join(settings.USER_DIR, f'{username}.json')
        os.remove(user_data)
        return True,f"删除用户{username}成功！"
    else:
        print("用户不存在")

# 修改用户额度
def change_balabce():
    username = input("请输入要提额用户名:")
    balabce = input("请输入提额数:")
    user_dic = user_auth.user_select(username)
    if user_dic:
        user_dic['deflimit'] += int(balabce)
        msg = f"用户{username}提额成功,余额为:{user_dic['deflimit']}"
        user_dic["flow"].append(msg)
        user_auth.user_save(user_dic)
    else:
        print("用户不存在")
# 锁定用户
def user_lock():
    username = input("请输入要锁定用户名:")
    user_dic = user_auth.user_select(username)
    if user_dic:
        user_dic['status'] = 1
        user_auth.user_save(user_dic)
    else:
        print("用户不存在")




