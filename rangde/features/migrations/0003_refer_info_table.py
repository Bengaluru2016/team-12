# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-10 00:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_auto_20160710_0551'),
    ]

    operations = [
        migrations.CreateModel(
            name='refer_info_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referrer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('referred_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email_id', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'refer_info',
            },
        ),
    ]
