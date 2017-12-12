from collections import defaultdict

with open("../data/8.txt") as f:
    lines = [x.replace("\n", "") for x in f.readlines()]

memory = defaultdict(int)

for line in lines:
    tokens = line.split(" ")
    var_name, operation, operation_val, condition_var, condition, condition_val = tokens[0], tokens[1], tokens[2], tokens[4], tokens[5], tokens[6]
    code = "{} {} {}".format(memory[condition_var], condition, condition_val)
    boolean = eval(code)
    if boolean:
        value = -int(operation_val) if operation == "dec" else int(operation_val)
        code = "memory['{}'] += {}".format(var_name, value)
        exec(code)

print(max(memory.values()))
