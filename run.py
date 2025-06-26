print("\033[92mCubeHackCraft")

print("""
Ban(need Ban.ini)
Kick(need Kick.ini)
give(need give.ini)
crash: Crash the server
seed: crack the seed
\033[0m
""")

import os
i = 0
a = ["",""]
b = ""
c = "\033[0m"
title = """
\033[92m
Ban(need Ban.ini)
Kick(need Kick.ini)
give(need give.ini)
crash:Crash the server
seed: crack the seed
\033[0m
"""
while i ==0:
    cmd = input(f"{c}{b}>")
    a = cmd.split()
    if a[0] == f"cd":
        b = a[1]
        if a[1] == "/":
            b = ""
    if a[0] == "dev":
        print(f"""list a: {a}
list b: {b}
i: {i}
        """)
    if a[0] == "clear":
        os.system("clear")
        print(title)
    if a[0] == "cleartitle":
        print("Fehler")
    if a[0] == "settitle":
        print("Fehler")
    if a[0] == "color":
        if a[1] == "green":
            c = "\033[92m"
        if a[1] == "reset":
            c = "\033[0m"
    if a[0] == "setadmin" and b == "Bur":
        if a[1] == "123456789":
            b = "Bur:Admin7638463947493758449474847"
        else:
            print("Falsches passwort")
    if a[0] == "delsys" and b == "Bur:Admin7638463947493758449474847":
        exit()
    
    
    