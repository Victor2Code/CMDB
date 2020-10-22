#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @author: xiaofu
# @date: 2020-Oct-22

from importlib import import_module

from CMDB.settings import API_HANDLER_PLUGINS


def info_handler(server_obj, info):
    for key, value in API_HANDLER_PLUGINS.items():
        module_path, class_name = value.rsplit('.', maxsplit=1)
        module = import_module(module_path)
        if hasattr(module, class_name):
            obj = getattr(module, class_name)()
            obj.process(server_obj, info)


if __name__ == '__main__':
    info_handler()
