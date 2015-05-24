# -*- coding: utf-8 -*-
"""

 用手机与手机软件 演译桥接模式
 Created by 相濡HH on 3/18/15.
"""


class HandSetSoft(object):
    """
    类型:接口
    """

    def run(self):
        """
        软件运行方法
        :return:
        """


class GameHandSetSoft(HandSetSoft):
    """
    类型:实现类
    游戏类
    """

    def run(self):
        """

        :return:
        """
        print("运行游戏A :A")


class AddressHandSetSoft(HandSetSoft):
    """
    类型:实现类
    通迅录
    """

    def run(self):
        """

        :return:
        """
        print("运行通迅录A :A")


class HadnhandBrand(object):
    """
    手机品牌类,起接口的作用
    """

    def __init__(self):
        """

        :return:
        """
        self.hand_soft = None

    def set_hand_set_soft(self, soft):
        """

        :param soft: HandSetSoft接口的实现类
        :return:
        """
        self.hand_soft = soft

    def run(self):
        """
        运行软件
        :return:
        """


class HandSetBrandM(HadnhandBrand):
    def run(self):
        """
        子类调用接口方法
        :return:
        """
        print("手机M:")
        self.hand_soft.run()


class HandSetBrandN(HadnhandBrand):
    def run(self):
        """
        子类调用接口方法
        :return:
        """
        print("手机N:")
        self.hand_soft.run()


if __name__ == '__main__':
    """
        独立运行
    """

    handBrand = HandSetBrandM()
    handBrand.set_hand_set_soft(GameHandSetSoft())
    handBrand.run()
    handBrand.set_hand_set_soft(AddressHandSetSoft())
    handBrand.run()

    handBrand = HandSetBrandN()
    handBrand.set_hand_set_soft(GameHandSetSoft())
    handBrand.run()
    handBrand.set_hand_set_soft(AddressHandSetSoft())
    handBrand.run()
