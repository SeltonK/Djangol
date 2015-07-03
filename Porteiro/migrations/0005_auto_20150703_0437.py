# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Porteiro', '0004_porteiro_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='porteiro',
            name='data_de_nascimento',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='porteiro',
            name='deficiente',
            field=models.CharField(max_length=3, null=True, choices=[(b'sim', b'Sim'), (b'nao', b'Nao')]),
        ),
        migrations.AddField(
            model_name='porteiro',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='porteiro',
            name='foto',
            field=models.ImageField(null=True, upload_to=b'images'),
        ),
        migrations.AddField(
            model_name='porteiro',
            name='rg',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='porteiro',
            name='telefone',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='porteiro',
            name='nome',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
