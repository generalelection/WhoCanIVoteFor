# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 22:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0002_auto_20160323_1533'),
        ('people', '0003_auto_20160323_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='election',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='elections.Election'),
        ),
    ]