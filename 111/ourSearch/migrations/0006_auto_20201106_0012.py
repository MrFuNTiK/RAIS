# Generated by Django 3.1.3 on 2020-11-05 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourSearch', '0005_auto_20201105_0632'),
    ]

    operations = [
        migrations.CreateModel(
            name='URLTable',
            fields=[
                ('urladress', models.URLField()),
                ('idurl', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='WORDSTable',
            fields=[
                ('idword', models.AutoField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=11)),
            ],
        ),
        migrations.DeleteModel(
            name='OurUrl',
        ),
        migrations.AddField(
            model_name='urltable',
            name='friends',
            field=models.ManyToManyField(to='ourSearch.WORDSTable'),
        ),
    ]
