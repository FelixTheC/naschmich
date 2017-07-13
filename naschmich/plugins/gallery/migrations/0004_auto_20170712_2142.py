# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20170712_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery4',
            name='header',
            field=models.CharField(max_length=100, default='Gallery'),
        ),
        migrations.AddField(
            model_name='gallery6',
            name='header',
            field=models.CharField(max_length=100, default='Gallery'),
        ),
        migrations.AddField(
            model_name='gallery8',
            name='header',
            field=models.CharField(max_length=100, default='Gallery'),
        ),
        migrations.AlterField(
            model_name='gallery4',
            name='pic1',
            field=filer.fields.image.FilerImageField(blank=True, null=True, related_name='Gallery4_pic1', to='filer.Image'),
        ),
        migrations.AlterField(
            model_name='gallery4',
            name='pic2',
            field=filer.fields.image.FilerImageField(blank=True, null=True, related_name='Gallery4_pic2', to='filer.Image'),
        ),
        migrations.AlterField(
            model_name='gallery4',
            name='pic3',
            field=filer.fields.image.FilerImageField(blank=True, null=True, related_name='Gallery4_pic3', to='filer.Image'),
        ),
        migrations.AlterField(
            model_name='gallery4',
            name='pic4',
            field=filer.fields.image.FilerImageField(blank=True, null=True, related_name='Gallery4_pic4', to='filer.Image'),
        ),
    ]
