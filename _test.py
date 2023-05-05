import unittest
import json
import os
from main import 

from main import create_record
from main import get_fields
from main import read_record
from main import update_record
from main import delete_record
from main import list_records
from io import StringIO
from main import create_record, update_record, delete_record, display_table

class TestCreateRecord(unittest.TestCase):
    def test_create_record(self):
        pass
        

class TestGetFields(unittest.TestCase):
    def test_get_fields(self):
        # write your test cases for get_fields function here
        result = get_fields()
        self.assertGreater(len(result), 0)

class TestReadRecord(unittest.TestCase):
    def test_read_record(self):
        # write your test cases for read_record function here
        pass

class TestUpdateRecord(unittest.TestCase):
    def setUp(self):
        self.db_file = 'test_db.json'
        with open(self.db_file, 'w') as file:
            json.dump([
                {'id': 1, 'name': 'John', 'age': 30},
                {'id': 2, 'name': 'Mary', 'age': 25},
                {'id': 3, 'name': 'Tom', 'age': 40}
            ], file)
        
    def test_update_existing_record(self):
        id = 2
        new_name = 'Alex'
        new_age = 35
        expected_records = [
            {'id': 1, 'name': 'John', 'age': 30},
            {'id': 2, 'name': new_name, 'age': new_age},
            {'id': 3, 'name': 'Tom', 'age': 40}
        ]
        # Set up input stream with desired inputs
        inputs = [new_name, new_age]
        input_stream = StringIO('\n'.join(map(str, inputs)))
        # Call update_record with the input stream
        with open(self.db_file, 'r+') as file:
            actual_result = update_record(id, input_stream=input_stream, db_file=file)
            file.seek(0)
            actual_records = json.load(file)
        self.assertTrue(actual_result)
        self.assertEqual(expected_records, actual_records)
    def test_update_record(self):
        # write your test cases for update_record function here
        pass

class TestDeleteRecord(unittest.TestCase):
    def test_delete_record(self):
        # write your test cases for delete_record function here
        
        # need to create a temp json file to test the function
        with open("deletedMe.json" , "w") as tempFile:
            tempFile.write('[{"id": 1, "name": "Steve", "age": 21}]')

        result = delete_record(1)
        self.assertTrue(result)

class TestListRecords(unittest.TestCase):
    
    def test_list_records(self):
        DB_FILE_NAME = 'data.json' #creates a dummy test file

class TestDisplayTable(unittest.TestCase):
    def setUp(self):
        self.db_file = 'test_db.json'
        with open(self.db_file, 'w') as file:
            json.dump([
                {'id': '1', 'name': 'John', 'age': 30, 'major': 'Computer Science'},
                {'id': '2', 'name': 'Mary', 'age': 25, 'major': 'Electrical Engineering'},
                {'id': '3', 'name': 'Tom', 'age': 40, 'major': 'Mathematics'}
            ], file)
        
    def test_display_table(self):
        # Set up expected output
        expected_output = '+------+-----+------------------------+\n'
        expected_output += '| Name | Age |         Major          |\n'
        expected_output += '+------+-----+------------------------+\n'
        expected_output += '| John |  30 |    Computer Science    |\n'
        expected_output += '| Mary |  25 | Electrical Engineering |\n'
        expected_output += '| Tom  |  40 |       Mathematics      |\n'
        expected_output += '+------+-----+------------------------+'
        
        # Capture output of display_table function
        captured_output = StringIO()
        display_table(self.db_file, output_stream=captured_output)
        actual_output = captured_output.getvalue().strip()

        # Assert that the output matches the expected output
        self.assertEqual(expected_output, actual_output)

        
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