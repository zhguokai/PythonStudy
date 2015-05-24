# -*- coding: utf-8 -*-
"""
 Created by 相濡HH on 3/15/15.
"""

import unittest

from build.Builder import ConcreteBuilder_B
from build.director import Director
from build.product import Product


class MyTestCase(unittest.TestCase):
    def test_director(self):
        builder = ConcreteBuilder_B()
        director = Director(builder)
        person = director.create_product()
        for p in person.person:
            print(p)
        print(person)
        self.assertEqual(isinstance(person, Product), True)


if __name__ == '__main__':
    unittest.main()
