# Generated by Django 3.0.6 on 2021-06-28 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_auto_20210628_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assigntime',
            name='enddate',
        ),
        migrations.RemoveField(
            model_name='assigntime',
            name='startdate',
        ),
        migrations.AlterField(
            model_name='attendancerange',
            name='end_date',
            field=models.DateField(default='2018-10-23'),
        ),
        migrations.AlterField(
            model_name='attendancerange',
            name='start_date',
            field=models.DateField(default='2018-10-23'),
        ),
    ]
