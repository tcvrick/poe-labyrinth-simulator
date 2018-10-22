import numpy as np

from Entities.Entity import Entity
from Tiles.TileRegistry import tile_registry
from Tiles.PathableTile import PathableTile
from Tiles.UnpathableTile import UnpathableTile
from Tiles.HazardousTile import HazardousTile


class PeriodicSpikeTrap(Entity):

    footprint_shape = (3, 3)
    interacts_with_world = True
    movement_speed = 0

    pathable_footprint = np.ones(footprint_shape, dtype=np.uint16) * tile_registry[PathableTile]
    unpathable_footprint = np.ones(footprint_shape, dtype=np.uint16) * tile_registry[UnpathableTile]
    hazardous_footprint = np.ones(footprint_shape, dtype=np.uint16) * tile_registry[HazardousTile]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.footprint = self.pathable_footprint
        self.period = 2

        offset = kwargs.get('offset')
        if offset and offset >= 0:
            self.internal_clock = offset % self.period
        elif offset and offset < 0:
            self.internal_clock = offset
        else:
            self.internal_clock = 0

    def tick(self):
        self.internal_clock = round(self.internal_clock + 1 / self.world_framerate, 3)

        if self.period <= self.internal_clock < self.period + 1:
            self.footprint = self.hazardous_footprint
        elif self.internal_clock >= self.period:
            self.internal_clock = 0
            self.footprint = self.pathable_footprint
        else:
            self.footprint = self.pathable_footprint
