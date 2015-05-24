# -*- coding: utf-8 -*-
"""

 组合模式:
   将对象组合成树型结构以表示'部分-整体'的层次结构.组合模式使得用户对单个对象和组合对象的使用具有一致性

 Created by 相濡HH on 3/19/15.
"""


class Component(object):
    """
    对象声明结口,在适当的情况下实现所有类共有接口的默认行为
    声明一个接口用于管理与访问Component子部件
    """
    # 此处定义的为全局静态变量
    def __init__(self, name):
        """
        初始化方法
        :return:
        """
        self.name = name
        # 存放子部件


    def add(self, component):
        """
        增加部件
        :param component:
        :return:
        """

    def remove(self, component):
        """
        删除子部件
        :param component:
        :return:
        """

    def display(self, depth):
        """
        展示信息
        :return:
        """


class Leaf(Component):
    """
    叶子结点
    """

    def __init__(self, name):
        """
        初始化方法
        :param name:
        :return:
        """
        Component.__init__(self, name)
        self.name = name

    def display(self, depth):
        """
        展示方法
        :return:
        """
        print("-" * depth + self.name)


class Composite(Component):
    """
    定义有枝节点行为:
    用于存储子部件
    """

    def __init__(self, name):
        Component.__init__(self, name)
        self.comp = []

    def add(self, component):
        """
        增加部件
        :param component:
        :return:
        """
        self.comp.append(component)

    def remove(self, component):
        """
        删除子部件
        :param component:
        :return:
        """
        self.comp.remove(component)

    def display(self, depth):
        """
        展示信息
        :return:
        """
        print("-" * depth + self.name)
        for com in self.comp:
            com.display(depth + 2)


class Client(object):
    """
    客户端调用
    """

    def call_method(self):
        """
        调用方法
        :return:
        """
        root = Composite("root")
        root.add(Leaf('LeafA'))
        root.add(Leaf('LeafB'))

        comp = Composite('Composite X')
        comp.add(Leaf('Leaf XA'))
        comp.add(Leaf('Leaf XB'))
        root.add(comp)

        comp2 = Composite('Composite Y')
        comp2.add(Leaf('Leaf YA'))
        comp2.add(Leaf('Leaf YB'))
        root.add(comp2)

        root.add(Leaf("Leaf C"))

        leafd = Leaf("Leaf D")
        root.add(leafd)
        root.remove(leafd)

        root.display(1)


