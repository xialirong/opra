# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 18:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_question_follow_up'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Student'),
        ),
    ]
