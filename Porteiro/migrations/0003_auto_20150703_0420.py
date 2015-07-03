# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Porteiro', '0002_auto_20150701_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='porteiro',
            name='celular',
        ),
        migrations.RemoveField(
            model_name='porteiro',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='porteiro',
            name='data_de_nascimento',
        ),
        migrations.RemoveField(
            model_name='porteiro',
            name='deficiente',
        ),
        migrations.RemoveField(
            model_name='porteiro',
            name='email',
        ),
        migrations.RemoveField(
            model_name='porteiro',
            name='foto',
        ),
        migrations.RemoveField(
            model_name='porteiro',
            name='rg',
        ),
        migrations.RemoveField(
            model_name='porteiro',
            name='telefone',
        ),
    ]
