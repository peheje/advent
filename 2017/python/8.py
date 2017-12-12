from collections import defaultdict

with open("../data/8.txt") as f:
    lines = [x.replace("\n", "") for x in f.readlines()]

print(lines)
memory = defaultdict(int)

for line in lines:
    tokens = line.split(" ")
    var_name, operation, operation_val, condition_var, condition, condition_val = tokens[0], tokens[1], tokens[2], tokens[4], tokens[5], tokens[6]



    print(line)
    print("var_name", var_name)
    print("operation", operation)
    print("operation_val", operation_val)
    print("condition_var", condition_var)
    print("condition", condition)
    print("condition_val", condition_val)
    print("_____")