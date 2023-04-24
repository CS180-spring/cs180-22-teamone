import json  # import the json module to work with JSON data
import os   # import the os module for operating system dependent functionality

# One file for now change this to allow for multiple files. 
DB_FILE_NAME = ''  # define the name of the file where records will be stored
EXISTING_DATA_BASES = []



# Function to create records
def create_record():
    if len(DB_FILE_NAME) == 0:
        print("Error: No DataBase Selected")
        return 

    data = {}  # create an empty dictionary to store the data for a new record
    data['id'] = input("Enter ID: ")  # prompt the user to input the ID for the new record and store it in the 'id' key of the dictionary
    
    for field in get_fields():  # iterate over the fields returned by the get_fields function
        data[field] = input(f'Enter {field}: ')  # prompt the user to input the data for each field and store it in the corresponding key of the dictionary
        
    with open(DB_FILE_NAME, 'r+') as file:  # open the data file in read-write mode using a 'with' statement
        records = json.load(file)  # load the existing records from the file into the 'records' list
        records.append(data)  # add the new record (stored in the 'data' dictionary) to the 'records' list
        file.seek(0)  # move the file pointer to the beginning of the file
        json.dump(records, file, indent=4)  # write the updated records list to the file in JSON format with indentation
 
        
def get_fields():
    fields = []  # create an empty list to store the field names
    while True:
        field = input("enter field name (or leave blank to finish): ")  # prompt the user to input a field name or leave it blank to finish
        if not field:
            break  # if the user leaves the field name blank, break out of the loop
        fields.append(field)  # add the field name to the 'fields' list
    return fields  # return the list of field names


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

def create_dataBase():
    exit_loop = False
    while not exit_loop:
        new_file = input("Type name of new Data Base you want to create: ")
        for file_name in EXISTING_DATA_BASES:
            if new_file == file_name:
                print("Sorry, this name is already in use, use another")
                break
        else:
            exit_loop = True

    with open("ExistingDataBases.txt", "w") as file:
        file.write(new_file)

    DB_FILE_NAME = new_file + '.json'
    EXISTING_DATA_BASES.append(DB_FILE_NAME)
    

def choose_database():
    
    return 
