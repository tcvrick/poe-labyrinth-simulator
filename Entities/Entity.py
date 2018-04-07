import math

from abc import ABCMeta, abstractmethod
from enum import Enum

from Actions.IdleAction import IdleAction


class Entity(metaclass=ABCMeta):

    def __init__(self, *args, **kwargs):
        self.footprint = None
        self.position = kwargs['position']
        self.world = kwargs['world']
        self.world_framerate = self.world.framerate

        self.current_action = IdleAction()

        # Movement Related
        self.movement_speed = 0
        self.movement_direction = None
        self.movement_accumlated_distance = 0
        self.movement_step_size = 1

    @property
    def footprint_shape(self):
        return None

    @property
    def interacts_with_world(self):
        return False

    @abstractmethod
    def tick(self):
        pass

    def get_int_position(self):
        return int(self.position[0]), int(self.position[1])
