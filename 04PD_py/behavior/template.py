# -*- coding: utf-8 -*-
"""

 模板方法：
    定义一个操作中算法骨架，而将一些步骤延迟到子类中。模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤

 模板方法特点：
    1、模板方法是通过把不变行为搬到超类，去除子类中重复代码来体现它的优势
    2、当不变的和可变的行为在方法的子类实现中混合在一起的时候，不变的行为就会在子类中重复出现，当使用模板方法模式把这些行为搬移到单一的地方，这样做帮助子类摆况脱重复的不变行为的纠缠。

 Created by 相濡HH on 4/10/15.
"""


class TemplateInterface(object):
    """
    模板方法，模板接口
    """

    def primitive_operation1(self):
        """
        私有操作1
        :return:
        """

    def primitive_opreation2(self):
        """
        私有操作2
        :return:
        """

    def template_method(self):
        """

        """
        self.primitive_operation1()
        self.primitive_opreation2()
        self.common_method()
        print("调用的子类方法么")

    def common_method(self):
        print("公共方法：ABC ")


class ConcreteImplA(TemplateInterface):
    """
    具体子类A
    """

    def primitive_operation1(self):
        """
        具体子类方法A的实现
        :return:
        """
        print("具体类A方法1的实现")

    def primitive_opreation2(self):
        """
        具体子类方法B的实现
        :return:
        """
        print("具体类A方法2的实现")


class ConcreteImplB(TemplateInterface):
    """
    具体子类B
    """

    def primitive_operation1(self):
        """
        具体子类方法A的实现
        :return:
        """
        print("具体类B方法1的实现")

    def primitive_opreation2(self):
        """
        具体子类方法B的实现
        :return:
        """
        print("具体类B方法2的实现")


if __name__ == '__main__':
    c = ConcreteImplA()
    c.template_method()

    c = ConcreteImplB()
    c.template_method()
