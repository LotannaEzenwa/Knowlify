from unittest import TestCase
from context import knowlify


class TestLoad(TestCase):
    def test_have_version(self):
        s = knowlify.__version__
        self.assertTrue(isinstance(s, basestring))
