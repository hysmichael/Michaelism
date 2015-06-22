# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20150510_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essay',
            name='tags',
            field=models.ManyToManyField(related_name='essays', to='pages.Tag', blank=True),
        ),
    ]
