import json
import os
from Functions import *


def main():
    while True:
        print('\nMenu')
        print('1. Create a DataBase')
        print('2. Current Database')
        print('3. Choose Database')
        print('4. Delete Database')
        print('5. Create record')
        print('6. Read Record')
        print('7. Update record')
        print('8. Delete record')
        print('9. List records')
        print('10. Create Database from CSV')
        print('11. Search Database')
        print('12. Quit')
        
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
        
        elif choice == '10':
            create_databaseCSV()

        elif choice == '11':
            record = searchCurrentDatabase()
            if record:
                print(record)
            else:
                print("No Records Found")
        
        elif choice == '12':
            
            break

if __name__ == '__main__':
    main()



