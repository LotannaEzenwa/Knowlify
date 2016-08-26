from unittest import TestCase
from context import knowlify
import urllib


class TestLoad(TestCase):
    def test_have_version(self):
        s = knowlify.__version__
        self.assertTrue(isinstance(s, basestring))

    def test_load_local_html(self):
        pass

    def test_load_external_html(self):
        pass

