#!/usr/bin/env python3

import os
import sys


conf_path = os.path.dirname(os.path.abspath(__file__))
py_path = conf_path.split('aps')[0]
sim_path = os.path.abspath(os.path.join(py_path, 'sim'))
print(f"conf_path: {conf_path}, sim_path: {sim_path}")
sys.path.append(sim_path)

# ../../sim dir
from sim.application import Application
from sim.norm import Database
from sim.cache import AppCachePool

from wes.config import AppConfig


APP_NAME = 'wes'

db = Database()
cache_pool = AppCachePool()


def create_app():
    """
    :param config_name: dev/live
    :return:
    """
    app = Application(APP_NAME)

    AppConfig.init_app(app)

    db.init_app(app)
    cache_pool.init_app(app)

    return app


app = create_app()

# 让Python加载模块，否则app.route装饰器不会运行，无法添加路由
from . import api
