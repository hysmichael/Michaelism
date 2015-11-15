# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20150629_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='essay',
            name='abstract',
            field=models.TextField(null=True, blank=True),
        ),
    ]
