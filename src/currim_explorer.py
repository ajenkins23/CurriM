import os
from src.currim_lms import *
from src.currim_io import *
    
def get_currim_tree():
    tree={}
    for module in get_name_uid(GetRaw("modules","")):
        top={}
        for topic in get_name_uid(GetRaw("topics",module[1])):
            prob={}
            for problem in get_name_uid(GetRaw("problems",topic[1])):
                prob.update({problem[0]:problem[1]})
            top.update({topic:prob})
        tree.update({module:top})
    return tree

def get_all_raw():
    all_raw={}
    mod_raw=GetRaw("modules","")
    top_raw,pro_raw=[],[]
    for module in get_name_uid(mod_raw):
        temp_top=GetRaw("topics",module[1])
        for topic in get_name_uid(temp_top):
            temp_pro=GetRaw("problems",topic[1])
            pro_raw.append(temp_pro)
        top_raw.append(temp_top)
    all_raw.update({"modules":mod_raw})
    all_raw.update({"topics":top_raw})
    all_raw.update({"problems":pro_raw})
    return all_raw

def save_currim_tree():
    if not (os.path.exists(CURRIM_LOC+"/.data/currim")): os.system(f"mkdir {CURRIM_LOC}/.data/currim")
    save_data(CURRIM_LOC+"/.data/currim/tree",get_currim_tree())
