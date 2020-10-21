#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @author: xiaofu
# @date: 2020-Oct-08
import re
import traceback

from Controller import settings as cs
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
            # result.data=method(host[0],host[1],'df')
            response = open(cs.LOCAL_DISK_FILE).read()
            result.data = self.parse(response)
        except Exception as e:
            result.status = False
            result.error = traceback.format_exc()
            controller_logger.error(traceback.format_exc())
        return result.dict
        # return method(host[0],host[1],'df')

    def parse(self, content):
        """
        从硬盘原始返回提取有用数据
        :param content:
        :return:
        """
        result = {}
        key_map = {
            'Slot Number': 'slot',
            'Raw Size': 'capacity',
            'Inquiry Data': 'model',
            'PD Type': 'pd_type',
        }
        for item in content.split('\n\n\n\n'):
            temp_dict = {}
            for row in item.split('\n'):
                if not row.strip():
                    continue
                if len(row.split(':')) != 2:
                    continue
                key, value = row.split(':')
                if key in key_map:
                    if key == 'Raw Size':
                        raw_size = re.search(r'(\d+\.\d+)', value.strip())
                        if raw_size:
                            temp_dict[key_map[key]]=raw_size.group()
                        else:
                            temp_dict[key_map[key]]=0
                    else:
                        temp_dict[key_map[key]]=value.strip()
            if temp_dict:
                result[temp_dict[key_map['Slot Number']]]=temp_dict
        return result