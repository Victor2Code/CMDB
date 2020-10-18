#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @author: xiaofu
# @date: 2020-Oct-08
from Controller.plugins.base import BasePlugin
from tools.log import controller_logger


class DiskPlugin(BasePlugin):
    """
    采集硬盘信息
    """
    def process(self, method, host):
        # try:
        #     a=int('sss')
        # except Exception as e:
        #     controller_logger.error('error')
        return method(host[0],host[1],'df')
