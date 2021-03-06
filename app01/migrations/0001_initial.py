# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-12 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='名称')),
                ('address', models.CharField(max_length=128, verbose_name='地址')),
            ],
            options={
                'verbose_name': '出版社',
                'verbose_name_plural': '出版社',
            },
        ),
    ]
