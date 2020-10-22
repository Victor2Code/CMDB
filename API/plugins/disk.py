#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @author: xiaofu
# @date: 2020-Oct-22
from API.models import Disk
from API.plugins.base import BaseHandler


class DiskHandler(BaseHandler):
    """
    处理汇报来的硬盘信息
    """

    def process(self, server_obj, info):
        disk_info = info.get('disk')
        if not disk_info['status']:
            print('获取硬盘资产信息出错，错误信息如下')
            print(disk_info['error'])
            return
        else:
            new_disk_info = disk_info['data']  # 新汇报上来的硬盘数据
            db_disks = Disk.objects.filter(server=server_obj)
            db_disk_info = {row.slot: row for row in db_disks}  # db中已存在的硬盘数据，没有则为空集合
            new_slot_set = set(new_disk_info)  # 对字典进行set操作只会将key加入集合
            db_slot_set = set(db_disk_info)
            create_slot_set = new_slot_set - db_slot_set
            update_slot_set = new_slot_set & db_slot_set
            delete_slot_set = db_slot_set - new_slot_set
            print('新增：', create_slot_set)
            print('更新：', update_slot_set)
            print('删除：', delete_slot_set)
            ## 新增
            for slot in create_slot_set:
                Disk.objects.create(**new_disk_info[slot], server=server_obj)

            ## 删除
            Disk.objects.filter(server=server_obj, slot__in=delete_slot_set).delete()

            ## 更新
            for slot in update_slot_set:
                for key, value in new_disk_info[slot].items():
                    setattr(db_disk_info[slot], key, value)  # 因为key是字符串，不能直接通过点号来赋值
                    db_disk_info[slot].save()
