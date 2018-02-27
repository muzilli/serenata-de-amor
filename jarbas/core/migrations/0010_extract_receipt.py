# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_add_latitude_and_longitude'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, default=None, max_length=128, null=True, verbose_name='URL')),
                ('fetched', models.BooleanField(default=False, verbose_name='Was fetched?')),
            ],
        ),
        migrations.RemoveField(
            model_name='document',
            name='receipt_fetched',
        ),
        migrations.RemoveField(
            model_name='document',
            name='receipt_url',
        ),
        migrations.AddField(
            model_name='receipt',
            name='document',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Document'),
        ),
    ]
