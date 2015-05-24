# -*- coding: utf-8 -*-
"""
  代理模式(Proxy),为其他对象提供一种代理以控制这个对象的访问
  模式方式:
      第一:远程代理,也就是为一个对象在不同的地址空间提供局部代表,这样可以隐藏一个对象存在于不同地址空间的事实
      第二:虚拟代理,是根据需要创建开销很大的对象,通过它来存放实例化需要很长时间的真实对象
      第三:安全代理,用来控制真实对象访问时的权限.
      第四:智能指引,是指当调用真实的对象时,代理处理另外一些事.
 Created by 相濡HH on 4/1/15.d
"""


class Subject(object):
    """
    定义了RealSubject 和 Proxy 的共用接口,这样就在任务RealSubject的地方都可以使用Proxy
    """

    def request(self):
        """
        请求
        :return:
        """


class RealSubject(object):
    """
    真实的请求类
    """

    def request(self):
        """

        :return:
        """
        print("真实的请求:")


class Proxy(Subject):
    """
     代理类
    """

    def __init__(self):
        self.__real = RealSubject()

    def request(self):
        """
        请求实际
        :return:
        """
        if self.__real is None:
            self.__real = RealSubject()
        self.__real.request()


class Client(object):
    """
    客户端
    """

    def test(self):
        proxy = Proxy()
        proxy.request()


if __name__ == '__main__':
    cls = Client()
    cls.test()
