# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-23 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destinatario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=14)),
                ('indicador_ie_destinatario', models.IntegerField(blank=True, null=True)),
                ('inscricao_estadual', models.CharField(max_length=20)),
                ('isuf', models.CharField(blank=True, max_length=50, null=True)),
                ('nome_razao', models.CharField(max_length=200)),
                ('fone', models.CharField(blank=True, max_length=13, null=True)),
                ('cep', models.CharField(max_length=8)),
                ('logradouro', models.CharField(max_length=200)),
                ('numero_casa', models.CharField(blank=True, max_length=10, null=True)),
                ('complemento', models.CharField(blank=True, max_length=100, null=True)),
                ('bairro', models.CharField(max_length=200)),
                ('cidade_codigo', models.IntegerField(blank=True, null=True)),
                ('cidade', models.CharField(max_length=200)),
                ('uf', models.CharField(max_length=2)),
                ('pais_codigo', models.IntegerField(default=1058)),
                ('pais', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('nome_razao',),
                'db_table': 'destinatario',
            },
        ),
        migrations.CreateModel(
            name='Emitente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=14)),
                ('inscricao_estadual', models.CharField(max_length=20)),
                ('nome_razao', models.CharField(max_length=200)),
                ('nome_fantasia', models.CharField(max_length=200)),
                ('fone', models.CharField(blank=True, max_length=13, null=True)),
                ('cep', models.CharField(max_length=8)),
                ('logradouro', models.CharField(max_length=200)),
                ('numero_casa', models.CharField(blank=True, max_length=10, null=True)),
                ('complemento', models.CharField(blank=True, max_length=100, null=True)),
                ('bairro', models.CharField(max_length=200)),
                ('cidade_codigo', models.IntegerField(blank=True, null=True)),
                ('cidade', models.CharField(max_length=200)),
                ('uf', models.CharField(max_length=2)),
                ('im', models.CharField(max_length=50)),
                ('cnae', models.CharField(max_length=50)),
                ('pais_codigo', models.IntegerField(default=1058)),
                ('pais', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('nome_fantasia', 'nome_razao'),
                'db_table': 'emitente',
            },
        ),
    ]
