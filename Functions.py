import json
import os



# One file for now change this to allow for multiple files. 
DB_FILE_NAME = 'data.json'

# Function to create records
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
        field = input("enter field name (or leave blank to finish): ") # Keep prompting for field input until empty
        if not field:
            break
        fields.append(field)
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
