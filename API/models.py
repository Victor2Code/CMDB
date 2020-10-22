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
