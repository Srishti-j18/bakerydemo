# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 21:57
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("locations", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="locationsindexpage",
            name="body",
        ),
    ]
