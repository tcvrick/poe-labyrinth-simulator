import numpy as np
import copy

from Entities.Agent.Player import Player
from Actions.IdleAction import IdleAction
from Actions.MovingAction import MovingAction, MovementDirection, PrecomputedMovementFactors, directions_and_movefactors


class GameState:

    def __init__(self, world_type):
        self.world = world_type(game_state=self)

    def get_next_state(self, action, fast_forward_ticks=5):
        next_state = copy.deepcopy(self)
        next_state.world.agent.current_action = action
        for i in range(fast_forward_ticks):
            next_state.world.tick()
        return next_state

    def get_legal_actions(self):
        agent = self.world.agent
        legal_actions = []

        if isinstance(agent, Player):
            legal_actions.append(IdleAction())

            if isinstance(agent.current_action, IdleAction):
                # Check movement possibilities.
                valid_tiles = self.world.grid
                max_y, max_x = self.world.grid.shape
                max_y, max_x = max_y - 1, max_x - 1
                y, x = agent.position
                movespeed_factor = agent.movement_speed / self.world.framerate

                for direction, (dy, dx) in directions_and_movefactors:
                    int_y, int_x = y + dy*movespeed_factor, x + dx*movespeed_factor
                    if int_y < 0 or int_x < 0:
                        pass
                    elif int_y > max_y or int_x > max_x:
                        pass
                    else:
                        int_y, int_x = int(int_y), int(int_x)
                        if valid_tiles[int_y, int_x] != 0:
                            legal_actions.append(MovingAction(direction=direction))
        return legal_actions
