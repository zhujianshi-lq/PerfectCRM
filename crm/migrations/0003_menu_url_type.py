# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-02-02 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20200203_0603'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='url_type',
            field=models.SmallIntegerField(choices=[(0, 'alias'), (1, 'absolute_url')], default=0),
        ),
    ]
