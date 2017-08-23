# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-23 08:07
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(30)], verbose_name='team name'),
        ),
        migrations.AlterField(
            model_name='team',
            name='website',
            field=models.CharField(default='', max_length=100),
        ),
    ]
