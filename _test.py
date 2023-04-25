import unittest
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
        
        # need to create a temp json file to test the function
        with open("deletedMe.json" , "w") as tempFile:
            tempFile.write('[{"id": 1, "name": "Steve", "age": 21}]')

        result = delete_record(1)
        self.assertTrue(result)

class TestListRecords(unittest.TestCase):
    def test_list_records(self):
        # write your test cases for list_records function here
        pass


if __name__ == '__main__':
    unittest.main()