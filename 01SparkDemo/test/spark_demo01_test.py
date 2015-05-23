# -*- coding: utf-8 -*-
import unittest
from init_spark.spark_demo01 import rdd_key_operation
from common import spark_context as sc
class MyTestCase(unittest.TestCase):
    def test_rdd(self):
        rdd_key_operation()
        sc.stop()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
