import json
import os
from Functions import *


def main():
    if not os.path.exists(DB_FILE_NAME):
        with open(DB_FILE_NAME, 'w') as file:
            json.dump([], file)
            
    while True:
        print('\nMenu')
        print('1. Create record')
        print('2. Read Record')
        print('3. Update record')
        print('4. Delete record')
        print('5. List records')
        print('6. Quit')
        
        choice = input('\Enter choice: ')
        
        if choice == '1':
            create_record()
        
        elif choice == '2':
            id = input('Enter ID: ')
            record = read_record(id)
            if record:
                print(record)
            else:
                print('Record not found')
        
        elif choice == '3':
            id = input("Enter ID: ")
            if update_record(id):
                print("Record updated")
            else:
                print("Record not found")
        
        elif choice == '4' :
            id = input("Enter ID: ")
            if delete_record(id):
                print('Record deleted')
            else:
                print("Record not found")
        elif choice == '5':
            list_records()
        
        elif choice == '6':
            break;

if __name__ == '__main__':
    main()