"""Templatetags for the social_media_links app."""
from django import template

from .. import models


register = template.Library()


@register.assignment_tag
def get_social_media_links():
    return models.Link.objects.all()
