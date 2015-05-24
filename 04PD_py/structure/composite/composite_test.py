# -*- coding: utf-8 -*-
"""
 Created by 相濡HH on 3/19/15.
"""

import unittest

from structure.composite.composite import Client


class MyTestCase(unittest.TestCase):
    def test_something(self):
        cl = Client()
        cl.call_method()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
