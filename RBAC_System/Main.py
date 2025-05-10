import sqlite3
from hashlib import sha256
from re import Match

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

def menuAdmin():
    while True:
        print("-"*20)
        print("Menu")
        print("-" * 20)
        print("1- Create a user")
        print("2 - Change permission")
        print("3 - Remove permission ")
        print("4 - Delete user ")
        print("5 - Create a file")
        print("6 - Edit a file ")
        print("7 - Read a file")
        print("-" * 20)
        option = input("Select an option")
        match option :
            case 1:
                cadNewUser()
            case 2:
            case 3:
            case 4:
            case 5:
            case 6:
            case 7:


def menuAuthor():
    while True:
        print("-" * 20)
        print("Select an option")
        print("-" * 20)
        print("1 - Create a file")
        print("2 - Edit a file ")
        print("3 - Read a file")

def menuGuest():
    print("-" * 20)
    print("Select an option")
    print("-" * 20)
    print("1 - Read a file")

signup()

conn.close()
quit()