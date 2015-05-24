# -*- coding: utf-8 -*-
"""
 桥接模式适应场景:
 1 不希望在抽象和它的实现部分之间有一个固定的绑定
 2 类的抽象以及它的实现部分都应该可以通过生成子类的方法加以扩充
 3 对一个抽象的实现部分的修改对应的客户不产生影响,即客户的代码不必重新编译

 Created by 相濡HH on 3/18/15.
"""


class Abstraction(object):
    """
    抽象结口
    """

    def __init__(self, impl):
        """
        参数具体实例
        :param impl:
        :return:
        """
        self.impl = impl

    def operation(self):
        """
        操作方法
        :return:
        """
        self.imp.operation()


class RefinedAbstraction(Abstraction):
    """
    实现接口
    """

    def operation(self):
        """
        操作应该
        :return:
        """
        self.impl.operation()


class ImPlementor(object):
    """
    实现接口
    """

    def operation(self):
        """
        接口
        :return:
        """
        print("AAAAA:ABSTRACt")


class ConcreteImplementorA(ImPlementor):
    """
    实现接口
    """

    def operation(self):
        """

        :return:
        """
        print("实际子类:A")
        super(ConcreteImplementorA, self).operation()


class ConcrteImplementorB(ImPlementor):
    """

    """

    def operation(self):
        """

        :return:
        """
        super(ConcrteImplementorB, self).operation()
        print("实际子类B")


class Client(object):
    """
    客户端
    """

    def test(self):
        """

        :return:
        """
        impl = ConcreteImplementorA()
        abstract = RefinedAbstraction(impl)
        abstract.operation()

        impl = ConcrteImplementorB()
        abstract = RefinedAbstraction(impl)
        abstract.operation()


if __name__ == '__main__':
    client = Client()
    client.test()
