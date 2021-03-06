#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @author: xiaofu
# @date: 2020-Oct-08
import traceback

from Controller.plugins.base import BasePlugin
from tools.log import controller_logger
from tools.response import BaseResponse


class MemoryPlugin(BasePlugin):
    """
    采集内存信息
    """
    def process(self, method, host):
        result = BaseResponse()
        try:
            response = method(host[0], host[1], 'dmidecode -q -t 17 2>/dev/null')
            result.data = self.parse(response)
        except Exception as e:
            result.status = False
            result.error = traceback.format_exc()
            controller_logger.error(traceback.format_exc())
        return result.dict


    def parse(self, content):
        """
        从内存原始返回提取有用数据
        :param content:
        :return:
        """
        result = {}
        key_map = {
            'Size': 'Size',
            'Locator': 'Slot',
            'Type': 'Model',
            'Speed': 'Speed',
            'Manufacturer': 'Manufacturer',
            'Serial Number': 'SN',
        }
        devices = content.split('Memory Device')
