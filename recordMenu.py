from Functions import *

def createDatabase():
    print('1. Manually input Database')
    print('2. Import Database from CsV')
    choice = input(' Enter choice: ')

    if choice == '1':
        create_dataBase()
    else:
        create_databaseCSV()

def searchDatabase():
    print('1. Search current database')
    print('2. Search all databases')
    choice = input(' Enter choice: ')

    if choice == '1':
        searchCurrentDatabase()
    else:
        searchThroughAllDatabases()

def exportDatabase():
    print('1. Export database to CSV')
    print('2. Backup a database')
    choice = input(' Enter choice: ')

    if choice == '1':
        export_databaseCSV()
    else:
        search_and_backup_json()

def recordMenu():
    while True:
        print("Record Menu")
        print("1. Create Record")
        print("2. Read Record")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. List Record")
        print("6. List Record by Field")
        print("7. Return to Database Menu")

        choice = input(' Enter choice: ')

        if choice == '1':
            create_record()
        elif choice == '2':
            read_record()
        elif choice == '3':
            update_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            list_records()
        elif choice == '6':
            listField()
        else:
            break



     