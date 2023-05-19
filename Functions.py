import csv # import the CSV files
import json  # import the json module to work with JSON data
import os   # import the os module for operating system dependent functionality
from prettytable import PrettyTable
import hashlib
import shutil
#from prettytable import prettytable


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
                confirm = input(f"Are you sure you want to delete the record with ID '{id}'? (y/n): ")
                if confirm.lower() == 'y':
                    del records[i]
                    file.seek(0)
                    file.truncate(0)
                    json.dump(records, file, indent=4)
                    return True
                else:
                    return False
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
    # Print all Data Bases Currently Created 
    with open('ExistingDataBases.txt', 'r') as f:
        for line_number, line in enumerate(f, start=1):
            print(f"{line_number}: {line[:-6]}\n")
    
    userInput = input("Type name of Database: ")
    userInput += '.json'
    found = False

    #check if there is a data base the user input exists or not 
    with open('ExistingDataBases.txt', 'r') as f:
        for line in f.readlines():
            if userInput == line.strip():
                found = True

    if not found: 
         print(f"Error: No DataBase under the name {userInput[:-5]} was found")
         return
    
    DB_FILE_NAME = userInput


def delete_database(): # option 4
    global DB_FILE_NAME, EXISTING_DATA_BASES

    # update EXISTING_DATA_BASES list variable
    with open("ExistingDataBases.txt", "r") as file:
        EXISTING_DATA_BASES = [line.strip() for line in file]

    # delete the .json file
    temp = input("Type name of Database you want to delete: ")
    temp += ".json"
    if temp in EXISTING_DATA_BASES:
        EXISTING_DATA_BASES.remove(temp)
        os.remove(temp)
        print("Database successfully deleted")
    else:
        print("Database does not exist")

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
 

def export_databaseCSV():
    global DB_FILE_NAME

    if len(DB_FILE_NAME) == 0:
        print('Database not selected. Please choose one before exporting')
        raise Exception('Database not selected. Please choose one before exporting')
 
        
    with open(DB_FILE_NAME, 'r') as file:  #loads current database into data array
        data = json.load(file)
    filename = DB_FILE_NAME[:-5]   #finds name of file (removes the .json part of the string)
    filename = filename + '.csv'   #appends .csv to make the file a .csv

    if os.path.exists(filename):  #if a file already exists, engage duplicate protocol
        filename = filename[:-4]   #removes .csv
        filename = filename + '(1).csv'  #adds (1) to the end. Would like to add functionality to increment a counter instead of just appending (1) all the time but oh well)
     
    with open(filename, 'w', newline='') as file: #creates a new csv file with name
        writer = csv.writer(file)
        writer.writerow(data[0].keys()) #writes in the keys as the header
        for row in data:
            writer.writerow(row.values()) #writes in the rows as data
    print('Database successfully exported. Check filepath for CSV') #visual confirmation for user

       
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
    
    return AllRecords 
                    

def listField():
    global DB_FILE_NAME
    
    if len(DB_FILE_NAME) == 0:
        print("Error: No Databse Selected")
        return
    found = False

    print("This functions to show all data on some specfied Field in your Data Base")
    userInput = input("Insert Field: ")
    
    with open(DB_FILE_NAME, 'r') as file:
        records = json.load(file)
        for record in records:
            if userInput in record:
                print(userInput,": ",record[userInput])
                found = True
            
    if not found: 
         print(f"No data under the field name {userInput} was found")

    
def hash_password(password):
    sha_signature = hashlib.sha256(password.encode()).hexdigest()
    return sha_signature

def save_users(users):
    with open('users.json', 'w') as f:
        json.dump(users, f)

def load_users():
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as f:
            users = json.load(f)
    else:
        users = {}
    return users

def displayMenu(users):
    print("LOGIN MENU")
    print("1. Create User\n")
    print("2. Log In\n")
    print("3. Reset Password\n")
    print("4. Exit")
    choice = input("Please Select your option: ")

    if (choice == "1"):
        username = input("Username: ")

        if username in users:
            print("\nUsername Already Exists!\n")
        else:
            password = hash_password(input("Password: "))
            security_questions = getSecurityQuestions()
            permissions = 'edit'
            users[username] = {'password': password, 'security_questions': security_questions, 'permissions': permissions}
            print("User Created!")
            save_users(users)

    elif (choice == "2"):
        username = input("Enter Username: ")
        password = hash_password(input("Enter Password: "))

        if username in users and users[username]['password'] == password:
            print("\nLogin Successful\n")
            mainMenu()
        else:
            print("\nUser Doesn't Exist // Wrong Password\n")

    elif (choice == "3"):
        username = input("Enter Username: ")
        if username in users:
            if validateSecurityQuestions(users[username]['security_questions']):
                new_password = hash_password(input("Enter new password: "))
                users[username]['password'] = new_password
                print("Password has been reset!")
                save_users(users)
            else:
                print("\nSecurity Question Validation Failed!\n")
        else:
            print("\nUser Doesn't Exist\n")

    elif (choice == "4"):
        exit()


