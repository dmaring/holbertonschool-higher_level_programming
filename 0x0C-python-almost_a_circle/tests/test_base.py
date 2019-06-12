#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
"""
Module for unittests for the Base class
"""


class TestBaseClassCreation(unittest.TestCase):
    """Test class for Base class instantiation tests"""

    def test_id_positive(self):
        bo = Base(23)
        self.assertEqual(bo.id, 23)
        bo = Base(34)
        self.assertEqual(bo.id, 34)

    def test_id_negative(self):
        bo = Base(-4)
        self.assertEqual(bo.id, -4)
        bo = Base(-10)
        self.assertEqual(bo.id, -10)

    def test_id_none(self):
        bo = Base()
        self.assertEqual(bo.id, 1)
        bo = Base(None)
        self.assertEqual(bo.id, 2)

    def test_id_inf(self):
        bo = Base(float('inf'))
        #TODO what should this do

    def test_id_neg_inf(self):
        bo = Base(float('-inf'))
        #TODO what should this do

    def test_id_inf(self):
        bo = Base(float('-inf'))
        #TODO what should this do

    def test_id_inf(self):
        bo = Base(float('NaN'))
        #TODO what should this do


class TestBaseToJsonStringMethod(unittest.TestCase):
    """Test class for Base class to_json_string method"""

    #test passing None
    def test_pass_none(self):
        ret = Base.to_json_string(None)
        self.assertEqual(ret, [])

    def test_pass_empty_list(self):
        ret = Base.to_json_string([])
        self.assertEqual(ret, [])

    def test_pass_one(self):
        Base.reset_id()
        r1 = Rectangle(3, 4)
        rd = r1.to_dictionary()
        str_ = '{"height": 4, "id": 1, "width": 3, "x": 0, "y": 0}'
        self.assertEqual(Base.to_json_string(rd), str_)

    def test_pass_list_dicts(self):
        Base.reset_id()
        r1 = Rectangle(3, 4, 5, 6)
        rd1 = r1.to_dictionary()
        r2 = Rectangle(8, 9, 10, 11)
        rd2 = r2.to_dictionary()
        ret = Base.to_json_string([rd1, rd2])
        str_ = '[{"height": 4, "id": 1, "width": 3, "x": 5, "y": 6}, {"height": 9, "id": 2, "width": 8, "x": 10, "y": 11}]'
        self.assertEqual(ret, str_)

    def test_pass_list_dicts_type(self):
        Base.reset_id()
        r1 = Rectangle(3, 4, 5, 6)
        rd1 = r1.to_dictionary()
        r2 = Rectangle(8, 9, 10, 11)
        rd2 = r2.to_dictionary()
        ret = Base.to_json_string([rd1, rd2])
        self.assertIsInstance(ret, str)



class TestBaseToSaveToFileMethod(unittest.TestCase):
    """Test class for Base class method save_to_file"""

    def test_correct_file_save_rectangle(self):
        Base.reset_id()
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Base.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            file_read = file.read()
        cmp_str = '[{"height": 7, "id": 1, "width": 10, "x": 2, "y": 8}, {"height": 4, "id": 2, "width": 2, "x": 0, "y": 0}]'
        self.assertEqual(file_read, cmp_str)

    def test_correct_file_save_square(self):
        Base.reset_id()
        s1 = Square(10, 4, 2)
        s2 = Square(2, 3, 2)
        Base.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            file_read = file.read()
        cmp_str = '[{"height": 10, "id": 1, "width": 10, "x": 4, "y": 2}, {"height": 2, "id": 2, "width": 2, "x": 3, "y": 2}]'
        self.assertEqual(file_read, cmp_str)

    def test_write_empty_file(self):
        Base.reset_id()
        Base.save_to_file(None)
        with open("None.json", "r") as file:
            file_read = file.read()
        self.assertEqual(file_read, '"[]"')

class TestBaseFromJsonStringMethod(unittest.TestCase):
    """Test class for Base class method json_to_string_method"""
    def setUp(self):
        Base.reset_id()
        self.single_item = '[{"height": 4, "id": 1, "width": 3, "x": 0, "y": 0}]'
        self.mult_item = '[{"height": 4, "id": 1, "width": 3, "x": 0, "y": 0}, {"height": 6, "id": 2, "width": 5, "x": 0, "y": 0}]'

    #test passing empty list
    def test_passing_empyt_list(self):
        self.assertEqual(Base.from_json_string('[]'), [])

    #test passing None instead of list
    def test_passing_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    #test that object returned is correct with multiple dictionaries
    def test_pass_multiple(self):
        ret_val = Base.from_json_string(self.mult_item)
        cor_val = [{'id': 1, 'y': 0, 'height': 4, 'x': 0, 'width': 3}, {'id': 2, 'y': 0, 'height': 6, 'x': 0, 'width': 5}]
        self.assertEqual(ret_val, cor_val)

    #test that object returned is correct with 1 dictionary
    def test_pass_single(self):
        ret_val = Base.from_json_string(self.single_item)
        cor_val = [{'id': 1, 'y': 0, 'height': 4, 'x': 0, 'width': 3}]
        self.assertEqual(ret_val, cor_val)

    #test object returned is list with 1 dictionary passed
    def test_pass_single_type_check(self):
        ret_val = Base.from_json_string(self.single_item)
        self.assertIsInstance(ret_val, list)

    #test object returned is a list with multiple dictionaries
    def test_pass_mult_type_check(self):
        ret_val = Base.from_json_string(self.mult_item)
        self.assertIsInstance(ret_val, list)

class TestBaseDictionaryToInstance(unittest.TestCase):
    """Test class for Base class method dictionary_to_instance"""
    def setUp(self):
        Base.reset_id()
        self.r1 = Rectangle(3, 5, 1)
        self.r1_dictionary = self.r1.to_dictionary()
        self.r2 = Rectangle.create(**self.r1_dictionary)

        self.s1 = Square(3, 5, 1)
        self.s1_dictionary = self.s1.to_dictionary()
        self.s2 = Square.create(**self.s1_dictionary)

    def test_create_rectangle(self):
        self.assertEqual(str(self.r1), str(self.r2))

    def test_create_square(self):
        self.assertEqual(str(self.s1), str(self.s2))

    def test_instance_rectangle(self):
        self.assertIsInstance(self.r1, Rectangle)

    def test_instance_square(self):
        self.assertIsInstance(self.s1, Square)

    def test_not_is_rectangle(self):
        self.assertIsNot(self.r1, self.r2)

    def test_not_is_square(self):
        self.assertIsNot(self.s1, self.s2)

    def test_is_not_equal_rectangle(self):
        self.assertNotEqual(self.r1, self.r2)

    def test_is_not_equal_square(self):
        self.assertNotEqual(self.s1, self.s2)

if __name__ == '__main__':
    unittest.main()
