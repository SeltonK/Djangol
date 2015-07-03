# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Porteiro', '0003_auto_20150703_0420'),
    ]

    operations = [
        migrations.AddField(
            model_name='porteiro',
            name='cpf',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
