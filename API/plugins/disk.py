#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @author: xiaofu
# @date: 2020-Oct-22
from API.models import Disk, Record
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

            record_list = []  # 总的变更记录列表

            ## 新增
            for slot in create_slot_set:
                Disk.objects.create(**new_disk_info[slot], server=server_obj)
                msg = '【新增硬盘】槽位：{slot}，类型：{pd_type}，容量：{capacity}'.format(**new_disk_info[slot])
                record_list.append(msg)

            ## 删除
            Disk.objects.filter(server=server_obj, slot__in=delete_slot_set).delete()
            if delete_slot_set:
                """
                如果没有要删除的槽位，上面的对象操作不会报错，但是会出现空记录，所以要判断
                """
                msg = '【删除硬盘】槽位：{}'.format('，'.join(delete_slot_set))
                record_list.append(msg)

            ## 更新
            for slot in update_slot_set:
                temp = []
                for key, value in new_disk_info[slot].items():
                    if getattr(db_disk_info[slot], key) == value:
                        continue
                    else:
                        msg = '{}由{}改为{}'.format(key, getattr(db_disk_info[slot], key), value)
                        temp.append(msg)
                        setattr(db_disk_info[slot], key, value)  # 因为key是字符串，不能直接通过点号来赋值
                    if temp:
                        record_list.append('【更新硬盘】槽位：{}，'.format(slot) + '；'.join(temp))
                        db_disk_info[slot].save()
            if record_list:
                Record.objects.create(content='\n'.join(record_list), server=server_obj)
