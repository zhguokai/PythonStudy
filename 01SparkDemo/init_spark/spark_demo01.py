# -*- coding: utf-8 -*-

__author__ = 'python'

"""
RDD 转换与操作
"""
from common import spark_context as sc


def rdd_func(line):
    """
    自定义方法，用于分解行内容
    :param line:
    :return:
    """
    words = line.split(" ")
    return len(words)


def rdd_basics():
    # 读取文件
    lines = sc.textFile('data.txt')
    # lines 为行的遍历器
    # line_length = lines.map(lambda s: len(s))
    # 传递函数
    line_length = lines.map(rdd_func)
    total_length = line_length.reduce(lambda a, b: a + b)
    print "总长度：%d" % total_length
    line_length.persist()


def rdd_key_operation():
    """
    操作KEY_VALUE Pairs
    :return:
    """
    lines = sc.textFile('data.txt')
    pairs = lines.map(lambda s: (s, 1))
    counts = pairs.reduceByKey(lambda a, b: a + b)
    print "数据： %s " % counts.collect()


def broadcast_variables():
    """
    共享数据
    :return:
    """
    broadcast_var = sc.broadcast([1, 2, 3, ])
    print broadcast_var.value


def accumulator():
    """
    累加器，只支持数字类型
    :return:
    """
    accum = sc.accumulator(0)
    sc.parallelize([1, 2, 3, 4, 5, 6]).foreach(lambda x: accum.add(x + 3))
    print accum.value


if __name__ == "__main__":
    # rdd_basics()
    # rdd_key_operation()
    # broadcast_variables()
    accumulator()
