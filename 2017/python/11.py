import math


class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return "({}:{})".format(self.x, self.y)

    def distance(self):
        # Take diagonal steps towards self.x == 0
        steps = abs(self.x)
        # Diagonal steps changes y too:
        if self.y > 0:
            # Might still be positive, but never negative (never go too far)
            y = max(self.y - steps, 0)
        else:
            # Might still be negative, but not positive (never go too far)
            y = min(self.y + steps, 0)
        # You move 2 positions north/south by a single move so divide y's by 2
        return abs(y) // 2 + abs(steps)


moveset = {
    "n": Position(0, 2),
    "ne": Position(1, 1),
    "se": Position(1, -1),
    "s": Position(0, -2),
    "sw": Position(-1, -1),
    "nw": Position(-1, 1),
}

with open("../data/11.txt") as f:
    moves = f.readline().split(",")

pos = Position(0, 0)
farthest = 0

for move_str in moves:
    move = moveset[move_str]
    pos += move

    dist = pos.distance()
    if dist > farthest:
        farthest = dist

print(pos)
print("pt1", pos.distance())
print("pt2", farthest)
