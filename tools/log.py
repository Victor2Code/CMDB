#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @author: xiaofu
# @date: 2020-Oct-18
import logging

from Controller import settings as con_set


class myLogger:
    def __init__(self, filename, level=logging.INFO):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level=level)
        self.handler = logging.FileHandler(filename)  # 存储到文件，还可以有很多种handler
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s - 第%(lineno)s行 - %('
                                           'message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def error(self, message):
        """
        只有error级别的日志会显示详细的堆栈信息
        :param message:
        :return:
        """
        self.logger.error(message, exc_info=True)

    def warning(self, message):
        self.logger.warning(message)


controller_logger = myLogger(con_set.LOGGING_PATH)