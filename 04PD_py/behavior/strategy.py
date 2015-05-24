# -*- coding: utf-8 -*-
"""
  策略模式：定义了算法加族，分别封装起来，让他们之间可以相互替换，此模式让算法的变化，不会影响到使用算法的客户
 
 Created by 相濡HH on 4/9/15.
"""


class Strategy(object):
    """
    封装算法接口
    """

    def alogorithm_interface(self):
        """
        算法接口
        :return:
        """


class ConcreteStrategyA(Strategy):
    """
    算法A实现
    """

    def alogorithm_interface(self):
        """
        算法A实现
        :return:
        """
        print("算法A ：计算 ")


class ConcreteStrategyB(Strategy):
    """
    算法A实现
    """

    def alogorithm_interface(self):
        """
        算法A实现
        :return:
        """
        print("算法B ：计算B ")


class ConcreteStrategyC(Strategy):
    """
    算法A实现
    """

    def alogorithm_interface(self):
        """
        算法A实现
        :return:
        """
        print("算法C ：计算C ")


class Context(object):
    """
    算法上下文管理器
    """

    def __init__(self, type):
        """
        初始化算法接口
        :param algo:
        :return:
        """
        if type == 'A':
            self._algo = ConcreteStrategyA()
        elif type == 'B':
            self._algo = ConcreteStrategyB()
        elif type == 'C':
            self._algo = ConcreteStrategyC()
        else:
            self._algo = None

    def get_result(self):
        """
        调用返回接果
        :return:
        """
        if self._algo is None:
            print("没有合适的算法")
        else:
            self._algo.alogorithm_interface()


class Client(object):
    """
    客户端，演示策略模式的调用
    """

    @staticmethod
    def test():
        context = Context("AB")
        context.get_result()


if __name__ == '__main__':
    Client.test()
