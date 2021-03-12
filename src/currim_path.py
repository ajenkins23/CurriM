from pathlib import Path
from src.currim_io import *

HOME=str(Path.home())
CURRIM_LOC=HOME+"/.currim"
DATA=CURRIM_LOC+"/.data"
WTC_LMS=DATA+"lms/wtc-lms"
CONFIG=HOME+"/.config/wtc/config.yml"
REPO=DATA+"/users"
LMS=CURRIM_LOC+"/.data/lms/wtc-lms"


def ReplaceConfig(username):
    config_yml=load_file(CONFIG)
    for line in range(len(config_yml)):
        if "repo_path" in config_yml[line]: config_yml[line]=f"repo_path: {REPO}/{username}\n"
        if "username" in config_yml[line]: config_yml[line]=f"username: {username}@student.wethinkcode.co.za\n"
    save_file(CONFIG,config_yml)