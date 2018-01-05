import strutils
import times, os

var steps = newSeq[int]()
for line in lines r"/Users/phj/GitRepos/advent/2017/data/5.txt":
    steps.add(parseint(line))
# echo steps

proc part1(steps: var seq[int]): int =
    var
        n_steps = 0
        pos = 0
    while -1 < pos and pos < len(steps):
        var offset = steps[pos]
        steps[pos] += 1
        pos += offset
        n_steps += 1
    return n_steps

proc part2(steps: var seq[int]): int =
    var
        n_steps = 0
        pos = 0
        offset = 0
    while -1 < pos and pos < len(steps):
        offset = steps[pos]
        if offset > 2:
            steps[pos] -= 1
        else:
            steps[pos] += 1
        pos += offset
        n_steps += 1
    return n_steps

# Part 1
var steps1: seq[int]
deep_copy(steps1, steps)
echo "pt1 ", part1(steps1)

# Part 2
let t0 = cpuTime()
var steps2: seq[int]
deep_copy(steps2, steps)
echo "pt2 ", part2(steps2)
let t1 =  cpuTime()
echo "Pt2 Time elapsed for Nim: ", $(t1 - t0)