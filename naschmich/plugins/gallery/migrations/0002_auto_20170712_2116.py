# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='gallery6',
            name='pic1',
            field=filer.fields.image.FilerImageField(blank=True, null=True, related_name='Gallery6_pic1', to='filer.Image'),
        ),
        migrations.AlterField(
            model_name='gallery6',
            name='pic2',
            field=filer.fields.image.FilerImageField(blank=True, null=True, related_name='Gallery6_pic2', to='filer.Image'),
        ),
        migrations.AlterField(
            model_name='gallery6',
            name='pic3',
            field=filer.fields.image.FilerImageField(blank=True, null=True, related_name='Gallery6_pic3', to='filer.Image'),
        ),
        migrations.AlterField(
            model_name='gallery6',
            name='pic4',
            field=filer.fields.image.FilerImageField(blank=True, null=True, related_name='Gallery6_pic4', to='filer.Image'),
        ),
        migrations.AlterField(
            model_name='gallery6',
            name='pic5',
            field=filer.fields.image.FilerImageField(blank=True, null=True, related_name='Gallery6_pic5', to='filer.Image'),
        ),
        migrations.AlterField(
            model_name='gallery6',
            name='pic6',
            field=filer.fields.image.FilerImageField(blank=True, null=True, related_name='Gallery6_pic6', to='filer.Image'),
        ),
        migrations.AlterField(
            model_name='gallery8',
            name='pic1',
            field=filer.fields.image.FilerImageField(blank=True, null=True, related_name='Gallery8_pic1', to='filer.Image'),
        ),
        migrations.AlterField(
            model_name='gallery8',
            name='pic2',
            field=filer.fields.image.FilerImageField(blank=True, null=True, related_name='Gallery8_pic2', to='filer.Image'),
        ),
        migrations.AlterField(
            model_name='gallery8',
            name='pic3',
            field=filer.fields.image.FilerImageField(blank=True, null=True, related_name='Gallery8_pic3', to='filer.Image'),
        ),
        migrations.AlterField(
            model_name='gallery8',
            name='pic4',
            field=filer.fields.image.FilerImageField(blank=True, null=True, related_name='Gallery8_pic4', to='filer.Image'),
        ),
        migrations.AlterField(
            model_name='gallery8',
            name='pic5',
            field=filer.fields.image.FilerImageField(blank=True, null=True, related_name='Gallery8_pic5', to='filer.Image'),
        ),
        migrations.AlterField(
            model_name='gallery8',
            name='pic6',
            field=filer.fields.image.FilerImageField(blank=True, null=True, related_name='Gallery8_pic6', to='filer.Image'),
        ),
        migrations.AlterField(
            model_name='gallery8',
            name='pic7',
            field=filer.fields.image.FilerImageField(blank=True, null=True, related_name='Gallery8_pic7', to='filer.Image'),
        ),
        migrations.AlterField(
            model_name='gallery8',
            name='pic8',
            field=filer.fields.image.FilerImageField(blank=True, null=True, related_name='Gallery8_pic8', to='filer.Image'),
        ),
    ]
