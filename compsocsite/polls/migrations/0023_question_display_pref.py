# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-24 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_auto_20160622_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='display_pref',
            field=models.IntegerField(default=1),
        ),
    ]
