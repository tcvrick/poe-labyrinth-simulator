import math
import numpy as np
import matplotlib
import matplotlib.animation

from abc import ABCMeta
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib import pyplot as plt

from Actions.IdleAction import IdleAction
from Actions.MovingAction import MovingAction, MovementDirection, PrecomputedMovementFactors
from Optimizers.tree_maximizer import TreeMaximizer
from Tiles.TileRegistry import tile_registry
from Tiles.UnpathableTile import UnpathableTile


class World(metaclass=ABCMeta):

    def __init__(self, *args, **kwargs):
        self.grid = None
        self.entities = []
        self.world_time = 0
        self.plot_image = None
        self.agent = None
        self.game_state = kwargs['game_state']

    @property
    def framerate(self):
        return 0

    def tick(self):
        # print(self.agent.evaluate())

        for entity in self.entities:
            entity.tick()
            if entity.interacts_with_world:
                self.update_world_interaction(entity)
            if isinstance(entity.current_action, MovingAction):
                self.update_entity_position(entity)

    def update_world_interaction(self, entity):
        # Update footprint interaction.
        y, x = entity.position
        y, x = int(y), int(x)

        height, width = int((entity.footprint.shape[0] - 1) / 2), int((entity.footprint.shape[1] - 1) / 2)
        self.grid[(y - height):(y + height + 1), (x - width): (x + width + 1)] = entity.footprint

    def update_entity_position(self, entity):
        assert isinstance(entity.current_action, MovingAction)
        direction = entity.current_action.direction

        if direction is MovementDirection.E:
            dy, dx = PrecomputedMovementFactors.y_E, PrecomputedMovementFactors.x_E
        elif direction is MovementDirection.N:
            dy, dx = PrecomputedMovementFactors.y_N, PrecomputedMovementFactors.x_N
        elif direction is MovementDirection.W:
            dy, dx = PrecomputedMovementFactors.y_W, PrecomputedMovementFactors.x_W
        elif direction is MovementDirection.S:
            dy, dx = PrecomputedMovementFactors.y_S, PrecomputedMovementFactors.x_S
        elif direction is MovementDirection.NE:
            dy, dx = PrecomputedMovementFactors.y_NE, PrecomputedMovementFactors.x_NE
        elif direction is MovementDirection.NW:
            dy, dx = PrecomputedMovementFactors.y_NW, PrecomputedMovementFactors.x_NW
        elif direction is MovementDirection.SW:
            dy, dx = PrecomputedMovementFactors.y_SW, PrecomputedMovementFactors.x_SW
        elif direction is MovementDirection.SE:
            dy, dx = PrecomputedMovementFactors.y_SE, PrecomputedMovementFactors.x_SE
        else:
            raise ValueError

        # Calculate new position.
        dy = dy * entity.movement_speed / self.framerate
        dx = dx * entity.movement_speed / self.framerate
        y, x = entity.position[0] + dy, entity.position[1] + dx

        # Keep within bounds.
        within_bounds = True
        if y + 1 > self.grid.shape[0]:
            y = self.grid.shape[0] - 1
            within_bounds = False
        elif y < 0:
            y = 0
            within_bounds = False
        if x + 1 > self.grid.shape[1]:
            x = self.grid.shape[1] - 1
            within_bounds = False
        elif x < 0:
            x = 0
            within_bounds = False

        # Keep out of unpathable tiles. No support for diagonal movements.
        if within_bounds and self.grid[int(y), int(x)] == tile_registry[UnpathableTile]:
                y, x = entity.position

        # Update entity position.
        entity.position = (y, x)
        entity.movement_accumlated_distance += abs(dy) + abs(dx)

        # Finish action after moving 1 unit of distance.
        if round(entity.movement_accumlated_distance, 3) >= 1:
            entity.movement_accumlated_distance = 0
            entity.current_action = IdleAction()
            entity.movement_direction = MovementDirection.Null


class Visualizer:

    def __init__(self, world, use_ai, depth):
        self.world = world
        self.use_ai = use_ai
        self.depth = depth

    def visualize(self, period):
        fig = plt.figure()

        cmap = ListedColormap(['black', 'white', 'red', 'green', 'orange'])
        bounds = [0, 1, 2, 3, 4, 5]
        norm = BoundaryNorm(bounds, cmap.N)
        self.plot_image = plt.imshow(self.world.grid, interpolation='nearest',
                                     cmap=cmap, norm=norm, origin='lower')

        ani = matplotlib.animation.FuncAnimation(fig, self.animation_update, interval=period)
        plt.show()

    def animation_update(self, i):
        # print("My current action is: " + str(self.world.agent.current_action))
        if self.use_ai and isinstance(self.world.agent.current_action, IdleAction):
            tree_maximizer = TreeMaximizer(self.depth)
            best_action = tree_maximizer.get_best_action(self.world.game_state)
            # print("The best action is:" + str(best_action))
            self.world.agent.current_action = best_action
        self.world.tick()

        # Player Co-ordinates
        y, x = self.world.agent.position
        y, x = int(y), int(x)
        agent_pos = (y, x)

        # Visualize Player
        agent_pos_value = self.world.grid[agent_pos]
        self.world.grid[agent_pos] = 3

        # Visualize Player Path
        path = self.world.agent.get_path()
        tmp_values = []
        for pos in path:
            tmp_values.append(self.world.grid[pos])
            self.world.grid[pos] = 4

        # Draw grid
        self.plot_image.set_data(self.world.grid)

        # Restore grid to normal properties.
        for i, pos in enumerate(path):
            self.world.grid[pos] = tmp_values[i]
        self.world.grid[agent_pos] = agent_pos_value
        return self.plot_image
