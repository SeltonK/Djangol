# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Porteiro', '0006_auto_20150703_0439'),
    ]

    operations = [
        migrations.AddField(
            model_name='porteiro',
            name='bairro',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='porteiro',
            name='cidade',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='porteiro',
            name='numero_da_residencia',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='porteiro',
            name='rua',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='porteiro',
            name='turno',
            field=models.CharField(max_length=5, null=True, choices=[(b'manha', b'Manha'), (b'tarte', b'Tarde'), (b'noite', b'Noite')]),
        ),
    ]
