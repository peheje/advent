from copy import copy
import numba as nb

from Timer import Timer

with open("../data/5.txt") as f:
    steps = [int(row.replace("\n", "")) for row in f.readlines()]


# steps = [0, 3, 0, 1, -3]

@nb.njit(cache=True)
def part1(steps):
    n_steps = 0
    pos = 0
    while -1 < pos < len(steps):
        offset = steps[pos]
        steps[pos] += 1
        pos += offset
        n_steps += 1
    return n_steps


@nb.njit(cache=True)
def part2(steps):
    n_steps = 0
    pos = 0
    while -1 < pos < len(steps):
        offset = steps[pos]
        if offset > 2:
            steps[pos] -= 1
        else:
            steps[pos] += 1
        pos += offset
        n_steps += 1
    return n_steps


with Timer():
    print("pt1", part1(copy(steps)))

with Timer():
    print("pt2", part2(copy(steps)))
