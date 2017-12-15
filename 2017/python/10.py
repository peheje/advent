from functools import reduce


def take_circular(x: iter, pos: int, length: int):
    c = [x[(pos + i) % len(x)] for i in range(length)]
    return c


def insert_circular(main: list, sub: iter, begin: int):
    for i, v in enumerate(sub):
        main[(begin + i) % len(main)] = v
    return main


def one_round(knot: list, pos: int, skip: int, lengths: iter):
    for length in lengths:
        sublist = take_circular(knot, pos, length)
        knot = insert_circular(knot, reversed(sublist), pos)
        pos += length + skip
        skip += 1
    return knot, pos, skip


def to_chunks(x: iter, n: int):
    for i in range(0, len(x), n):
        yield x[i:i + n]


def xor_many(x: list, n: int):
    xored_list = []
    chunks = to_chunks(x, n)
    for chunk in chunks:
        xored = reduce(lambda a, b: a ^ b, chunk)
        xored_list.append(xored)
    return xored_list


with open("../data/10.txt") as f:
    data = f.readline()
lengths = [int(x) for x in data.split(",")]
suffix = [17, 31, 73, 47, 23]
lengths_ascii = [ord(c) for c in data] + suffix

# Part 1
knot = [i for i in range(256)]
pos, skip = 0, 0
knot, pos, skip = one_round(knot, pos, skip, lengths)
print("pt1", knot[0] * knot[1])

# Part 2
pos, skip = 0, 0
knot = [i for i in range(256)]
for i in range(64):
    knot, pos, skip = one_round(knot, pos, skip, lengths_ascii)
dense = xor_many(knot, 16)
knot_hash = "".join([format(x, '02x') for x in dense])
print("pt2", knot_hash)
