# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-04 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0004_remove_image_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='date_uploaded',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
