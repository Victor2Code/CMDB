from django.db import models


# Create your models here.


class Server(models.Model):
    """
    服务器表
    """
    host = models.CharField(max_length=32, verbose_name='主机名')

    class Meta:
        db_table = 'Server'


class Disk(models.Model):
    """
    硬盘表
    """
    slot = models.CharField(max_length=2, verbose_name='槽位')
    pd_type = models.CharField(max_length=16, verbose_name='类型')
    capacity = models.FloatField(default=0, verbose_name='容量')
    model = models.CharField(max_length=256, verbose_name='型号')
    server = models.ForeignKey(Server, on_delete=models.CASCADE, verbose_name='服务器')

    class Meta:
        db_table = 'Disk'


class Record(models.Model):
    """
    资产变更记录
    """
    server = models.ForeignKey(Server, on_delete=models.CASCADE,verbose_name='服务器')
    content = models.TextField(verbose_name='内容')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='时间')  # auto_now_add只记录第一次时间，auto_now每次修改都会更新

    class Meta:
        db_table = 'Record'
