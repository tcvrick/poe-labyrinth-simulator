from abc import ABCMeta


class Tile(metaclass=ABCMeta):

    def __init__(self, *args, **kwargs):
        self.pathable = False


