# -*- coding: utf-8 -*-
"""

 中介者模式：
    用一个中介者对象来封装一系列对象的交互。中介者使对象不需要显式的相互引用，从而使其耦合松散，而且可以独立地
    改变它们之间的交互
 Created by 相濡HH on 4/14/15.
"""


class Mediator(object):
    """
    抽象中介者，定义了同事对象到中介者对象的接口
    """

    def send(self, msg, colleague):
        pass


class Colleague(object):
    """
    抽象同事类
    """

    def __init__(self, mediator):
        """
        初始化中介者对象
        :param media:
        :return:
        """
        self.media = mediator


class ConcreteMediator(Mediator):
    """
    具体中介者类
    """

    def __init__(self):
        """
        初始化抽象同事
        :return:
        """
        self.collA = None
        self.collB = None

    def send(self, msg, colleague):
        """
        发送消息
        :param msg:
        :param colleague:
        :return:
        """
        if colleague is not None and colleague == self.collA:
            """
            当传入同事A 时，通知同事B
            否则通知同事A
            """
            self.collB.notify(msg)
        else:
            self.collA.notify(msg)


class ConcretrColleagueA(Colleague):
    """
    具体抽象同事类
    """

    def __init__(self, mediator):
        Colleague.__init__(self, mediator)

    def send_msg(self, msg):
        self.media.send(msg, self)

    def notify(self, msg):
        print("同事A 得到消息：%s" % msg)


class ConcretrColleagueB(Colleague):
    """
    具体抽象同事类
    """

    def __init__(self, mediator):
        Colleague.__init__(self, mediator)

    def send_msg(self, msg):
        self.media.send(msg, self)

    def notify(self, msg):
        print("同事B 得到消息：%s" % msg)


if __name__ == '__main__':
    media = ConcreteMediator()
    c1 = ConcretrColleagueA(media)
    c2 = ConcretrColleagueB(media)
    media.collA = c1
    media.collB = c2
    c1.send_msg('吃过饭了么')
    c2.send_msg('没有呢，你打算请客？')
