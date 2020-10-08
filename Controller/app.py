#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @author: xiaofu
# @date: 2020-Oct-07

import paramiko
import requests

from Controller import settings


def get_server_info(hostname, port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)  # 初次连接自动信任
    ssh.connect(hostname, port, settings.SSH_USER, settings.SSH_PASSWORD)  # 生产环境使用key登录，这里测试环境使用统一密码
    stdin, stdout, stderr = ssh.exec_command('df')
    # print(stdout)  # paramiko.ChannelFile
    # print(type(stdout))  # <class 'paramiko.channel.ChannelFile'>
    result = stdout.read()  # 类文件对象，可以用操作文件的方式来操作，返回bytes类型
    ssh.close()  # 不要忘记关闭连接
    return result.decode('utf-8')[:10]


def run():
    # 获取服务器资产信息
    for host in settings.SSH_HOST_LIST:
        result = get_server_info(host[0], host[1])
        # print(result)
        # 资产信息发送到API平台入库
        # 可以使用get请求
        # response=requests.get('http://127.0.0.1:8000/api/get_data/', params={'host':host[0],'info':result})
        # 也可以使用post请求，但是要注意csrf
        response = requests.post('http://127.0.0.1:8000/api/get_data/', data={'host': host[0], 'info': result})
        print(response.text)


if __name__ == '__main__':
    run()
