# -*- coding: utf-8 -*-
"""
适配器模式:
    当系统的数据和行为都正确,但接口不符时,使用适配器,目的是使控制范围之外的一个原有对象与某个接口匹配
    适配器主要应用于希望复用一些现存的类,但是接口又与复用环境要求不一致的情况
 
 Created by 相濡HH on 3/17/15.
"""


class Target(object):
    """
    供客户端调用的接口,返回一个具体的类
    """

    def call_method(self):
        """
        调用方法,在具体的子类中,需要实现的方法,
        :return:
        """


class AdapterTarget(object):
    """
    已有的类,但无法直接被客户端调用,需要通过适配器进行中转
    """

    def tartget_method(self):
        """
        最终要调用方法
        :return:
        """
        print("最终目的是打印:200块钱")


class Adapter(Target):
    """
    具体的适配器子类,实例化后为客户端调用实例对象
    """

    def __init__(self):
        """
        初始化方法,将目标类实例化后赋值
        :return:
        """
        self.__target = AdapterTarget()

    def call_method(self):
        """
        中转方法,调用目标类具体的方法
        :return:
        """
        print("原本打印:100块")
        self.__target.tartget_method()


class Client(object):
    """
    客户端类,用于测试适配器模式
    """

    def __init__(self):
        """

        :return:
        """
        self.__target = Adapter()

    def test(self):
        """
        调用方法
        :return:
        """
        self.__target.call_method()


if __name__ == '__main__':
    """
    单独调用
    """
    client = Client()
    client.test()
