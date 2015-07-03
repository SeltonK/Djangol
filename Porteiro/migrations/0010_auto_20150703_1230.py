# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Porteiro', '0009_porteiro_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='porteiro',
            old_name='foto',
            new_name='image',
        ),
    ]
