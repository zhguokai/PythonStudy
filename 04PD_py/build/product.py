# -*- coding: utf-8 -*-
"""

 
 Created by 相濡HH on 3/15/15.
"""


class Product(object):
    """
    产品
    """

    def __init__(self):
        """
        定义完整的人
        :return:
        """
        self.person = {}

    def add_head(self, part_str):
        """
        增加头部
        :param head:
        :return:
        """
        self.person['head'] = part_str

    def add_body(self, part_str):
        """
        增加身体
        :param head:
        :return:
        """
        self.person['body'] = part_str

    def add_hand(self, part_str):
        """
        增加身体
        :param head:
        :return:
        """
        self.person['hand'] = part_str

    def add_eye(self, part_str):
        """
        增加眼睛
        :param head:
        :return:
        """
        self.person['eye'] = part_str
