#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @author: xiaofu
# @date: 2020-Oct-07
from importlib import import_module

from Controller.settings import PLUGINS


def get_server_info(method, host):
    server_info = {}
    for key, path in PLUGINS.items():
        module_path, class_name = path.rsplit('.', maxsplit=1)
        module = import_module(module_path)
        if hasattr(module, class_name):
            obj = getattr(module, class_name)()
            info = obj.process(method, host)
            # print(key,info)
            server_info[key] = info
    # print(server_info)
    return server_info
