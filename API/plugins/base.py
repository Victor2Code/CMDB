#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @author: xiaofu
# @date: 2020-Oct-22


class BaseHandler:
    def process(self):
        raise NotImplementedError('{}必须实现process方法'.format(self.__class__.__name__))
