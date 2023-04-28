import unittest
import json
import os


from main import create_record
from main import get_fields
from main import read_record
from main import update_record
from main import delete_record
from main import list_records

class TestCreateRecord(unittest.TestCase):
    def test_create_record(self):
        
        pass

class TestGetFields(unittest.TestCase):
    def test_get_fields(self):
        # write your test cases for get_fields function here
        pass

class TestReadRecord(unittest.TestCase):
    def test_read_record(self):
        # write your test cases for read_record function here
        pass

class TestUpdateRecord(unittest.TestCase):
    def test_update_record(self):
        # write your test cases for update_record function here
        pass

class TestDeleteRecord(unittest.TestCase):
    def test_delete_record(self):
        # write your test cases for delete_record function here
        pass

class TestListRecords(unittest.TestCase):
    
    def test_list_records(self):
        DB_FILE_NAME = 'data.json' #creates a dummy test file

        data = { #defines the data set to put into the dummy test file
            "Name" : "Brandon",
            'Age' : 21,
            'Major' : 'CHEN'    
                }
        
        #expectedResult = json.dumps(data)
        #ideally, #50 would be used to save the expected result to compare for later
        #but I am running into issues with quotation marks

        with open(DB_FILE_NAME, 'w') as file: #opening with 'w' ACTUALLY creates the test file
            json.dump(data, file) #dumps data set into file

        with open(DB_FILE_NAME, 'r') as file:
            expectedResult = json.load(file) #reads data set immediately after to save expectedResult

        self.assertEqual(list_records(), expectedResult) #checks

#-------CREDIT TO CHATGPT for explaining the concept of removing files to Brandon Nguyen------------------------------
        if 'file' in locals() or 'file' in globals():   #checks to see if file is open in memory
            file.close()
        
        os.remove(DB_FILE_NAME) #removes it since unit test is over.


if __name__ == '__main__':
    unittest.main()