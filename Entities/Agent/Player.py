from Entities.Entity import Entity
from Actions.MovingAction import MovingAction, MovementDirection
from Actions.IdleAction import IdleAction
from ExternalTools.a_star import astar
from Tiles.TileRegistry import tile_registry
from Tiles.HazardousTile import HazardousTile


class Player(Entity):

    footprint_shape = (1, 1)
    interacts_with_world = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.movement_speed = 5
        self.target_position = self.world.target_position

    def tick(self):
        pass

    def get_path(self):
        return astar(self.world.grid, (self.get_int_position()), self.target_position)

    def evaluate(self):
        score = 0
        path = self.get_path()
        if path:
            score -= len(path)
        else:
            score -= 1e6
        if self.world.grid[self.get_int_position()] == tile_registry[HazardousTile]:
            score -= 2e6

        return score

    def check_if_dead(self):
        if self.world.grid[self.get_int_position()] == tile_registry[HazardousTile]:
            return True
        else:
            return False


