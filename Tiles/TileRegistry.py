from Tiles.UnpathableTile import UnpathableTile
from Tiles.PathableTile import PathableTile
from Tiles.HazardousTile import HazardousTile

tile_registry = {UnpathableTile: 0,
                 PathableTile: 1,
                 HazardousTile: 2}

# Make the registry a one-to-one, bi-directional dictionary
d = {}
for k, v in tile_registry.items():
    assert tile_registry.get(v) is None
    d[v] = k
tile_registry.update(d)
