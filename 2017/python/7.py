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


def children_weight(nodes, node):
    # Call once with node=root
    if len(node.children) > 0:
        s = sum(children_weight(nodes, cnode) for _, cnode in node.children.items())
        node.tower_weight = s + node.weight
        return node.tower_weight
    else:
        return node.weight


def find_wrong_weight(nodes):
    for name, node in nodes.items():
        if len(node.children) > 0:
            if not all(x.tower_weight == node.children[0].tower_weight for x in node.children):
                pass


with open("../data/7.txt") as f:
    lines = [x.replace("\n", "") for x in f.readlines()]

nodes = read_nodes(lines)

# To references
for name, node in nodes.items():
    for cname in node.child_names:
        node.children[cname] = nodes[cname]

# Find root
root = find_root(nodes)
print("pt1", root.name)

# Find tower weights
children_weight(nodes, root)

d = 2