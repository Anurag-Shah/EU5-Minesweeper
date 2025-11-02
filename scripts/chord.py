s = ""

for i in range(0,16):
    for j in range(0,30):
        s += "    else_if = {\n"
        s += f"        limit = {{ AND = {{ var:ms_t_cr = {{ compare_value = {i} }} var:ms_t_cc = {{ compare_value = {j} }} var:value_{i}_{j} = {{ compare_value > 0 }} var:value_{i}_{j} = {{ compare_value <= 8 }} }} }}\n"
        
        # step 1 - count flags

        s += "        set_variable = { name = ms_flag_counter value = 0 }\n"

        if i != 0:
            s += "        if = { limit = { var:value_" + f"{i-1}_{j}" + " = { compare_value = 11 } } change_variable = { name = ms_flag_counter add = 1 } }\n"
            if j != 0:
                s += "        if = { limit = { var:value_" + f"{i-1}_{j-1}" + " = { compare_value = 11 } } change_variable = { name = ms_flag_counter add = 1 } }\n"
            if j != 29:
                s += "        if = { limit = { var:value_" + f"{i-1}_{j+1}" + " = { compare_value = 11 } } change_variable = { name = ms_flag_counter add = 1 } }\n"
        
        if i != 15:
            s += "        if = { limit = { var:value_" + f"{i+1}_{j}" + " = { compare_value = 11 } } change_variable = { name = ms_flag_counter add = 1 } }\n"
            if j != 0:
                s += "        if = { limit = { var:value_" + f"{i+1}_{j-1}" + " = { compare_value = 11 } } change_variable = { name = ms_flag_counter add = 1 } }\n"
            if j != 29:
                s += "        if = { limit = { var:value_" + f"{i+1}_{j+1}" + " = { compare_value = 11 } } change_variable = { name = ms_flag_counter add = 1 } }\n"
        
        if j != 0:
            s += "        if = { limit = { var:value_" + f"{i}_{j-1}" + " = { compare_value = 11 } } change_variable = { name = ms_flag_counter add = 1 } }\n"
        
        if j != 29:
            s += "        if = { limit = { var:value_" + f"{i}_{j+1}" + " = { compare_value = 11 } } change_variable = { name = ms_flag_counter add = 1 } }\n"

        # step 2 - counter check

        s += "        if = {\n"
        s += f"            limit = {{ var:ms_flag_counter = {{ compare_value = root.var:value_{i}_{j} }} }}\n"

        # step 3 - reveal value 12 neighbors

        if i != 0:
            s += "            if = { limit = { var:value_" + f"{i-1}_{j}" + " = { compare_value = 12 } } set_variable = { name = " + f"value_{i-1}_{j}" + " value = " + f"var:comp_{i-1}_{j}" + " } }\n"
            if j != 0:
                s += "            if = { limit = { var:value_" + f"{i-1}_{j-1}" + " = { compare_value = 12 } } set_variable = { name = " + f"value_{i-1}_{j-1}" + " value = " + f"var:comp_{i-1}_{j-1}" + " } }\n"
            if j != 29:
                s += "            if = { limit = { var:value_" + f"{i-1}_{j+1}" + " = { compare_value = 12 } } set_variable = { name = " + f"value_{i-1}_{j+1}" + " value = " + f"var:comp_{i-1}_{j+1}" + " } }\n"
        
        if i != 15:
            s += "            if = { limit = { var:value_" + f"{i+1}_{j}" + " = { compare_value = 12 } } set_variable = { name = " + f"value_{i+1}_{j}" + " value = " + f"var:comp_{i+1}_{j}" + " } }\n"
            if j != 0:
                s += "            if = { limit = { var:value_" + f"{i+1}_{j-1}" + " = { compare_value = 12 } } set_variable = { name = " + f"value_{i+1}_{j-1}" + " value = " + f"var:comp_{i+1}_{j-1}" + " } }\n"
            if j != 29:
                s += "            if = { limit = { var:value_" + f"{i+1}_{j+1}" + " = { compare_value = 12 } } set_variable = { name = " + f"value_{i+1}_{j+1}" + " value = " + f"var:comp_{i+1}_{j+1}" + " } }\n"
        
        if j != 0:
            s += "            if = { limit = { var:value_" + f"{i}_{j-1}" + " = { compare_value = 12 } } set_variable = { name = " + f"value_{i}_{j-1}" + " value = " + f"var:comp_{i}_{j-1}" + " } }\n"
        
        if j != 29:
            s += "            if = { limit = { var:value_" + f"{i}_{j+1}" + " = { compare_value = 12 } } set_variable = { name = " + f"value_{i}_{j+1}" + " value = " + f"var:comp_{i}_{j+1}" + " } }\n"

        # step 4 - set value 10 neighbors to value 9 and mark loss
        s += "            set_variable = { name = ms_loss_counter value = 0 }\n"
        if i != 0:
            s += "            if = { limit = { var:value_" + f"{i-1}_{j}" + " = { compare_value = 10 } } set_variable = { name = " + f"value_{i-1}_{j}" + " value = 9 } change_variable = { name = ms_loss_counter add = 1 } }\n"
            if j != 0:
                s += "            if = { limit = { var:value_" + f"{i-1}_{j-1}" + " = { compare_value = 10 } } set_variable = { name = " + f"value_{i-1}_{j-1}" + " value = 9 } change_variable = { name = ms_loss_counter add = 1 } }\n"
            if j != 29:
                s += "            if = { limit = { var:value_" + f"{i-1}_{j+1}" + " = { compare_value = 10 } } set_variable = { name = " + f"value_{i-1}_{j+1}" + " value = 9 } change_variable = { name = ms_loss_counter add = 1 } }\n"
        
        if i != 15:
            s += "            if = { limit = { var:value_" + f"{i+1}_{j}" + " = { compare_value = 10 } } set_variable = { name = " + f"value_{i+1}_{j}" + " value = 9 } change_variable = { name = ms_loss_counter add = 1 } }\n"
            if j != 0:
                s += "            if = { limit = { var:value_" + f"{i+1}_{j-1}" + " = { compare_value = 10 } } set_variable = { name = " + f"value_{i+1}_{j-1}" + " value = 9 } change_variable = { name = ms_loss_counter add = 1 } }\n"
            if j != 29:
                s += "            if = { limit = { var:value_" + f"{i+1}_{j+1}" + " = { compare_value = 10 } } set_variable = { name = " + f"value_{i+1}_{j+1}" + " value = 9 } change_variable = { name = ms_loss_counter add = 1 } }\n"
        
        if j != 0:
            s += "            if = { limit = { var:value_" + f"{i}_{j-1}" + " = { compare_value = 10 } } set_variable = { name = " + f"value_{i}_{j-1}" + " value = 9 } change_variable = { name = ms_loss_counter add = 1 } }\n"
        
        if j != 29:
            s += "            if = { limit = { var:value_" + f"{i}_{j+1}" + " = { compare_value = 10 } } set_variable = { name = " + f"value_{i}_{j+1}" + " value = 9 } change_variable = { name = ms_loss_counter add = 1 } }\n"

        # step 5 - if loss, lose
        s += """
            if = {
                limit = {
                    var:ms_loss_counter = { compare_value > 0 }
                }
                ms_lose_game = yes
            }\n"""

        # step 2 end
        s += "        }\n"
        # step 1 end
        s += "    }\n"

with open("output.txt", "w") as f:
    f.write(s)