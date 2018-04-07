import time

from Game.GameState import GameState
from Worlds.TestWorld import TestWorld
from Optimizers.tree_maximizer import TreeMaximizer


def main():
    game_state = GameState(TestWorld)
    with Timer() as t:
        tree_maximizer = TreeMaximizer(4)
        result = tree_maximizer.maximize(game_state)
    result = tree_maximizer.convert_to_action_list(result)
    for res in result:
        print(res)
    # print(result.children)
    # print(result.children[1].children)
    # result = max(result, key=lambda x: x[-1][-1])
    # print(result)
    # for arr in result[0][0]:
    #     print(arr)


class Timer:

    def __init__(self, title=None):
        self.time_start = time.time()
        self.title = title

    def __enter__(self):
        if self.title:
            print(self.title)
        yield

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Time Elapsed: [{}]".format(time.time() - self.time_start))


if __name__ == '__main__':
    main()
