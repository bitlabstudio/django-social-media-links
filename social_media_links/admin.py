"""Admin classes for the social_media_links app."""
from django.contrib import admin

from . import models


class LinkTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'symbol', ]


class LinkAdmin(admin.ModelAdmin):
    list_display = ['link_type', 'name', 'url', 'title', 'position', ]


admin.site.register(models.LinkType, LinkTypeAdmin)
admin.site.register(models.Link, LinkAdmin)
