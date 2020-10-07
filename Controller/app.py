#! /usr/bin/env python
# -*- coding: utf-8 -*- 
# @author: xiaofu
# @date: 2020-Oct-07

import paramiko

from Controller import settings

for host in settings.SSH_HOST_LIST:
    transport = paramiko.Transport(host)
    transport.connect(username=settings.SSH_USER, password=settings.SSH_PASSWORD)
    sftp = paramiko.SFTPClient.from_transport(transport)  # sftp基于已经建立链接的transport层ssh协议
    sftp.chdir('/root')
    sftp.mkdir('testSFTP')
    sftp.put('settings.py', 'testSFTP/settings.py')  # 远程路径必须包含文件名
    # 创建一个新文件供下载
    newfile = sftp.file('testSFTP/newfile.txt','w')
    newfile.write('Life is wonderful\nLet\'s have some fun')
    newfile.flush()
    newfile.close()
    sftp.get('testSFTP/newfile.txt','newfile.txt')
    # sftp.close()
    transport.close()

    # ssh = paramiko.SSHClient()
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)  # 初次连接自动信任
    # ssh.connect(host[0], host[1], settings.SSH_USER, settings.SSH_PASSWORD)
    # stdin, stdout, stderr = ssh.exec_command('df')
    # print(stdout)  # paramiko.ChannelFile
    # print(type(stdout))  # <class 'paramiko.channel.ChannelFile'>
    # result = stdout.read()  # 类文件对象，可以用操作文件的方式来操作，返回bytes类型
    # print(result.decode('utf-8'))
    # ssh.close()  # 不要忘记关闭连接
