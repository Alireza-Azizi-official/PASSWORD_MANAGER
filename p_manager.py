from  cryptography.fernet  import Fernet


# to make a key to lock the pass file 
# def write_key():
#     key = Fernet.generate_key()
#     with open("Key.key", "wb") as key_file:
#         key_file.write(key)
#write_key()

def load_key():
    file = open("Key.key","rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password?") 
key = load_key()  + master_pwd.encode()
fer = Fernet(key)

def view():
    with open("password.txt", "r") as f :
        for line in f.readlines():
            data= line.rstrip()
            parts = data.split('|')
            if len(parts)== 2:
                user, passw = parts
                print("User: ", user, " | Password: ",fer.decrypt(passw.encode()).decode())
            else:
                print("Invalid line format:", data)
            

def add():
    name = input("Account name:")
    pwd = input("Password:")

    with open("password.txt", "a") as f :
         f.write(name + "|" +  fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones(view, add)? press q to quit. ").lower()
    
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue