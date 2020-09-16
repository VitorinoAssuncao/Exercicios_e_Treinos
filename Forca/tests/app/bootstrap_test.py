import unittest
from unittest.mock import Mock,patch
from app.bootstrap import Bootstrap

class Bootstrap_Test(unittest.TestCase):
    def test_execute(self):
        bootstrap = Bootstrap()
        bootstrap.execute()
        self.assertTrue(1==1)