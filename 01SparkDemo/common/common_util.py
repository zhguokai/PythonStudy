"""
get SparkContext
"""
__author__ = 'python'

from pyspark import SparkContext,SparkConf,SparkJobInfo,SparkStageInfo,SparkFiles

def get_sparkcontext():

    conf = SparkConf()
    conf.setAppName("sparkDemo")
    conf.setMaster("local")
    spark_context = SparkContext(conf=conf)
    return spark_context

