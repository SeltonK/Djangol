# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Porteiro', '0007_auto_20150703_0447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='porteiro',
            name='foto',
        ),
    ]
