# -*- coding: utf-8 -*-
"""

 建造者模式,建造器,是创建一个Product对象的各个部件指定的抽象接口
 Created by 相濡HH on 3/15/15.
"""
from build.product import Product


class Builder(object):
    """
    创建产品各个部分的接口
    """

    def build_product_head(self):
        """
        创建产品头部部分
        :return:
        """

    def build_product_body(self):
        """
        创建产品身体部分
        :return:
        """

    def build_product_hand(self):
        """
        创建产品手部部分
        :return:
        """

    def build_product_eye(self):
        """
        创建产品眼部部分
        :return:
        """

    def getPerson(self):
        """
        返回完整的人物
        :return:
        """


class ConcreteBuilder_A(Builder):
    """
    创建产品各个部分的接口
    """
    person = Product()

    def build_product_head(self):
        """
        创建产品头部部分
        :return:
        """
        self.person.add_head('A的头部')

    def build_product_body(self):
        """
        创建产品身体部分
        :return:
        """
        self.person.add_body('A的身体')

    def build_product_hand(self):
        """
        创建产品手部部分
        :return:
        """
        self.person.add_hand('A的手')

    def build_product_eye(self):
        """
        创建产品眼部部分
        :return:
        """
        self.person.add_eye('A的眼睛')

    def getPerson(self):
        """
        返回完整的人物
        :return:
        """
        return self.person


class ConcreteBuilder_B(Builder):
    """
    创建产品各个部分的接口
    """
    person = Product()

    def build_product_head(self):
        """
        创建产品头部部分
        :return:
        """
        self.person.add_head('B的头部')

    def build_product_body(self):
        """
        创建产品身体部分
        :return:
        """
        self.person.add_body('B的身体')

    def build_product_hand(self):
        """
        创建产品手部部分
        :return:
        """
        self.person.add_hand('B的手')

    def build_product_eye(self):
        """
        创建产品眼部部分
        :return:
        """
        self.person.add_eye('B的眼睛')

    def getPerson(self):
        """
        返回完整的人物
        :return:
        """
        return self.person
