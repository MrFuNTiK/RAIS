# Generated by Django 3.1.3 on 2020-11-05 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ourSearch', '0006_auto_20201106_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urltable',
            name='friends',
        ),
    ]
