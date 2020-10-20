#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @author: xiaofu
# @date: 2020-Oct-08
import traceback

from Controller.plugins.base import BasePlugin
from tools.log import controller_logger
from tools.response import BaseResponse


class DiskPlugin(BasePlugin):
    """
    采集硬盘信息
    """
    def process(self, method, host):
        result = BaseResponse()
        try:
            result.data=method(host[0],host[1],'df')
        except Exception as e:
            result.status = False
            result.error = traceback.format_exc()
            controller_logger.error(traceback.format_exc())
        return result.dict
        # return method(host[0],host[1],'df')
