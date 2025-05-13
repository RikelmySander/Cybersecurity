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

def changePermission():
    user = input("Type a CPF of the user that you want change a permission: ")
    cursor.execute("SELECT cpf,name,idrole from user where cpf = ?", (user,))
    username = cursor.fetchone()
    conn.commit()
    print(f"You want alter a permission of the user {username[1]} with permission {username[2]} ys?")
    option = input("Select a option: ")
    if option.upper() == "Y" or "YES":
        print("Type 1 for admin, 2 for Author and 3 for Reading")
        role = input("Select a option: ")
        cursor.execute("UPDATE user SET idrole = ? WHERE cpf = ?", (role, username[0]))
        conn.commit()
        print("Successefully changed!")
    else:
        print("Operation canceleted!")

def removePermission():
    user = input("Type a CPF of the user that you want delete: ")
    cursor.execute("SELECT cpf,name from user where cpf = ?", (user,))
    username = cursor.fetchone()
    conn.commit()
    option = input(f"You want delete a user {username[1]} ys")
    if option.upper() == "Y" or "YES":
        cursor.execute("DELETE cpf,name from user where cpf = ?", (user,))
        conn.commit()
    else:
        print("Operation canceleted!")

def deleteUser():
    user = input("Type a CPF of the user that you want delete: ")
    cursor.execute("SELECT cpf,name from user where cpf = ?", (user,))
    username = cursor.fetchone()
    conn.commit()
    option = input(f"You want delete a user {username[1]} ys")
    if option.upper() == "Y" or "YES":
        cursor.execute("DELETE cpf,name from user where cpf = ?", (user,))
        conn.commit()
        print("Successefully deletes!")
    else:
        print("Operation canceleted!")

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
                pass
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