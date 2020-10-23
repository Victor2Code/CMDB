#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @author: xiaofu
# @date: 2020-Oct-07
from concurrent.futures.thread import ThreadPoolExecutor
from importlib import import_module

import paramiko
import requests

from Controller import settings
from Controller.settings import PLUGINS
from Controller.plugins import get_server_info


def paramiko_ssh(hostname, port, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)  # 初次连接自动信任
    ssh.connect(hostname, port, settings.SSH_USER, settings.SSH_PASSWORD)  # 生产环境使用key登录，这里测试环境使用统一密码
    stdin, stdout, stderr = ssh.exec_command(cmd)
    # print(stdout)  # paramiko.ChannelFile
    # print(type(stdout))  # <class 'paramiko.channel.ChannelFile'>
    result = stdout.read()  # 类文件对象，可以用操作文件的方式来操作，返回bytes类型
    ssh.close()  # 不要忘记关闭连接
    return result.decode('utf-8')


# def run():
#     # 获取服务器资产信息
#     for host in settings.SSH_HOST_LIST:
#         result = get_server_info(host[0], host[1])
#         # print(result)
#         # 资产信息发送到API平台入库
#         # 可以使用get请求
#         # response=requests.get('http://127.0.0.1:8000/api/get_data/', params={'host':host[0],'info':result})
#         # 也可以使用post请求，但是要注意csrf
#         # response = requests.post('http://127.0.0.1:8000/api/get_data/', data={'host': host[0], 'info': result})
#         # post请求中用data关键字传递字典，请求体中自动转换为&符号连接的格式。而如果post中不是用data传输，而是用json，
#         # 那么请求体中还是字典的格式，此时在Django后端是不能用request.POST来获取的，需要用request.body获取原始字典格式再处理
#         # 实际使用中用json传递比较常见，因为可以实现json格式的嵌套
#         response = requests.post('http://127.0.0.1:8000/api/get_data/', json={'host': host[0], 'info': result})
#         print(response.text)


def task(host):
    result = get_server_info(paramiko_ssh, host)
    print(result)
    response = requests.post('http://127.0.0.1:8000/api/get_data/', json={'host': host[0], 'info': result})
    print(response.text)



def run():
    pool = ThreadPoolExecutor(5)
    result = requests.get('http://127.0.0.1:8000/api/get_server/').json()
    # for host in settings.SSH_HOST_LIST:
    for server in result['server_list']:
        pool.submit(task, server)


if __name__ == '__main__':
    run()
