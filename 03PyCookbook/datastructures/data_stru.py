# -*- coding: utf-8 -*-
"""
CookBook 数据结构与算法
序列分解工作实际上不仅仅对元组、列表有效，它对所有可迭代的对象有效，如字符串、文件、
迭代器、生成器
"""

# 将序列的元素分解成单个的元素
"""
You have an N-element tuple or sequence that you would like to unpack into a collection of N
variables.
"""
# 使用赋值操作符解决

def unpack_sequence():
    data_tuple = (4, 5)
    x, y = data_tuple
    print(x, y)

    data_list = ['ACME', 50, 91.1, (2012, 12, 21)]
    name, shares, price, date = data_list
    print(name, shares, price, date)

    data_string = "hello"
    a, b, c, d, e = data_string
    print(a, b, c, d, e)

    _, shares, price, _ = data_list
    print(shares, price)


"""
You need to unpack N elements from an iterable, but the iterable may be longer than N elements,
causing a “too many values to unpack” exception
"""
# 分解任意数量的元素
"""
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)
"""


def unpack_arbitrary_sequence():
    record = ('Dave', 'dave@example.com', '733-555-1212', '847-555-1212')
    name, email, *phone_numbers = record
    print(phone_numbers)


if __name__ == '__main__':
    unpack_sequence()
