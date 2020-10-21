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
    slot = models.CharField(max_length=2)
    pd_type = models.CharField(max_length=16)
    capacity = models.FloatField(default=0)
    model = models.CharField(max_length=256)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Disk'
