with open("../data/9.txt") as f:
    data = f.readline()


def is_valid(string: str, idx: int):
    exclamations = 0
    while idx > 0:
        idx -= 1
        if string[idx] == "!":
            exclamations += 1
        else:
            break
    # If even number of exclamations they cancel out, else invalid.
    return exclamations % 2 == 0


def remove_garbage(string: str):
    n_removed = 0
    while "<" in string:
        # Find valid start and end of garbage
        search_begin = 0
        start_idx = string.index("<", search_begin)
        while not is_valid(string, start_idx):
            search_begin += 1
            start_idx = string.index("<", search_begin)

        search_begin = 0
        end_idx = string.index(">", start_idx + search_begin)
        while not is_valid(string, end_idx):
            search_begin += 1
            end_idx = string.index(">", start_idx + search_begin)

        # Remove garbage
        removed = string[start_idx:end_idx + 1]
        string = string[:start_idx] + string[end_idx + 1:]
        n_removed += count_valid_removed(removed)
    return string, n_removed


def count_valid_removed(removed: str):
    valid = -2
    for i, c in enumerate(removed):
        if is_valid(removed, i) and c != "!":
            valid += 1
    return valid


def count_groups(string: str):
    count = 0
    level = 1
    for c in string:
        if c == "{":
            count += level
            level += 1
        elif c == "}":
            level -= 1
    return count


cleaned, n_removed = remove_garbage(data)
print("pt1", count_groups(cleaned))
print("pt2", n_removed)
