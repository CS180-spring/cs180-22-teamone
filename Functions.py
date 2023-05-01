import json  # import the json module to work with JSON data
import os   # import the os module for operating system dependent functionality

# One file for now change this to allow for multiple files. 
DB_FILE_NAME = ''  # define the name of the file where records will be stored
EXISTING_DATA_BASES = []



# Function to create records
def create_record():
    global DB_FILE_NAME
    print("Name of Current Data base: ", DB_FILE_NAME)
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
    global DB_FILE_NAME
    fields = []  # create an empty list to store the field names
    while True:
        field = input("enter field name (or leave blank to finish): ")  # prompt the user to input a field name or leave it blank to finish
        if not field:
            break  # if the user leaves the field name blank, break out of the loop
        fields.append(field)  # add the field name to the 'fields' list
    return fields  # return the list of field names


def read_record(id):
    global DB_FILE_NAME
    with open(DB_FILE_NAME, 'r') as file:
        records = json.load(file)
        for record in records:
            if record['id'] == id:
                return record
        return None


def update_record(id):
    global DB_FILE_NAME
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

def delete_record(id):
    global DB_FILE_NAME
    with open(DB_FILE_NAME, 'r+') as file:
        records = json.load(file) # taking all the data from json file put into records 
        for i, record in enumerate(records): # it will return index and object that it is pointing to 
            if record['id'] == id: 
                del records[i]
                file.seek(0)
                file.truncate(0)
                json.dump(records, file, indent=4)
                return True
        return False

def list_records():
    global DB_FILE_NAME
    with open(DB_FILE_NAME, 'r') as file:
        records = json.load(file)
        for record in records:
            print(record)

def create_dataBase():
    global DB_FILE_NAME, EXISTING_DATA_BASES
    EXISTING_DATA_BASES.clear()

    #We  clear then add all ements inside of EXISTING_DATA_BASES
    with open("ExistingDataBases.txt", "r") as file:
        file.seek(0)
        for line in file:
            EXISTING_DATA_BASES.append(line.strip())

    # Temporary test file
    for db in EXISTING_DATA_BASES:
        print("DataBase: ", db)

    exit_loop = False
    while not exit_loop:
        new_file = input("Type name of new Data Base you want to create: ")    
        if not new_file: # Check if user typed nothing 
            print("Database not created")
            break
        new_file = new_file + '.json' 
        
        for file_name in EXISTING_DATA_BASES: # Check if name already used           
            if new_file == file_name:
                print("Sorry, this name is already in use, please use another")
                break
        else:
            exit_loop = True

    with open("ExistingDataBases.txt", "w") as file:
        file.write(new_file)
    
    DB_FILE_NAME = new_file 
    with open(DB_FILE_NAME, 'w') as file:
        json.dump([], file)
    
    EXISTING_DATA_BASES.append(DB_FILE_NAME)
    
    with open('ExistingDataBases.txt', 'w') as f:
        f.seek(0)
        for index in EXISTING_DATA_BASES:
            f.write(index + '\n')


def current_database():
    global DB_FILE_NAME
    temp = DB_FILE_NAME[:-5]
    print("Current Database: "+ temp) 


def choose_database():
    global DB_FILE_NAME
    with open('ExistingDataBases.txt', 'r') as f:
        for line_number, line in enumerate(f, start=1):
            print(f"{line_number}: {line[:-6]}\n")
    
    userInput = input("Type name of Database: ")
    #handle error for checking if data base exists later 
    DB_FILE_NAME = userInput + '.json'


def delete_database():
    global DB_FILE_NAME, EXISTING_DATA_BASES

    # update EXISTING_DATA_BASES list variable
    with open("ExistingDataBases.txt", "r") as file:
        EXISTING_DATA_BASES = [line.strip() for line in file]

    #print("Before Deleting: ")
    #for db in EXISTING_DATA_BASES:
        #print(db)

    # delete the .json file
    temp = input("Type name of Database you want to delete: ")
    temp += ".json"
    if temp in EXISTING_DATA_BASES:
        EXISTING_DATA_BASES.remove(temp)
        os.remove(temp)
        print("Database successfully deleted")
    else:
        print("Database does not exist")

   #print("After Deleting:")
    #for db in EXISTING_DATA_BASES:
     #   print(db)

    # update ExistingDataBases.txt
    with open("ExistingDataBases.txt", "w") as file:
        for db in EXISTING_DATA_BASES:
            file.write(db + "\n")



def searchCurrentDatabase():
    key = input("Name of Value to search for: ")
    value = input("Value to search for: ")
    
    foundRecords = []
    
    global DB_FILE_NAME
    with open(DB_FILE_NAME, 'r') as file:
        records = json.load(file)
        for record in records:
            if key in record and record[key] == value:
                foundRecords.append(record)
        return foundRecords
    

    
    
    
