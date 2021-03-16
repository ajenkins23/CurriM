from os import mkdir
from os.path import exists,realpath
from os import system
from pathlib import Path

HOME=str(Path.home())
INSTALL_LOC=HOME+ "/.currim"
CURRIM_LOC=realpath(__file__)[:len(realpath(__file__))-22]
LMS=CURRIM_LOC+"/setup/wtc-lms"
 

def mkdir(Path):
    system(f"mkdir {Path}")

def cp(file_path, location_path):
    system(f"cp {file_path} {location_path}")

def cpdir(dir_path, location_path):
    system(f"cp -R {dir_path} {location_path}")

def rm(file_path):
    system(f"rm {file_path}")

def CheckInstallPaths():
    if not(exists(INSTALL_LOC)):mkdir(INSTALL_LOC) 
    if not(exists(INSTALL_LOC+"/.data")):mkdir(INSTALL_LOC+"/.data")

def InstallCurrim():
    CheckInstallPaths()
    cpdir(CURRIM_LOC+"/src",INSTALL_LOC)
    cp(CURRIM_LOC+"/main.py",INSTALL_LOC)
    InstallLms()

def GetRc():
    rc=[False,False]
    if exists(HOME+"/.bashrc"):rc[0]=True
    if exists(HOME+"/.zshrc"):rc[1]=True
    return rc

def AddAlias():
    rc=GetRc()
    alias_currim=f'alias "currim"="{INSTALL_LOC}/main.py"\n'
    alias_lms=f'alias "wtc-lms"="{INSTALL_LOC}/.data/lms/wtc-lms"\n'
    if rc[0]==True:
        with open(HOME+"/.bashrc") as file:bash=file.readlines()
        if alias_currim not in bash: bash.append(alias_currim)
        if alias_lms not in bash: bash.append(alias_lms)
        with open(HOME+"/.bashrc","w+") as file: file.writelines(bash)  

    if rc[1]==True:
        with open(HOME+"/.zshrc") as file:zsh=file.readlines()
        if alias_currim not in zsh:zsh.append(alias_currim)
        if alias_lms not in zsh:zsh.append(alias_lms)
        with open(HOME+"/.zshrc","w+") as file:file.writelines(zsh)  


def InstallLms():
    if not(exists(INSTALL_LOC+"/.data/lms")): mkdir(INSTALL_LOC+"/.data/lms")
    cp(LMS,INSTALL_LOC+"/.data/lms")
    lms_dest=INSTALL_LOC+"/.data/lms/wtc-lms"
    if (exists(HOME+"/.config/wtc/config.yml")): rm(HOME+"/.config/wtc/config.yml")
    if not(exists(f"{HOME}/.config/wtc")): mkdir(f"{HOME}/.config/wtc")
    cp(CURRIM_LOC+"/setup/config.yml",HOME+"/.config/wtc/")
    AddAlias()
    system(f"chmod +x {INSTALL_LOC}/main.py")
    system(f"chmod +x {lms_dest}")
    system("bash")
    
InstallCurrim()