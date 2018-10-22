import numpy as np

from Worlds.World import World
from Tiles.TileRegistry import tile_registry
from Tiles.PathableTile import PathableTile
from Tiles.UnpathableTile import UnpathableTile
from Entities.Traps.PeriodicSpikeTrap import PeriodicSpikeTrap
from Entities.Agent.Player import Player


class TestWorld(World):

    display_name = 'Test World'
    framerate = 5
    target_position = (13, 0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Grid
        pathable_tile_id = tile_registry[PathableTile]
        self.grid = np.ones((14, 25), dtype=np.uint8) * pathable_tile_id

        # Player
        player = Player(position=(0, 0), world=self)
        self.agent = player
        self.entities.append(player)

        # ==================================
        # First Gauntlet
        # ==================================
        # First row of traps.
        for i in range(7):
            offset = 1 if i % 2 == 0 else 2
            self.entities.append(PeriodicSpikeTrap(position=(1, 4+i*3), offset=offset, world=self))

        # Second row impassable.
        self.grid[3:8, :-1] = tile_registry[UnpathableTile]
        self.grid[3:5, :-1:3] = 1

        # ==================================
        # Second Gauntlet
        # ==================================
        # First row of traps.
        for i in range(7):
            for j in range(2):
                offset = 1 if i % 2 == 0 else 2
                self.entities.append(PeriodicSpikeTrap(position=(9 + j*3, 4 + i * 3), offset=offset + j, world=self))
