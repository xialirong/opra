# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-04 10:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('polls', '0028_auto_20160702_1713'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiPoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=500)),
                ('status', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MultiPollQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0)),
                ('multipoll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='multipolls.MultiPoll')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='multipoll',
            name='questions',
            field=models.ManyToManyField(through='multipolls.MultiPollQuestion', to='polls.Question'),
        ),
        migrations.AddField(
            model_name='multipoll',
            name='voters',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
