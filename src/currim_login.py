from src import currim_lms,currim_path

def Login():
    username=input("Please enter your username:\n > ")
    currim_path.ReplaceConfig(username)
    output=currim_lms.login()
    if "Invalid user credentials" in output:
        print("invalid_user_creds")
        return False
    elif "ConnectError" in output:
        print("no_internet")
        return False
    elif "Login successful" in output: 
        print("Log in successfull")
        return True
    else:
        print(output,"\n\n\n Unknown Error")
        return False
