from abc import ABCMeta, abstractmethod


class Action(metaclass=ABCMeta):

    def __init__(self, *args, **kwargs):
        pass

    def __str__(self):
        return str(self.__class__.__name__)

    __repr__ = __str__
