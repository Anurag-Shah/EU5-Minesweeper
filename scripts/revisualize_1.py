s = ""

for i in range(0,16):
    for j in range(0,30):
        for k in range(0,14):
            s += f"    remove_variable = show_{i}_{j}_{k}\n"
s += "\n\n"
for i in range(0,16):
    for j in range(0,30):
        for k in range(0,14):
            s += f"    if = {{ limit = {{ var:value_{i}_{j} = {{ compare_value = {k} }} }} set_variable = show_{i}_{j}_{k} }}\n"

with open("output.txt", "w") as f:
    f.write(s)