# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-11 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geradornf', '0009_transportador_cep'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('data_cadastro', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
