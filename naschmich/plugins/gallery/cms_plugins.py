from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .models import Gallery4, Gallery6, Gallery8


class Gallery4Plugin(CMSPluginBase):
    model = Gallery4
    render_template = "gallery_with_4.html"
    cache = False


class Gallery6Plugin(CMSPluginBase):
    model = Gallery6
    render_template = "gallery_with_6.html"
    cache = False


class Gallery8Plugin(CMSPluginBase):
    model = Gallery8
    render_template = "gallery_with_8.html"
    cache = False


plugin_pool.register_plugin(Gallery4Plugin)
plugin_pool.register_plugin(Gallery6Plugin)
plugin_pool.register_plugin(Gallery8Plugin)
