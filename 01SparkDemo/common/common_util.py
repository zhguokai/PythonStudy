"""
get SparkContext
"""
__author__ = 'python'

import os

from pyspark import SparkContext, SparkConf


def get_sparkcontext():
    conf = SparkConf()
    conf.setAppName("sparkDemo")
    conf.setMaster("local[5]")
    spark_context = SparkContext(conf=conf)
    return spark_context
