# -*- coding: utf-8 -*-
"""

 备忘录模式：
     在不破坏封装的前提下，捕获一个对象的内部状态，并在该对象之外的保存这个状态。这样以后就可以恢复到原先的状态
 Created by 相濡HH on 4/14/15.
"""


class Memento(object):
    """
    备记录 用于存储状态信息
    """

    def __init__(self, states):
        if isinstance(states, dict):
            self.state = states
        else:
            print('参数类型不对')


class Creataker(object):
    """
    备忘录的管理者
    """

    def __init__(self):
        """

        :return:
        """
        self._memento = None

    def set_state(self, memento):
        """
        设置状态
        :param memento:
        :return:
        """
        self._memento = memento

    def get_state(self):
        """
        返回状态
        :return:
        """
        if self._memento is not None:
            return self._memento
        else:
            return None


class Originator(object):
    """
    负责创建一个备忘录Memento，并记录当时的内部状态
    并可恢复状态
    """

    def __init__(self):
        """
        设置信息
        :return:
        """
        self.age = None
        self.text = None
        self.msg = None

    def create_memento(self):
        """
        创建备忘录
        :return:
        """
        state = {
            'age': self.age,
            'text': self.text,
            'msg': self.msg
        }
        memento = Memento(state)
        return memento

    def recovery_memento(self, memento):
        """
        创建备忘录
        :return:
        """
        state = memento.state

        self.age = state['age']
        self.text = state['text']
        self.msg = state['msg']

    def show_state(self):
        print("{'age':%s,'text': %s,'msg': %s}" % (self.age, self.text, self.msg))

    def set_state(self, age, text, msg):
        self.age = age
        self.text = text
        self.msg = msg


if __name__ == '__main__':
    # 备忘录模式
    orig = Originator()
    orig.set_state('32', '44', '66')
    cre = Creataker()
    cre.set_state(orig.create_memento())
    orig.show_state()
    orig.set_state('132', '144', '166')
    orig.show_state()
    orig.recovery_memento(cre.get_state())
    orig.show_state()
