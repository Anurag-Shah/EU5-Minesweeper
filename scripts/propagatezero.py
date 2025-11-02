s = ""

for i in range(0,16):
    for j in range(0,30):
        s += "        if = {\n"
        s += f"            limit = {{ var:value_{i}_{j} = {{ compare_value = 12 }} }}\n"
        if i != 0:
            s += "            if = { limit = { var:value_" + f"{i-1}_{j}" + " = { compare_value = 0 } } set_variable = { name = " + f"value_{i}_{j}" + " value = " + f"var:comp_{i}_{j}" + " } change_variable = { name = ms_prop_counter add = 1 } }\n"
            if j != 0:
                s += "            if = { limit = { var:value_" + f"{i-1}_{j-1}" + " = { compare_value = 0 } } set_variable = { name = " + f"value_{i}_{j}" + " value = " + f"var:comp_{i}_{j}" + " } change_variable = { name = ms_prop_counter add = 1 } }\n"
            if j != 29:
                s += "            if = { limit = { var:value_" + f"{i-1}_{j+1}" + " = { compare_value = 0 } } set_variable = { name = " + f"value_{i}_{j}" + " value = " + f"var:comp_{i}_{j}" + " } change_variable = { name = ms_prop_counter add = 1 } }\n"
        
        if i != 15:
            s += "            if = { limit = { var:value_" + f"{i+1}_{j}" + " = { compare_value = 0 } } set_variable = { name = " + f"value_{i}_{j}" + " value = " + f"var:comp_{i}_{j}" + " } change_variable = { name = ms_prop_counter add = 1 } }\n"
            if j != 0:
                s += "            if = { limit = { var:value_" + f"{i+1}_{j-1}" + " = { compare_value = 0 } } set_variable = { name = " + f"value_{i}_{j}" + " value = " + f"var:comp_{i}_{j}" + " } change_variable = { name = ms_prop_counter add = 1 } }\n"
            if j != 29:
                s += "            if = { limit = { var:value_" + f"{i+1}_{j+1}" + " = { compare_value = 0 } } set_variable = { name = " + f"value_{i}_{j}" + " value = " + f"var:comp_{i}_{j}" + " } change_variable = { name = ms_prop_counter add = 1 } }\n"
        
        if j != 0:
            s += "            if = { limit = { var:value_" + f"{i}_{j-1}" + " = { compare_value = 0 } } set_variable = { name = " + f"value_{i}_{j}" + " value = " + f"var:comp_{i}_{j}" + " } change_variable = { name = ms_prop_counter add = 1 } }\n"
        
        if j != 29:
            s += "            if = { limit = { var:value_" + f"{i}_{j+1}" + " = { compare_value = 0 } } set_variable = { name = " + f"value_{i}_{j}" + " value = " + f"var:comp_{i}_{j}" + " } change_variable = { name = ms_prop_counter add = 1 } }\n"
        s += "        }\n"

with open("output.txt", "w") as f:
    f.write(s)