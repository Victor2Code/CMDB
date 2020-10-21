#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @author: xiaofu
# @date: 2020-Oct-20

import traceback

from Controller.plugins.base import BasePlugin
from tools.log import controller_logger
from tools.response import BaseResponse


class BoardPlugin(BasePlugin):
    """
    采集主板信息
    """

    def process(self, method, host):
        result = BaseResponse()
        try:
            response = method(host[0], host[1], 'dmidecode -t 1')
            result.data=self.parse(response)
        except Exception as e:
            result.status = False
            result.error = traceback.format_exc()
            controller_logger.error(traceback.format_exc())
        return result.dict
        # return method(host[0],host[1],'df')

    def parse(self, content):
        """
        从主板原始返回提取有用数据
        :param content:
        :return:
        """
        result = {}
        key_map = {
            'Manufacturer': 'manufacturer',
            'Product Name': 'model',
            'Serial Number': 'sn',
        }
        for item in content.split('\n'):
            raw_data = item.strip().split(':')
            if len(raw_data) == 2 and raw_data[0] in key_map:
                result[key_map[raw_data[0]]] = raw_data[1].strip()
        return result
