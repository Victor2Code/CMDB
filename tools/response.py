#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @author: xiaofu
# @date: 2020-Oct-20


class BaseResponse:
    """
    对资产的返回数据进行数据封装
    """
    def __init__(self, status=True, data=None, error=None):
        self.status = status
        self.data = data
        self.error = error

    @property
    def dict(self):
        return self.__dict__