# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20161224_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='PType',
            field=models.BooleanField(default=True, verbose_name=b'PostType:'),
            preserve_default=False,
        ),
    ]
