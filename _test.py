import unittest

from main import

class TestCreateRecord(unittest.TestCase):
    def test_my_function(self):
        #self.assertEqual(my_function(2), 4)
        #self.assertEqual(my_function(0), 0)
        #self.assertEqual(my_function(-1), -2)


class TestGetFields(unittest.TestCase):
    def test_my_function(self):
        #self.assertEqual(my_function(2), 4)
        #self.assertEqual(my_function(0), 0)
        #self.assertEqual(my_function(-1), -2)


class TestReadRecord(unittest.TestCase):
    def test_my_function(self):
        #self.assertEqual(my_function(2), 4)
        #self.assertEqual(my_function(0), 0)
        #self.assertEqual(my_function(-1), -2)

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

class TestDeleteRecord(unittest.TestCase):
    def test_my_function(self):
        #self.assertEqual(my_function(2), 4)
        #self.assertEqual(my_function(0), 0)
        #self.assertEqual(my_function(-1), -2)

class TestListRecords(unittest.TestCase):
    def test_my_function(self):
        #self.assertEqual(my_function(2), 4)
        #self.assertEqual(my_function(0), 0)
        #self.assertEqual(my_function(-1), -2)

import unittest
import json
from io import StringIO
from main import create_record, update_record, delete_record, display_table

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
        

if __name__ == '__main__':
    unittest.main()