from copy import copy

with open("../data/6.txt") as f:
    bank = [int(x) for x in f.readline().split("\t")]

# bank = [0, 2, 7, 0]
c = 0
seen = []
while bank not in seen:
    seen.append(copy(bank))

    imax = bank.index(max(bank))
    redistribute = bank[imax]
    bank[imax] = 0

    for i in range(1, redistribute + 1):
        bank[(imax + i) % len(bank)] += 1


idx = seen.index(bank)

print("pt1", len(seen))
print("pt2", len(seen)-idx)