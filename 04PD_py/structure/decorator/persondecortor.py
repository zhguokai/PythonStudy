# -*- coding: utf-8 -*-
"""

 人物服装版装饰版装饰模式
 Created by 相濡HH on 3/20/15.
"""


class Person(object):
    """
    人物接口
    """

    def __init__(self, name):
        """
        初始化姓名
        :param name:
        :return:
        """
        self._name = name

    def display(self):
        """
        展示人物形象接口
        :return:
        """
        print(" 装扮的 %s" % self._name)


class Finery(Person):
    """
    服饰接口
    """

    def __init__(self):
        """
        初始化方法
        :return:
        """
        self._person = None

    def decorator(self, person):
        """
        装扮人
        :param person:
        :return:
        """
        self._person = person

    def display(self):
        """
        形象展示
        :return:
        """
        if self._person is not None:
            self._person.display()
            # print("准备装饰的服装:")


class Tshirt(Finery):
    """
    T恤具体服装类
    """

    def display(self):
        """
        展示服装
        :return:
        """
        super(Tshirt, self).display()
        print("大T恤")


class BigTrouser(Finery):
    """
    T恤具体服装类
    """

    def display(self):
        """
        展示服装
        :return:
        """
        super(BigTrouser, self).display()
        print("大马裤")


class LeatherShoes(Finery):
    """
    T恤具体服装类
    """

    def display(self):
        """
        展示服装
        :return:
        """
        super(LeatherShoes, self).display()
        print("皮鞋")


class Client(object):
    """
    客户端测试类
    """

    def test(self):
        """
        测试方法
        :return:
        """
        # 人
        per = Person("小菜")
        #
        print("第一种装扮:")
        #
        ts = Tshirt()
        kk = BigTrouser()

        ts.decorator(per)
        kk.decorator(ts)
        kk.display()

        print("第二种装扮")

        px = LeatherShoes()
        px.decorator(kk)
        px.display()


if __name__ == '__main__':
    cl = Client()
    cl.test()
