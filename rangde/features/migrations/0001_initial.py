# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-09 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='investor_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile_number', models.IntegerField(blank=True, null=True)),
                ('email_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'investor_info',
            },
        ),
        migrations.CreateModel(
            name='seek_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_name', models.CharField(blank=True, max_length=255, null=True)),
                ('refer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=255, null=True)),
                ('email_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'seek_info',
            },
        ),
    ]
