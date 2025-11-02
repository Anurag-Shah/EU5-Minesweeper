s = ""

for i in range(0,16):
    s += "                hbox = {\n"
    for j in range(0,30):
        for k in range(0,14):
            s += f"                    ms_{k} = {{\n"
            s += f"                        visible = \"[GetPlayer.MakeScope.Var('show_{i}_{j}_{k}').IsSet]\"\n"
            if k in range(1,9) or k == 12: s += f"                        onclick = \"[GetScriptedGui('lc_{i}_{j}').Execute(GuiScope.SetRoot(GetPlayer.MakeScope).End)]\"\n"
            if k == 11 or k == 12: s += f"                        onrightclick = \"[GetScriptedGui('rc_{i}_{j}').Execute(GuiScope.SetRoot(GetPlayer.MakeScope).End)]\"\n"
            s += "                    }\n"
    s += "                }\n\n"

with open("output.txt", "w") as f:
    f.write(s)