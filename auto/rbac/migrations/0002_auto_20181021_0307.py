# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-21 03:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permission',
            old_name='parent_id',
            new_name='parent',
        ),
    ]
