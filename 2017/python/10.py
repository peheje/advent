def take_circular(x: list, pos: int, length: int):
    c = [x[(pos + i) % len(x)] for i in range(length)]
    return c


def insert_circular(main: list, sub: list, begin: int):
    for i, v in enumerate(sub):
        main[(begin + i) % len(main)] = v
    return main


# knot = [i for i in range(5)]
# lengths = [3, 4, 1, 5]

knot = [i for i in range(256)]
with open("../data/10.txt") as f:
    lengths = [int(x) for x in f.readline().split(",")]

pos = 0
skip = 0

for length in lengths:
    sublist = take_circular(knot, pos, length)
    rev = list(reversed(sublist))
    knot = insert_circular(knot, rev, pos)

    pos += length + skip
    skip += 1

print(knot)

print("pt1", knot[0]*knot[1])