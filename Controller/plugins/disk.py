#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @author: xiaofu
# @date: 2020-Oct-08
from Controller.plugins.base import BasePlugin


class DiskPlugin(BasePlugin):
    """
    采集硬盘信息
    """
    def process(self, method, host):
        return method(host[0],host[1],'df')
