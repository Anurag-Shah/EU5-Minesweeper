s = ""

for i in range(0,16):
    for j in range(0,30):
        s += f"set_variable = {{ name = comp_{i}_{j} value = root.var:value_{i}_{j} }}\n"

with open("output.txt", "w") as f:
    f.write(s)