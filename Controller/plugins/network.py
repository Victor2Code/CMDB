#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @author: xiaofu
# @date: 2020-Oct-08
from Controller.plugins.base import BasePlugin


class NetworkPlugin(BasePlugin):
    """
    采集网卡信息
    """
    def process(self, method, host):
        return {'ip': '1.2.3.4'}
