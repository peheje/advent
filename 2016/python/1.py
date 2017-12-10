from collections import defaultdict, deque

content = "R1, R1, R3, R1, R1, L2, R5, L2, R5, R1, R4, L2, R3, L3, R4, L5, R4, R4, R1, L5, L4, R5, R3, L1, R4, R3, L2, L1, R3, L4, R3, L2, R5, R190, R3, R5, L5, L1, R54, L3, L4, L1, R4, R1, R3, L1, L1, R2, L2, R2, R5, L3, R4, R76, L3, R4, R191, R5, R5, L5, L4, L5, L3, R1, R3, R2, L2, L2, L4, L5, L4, R5, R4, R4, R2, R3, R4, L3, L2, R5, R3, L2, L1, R2, L3, R2, L1, L1, R1, L3, R5, L5, L1, L2, R5, R3, L3, R3, R5, R2, R5, R5, L5, L5, R2, L3, L5, L2, L1, R2, R2, L2, R2, L3, L2, R3, L5, R4, L4, L5, R3, L4, R1, R3, R2, R4, L2, L3, R2, L5, R5, R4, L2, R4, L1, L3, L1, L3, R1, R2, R1, L5, R5, R3, L3, L3, L2, R4, R2, L5, L1, L1, L5, L4, L1, L1, R1"
data = content.split(", ")


class Position:
    def __init__(self):
        self.row = 0
        self.col = 0

    def manhatten(self):
        return abs(self.row) + abs(self.col)


compass = deque("NESW")
pos = Position()
visited = defaultdict(int)
visited["0:0"] = 1
visited_twice = False
moves = {"N": {"row": 1, "col": 0},
         "S": {"row": -1, "col": 0},
         "E": {"row": 0, "col": 1},
         "W": {"row": 0, "col": -1}}

for move in data:
    steps = int(move[1:])
    direction = move[0]

    if direction == "R":
        compass.rotate(-1)
    else:
        compass.rotate()
    heading = compass[0]

    for i in range(steps):
        pos.row += moves[heading]["row"]
        pos.col += moves[heading]["col"]
        visited[str(pos.row) + ":" + str(pos.col)] += 1

        if not visited_twice:
            if any(v > 1 for v in visited.values()):
                print("Pt2", pos.manhatten())
                visited_twice = True

print("Pt1", pos.manhatten())
