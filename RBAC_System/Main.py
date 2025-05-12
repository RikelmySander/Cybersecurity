import sqlite3
from hashlib import sha256

conn = sqlite3.connect("db_rbac.db")
cursor = conn.cursor()

def signup():
    while True:
        print("-" * 20)
        print("SIGNUP")
        print("-" * 20)
        login = input("Login: ")
        cursor.execute("SELECT login from user where login = ?", (login,))
        login_attempt = cursor.fetchone()
        if login_attempt:
            password = input("Password: ")
            password = sha256(password.encode('utf-8')).hexdigest()
            cursor.execute("SELECT senha from user where senha = ?", (password,))
            pass_attempt = cursor.fetchone()
            if pass_attempt:
                print(f"You are logged!, {login}")
                break
        else:
            print("User not exist!")
            answer = input("Want to create a new user?? (y/n) ")
            if answer.upper() == "Y" or "YES":
                cadNewUser()
            break
    #I can't get back
    return login

def cadNewUser():
    cpf = input("CPF:")
    name = input("Name:")
    login = input("Login")
    password = input("Password")
    idrole = int(input("ID role: "))
    password = sha256(password.encode('utf-8')).hexdigest()
    conn.execute("INSERT INTO user VALUES (?,?,?,?,?)", (cpf,name,login,password,idrole))
    conn.commit()
    print("Registered!")

def menuEdit(archive):
    print("-" * 20)
    print("MENU EDIT")
    print("-" * 20)
    print("1 - Overwrite the file ")
    print("2 - Add the end of the text")
    option = input("Select an option: ")
    match option:
        case "1":
            contend = input("Enter the contend: ")
            with open(archive, "w") as file:
                file.write(contend)
            print("Successfully overwritten!")
        case "2":
            contend = input("Enter the contend: ")
            with open(archive , "r") as file:
                file_contend = file.read()
                file_contend += contend
            with open(archive, "w") as filerec:
                filerec.write(file_contend)
    print("Successfully edit!")

def menu():
    while True:
        print("-"*20)
        print("MENU")
        print("-" * 20)
        print("1 - Create a user")
        print("2 - Change permission")
        print("3 - Remove permission ")
        print("4 - Delete user ")
        print("5 - Create a file")
        print("6 - Edit a file ")
        print("7 - Read a file")
        print("0 - Exit")
        print("-" * 20)
        option = input("Select an option: ")
        match option :
            case "1":
                cadNewUser()
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                contend = input("Type name of file: ")
                contend += ".txt"
                with open(contend, "w") as file:
                    contend = input("Write the contents of the file: ")
                    file.write(contend)
                    print("Successfully created!")
            case "6":
                file_name = input("Type name of file for edit: ")
                with open(file_name, "r") as file:
                    if file.read():
                        print(file.read())
                        menuEdit(file_name)
                    else:
                        print("File not exist!")
                        break
            case "7":
                pass
            case "0":
                break

menu()

conn.close()
quit()