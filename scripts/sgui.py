s = ""

for i in range(0,16):
    for j in range(0,30):
        s += f"lc_{i}_{j} = {{ effect = {{ ms_lc = {{ r = {i} c = {j} }} }} }}\n"
        s += f"rc_{i}_{j} = {{ effect = {{ ms_rc = {{ r = {i} c = {j} }} }} }}\n"

with open("output.txt", "w") as f:
    f.write(s)