# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 11:45
from __future__ import unicode_literals

from django.db import migrations, models
import tweets.models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_tweet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(default='', max_length=140, validators=[tweets.models.validate_content]),
        ),
    ]