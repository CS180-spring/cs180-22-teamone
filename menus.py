import csv # import the CSV files
import json  # import the json module to work with JSON data
import os   # import the os module for operating system dependent functionality
from prettytable import PrettyTable
import hashlib
import shutil
import tkinter as tk
import smtplib
from email.message import EmailMessage
import ssl # for protecting sensitive data 
#from prettytable import prettytable
import getpass
import random
from Functions import *
import main
users = load_users()


def userMenu(users):
    print( '''

 ██████╗ ███╗   ██ ███████╗    ██████╗██████╗ 
██╔═══██ ████╗  ██ ██╔════╝    ██╔══██ ██╔══██╗
██║   ██ ██╔██╗ ██ █████╗      ██║  ██ ██████╔╝
██║   ██ ██║╚██╗██ ██╔══╝      ██║  ██ ██╔══██╗
╚██████╔ ██║ ╚████ ███████╗    ██████╔██████╔╝
 ╚═════╝╚═╝    ╚═══╚══════╝    ╚═════╝╚═════╝ 
                                            

''')
    print("╔══════════════════════════════╗")
    print("║         LOGIN MENU           ║")
    print("║══════════════════════════════║")
    print("║ 1. Create User               ║")
    print("║ 2. Log In                    ║")
    print("║ 3. Reset Password            ║")
    print("║ x. Exit                      ║")
    print("╚══════════════════════════════╝")
    choice = input("\nPlease Select your option: ")

   
    if (choice == "1"):
        username = input("Username: ")
        if username in users:
            print("\nUsername Already Exists!\n")
            userMenu(users)
           
        else:
            email = input("Email: ")
            for user in users.values():
                if user['email'] == email:
                    print("Email Already In Use!\n Please use another\n")
                    userMenu(users)

            password = hash_password(input("Password: "))
            security_questions = getSecurityQuestions()
            permissions = 'admin'
            users[username] = {'username': username, 'password': password, 'security_questions': security_questions, 'email': email, 'permissions': permissions}
            print("User Created!")
            save_users(users)

    elif (choice == "2"):
        users = load_users() #updates the userMenu every time it is run, in case user permissions were changed.
        username = input("Enter Username: ")
        password = hash_password(input("Enter Password: "))

        if username in users and users[username]['password'] == password:
            print("\nLogin Successful\n")
            if(users[username]['permissions'] == 'admin'):
                mainMenu()
            if(users[username]['permissions'] == 'edit'):
                editMenu()
            if(users[username]['permissions'] == 'view'):
                viewMenu()
        else:
            print("\nUser Doesn't Exist // Wrong Password\n")
            userMenu(users)

    elif (choice == "3"):
        print("How would you like to recover your password?\n1. Send Pasword Recover via email\n2. Input Security Questions")
        temp = input()
        
        # User wants to Sends Password Recovery 
        if(temp == "1"):
            username = input("Enter Username: ")
            email = input("Enter Email: ").strip()
            
            with open('users.json') as file:
                data = json.load(file)
            
            if username in data and data[username]['email'] == email:
                print("Account Found")
                sendRecoveryEmail(email,users,username)
                userMenu(users)
                
            else:
                print("Account not found,try again\b")
                userMenu(users)

        # Security Question Password Recovery    
        else:
             username = input("Username: ")
             if username in users:
                if validateSecurityQuestions(users[username]['security_questions']):
                    new_password = hash_password(input("Please enter new password: "))
                    users[username]['password'] = new_password
                    print("Password has been reset!")
                    save_users(users)
                else:
                    print("\nSecurity Question Validation Failed!\n")
             else:
                print("\nUser Doesn't Exist\n")

    elif (choice >= "x"):
        print('''
                ██████████╗  ██╗ █████╗ ███╗   ██ ██╗  ██╗    ██╗   ██╗██████╗ ██╗   ██╗                          
                ╚══██╔══██║  ██ ██╔══██ ████╗  ██ ██║ ██╔╝    ╚██╗ ██╔██╔═══██ ██║   ██║                          
                   ██║  ███████ ███████ ██╔██╗ ██ █████╔╝      ╚████╔╝██║   ██ ██║   ██║                          
                   ██║  ██╔══██ ██╔══██ ██║╚██╗██ ██╔═██╗       ╚██╔╝ ██║   ██ ██║   ██║                          
                   ██║  ██║  ██ ██║  ██ ██║ ╚████ ██║  ██╗       ██║  ╚██████╔╚ ██████╔╝                          
                   ╚═╝  ╚═╝  ╚═ ╚═╝  ╚═ ╚═╝  ╚═══ ╚═╝  ╚═╝       ╚═╝   ╚═════╝ ╚═════╝                           
███████╗██████╗ ██████╗     ██╗   ██ ███████ ██ ███╗   ██╗ ██████╗      ██████╗ ███╗   ██ ███████╗    ██████╗██████╗ 
██╔════██╔═══██ ██╔══██╗    ██║   ██ ██╔════ ██ ████╗  ██ ██╔════╝     ██╔═══██ ████╗  ██ ██╔════╝    ██╔══██ ██╔══██╗
█████╗ ██║   ██ ██████╔╝    ██║   ██ ███████ ██ ██╔██╗ ██ ██║  ███╗    ██║   ██ ██╔██╗ ██ █████╗      ██║  ██ ██████╔╝
██╔══╝ ██║   ██ ██╔══██╗    ██║   ██ ╚════██ ██ ██║╚██╗██ ██║   ██║    ██║   ██ ██║╚██╗██ ██╔══╝      ██║  ██ ██╔══██╗
██║    ╚██████╔ ██║  ██║    ╚██████╔ ███████ ██ ██║ ╚████╚ ██████╔╝    ╚██████╔ ██║ ╚████ ███████╗    ██████╔██████╔╝
╚═╝     ╚═════╝ ╚═╝  ╚═╝     ╚═════╝╚══════╚═╚═╝     ╚═══╝╚═════╝       ╚═════╝ ╚═╝  ╚═══ ╚══════╝    ╚═════╝╚═════╝ 
                                                                                                              
''')
        exit()

