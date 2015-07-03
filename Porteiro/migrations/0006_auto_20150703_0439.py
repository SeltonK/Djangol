# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Porteiro', '0005_auto_20150703_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porteiro',
            name='data_de_nascimento',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
