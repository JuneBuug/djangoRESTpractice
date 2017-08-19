# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 03:40
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('img_url', models.CharField(max_length=2048)),
                ('brand', models.CharField(max_length=128)),
                ('category', models.CharField(max_length=128)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_date', models.DateTimeField(auto_created=True, auto_now=True)),
                ('img_url', models.CharField(max_length=2048)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cs.Product')),
            ],
        ),
    ]