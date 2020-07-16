# -*- coding: utf-8 -*-
# @Time : 2020/7/3 18:35
# @Author : tchua
# @Email : tchuaxiaohua@163.com
# @File : common.py
# @Software: PyCharm
import hashlib
import logging.config
from conf import settings

# 登录装饰器
def login_auth(func):
    from src import main
    def inner(*args,**kwargs):
        if main.login_user:
            res = func(*args,**kwargs)
            return res
        else:
            print("用户未登录")
            main.login()
    return inner

# md5加密
def md5_pwd(user,password):
    md5 = hashlib.md5(user.encode('utf-8'))
    md5.update(password.encode('utf-8'))
    pwd = md5.hexdigest()
    return pwd

# 日志
def get_logger(log_type):
    '''

    :param log_type: 具体的应用日志
    :return:
    '''
    logging.config.dictConfig(
        settings.LOGGING_DIC
    )

    # 获取logger对象
    logger = logging.getLogger(log_type)

    return logger
