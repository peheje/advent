with open("../data/12.txt") as f:
    lines = [x
                 .replace("\n", "")
                 .replace(",", "")
                 .replace("<->", "")
                 .replace("  ", " ") for x in f.readlines()]

print(lines)


class Connection:
    def __init__(self, name, connection_names):
        self.name = name,
        self.connection_names = connection_names
        self.connections = {}


connections = {}
for line in lines:
    data = line.split(" ")
    name = data[0]
    cons_names = data[1:]
    connections[name] = Connection(name, cons_names)

# To references
for name, con in connections.items():
    for con_name in con.connection_names:
        con.connections[con_name] = connections[con_name]


def search(connection, target_id):
    c = 0
    for name, con in connection.connections.items():
        found = False
        for name2, con2 in con.connections.items():
            if name != name2:
                search(con, target_id)
            if name2 == target_id:
                found = True
                break
        if found:
            c += 1
    return c

# Search for 0
for con in connections.values():
    search(con, "0")
