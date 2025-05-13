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
            answer = input("You want to create a new user?? (y/n) ")
            if answer.upper() == "Y" or "YES":
                cadNewUser()
            break
    #I can't get back
    return login

def cadNewUser():
    cpf = input("CPF: ")
    name = input("Name: ")
    login = input("Login: ")
    password = input("Password: ")
    idrole = int(input("ID role: "))
    password = sha256(password.encode('utf-8')).hexdigest()
    conn.execute("INSERT INTO user VALUES (?,?,?,?,?)", (cpf,name,login,password,idrole))
    conn.commit()
    print("Registered!")

def changePermission():
    cpfUser = input("Type a CPF of the user that you want change a permission: ")
    cursor.execute("SELECT cpf,name,idrole FROM user WHERE cpf = ?", (cpfUser,))
    username = cursor.fetchone()
    conn.commit()
    option = input(f"You want alter a permission of the user {username[1]} who has permission {username[2]} y/s?")
    if option.upper() == "Y" or "YES":
        print("Enter 1 for Administrator, 2 for Author and 3 for Reader")
        role = input("Select a option: ")
        if role == "1" or "2" or  "3":
            cursor.execute("UPDATE user SET idrole = ? WHERE cpf = ?", (role, username[0]))
            conn.commit()
            print("Successfully changed!")
        else:
            print("You must have entered the wrong number!")
            print("Operation canceled!")

def removePermission():
    cpf_user = input("Type a CPF of the user that you want remove permission: ")
    cursor.execute("SELECT cpf,name,idrole FROM user WHERE cpf = ?", (cpf_user,))
    username = cursor.fetchone()
    conn.commit()
    option = input(f"You want to remove a permission from user {username[1]} who has the permission {username[2]}? (the default permission will be set to 3 - Reader) y/n: ")
    if option.upper() == "Y" or "YES":
        cursor.execute("UPDATE user SET idrole = ? WHERE cpf = ?", ("3",cpf_user))
        conn.commit()
        print("Successfully Removed!")
    else:
        print("You must have entered the wrong number!")
        print("Operation canceled!")

def deleteUser():
    user = input("Enter the CPF of the user you want to delete: ")
    cursor.execute("SELECT cpf,name FROM user WHERE cpf = ?", (user,))
    username = cursor.fetchone()
    conn.commit()
    option = input(f"You want delete a user {username[1]} ys")
    if option.upper() == "Y" or "YES":
        cursor.execute("DELETE FROM user WHERE cpf = ?", (username[0],))
        conn.commit()
        print("Successfully deleted!")
    else:
        print("Operation canceled!")

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
                file_edit = file_contend + " " + contend
            with open(archive, "w") as filerec:
                filerec.write(file_edit)
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
                changePermission()
            case "3":
                removePermission()
            case "4":
                deleteUser()
            case "5":
                contend = input("Type name of file: ")
                contend += ".txt"
                with open(contend, "w") as file:
                    contend = input("Write the contents of the file: ")
                    file.write(contend)
                    print("Successfully created!")
            case "6":
                file_name = input("Type name of file for edit: ")
                file_name += ".txt"
                with open(file_name, "r") as file:
                    file_contend = file.read()
                    print(f"This is the contend of the file: {file_contend}")
                    if file_contend:
                        menuEdit(file_name)
                    else:
                        print("File not exist!")
                        break
            case "7":
                file_name = input("Type name of file for read: ")
                file_name += ".txt"
                with open(file_name, "r") as file:
                    file_contend = file.read()
                    print(f"This is the contend of the file: {file_contend}")
            case "0":
                break

menu()

conn.close()
quit()