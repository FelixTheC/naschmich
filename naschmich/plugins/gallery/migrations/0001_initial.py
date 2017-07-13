# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery4',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='gallery_gallery4', parent_link=True, to='cms.CMSPlugin')),
                ('pic1', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic2', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic3', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic4', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Gallery6',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='gallery_gallery6', parent_link=True, to='cms.CMSPlugin')),
                ('pic1', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic2', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic3', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic4', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic5', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic6', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Gallery8',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='gallery_gallery8', parent_link=True, to='cms.CMSPlugin')),
                ('pic1', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic2', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic3', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic4', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic5', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic6', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic7', models.ImageField(blank=True, null=True, upload_to='')),
                ('pic8', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
