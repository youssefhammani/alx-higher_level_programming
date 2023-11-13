#!/usr/bin/python3
"""Unit tests for the Rectangle class"""

import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def setUp(self):
        """Set up before each test"""
        Base._Base__nb_objects = 0

    def test_constructor_id(self):
        """Test constructor and id generation"""
        rectangle1 = Rectangle(1, 2)
        self.assertEqual(rectangle1.id, 1)

        rectangle2 = Rectangle(2, 3)
        self.assertEqual(rectangle2.id, 2)

        rectangle3 = Rectangle(3, 4)
        self.assertEqual(rectangle3.id, 3)

        rectangle4 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rectangle4.id, 12)

        rectangle5 = Rectangle(10, 2, 4, 5, 34)
        self.assertEqual(rectangle5.id, 34)

        rectangle6 = Rectangle(10, 2, 4, 5, -5)
        self.assertEqual(rectangle6.id, -5)

        rectangle7 = Rectangle(10, 2, 4, 5, 9)
        self.assertEqual(rectangle7.id, 9)

    def test_constructor_attributes(self):
        """Test constructor attributes"""
        rectangle1 = Rectangle(10, 2)
        self.assertEqual(rectangle1.width, 10)
        self.assertEqual(rectangle1.height, 2)
        self.assertEqual(rectangle1.x, 0)
        self.assertEqual(rectangle1.y, 0)

        rectangle2 = Rectangle(10, 2, 4, 5, 24)
        self.assertEqual(rectangle2.width, 10)
        self.assertEqual(rectangle2.height, 2)
        self.assertEqual(rectangle2.x, 4)
        self.assertEqual(rectangle2.y, 5)

    def test_constructor_missing_args(self):
        """Test constructor with missing arguments"""
        with self.assertRaises(TypeError) as context:
            rectangle = Rectangle(5)
        self.assertEqual(
            str(context.exception),
            "__init__() missing 1 required positional argument: 'height'"
        )

        with self.assertRaises(TypeError) as context:
            rectangle = Rectangle()
        self.assertEqual(
            str(context.exception),
            "__init__() missing 2 required positional "
            "arguments: 'width' and 'height'"
        )

    def test_inheritance(self):
        """Test inheritance"""
        rectangle = Rectangle(9, 3)
        self.assertIsInstance(rectangle, Base)
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))

    def test_invalid_attributes(self):
        """Test invalid attributes"""
        with self.assertRaises(TypeError) as context:
            rectangle = Rectangle("Hello", 2)
        self.assertEqual(
            str(context.exception),
            "width must be an integer"
        )

        with self.assertRaises(TypeError) as context:
            rectangle = Rectangle(2, "World")
        self.assertEqual(
            str(context.exception),
            "height must be an integer"
        )

        with self.assertRaises(TypeError) as context:
            rectangle = Rectangle(1, 2, "Foo", 3)
        self.assertEqual(
            str(context.exception),
            "x must be an integer"
        )

        with self.assertRaises(TypeError) as context:
            rectangle = Rectangle(1, 2, 2, "Bar")
        self.assertEqual(
            str(context.exception),
            "y must be an integer"
        )

        with self.assertRaises(ValueError) as context:
            rectangle = Rectangle(0, 2)
        self.assertEqual(
            str(context.exception),
            "width must be > 0"
        )

        with self.assertRaises(ValueError) as context:
            rectangle = Rectangle(2, 0)
        self.assertEqual(
            str(context.exception),
            "height must be > 0"
        )

        with self.assertRaises(ValueError) as context:
            rectangle = Rectangle(2, -3)
        self.assertEqual(
            str(context.exception),
            "height must be > 0"
        )

        with self.assertRaises(ValueError) as context:
            rectangle = Rectangle(2, 5, -5, 6)
        self.assertEqual(
            str(context.exception),
            "x must be >= 0"
        )

        with self.assertRaises(ValueError) as context:
            rectangle = Rectangle(2, 8, 9, -65)
        self.assertEqual(
            str(context.exception),
            "y must be >= 0"
        )

    def test_area_method(self):
        """Test the area method"""
        rectangle1 = Rectangle(3, 2)
        self.assertEqual(rectangle1.area(), 6)

        rectangle2 = Rectangle(75, 2)
        self.assertEqual(rectangle2.area(), 150)

        rectangle3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(rectangle3.area(), 56)

    def test_area_method_with_invalid_args(self):
        """Test area method with incorrect arguments"""
        with self.assertRaises(TypeError) as context:
            rectangle1 = Rectangle(3, 2)
            rectangle1.area("Hello")
        self.assertEqual(
            str(context.exception),
            "area() takes 1 positional argument but 2 were given"
        )

    def test_display_method(self):
        """Test the display method"""
        f = io.StringIO()
        rectangle1 = Rectangle(4, 5)
        with contextlib.redirect_stdout(f):
            rectangle1.display()
        s = f.getvalue()
        expected_output = "####\n####\n####\n####\n####\n"
        self.assertEqual(s, expected_output)

    def test_display_method_with_invalid_args(self):
        """Test display method with incorrect arguments"""
        with self.assertRaises(TypeError) as context:
            rectangle1 = Rectangle(9, 6)
            rectangle1.display(9)
        self.assertEqual(
            str(context.exception),
            "display() takes 1 positional argument but 2 were given"
        )

    def test_str_representation(self):
        """Test the __str__ representation"""
        f = io.StringIO()
        rectangle1 = Rectangle(4, 6, 2, 1, 12)
        with contextlib.redirect_stdout(f):
            print(rectangle1)
        s = f.getvalue()
        expected_output = "[Rectangle] (12) 2/1 - 4/6\n"
        self.assertEqual(s, expected_output)

    def test_display_method_with_coordinates(self):
        """Test display method with x and y coordinates"""
        f = io.StringIO()
        rectangle1 = Rectangle(2, 3, 2, 2)
        with contextlib.redirect_stdout(f):
            rectangle1.display()
        s = f.getvalue()
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(s, expected_output)

    def test_update_method(self):
        """Test the update method"""
        rectangle1 = Rectangle(10, 10, 10, 10)
        rectangle1.update(89)
        self.assertEqual(rectangle1.id, 89)

        rectangle1.update(89, 2)
        self.assertEqual(rectangle1.width, 2)

        rectangle1.update(89, 2, 3)
        self.assertEqual(rectangle1.height, 3)

        rectangle1.update(89, 2, 3, 4)
        self.assertEqual(rectangle1.x, 4)

        rectangle1.update(89, 2, 3, 4, 5)
        self.assertEqual(rectangle1.y, 5)

        rectangle1.update()
        self.assertEqual(str(rectangle1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_method_with_incorrect_types(self):
        """Test for update method with incorrect types."""
        rectangle = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as context:
            rectangle.update("hi")
        self.assertEqual(str(context.exception), "id must be an integer")

        with self.assertRaises(TypeError) as context:
            rectangle.update(65, 89, "hi")
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_update_method_with_kwargs(self):
        """Test for update with kwargs."""
        rectangle = Rectangle(10, 10, 10, 10)
        rectangle.update(height=1)
        self.assertEqual(rectangle.height, 1)

        rectangle.update(x=1, height=2, y=3, width=4)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.height, 2)

    def test_update_method_with_incorrect_types_in_kwargs(self):
        """Test for update with incorrect types in kwargs."""
        rectangle = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as context:
            rectangle.update(id='hi')
        self.assertEqual(str(context.exception), "id must be an integer")

        with self.assertRaises(TypeError) as context:
            rectangle.update(height=65, x=2, width="hi")
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_to_dictionary_method(self):
        """Test for to_dictionary method."""
        rectangle1 = Rectangle(10, 2, 1, 9)
        rectangle1_dictionary = rectangle1.to_dictionary()
        expected_dictionary = {
                'x': 1,
                'y': 9,
                'id': 1,
                'height': 2,
                'width': 10
        }
        self.assertEqual(len(rectangle1_dictionary), len(expected_dictionary))
        self.assertEqual(type(rectangle1_dictionary), dict)

        rectangle2 = Rectangle(1, 1)
        rectangle2.update(**rectangle1_dictionary)
        rectangle2_dictionary = rectangle2.to_dictionary()
        self.assertEqual(
                len(rectangle1_dictionary),
                len(rectangle2_dictionary)
        )
        self.assertEqual(type(rectangle2_dictionary), dict)
        self.assertFalse(rectangle1 == rectangle2)

    def test_to_dictionary_method_with_incorrect_args(self):
        """Test for to_dictionary with incorrect args."""
        error_message = (
                "to_dictionary() takes 1 positional argument "
                "but 2 were given"
        )
        with self.assertRaises(TypeError) as context:
            rectangle1 = Rectangle(10, 2, 1, 9)
            rectangle1.to_dictionary("Hi")
        self.assertEqual(str(context.exception), error_message)


if __name__ == '__main__':
    unittest.main()
