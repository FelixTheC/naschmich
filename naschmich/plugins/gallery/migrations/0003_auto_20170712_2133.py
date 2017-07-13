# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20170712_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery4',
            name='pic1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='gallery4',
            name='pic2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='gallery4',
            name='pic3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='gallery4',
            name='pic4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
