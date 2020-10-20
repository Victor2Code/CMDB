#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @author: xiaofu
# @date: 2020-Oct-07

import os
from Controller import credentials

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SSH_HOST_LIST = [
    ('10.18.99.66', 57522),
]
# 生产环境使用密钥进行登录，这里测试环境使用用户名和密码
SSH_USER = credentials.USER
SSH_PASSWORD = credentials.PASSWORD

PLUGINS = {
    'disk': 'plugins.disk.DiskPlugin',
    'memory': 'plugins.memory.MemoryPlugin',
    'network': 'plugins.network.NetworkPlugin',
    'board': 'plugins.board.BoardPlugin',
}

LOGGING_PATH = os.path.join(BASE_DIR, '../log/controller.log')  ## 日志文件目录在上一级

LOCAL_DISK_FILE = os.path.join(BASE_DIR, 'files/disk.out')  # 本地用来模拟物理机硬盘信息的文件
