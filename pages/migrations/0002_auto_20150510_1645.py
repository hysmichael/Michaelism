# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essay',
            name='bundle',
            field=models.ForeignKey(related_name='essays', blank=True, to='pages.EssayBundle', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='essay',
            name='posted_at',
            field=models.DateField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='essay',
            name='tags',
            field=models.ManyToManyField(related_name='essays', null=True, to='pages.Tag', blank=True),
            preserve_default=True,
        ),
    ]
