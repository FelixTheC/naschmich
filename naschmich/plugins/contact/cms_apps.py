from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from . import views

class ContactApp(CMSApp):
    name = _("Contact Apphook")
    app_name = 'contact'

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            url(r'^$', views.contact_view),
        ]

apphook_pool.register(ContactApp)
