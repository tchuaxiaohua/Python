# -*- coding: utf-8 -*-
# @Time : 2020/7/7 14:29
# @Author : tchua
# @Email : tchuaxiaohua@163.com
# @File : shopping_center.py
# @Software: PyCharm
from src import user_auth
from conf import settings
import os
import json
import datetime

# 获取用户购物车
def user_shopping_car(username):
    user_dic = user_auth.user_select(username)
    return user_dic.get('shoppong_cat')


# 用户结算
def user_goods_bill(goods_car,username):
    if goods_car:
        settle_money = 0
        for k, v in goods_car.items():
            per_order_money = int(v[0]) * v[1]
            settle_money += int(per_order_money)
        user_dic = user_auth.user_select(username)
        if user_dic['deflimit'] >= settle_money:
            user_dic['deflimit'] -= settle_money
            # 保留最近一次购物至购物车
            user_dic['shoppong_cat'] = goods_car
            msg = f"{datetime.datetime.now()}-用户{username}购物结算成功，本次消费￥{settle_money}"
            user_dic['flow'].append(msg)
            user_auth.user_save(user_dic)
            # 写入订单库
            user_order_history(username,user_dic['shoppong_cat'])
            return True,f"用户{username}购物结算成功，本次消费￥{settle_money}"
        else:
            return False,f"余额不足,结算金额为￥{settle_money},您当前余额为￥{user_dic['deflimit']},请您重新选择物品！"
    else:
        return False,f'用户{username}购物车没有商品'

# 订单保存
def user_order_history(username,user_order_data):
    order_file = os.path.join(settings.USER_ORDER_DIR, f'{username}_order.json')
    user_orders = user_order_view(username)
    if os.path.exists(order_file):
        for item in user_order_data:
            if item in user_orders:
                user_orders[item][1] += user_order_data[item][1]
            else:
                user_orders[item] = user_order_data[item]
        with open(order_file,'w',encoding='utf-8') as f:
            json.dump(user_orders,f,ensure_ascii=False)
    else:
        with open(order_file,'w',encoding='utf-8') as f:
            json.dump(user_order_data,f,ensure_ascii=False)
# 订单查询
def user_order_view(username):
    # 获取用户订单数据
    user_file = os.path.join(settings.USER_ORDER_DIR, f'{username}_order.json')
    if os.path.exists(user_file):
        with open(user_file,'r',encoding='utf-8') as f:
            user_orders = json.load(f)
            return user_orders