"""Tests for the models of the social_media_links app."""
from django.test import TestCase

from . import factories


class LinkTypeTestCase(TestCase):
    """Tests for the ``LinkType`` model."""
    def test_model(self):
        obj = factories.LinkTypeFactory()
        self.assertTrue(obj.pk)


class LinkTestCase(TestCase):
    """Tests for the ``Link`` model."""
    def test_model(self):
        obj = factories.LinkFactory()
        self.assertTrue(obj.pk)
