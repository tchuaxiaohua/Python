# -*- coding: utf-8 -*-
# @Time : 2020/7/3 13:35
# @Author : tchua
# @Email : tchuaxiaohua@163.com
# @File : settings.py
# @Software: PyCharm
"""
配置文件
"""
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# 用户信息根目录
USER_DIR = BASE_DIR + "/data/user_data"

# 用户历史订单数据目录
USER_ORDER_DIR = BASE_DIR + "/data/goods_data"
# 用户注册模板
USER_DIC = {
        'user': None,
        'passwd': None,
        'deflimit': 1500,
        'shoppong_cat': {},
        'flow': [],
        'adm': False,
        'status': 0
    }
# 商品信息
GOODS_LST = [
    ["笔记本", "12000"],
    ['自行车', '5420'],
    ['雪糕', '10'],
    ['辣条', '5'],
    ['大豫竹','1'],
    ['牙刷','5']
       ]

# 日志配置
# 日志根目录
LOG_PATH = os.path.join(BASE_DIR,"logs/atm.log")

# ## 标准格式
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'
# ## 简单格式
simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

# ## 测试格式
test_format = '%(asctime)s] %(message)s'

# 日志字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
        'test': {
            'format': test_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件,日志轮转
            'formatter': 'standard',
            # 可以定制日志文件路径
            'filename': LOG_PATH,  # 日志文件
            'maxBytes': 1024*1024*50,  # 日志大小 5M
            'backupCount': 10,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['default'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG', # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
    },
}