from Game.GameState import GameState
from Worlds.TestWorld import TestWorld
from Worlds.World import Visualizer


def main():
    game_state = GameState(TestWorld)
    game_state.world.tick()
    visualizer = Visualizer(game_state.world, use_ai=True, depth=3, save_frames=True)

    frame_rate = 10
    period = 1000 / frame_rate
    visualizer.visualize(period=period)


if __name__ == '__main__':
    main()
