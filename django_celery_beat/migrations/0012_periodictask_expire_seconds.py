# Generated by Django 2.2.4 on 2019-08-30 00:46
# flake8: noqa
from __future__ import absolute_import, unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0011_auto_20190508_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodictask',
            name='expire_seconds',
            field=models.PositiveIntegerField(blank=True, help_text='Timedelta with seconds which the schedule will no longer trigger the task to run', null=True, verbose_name='Expires timedelta with seconds'),
        ),
    ]
