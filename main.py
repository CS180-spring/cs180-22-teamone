import json
import os


# One file for now change this to allow for multiple files. 
DB_FILE_NAME = 'data.json'

def create_record():
    data = {} # This is a dictionary 
    data['id'] = input("Enter ID: ")  # assign ID key to whatever the user inputs 
    
    for field in get_fields():   # calls get_Fields Function once and returns list 
        data[field] = input(f'Enter {field}: ') # This will print all fields then allow user to input data 
        
    with open(DB_FILE_NAME, 'r+') as file: # r+ gives permission to read and write 
        records = json.load(file) # Preps and loads into memory  
        records.append(data) # Go back to the top 
        file.seek(0) # takes us to the very top  
        json.dump(records, file, indent=4) # Here is where we write to json file  

def get_fields():
    fields = [] # similar to an array 
    while True:
        field = input("enter field name (or leave blank to finsih): ") # keep reading entries until empty 
        if not field: # loops through all entries 
            break
        fields.append(field) # Adds all elements the user input into the array fields 
    return fields

def read_record(id):
    with open(DB_FILE_NAME, 'r') as file:
        records = json.load(file)
        for record in records:
            if record['id'] == id:
                return record
        return None


def update_record(id):
    with open(DB_FILE_NAME, 'r+') as file:
        records = json.load(file)
        for i, record in enumerate(records):
            if record['id'] == id:
                for field in get_fields():
                    record[field] = input(f'Enter new {field}: ')
                records[i] = record
                file.seek(0)
                json.dump(records, file, indent=4)
                return True
        return False 

def delete_record():
    with open(DB_FILE_NAME, 'r+') as file:
        records = json.load(file) # taking all the data from json file put into records 
        for i, record in enumerate(records): # it will return index and object that it is pointing to 
            if record['id'] == id: 
                del records[i]
                file.seek(0)
                json.dump(records, file, indent=4)
                return True
        return False

def list_records():
    with open(DB_FILE_NAME, 'r') as file:
        records = json.load(file)
        for record in records:
            print(record)

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