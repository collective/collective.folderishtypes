# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.folderishtypes.testing import COLLECTIVE_FOLDERISHTYPES_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.folderishtypes is properly installed."""

    layer = COLLECTIVE_FOLDERISHTYPES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.folderishtypes is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.folderishtypes'))

    def test_browserlayer(self):
        """Test that ICollectiveFolderishtypesLayer is registered."""
        from collective.folderishtypes.interfaces import (
            ICollectiveFolderishtypesLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveFolderishtypesLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_FOLDERISHTYPES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.folderishtypes'])

    def test_product_uninstalled(self):
        """Test if collective.folderishtypes is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.folderishtypes'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveFolderishtypesLayer is removed."""
        from collective.folderishtypes.interfaces import ICollectiveFolderishtypesLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveFolderishtypesLayer, utils.registered_layers())
