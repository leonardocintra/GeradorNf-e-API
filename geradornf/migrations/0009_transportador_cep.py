# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-10 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geradornf', '0008_auto_20160801_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='transportador',
            name='cep',
            field=models.CharField(default=37990000, max_length=8),
            preserve_default=False,
        ),
    ]