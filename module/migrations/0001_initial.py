# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-10 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mName', models.CharField(max_length=20)),
                ('mUrl', models.CharField(max_length=200)),
            ],
        ),
    ]