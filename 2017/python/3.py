from collections import deque, defaultdict


def neighbors(x, y, mem):
    n = 0
    for i, j in [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]:
        n += mem[i + x, j + y]
    return n


def neighbors_check(x, y, mem, target):
    global run
    if not run:
        return 0
    n = neighbors(x, y, mem)
    if n > target:
        print("pt2 {}".format(n))
        run = False
    return n


target = 347991
compass = deque("ENWS")
height, width, counter = 1, 1, 1
x, y = 0, 0
heading = ""
memory = defaultdict(int)
memory[0, 0] = 1
run = True

while counter < target or run:
    # Take step in heading
    heading = compass[0]

    # Add to height or width
    if heading == "E":
        for i in range(1, width + 1):
            memory[x + i, y] = neighbors_check(x + i, y, memory, target)
        x += width
        counter += width
        width += 1
    elif heading == "W":
        for i in range(1, width + 1):
            memory[x - i, y] = neighbors_check(x - i, y, memory, target)
        x -= width
        counter += width
        width += 1
    elif heading == "N":
        for i in range(1, height + 1):
            memory[x, y + i] = neighbors_check(x, y + i, memory, target)
        y += height
        counter += height
        height += 1
    else:
        for i in range(1, height + 1):
            memory[x, y - i] = neighbors_check(x, y - i, memory, target)
        y -= height
        counter += height
        height += 1

    # Rotate compass
    compass.rotate(-1)

# Calculate distance to 1 maybe took too many steps in heading
extra = counter - target
if heading == "E":
    x -= extra
elif heading == "W":
    x += extra
elif heading == "N":
    y -= extra
else:
    y += extra
print("pt1", abs(x) + abs(y))
