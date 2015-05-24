# -*- coding: utf-8 -*-
"""

 责任链模式:Chain of responsibility:使多个对象都有机会去处理请求,从而避免请求的发送者和接收者之间的耦合关系
          将这个对象连成一条链,并沿着这条链传递该请求,直到有一个对象处理它为止
 Created by 相濡HH on 4/2/15.
"""


class Handler(object):
    """
    定义一个请求接口
    """

    def __init__(self):
        self.successor = None

    def set_successor(self, handler):
        """
        设置处理该事务的子类
        :return:
        """
        self.successor = handler

    def handle_request(self, content):
        """
        处理请求
        :return:
        """


class ConcreteHandlerA(Handler):
    """
    目体处理者类
    """

    def handle_request(self, content):
        """
        具体处理内容
        :return:
        """
        if (content > 0) and (content < 10):
            print('A正在处理:%s' % content)
        elif self.successor is not None:
            self.successor.handle_request(content)


class ConcreteHandlerB(Handler):
    """
    目体处理者类
    """

    def handle_request(self, content):
        """
        具体处理内容
        :return:
        """
        if (content > 10) and (content < 20):
            print('B正在处理:%s' % content)
        elif self.successor is not None:
            self.successor.handle_request(content)


class ConcreteHandlerC(Handler):
    """
    目体处理者类
    """

    def handle_request(self, content):
        """
        具体处理内容
        :return:
        """
        if (content > 20) and (content < 30):
            print('C正在处理:%s' % content)
        elif self.successor is not None:
            self.successor.handle_request(self, content)


class ChianClient(object):
    @staticmethod
    def test():
        h1 = ConcreteHandlerA()

        h2 = ConcreteHandlerB()
        h3 = ConcreteHandlerC()

        # 组装责任链
        h1.set_successor(h2)
        h2.set_successor(h3)

        for i in range(1, 30, 4):
            h1.handle_request(i)
        print("测试完成:")


"""
加薪责任链申请
"""


class Manger(object):
    """
    管理者
    """

    def __init__(self, name):
        """
        初始化方法
        :return:
        """
        self.name = name
        self.superior = None

    def set_superior(self, superior):
        """
        设置上级
        :param superior:
        :return:
        """
        self.superior = superior

    def req_app(self, req):
        """
        请求
        :return:
        """


class JLManger(Manger):
    """
    经理
    """

    def __init__(self, name):
        Manger.__init__(self, name)

    def req_app(self, req):
        if req['type'] == '请假' and req['number'] < 2:
            print("%s经理批准了%s:请假 %s 天" % (self.name, req['name'], req['number']))
        elif self.superior is not None:
            self.superior.req_app(req)


class ZJManger(Manger):
    """
    经理
    """

    def __init__(self, name):
        Manger.__init__(self, name)

    def req_app(self, req):
        if req['type'] == '请假' and req['number'] <= 5:
            print("%s总监批准了%s:请假 %s 天" % (self.name, req['name'], req['number']))
        elif self.superior is not None:
            self.superior.req_app(req)


class LBManger(Manger):
    """
    经理
    """

    def __init__(self, name):
        Manger.__init__(self, name)

    def req_app(self, req):
        if req['type'] == '请假' and req['number'] <= 15:
            print("%s老板批准了%s:请假 %s 天" % (self.name, req['name'], req['number']))
        elif req['type'] == '加薪' and req['number'] <= 500:
            print("%s老板批准了:加薪 %s 元" % (self.name, req['number']))
        elif self.superior is not None:
            self.superior.req_app(req)
        else:
            print("%s老板无法处理%s提出%s%s请求" % (self.name, req['name'], req['type'], req['number']))


class MangerClient(object):
    @staticmethod
    def test():
        jl = JLManger('金')
        zj = ZJManger('王')
        lb = LBManger('张')

        # 请假
        req = {'type': '请假', 'number': 3, 'name': '张三'}
        jl.set_superior(zj)
        zj.set_superior(lb)
        jl.req_app(req)

        req = {'type': '请假', 'number': 8, 'name': '小菜'}
        jl.req_app(req)

        req = {'type': '加薪', 'number': 800, 'name': '小菜'}
        jl.req_app(req)

        req = {'type': '加薪', 'number': 300, 'name': '小菜'}
        jl.req_app(req)

        print('处理完成')


if __name__ == '__main__':
    MangerClient.test()
