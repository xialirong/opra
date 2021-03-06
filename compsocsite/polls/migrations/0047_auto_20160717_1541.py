# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-17 19:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0046_remove_question_openhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllocationVoter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='question_voters',
            field=models.ManyToManyField(related_name='poll_participated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='allocationvoter',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
        migrations.AddField(
            model_name='allocationvoter',
            name='response',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Response'),
        ),
        migrations.AddField(
            model_name='allocationvoter',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
