with open("../data/4.txt") as f:
    content = [row.replace("\n", "") for row in f.readlines()]


def part1():
    n_valid = 0
    for line in content:
        words = line.split(" ")
        valid = True
        for word in words:
            if words.count(word) > 1:
                valid = False
                break
        if valid:
            n_valid += 1
    return n_valid


def part2():
    n_valid = 0
    for line in content:
        words = line.split(" ")
        sorted_words = [sorted(w) for w in words]
        valid = True
        for word in words:
            sorted_word = sorted(word)
            if sorted_words.count(sorted_word) > 1:
                valid = False
                break
            if words.count(word) > 1:
                valid = False
                break
        if valid:
            n_valid += 1
    return n_valid


print("pt1", part1())
print("pt2", part2())

