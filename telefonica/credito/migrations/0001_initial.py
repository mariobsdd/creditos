# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-03 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('salario', models.FloatField()),
                ('tel1', models.IntegerField(max_length=8)),
                ('tel2', models.IntegerField(max_length=8)),
                ('tel3', models.IntegerField(max_length=8)),
                ('cuota', models.FloatField()),
                ('tipo', models.BooleanField(default=True)),
            ],
        ),
    ]
