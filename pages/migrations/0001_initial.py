# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Essay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('body', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True, db_index=True)),
                ('posted_at', models.DateField(null=True, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EssayBundle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, db_index=True)),
                ('localized_name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='essay',
            name='bundle',
            field=models.ForeignKey(related_name='essays', to='pages.EssayBundle', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='essay',
            name='language',
            field=models.ForeignKey(related_name='essays', to='pages.Language'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='essay',
            name='tags',
            field=models.ManyToManyField(related_name='essays', to='pages.Tag'),
            preserve_default=True,
        ),
    ]
