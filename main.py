import json
import os


# One file for now change this to allow for multiple files. 
DB_FILE_NAME = 'data.json'

def create_record():
    data = {}
    data['id'] = input("Enter ID: ")
    
    for field in get_fields():
        data[field] = input(f'Enter {field}: ')
        
    with open(DB_FILE_NAME, 'r+') as file:
        records = json.load(file)
        records.append(data)
        file.seek(0)
        json.dump(records, file, indent=4)

def get_fields():
    fields = []
    while True:
        field = input("enter field name (or leave blank to finsih): ")
        if not field:
            break
        field.append(field)
    return fields

def read_record(id):
    pass


def update_record(id):
    pass

def delete_record():
    pass

def list_records():
    pass

def main():
    if not os.path.exists(DB_FILE_NAME):
        with open(DB_FILE_NAME, 'w') as file:
            json.dump([], file)
    
    while