#!/usr/bin/python3
"""Unit tests for models/base.py"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """Test cases for the Base class"""

    def setUp(self):
        """Set up the test environment"""
        Base._Base__nb_objects = 0

    def test_generate_unique_id(self):
        """Test the generation of unique IDs"""

        instance_1 = Base()
        self.assertEqual(instance_1.id, 1)

        instance_2 = Base()
        self.assertEqual(instance_2.id, 2)

        instance_3 = Base(12)
        self.assertEqual(instance_3.id, 12)

        instance_4 = Base(0)
        self.assertEqual(instance_4.id, 0)

        instance_5 = Base(927)
        self.assertEqual(instance_5.id, 927)

        instance_6 = Base(-5)
        self.assertEqual(instance_6.id, -5)

        instance_7 = Base(9)
        self.assertEqual(instance_7.id, 9)

    def test_instance_type(self):
        """Test the instance type"""

        instance_6 = Base()
        self.assertEqual(type(instance_6), Base)
        self.assertTrue(isinstance(instance_6, Base))

    def test_to_json_string_valid_input(self):
        """Test to_json_string method with valid input"""

        dictionary_data = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_string = Base.to_json_string([dictionary_data])

        self.assertTrue(isinstance(dictionary_data, dict))
        self.assertTrue(isinstance(json_string, str))
        self.assertCountEqual(
            json_string,
            '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        )

    def test_to_json_string_empty_input(self):
        """Test to_json_string method with empty input"""

        json_string_empty = Base.to_json_string([])
        self.assertEqual(json_string_empty, "[]")

    def test_to_json_string_none_input(self):
        """Test to_json_string method with None input"""

        json_string_none = Base.to_json_string(None)
        self.assertEqual(json_string_none, "[]")

    def test_to_json_string_incorrect_type(self):
        """Test to_json_string method with incorrect input type"""

        with self.assertRaises(TypeError) as x:
            Base.to_json_string(9)
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))

        with self.assertRaises(TypeError) as x:
            Base.to_json_string("Hello")
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))

        with self.assertRaises(TypeError) as x:
            Base.to_json_string(["Hi", "Here"])
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))

        with self.assertRaises(TypeError) as x:
            Base.to_json_string(7.8)
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))

        with self.assertRaises(TypeError) as x:
            Base.to_json_string([2, 1, 3, 4])
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))

        with self.assertRaises(TypeError) as x:
            Base.to_json_string({1: 'hi', 2: 'there'})
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))

        with self.assertRaises(TypeError) as x:
            Base.to_json_string((9, 0))
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))

        with self.assertRaises(TypeError) as x:
            Base.to_json_string(True)
        self.assertEqual(
            "list_dictionaries must be a list of dictionaries", str(
                x.exception))

    def test_to_json_string_incorrect_number_of_args(self):
        """Test to_json_string method with incorrect number of arguments"""

        error_msg_missing_arg = (
            "to_json_string() missing 1 required positional argument: "
            "'list_dictionaries'"
        )
        with self.assertRaises(TypeError) as x:
            Base.to_json_string()
        self.assertEqual(error_msg_missing_arg, str(x.exception))

        error_msg_extra_arg = (
            "to_json_string() takes 1 positional argument but 2 were given"
        )
        with self.assertRaises(TypeError) as x:
            Base.to_json_string([{1, 2}], [{3, 4}])
        self.assertEqual(error_msg_extra_arg, str(x.exception))

    def test_save_to_file_valid_input(self):
        """Test save_to_file method with valid input"""

        rectangle_1 = Rectangle(10, 7, 2, 8)
        rectangle_2 = Rectangle(2, 4)
        Rectangle.save_to_file([rectangle_1, rectangle_2])

        expected_output = (
            '[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},'
            ' {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]'
        )

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), len(expected_output))

        Rectangle.save_to_file(None)
        expected_output_empty = "[]"

        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), expected_output_empty)

        os.remove("Rectangle.json")
        Rectangle.save_to_file([])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), expected_output_empty)

        square_1 = Square(9, 3, 1, 12)
        square_2 = Square(6, 7)
        Square.save_to_file([square_1, square_2])

        expected_square_output = (
            '[{"id": 12, "size": 9, "x": 3, "y": 1},'
            ' {"id": 3, "size": 6, "x": 7, "y": 0}]'
        )

        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), len(expected_square_output))

        Square.save_to_file(None)

        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), expected_output_empty)

        os.remove("Square.json")
        Square.save_to_file([])

        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), expected_output_empty)

    def test_save_to_file_method_with_error(self):
        """Test save_to_file method with error"""

        with self.assertRaises(AttributeError) as x:
            Base.save_to_file([Base(9), Base(5)])
        self.assertEqual(
            "'Base' object has no attribute 'to_dictionary'", str(x.exception))

        with self.assertRaises(AttributeError) as x:
            Rectangle.save_to_file([3, 4])
        self.assertEqual(
            "'int' object has no attribute 'to_dictionary'", str(x.exception))

        with self.assertRaises(TypeError) as x:
            Rectangle.save_to_file(5)
        self.assertEqual("'int' object is not iterable", str(x.exception))

    def test_save_to_file_with_incorrect_args(self):
        """Test save_to_file with incorrect args"""

        error_msg_missing_arg = (
            "save_to_file() missing 1 required"
            " positional argument: 'list_objs'"
        )

        with self.assertRaises(TypeError) as x:
            Rectangle.save_to_file()
        self.assertEqual(error_msg_missing_arg, str(x.exception))

        error_msg_extra_arg = (
            "save_to_file() takes 2 positional"
            " arguments but 3 were given"
        )

        with self.assertRaises(TypeError) as x:
            Rectangle.save_to_file([Rectangle(9, 4), Rectangle(8, 9)], 98)
        self.assertEqual(error_msg_extra_arg, str(x.exception))

    def test_from_json_string_correct_types(self):
        """Test from_json_string with correct types."""

        input_data = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_input = Rectangle.to_json_string(input_data)
        output_list = Rectangle.from_json_string(json_input)
        expected_result = [
                {'width': 10, 'height': 4, 'id': 89},
                {'width': 1, 'height': 7, 'id': 7}
        ]
        self.assertCountEqual(output_list, expected_result)
        self.assertEqual(type(output_list), list)

        empty_string_output = Rectangle.from_json_string('')
        self.assertEqual(empty_string_output, [])

        none_output = Rectangle.from_json_string(None)
        self.assertEqual(none_output, [])

    def test_from_json_string_incorrect_type(self):
        """Test from_json_string with incorrect type."""

        with self.assertRaises(TypeError) as x:
            output_list = Rectangle.from_json_string([8, 9])
        self.assertEqual("json_string must be a string", str(x.exception))

        with self.assertRaises(TypeError) as x:
            output_list = Rectangle.from_json_string(8)
        self.assertEqual("json_string must be a string", str(x.exception))

        with self.assertRaises(TypeError) as x:
            output_list = Rectangle.from_json_string(9.6)
        self.assertEqual("json_string must be a string", str(x.exception))

        with self.assertRaises(TypeError) as x:
            output_list = Rectangle.from_json_string((4, 5))
        self.assertEqual("json_string must be a string", str(x.exception))

        with self.assertRaises(TypeError) as x:
            output_list = Rectangle.from_json_string({1: 'Hello', 2: 'Hi'})
        self.assertEqual("json_string must be a string", str(x.exception))

    def test_from_json_string_incorrect_args(self):
        """Test from_json_string with incorrect args."""

        missing_arg_error = (
            "from_json_string() missing 1"
            " required positional argument: 'json_string'"
        )
        with self.assertRaises(TypeError) as x:
            Rectangle.from_json_string()
        self.assertEqual(missing_arg_error, str(x.exception))

        extra_arg_error = (
            "from_json_string() takes 1 positional argument"
            " but 2 were given"
        )
        with self.assertRaises(TypeError) as x:
            Rectangle.from_json_string("Hi", 98)
        self.assertEqual(extra_arg_error, str(x.exception))

    def test_create_with_correct_types(self):
        """Test create with correct types."""

        rectangle_instance_1 = Rectangle(3, 5, 1)
        rectangle_dict_1 = rectangle_instance_1.to_dictionary()
        rectangle_instance_2 = Rectangle.create(**rectangle_dict_1)
        self.assertEqual(str(rectangle_instance_1), str(rectangle_instance_2))
        self.assertFalse(rectangle_instance_1 is rectangle_instance_2)
        self.assertFalse(rectangle_instance_1 == rectangle_instance_2)

        square_instance_1 = Square(3, 5)
        square_dict_1 = square_instance_1.to_dictionary()
        square_instance_2 = Square.create(**square_dict_1)
        self.assertEqual(str(square_instance_1), str(square_instance_2))
        self.assertFalse(square_instance_1 is square_instance_2)
        self.assertFalse(square_instance_1 == square_instance_2)

    def test_create_with_incorrect_types(self):
        """Test create with incorrect types."""

        with self.assertRaises(TypeError) as x:
            arg_value = "Hello"
            Rectangle.create(arg_value)
        self.assertEqual(
            "create() takes 1 positional argument but 2 were given", str(
                x.exception))

    def test_load_from_file_with_correct_types(self):
        """Test load_from_file with correct types."""

        rectangle_instance_1 = Rectangle(10, 7, 2, 8)
        rectangle_instance_2 = Rectangle(2, 4)
        list_rectangles_input = [rectangle_instance_1, rectangle_instance_2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        for input_instance, output_instance in zip(
                list_rectangles_input, list_rectangles_output):
            self.assertEqual(str(input_instance), str(output_instance))

        square_instance_1 = Square(10, 2)
        square_instance_2 = Square(9)
        list_squares_input = [square_instance_1, square_instance_2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        for input_instance, output_instance in zip(
                list_squares_input, list_squares_output):
            self.assertEqual(str(input_instance), str(output_instance))

    def test_load_from_file_without_files(self):
        """Test load_from_file without files."""

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output, [])
        list_squares_output = Square.load_from_file()
        self.assertEqual(list_squares_output, [])

    def test_load_from_file_with_incorrect_args(self):
        """Test load_from_file with incorrect args."""

        error_message = (
                "load_from_file() takes 1 positional argument "
                "but 2 were given"
        )
        with self.assertRaises(TypeError) as x:
            list_rectangles_output = Rectangle.load_from_file("Hello")
        self.assertEqual(error_message, str(x.exception))

    def test_save_to_file_csv_with_correct_types(self):
        """Test save_to_file_csv with correct types."""

        rectangle_instance_1 = Rectangle(10, 7, 2, 8)
        rectangle_instance_2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([
            rectangle_instance_1,
            rectangle_instance_2
        ])
        expected_result = "id,width,height,x,y\n1,10,7,2,8\n2,2,4,0,0\n"
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(len(file.read()), len(expected_result))

        square_instance_1 = Square(9, 3, 1, 12)
        square_instance_2 = Square(6, 7)
        Square.save_to_file_csv([square_instance_1, square_instance_2])
        expected_result = "id,size,x,y\n12,9,3,1\n3,6,7,0\n"
        with open("Square.csv", "r") as file:
            self.assertEqual(len(file.read()), len(expected_result))

    def test_save_to_file_csv_with_errors(self):
        """Test save_to_file_csv with errors."""

        with self.assertRaises(AttributeError) as exception_context:
            Base.save_to_file_csv([Base(9), Base(5)])
        self.assertEqual(
            "'Base' object has no attribute 'to_dictionary'", str(
                exception_context.exception))

        with self.assertRaises(TypeError) as exception_context:
            Rectangle.save_to_file_csv([3, 4])
        self.assertEqual(
            "list_objs must be a list of instance", str(
                exception_context.exception))

        with self.assertRaises(TypeError) as exception_context:
            Rectangle.save_to_file_csv(5.9)
        self.assertEqual(
            "list_objs must be a list of instance", str(
                exception_context.exception))

    def test_load_from_file_csv_with_correct_types(self):
        """Test load_from_file_csv with correct types."""

        rectangle_instance_1 = Rectangle(10, 7, 2, 8)
        rectangle_instance_2 = Rectangle(2, 4)
        list_rectangles_input = [rectangle_instance_1, rectangle_instance_2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        for input_instance, output_instance in zip(
                list_rectangles_input, list_rectangles_output):
            self.assertEqual(str(input_instance), str(output_instance))

        square_instance_1 = Square(10, 2)
        square_instance_2 = Square(9)
        list_squares_input = [square_instance_1, square_instance_2]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        for input_instance, output_instance in zip(
                list_squares_input, list_squares_output):
            self.assertEqual(str(input_instance), str(output_instance))

    def test_load_from_file_csv_with_missing_files(self):
        """Test class method load_from_file_csv with missing files."""

        os.remove("Rectangle.csv")
        os.remove("Square.csv")
        os.remove("Base.csv")
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(list_rectangles_output, [])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(list_squares_output, [])

    def test_load_from_file_csv_with_incorrect_args(self):
        """Test load_from_file_csv with incorrect args."""

        error_message = (
                "load_from_file_csv() takes 1 positional argument "
                "but 2 were given"
        )
        with self.assertRaises(TypeError) as exception_context:
            list_rectangles_output = Rectangle.load_from_file_csv("Hello")
        self.assertEqual(error_message, str(exception_context.exception))
