# -*- coding: utf-8 -*-
"""
 装饰模式:
  动态的给一个对象增加一些额外的职责,就增加功能来说,装饰模式比子类更灵活
 
 Created by 相濡HH on 3/20/15.
"""


class Componet(object):
    """
    装饰对象接口
    """

    def operation(self):
        """
        操作接口
        :return:
        """


class ConcretorComponet(Componet):
    """
    实现装饰对象接口
    """

    def operation(self):
        """
        重写操作接口方法
        :return:
        """
        print("具体对象的操作:AAA")


class Decorator(Componet):
    """
    装饰抽象类,从外类扩展Component,
    但Component无需知道Decorator
    """

    def __init__(self):
        """
        定义变量
        :return:
        """
        # 受保护的变量
        self._componet = None

    def set_componet(self, component):
        """
        设置装饰部件
        :param component:
        :return:
        """
        self._componet = component

    def operation(self):
        """
        具体对象行为
        :return:
        """
        try:
            if self._componet is not None:
                self._componet.operation()
        except BaseException as e:
            print("%s" % e.args)


class ConcrectorADecrator(Decorator):
    """
    具体装饰子类A
    """

    def __init__(self):
        """
        初始化方法
        :return:
        """
        self._state = None

    def operation(self):
        """
        行为方法
        :return:
        """
        self._state = "New State"
        super(ConcrectorADecrator, self).operation()
        print("具体装饰对象A的操作")


class ConcrectorBDecrator(Decorator):
    """
    具体装饰子类
    """

    def __init__(self):
        """
        初始化方法
        :return:
        """
        self._state = None

    def operation(self):
        """
        行为方法
        :return:
        """
        self._state = "New State"
        super(ConcrectorBDecrator, self).operation()
        print("具体装饰对象B的操作")
        self.add_behavior()

    def add_behavior(self):
        """
        具体装饰对象B独有的方法
        :return:
        """
        print("执行动作:A")


class Client(object):
    """
    客户端对象
    """

    def test(self):
        """
        测试对象方法
        :return:
        """
        comp = ConcretorComponet()
        a1 = ConcrectorADecrator()
        a2 = ConcrectorBDecrator()

        a1.set_componet(comp)
        a2.set_componet(a1)
        a2.operation()


if __name__ == '__main__':
    cl = Client()
    cl.test()
