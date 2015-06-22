# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150511_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='essay',
            name='preface',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
