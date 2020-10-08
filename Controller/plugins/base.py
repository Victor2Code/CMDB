#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @author: xiaofu
# @date: 2020-Oct-08


class BasePlugin:
    """
    所有插件的父类，用来约束之类中必须实现process方法
    """

    def process(self, method, host):
        raise NotImplementedError('{}必须实现process方法'.format(self.__class__.__name__))
