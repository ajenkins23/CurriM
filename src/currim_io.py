from pickle import load,dump
def load_data(path):
    path+=".pickle"
    with open(path,"rb+") as file: return(load(file))

def save_data(path,data):
    path+=".pickle"
    with open(path,"wb+") as file: dump(data,file)

def load_file(path):
    with open(path,"r") as file:
        return file.readlines()

def save_file(path,data):
    with open(path,"w") as file:
        file.writelines(data)