s = ""

for i in range(0,16):
    for j in range(0,30):
        s += f"""
    if = {{
        limit = {{ AND = {{ var:comp_{i}_{j} = {{ compare_value = 10 }} var:value_{i}_{j} = {{ compare_value = 12 }} }} }}
        set_variable = {{ name = value_{i}_{j} value = 10 }}
    }}"""

with open("output.txt", "w") as f:
    f.write(s)