import math

from enum import Enum
from Actions.Action import Action


class MovingAction(Action):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.direction = kwargs['direction']

    def __str__(self):
        return str(self.direction)

    __repr__ = __str__


class MovementDirection(Enum):
    Null = -1
    E = 0
    NE = 45
    N = 90
    NW = 135
    W = 180
    SW = 225
    S = 270
    SE = 315


class PrecomputedMovementFactors:
    y_E, x_E = math.sin(math.radians(MovementDirection.E.value)), math.cos(math.radians(MovementDirection.E.value))
    y_N, x_N = math.sin(math.radians(MovementDirection.N.value)), math.cos(math.radians(MovementDirection.N.value))
    y_W, x_W = math.sin(math.radians(MovementDirection.W.value)), math.cos(math.radians(MovementDirection.W.value))
    y_S, x_S = math.sin(math.radians(MovementDirection.S.value)), math.cos(math.radians(MovementDirection.S.value))
    y_NE, x_NE = math.sin(math.radians(MovementDirection.NE.value)), math.cos(math.radians(MovementDirection.NE.value))
    y_NW, x_NW = math.sin(math.radians(MovementDirection.NW.value)), math.cos(math.radians(MovementDirection.NW.value))
    y_SW, x_SW = math.sin(math.radians(MovementDirection.SW.value)), math.cos(math.radians(MovementDirection.SW.value))
    y_SE, x_SE = math.sin(math.radians(MovementDirection.SE.value)), math.cos(math.radians(MovementDirection.SE.value))


directions = [MovementDirection.E, MovementDirection.N, MovementDirection.W, MovementDirection.S,
              MovementDirection.NE, MovementDirection.NW, MovementDirection.SW, MovementDirection.SE][:4]

movement_factors = [(PrecomputedMovementFactors.y_E, PrecomputedMovementFactors.x_E),
                    (PrecomputedMovementFactors.y_N, PrecomputedMovementFactors.x_N),
                    (PrecomputedMovementFactors.y_W, PrecomputedMovementFactors.x_W),
                    (PrecomputedMovementFactors.y_S, PrecomputedMovementFactors.x_S),
                    (PrecomputedMovementFactors.y_NE, PrecomputedMovementFactors.x_NE),
                    (PrecomputedMovementFactors.y_NW, PrecomputedMovementFactors.x_NW),
                    (PrecomputedMovementFactors.y_SW, PrecomputedMovementFactors.x_SW),
                    (PrecomputedMovementFactors.y_SE, PrecomputedMovementFactors.x_SE)][:4]

directions_and_movefactors = list(zip(directions, movement_factors))
