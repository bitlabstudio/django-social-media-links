"""Factories for the social_media_links app."""
import factory

from .. import models


class LinkTypeFactory(factory.DjangoModelFactory):
    """Factory for the ``LinkCategory`` model."""
    FACTORY_FOR = models.LinkType

    name = factory.Sequence(lambda n: 'Category{0}'.format(n))
    symbol = '&#xe224;'


class LinkFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Link

    link_type = factory.SubFactory(LinkTypeFactory)
    name = factory.Sequence(lambda n: 'Link{0}'.format(n))
    url = 'www.example.com'
