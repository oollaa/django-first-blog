# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-09 14:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='crated_date',
            new_name='created_date',
        ),
    ]
