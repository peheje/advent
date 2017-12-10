from Timer import Timer


class Node:
    def __init__(self, name, child_names, weight):
        self.name = name  # String
        self.child_names = child_names  # List<String>
        self.children = {}  # Dictionary<String, Node>
        self.weight = weight  # Int
        self.tower_weight = 0  # Int


def read_nodes(lines):
    nodes = {}
    for line in lines:
        split = line.split(" ")
        name = split[0]
        weight = int(split[1].replace("(", "").replace(")", ""))
        parents = [x.replace(",", "") for x in split[3:]]
        nodes[name] = Node(name, parents, weight)

    # To references
    for name, node in nodes.items():
        for cname in node.child_names:
            node.children[cname] = nodes[cname]

    return nodes


def find_root(nodes):
    for cand_name, cand in nodes.items():
        is_root = True
        for name, node in nodes.items():
            if cand_name in node.child_names:
                is_root = False
                break
        if is_root:
            return cand
    return None


def calc_tower_weights(nodes, node):
    # Call once with node=root
    if len(node.children) > 0:
        s = sum(calc_tower_weights(nodes, cnode) for cnode in node.children.values())
        node.tower_weight = s + node.weight
        return node.tower_weight
    else:
        node.tower_weight = node.weight
        return node.weight


def find_wrong_weight(nodes, node):
    # Goto bottom of tree first
    if len(node.children) > 0:
        for cnode in node.children.values():
            find_wrong_weight(nodes, cnode)

    global balanced
    if balanced:
        return

    # We cannot do it on leaf nodes
    if len(node.children) > 0:
        # Check if all children has same tower_weight
        tower_weights = [x.tower_weight for x in node.children.values()]
        if not len(set(tower_weights)) == 1:
            # Iterating dictionaries not guaranteed to be same each time, so need to use tuples
            uneven_weights = [(x.weight, x.tower_weight) for x in list(node.children.values())]
            correct_weight(uneven_weights)
            balanced = True


def correct_weight(uneven_weights):
    tmp = [list(t) for t in zip(*uneven_weights)]
    weights = tmp[0]
    tower_weights = tmp[1]

    # Find the wrong value and its index
    wrong_tuple = next((i, x) for i, x in enumerate(tower_weights) if tower_weights.count(x) == 1)
    wrong_idx = wrong_tuple[0]
    wrong_tower_value = wrong_tuple[1]

    # Get a correct tower value and calculate correct weight for wrong weight
    correct_tower_weight = tower_weights[(wrong_idx + 1) % len(tower_weights)]
    correct_weight = weights[wrong_idx] + correct_tower_weight - wrong_tower_value

    print("pt2", correct_weight)


with open("../data/7.txt") as f:
    lines = [x.replace("\n", "") for x in f.readlines()]

with Timer():
    nodes = read_nodes(lines)
    root = find_root(nodes)
    print("pt1", root.name)
    calc_tower_weights(nodes, root)
    balanced = False
    find_wrong_weight(nodes, root)
