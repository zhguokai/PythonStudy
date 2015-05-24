# -*- coding: utf-8 -*-
"""
    建造者模式,建造指挥者
 
 Created by 相濡HH on 3/15/15.
"""


class Director(object):
    """
    建造指挥者
    """

    def __init__(self, builder):
        """

        :return:
        """
        self.builder = builder

    def create_product(self):
        """
        创建产品
        :return:
        """
        self.builder.build_product_hand()
        self.builder.build_product_eye()
        self.builder.build_product_body()
        self.builder.build_product_hand()
        return self.builder.getPerson()
