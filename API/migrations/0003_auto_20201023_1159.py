# Generated by Django 3.0.3 on 2020-10-23 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20201021_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disk',
            name='capacity',
            field=models.FloatField(default=0, verbose_name='容量'),
        ),
        migrations.AlterField(
            model_name='disk',
            name='model',
            field=models.CharField(max_length=256, verbose_name='型号'),
        ),
        migrations.AlterField(
            model_name='disk',
            name='pd_type',
            field=models.CharField(max_length=16, verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='disk',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Server', verbose_name='服务器'),
        ),
        migrations.AlterField(
            model_name='disk',
            name='slot',
            field=models.CharField(max_length=2, verbose_name='槽位'),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Server', verbose_name='服务器')),
            ],
            options={
                'db_table': 'Record',
            },
        ),
    ]
