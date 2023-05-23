import json
import os
from Functions import *
from MainTwo import * 
from prettytable import PrettyTable


def main():
    while True:
        print('\nMenu')
        print('1. Create a Database') # create
        print('2. Current Database') # choose
        print('3. Choose Database') # choose
        print('4. Delete Database')
        print('5. Search Database') # choose
        print('6. Sort a database') # choose
        print('7. Export Database')
        print('8. Go to records')
        print('9. Quit')
        
        choice = input(' Enter choice: ')
        
        if choice == '1':
            createDatabase() # function below
        elif choice == '2':
            current_database() 
        elif choice == '3':
            choose_database()
        elif choice == '4':
            delete_database()
        elif choice == '5':
            searchDatabase() # function below
        elif choice == '6':
            sortDatabase()
        elif choice =='7':
            exportDatabase()
        elif choice == '8':
            recordMenu()
        else:
            quit()
            break


if __name__ == '__main__':
    main()

