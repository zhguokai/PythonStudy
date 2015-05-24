# -*- coding: utf-8 -*-
"""
  状态模式：当一个对象的内在状态改变时允许改变其行为，这个对象看起来像是改变了其类。
    状态模式主要解决的是当控制一个对象状态转换的条件表达式过于复杂时的情况。把状态的判断逻辑转移到表示不同状态的一系列类当
  中，可以把复杂的逻辑判断简化

  应用场景：
 
 Created by 相濡HH on 4/12/15.
"""


class Context(object):
    """
    维护一个State的实例，这个实例定义了当前的状态
    """

    def __init__(self, state):
        """
        初始化方法
        :param state:
        :return:
        """
        self.state = state
        print('当前状态是：%s' % state)

    def request(self):
        """
        执行完请求之后，设置当前状态
        :return:
        """
        print("处理当前请求")
        self.state.handle(self)


class State(object):
    """
    状态虚类
    """

    def handle(self, context):
        """
        设置当前状态
        :return:
        """
        context.state = self


class ConcreteAState(State):
    """
     具体状态A
    """

    def handle(self, context):
        """
        设置下一状态
        :param context:
        :return:
        """
        print("执行 %s 的方法" % self.__class__.__name__)
        context.state = ConcreteBState()


class ConcreteBState(State):
    """
    具体状态B
    """

    def handle(self, context):
        """
        设置下一状态
        :param context:
        :return:
        """
        print("执行 %s 的方法" % self.__class__.__name__)
        context.state = ConcreteAState()


if __name__ == '__main__':
    cls = Context(ConcreteAState())
    cls.request()
    cls.request()
    cls.request()
    cls.request()
