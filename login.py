import os
import json

from Functions import *
from databaseMenu import *
import shutil
import hashlib

def displayMenu(users):
    print("LOGIN MENU")
    print("1. Create User\n")
    print("2. Log In\n")
    print("3. Reset Password\n")
    print("4. Exit")
    choice = input("Please Select your option: ")

    if (choice == "1"):
        username = input("Username: ")

        if username in users:
            print("\nUsername Already Exists!\n")
        else:
            password = hash_password(input("Password: "))
            security_questions = getSecurityQuestions()
            users[username] = {'password': password, 'security_questions': security_questions}
            print("User Created!")
            save_users(users)

    elif (choice == "2"):
        username = input("Enter Username: ")
        password = hash_password(input("Enter Password: "))

        if username in users and users[username]['password'] == password:
            print("\nLogin Successful\n")
            mainMenu()
        else:
            print("\nUser Doesn't Exist // Wrong Password\n")

    elif (choice == "3"):
        username = input("Enter Username: ")
        if username in users:
            if validateSecurityQuestions(users[username]['security_questions']):
                new_password = hash_password(input("Enter new password: "))
                users[username]['password'] = new_password
                print("Password has been reset!")
                save_users(users)
            else:
                print("\nSecurity Question Validation Failed!\n")
        else:
            print("\nUser Doesn't Exist\n")

    elif (choice == "4"):
        exit()
