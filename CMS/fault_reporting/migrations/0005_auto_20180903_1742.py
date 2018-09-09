# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-03 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fault_reporting', '0004_auto_20180903_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faultreport',
            name='comment_count',
            field=models.IntegerField(default=0, verbose_name='评论数'),
        ),
        migrations.AlterField(
            model_name='faultreport',
            name='down_count',
            field=models.IntegerField(default=0, verbose_name='踩灭数'),
        ),
        migrations.AlterField(
            model_name='faultreport',
            name='up_count',
            field=models.IntegerField(default=0, verbose_name='点赞数'),
        ),
    ]
