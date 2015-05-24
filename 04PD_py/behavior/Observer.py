# -*- coding: utf-8 -*-
"""

 观察者模式：定义了一种一对多的依赖关系，让多个观察者对象同时监听某一个主题对象。这个主题对象在状态发生变化时，会通知所有
 观察者对象，使它们能够自动更新自己

 使用时机：
    当一个对象的改变需要同时改变其他对象的时候
    观察者模式的作用就是解除耦合，让耦合的双方都依赖于抽象，而不依赖于具体，从而使得各自的变化都不会影响另一边的变化

 Created by 相濡HH on 4/10/15.
"""


class Observer(object):
    """
    定义观察者
    """

    def update(self, msg):
        """
        更新自己
        :return:
        """
        print("更新自己：%s" % self.__class__)


class ConcreteObserverA(Observer):
    """
    具体观察者A
    """

    def update(self, msg):
        """
        具体实现
        """
        super(ConcreteObserverA, self).update(msg)
        print("更新观察者A ：%s" % self.__class__)


class ConcreteObserverB(Observer):
    """
    具体观察者A
    """

    def update(self, msg):
        """
        具体实现
        """
        super(ConcreteObserverB, self).update(msg)
        print("更新观察者A ：%s" % msg)


class ConcreteObserverC(Observer):
    """
    具体观察者A
    """

    def update(self, msg):
        """
        具体实现
        """
        super(ConcreteObserverC, self).update(msg)
        print("更新观察者C ：%s" % msg)


class Subject(object):
    """
    主题
    """

    def __init__(self):
        self._obs = []
        self._msg = None

    def add_obs(self, obs):
        self._obs.append(obs)

    def remove_obs(self, obs):
        if len(self._obs) > 0:
            self._obs.remove(obs)

    def notify(self):
        """
        通知所有子类
        """
        for obs in self._obs:
            obs.update(self._msg)


class ConcreSubject(Subject):
    """
    具体实现类
    """

    def set_msg(self, msg):
        """

        :return:
        """

        self._msg = msg + "发奖金了。。。"


if __name__ == "__main__":
    cs = ConcreSubject()
    cs.set_msg("张总")
    cs.add_obs(ConcreteObserverA())
    cs.add_obs(ConcreteObserverB())
    cs.add_obs(ConcreteObserverC())
    cins = ConcreteObserverC()
    cs.add_obs(cins)
    cs.notify()
    cs.set_msg('李总')
    cs.remove_obs(cins)
    cs.notify()
