# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-05-12 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180512_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='images/blog_default.png', upload_to='images/blog/%Y/%m', verbose_name='封面'),
        ),
    ]