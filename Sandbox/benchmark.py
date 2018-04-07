import time

from Game.GameState import GameState
from Worlds.TestWorld import TestWorld
from multiprocessing import Pool


n_states = 1000


def main():
    # with Timer() as t:
    #     with Pool(processes=5) as p:
    #         print(p.map(test, [1, 2, 3, 4, 5]))

    with Timer() as t:
        test2()


def test(x):
    for i in range(n_states):
        g = GameState(TestWorld)
        g.world.tick()
    return x


def test2():
    for j in range(5):
        for i in range(n_states):
            g = GameState(TestWorld)
            g.world.tick()


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
