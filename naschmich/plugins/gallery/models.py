from cms.models.pluginmodel import CMSPlugin
from django.db import models
from filer.fields.image import FilerImageField


class Gallery4(CMSPlugin):
    header = models.CharField(max_length=100, default='Gallery')
    pic1 = FilerImageField(null=True, blank=True, related_name='Gallery4_pic1')
    pic2 = FilerImageField(null=True, blank=True, related_name='Gallery4_pic2')
    pic3 = FilerImageField(null=True, blank=True, related_name='Gallery4_pic3')
    pic4 = FilerImageField(null=True, blank=True, related_name='Gallery4_pic4')

class Gallery6(CMSPlugin):
    header = models.CharField(max_length=100, default='Gallery')
    pic1 = FilerImageField(null=True, blank=True, related_name='Gallery6_pic1')
    pic2 = FilerImageField(null=True, blank=True, related_name='Gallery6_pic2')
    pic3 = FilerImageField(null=True, blank=True, related_name='Gallery6_pic3')
    pic4 = FilerImageField(null=True, blank=True, related_name='Gallery6_pic4')
    pic5 = FilerImageField(null=True, blank=True, related_name='Gallery6_pic5')
    pic6 = FilerImageField(null=True, blank=True, related_name='Gallery6_pic6')


class Gallery8(CMSPlugin):
    header = models.CharField(max_length=100, default='Gallery')
    pic1 = FilerImageField(null=True, blank=True, related_name='Gallery8_pic1')
    pic2 = FilerImageField(null=True, blank=True, related_name='Gallery8_pic2')
    pic3 = FilerImageField(null=True, blank=True, related_name='Gallery8_pic3')
    pic4 = FilerImageField(null=True, blank=True, related_name='Gallery8_pic4')
    pic5 = FilerImageField(null=True, blank=True, related_name='Gallery8_pic5')
    pic6 = FilerImageField(null=True, blank=True, related_name='Gallery8_pic6')
    pic7 = FilerImageField(null=True, blank=True, related_name='Gallery8_pic7')
    pic8 = FilerImageField(null=True, blank=True, related_name='Gallery8_pic8')
