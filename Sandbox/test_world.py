import time

from Game.GameState import GameState
from Worlds.TestWorld import TestWorld
from Worlds.World import Visualizer


def main():
    game_state = GameState(TestWorld)
    game_state.world.tick()
    visualizer = Visualizer(game_state.world, use_ai=True, depth=3)

    period = 1000 / game_state.world.framerate
    period = 100
    visualizer.visualize(period=period)


if __name__ == '__main__':
    main()
