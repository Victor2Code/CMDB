#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @author: xiaofu
# @date: 2020-Oct-07

from Controller import credentials

SSH_HOST_LIST = [
    ('10.18.99.66', 57522),
]
# 生产环境使用密钥进行登录，这里测试环境使用用户名和密码
SSH_USER = credentials.USER
SSH_PASSWORD = credentials.PASSWORD
