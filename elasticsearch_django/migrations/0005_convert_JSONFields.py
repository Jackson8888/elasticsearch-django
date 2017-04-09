# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-03 16:11
from django.db import migrations

from ..db.fields import JSONField


class Migration(migrations.Migration):

    dependencies = [
        ('elasticsearch_django', '0004_auto_20161129_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchquery',
            name='hits',
            field=JSONField(
                help_text=b'The list of meta info for each of the query matches returned.'
            ),
        ),
        migrations.AlterField(
            model_name='searchquery',
            name='query',
            field=JSONField(help_text=b'The raw ElasticSearch DSL query.'),
        ),
    ]
