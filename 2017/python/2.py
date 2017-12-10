with open("../data/2.txt") as f:
    content = [row.replace("\n", "").split("\t") for row in f.readlines()]
    matrix = [[int(x) for x in row] for row in content]
    print(matrix)

# Part 1
pt1 = [max(row) - min(row) for row in matrix]
print(sum(pt1))

# Part 2
pt2 = []
for row in matrix:
    other_pairs = [(a, b) for i, a in enumerate(row) for j, b in enumerate(row) if i != j]
    for a, b in other_pairs:
        quot, rem = divmod(a, b)
        if rem != 0: continue
        pt2.append(quot)
print(sum(pt2))
