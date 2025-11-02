s = ""

for i in range(0,16):
    for j in range(0,30):
        s += "    if = {\n"
        s += f"        limit = {{ var:comp_{i}_{j} = {{ compare_value = 12 }} }}\n"
        s += "        set_variable = { name = ms_comp_counter value = 0 }\n"
        if i != 0:
            s += "        if = { limit = { var:comp_" + f"{i-1}_{j}" + " = { compare_value = 10 } } change_variable = { name = ms_comp_counter add = 1 } }\n"
            if j != 0:
                s += "        if = { limit = { var:comp_" + f"{i-1}_{j-1}" + " = { compare_value = 10 } } change_variable = { name = ms_comp_counter add = 1 } }\n"
            if j != 29:
                s += "        if = { limit = { var:comp_" + f"{i-1}_{j+1}" + " = { compare_value = 10 } } change_variable = { name = ms_comp_counter add = 1 } }\n"
        
        if i != 15:
            s += "        if = { limit = { var:comp_" + f"{i+1}_{j}" + " = { compare_value = 10 } } change_variable = { name = ms_comp_counter add = 1 } }\n"
            if j != 0:
                s += "        if = { limit = { var:comp_" + f"{i+1}_{j-1}" + " = { compare_value = 10 } } change_variable = { name = ms_comp_counter add = 1 } }\n"
            if j != 29:
                s += "        if = { limit = { var:comp_" + f"{i+1}_{j+1}" + " = { compare_value = 10 } } change_variable = { name = ms_comp_counter add = 1 } }\n"
        
        if j != 0:
            s += "        if = { limit = { var:comp_" + f"{i}_{j-1}" + " = { compare_value = 10 } } change_variable = { name = ms_comp_counter add = 1 } }\n"
        
        if j != 29:
            s += "        if = { limit = { var:comp_" + f"{i}_{j+1}" + " = { compare_value = 10 } } change_variable = { name = ms_comp_counter add = 1 } }\n"
        s += "        set_variable = { name = " + f"comp_{i}_{j}" + " value = root.var:ms_comp_counter }\n"
        s += "    }\n"

with open("output.txt", "w") as f:
    f.write(s)