import subprocess
from src.currim_path import *

def login():
    out=subprocess.getoutput(f"{LMS} login")
    return out

def GetRaw(name,uid):
    return [line for line in subprocess.getoutput(f"{LMS} {name} {uid}").splitlines() if '[' in line]

def get_name_uid(raw): 
    return [(line[0:line.find('[')-1], line[line.find('(')+1:line.find(")")]) for line in raw]

# def IsLoggedIn():
    # token=