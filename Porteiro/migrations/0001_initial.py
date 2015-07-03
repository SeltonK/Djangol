# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Porteiro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto', models.ImageField(upload_to=b'images')),
                ('nome', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=11)),
                ('celular', models.CharField(max_length=11)),
                ('data_de_nascimento', models.DateTimeField()),
                ('deficiente', models.CharField(max_length=3, choices=[(b'sim', b'Sim'), (b'nao', b'Nao')])),
            ],
        ),
    ]
