import strutils, future, math

iterator enumerate[T](s: seq[T]): (int, T) =
   var i = 0
   while i < len(s):
       yield (i, s[i])
       i += 1

# Read data
var matrix = newSeq[seq[int]]()
for line in lines r"/Users/phj/GitRepos/advent/2017/data/2.txt":
    let 
        format_row = line.replace("\n", "").split("\t")
        row = lc[parseInt(x) | (x <- format_row), int]
    matrix.add(row)
# echo(matrix)

# Part 1
let pt1 = lc[max(row) - min(row) | (row <- matrix), int]
echo("pt1 ", sum(pt1))

# Part 2
var pt2 = newSeq[int]()
for row in matrix:
    var other_pairs = newSeq[(int, int)]()
    for i, a in enumerate(row):
        for j, b in enumerate(row):
            if i != j:
                other_pairs.add((a, b))
    for a, b in items(other_pairs):
        if (a mod b) != 0: continue
        pt2.add(int(a/b))
echo("pt2: ", sum(pt2))
