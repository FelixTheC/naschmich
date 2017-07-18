from django.db import models
from cms.models.fields import PlaceholderField


class Contact(models.Model):
    contact_placeholder = PlaceholderField('contact_plugin')
