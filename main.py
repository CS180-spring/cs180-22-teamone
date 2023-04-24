import json
import os
from Functions import *


def main():
    '''
    if not os.path.exists(DB_FILE_NAME):
        with open(DB_FILE_NAME, 'w') as file:
            json.dump([], file)
    '''


    while True:
        print('\nMenu')
        print('1. Create a DataBase')
        print('2. Switch Database')
        print('3. Create record')
        print('4. Read Record')
        print('5. Update record')
        print('6. Delete record')
        print('7. List records')
        print('8. Quit')
        
        choice = input(' Enter choice: ')
        
        if choice == '1':
            create_dataBase()

        if choice == '2':
            choose_database()

        if choice == '3':
            create_record()
        
        elif choice == '4':
            id = input('Enter ID: ')
            record = read_record(id)
            if record:
                print(record)
            else:
                print('Record not found')
        
        elif choice == '5':
            id = input("Enter ID: ")
            if update_record(id):
                print("Record updated")
            else:
                print("Record not found")
        
        elif choice == '6' :
            id = input("Enter ID: ")
            if delete_record(id):
                print('Record deleted')
            else:
                print("Record not found")
      
        elif choice == '7':
            list_records()
        
        elif choice == '8':
            break;

if __name__ == '__main__':
    main()