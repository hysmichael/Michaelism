# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_remove_essay_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, db_index=True)),
                ('color', colorful.fields.RGBColorField()),
            ],
        ),
        migrations.RemoveField(
            model_name='essay',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AddField(
            model_name='essay',
            name='category',
            field=models.ForeignKey(related_name='essays', blank=True, to='pages.Category', null=True),
        ),
    ]
