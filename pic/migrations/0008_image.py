# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-05 08:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pic', '0007_auto_20190305_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.ImageField(upload_to='images/')),
                ('image_name', models.CharField(max_length=30)),
                ('image_description', models.CharField(max_length=30)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('image_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pic.Category')),
                ('image_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pic.Location')),
            ],
            options={
                'ordering': ['image_name'],
            },
        ),
    ]
