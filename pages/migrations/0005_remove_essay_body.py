# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_essay_preface'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='essay',
            name='body',
        ),
    ]
