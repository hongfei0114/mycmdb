# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-25 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20180825_0244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hosts',
            name='Services',
        ),
        migrations.AddField(
            model_name='hosts',
            name='services',
            field=models.ManyToManyField(related_name='hosts', to='app01.Service'),
        ),
    ]
