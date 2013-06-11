"""Tests for the templatetags of the social_media_links app."""
from django.test import TestCase

from ..templatetags.social_media_links_tags import get_social_media_links
from . import factories


class GetSocialMediaLinksTestCase(TestCase):
    """Tests for the ``get_social_media_links`` assignment tag."""
    def setUp(self):
        factories.LinkFactory()
        factories.LinkFactory()

    def test_tag(self):
        result = get_social_media_links()
        self.assertEqual(result.count(), 2)
