# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_parse', '0002_auto_20171021_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='serial_number',
            field=models.TextField(null=True, verbose_name='Серийный номер'),
        ),
    ]
