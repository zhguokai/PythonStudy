# -*- coding: utf-8 -*-
"""
 命令模式,将一个请求封装为一个对象,从而使你可用的不同请求对客户时行参数化;对请求排队或记录请求日志,以及支持可撤销的操作.
 命令模式优势:
    1、较容易的设计一个命令队列
    2、在需要的情况下，可以容易的将命令记入日志
    3、允许接收请求的一方决定是否要否决请求
    4、可以容易的实现对请求的撤销和重做
    5、由于新加进的具体命令类不影响其他的类，因此增加新类很容易
    6、命令模式把请求一个操作的对象与知道怎么执行一个操作的对象分开

 Created by 相濡HH on 4/7/15.
"""


class Command(object):
    """
    命令接口,用于声明操作的接口
    """

    def __init__(self, receiver):
        """
        初始化方法
        :return:
        """
        self._receiver = receiver

    def execute(self):
        """
        执行操作
        :return:
        """


class ConcreteCommand(Command):
    """
    命令的具体实现类
    """

    def __init__(self, receiver):
        """
        初始化
        :param receiver:
        :return:
        """
        Command.__init__(self, receiver)

    def execute(self):
        """
        调用接收者执行操作
        :return:
        """
        self._receiver.action()


class Receiver(object):
    """
    具体命令的执行者
    """

    def action(self):
        """
        任务执行方法
        :return:
        """
        print("请求执行!")


class Invoker(object):
    """
    要求命令执行请求
    """

    def __init__(self, command):
        """
        初始化,增加Command
        :return:
        """
        self._command = command

    def execute_command(self):
        """
        执行命令
        :return:
        """
        self._command.execute()


class Client(object):
    """
    客户端调用方式
    """

    @staticmethod
    def test():
        """

        :return:
        """

    receiver = Receiver()
    command = ConcreteCommand(receiver)
    invoker = Invoker(command)
    invoker.execute_command()

if __name__ == '__main__':
    Client.test()