def getSecurityQuestions():
    questions = [
        "Security Question 1: Where were you born?",
        "Security Question 2: What is your favorite meal?",
        "Security Question 3: What city did your parents meet?"
    ]
    answers = {}
    for question in questions:
        answers[question] = input(question + ': ')
    return answers

def validateSecurityQuestions(security_questions):
    for question, answer in security_questions.items():
        user_answer = input(question + ': ')
        if user_answer != answer:
            return False
    return True


def chooseUserPermissions():
    print("Choose User to change permissions: ")
    counter = 1
    with open('users.json', 'r') as file:
        userList = json.load(file)
        for user in userList:
            print(str(counter) + ". " + user)
            counter += 1
    username = input("Choose User to change permissions:")
    print("Choose the permission to change to: ")
    print("1. Admin")
    print ("2. Editor")
    print("3. Viewer")
    with open('users.json', 'r+') as file:
        userList = json.load(file)
    
def mainMenu():
    while True:
        print('\nMenu')
        print('1. Create a DataBase')
        print('2. Current Database')
        print('3. Choose Database')
        print('4. Delete Database')
        print('5. Create record')
        print('6. Read Record')
        print('7. Update record')
        print('8. Delete record')
        print('9. List records')
        print ('10. List by field')
        print('11. Create Database from CSV')
        print('12. Export Current Database to CSV')
        print('13. Search Database')
        print('14. Search All Databases')
        print('//WIP: 15. Display Table')
        print('16. Quit')
        
        choice = input(' Enter choice: ')
        
        if choice == '1':
            create_dataBase()

        if choice == '2':
            current_database()

        if choice == '3':
            choose_database()

        if choice == '4':          
            delete_database()

        if choice == '5':          
            create_record()
        
        elif choice == '6':
            id = input('Enter ID: ')
            record = read_record(id)
            if record:
                print(record)
            else:
                print('Record not found')
        
        elif choice == '7':
            id = input("Enter ID: ")
            if update_record(id):
                print("Record updated")
            else:
                print("Record not found")
        
        elif choice == '8' :
            id = input("Enter ID: ")
            if delete_record(id):
                print('Record deleted')
            else:
                print("Record not found")
      
        elif choice == '9':
            list_records()
        
        elif choice =='10':
            listField()

        elif choice == '11':
            create_databaseCSV()

        elif choice == '12':
            export_databaseCSV()

        elif choice == '13':
            record = searchCurrentDatabase()
            if record:
                print(record)
            else:
                print("No Records Found!")

        elif choice =='14':
            record = searchThroughAllDatabases()
            if record:
                print(record)
            else:
                print("No Records Found!")
        
      
        elif choice == '16':
            break
            
def display_table():
    with open(DB_FILE_NAME, 'r') as file:
        records = json.load(file)
        table = prettytable(['ID', 'Name', 'Age', 'Major'])
        for row in records:
            table.add_row([row.get('id', 'N/A'), row.get('Name', 'N/A'), row.get('Age', 'N/A'), row.get('Major', 'N/A')])
        print(table)


def backup_json_files_by_name(input_text):
    # Search for JSON files that match the name
    matching_files = []
    for root, dirs, files in os.walk("/"):  # Provide the starting directory to search from
        for file in files:
            if file.endswith(".json") and file.startswith(input_text):
                matching_files.append(os.path.join(root, file))

    # Back up the matching files to the user's desktop
    desktop_dir = os.path.expanduser("~/Desktop")
    for file_path in matching_files:
        shutil.copy(file_path, desktop_dir)

    # Display a success message
    print("Backup completed successfully!")

def search_and_backup_json():
    search_name = input("Enter the name to search for .json file: ")
    backup_folder = os.path.join(os.path.expanduser("~"), "Desktop", "Backup")
    os.makedirs(backup_folder, exist_ok=True)
    found_files = []

    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".json") and search_name.lower() in file.lower():
                found_files.append(os.path.join(root, file))

    if len(found_files) == 0:
        print("No matching .json files found.")
    else:
        for file_path in found_files:
            backup_path = os.path.join(backup_folder, os.path.basename(file_path))
            shutil.copy2(file_path, backup_path)
            print(f"File '{os.path.basename(file_path)}' backed up to '{backup_path}'.")
