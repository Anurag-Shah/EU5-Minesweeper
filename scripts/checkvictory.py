s = "AND = {"

for i in range(0,16):
    for j in range(0,30):
        s += f"""
                OR = {{
                    AND = {{
                        NOT = {{ var:value_{i}_{j} = {{ compare_value = 11 }} }}
                        NOT = {{ var:value_{i}_{j} = {{ compare_value = 12 }} }}
                    }}
                    AND = {{
                        OR = {{
                            var:value_{i}_{j} = {{ compare_value = 11 }}
                            var:value_{i}_{j} = {{ compare_value = 12 }}
                        }}
                        var:comp_{i}_{j} = {{ compare_value = 10 }}
                    }}
                }}"""
s += "            }"
with open("output.txt", "w") as f:
    f.write(s)