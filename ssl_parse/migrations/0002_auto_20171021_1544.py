# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_parse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='common_name',
            field=models.TextField(null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='country_name',
            field=models.TextField(null=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='email_address',
            field=models.TextField(null=True, verbose_name='Электронный адрес'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='given_name',
            field=models.TextField(null=True, verbose_name='Имя, Отчество'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='locality_name',
            field=models.TextField(null=True, verbose_name='Местоположение'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='organization_name',
            field=models.TextField(null=True, verbose_name='Организация'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='state_or_province_name',
            field=models.TextField(null=True, verbose_name='Регион'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='street_address',
            field=models.TextField(null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='surname',
            field=models.TextField(null=True, verbose_name='Фамилия'),
        ),
    ]