# -*- coding: utf-8 -*-
"""
 公司层级间的组合模式应用
 
 Created by 相濡HH on 3/19/15.
"""


class Company(object):
    """
    公司接口
    """

    def __init__(self, name):
        """
        初始化方法
        :param name:
        :return:
        """
        self._name = name

    def add(self, company):
        """
        增加公司接口
        :param company:
        :return:
        """

    def remvoe(self, company):
        """
        删除公司接口
        :param company:
        :return:
        """

    def display(self, depth):
        """
        显示层级关系
        :param depth:
        :return:
        """

    def run_resp(self):
        """
        履行职责接口
        :return:
        """


class ConcreteCompany(Company):
    """
    公司具体实现类
    """

    def __init__(self, name):
        """
        初始化方法
        :param name:
        :return:
        """
        Company.__init__(self, name)
        self.compay_list = []

    def add(self, company):
        """
        增加公司接口
        :param company:
        :return:
        """
        self.compay_list.append(company)

    def remvoe(self, company):
        """
        删除公司接口
        :param company:
        :return:
        """
        self.compay_list.remove(company)

    def display(self, depth):
        """
        显示层级关系
        :param depth:
        :return:
        """
        print("-" * depth + self._name)
        for com in self.compay_list:
            com.display(depth + 2)


    def run_resp(self):
        """
        履行职责接口
        :return:
        """
        print("执行任务")
        for com in self.compay_list:
            com.run_resp()


class HRCompany(Company):
    """
    人力资源子类
    """

    def __init__(self, name):
        """
        初始化方法
        :param name:
        :return:
        """
        Company.__init__(self, name)


    def add(self, company):
        """
        增加公司接口
        :param company:
        :return:
        """

    def remvoe(self, company):
        """
        删除公司接口
        :param company:
        :return:
        """

    def display(self, depth):
        """
        显示层级关系
        :param depth:
        :return:
        """
        print("-" * depth + self._name)

    def run_resp(self):
        """
        履行职责接口
        :return:
        """
        print("%s: 员工招聘培训管理" % self._name)


class FianceCompany(Company):
    """
    财务子类
    """

    def __init__(self, name):
        """
        初始化方法
        :param name:
        :return:
        """
        Company.__init__(self, name)


    def add(self, company):
        """
        增加公司接口
        :param company:
        :return:
        """

    def remvoe(self, company):
        """
        删除公司接口
        :param company:
        :return:
        """

    def display(self, depth):
        """
        显示层级关系
        :param depth:
        :return:
        """
        print("-" * depth + self._name)

    def run_resp(self):
        """
        履行职责接口
        :return:
        """
        print("%s: 公司财务结算" % self._name)


class Client(object):
    """
        客户端
    """

    def test(self):
        root = ConcreteCompany("北京总公司")
        root.add(HRCompany("总公司人力资源部"))
        root.add(FianceCompany("总公司财务部"))

        comp_a = ConcreteCompany("华东分公司")
        comp_a.add(HRCompany("华东公司人力资源部"))
        comp_a.add(FianceCompany("华东公司财务部"))
        root.add(comp_a)

        comp_a = ConcreteCompany("南京分公司")
        comp_a.add(HRCompany("南京公司人力资源部"))
        comp_a.add(FianceCompany("南京公司财务部"))
        root.add(comp_a)

        root.display(1)
        root.run_resp()


if __name__ == '__main__':
    cls = Client()
    cls.test()
