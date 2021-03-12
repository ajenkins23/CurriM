#!/usr/bin/env python3
from src.currim_login import Login
from src.currim_explorer import *
from src.currim_path import *
from os.path import exists

Login()

if not exists(f"{CURRIM_LOC}/.data/currim/tree.pickle"):
    save_currim_tree()
tree=load_data(f"{CURRIM_LOC}/.data/currim/tree")

for uid,module in tree.items():
    for uid, topic in module.items():
        for problem,uid in topic.items():
            print(problem,uid)