emailSender = "DataBaseTeamOne@gmail.com"
# emailSenderPassword = os.environ.get("EMAIL_PASSWORD")
emailSenderPassword = "qnajzmjpwjthpzky"

def sendRecoveryEmail(emailReciever,users,username):
    subject = "Data Base Password Recovery"

    randomCode = generateCode()
    #print("Random Code: ",randomCode)

    mainBody = """
            We received a request to reset your password for your account.
            If you did not initiate this request, please ignore this message.
            To reset your password, type in the randomly generated code in the
            Data Base Program below.  
             
            Code: """
    
    body = mainBody + randomCode
    
    em = EmailMessage()  # Create an instance of the class
    em['From'] = emailSender
    em['To'] = emailReciever
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(emailSender, emailSenderPassword)
        smtp.sendmail(emailSender, emailReciever, em.as_string())
        print("Recovery Code Sent")
    
    userInput = input("Enter the Recovery Code: ")
    #print("userInput = ", userInput, "and randomCode = ", randomCode)

    if(userInput == randomCode):
        print("Match!")
        new_password = hash_password(input("Please enter new password: "))
        users[username]['password'] = new_password
        print("Password has been reset!")
        save_users(users)
    
    else:
        print("Code does not match")


def databaseMenu():
    while True:
        print('''
╔══════════════════════════════════════╗
║              Menu                    ║
║══════════════════════════════════════║ 
║ 1. Create a DataBase                 ║
║ 2. Current Database                  ║
║ 3. Choose Database                   ║
║ 4. Delete Database                   ║
║ x. Log Out                           ║
╚══════════════════════════════════════╝
    ''')
        
        
        
        choice = input(' Enter choice: ')
        
        
        if choice == '1':
            create_dataBase()

        if choice == '2':
            current_database()

        if choice == '3':
            
            choose_database()
            
            crudMenu()
            

        if choice == '4':          
            delete_database()
        
        if choice == 'x':
            break
        
        
def MoreOptions():
    while True:
        
        print('''
╔══════════════════════════════════════════════════════════╗
║ 12. Create Database from CSV                             ║
║ 13. Export Current Database to CSV                       ║
║ 14. Search Database                                      ║
║ 15. Search All Databases                                 ║
║ 16. Search json file using keyword                       ║
║ 17. Sort a database                                      ║
║ 18. Display Table                                        ║
║ 19. Backup Database                                      ║
║ 20. Change User Permissions                              ║
║ x. Back                                                  ║
╚══════════════════════════════════════════════════════════╝
    ''')
        choice = input(' Enter choice: ')
        
        if choice == '12':
            create_databaseCSV()
            
        
        elif choice == '13':
            export_databaseCSV()
        elif choice == '14':
            record = searchCurrentDatabase()
            if record:
                print(record)
            else:
                print("No Records Found!")

        elif choice =='15':
            record = searchThroughAllDatabases()
            if record:
                print(record)
            else:
                print("No Records Found!")
        
        elif choice == '16':
            fileFound = searchJsonFile()
            if fileFound:
                print("File found with keyword in:", fileFound)
            else:
                print("File not found with keyword, try another.")

        elif choice == '17':
            sortDatabase()

        elif choice == '18':
            display_table()

        elif choice == '19':
            search_and_backup_json()
   
        elif choice == '20':
            chooseUserPermissions(users)
        elif choice == 'x':
            break
        else:
            break
        
        
        
        
