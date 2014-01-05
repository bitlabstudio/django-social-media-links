"""Just an empty models file to let the testrunner recognize this as app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _


class LinkType(models.Model):
    """
    Different link types can have different social media icons.

    :name: The name of this link type, i.e. 'Facebook'
    :symbol: The code for the symbol of this link type. See
      http://drinchev.github.io/monosocialiconsfont/ for available codes.
    :image: If you don't want to use the font, you can upload an image.

    """
    name = models.CharField(
        max_length=256,
        verbose_name=_('Name'),
    )

    symbol = models.CharField(
        max_length=256,
        verbose_name=_('Symbol'),
        blank=True,
    )

    image = models.ImageField(
        upload_to='social_media_links',
        verbose_name=_('Image'),
        null=True, blank=True,
    )

    def __unicode__(self):
        return self.name


class Link(models.Model):
    """
    A link to a social media profile.

    :link_type: The type of this link.
    :name: The display name for this link.
    :url: The href attribute of this link.
    :title: The title attribute of this link.

    """
    link_type = models.ForeignKey(
        LinkType,
        verbose_name=_('Link type'),
    )

    name = models.CharField(
        max_length=256,
        verbose_name=_('Name'),
    )

    url = models.CharField(
        max_length=4000,
        verbose_name=_('URL'),
    )

    title = models.CharField(
        max_length=512,
        verbose_name=_('Title'),
        blank=True,
    )

    position = models.IntegerField(
        verbose_name=_('Position'),
        blank=True, null=True,
    )

    class Meta:
        ordering = ('position', )

    def __unicode__(self):
        return self.name
