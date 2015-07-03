# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Porteiro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porteiro',
            name='data_de_nascimento',
            field=models.CharField(max_length=10),
        ),
    ]
