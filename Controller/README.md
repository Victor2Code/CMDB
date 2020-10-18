## paramiko模块
ssh到远程机器执行远程操作或者通过SFTP上传下载文件，类似功能还可以通过ansible或者saltstack来完成。
### ssh客户端
```python
for host in settings.SSH_HOST_LIST:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)  # 初次连接自动信任
    ssh.connect(host[0], host[1], settings.SSH_USER, settings.SSH_PASSWORD)
    stdin, stdout, stderr = ssh.exec_command('df')
    print(stdout)  # paramiko.ChannelFile
    print(type(stdout))  # <class 'paramiko.channel.ChannelFile'>
    result = stdout.read()  # 类文件对象，可以用操作文件的方式来操作，返回bytes类型
    print(result.decode('utf-8'))
    ssh.close()  # 不要忘记关闭连接
```

### SFTP上传下载文件
```python
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
```

## 反射与工厂模式
出于对源码封闭，对配置文件开放的**开闭原则**，将每个采集项做为单独插件，在配置文件中进行动态导入。

**配置文件**
```python
PLUGINS = {
    'disk': 'plugins.disk.DiskPlugin',
    'memory': 'plugins.memory.MemoryPlugin',
    'network': 'plugins.network.NetworkPlugin',
}
```
**业务代码**
```python
for key, path in PLUGINS.items():
    module_path, class_name = path.rsplit('.', maxsplit=1)
    module = import_module(module_path)
    if hasattr(module, class_name):
        obj = getattr(module, class_name)()
        info = obj.process()
        print(key, info)
```

## 约束
通过工厂模式实现插件的可扩展时，必须保证每个插件类中实现了`process`方法。
为了避免新创建的插件没有实现`process`方法造成反射时候报错，通过所有插件类统一继承自父类并在父类中建立约束来达到该目的。

**父类约束**
```python
class BasePlugin:
    """
    所有插件的父类，用来约束之类中必须实现process方法
    """
    def process(self):
        raise NotImplementedError('{}必须实现process方法'.format(self.__class__.__name__))
```

## 分总的概念
在`plugins`的init文件中对所有的插件进行收集并且返回，而真正在业务代码中只需要将实现ssh执行命令的函数名传递进去即可，该函数可以是用paramiko实现，
或者是ansible和saltstack。

这样使得业务代码尽量精简，各个组件耦合度减低。

## 线程池
因为是IO密集型操作，利用`concurrent.futures`模块创建线程池同时对对台目标服务器进行信息采集


## 单例模式和日志记录
通过单例模式实现的全局日志模块，在`tools/log.py`中定义了自己的日志类`myLogger`，通过自定义文件存储目录和日志记录等级达到
不同模块的日志分开存储的目的。
目前只是调用了`fileHandler`实现日志的文件存储，后续还可以调用`httpHandler`等实现远程日志记录等功能。