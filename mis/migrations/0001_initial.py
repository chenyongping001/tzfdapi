# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-03-28 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeePhone',
            fields=[
                ('ygdm', models.CharField(max_length=55, primary_key=True, serialize=False)),
                ('ygmc', models.CharField(max_length=55)),
                ('sjhm', models.CharField(max_length=55)),
                ('dhhm', models.CharField(blank=True, max_length=55, null=True)),
                ('bgdh', models.CharField(blank=True, max_length=55, null=True)),
            ],
            options={
                'db_table': 'v_cyp_ygsj',
                'managed': False,
            },
        ),
    ]
