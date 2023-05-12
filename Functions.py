import csv # import the CSV files
import json  # import the json module to work with JSON data
import os   # import the os module for operating system dependent functionality

# One file for now change this to allow for multiple files. 
DB_FILE_NAME = ''  # define the name of the file where records will be stored
EXISTING_DATA_BASES = []



# Function to create records
def create_record(): # option 5
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


def read_record(id): # option 6
    global DB_FILE_NAME
    with open(DB_FILE_NAME, 'r') as file:
        records = json.load(file)
        for record in records:
            if record['id'] == id:
                return record
        return None


def update_record(id): # option 7
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

def delete_record(id): # option 8
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

def list_records(): # option 9
    global DB_FILE_NAME
    with open(DB_FILE_NAME, 'r') as file:
        records = json.load(file)
        for record in records:
            print(record)
    return records #purely for unit testing purposes. This should not affect the end user's performance

def create_dataBase(): # option 1
    global DB_FILE_NAME, EXISTING_DATA_BASES
    EXISTING_DATA_BASES.clear()

    #We  clear then add all elements inside of EXISTING_DATA_BASES
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


def current_database(): # option 2
    global DB_FILE_NAME
    temp = DB_FILE_NAME[:-5]
    print("Current Database: "+ temp) 


def choose_database(): # option 3
    global DB_FILE_NAME
    with open('ExistingDataBases.txt', 'r') as f:
        for line_number, line in enumerate(f, start=1):
            print(f"{line_number}: {line[:-6]}\n")
    
    userInput = input("Type name of Database: ")
    #handle error for checking if data base exists later 
    DB_FILE_NAME = userInput + '.json'


def delete_database(): # option 4
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

def create_databaseCSV(): # option 10
    global DB_FILE_NAME, EXISTING_DATA_BASES

    EXISTING_DATA_BASES.clear()

    #We  clear then add all elements inside of EXISTING_DATA_BASES
    with open("ExistingDataBases.txt", "r") as file:
        file.seek(0)
        for line in file:
            EXISTING_DATA_BASES.append(line.strip())

    # gets user input to the CSV file
    exitLoop = False
    while not exitLoop:
        fileName = input("Enter CSV file: ") 
        if not fileName: # checks for no input
            print("Database not created")
        # csvFile = fileName + '.csv'
        # tempJson = fileName + '.json'
        else:
            csvFile = fileName + '.csv'
            tempJson = fileName + '.json'
            # checks if files dont already exist in database
            if len(EXISTING_DATA_BASES) == 0:
                exitLoop = True
            for existingFiles in EXISTING_DATA_BASES:
                if tempJson == existingFiles:
                    print("This CSV file has already been converted, pick another.")
                    break
                else:
                    exitLoop = True

    # checks if the CSV file exists in the OS directory
    if os.path.exists(csvFile):

        # open and read the current CSV file 
        with open(csvFile, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            # create empty list for data population from CSV file
            csvData = []

            # adds each row from CSV to list
            for eachRow in csv_reader:
                csvData.append(eachRow)

            # writes the list to the json file
            jsonFile = fileName + ".json"
            with open(jsonFile, 'w') as json_file:
                json.dump(csvData, json_file, indent=4)
        

        with open("ExistingDataBases.txt", "w") as file:
            file.write(jsonFile)
        
        # DB_FILE_NAME = jsonFile 
        # with open(DB_FILE_NAME, 'w') as file:
        #     json.dump([], file)
        
        EXISTING_DATA_BASES.append(jsonFile)
    
        with open('ExistingDataBases.txt', 'w') as f:
            f.seek(0)
            for index in EXISTING_DATA_BASES:
                f.write(index + '\n')

    else:
        print("CSV File does not exist!")
 
       
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
    
def searchThroughAllDatabases():
    AllRecords = []
    
    key = input("Name of Value to search for: ")
    value = input("Value to search for: ")
    
    with open("ExistingDataBases.txt", "r") as file:
        file.seek(0)
        for line in file:
            EXISTING_DATA_BASES.append(line.strip())
    for i, filename in enumerate(EXISTING_DATA_BASES):
        with open(filename, 'r') as file:
            records = json.load(file)
            for record in records:
                if key in record and record[key] == value:
                    AllRecords.append(record)
    return AllRecords

def searchJsonFile():
    keyWord = input("Enter the keyword to search thru all json files: ")
    # print(EXISTING_DATA_BASES)
    for jsonFile in EXISTING_DATA_BASES:
        with open(jsonFile, 'r') as file:
            jsonData = json.load(file)
            if keyWord in json.dumps(jsonData):
                return jsonFile
    return None

def sortDatabase():
    if len(EXISTING_DATA_BASES) == 0:
        return

    for existingFiles in EXISTING_DATA_BASES:
        # existingFiles = existingFiles - ".json"
        print ("These are the existing databases:", existingFiles)

    userFile = input("Which database will you like to sort? ")
    userFile = userFile + ".json"

    with open(userFile, 'r') as file:
        jsonData = json.load(file)

    if jsonData:
        fileKeys = list(jsonData[0].keys())
        keyStrings = ', ' .join(fileKeys)
        print("These are the available keys.", keyStrings)
        userKey = input("Pick a key to modify/sort: ")

    sortedData = sorted(jsonData, key=lambda x: x[userKey])

    with open(userFile, 'w',) as sortedFile:
        json.dump(sortedData, sortedFile, indent=4)
    