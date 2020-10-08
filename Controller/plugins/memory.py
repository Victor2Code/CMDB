#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @author: xiaofu
# @date: 2020-Oct-08
from Controller.plugins.base import BasePlugin


class MemoryPlugin(BasePlugin):
    """
    采集内存信息
    """
    def process(self, method, host):
        return {'memory': '16G'}