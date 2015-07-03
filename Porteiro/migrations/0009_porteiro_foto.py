# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Porteiro', '0008_remove_porteiro_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='porteiro',
            name='foto',
            field=models.ImageField(null=True, upload_to=b'media'),
        ),
    ]
