# -*- coding: utf-8 -*-
"""
  Facade模式,为子系统中的一组接口提供了一个一致的界面,
  Facade模式定义了一个高层的接口,用于组合杂乱无章的接口,将各个单个的接口组合在一起供其他系统调用,减少耦合性
  应用场景:
   设计初期阶段:有意识的将不同的两个层级分离
   开发阶段:不停的重构产生越来越多的类变得复杂时,使外部系统调用更加困难,增加一个Facade类
   后期维护阶段:系统变得难以维护,但又需要增加新功能时,开发一个Facade类来进行旧系统接口的处理工作
 Created by 相濡HH on 3/30/15.
"""


class Facade(object):
    """

    """

    def __init__(self):
        """
        初始化方法
        """
        self.one = SubSystemOne()
        self.two = SubSystemTwo()
        self.three = SubSystemThere()
        self.four = SubSystemFour()

    def method_a(self):
        """
        创建方法组
        """
        print("方法组A :")
        self.one.method()
        self.two.method()

    def method_b(self):
        """
        创建方法组B
        """
        print("方法组B :")
        self.three.method()
        self.four.method()


class SubSystemOne(object):
    """
    子系统A
    """

    def method(self):
        """
        业务操作
        :return:
        """
        print("业务操作A ")


class SubSystemTwo(object):
    """
    子系统A
    """

    def method(self):
        """
        业务操作
        :return:
        """
        print("业务操作B ")


class SubSystemThere(object):
    """
    子系统A
    """

    def method(self):
        """
        业务操作
        :return:
        """
        print("业务操作C ")


class SubSystemFour(object):
    """
    子系统A
    """

    def method(self):
        """
        业务操作
        :return:
        """
        print("业务操作D ")


class Client(object):
    """
    客户端
    """

    def method(self):
        """
        测试方法
        :return:
        """
        fac = Facade()
        fac.method_a()
        fac.method_b()


if __name__ == '__main__':
    cls = Client()
    cls.method()
