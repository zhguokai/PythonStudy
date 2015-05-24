# -*- coding: utf-8 -*-
"""
  享元模式,运用共享技术有效地支持大量细粒度对象
 使用场景:
    如果一个应用程序使用了大量的对象,而大量的的这些对象造成了很大的内存开销时,就应该考虑使用
    对象的大多数状态可以外部状态,如果删除了对象的外部状态,那么可以用相对较少的共享对象取代多组对象,可以考虑使用
 Created by 相濡HH on 3/30/15.
"""


class FlyweightFactory(object):
    """
    享元模式工厂
    """

    def __init__(self):
        """
        初始化
        :return:
        """
        self.flyweight = dict({})
        self.flyweight['X'] = ConcreteFlyweight()
        self.flyweight['Y'] = ConcreteFlyweight()
        self.flyweight['Z'] = ConcreteFlyweight()

    def get_flyweight(self, key):
        """
        获取享元实例,通过Key值
        :param key:
        :return:
        """
        return self.flyweight.get(key)


class Flyweight(object):
    """
    享元接口,所有具体享元类的超类或接口,通过这个接口享元类可以接受并作用于外部状态
    """

    def operation(self, extrinsicstate):
        """
        外部状态
        :param extrinsicstate:
        :return:
        """
        pass


class ConcreteFlyweight(Flyweight):
    """
    享元类的实例类,并为内部状态增加存储空间
    """

    def operation(self, extrinsicstate):
        """
        为内部状态增加存储空间
        :param extrinsicstate:
        :return:
        """
        print("具体的Flyweight:%s" % extrinsicstate)


class UnSharaeConcreteFlyweight(Flyweight):
    """
        无需共享的实现类
    """

    def operation(self, extrinsicstate):
        """
        那些不需要共享的Flyweight子类,因为Flyweight接口共享成为可能,但并不强制共享
        :param extrinsicstate:

        :return:
        """
        print("不需要共享的具体的Flyweight:%s" % extrinsicstate)


class Client(object):
    """
    客户端
    """

    def test(self):
        """
        测试
        :return:
        """
        extrinsicstate = 22

        fly = FlyweightFactory()

        fx = fly.get_flyweight('X')
        fx.operation(extrinsicstate - 1)

        fy = fly.get_flyweight('Y')
        fy.operation(extrinsicstate - 2)

        fz = fly.get_flyweight('Z')
        fz.operation(extrinsicstate - 3)

        uf = UnSharaeConcreteFlyweight()
        uf.operation(extrinsicstate)


if __name__ == '__main__':
    cls = Client()
    cls.test()
