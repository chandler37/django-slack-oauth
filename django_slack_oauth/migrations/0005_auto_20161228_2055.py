# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 20:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_slack_oauth', '0004_auto_20161226_1937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slackoauthrequest',
            options={'verbose_name': 'Slack OAuth Request', 'verbose_name_plural': 'Slack OAuth Requests'},
        ),
    ]
