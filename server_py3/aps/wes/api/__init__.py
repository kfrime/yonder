#!/usr/bin/env python3

# 让Python加载模块，否则app.route装饰器不会运行，无法添加路由
from . import v1, v2
