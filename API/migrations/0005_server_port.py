# Generated by Django 3.0.3 on 2020-10-23 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_server_last_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='port',
            field=models.IntegerField(default=57522, verbose_name='端口'),
        ),
    ]