def crudMenu():
    while True:
        print('''
╔══════════════════════════════════╗
║ 5.  Create record                ║
║ 6.  Read Record                  ║
║ 7.  Update record                ║
║ 8.  Delete record                ║
║ 9.  List records                 ║
║ 10. List by field                ║
║ 11. More Options                 ║
║ x.  Back                         ║
╚══════════════════════════════════╝
    ''')
        
        choice = input(' Enter choice: ')

        if choice == '5':          
            create_record()
        
        elif choice == '6':
            id = input('Enter ID: ')
            record = read_record(id)
            if record:
                print(record)
            else:
                print('Record not found')
        
        elif choice == '7':
            id = input("Enter ID: ")
            if update_record(id):
                print("Record updated")
            else:
                print("Record not found")
        
        elif choice == '8' :
            id = input("Enter ID: ")
            if delete_record(id):
                print('Record deleted')
            else:
                print("Record not found")
        elif choice == '9':
            list_records()
        
        elif choice =='10':
            listField()
        
        elif choice == '11':
            MoreOptions()
        elif choice == 'x':
            break
    


        
        


def mainMenu():
        databaseMenu()



def editMenu():
    while True:
        print('''
╔════════════════════════════════════════════════════════╗
║                     Menu                               ║
╠════════════════════════════════════════════════════════╣
║ 1.  Create a DataBase                                  ║
║ 2.  Current Database                                   ║
║ 3.  Choose Database                                    ║
║ 4.  Delete Database                                    ║
║ 5.  Create record                                      ║
║ 6.  Read Record                                        ║
║ 7.  Update record                                      ║
║ 8.  Delete record                                      ║
║ 9.  List records                                       ║
║ 10. List by field                                      ║
║ 11. Create Database from CSV                           ║
║ 12. Export Current Database to CSV                     ║
║ 13. Search Database                                    ║
║ 14. Search All Databases                               ║
║ 15. Search json file using keyword                     ║
║ 16. Sort a database                                    ║
║ 17. Display Table                                      ║
║ 18. Backup Database                                    ║
║ 19. Quit                                               ║
╚════════════════════════════════════════════════════════╝
    ''')
        
        choice = input(' Enter choice: ')
        
        if choice == '1':
            create_dataBase()

        if choice == '2':
            current_database()

        if choice == '3':
            choose_database()

        if choice == '4':          
            delete_database()

        if choice == '5':          
            create_record()
        
        elif choice == '6':
            id = input('Enter ID: ')
            record = read_record(id)
            if record:
                print(record)
            else:
                print('Record not found')
        
        elif choice == '7':
            id = input("Enter ID: ")
            if update_record(id):
                print("Record updated")
            else:
                print("Record not found")
        
        elif choice == '8' :
            id = input("Enter ID: ")
            if delete_record(id):
                print('Record deleted')
            else:
                print("Record not found")
      
        elif choice == '9':
            list_records()
        
        elif choice =='10':
            listField()

        elif choice == '11':
            create_databaseCSV()

        elif choice == '12':
            export_databaseCSV()

        elif choice == '13':
            record = searchCurrentDatabase()
            if record:
                print(record)
            else:
                print("No Records Found!")

        elif choice =='14':
            record = searchThroughAllDatabases()
            if record:
                print(record)
            else:
                print("No Records Found!")
        
        elif choice == '15':
            fileFound = searchJsonFile()
            if fileFound:
                print("File found with keyword in:", fileFound)
            else:
                print("File not found with keyword, try another.")

        elif choice == '16':
            sortDatabase()

        elif choice == '17':
            display_table()

        elif choice == '18':
            search_and_backup_json()

        elif choice == '19':
            break
        else:
            break




def viewMenu():
    while True:
        print('''
╔════════════════════════════════════════════════════════╗
║                     Menu                               ║
╠════════════════════════════════════════════════════════╣
║ 1.  Current Database                                   ║
║ 2.  Choose Database                                    ║
║ 3.  Read Record                                        ║
║ 4.  List records                                       ║
║ 5.  List by field                                      ║
║ 6.  Export Current Database to CSV                     ║
║ 7.  Search Database                                    ║
║ 8.  Search All Databases                               ║
║ 9.  Search json file using keyword                     ║
║ 10. Sort a database                                    ║
║ 11. Display Table                                      ║
║ 12. Backup Database                                    ║
║ 13. Quit                                               ║
╚════════════════════════════════════════════════════════╝
    ''')
        
        choice = input(' Enter choice: ')
        
    
        if choice == '1':
            current_database()

        if choice == '2':
            choose_database()
        
        if choice == '3':
            id = input('Enter ID: ')
            record = read_record(id)
            if record:
                print(record)
            else:
                print('Record not found')
        if choice == '4':
            list_records()
        
        elif choice =='5':
            listField()

        elif choice == '6':
            export_databaseCSV()

        elif choice == '7':
            record = searchCurrentDatabase()
            if record:
                print(record)
            else:
                print("No Records Found!")

        elif choice =='8':
            record = searchThroughAllDatabases()
            if record:
                print(record)
            else:
                print("No Records Found!")
        
        elif choice == '9':
            fileFound = searchJsonFile()
            if fileFound:
                print("File found with keyword in:", fileFound)
            else:
                print("File not found with keyword, try another.")

        elif choice == '10':
            sortDatabase()

        elif choice == '11':
            display_table()

        elif choice == '12':
            search_and_backup_json()
            
        elif choice == '13':
            break
        else:
            break